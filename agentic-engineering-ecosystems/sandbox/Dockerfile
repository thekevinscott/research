FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    git curl wget jq ripgrep fd-find \
    build-essential \
    sudo ca-certificates tmux unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
    > /etc/apt/sources.list.d/github-cli.list \
    && apt-get update && apt-get install -y gh \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @anthropic-ai/claude-code @earendil-works/pi-coding-agent

# Install Bun (for channel server)
RUN curl -fsSL https://bun.sh/install | bash \
    && ln -s /root/.bun/bin/bun /usr/local/bin/bun

RUN useradd -m -s /bin/bash agent \
    && echo "agent ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /home/agent

COPY --chown=agent:agent .claude/ /home/agent/.claude/
COPY .claude/ /root/.claude/

COPY --chown=agent:agent sandbox-config/CLAUDE.md /home/agent/CLAUDE.md
COPY --chown=agent:agent sandbox-config/AGENTS.md /home/agent/AGENTS.md
COPY --chown=agent:agent sandbox-config/settings.json /home/agent/.claude/settings.json
COPY sandbox-config/settings.json /root/.claude/settings.json
COPY --chown=agent:agent sandbox-config/.mcp.json /home/agent/.mcp.json

# Channel server
COPY --chown=agent:agent channel-server/ /home/agent/channel-server/
RUN cd /home/agent/channel-server && bun install

RUN printf '{"hasCompletedOnboarding":true,"lastOnboardingVersion":"2.1.141"}' > /root/.claude.json \
    && cp /root/.claude.json /home/agent/.claude.json \
    && chown agent:agent /home/agent/.claude.json

COPY watchdog.sh /usr/local/bin/watchdog.sh
RUN chmod +x /usr/local/bin/watchdog.sh

EXPOSE 8788

CMD ["bash", "-c", "/usr/local/bin/watchdog.sh & sleep inf"]
