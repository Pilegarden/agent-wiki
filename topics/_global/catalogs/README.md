# Agent Wiki Fleet

Fleet dashboard of topics, agents, skills, loops.

## Topics

| Topic | Status | Watch item |
|---|---|---|
| trading | 🟡 Partial | daily-brief.md missing, Market Daily Snapshot blocked; primary SIVE insider dataset path `/mnt/download` absent, hoard finalization blocked |
| ops | 🟡 Partial | gbrain MCP heartbeat DOWN(scope); vault-mirror push blocked |
| sysadmin | 🟡 Active | AdGuard HA .200/.201 active on VIP 192.168.10.254; tooling work: hoarding catalog analyzed, markitdown/codegraph/fredapi installed, reference notes batch, macro-tooling decision written, repo-catalog-evaluated-2026-07-24.md finalized; o2b/NFS/Playwright blockers open; `.251` SSH blocked; legacy .252/.253 destroyed; NUCBox/Box.104 plans pending; `.251` web UI port changed to 6060 (awaiting operator decision) |
| system | 🟡 Scaffolded | Topic scaffold created; sub-topic `system/orm` exists |
| travel | 🟢 Idle | Telegram not wired to travel profile |
| integration | 🟢 Idle | README scaffolded |
| nous-girl | 🟢 Stable | Front-door agent |
| openclaw | 🟡 Active | CC 170 mandate doc not yet adopted |
| system/orm | 🟡 Active | ISO 27001 doc not yet adopted |
| dev | 🟡 Active | 3 loops recovered to active (discord-preview-watchdog, adguard-home-sync, config-edit-verifier); 2 loop-less agents pending [LOOPS] direction |

## Active Blockers
- trading: `/home/hermes/.hermes/profiles/dev/market/daily-brief.md` missing
- ops: gbrain HTTP daemon / MCP admin scope
- travel: `travel` profile Telegram not wired — `channel_directory.json` shows `telegram: []`
- openclaw: CC 170 mandate doc selected but not adopted
- system/orm: ISO 27001 doc selected but not adopted
- sysadmin: `o2b` CLI broken; Brain note writes fallback to Python until binary restored
- sysadmin: NFS root-owned file permissions on `/mnt/obsidian-vault` block `rsync --delete` primary → secondary mirror
- sysadmin: `browser-use` runtime absent; Playwright wrapper provisioning pending on `.205`
- sysadmin: 127 bookmark-derived repos need dedupe against 68-repo hoarding catalog
- trading: portfolio.json stale (2026-07-14); user dropped refresh directive
- trading: OBDU position discrepancy — 100 shares in JSON vs 609 shares in hoard note
- trading: focus topic assets pending ingestion (SIVE 32.8 SEK, YouTube, X statuses, odaily article)
- trading: Obducat Q2 2026 report cron `29bbf060bd7d` status unknown

## Recent Activity

> [2026-07-26 12:25 CEST] context-factory tick completed
>   - Nous-girl session `20260711_092022_7d3ac023` tail surfaces new durable artifact: `consumer-upgrade-advisory` skill created via `/learn` from phone upgrade conversation (Fold6 → Fold7/S25 Ultra/Fold8 comparison).
>   - Skill registered in wiki skill-registry under nous-girl and _global mirrors; wiki mirror docs written to `topics/nous-girl/skills/` and `topics/_global/skills/`.
>   - Memory/model-routing discussion (Hermes vs Claude memory, free Claude access) was conversational; no new topic, agent, loop, or queue item warranted.
>   - No roster change; no new topics, agents, or loops.

> [2026-07-24 10:23 CEST] context-factory tick completed
>   - Scanned sessions across nous-girl, trading, sysadmin, ops, travel: no new user-facing chats since prior tick.
>   - Bootstrap: `system` topic scaffold created (README, continuity, injections, queue, empty skill/agent/loop dirs).
>   - fleet README, topic-index, and fleet-dashboard updated with `system` row (0/0/0 scaffolded).
>   - No queue changes needed.

> [2026-07-23 23:xx CEST] context-factory tick completed
>   - Trading session `20260720_063611_b6abdce6` tail surfaces SIVE insider dataset path blocker: `/mnt/download` does not exist, `/mnt/downloads` unrelated, `/mnt/vault/downloads` empty. Consolidated insider analysis pinned on dev cache file.
>   - Sysadmin Discord session `20260709_135620_af1dab49` tail resolves `.250` dashboard blank (`statistics.enabled: false` → `true`), `.2` 46 user rules migrated to `.200`, `.250` recovered from YAML corruption via known-good backup, and active dev Discord config patched with `streaming: true` + tool-progress settings on `/home/hermes/.hermes/profiles/dev/config.yaml`.
>   - trading/sysadmin README/continuity/queue updated; fleet dashboard watch items refreshed; no roster change; no new topics, agents, skills, or loops.

