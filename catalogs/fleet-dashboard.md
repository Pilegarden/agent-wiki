---
title: Fleet Dashboard
created: 2026-07-12
updated: 2026-07-28T15:04+02:00
type: catalog
tags: [goop, fleet, dashboard]
---

# Fleet Dashboard

| Topic | Agents | Skills | Loops | Active Blockers | Recent Activity |
|---|---|---|---|---|---|
| _global | 2 | 5 | 1 | — | 2026-07-20 registry sync / idle-tick watchdog normal |
| integration | 1 | 1 | 1 | nexus-intel-sync `live/runtime-error` (cron `da64be0fe62c` present in nexus-integration profile cron store but profile stopped; job never executed). Prior stale phantom misclassification corrected 2026-07-25. | 2026-07-23 cc-170 loop created |
| nous-girl | 0 | 1 | 0 | — | 2026-07-21 topic scaffold created |
| openclaw | 1 | 1 | 1 | CC 170 mandate doc not adopted | 2026-07-23 cc-170 loop created |
| ops | 0 | 1 | 3 | vault-mirror push blocked | 2026-07-25 phantom audit corrected brain-heartbeat-recovery active; vault-mirror-sync remains phantom |
| sysadmin | 0 | 0 | 13 | — | 2026-07-27 5 manual loop docs drafted (Tailscale, MiniBox, HA token, BWS, x-twitter investigation); pending approval |
| system | 0 | 0 | 0 | — | 2026-07-24 topic scaffold created |
| system/orm | 1 | 2 | 1 | ISO 27001 doc not yet adopted | 2026-07-23 orm loop created |
| dev | 2 | 0 | 3 | — | 2026-07-27 2 loops recovered to active (adguard-home-sync, config-edit-verifier); 2 loop-less agents pending [LOOPS] direction |
| trading | 2 | 4 | 14 | avanza-mcp-watchdog stale/phantom; portfolio-snapshot-daily active (recovered 2026-07-28 06:00) | 2026-07-27 loops-factory idle-tick: `x-twitter-heartbeat` removed by user [Stop] (cron `e0260ed247a1`); `portfolio-snapshot-daily` recovered to active; `avanza-mcp-watchdog` corrected stale/phantom; other trading loops active |
| travel | 0 | 0 | 0 | — | 2026-07-20 queue idle |

## Phantom / Drift Watch

- trading: `avanza-mcp-watchdog` stale/phantom (cron `55c3a863d778` absent from all stores; prior recovery claim false); `x-twitter-heartbeat` removed 2026-07-27 16:06 CEST (cron `e0260ed247a1` absent after user [Stop]); `trading-infra-watcher` active; `portfolio-snapshot-daily` recovered 2026-07-28 06:00; `trading-watcher` retained as resolved/superseded; `thesis-fit-review-last` idle artifact.
- trading/infra: `trading-infra-watcher` and `trading-watcher` wiki docs exist but have no Hermes profile (~/.hermes/profiles/ missing).
- ops: vault-mirror-sync remains phantom; brain-heartbeat-recovery active; phantom audit refreshed 2026-07-27 04:27 CEST.
- sysadmin: vault-sync-push-trigger and cron-dependency-monitor active after script restoration on 2026-07-22.
- _global: nous-girl-system has per-turn loop doc and is active; loop-less anomaly cleared.
- integration: nexus-intel-sync `live/runtime-error` (cron `da64be0fe62c` present in nexus-integration profile cron store but profile stopped; never executed).
- dev: `dev-ops-helper` and `vault-sync-checker` agents lack deployed loops; pending explicit [LOOPS] queue items or user direction.
- dev: `discord-preview-watchdog` active — verified live in dev cron store on 2026-07-28 (cron `f5b553f70ca0`); phantom classification corrected to active.
- openclaw: `openclaw-system-agent` has deployed loop `cc-170-mandate-reconciler` (cron `f9aefeca065b` active).

