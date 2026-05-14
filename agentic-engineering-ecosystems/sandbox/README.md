# Agent Sandbox (Fly.io)

Ephemeral Firecracker microVM on Fly.io for running coding agents with full permissions in hardware-isolated sandbox.

## What You Get

- Ubuntu 24.04 with Python, Node, git, build tools
- `agent` user with passwordless sudo (full root)
- Your local `~/.claude` config auto-copied into the sandbox
- No public ports — SSH only via WireGuard tunnel
- Hardware isolation (Firecracker microVM, not Docker)
- ~$0.032/hr (4 shared CPU, 4GB RAM)
- Billed per second, $0 when destroyed

## Prerequisites

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Authenticate
fly auth login
```

Credit card required (no free tier).

## Usage

```bash
# Launch sandbox
./scripts/launch.sh

# Connect (SSH over WireGuard, no exposed ports)
./scripts/connect.sh

# Inside the sandbox — agent has full permissions:
sudo apt install anything
pip install anything
git clone anything
rm -rf /  # won't affect your host

# Destroy when done (stops billing)
./scripts/destroy.sh
```

## Custom App Name

All scripts accept an optional app name argument:

```bash
./scripts/launch.sh my-agent-task-42
./scripts/connect.sh my-agent-task-42
./scripts/destroy.sh my-agent-task-42
```

## Secrets (API Keys)

```bash
fly secrets set ANTHROPIC_API_KEY=sk-ant-... --app agent-sandbox
fly secrets set OPENAI_API_KEY=sk-... --app agent-sandbox
```

Secrets are available as env vars inside the machine.

## Persistent Storage (Optional)

If you want data to survive machine restarts:

```bash
fly volumes create workspace --size 10 --app agent-sandbox --region iad
```

Then add to `fly.toml`:

```toml
[mounts]
  source = "workspace"
  destination = "/home/agent/workspace"
```

## Architecture

```
Your machine
    │
    │ fly ssh console (WireGuard tunnel)
    ▼
Fly.io edge (iad)
    │
    ▼
┌─────────────────────────────┐
│ Firecracker microVM         │
│ ┌─────────────────────────┐ │
│ │ Ubuntu 24.04            │ │
│ │ agent user (sudo)       │ │
│ │ YOUR CODE RUNS HERE     │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
    │
    │ NAT (outbound internet)
    ▼
  Internet (pip, git, APIs)
```

## Cost

| Action | Cost |
|--------|------|
| Running (4 CPU, 4GB) | $0.032/hr |
| Stopped | $0.15/GB rootfs/month |
| Destroyed | $0 |
| 30-min agent task | ~$0.016 |
| 1 hour heavy session | ~$0.032 |

## Security Model

- Firecracker microVM = hardware isolation (KVM)
- Separate Linux kernel from host
- No shared filesystem with host or other VMs
- Agent can `rm -rf /`, install malware, mine crypto — contained to VM
- Destroy the machine = gone forever
