# dev-ops-helper

## Status
Provisioned (2026-07-27)

## Source/Queue Reference
- Queue: `topics/dev/.system/queue.md`
- Item: `dev-ops-helper — read-only ops helper for PVE/LXC/AdGuard triage`

## Profile Location and Key Files
- Profile path: `~/.hermes/profiles/dev-ops-helper/`
- Identity: `SOUL.md`
- Config: `config.yaml`

## Summary of Responsibilities
Read-only infrastructure triage agent. Inspects Proxmox VE/LXC node and container state, AdGuard HA status, keepalived state, firewall, and ARP/reachability. Routes inspection through PVE `.120` via `pct exec`. Surfaces exact failing service/command/path with concise triage output. Pulls credentials only via BWS.

## Operating Constraints
- Read-only by default; no service mutations without explicit approval
- BWS for secrets; never echo credentials into chat
- Concise output: status → evidence → exact failing service/command/path

## Next Actions
- Configure model/toolsets in `config.yaml` if needed
- Verify profile loads correctly: `dev-ops-helper chat`
