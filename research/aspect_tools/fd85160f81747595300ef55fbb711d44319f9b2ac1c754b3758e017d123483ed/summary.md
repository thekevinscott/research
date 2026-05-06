# Summary

Northflank's "Ephemeral execution environments for AI agents in 2026" defines the sandbox layer for dark factories: an isolated runtime created, used, and destroyed per pull request, function call, or agent task, that holds state within a session but is ephemeral across sessions. Northflank itself runs Firecracker, gVisor, and Kata Containers and processes 2M+ isolated workloads/month with BYOC across major clouds.

For dark-factory builders Northflank is both vendor and oracle: their blog is the definitive public comparison of e2b vs Daytona vs Modal vs Cloudflare sandboxes, and their own platform is one of the heavier-used Kubernetes-native options for orchestrating agent sandboxes at scale, particularly when teams need to bring their own cloud or run on-prem.
