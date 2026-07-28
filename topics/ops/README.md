# Operations

Hermes ops, cron health, knowledge-system health, watchdogs, systemd recovery.

## Status
🟡 Partial — host healthy, but gbrain MCP heartbeat DOWN.

## Active Issues
- Brain heartbeat reports MCP gbrain DOWN.
  -  returns , then unreachable after 4 consecutive failures.
  - Possible causes: gbrain HTTP daemon not running on this host, admin-scope bearer missing or revoked, conda-plugin host blocker.
- Factory queue tickets open for  and .

## Notes
-  NAS migration succeeded on 2026-07-13/14 but host deletion was blocked by approval gate.
- Vault mirror sync (cron `87e93b77a514`): fixed local git identity in session; commit succeeded (`65a05fd`). Push still fails: `error: Push to create is not enabled for users.` `fatal: Could not read from remote repository.` -> remote-side permission/policy/SSH user state on `git@192.168.10.104:burtgit/hermes-backup.git`.
- gbrain MCP heartbeat narrowed: `mcp__gbrain__get_status_snapshot` returns `insufficient_scope`; current scopes `read,write`; requires `admin` scope. Past `DOWN` remains true and diagnosis is now precise.
- agents/skills factories both reported no queue files found under `topics/*/.system/queue.md` or `~/.hermes/.system/queue.md`; no [AGENTS]/[SKILLS] work emitted this tick.
