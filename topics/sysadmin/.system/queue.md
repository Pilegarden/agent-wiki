## [OPS] pending manual triage
- [ ] vault-root runtime pollution cleanup — move `active_profile`, `chains.json`, `channel_directory.json`, `config.yaml`, `gateway_state.json`, `cron/`, `dev/`, `gbrain/`, `osb/`, `STATUS.md.bak.*` out of `/opt/obsidian-vault/`; update `.gitignore` + dependent refs (only `mempalace-vault-recovery.md` found); conservative path = doc fix + gitignore, full move pending approval.
- [ ] tools-registry git status mismatch — `tools-registry/` files reported committed/pushed to `burtgit/hermes-state.git` main but show as untracked in local vault `git status` at `/opt/obsidian-vault/`; root cause unverified; queue repair.
|- [ ] AdGuard HA .200/.201 direct host install — deployed on `.120` PVE (CT 200=192.168.10.250 primary, CT 201=192.168.10.251 backup). Direct host install (no Docker); keepalived MASTER/.200 prio 150, BACKUP/.201 prio 100, VIP `192.168.10.254/24`. adguardhome-sync resident on .250; config points to .251. **Remaining:** copy block lists from legacy .252 to .200; verify sync replication .250→.251; .251 direct SSH blocked by sshd_config (`PermitRootLogin`/`PubkeyAuthentication` disabled, manual console fix required); test VIP failover; legacy .252/.253 destroyed prior Docker LXC HA pair retired.
|- [ ] `.51` (`pve-sff`) PVE host unreachable since `bridge fdb flush dev vmbr0` — blocks `.51`-managed ops and `.253` access; requires local/KVM or `.120` node reboot access.
- [x] Discord webhook delivery verification — verified via GitHub Actions path (`discord-notify.yml` + repo secret); native GitHub webhook returned 400 and was removed; Actions path remains viable.
- [ ] MiniBox SSH auth resolution — required before Hybrid CPU allocation plan and Docker template patch can proceed. Blocked: automated SSH returns `Permission denied` despite valid BSM password; user-local interactive SSH works; session-level ssh-agent/identities interference suspected. New: GPU/HW mapping known (Plex iGPU, NVIDIA services = frigate/immich/a-eye); revised CPU set proposal drafted pending exact P/E core verification.
- [ ] 9119 TUI bind repair — Hermes dashboard TUI bind broken; repair pending.
- [ ] Medical research access control decision — pending approval on access model.
- [ ] Duplicate-token analysis finalization — from gateway token audit; complete remaining token mapping and remediation.
- [ ] X post body retrieval for `2078972949483454619` — blocked by no headless browser on hermesvm.
- [ ] Reddit megathread `1t6gf4j` retrieval — inaccessible via all methods; blocked.
- [ ] NUCBox CPU pinning apply — Option B plan saved at `/mnt/obsidian-vault/sys/homelab/minibox/nucbox-cpu-pinning-2026-07-22.md`; user to run virsh + docker repin script.
- [ ] NUCBox Jellyfin AMD HW transcoding — recreate container with `--device=/dev/dri`, bind correct volumes, enable VCN in UI.
- [ ] Box .104 CPU pinning script — inventory complete (6C/12T, 21 disks, 10 containers); script pending.
- [ ] Profile decisions — `general` retirement, `research` naming, NUCBox migration; draft at `/mnt/obsidian-vault/topics/hermes/profiles/profile-decision-draft-2026-07-22.md`.
- [ ] portfolio.json refresh — stale since 2026-07-17; reconcile Nordnet exposure.
- [x] Dedupe 127 bookmark-derived repos against 68-repo hoarding catalog (`tools-registry/incoming/hoarding-github-catalog-detailed-20260720.md`). Result: 79 unique repos written to `all-repos-deduped-20260720.md`.
|- [ ] Restore `o2b` CLI so Brain note creation works (current binary broken; terminal Python fallback used).
|- [ ] Provision Playwright wrapper on `.205` to replace `browser-use` PyPI runtime.
|- [ ] Fix NFS root-owned file permissions on `/mnt/obsidian-vault` (Box `.104` export) to enable primary → secondary vault mirror.
||- [ ] Evaluate remaining EXTRACT hoarding candidates: markitdown ✅, codegraph ✅, fredapi 0.5.2 ✅, feedoracle-macro-mcp (deferred), others — promote/install or finalize DEFER/SKIP per catalog rules. Completed in `/opt/obsidian-vault/tools-registry/incoming/repo-catalog-evaluated-2026-07-24.md`.
||- [ ] Clean up phantom AdGuard watchdog cron `adguard-ha-watchdog` (job_id `8a7ab63c3e9b`) — stale alert fired for `/opt/data/.hermes/scripts/adguard-watch-minimal.sh`; job absent from all profile cron stores; remove/suppress output so Discord is not noisy.
||- [ ] Inspect graylog on `.120` PVE CT 105 — verify systemd/docker/port 9000/JAVA/disk; user issued `pct enter 105 -- bash -lc '...'` which hit arg parsing error; shorter command provided, awaiting user output.
- [ ] `.51` (`pve-sff`) PVE host unreachable since `bridge fdb flush dev vmbr0` — blocks `.51`-managed ops and `.253` access; requires local/KVM or `.120` node reboot access.
- [ ] `.251` AdGuard web UI port decision — `http.port` currently `6060` on `.251` (was `80`); user observed dashboard inaccessible this afternoon; need decision to revert to `80` or document new path. Config: `/opt/adguard/conf/AdGuardHome.yaml`.
## [SKILLS] items
- [x] `systemd-recover-missing-script`
## [LOOPS] items
- [x] Brain MCP heartbeat scope: `get_status_snapshot` returns `insufficient_scope` (`admin` required, only `read`/`write` granted). Rewrite heartbeat to a `read`-level status call or grant `admin` scope before re-enabling automated health snapshot.
<!-- skills-factory receipt 2026-07-15T11:54:23.486497+02:00: inspected queue sysadmin; no open [SKILLS]; no skills created; queue metadata appended -->
<!-- skills-factory receipt 2026-07-15 19:01 CEST: inspected queue sysadmin; no open [SKILLS]; no skills created; queue metadata appended -->