## Last loops-factory tick
- **2026-07-28 13:00 CEST** — idle-tick phantom audit: nexus-intel-sync corrected from `active` to `live/runtime-error` because profile "nexus-integration" is stopped; job `da64be0fe62c` present in profile cron store but `last_run_at` is null (created 2026-07-24, never executed). Loop doc updated to reflect actual state. Fleet-dashboard blocker and drift-watch annotations updated. Catalog sync: all 5 catalogs == live. No new artifacts or crons created.
- **2026-07-28 CEST** — idle-tick phantom audit + live-evidence override: all queues idle; verified 37 loop docs == 37 registry rows; `discord-preview-watchdog` (dev) corrected from stale/phantom to active after verified live in dev cron store (job `f5b553f70ca0`); loop doc rewritten from phantom to active; fleet-dashboard phantom-watch updated; catalogs in sync; no new artifacts or crons created.
- **2026-07-28 01:45 CEST** — idle-tick phantom audit: all queues idle; verified 37 loop docs == 37 registry rows; `discord-preview-watchdog` (dev) corrected to stale/phantom (Job ID `f5b553f70ca0` absent from all cron stores); loop doc annotated; fleet-dashboard phantom-watch updated; catalogs in sync; no new artifacts or crons created.
- **2026-07-27T21:57 CEST** — idle-tick maintenance with active [LOOPS]: phantom audit verified existing entries stable; 5 sysadmin manual loop docs drafted (Tailscale, MiniBox, HA token, BWS, x-twitter investigation); loop-registry 32→37 rows; topic-index and fleet-dashboard counts updated; queues marked [x]; catalogs synced; no new crons created.
- **2026-07-27 12:01 CEST** — active maintenance: verified 3 dev queue loops ([LOOPS] items) were already deployed; recovered loop docs + registry entries with accurate job IDs/schedules; loop-registry full canonical rewrite (33 rows); fleet-dashboard updated; catalogs synced; phantom audit applied; loop-less anomalies documented; no new artifacts or crons created.
- **2026-07-27 12:16 CEST** — agents-factory: provisioned `dev-ops-helper` and `vault-sync-checker` profiles; SOUL.md + config.yaml written to each; wiki agent docs updated; agent-roster expanded (9 rows, malformed rows repaired with full rewrite — patch inversion trap avoided); catalogs synced; fleet-dashboard loop-less anomaly note already present.
- **2026-07-27 09:58 CEST** — idle-tick maintenance; phantom-loop audit applied; avanza-mcp-watchdog false recovery corrected to stale/phantom (cron `55c3a863d778` absent from all stores); portfolio-snapshot-daily status verified live/runtime-error with script execute-bit fix; loop-registry 29 rows == disk 29 loop docs; agent-roster 7 rows == disk 7 flat agents; topic-index counts match disk; no catalog drift found; queues idle; no new artifacts or crons created.
- **2026-07-27 07:32 CEST** — idle-tick maintenance; phantom-loop audit applied; portfolio-snapshot-daily loop doc and registry corrected (script still missing, awaiting approval); loop-registry malformed row 22 repaired with full canonical rewrite (29 rows); catalogs synced; no new artifacts or crons created.
- **2026-07-26 01:25 CEST** — active recovery: recreated 4 trading phantom crons (`trading-infra-watcher`, `x-twitter-heartbeat`, `portfolio-snapshot-daily`, `avanza-mcp-watchdog`); `trading-watcher` resolved/superseded; loop-registry rebuilt (29 rows, no malformed); fleet-dashboard and catalogs synced.
- **2026-07-27T20:37 CEST** — idle-tick phantom audit + live/runtime-error repair: all queues idle; verified 32 loop docs == 32 registry rows; no malformed rows; `portfolio-snapshot-daily` and `x-twitter-heartbeat` loop docs + registry + fleet-dashboard corrected to reflect Hermes runtime "Script not found" despite valid on-disk scripts (path-resolution/sandbox infra finding); catalogs in sync; no new crons or artifacts created.
- **2026-07-27T13:38+02:00** — idle-tick maintenance with active [LOOPS]: phantom audit verified existing entries stable; 5 sysadmin manual loop docs drafted (Tailscale, MiniBox, HA token, BWS, x-twitter investigation); loop-registry 32→37 rows; topic-index and fleet-dashboard counts updated; queues marked [x]; catalogs synced; no new crons created.
- **2026-07-28 01:45 CEST** — skills-factory idle tick: no open [SKILLS]; disk skills 15 == registry 15 rows; no malformed rows; catalogs in sync; agent-roster stale row cleaned (trading-watcher resolved/superseded) to reflect disk 8 flat agents; no new artifacts created.
