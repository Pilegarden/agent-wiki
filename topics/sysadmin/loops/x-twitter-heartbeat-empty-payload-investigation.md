# x-twitter-heartbeat-empty-payload-investigation

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `x-twitter-heartbeat empty payload investigation`
|- status: **resolved/superseded** — user removed cron `e0260ed247a1` via [Stop] at 2026-07-27 16:06 CEST; investigation no longer applies.
- mode: manual
- deliver: local

## Scope

Investigate why `x-twitter-heartbeat.sh` returns 0 bookmarks from Spectre
`get_bookmarks` after the script was restored and smoke-tested on 2026-07-27.
Distinguish between token/auth expiry, endpoint regression, and exhausted
bookmark state.

## Context

- Script path: `/home/hermes/.hermes/scripts/x-twitter-heartbeat.sh`
- Cron job `e0260ed247a1` in trading topic has a separate runtime-path issue
  (`Script not found: /home/hermes/.hermes/profiles/dev/scripts-local/...`);
  this investigation covers the script logic/state itself, not cron path-resolution.

## Steps

1. Run script manually with verbose/debug flags if supported.
2. Inspect `SPECTRE_*` env vars / config for token/auth validity (not logged).
3. Confirm endpoint URL and HTTP method in script.
4. Check `processed_bookmarks.json` or equivalent state for exhaustion.
5. Test a known bookmark ID / state via Spectre MCP directly to rule out platform-side issue.
6. Record root cause and remediation in loop doc.

## Safety

Do not log or echo tokens/API keys. Use BWS/BSM for any credential rotation needed.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
