# Firecracker microVM: Secure Sandboxing for Autonomous Coding Agents

The core question: **can you launch a coding agent with 100% permissions inside a sandbox and not worry about it escaping?** Firecracker microVMs are the industry's answer. Hardware-level isolation, ~125ms boot, ~5 MiB overhead — near-Docker density with VM-grade security.

---

## Why Not Docker?

Docker containers share the host kernel. This is the fundamental problem for untrusted code execution.

| Risk | Docker | Firecracker microVM |
|------|--------|-------------------|
| Kernel attack surface | ~300+ syscalls exposed | Guest has own kernel; host sees ~24 syscalls from VMM |
| Container/VM escapes | Multiple CVEs per year (runc, containerd) | Historically rare; minimal device model |
| Host compromise path | One kernel bug away | Must escape guest kernel → VMM → jailer → host |
| Privilege escalation | Regular occurrence via kernel vulns | Hardware isolation (VT-x/AMD-V) prevents it |
| Recent CVEs | CVE-2024-21626 "Leaky Vessels" (all Docker <25.0.2) | CVE-2026-5747 (PCI transport initialization — patched in v1.15.1) |

**The security equation for AI agents:**
- Docker = your agent's arbitrary code runs on your host kernel directly
- Firecracker = agent code runs inside a separate kernel, behind hardware virtualization, inside a jailed process with seccomp-BPF filtering

For a coding agent with full `sudo`, `apt install`, network access, and arbitrary shell execution — Docker is insufficient. Firecracker is purpose-built for this.

---

## Performance Overhead vs Docker

All Firecracker numbers from SPECIFICATION.md (CI-enforced on M5D.metal / M6G.metal) or NSDI 2020 paper.

| Metric | Firecracker | Docker | Delta |
|--------|-------------|--------|-------|
| Boot time (cold) | ≤125 ms | 100-300 ms (cached Alpine) | Comparable |
| Snapshot restore | ~5-10 ms | N/A (no equivalent) | Firecracker wins |
| VMM memory overhead | ≤5 MiB per VM | Negligible (shared kernel) | +5 MiB per instance |
| CPU performance | >95% of bare metal | ~98-100% of bare metal | 3-5% penalty |
| Network throughput | 14.5 Gbps @ 80% core | Near line-rate | Slight penalty |
| Network latency added | 0.06 ms | Microseconds (veth) | Negligible |
| Storage throughput | 1 GiB/s @ 70% core | Near-native (overlay2) | I/O emulation cost |
| Density | 4,000+ per host demonstrated | Thousands+ | Comparable |
| Creation rate | 5/core/second (180/s on 36-core) | Faster | Slight penalty |