<!-- skills-factory receipt 2026-07-20 01:16 CEST: inspected queue; no open [SKILLS]; idle-tick skill-registry/topic-index/fleet-dashboard drift repaired; catalogs synced -->
<!-- skills-factory receipt 2026-07-20 07:16 CEST: inspected queue sysadmin; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced, queue metadata appended -->
<!-- skills-factory receipt 2026-07-20 03:29 CEST: inspected queue sysadmin; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, skill-registry malformed rows repaired; catalogs synced -->
<!-- skills-factory receipt 2026-07-20 04:52 CEST: inspected queue; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced, queue metadata appended --><!-- skills-factory receipt 2026-07-20 07:46 CEST: inspected queue sysadmin; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced -->
<!-- loops-factory receipt 2026-07-20 08:27 CEST: inspected queue sysadmin; no open [LOOPS]; phantom-loop audit applied; queues metadata appended; no new artifacts or crons created -->

<!-- loops-factory receipt 2026-07-20 09:34 CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; queue metadata appended; no new artifacts or crons created --><!-- loops-factory receipt 2026-07-20 09:34 CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; queues metadata appended; no new artifacts or crons created -->

<!-- skills-factory receipt 2026-07-20 10:36 CEST: inspected queue; no open [SKILLS]; no skills created; idle-tick counts verified against disk, catalogs checked -->
<!-- loops-factory receipt 2026-07-20 14:29 CEST: inspected queue sysadmin; no open [LOOPS]; phantom-loop audit applied; rebuilt missing docs for vault-sync-push-trigger and cron-dependency-monitor as live/runtime-error with pending approval; idle-tick loop-registry malformed rows repaired and catalogs synced --><!-- loops-factory receipt 2026-07-20 19:xx CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; loop-registry runtime-error/live-state notes refreshed; queues metadata appended -->
<!-- context-factory receipt 2026-07-21 02:23 CEST: inspected queue sysadmin; queue idle; Brain admin scope breaker still open; no new [SKILLS]/[AGENTS]/[LOOPS] items; README and continuity refreshed with latest systemd/disk state -->

