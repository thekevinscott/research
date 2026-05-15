#!/usr/bin/env node

const { execSync } = require("node:child_process");
const { writeFileSync, unlinkSync } = require("node:fs");
const { randomUUID } = require("node:crypto");
const http = require("node:http");

const PORT = parseInt(process.env.CHANNEL_PORT || "8788");
const AUTH_TOKEN = process.env.CHANNEL_AUTH_TOKEN || "";
const TMUX_SESSION = "claude";

const listeners = new Set();

function broadcast(event, data) {
  const payload = JSON.stringify({ event, data, ts: Date.now() });
  const chunk = `data: ${payload}\n\n`;
  for (const res of listeners) {
    res.write(chunk);
  }
}

function tmuxAlive() {
  try {
    execSync(`tmux has-session -t ${TMUX_SESSION} 2>/dev/null`);
    return true;
  } catch {
    return false;
  }
}

function sendToTmux(message) {
  const tmpFile = `/tmp/msg-${randomUUID()}.txt`;
  try {
    writeFileSync(tmpFile, message);
    execSync(`tmux load-buffer ${tmpFile}`);
    execSync(`tmux paste-buffer -t ${TMUX_SESSION}`);
    execSync(`tmux send-keys -t ${TMUX_SESSION} Enter`);
  } finally {
    try { unlinkSync(tmpFile); } catch {}
  }
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

let lastResponse = null;

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

  // SSE stream
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

  // Health check
  if (req.method === "GET" && url.pathname === "/health") {
    const alive = tmuxAlive();
    const body = JSON.stringify({
      status: alive ? "ok" : "no_tmux",
      name: "blunderdome",
      tmux_alive: alive,
    });
    res.writeHead(200, { ...corsHeaders, "Content-Type": "application/json" });
    res.end(body);
    return;
  }

  // User sends message → tmux
  if (req.method === "POST" && url.pathname === "/message") {
    let body = "";
    req.on("data", (chunk) => { body += chunk; });
    req.on("end", () => {
      console.error(`[channel] POST /message: "${body.slice(0, 100)}"`);
      try {
        sendToTmux(body);
        broadcast("message_received", { content: body });
        res.writeHead(200, { ...corsHeaders, "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: "sent" }));
      } catch (err) {
        console.error(`[channel] tmux send error: ${err.message}`);
        res.writeHead(500, { ...corsHeaders, "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: "error", error: err.message }));
      }
    });
    return;
  }

  // Stop hook delivers structured response
  if (req.method === "POST" && url.pathname === "/hook/stop") {
    let body = "";
    req.on("data", (chunk) => { body += chunk; });
    req.on("end", () => {
      console.error(`[channel] POST /hook/stop: ${body.slice(0, 200)}`);
      try {
        const data = JSON.parse(body);
        lastResponse = data;
        broadcast("reply", { text: data.text, session_id: data.session_id });
        res.writeHead(200, { ...corsHeaders, "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: "ok" }));
      } catch (err) {
        console.error(`[channel] hook parse error: ${err.message}`);
        res.writeHead(400, { ...corsHeaders, "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: "error", error: err.message }));
      }
    });
    return;
  }

  res.writeHead(404, { ...corsHeaders, "Content-Type": "text/plain" });
  res.end("not found");
});

server.listen(PORT, "0.0.0.0", () => {
  console.error(`[blunderdome-channel] listening on port ${PORT} (hooks+tmux mode)`);
});
