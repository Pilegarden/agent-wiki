## [SKILLS] items
_(none)_

## [LOOPS] items
- [x] discord-preview-watchdog — verify `tool_preview_length`, `tool_progress_command`, and `streaming` actually surface Hermes command/action output in Discord after gateway restarts.
- [x] adguard-home-sync — monitor connectivity from `.250` → `.251:80`; alert when sync fails after ARP/routing fixes.
- [x] config-edit-verifier — detect when Hermes profile config edits are blocked by file mutation verifier and report the exact fallback path (`hermes config set` or `~/.hermes/config.yaml`).

## [AGENTS] items
- [x] dev-ops-helper — read-only ops helper for PVE/LXC/AdGuard triage.
- [x] vault-sync-checker — verify vault sync health and NFS permission drift on `/mnt/obsidian-vault`.

<!-- loops-factory receipt 2026-07-27T12:15:00+0200: inspected queue dev; seeded [LOOPS], [AGENTS], [SKILLS]; queue metadata appended -->


<!-- agents-factory receipt 2026-07-28 06:03 CEST: inspected queue; no open [AGENTS]; idle-tick agent-roster/topic-index/fleet-dashboard counts verified against disk=9; no malformed rows; catalogs in sync; no new artifacts or profiles created -->
