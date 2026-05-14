FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    nodejs npm \
    git curl wget jq ripgrep fd-find \
    build-essential \
    sudo ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash agent \
    && echo "agent ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER agent
WORKDIR /home/agent

COPY --chown=agent:agent .claude/ /home/agent/.claude/

CMD ["sleep", "inf"]