> [2026-07-23 15:47 CEST] context-factory tick completed
> - Sysadmin Discord session tail (`20260709_135620_af1dab49`) surfaces new VIP/topology change: user destroyed legacy `.252`/`.253` LXCs and switched `.200`/`.201` keepalived VIP from `192.168.10.249` to `192.168.10.254`.
>   - Active state verified: `.250` MASTER + `.251` BACKUP, AdGuard active on both, adguardhome-sync resident on .250, replication to .251 pending verification.
>   - `.251` direct SSH blocked by sshd_config; `.51` (`pve-sff`) PVE host unreachable after `bridge fdb flush dev vmbr0`.
> - sysadmin README/continuity/queue updated with verified topology; fleet dashboard watch item refreshed.
> - **Roster change:** `openclaw` and `system/orm` topics exist on disk but were missing from this fleet README; added.

> [2026-07-23 13:xx CEST] context-factory tick completed
>   - Trading session `20260720_063611_b6abdce6` tail surfaces Nokia Q2 2026 note + Obducat Q2 2026 one-shot watcher cron.
>   - trading continuity/README updated with Nokia/Obducat artifacts/active issue; no roster change; no new topics, agents, skills, or loops.

> [2026-07-23 10:08 CEST] context-factory tick completed
>   - Sysadmin session tail surfaces two new AdGuard HA findings: `.252` Unbound container listening on `5335` but DNS fails due to missing device nodes in bind-mounted config dir (volume issue, not networking); `.253` switching to direct public resolvers (`1.1.1.1`, `8.8.8.8`) for apt/curl while AdGuard DNS on `:53` is investigated. `.253` direct resolvers step awaiting user confirmation.
>   - sysadmin README/continuity/queue updated with current blocker state; no roster change; no new topics, agents, skills, or loops.

> [2026-07-23 06:18 CEST] context-factory tick completed
>   - Sysadmin session tail surfaces two additional Ad blocker findings on `.252`/`.253`: bcrypt hash mismatch on `.252` AdGuard config (401 on `/control/status`), and `.253` DNS timeout from outside (`192.168.10.253#53` UDP/TCP). Both appended to sysadmin continuity; queue item #4 updated with current blocker state.

> [2026-07-22 18:59 CEST] context-factory tick completed
>   - Sysadmin Discord session tail surfaces AdGuard HA `.253` compose install blocker: `docker.io` installs but compose plugin absent, `python3-pip` missing, `apt-get install` hangs intermittently; user executing manual install interactively.
>   - No new topics, skills, agents, or loops; fleet roster unchanged.
>   - sysadmin README/continuity/queue updated with blocker state; no [SKILLS]/[AGENTS]/[LOOPS] items added.

> [2026-07-22 16:15 CEST] context-factory tick completed
>   - Sysadmin session surfaces AdGuard HA .252/.253 deployment progress: Docker installed on both LXCs, compose/unbound configs drafted, user to apply and verify VIP failover.
>   - NUCBox Option B CPU pinning plan saved; Jellyfin AMD HW container recreate in progress.
>   - Box .104 inventory complete; CPU pinning script queued.
>   - Profile decision draft written (`general` retirement, `research` naming, NUCBox migration).
>   - `nexus-integration` profile archived.
>   - Sysadmin queue updated with 5 new action items; no new topics or roster drift.

> [2026-07-22 13:xx CEST] context-factory tick completed
>   - Discord session tail surfaces SIVE insider export blocker: user submitted 4 FI.SE `.csv` files for SIVE insider holdings; runtime inspection confirms all 4 are workbook/binary despite extension.
>   - Trading continuity/README updated; no queue change needed; parser fallback required (text export, screenshots/OCR, or runtime with spreadsheet parser).
>   - Fleet roster unchanged; no new topics, agents, skills, or loops.

> [2026-07-20 08:46 CEST] context-factory tick completed
>   - Scanned latest sessions for nous-girl, trading, sysadmin, ops, travel, integration: found no new identifiable project/entity/action items beyond ongoing factory traffic.
>   - `research` topic was the only active drift: row existed in fleet dashboard without a topic directory; removed.
>   - Integration queue exists without `README.md`; created scaffold `topics/integration/README.md`.
>   - No queue changes needed elsewhere; queues effectively empty.
>   - Fleet dashboard/recent activity updated with this tick entry; no roster change.