<!-- loops-factory receipt 2026-07-22 07:10 CEST: inspected queue sysadmin; no open [LOOPS]; phantom-loop audit applied; loop-registry malformed rows repaired; vault-sync-push-trigger and cron-dependency-monitor updated to active after script restoration; catalogs synced; queue metadata appended -->

- [x] `.200` AdGuard YAML fix — `!!seq into string` at line 20 of `/opt/adguard/conf/AdGuardHome.yaml` blocks restart; fix schema so service reaches `active` and `/control/status` returns 200.
- [x] `.201` AdGuard API stability verification — confirm `/control/status` returns 200 consistently with configured credentials; verify VIP failover behavior.
- [x] keepalived VIP failover test — VIP `192.168.10.249` currently on `.200` MASTER; simulate `.200` failure and confirm `.201` takes VIP.
- [x] adguardhome-sync schema compatibility — dry-run fails on both due to outdated schema; review config schema for v0.9.2 compatibility and test sync `.200` → `.201`.
<!-- loops-factory receipt 2026-07-24 04:51 CEST: inspected queue sysadmin; [BREAKER] Brain MCP heartbeat scope still open (unclaimed); phantom-loop audit applied; loop-registry rebuilt canonical (26 rows); catalogs synced; no new artifacts or crons created -->
|- [x] Hermes dashboard auth lookup — user asked for dashboard username/password; inspect local Hermes webui/auth files and document where credentials are set/reset.
||- [x] Tailscale subnet route on Hermes VM — apply subnet route + accept in Tailscale admin console so phone clients reach `192.168.10.0/24` via Hermes VM. Note saved to `/mnt/obsidian-vault/sys/homelab/topology/tailscale-hermes-subnet-route.md`.
||- [x] MiniBox RAM upgrade + consolidation decision — NUCBox `.13` retains 64 GB; MiniBox `.103` should upgrade to 64 GB DDR5 + Arc A580 if keeping AI/Hermes role. Decision doc: `/mnt/obsidian-vault/sys/homelab/improvements/ram-constrained-consolidation-2026-07-27.md`.
||- [x] Rotate Home Assistant long-lived token — token was shared in Discord chat before being stored to BWS secret `homelab/home-assistant/jarvis-long-lived-token`; rotate in HA UI and use BWS as canonical source.
||- [x] BWS-first secret handling — enforce BWS/BSM secret push in active sysadmin sessions; never paste live tokens in chat.

|- [x] x-twitter-heartbeat empty payload investigation — script `/home/hermes/.hermes/scripts/x-twitter-heartbeat.sh` restored and smoke-tested 2026-07-27; Spectre `get_bookmarks` returned 0 records at test time. Verify Spectre token/auth/endpoint and whether bookmark state is exhausted or retrieval path regressed.
<!-- loops-factory receipt 2026-07-27T13:38:00+02:00: inspected queue sysadmin; 5 [LOOPS] claimed and drafted as manual loop docs (Tailscale, MiniBox, HA token, BWS, x-twitter investigation); loop-registry full canonical rewrite 37 rows; topic-index and fleet-dashboard counts updated; catalogs synced; queue metadata appended -->

<!-- agents-factory receipt 2026-07-28 06:03 CEST: inspected queue; no open [AGENTS]; idle-tick agent-roster/topic-index/fleet-dashboard counts verified against disk=9; no malformed rows; catalogs in sync; no new artifacts or profiles created -->
