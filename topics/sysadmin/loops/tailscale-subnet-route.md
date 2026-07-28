# tailscale-subnet-route

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `Tailscale subnet route on Hermes VM`
- status: **draft/awaiting approval** — manual network configuration required
- mode: manual
- deliver: local

## Scope

Apply Tailscale subnet route + accept so phone clients can reach
`192.168.10.0/24` via the Hermes VM. Note saved at
`/mnt/obsidian-vault/sys/homelab/topology/tailscale-hermes-subnet-route.md`.

## Steps

1. Verify Hermes VM Tailnet IP and existing subnet routes.
2. Add subnet route for `192.168.10.0/24` via Hermes VM in Tailscale admin console.
3. Enable subnet route accept on Hermes VM Tailscale interface.
4. Verify reachability from a phone client to a LAN host (e.g. `.200` or `.104`).
5. Record outcome in loop doc.

## Safety

Do not disrupt active Tailscale exit-node or ACL settings. Confirm route
before full rollout.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
