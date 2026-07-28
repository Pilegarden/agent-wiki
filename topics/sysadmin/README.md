# Sysadmin Topic — Human Dashboard

**Last updated:** 2026-07-27 10:24 CEST  \
**Status:** 🟡 Active ops — AdGuard HA .200/.201 direct host install active on VIP 192.168.10.254 (.250 MASTER/.251 BACKUP); keepalived/adguardhome-sync healthy; .251 direct SSH blocked awaiting manual sshd_config fix; legacy .252/.253 destroyed; NUCBox/Box.104/MiniBox inventory complete; hardware consolidation + topology revision in progress; `.251` web UI port changed to 6060 (awaiting operator decision).

## Active ops work
- **Vault pollution cleanup (2026-07-21):** User identified Hermes runtime files at vault root: `active_profile`, `chains.json`, `channel_directory.json`, `config.yaml`, `gateway_state.json`, `cron/`, `dev/`, `gbrain/`, `osb/`, plus `STATUS.md.bak.*`. Only dependency found: `mempalace-vault-recovery.md` references `/opt/obsidian-vault/dev/`. Conservative path = fix bad-pattern doc reference + update `.gitignore`; full move pending approval.
- **Hermes dashboard auth lookup (2026-07-25):** User asked for dashboard username/password. Inspect local Hermes webui/auth files (webui.ctl.env, webui.pid, dashboard-auth.log, profile webui_state) and document reset procedure if needed.

## Observed system state

|| **AdGuard HA playbook vs runtime discrepancy (2026-07-21 15:07 CEST)**
||- User asserts per AdGuard HA playbook: CT 200 is primary on `.120`, CT 201 is backup on `.51`.
||- Direct Proxmox API verification via `root@pam!monitoring` token on `.120`:
  - CT 100 `adguardhome-primary` is **running**.
  - CT 200 `adguard-200` exists but is **stopped**.
  - CT 201 does **not exist** on `.120`.
||- Direct Proxmox API verification on `.51`:
  - CT 200 and CT 201 do **not exist** on `.51`.
  - CT 102 `adguardhome-backup` is running.
||- **Finding:** Either the playbook IDs are stale, the LXCs were recreated with different IDs, or HA is operating on CT 100 + CT 102 despite the playbook naming convention. This needs operator confirmation before any failover/repair plan is updated.
||- **Resolved 2026-07-23:** Legacy bare-metal/AdGuard Docker stack on `.252`/`.253` fully retired. New active HA pair is `.200`/`.201` direct host install on `.120` PVE with keepalived VIP `192.168.10.254`.

|| Host filesystem `/home`: **194 GB total, 113 GB available, ~40% used**.
||- User systemd failed services (0):
  - None. `infra-health.service` is no longer in failed set; prior homelab infra findings (Unraid EXITED containers, MINIBOX unreachable, UniFi 403) continue but no longer reflected as a failed user service.
||- Inactive user services still pending decision, not newly failing:
  - `model-ranker.service`
  - `portfolio-briefing.service`
  - `portfolio-move-watcher.service`
  - `portfolio-refresh.service`
  - `xfab-watcher.service`
||- Active infrastructure services remain healthy:
  - `hermes-gateway-dev.service` — active
  - `hermes-dashboard.service` — active
  - `portfolio-dashboard-8000.service` — active

|| **MiniBox (`192.168.10.103`) homelab CPU/GPU mapping (2026-07-22 16:10 CEST)**
||- User clarified GPU/HW assignment: Plex uses Intel 12800H iGPU; NVIDIA GPU reserved for `frigate`, `immich`, `a-eye`.
||- Hybrid-aware CPU allocation proposal drafted: P-cores/iGPU 2-7 (Plex stack), NVIDIA services 8-11, ollama 12-13, media 14-17, light 18, monitoring 19. Exact P/E numbering requires live SSH to verify kernel CPU ordering.
||- Automated SSH auth blocked (`Permission denied` despite valid BSM password); interactive SSH works. Suspected local ssh-agent/identities mismatch between non-interactive and user shells. Blocks: live device report, Docker template patch, GPU/HW acceleration audit.

