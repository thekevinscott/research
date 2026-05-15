#!/usr/bin/env node

const { spawn } = require("node:child_process");
const { createInterface } = require("node:readline");
const http = require("node:http");
const { existsSync } = require("node:fs");

const PORT = parseInt(process.env.CHANNEL_PORT || "8788");
const AUTH_TOKEN = process.env.CHANNEL_AUTH_TOKEN || "";
const WORKDIR = process.env.AGENT_WORKDIR || "/home/agent/work";
const effectiveWorkdir = existsSync(WORKDIR) ? WORKDIR : "/home/agent";

const listeners = new Set();

function broadcast(event, data) {
  const payload = JSON.stringify({ event, data, ts: Date.now() });
  const chunk = `data: ${payload}\n\n`;
  for (const res of listeners) {
    res.write(chunk);
  }
}

console.error(`[channel] spawning claude in ${effectiveWorkdir}`);

const claudeProc = spawn(
  "claude",
  [
    "-p",
    "--input-format", "stream-json",
    "--output-format", "stream-json",
    "--verbose",
    "--dangerously-skip-permissions",
  ],
  {
    cwd: effectiveWorkdir,
    stdio: ["pipe", "pipe", "pipe"],
    env: {
      ...process.env,
      CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1",
    },
  }
);

console.error(`[channel] Claude spawned, pid: ${claudeProc.pid}`);

let claudeReady = false;
let sessionId = "";

const rl = createInterface({ input: claudeProc.stdout });

rl.on("line", (line) => {
  if (!line.trim()) return;
  console.error(`[channel] stdout line (${line.length} chars)`);
  try {
    const msg = JSON.parse(line);
    handleClaudeMessage(msg);
  } catch {
    console.error("[channel] unparseable:", line.slice(0, 200));
  }
});

rl.on("close", () => {
  console.error("[channel] stdout closed");
  broadcast("system", { type: "claude_exited" });
});

function handleClaudeMessage(msg) {
  console.error(`[channel] msg type=${msg.type} subtype=${msg.subtype || ""}`);

  if (msg.type === "system" && msg.subtype === "init") {
    claudeReady = true;
    sessionId = msg.session_id || "";
    console.error("[channel] Claude ready, session:", sessionId);
    broadcast("system", { type: "ready", session_id: sessionId });
    return;
  }

  if (msg.type === "assistant") {
    const textBlocks = (msg.message?.content || []).filter((b) => b.type === "text");
    if (textBlocks.length > 0) {
      const text = textBlocks.map((b) => b.text).join("");
      console.error(`[channel] reply: ${text.slice(0, 100)}`);
      broadcast("reply", { text, message_id: msg.message?.id });
    }
    return;
  }

  if (msg.type === "stream_event") {
    const event = msg.event;
    if (event?.type === "content_block_delta" && event?.delta?.type === "text_delta") {
      broadcast("stream", { text: event.delta.text });
    }
    return;
  }

  if (msg.type === "result") {
    console.error(`[channel] result: cost=$${msg.total_cost_usd}`);
    broadcast("result", {
      text: msg.result,
      session_id: msg.session_id,
      cost: msg.total_cost_usd,
    });
    return;
  }
}

claudeProc.stderr.on("data", (chunk) => {
  console.error("[claude-stderr]", chunk.toString().trimEnd());
});

claudeProc.on("error", (err) => {
  console.error(`[channel] spawn error: ${err.message}`);
});

claudeProc.on("exit", (code, signal) => {
  console.error(`[channel] Claude exited: code=${code} signal=${signal}`);
  broadcast("system", { type: "claude_exited", code, signal });
});

let nextId = 1;

function sendToClaudeStdin(message) {
  const json = JSON.stringify({
    type: "user",
    message: {
      role: "user",
      content: message,
    },
  });
  const data = json + "\n";
  const ok = claudeProc.stdin.write(data);
  console.error(`[channel] stdin.write(${data.length} bytes) returned: ${ok}`);
}

function checkAuth(req) {
  if (!AUTH_TOKEN) return true;
  const auth = req.headers["authorization"];
  return auth === `Bearer ${AUTH_TOKEN}`;
}

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Authorization, Content-Type",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
};

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);

  if (req.method === "OPTIONS") {
    res.writeHead(204, corsHeaders);
    res.end();
    return;
  }

  if (!checkAuth(req)) {
    res.writeHead(401, { ...corsHeaders, "Content-Type": "text/plain" });
    res.end("unauthorized");
    return;
  }

  if (req.method === "GET" && url.pathname === "/events") {
    res.writeHead(200, {
      ...corsHeaders,
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    });
    res.write(": connected\n\n");
    listeners.add(res);
    req.on("close", () => listeners.delete(res));
    return;
  }

  if (req.method === "GET" && url.pathname === "/health") {
    const body = JSON.stringify({
      status: "ok",
      name: "blunderdome",
      claude_ready: claudeReady,
      claude_pid: claudeProc.pid,
      session_id: sessionId,
    });
    res.writeHead(200, { ...corsHeaders, "Content-Type": "application/json" });
    res.end(body);
    return;
  }

  if (req.method === "POST" && url.pathname === "/message") {
    let body = "";
    req.on("data", (chunk) => { body += chunk; });
    req.on("end", () => {
      const chat_id = String(nextId++);
      console.error(`[channel] POST /message: "${body.slice(0, 100)}" chat_id=${chat_id}`);
      sendToClaudeStdin(body);
      broadcast("message_received", { chat_id, content: body });
      res.writeHead(200, { ...corsHeaders, "Content-Type": "application/json" });
      res.end(JSON.stringify({ status: "sent", chat_id }));
    });
    return;
  }

  res.writeHead(404, { ...corsHeaders, "Content-Type": "text/plain" });
  res.end("not found");
});

server.listen(PORT, "0.0.0.0", () => {
  console.error(`[blunderdome-channel] listening on port ${PORT}`);
});
