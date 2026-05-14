const express = require('express');
const { WebSocketServer } = require('ws');
const pty = require('node-pty');
const { execSync, execFileSync } = require('child_process');
const http = require('http');
const path = require('path');
const url = require('url');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// --- Session API ---

function tmux(...args) {
  return execFileSync('tmux', args, { encoding: 'utf8' }).trim();
}

app.get('/api/sessions', (req, res) => {
  try {
    const out = tmux('ls', '-F', '#{session_name}');
    const sessions = out ? out.split('\n').filter(Boolean) : [];
    res.json(sessions);
  } catch {
    // tmux exits non-zero when no sessions exist
    res.json([]);
  }
});

app.post('/api/sessions', (req, res) => {
  const { name, command } = req.body;
  if (!name || /\s/.test(name)) {
    return res.status(400).json({ error: 'Session name required and must not contain spaces' });
  }
  try {
    tmux('new-session', '-d', '-s', name);
    if (command) {
      tmux('send-keys', '-t', name, command, 'Enter');
    }
    res.json({ name });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.delete('/api/sessions/:name', (req, res) => {
  try {
    tmux('kill-session', '-t', req.params.name);
    res.json({ ok: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// --- WebSocket Terminal Bridge ---

const server = http.createServer(app);
const wss = new WebSocketServer({ noServer: true });

server.on('upgrade', (request, socket, head) => {
  const parsed = url.parse(request.url, true);
  if (parsed.pathname !== '/terminal') {
    socket.destroy();
    return;
  }
  wss.handleUpgrade(request, socket, head, (ws) => {
    wss.emit('connection', ws, request);
  });
});

wss.on('connection', (ws, request) => {
  const parsed = url.parse(request.url, true);
  const sessionName = parsed.query.session;
  const cols = parseInt(parsed.query.cols) || 220;
  const rows = parseInt(parsed.query.rows) || 50;

  if (!sessionName) {
    ws.send('\r\nNo session specified.\r\n');
    ws.close();
    return;
  }

  // Verify session exists
  try {
    tmux('has-session', '-t', sessionName);
  } catch {
    ws.send(`\r\nSession '${sessionName}' not found.\r\n`);
    ws.close();
    return;
  }

  let ptyProcess;
  try {
    ptyProcess = pty.spawn('tmux', ['attach-session', '-t', sessionName], {
      name: 'xterm-256color',
      cols,
      rows,
      env: { ...process.env, TERM: 'xterm-256color' },
    });
  } catch (err) {
    ws.send(`\r\nFailed to attach: ${err.message}\r\n`);
    ws.close();
    return;
  }

  ptyProcess.onData((data) => {
    if (ws.readyState === ws.OPEN) {
      ws.send(data);
    }
  });

  ptyProcess.onExit(() => {
    if (ws.readyState === ws.OPEN) ws.close();
  });

  ws.on('message', (msg) => {
    // Resize frames come as JSON strings, keystrokes as binary/string
    const str = msg.toString();
    try {
      const frame = JSON.parse(str);
      if (frame.type === 'resize' && frame.cols && frame.rows) {
        ptyProcess.resize(frame.cols, frame.rows);
        return;
      }
    } catch {
      // not JSON — treat as raw input
    }
    ptyProcess.write(str);
  });

  ws.on('close', () => {
    try { ptyProcess.kill(); } catch {}
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, '0.0.0.0', () => {
  console.log(`tmux-mirror running at http://0.0.0.0:${PORT}`);
});
