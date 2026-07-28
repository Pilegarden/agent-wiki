# minibox-ram-consolidation

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `MiniBox RAM upgrade + consolidation decision`
- status: **draft/awaiting approval** — manual hardware/decision required
- mode: manual
- deliver: local

## Scope

Decide whether MiniBox `.103` upgrades to 64 GB DDR5 + Arc A580 or
consolidates roles onto `.13` (NUCBox, retains 64 GB). Decision doc saved at
`/mnt/obsidian-vault/sys/homelab/improvements/ram-constrained-consolidation-2026-07-27.md`.

## Steps

1. Review decision doc for exact CPU set / GPU / role mapping.
2. Confirm exact P/E core verification if AI/Hermes role retained.
3. Execute procurement/upgrade or migration plan.
4. Update agent/host inventory to match new state.
5. Record outcome in loop doc.

## Safety

Downtime is expected if consolidating roles to another host. Schedule
maintenance window.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