> [2026-07-20 01:38 CEST] context-factory tick completed
>   - Scanned latest sessions for nous-girl, trading, sysadmin, ops, travel, integration: found no new identifiable project/entity/action items beyond ongoing factory traffic.
>   - No topic README/continuity/queue changes needed; queues were effectively empty.
>   - Fleet dashboard/recent activity updated only with this tick entry; no roster change.

> [2026-07-21 22:17 CEST] context-factory tick completed
> [2026-07-21 15:07 CEST] context-factory tick completed
>   - AdGuard HA playbook vs runtime discrepancy surfaced from Discord sysadmin session `20260709_155620_f1fe9f90`: user asserts CT 252 on `.120` + CT 253 on `.51`; live Proxmox API shows CT 100 `adguardhome-primary` running on `.120`, CT 102 `adguardhome-backup` on `.51`, CT 252 stopped on `.120`, CT 253 absent.
>   - sysadmin README/continuity/queue updated; fleet dashboard watch item refreshed.

> [2026-07-21 10:00 CEST] context-factory tick completed
>   - `nous-girl` topic scaffold created (was missing from disk despite fleet dashboard reference).
>   - sysadmin continuity updated with memory architecture decision (vanilla Hermes memory + llm-wiki + Obsidian) and 12-point setup critique from user.
>   - sysadmin topology changes committed as `680b13d`: `power.md`, `cooling.md`, improvements playbooks (AdGuard HA repair, local Ollama embeddings, GitHub Actions mirror auth).
>   - Blockers retained: memory provider migration, vault pollution cleanup, tools-registry git mismatch, AdGuard HA failover, Discord webhook, MiniBox SSH, 9119 TUI bind, medical access control, duplicate-token, X post retrieval, Reddit megathread.

> [2026-07-21 07:46 CEST] context-factory tick completed
>   - Scanned latest sessions for nous-girl, trading, sysadmin, ops, travel, integration: found active vault-cleanup work in sysadmin Discord session `20260709_155620_f1fe9f90`.
>   - User directive: relocate Hermes runtime files out of `/opt/obsidian-vault/` root (`active_profile`, `chains.json`, `channel_directory.json`, `config.yaml`, `gateway_state.json`, `cron/`, `dev/`, `gbrain/`, `osb/`, `STATUS.md.bak.*`).
>   - Only dependency found: `mempalace-vault-recovery.md` references `/opt/obsidian-vault/dev/`.
>   - Conservative path proposed (doc fix + `.gitignore` update); full move pending approval.
>   - sysadmin README/continuity/queue updated; fleet dashboard watch item refreshed.

> [2026-07-25 15:10 CEST] context-factory tick completed
>   - Scanned sessions across all profiles: only new user-driven activity was in sysadmin Discord session `20260709_135620_af1dab49` tail (dashboard credentials question, model benchmark truthiness check).
>   - Sysadmin triage: 0 failed user services.
>   - New sysadmin queue item: Hermes dashboard auth lookup.
>   - No roster change; no new topics, agents, skills, or loops.

## Phantom / Drift Watch
- trading: `thesis-fit-review-last.md` status artifact present in loops dir but not promoted to registry pending explicit direction.
- integration: `nexus-integration` agent provisioned; `nexus-intel-sync` loop active — cleared.
- ops: `brain-heartbeat-recovery` and `vault-mirror-sync` marked stale/phantom; no recreation without approval.
- sysadmin: `vault-sync-push-trigger` and `cron-dependency-monitor` active after script restoration on 2026-07-22.
|- trading: `trading-watcher` marked resolved/phantom (duplicate claim); `trading-infra-watcher` recovered active (loops-factory 2026-07-26); `x-twitter-heartbeat` live/runtime-error — script missing (loops-factory 2026-07-27); agent summaries active.
- _global: `nous-girl-system` has per-turn loop doc and is active; loop-less anomaly cleared.

## Last loops-factory tick
- 2026-07-27 10:30 CEST — idle-tick maintenance; phantom-loop audit applied; x-twitter-heartbeat status corrected to live/runtime-error (Script not found); loop-registry row patched; loop doc rewritten with Actions Pending Approval; fleet-dashboard/watch annotations updated; catalogs synced; trading injection added; queues idle; no new artifacts or crons created.
- **2026-07-27 09:58 CEST** — idle-tick maintenance; phantom-loop audit applied; avanza-mcp-watchdog false recovery corrected to stale/phantom (cron `55c3a863d778` absent from all stores); portfolio-snapshot-daily status verified live/runtime-error with script execute-bit fix; loop-registry 29 rows == disk 29 loop docs; agent-roster 7 rows == disk 7 flat agents; topic-index counts match disk; no catalog drift found; queues idle; no new artifacts or crons created.

