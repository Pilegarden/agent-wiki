---
title: Loop Registry
created: 2026-07-12
updated: 2026-07-28T21:54 +02
type: catalog
tags: [goop, loops, registry]
---

# Loop Registry

| Loop | Topic | Job ID | Schedule | Status | Last Run/Note |
|---|---|---|---|---|---|
| nous-girl-system | _global | `none` | per-turn | active | continuous / per-turn |
| adguard-home-sync | dev | `6cf4ddcff112` | */15 * * * * | active | ok; ok |
| config-edit-verifier | dev | `124337b6d86a` | 0 8 * * * | active | ok; ok |
| discord-preview-watchdog | dev | `f5b553f70ca0` | */30 * * * * | active | ok; ok |
| nexus-intel-sync | integration | `da64be0fe62c` | 0 8 * * * | live/runtime-error | profile nexus-integration stopped; job present but `last_run_at` null (created 2026-07-24, never executed) |
| cc-170-mandate-reconciler | openclaw | `f9aefeca065b` | 0 9 * * * | active | ok; ok |
| brain-heartbeat-recovery | ops | `b2d9c7c4e555` | every 120m | active | ok; ok |
| vault-mirror-sync | ops | `none` | N/A | stale/phantom | absent from all Hermes profile cron stores |
| watchdog-recovery | ops | `none` | N/A | resolved | resolved 2026-07-13 |
| adguard-api-stability-verification | sysadmin | `none` | manual | draft/awaiting | VIP failover verification pending approval |
| adguard-dashboard-watchdog | sysadmin | `none` | N/A | disabled/resolved | resolved 2026-07-13 |
| adguard-yaml-fix | sysadmin | `none` | manual | draft/awaiting | YAML schema fix pending approval |
| adguardhome-sync-schema-compatibility | sysadmin | `none` | manual | draft/awaiting | schema compatibility review pending approval |
| bws-first-secret-handling | sysadmin | `none` | manual | draft/awaiting | BWS-first secret handling policy pending |
| cron-dependency-monitor | sysadmin | `7d390796d546` | 0 8 * * * | active | ok; ok |
| hermes-dashboard-auth-lookup | sysadmin | `none` | manual | completed | lookup executed 2026-07-25 |
| home-assistant-token-rotate | sysadmin | `none` | manual | draft/awaiting | HA long-lived token rotation pending |
| keepalived-vip-failover-test | sysadmin | `none` | manual | draft/awaiting | VIP failover test pending approval |
| minibox-ram-consolidation | sysadmin | `none` | manual | draft/awaiting | RAM upgrade decision pending |
| tailscale-subnet-route | sysadmin | `none` | manual | draft/awaiting | pending approval |
| vault-sync-push-trigger | sysadmin | `337fb9ff9a8a` | */15 * * * * | active | ok; ok |
| x-twitter-heartbeat-empty-payload-investigation | sysadmin | `none` | N/A | resolved/superseded | superseded after user removed x-twitter-heartbeat cron |
| orm-mandate-reconciler | system/orm | `97aff819f7ca` | 0 9 * * * | active | ok; ok |
| avanza-mcp-watchdog | trading | `none` | N/A | stale/phantom | absent from all Hermes profile cron stores; false recovery corrected 2026-07-27 |
| daily-brief-watcher | trading | `cfa9d1137d7f` | 30 6 * * 1-5 | active | ok; ok |
| hard-stop-daily-check | trading | `94c1991eff81` | 0 18 * * 1-5 | active | ok; ok |
| nordnet-position-reconciler | trading | `none` | N/A | stale/draft | never deployed |
| nordnet-watchdog | trading | `none` | N/A | deprecated | superseded |
| portfolio-snapshot-daily | trading | `62b064f80b5e` | 0 6 * * 1-5 | active | ok; recovered 2026-07-28 06:00 |
| session-db-repair | trading | `none` | manual | deferred | awaiting approval |
| thesis-fit-review | trading | `115b88c1d5fd` | 0 9,14 * * 1-5 | active | ok; ok |
| thesis-fit-review-last | trading | `none` | N/A | idle/artifact | duplicate run artifact; kept on disk |
| thesis-hoard-balance-audit | trading | `1a61890a11d1` | 0 9 * * 1 | active | ok; ok |
| trading-daily-snapshot-fix | trading | `none` | manual | queued | awaiting infra maintenance |
| trading-infra-watcher | trading | `b5aa5e1f418c` | 0 9,14 * * 1-5 | active | recovered 2026-07-26 |
| trading-watcher | trading | `none` | N/A | resolved/phantom | superseded by trading-infra-watcher |
| x-twitter-heartbeat | trading | `none` | N/A | removed | deliberately removed by user [Stop] 2026-07-27 16:06 CEST; investigation superseded |
| dev-ops-helper | dev | `none` | N/A | loopless | no loop doc; awaiting explicit [LOOPS] or user direction |
| vault-sync-checker | dev | `none` | N/A | loopless | no loop doc; awaiting explicit [LOOPS] or user direction |


## Creating a Loop

- **Automatic:** Context → queue → Loops writes.
- **Manual:** Edit `topics/<name>/.system/queue.md` and add under `## [LOOPS] items`.
