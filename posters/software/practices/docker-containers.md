---
title: "Containers vs Virtual Machines"
subtitle: How namespaces, control groups and layered filesystems isolate applications
byline: Software practices
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-014
colours:
  accent: "#0284c7"
  secondary: "#0369a1"
footer:
  left: Containers and VMs
  centre: Software Engineering Reference
  qr: https://opencontainers.org/
  qr-label: Open Container Initiative
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| Under 100 ms | To start a container; a VM takes 10 to 60 s |
| 1 kernel | Shared by every container on a host |
| 5 to 50 MB | A minimal Alpine or distroless image |
| 3 kernel features | Namespaces, cgroups and OverlayFS |

## Introduction {.abstract}

A **virtual machine (VM)** isolates a workload by emulating hardware with a **hypervisor**, and boots a whole guest operating system: gigabytes of memory and seconds to start. An **OCI container** is an ordinary process on a shared Linux kernel, isolated by **namespaces**, limited by **control groups**, and given a layered filesystem. It packages software reproducibly, at bare-metal speed.

## 1. A virtual machine

```stack
App A | app | With its libraries | green
Guest OS | kernel | A whole kernel per VM | amber
Hypervisor | KVM | Hyper-V, Xen | navy
Host | hardware | CPU, memory, disks | grey
side: One VM | 1-2 | amber
```

## 2. A container

```stack
App A | app | With its libraries | green
Runtime | runc | containerd, CRI-O | blue
Host kernel | Linux | Shared by every container | navy
Host | hardware | CPU, memory, disks | grey
side: One container | 1-1 | green
```

## 3. Side by side {.wide}

```compare
| Virtual machine | OCI container
Boundary | **Hardware virtualisation**: a hypervisor and CPU extensions | **Kernel namespaces and cgroups** on a shared kernel
Kernel | One per VM | **One for the host**
Start-up | **10 to 60 s**: firmware and a whole OS boot | **Under 100 ms**: a process starts
Size | Gigabytes of RAM, 5 to 20 GB of disk | Megabytes of RAM, 5 to 200 MB of image
Other operating systems | Windows on Linux, or the reverse | Linux containers need a Linux kernel, or a small VM
Blast radius | **Strong**: a guest kernel panic stays in the VM | A kernel bug can reach the host, unless hardened with seccomp and rootless mode
```

## 4. Three kernel features {.wide}

A "container" is not one thing in the kernel. It is a process given three features:

```cards cols=3 style=top
Namespaces: what it sees | Its own process tree (pid), network (net), mounts (mnt), hostname (uts), IPC and user IDs (user) | navy
cgroups: what it uses | Limits and accounts for CPU, memory, disk I/O and network, so one container cannot starve the rest | blue
OverlayFS: its files | Read-only image layers, shared on disk and in cache, under a thin copy-on-write layer for each container | teal
```

## 5. Image layers

Each read-only layer is named by its SHA-256 digest, so updating the app downloads only the top layer:

```stack
Writable layer | per container | Copy-on-write: gone with the container | amber
Application | /app/server | The changed layer | green
Runtime libraries | libc, CA certificates | Shared | blue
Base userland | Alpine or Debian | Shared | navy
side: Read-only, shared | 2-4 | navy
```

## 6. Multi-stage builds

Compile in a full toolchain image, then copy only the binary into a minimal one:

```dockerfile
# Stage 1: build with the full Go toolchain
FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app ./cmd/server

# Stage 2: a distroless runtime: no shell, no compiler
FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=builder /out/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

The result is about 12 MB.

## 7. Running it hardened

```terminal title="Least privilege"
$ docker run --read-only --tmpfs /tmp --cap-drop=ALL \
    --memory=256m --cpus=0.5 --user 65532:65532 \
    registry.example.com/app@sha256:9f86d0...
-- Read-only root, no capabilities, capped memory and CPU, a non-root user, and an image pinned by digest
```

## 8. Hardening checklist {style=card colour=blue}

```checklist
[x] A non-root user, and rootless mode so container root is not host root
[x] All capabilities dropped; add back only what is needed
[x] A read-only root filesystem, with tmpfs for scratch
[x] Memory and CPU limits, so one container cannot exhaust the host
[x] Base images pinned by digest and scanned in CI
```

## 9. Glossary {.wide}

```glossary cols=3
cgroups | Linux control groups: resource limits
CoW | Copy-on-write
KVM | Kernel-based Virtual Machine, Linux's hypervisor
Namespace | A per-process view of a kernel resource
OCI | Open Container Initiative: image and runtime standards
seccomp | A filter on the system calls a process may make
```

## In short {.summary}

Use a VM for a hard boundary between untrusted workloads, or another kernel. Use a container for fast, light, reproducible packaging on a shared Linux kernel.

### Share the kernel, isolate the view

Namespaces hide everything else; cgroups cap what is used. No hypervisor needed.

### Build in stages

Compile with the toolchain, ship only the binary.

### Never run as root

Drop capabilities, mount read-only, use a non-root user.