> [2026-07-23 11:52 CEST] context-factory tick completed
>   - Scanned newest sessions across nous-girl, trading, sysadmin, ops, travel: new identifiable activity in sysadmin Discord session `20260709_135620_af1dab49` regarding `.200`/`.201` AdGuard HA Docker LXCs on `.120`.
>   - sysadmin README/continuity/queue updated; fleet dashboard watch item refreshed.
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-24 18:32 CEST] context-factory tick completed
>   - Scanned newest cross-profile sessions: trading Discord `20260720_063611_b6abdce6` tail shows new artifacts (thesis-hoard origin docs, INDEX normalization, Nokia/ALL.SPACE notes, macro-tooling decision, reference notes batch) plus blockers (o2b CLI, NFS mirror, Playwright wrapper, bookmark dedupe, focus topic ingestion pending, OBDU discrepancy).
>   - trading/sysadmin README/continuity/queue updated; fleet dashboard watch item + active blockers refreshed.
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-24 20:49 CEST] context-factory tick completed
>   - Sysadmin Discord tail surfaces new findings: bookmark/repo dedupe completed (79 unique repos), phantom AdGuard watchdog cron `adguard-ha-watchdog` (job_id `8a7ab63c3e9b`) fired stale alert despite active cron `6a3e139bfc78` being healthy.
>   - sysadmin README/continuity/queue updated; fleet watch item refreshed.
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-25 12:56 CEST] context-factory tick completed
>   - Scanned sessions across all profiles: no new user-facing chats since last tick.
>   - Sysadmin triage: 0 failed user services; disk healthy (/home 41%, /tmp 2%).
>   - No queue changes; fleet roster unchanged; no new topics, agents, skills, or loops.

> [2026-07-26 01:38 CEST] context-factory idle tick completed
>   - Scanned newest sessions across nous-girl, trading, sysadmin, ops, travel: newest sessions are factory crons only; no new user-facing chats since prior tick.
>   - Preceding loops-factory tick (01:25 CEST) recovered 4 trading phantom crons: trading-infra-watcher, x-twitter-heartbeat, portfolio-snapshot-daily, avanza-mcp-watchdog; loop-registry expanded to 28 rows.
>   - Fleet Phantom/Drift Watch updated: trading x-twitter-heartbeat and trading-infra-watcher moved from stale/phantom to active; integration nexus-integration cleared (loop nexus-intel-sync active).
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-27 01:54 CEST] context-factory idle tick completed
>   - Scanned newest sessions across nous-girl, trading, sysadmin, ops, travel: newest sessions are factory crons only (01:32–01:52 CEST); no new user-facing narrative since prior tick (01:22 CEST).
>   - Queue scan: pre-existing open items remain in sysadmin and trading queues; no new [SKILLS]/[AGENTS]/[LOOPS] items appended.
>   - Disk–catalog verification: topic-index 10 rows, skill-registry 15 rows, agent-roster 7 flat agent docs, loop-registry 29 rows — all match disk. No malformed rows.
>   - Catalog drift detected after concurrent factory ticks: agent-roster.md, loop-registry.md, fleet-dashboard.md had drifted from live versions. Repaired by syncing catalogs/ to topics/_global/ canonical files.
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-27 16:17 CEST] context-factory tick
>   - Source: telegram session tail — user issued [Stop] to x-twitter-heartbeat cron output; removed cron job e0260ed247a1.
>   - Actions: trading queue x-twitter item marked [x]; trading loop doc status set removed; sysadmin loop doc marked resolved/superseded; loop-registry and fleet-dashboard updated; catalogs synced; continuity appended trading+sysadmin; brain log appended.
>   - No roster change; no new topics, agents, skills, or loops.

> [2026-07-28 04:15 CEST] context-factory idle tick completed
>   - Scanned newest sessions across nous-girl, trading, sysadmin, ops, travel: all factory-cron payloads only; no new user-facing chats since prior tick.
>   - Topic queues inspected: _global, dev, integration, nous-girl, openclaw, ops, sysadmin, system/orm, trading, travel. Zero open [SKILLS]/[AGENTS]/[LOOPS] items pending.
>   - Disk-catalog verification: 9 flat agents, 15 skills, 37 loop docs (excluding 7 factory-summary receipts) all match topic-index counts; no malformed rows; no catalog drift.
>   - Idle tail; no artifacts, queue entries, or profiles created.