|| **Resolved infra findings (2026-07-22)**
||- AdGuard watchdog: script `/opt/data/.hermes/scripts/adguard-watch-minimal.sh` patched and verified `OK`; cron `6a3e139bfc78` delivering alerts to `discord:#sysadmin`.
||- Discord webhook: native GitHub webhook returned 400 on deliveries and was removed; GitHub Actions path (`discord-notify.yml` + repo secret `DISCORD_WEBHOOK_URL` in `Pilegarden/hermes-state`) verified end-to-end.
||- Cron path resolution: created `/home/hermes/.hermes/profiles/dev/scripts-local/`, populated with `vault-sync-trigger.sh` and `cron-monitor-wrapper.sh`; `vault-sync-push-trigger` (job_id 337fb9ff9a8a) and `cron-dependency-monitor` (job_id 7d390796d546) now `last_status=ok`.
||- AdGuard HA .200/.201 topology deployed and verified active on `192.168.10.254`; legacy `.252`/`.253` Docker LXC pair destroyed.

## AdGuard HA .200/.201 direct host install deployment (2026-07-23)
- **.200** (`192.168.10.250`, primary, keepalived MASTER): AdGuard active, `/control/status` → 200, VIP `192.168.10.254/24` on eth0, adguardhome-sync resident (origin → .251 replica), direct SSH works, dashboard blank fixed (`statistics.enabled: true`), 37 user rules migrated from legacy `.2`.
- **.201** (`192.168.10.251`, backup, keepalived BACKUP): AdGuard active, `/control/status` → 200, direct SSH blocked by sshd_config (`PermitRootLogin`/`PubkeyAuthentication` disabled; manual `sed` fix required from .251 console).
- **keepalived**: MASTER priority 150 on .200, BACKUP priority 100 on .201, VIP `192.168.10.254/24`.
- **adguardhome-sync v0.9.2**: resident on .250; config points to .251; replication verified successful.
- **Next**: verify .251 sync replication after gateway restart; enable .251 direct SSH; test VIP failover; consider .51 pve-sff recovery after `bridge fdb flush` outage; verify Discord streaming/progress is visible to user.

## NUCBox (`192.168.10.13`) CPU pinning + Jellyfin AMD HW
- CPU pinning plan saved at `/mnt/obsidian-vault/sys/homelab/minibox/nucbox-cpu-pinning-2026-07-22.md`.
  - Hermes: 6 vCPUs on 1,9,2,10,3,11; SteamOS: 6 on 4,12,5,13,6,14; Docker: 7,15; host reserved 0,8.
- Jellyfin: stale container `newjellyfin` removed; user recreating with `--device=/dev/dri` and AMD VCN to be enabled in UI.

## Box .104 (`192.168.10.104`) inventory and pending CPU pinning
- Inventory complete: 6C/12T, 31GB RAM, 21 storage devices, 10 Docker containers (Gitea, Dozzle, Glances, etc.), no VMs/GPU.
- Next: CPU pinning script pending.

## Profile decisions draft
- `general` retirement, `research` naming, NUCBox migration candidates drafted at `/mnt/obsidian-vault/topics/hermes/profiles/profile-decision-draft-2026-07-22.md`.
- `nexus-integration` profile archived to `/home/hermes/.hermes/profiles/_archive/nexus-integration/`.

## OSB / MCP infra milestone (2026-07-13)

- Open Second Brain MCP servers added to **all 13 Hermes profiles** (reader + writer), with per-profile config blocks (no longer relying on root inheritance).
- 8 previously corrupted `config.yaml` profiles repaired mechanically (YAML parse errors); backups preserved as `.bak.20260713_*`.
- Dev gateway restarted → new PID `2039915` confirmed live with OSB writer connected (5 `brain_*` tools).
- Live `brain_note` write succeeded at 20:48:22Z → OSB directive now on real path; manual Brain log fallback retired.

## Profile consolidation question (2026-07-13 CLI session)

- User discussed merging `dev`/`trading`/`sysadmin` profiles vs keeping separate.
- Relevant files:
  - `/home/hermes/.hermes/profiles/{dev,trading,sysadmin,hoarding,general,...}/config.yaml`
  - `/home/hermes/.config/systemd/user/hermes-gateway-dev.service` (HERMES_HOME pin)
  - `/srv/trading/` (portfolio data root)
- No decision recorded; deferred to user.

## `.251` AdGuard web UI port override (2026-07-25 20:42 CEST)
- Source: Discord session `20260709_135620_af1dab49` tail.
- `.251` AdGuard is running and listening on `80`/`53`, but the HTTP UI moved to port `6060` per `/opt/adguard/conf/AdGuardHome.yaml`. User observed dashboard inaccessible this afternoon and asked why the port differs from morning.
|- **Action needed:** operator decision — revert `http.port` to `80` or document the new `192.168.10.251:6060` access path.