**Bottom line:** For a coding agent use case (one or a few concurrent sandboxes, not thousands), the overhead is invisible. The 3-5% CPU penalty and 5 MiB memory overhead are irrelevant compared to the cost of running an LLM.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Host (bare metal or nested-virt-capable cloud)         │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Jailer                                         │   │
│  │  - chroot + PID/net/mount namespaces            │   │
│  │  - cgroups (CPU, memory, blkio)                 │   │
│  │  - seccomp-BPF (24 allowed syscalls)            │   │
│  │  - drops all capabilities                       │   │
│  │                                                 │   │
│  │  ┌─────────────────────────────────────────┐   │   │
│  │  │  Firecracker VMM (Rust, ~3 MiB binary)  │   │   │
│  │  │  - REST API over Unix socket             │   │   │
│  │  │  - virtio-net, virtio-blk, vsock, RNG    │   │   │
│  │  │  - No BIOS, no USB, no PCI, no GPU       │   │   │
│  │  │                                          │   │   │
│  │  │  ┌──────────────────────────────────┐   │   │   │
│  │  │  │  Guest (own Linux kernel)         │   │   │   │
│  │  │  │  - Full root access               │   │   │   │
│  │  │  │  - Arbitrary code execution       │   │   │   │
│  │  │  │  - Network (configurable)         │   │   │   │
│  │  │  │  - YOUR CODING AGENT LIVES HERE   │   │   │   │
│  │  │  └──────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**Three trust boundaries (inside → out):**
1. Guest kernel (agent runs here with full permissions)
2. KVM hardware virtualization (VT-x/AMD-V enforces separation)
3. Jailer (even if VMM is compromised, it's sandboxed)

**Minimal device model:** Only virtio-net, virtio-blk, virtio-vsock, virtio-balloon, virtio-rng, serial console, partial i8042 (reboot only). No attack surface from USB, PCI, GPU, SCSI, sound, display.

---

## Key Specs

| Spec | Value |
|------|-------|
| Language | Rust (79% of codebase) |
| License | Apache-2.0 |
| GitHub Stars | 34,328 |
| Latest release | v1.15.1 (2026-04-07) |
| Binary size | ~3 MiB (static, musl-linked) |
| Max vCPUs | 32 per microVM |
| Guest RAM | Configurable (128 MiB default, balloon for dynamic) |
| Host kernel | Linux 5.10+ or 6.1+ |
| Guest kernel | Linux 5.10 or 6.1 (Amazon microvm kernels) |
| Architectures | x86_64, aarch64 |
| API | REST over Unix domain socket (OpenAPI spec) |
| Snapshot/restore | Full + differential (dirty page tracking) |
| Rate limiting | Token bucket per device (bandwidth + IOPS) |
| Network | TAP devices, /30 subnets, no built-in DHCP |
| Guest OS | Linux only (no Windows, no macOS) |

---

## What You CAN'T Do

Deliberately excluded by design (minimal attack surface):

- No GPU passthrough (no PCI bus)
- No USB devices
- No display/VGA
- No BIOS/UEFI (direct kernel boot only)
- No live migration (snapshot/restore only, same hardware)
- No nested virtualization
- No Windows/macOS guests
- No multi-queue networking
- No NUMA placement (use jailer cpuset)

For a coding agent sandbox, none of these matter. You need: shell, filesystem, network, maybe a browser. Firecracker provides all of that.

---

## Production Users

| User | Scale | Use Case |
|------|-------|----------|
| **AWS Lambda** | Billions of invocations | Original use case; powers all Lambda |
| **AWS Fargate** | Large | Container workload isolation for ECS/EKS |
| **Fly.io** | Global (30+ regions) | App hosting, scale-to-zero machines |
| **E2B** | AI-focused | Code execution sandboxes for AI agents |
| **Daytona** | Growing | AI agent sandbox infrastructure |
| **Kata Containers** | Kubernetes | Pod-level VM isolation (Firecracker as backend) |
| **Depot** | CI-focused | Fast container builds |
| **OpenAI Codex** | Likely | Network-isolated agent sandboxes (unconfirmed) |

---

## Comparison: Isolation Technologies for Agent Sandboxing

| | Firecracker | gVisor | Docker + seccomp | Kata Containers | V8 Isolates |
|--|-------------|--------|-----------------|-----------------|-------------|
| Isolation level | Hardware (KVM) | Userspace kernel | Kernel namespaces | Hardware (KVM) | Process + JIT |
| Boot time | ~125 ms | ~150 ms | ~100 ms | 500 ms - 1 s | <5 ms |
| Memory overhead | ~5 MiB | ~15-50 MiB | Negligible | ~20-40 MiB | ~2 MiB |
| CPU overhead | <5% | Near-native (but 2-10x syscall cost) | <1-2% | <5% | Near-native |
| Full Linux compat | Yes (own kernel) | Partial (~200/300 syscalls) | Yes | Yes (own kernel) | No (JS/WASM only) |
| GPU support | No | Yes (2024+) | Yes | Via Cloud Hypervisor | No |
| Untrusted code safe | **Yes** | Mostly (still shares host kernel surface) | **No** | **Yes** | Language-constrained |
| OCI compatible | No (needs wrapper) | Yes (runsc) | Yes | Yes | No |
| Best for | Serverless, agent sandboxes | Containers needing stronger isolation | Trusted workloads | Kubernetes pods | Edge functions |

**For your use case** (autonomous coding agent, 100% permissions, must not escape): Firecracker or Kata Containers are the correct choices. Docker is not. gVisor is a compromise — better than Docker, weaker than hardware isolation.

---

## Practical Setup for Agent Sandboxing

### Minimal configuration for a coding agent:

```bash
# 1. Get Firecracker + jailer
curl -L https://github.com/firecracker-microvm/firecracker/releases/download/v1.15.1/firecracker-v1.15.1-x86_64.tgz | tar xz

# 2. Get a kernel and rootfs
# Amazon microvm kernel (~8 MiB) + Ubuntu 24.04 rootfs

# 3. Configure via API (Unix socket)
curl --unix-socket /tmp/firecracker.socket -X PUT http://localhost/boot-source \
  -d '{"kernel_image_path": "./vmlinux", "boot_args": "console=ttyS0 reboot=k panic=1 pci=off"}'

curl --unix-socket /tmp/firecracker.socket -X PUT http://localhost/drives/rootfs \
  -d '{"drive_id": "rootfs", "path_on_host": "./rootfs.ext4", "is_root_device": true, "is_read_only": false}'

curl --unix-socket /tmp/firecracker.socket -X PUT http://localhost/machine-config \
  -d '{"vcpu_count": 4, "mem_size_mib": 4096}'

# 4. Network (TAP device for internet access)
curl --unix-socket /tmp/firecracker.socket -X PUT http://localhost/network-interfaces/eth0 \
  -d '{"iface_id": "eth0", "guest_mac": "AA:FC:00:00:00:01", "host_dev_name": "tap0"}'

# 5. Start
curl --unix-socket /tmp/firecracker.socket -X PUT http://localhost/actions \
  -d '{"action_type": "InstanceStart"}'
```

### What to provision inside the rootfs:

- Python, Node.js, git, build tools
- Your agent runtime (OpenHands, Claude Code, custom)
- SSH server or vsock for host ↔ guest communication
- Pre-cloned repository

### Network control options:

| Strategy | Config | Agent gets |
|----------|--------|-----------|
| Full internet | TAP + NAT | Unrestricted (pip install, git clone, API calls) |
| Restricted | TAP + iptables on host | Allowlisted domains only |
| Air-gapped | No network interface | Zero network; must pre-provision everything |
| API-only | TAP + iptables allow only LLM API endpoint | Can call LLM but nothing else |

---

## Platforms That Wrap Firecracker for You

If you don't want to manage raw Firecracker:

| Platform | Model | Self-host? | Agent-focused? |
|----------|-------|-----------|----------------|
| **E2B** | SDK (Python/TS) | Yes (Terraform + Nomad) | Yes — built for AI code execution |
| **Fly.io** | CLI + API | No (managed) | Not specifically, but Machines API works |
| **Kata Containers** | OCI runtime | Yes (Kubernetes) | No — general container isolation |
| **Daytona** | SDK | Partial | Yes — pivoted to AI agent infra |

**E2B is probably your fastest path** if you want Firecracker isolation without managing the VMM lifecycle yourself. Their infra is open-source (Apache-2.0) and deploys on AWS or GCP via Terraform.

---

## Snapshot/Restore for Fast Agent Launches

Key capability for agent sandboxing: prepare a "golden image" then clone instantly.

1. Boot a microVM with your full agent environment
2. Install all deps, configure SSH, clone repo
3. `PUT /snapshot/create` → memory file + state file
4. For each new task: `PUT /snapshot/load` → resume in ~5-10 ms

**Caveats:**
- Must restore on identical hardware/software
- Network connections reset (need reconnection logic)
- Entropy/crypto state duplicated (VMGenID re-seeds PRNG, but application-level tokens must be refreshed)
- Disk state NOT in snapshot (backup rootfs separately)

This is how AWS Lambda SnapStart works under the hood.

---

## Resource Requirements

### For a single coding agent sandbox:

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| Host vCPUs | 2 (1 for VMM + 1 for guest) | 4+ |
| Host RAM | Guest RAM + 5 MiB + host OS | 8+ GiB |
| Guest RAM | 512 MiB (bare minimum) | 2-4 GiB (for builds, large repos) |
| Guest vCPUs | 1 | 2-4 |
| Disk | 2-10 GiB rootfs | 20+ GiB (node_modules, caches) |
| Host kernel | Linux 5.10+ | 6.1+ (io_uring, better KVM) |

### For concurrent agent pool:

- Each additional agent: +guest RAM + 5 MiB VMM overhead
- On a 64 GiB host with 4 GiB per guest: ~15 concurrent agents comfortably
- With memory balloon: potentially 2x density (return unused guest RAM)

---

## Comparison with QEMU and Cloud Hypervisor

| Dimension | Firecracker | QEMU | Cloud Hypervisor |
|-----------|-------------|------|------------------|
| Language | Rust | C | Rust |
| Boot time | ~125 ms | ~500 ms+ | ~200 ms |
| Memory overhead | ~5 MiB | ~20-40 MiB | ~10-15 MiB |
| Attack surface | Minimal (no PCI, USB, display) | Large (hundreds of devices) | Moderate |
| GPU passthrough | No | Yes | Yes |
| Windows guests | No | Yes | Experimental |
| Live migration | No | Yes | Yes |
| Confidential compute | No | Limited | Yes (TDX, SEV-SNP) |
| Best for | Ephemeral sandboxes | General VMs | Cloud workloads needing VFIO |

**For agent sandboxing:** Firecracker. Smallest attack surface, fastest boot, sufficient features. Only choose Cloud Hypervisor if you need GPU (ML inference in sandbox) or confidential computing.

---

## The "Give Agent 100% Permissions" Architecture

Your stated goal: launch an agent with full permissions, don't worry about escape.

**What this looks like with Firecracker:**

```
Host machine (your server)
├── Firecracker jailer (chroot, seccomp, namespaces)
│   └── Firecracker VMM (Rust, 24 syscalls)
│       └── microVM (own kernel, hardware-isolated)
│           └── Agent runtime
│               ├── root access ✓
│               ├── sudo anything ✓
│               ├── pip/npm/apt install ✓
│               ├── arbitrary shell commands ✓
│               ├── modify any file ✓
│               ├── spawn processes ✓
│               ├── network access (configurable) ✓
│               └── CANNOT escape to host ✓
```

**What the agent CANNOT do even with full guest permissions:**
- Access host filesystem (separate kernel, no shared mounts)
- Read host memory (hardware isolation)
- Access host network beyond what TAP routing allows
- Interact with other VMs (no shared resources)
- Persist beyond VM lifecycle (ephemeral by default)
- Access host devices (no passthrough configured)

**The only realistic escape vectors:**
1. KVM vulnerability (extremely rare, heavily audited)
2. Virtio device emulation bug in Firecracker (small attack surface, Rust, fuzzed)
3. Side-channel attacks (Spectre-class — mitigated by host kernel patches)

This is the same isolation model protecting billions of AWS Lambda invocations from each other.

---

## Sources

- [Firecracker GitHub](https://github.com/firecracker-microvm/firecracker) — 34,328 stars, Apache-2.0
- [NSDI 2020 Paper](https://www.usenix.org/conference/nsdi20/presentation/agache) — "Firecracker: Lightweight Virtualization for Serverless Applications"
- [Firecracker Design Doc](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md)
- [Firecracker SPECIFICATION.md](https://github.com/firecracker-microvm/firecracker/blob/main/SPECIFICATION.md) — CI-enforced performance targets
- [E2B Infrastructure](https://github.com/e2b-dev/infra) — Open-source Firecracker orchestration
- [E2B SDK](https://github.com/e2b-dev/E2B) — 12.2K stars
- [Fly.io Blog](https://fly.io/blog/) — Firecracker in production at scale
- [Kata Containers](https://katacontainers.io) — OCI runtime using Firecracker as backend
- [gVisor](https://gvisor.dev/docs/architecture_guide/) — Alternative isolation (Google)
- [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor) — Rust VMM with GPU/VFIO support
- [AWS Blog: Firecracker](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/) — Original announcement (2018)
- [Daytona](https://www.daytona.io/) — AI agent sandbox platform on Firecracker
