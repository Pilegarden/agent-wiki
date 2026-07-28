# loops-factory summary | ops

## Scan result
- Topics scanned: ops
- New [LOOPS] items: 1
- Agents without loops: 0

## New artifacts
- loop doc: `topics/ops/loops/brain-heartbeat-recovery.md`
- script: `/home/hermes/.hermes/scripts/brain-heartbeat-recovery.sh`
- cron job: `5f4698960ed7` ("brain-heartbeat-recovery", every 2h, local)

## Open exception
- `ops/populate` — unchanged; still awaiting requirements for [SKILLS]/[LOOPS] materialization.
- `vault-mirror-sync` — failed cron `87e93b77a514` remains pending user repair/disable decision.

## Decision
`brain-heartbeat-recovery` deployed as transport-level guard; MCP admin-scope fix still pending.

## Next action
Rerun after queue changes or user resolves blockers.

## 2026-07-13 23:25 CEST
- Tick result: no new actionable [LOOPS] items; blockers unchanged.
- No new artifacts, crons, or kanban tickets created.

## 2026-07-14 10:21 CEST
- Tick result: scanned queue/content; no new loops or agents found.

## 2026-07-14 11:10 CEST
- Tick result: scanned ops queue/content; no new [LOOPS] items found; `ops/populate` still blocked pending requirements.
- No new artifacts, crons, or kanban tickets created.

## 2026-07-15 11:57 CEST
- New loop: brain-heartbeat-recovery deployed. Cron `5f4698960ed7` scheduled every 2h, local delivery.

<!-- loops-factory ran: 2026-07-15 11:57 CEST; deployed brain-heartbeat-recovery cron 5f4698960ed7 -->