## Hermes VM Tailscale subnet route (2026-07-26 ~10:12 CEST)
|- Source: Discord sysadmin session `20260709_135620_af1dab49` tail.
|- User wants Tailscale clients (phone) to reach `192.168.10.254` and the LAN through the Hermes VM.
|- Planned config on Hermes VM:
  - `net.ipv4.ip_forward = 1`
  - `net.ipv6.conf.all.forwarding = 1`
  - `tailscale up --advertise-routes=192.168.10.0/24 --accept-dns=false`
|- Note written to `/opt/obsidian-vault/sys/homelab/topology/tailscale-hermes-subnet-route.md`.
|- Status: pending operator approval to apply subnet route and accept the subnet in Tailscale admin console.

## Home Assistant long-lived token stored in BWS (2026-07-26 ~10:12 CEST)
|- Source: Discord sysadmin session `20260709_135620_af1dab49` tail.
|- User shared a Home Assistant long-lived token in chat; assistant stored it in Bitwarden Secrets Manager.
|- Secret ID: `b51f617c-686c-4804-bef9-b49300859112`
|- Project: `9a9c37f3-769f-471c-8143-b47a01347781`
|- Key: `homelab/home-assistant/jarvis-long-lived-token`
|- Action needed: rotate this token in Home Assistant since it was shared in chat prior to storage. Use BWS as the canonical source going forward.
|- User directive: future sessions must use BWS/BSM to push secrets, not paste them in chat.

## Failed-service triage

### infra-health.service
- Findings remain unchanged across Jul 10–13: Unraid EXITED containers, MINIBOX unreachable, UniFi 403.
- **Diagnosis:** real infrastructure findings from `infra-health-check.py`, not cron/timer/path breakage.
- **Status:** awaiting infra remediation or explicit ops direction; no script-level fix available.

### resolved / deferred items
- model-ranker ENOSPC — RESOLVED 2026-07-13 12:28.
- portfolio-briefing path mismatch — RESOLVED 2026-07-13 12:28.
- watchdog missing scripts/timers — disabled system-wide 2026-07-13 12:28; absent from user scope 2026-07-13 16:02.

## Blockers
- UniFi 403 / account or API lock state blocks gateway telemetry but not scripting.
- Unraid container exits / MINIBOX connection refused are ongoing infra degradation.
- Elevated swap pressure remains; monitor host memory pressure independently of filesystem capacity.

## .134/.74 topology and Docker incident (2026-07-14)

- `.134` (`192.168.10.134`) is the main Hermes host; core currently runs **native** (`python server.py`, ports 8000/8001/8081/8082/8012/8013, no systemd wrapper yet).
- `.74` (`192.168.10.74`) is now an **ops/troubleshooting node** for `.134` only. It does not run Hermes core.
- A prior recovery session from `.74` agent **Dockerized `.134`** via `/opt/hermes/docker-compose.yml` using `network_mode: host` + rw-bind of `~/.hermes`; this created SQLite corruption risk and was rolled back.
- Active Docker services that should stay containerized: crawl4ai, langfuse/postgres, searxng/groktocrawl, valkey, hermes-webui.
- Known-good recovery rule: gateway failure → restart / redeploy known-good / restore NAS backup. **Never** change deployment model mid-incident.
- Pending hardening: systemd --user unit for `.134` gateway; hermes-webui mount to `ro`; retire `/opt/hermes/docker-compose.yml` from active path; `.74` health-probe/alert runbook.

## Phantom AdGuard watchdog cron alert (2026-07-24)
- `adguard-ha-watchdog` (claimed job_id `8a7ab63c3e9b`) fired a Discord alert stating `/opt/data/.hermes/scripts/adguard-watch-minimal.sh` does not exist (exit 127).
- The script currently exists at that path (owner root:root, 234 bytes).
- The claimed job ID is absent from all Hermes profile cron stores; this is a phantom/legacy cron output reinjecting into Discord.
- The active healthy watchdog is cron `6a3e139bfc78` delivering alerts to `discord:#sysadmin`.
- **Action needed:** clean up or suppress the phantom watchdog cron/output to stop stale alerts.

## Tooling + hoarding catalog work (2026-07-24)
- **Hoarding catalog analysis complete**: 68 repos total (6 ADOPT/installed, 14 EXTRACT, 30 DEFER, 10 SKIP).
  - Promoted/verified installs: `markitdown` ✅, `codegraph` ✅ (source build at `/opt/codegraph`), `fredapi` 0.5.2 ✅.
  - `browser-use` PyPI package rejected/withdrawn; replacement is native Playwright wrapper.
  - `SkillOpt`/`gbrain` integration claim cleared as stale/not exposed.
  - `feedoracle-macro-mcp` deferred; `macro_reporter.py` migrate path chosen → `fredapi`.
