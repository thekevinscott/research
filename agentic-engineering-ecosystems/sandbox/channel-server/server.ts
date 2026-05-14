#!/usr/bin/env bun
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const PORT = parseInt(process.env.CHANNEL_PORT || "8788");
const AUTH_TOKEN = process.env.CHANNEL_AUTH_TOKEN || "";

const listeners = new Set<(chunk: string) => void>();

function broadcast(event: string, data: unknown) {
  const payload = JSON.stringify({ event, data, ts: Date.now() });
  const chunk = `data: ${payload}\n\n`;
  for (const emit of listeners) emit(chunk);
}

const mcp = new Server(
  { name: "blunderdome", version: "0.0.1" },
  {
    capabilities: {
      experimental: {
        "claude/channel": {},
        "claude/channel/permission": {},
      },
      tools: {},
    },
    instructions:
      'Messages from the user arrive as <channel source="blunderdome" chat_id="...">. ' +
      "Always reply using the reply tool, passing back the chat_id from the inbound tag. " +
      "Keep replies concise and helpful. Format with markdown when useful.",
  }
);

mcp.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "reply",
      description: "Send a message back to the user through the Blunderdome web UI",
      inputSchema: {
        type: "object" as const,
        properties: {
          chat_id: {
            type: "string",
            description: "The conversation ID from the inbound message",
          },
          text: {
            type: "string",
            description: "The message to send back (markdown supported)",
          },
        },
        required: ["chat_id", "text"],
      },
    },
  ],
}));

mcp.setRequestHandler(CallToolRequestSchema, async (req) => {
  if (req.params.name === "reply") {
    const { chat_id, text } = req.params.arguments as {
      chat_id: string;
      text: string;
    };
    broadcast("reply", { chat_id, text });
    return { content: [{ type: "text" as const, text: "sent" }] };
  }
  throw new Error(`unknown tool: ${req.params.name}`);
});

// Permission relay handler
import { z } from "zod";

const PermissionRequestSchema = z.object({
  method: z.literal("notifications/claude/channel/permission_request"),
  params: z.object({
    request_id: z.string(),
    tool_name: z.string(),
    description: z.string(),
    input_preview: z.string(),
  }),
});

mcp.setNotificationHandler(PermissionRequestSchema, async ({ params }) => {
  broadcast("permission_request", {
    request_id: params.request_id,
    tool_name: params.tool_name,
    description: params.description,
    input_preview: params.input_preview,
  });
});

await mcp.connect(new StdioServerTransport());

function checkAuth(req: Request): boolean {
  if (!AUTH_TOKEN) return true;
  const header = req.headers.get("Authorization");
  return header === `Bearer ${AUTH_TOKEN}`;
}

const PERMISSION_REPLY_RE = /^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i;
let nextId = 1;

Bun.serve({
  port: PORT,
  hostname: "0.0.0.0",
  idleTimeout: 0,
  async fetch(req) {
    const url = new URL(req.url);

    // CORS headers for browser access
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "Authorization, Content-Type",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    };

    if (req.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders });
    }

    if (!checkAuth(req)) {
      return new Response("unauthorized", { status: 401, headers: corsHeaders });
    }

    // SSE stream for outbound events (replies, permission prompts)
    if (req.method === "GET" && url.pathname === "/events") {
      const stream = new ReadableStream({
        start(ctrl) {
          const encoder = new TextEncoder();
          const emit = (chunk: string) => ctrl.enqueue(encoder.encode(chunk));
          emit(": connected\n\n");
          listeners.add(emit);
          req.signal.addEventListener("abort", () => listeners.delete(emit));
        },
      });
      return new Response(stream, {
        headers: {
          ...corsHeaders,
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          Connection: "keep-alive",
        },
      });
    }

    // Health check
    if (req.method === "GET" && url.pathname === "/health") {
      return new Response(JSON.stringify({ status: "ok", name: "blunderdome" }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }

    // Inbound message or permission verdict
    if (req.method === "POST" && url.pathname === "/message") {
      const body = await req.text();

      // Check for permission verdict
      const m = PERMISSION_REPLY_RE.exec(body);
      if (m) {
        await mcp.notification({
          method: "notifications/claude/channel/permission" as any,
          params: {
            request_id: m[2].toLowerCase(),
            behavior: m[1].toLowerCase().startsWith("y") ? "allow" : "deny",
          },
        });
        return new Response(
          JSON.stringify({ status: "verdict_recorded" }),
          { headers: { ...corsHeaders, "Content-Type": "application/json" } }
        );
      }

      // Normal message: forward to Claude
      const chat_id = String(nextId++);
      await mcp.notification({
        method: "notifications/claude/channel",
        params: {
          content: body,
          meta: { chat_id },
        },
      });

      broadcast("message_received", { chat_id, content: body });

      return new Response(
        JSON.stringify({ status: "sent", chat_id }),
        { headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    return new Response("not found", { status: 404, headers: corsHeaders });
  },
});

console.error(`[blunderdome-channel] listening on port ${PORT}`);
