FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    git curl wget jq ripgrep fd-find \
    build-essential \
    sudo ca-certificates tmux \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @anthropic-ai/claude-code @earendil-works/pi-coding-agent

RUN useradd -m -s /bin/bash agent \
    && echo "agent ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /home/agent

COPY --chown=agent:agent .claude/ /home/agent/.claude/
COPY .claude/ /root/.claude/

RUN printf '{"hasCompletedOnboarding":true,"lastOnboardingVersion":"2.1.141"}' > /root/.claude.json \
    && cp /root/.claude.json /home/agent/.claude.json \
    && chown agent:agent /home/agent/.claude.json

COPY watchdog.sh /usr/local/bin/watchdog.sh
RUN chmod +x /usr/local/bin/watchdog.sh

CMD ["bash", "-c", "/usr/local/bin/watchdog.sh & sleep inf"]