- **Reference notes batch written** to `/opt/obsidian-vault/tools-registry/incoming/`:
  - `reference-hkuds-vibe-trading.md`
  - `reference-google-gemini-cli.md`
  - `reference-bytebytego-system-design-101.md`
  - `reference-joshu-oss-ag-ui-copilotkit.md`
- **Decision note**: `/opt/obsidian-vault/research/trading/macro-tooling-decision-2026-07-24.md` captures the fredapi migration and deferred feedoracle-macro-mcp.
- **New blockers**:
  - `o2b` CLI broken (`/home/hermes/.hermes/profiles/dev/plugins/open-second-brain/scripts/o2b` exits 1); Brain notes written via terminal Python fallback until binary fixed.
  - NFS mirror permissions on `/mnt/obsidian-vault` (Box `.104` export) block `rsync --delete`; mirror remains one-way or manual until export permissions fixed.
  - **New artifacts**:
  - `all-repos-deduped-20260720.md` (79 unique repos)
  - `repo-catalog-evaluated-2026-07-24.md` (ADOPT/EXTRACT/DEFER/SKIP with evidence-backed why/why-not rationale)
  - Playwright wrapper not yet provisioned on `.205`; `browser-use` runtime remains uninstalled.
|- System state (this tick): 0 failed user services; `/home` 77G used / 110G free (42%); `/tmp` 1% used. No ENOSPC.

## Hardware inventory + consolidation (2026-07-26–27)
- Completed per-host inventory docs under `/opt/obsidian-vault/sys/homelab/inventory/`: `pve.md` (.120), `pve-sff.md` (.51), `nucbox.md` (.13), `minibox.md` (.102/.103), `box.md` (.104).
- Completed hardware roadmap with 8 bottleneck write-ups (`hardware-roadmap.md`).
- RAM-constrained consolidation decision documented: keep NUCBox `.13` as lean Hermes box (16 GB), new NUCBox 64 GB for gaming/arrs/media, MiniBox `.103` for NVIDIA AI/Hermes fallback. Decision docs: `ram-constrained-consolidation-2026-07-27.md` and `recommended-topology-2026-07-27.md`.
- Arc A580 + RX 6600 XT + 10GbE planned for new NUCBox via PCIe bifurcation; topology revised with 3×10GbE congestion guardrails.
- MiniBox ZFS Docker migration analysis: keep ZFS for appdata, move Docker data-root to `/mnt/scratch/docker` on XFS with `overlay2` driver. Analysis doc: `unraid-zfs-docker-migration-analysis-2026-07-26.md`.

## Home Assistant inspection (2026-07-26)
|- HA Core `2026.7.0b2` (update `2026.7.4` available); Supervisor `2026.07.4`; error log empty.
|- 346 entities, 19 automations, 9 scenes, 108 sensors, 8 media players.
|- Integrations include frigate, reolink, music_assistant, zha, assist_satellite, conversation, assist_pipeline, wake_word, yeelight, mqtt, thread, dhcp, backup, hacs, cloud, webhook, remote.
|- Long-lived token stored in BWS (secret ID `b51f617c-...`); rotation required because token was shared in chat before storage.

## Unraid ZFS Docker migration analysis (2026-07-26)
|- Subject: MiniBox `.103` stuck container (`jellystat-postgresql15`) due to ZFS `dataset is busy` phantom reference.
|- Verdict: keep ZFS for Cache pool + bind-mounted appdata; move Docker `data-root` to `/mnt/scratch/docker` on XFS with `overlay2` driver.
|- All real container data is bind-mounted, so data-root wipe is safe. Named volumes `flaresolverr` and `plex-auto-languages` are low-value/recreatable.
|- Analysis doc: `unraid-zfs-docker-migration-analysis-2026-07-26.md`.

## Tailscale subnet route (2026-07-26)
|- Planned: Hermes VM advertises `192.168.10.0/24` so phone clients can reach `192.168.10.254` and LAN.
|- Status: subnet advertisement attempted; `accept-routes=true` blocked by approval policy; pending admin approval in Tailscale console.

## `.251` AdGuard direct SSH blocked
|-- sshd_config on `.251` disables `PermitRootLogin`/`PubkeyAuthentication`; manual console fix required.
|- `.251` web UI moved to port `6060` per `/opt/adguard/conf/AdGuardHome.yaml` (was `80`); operator decision pending on whether to revert.

## MiniBox automated SSH auth
|- Interactive SSH works; automated/scripted SSH returns `Permission denied` despite valid BSM password.
|- Suspected ssh-agent/identities mismatch between non-interactive and user shells.
|- Blocks: exact CPU core verification, Docker template patch, GPU/HW acceleration audit.

