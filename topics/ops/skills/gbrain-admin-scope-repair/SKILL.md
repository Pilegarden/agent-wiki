---
name: gbrain-admin-scope-repair
description: Restore admin scope for gbrain MCP heartbeat when `mcp__gbrain__get_status_snapshot` returns `insufficient_scope`. Use when gbrain MCP calls fail with auth/scope errors, bearer token lacks `admin`, or the heartbeat probe is blocked by scope mismatch.
---

# gbrain-admin-scope-repair

Fix the gbrain MCP admin-scope breakage that blocks `mcp__gbrain__get_status_snapshot`.

## Contract (must be true before starting)
- gbrain HTTP server is reachable at `127.0.0.1:12787` (`/mcp`).
- `/home/hermes/.bun/bin/gbrain` is available and is `garrytan/gbrain`, not `stormcolor/gbrain`.
- Bearer token source of truth is `/home/hermes/.gbrain_mcp_bearer.txt` (`chmod 600`).
- Ops profile allows restarting `gbrain serve --http`.
- This skill edits MCP/module config files but does not touch `config.yaml`, provider credentials, or other profiles.

## When to use
- `mcp__gbrain__get_status_snapshot` returns `insufficient_scope`.
- gbrain MCP logs show `admin` required.
- Heartbeat/daemon is healthy, but MCP tool calls are blocked on scope.

## Diagnosis
```bash
# Show token presence and permissions
ls -l /home/hermes/.gbrain_mcp_bearer.txt
grep -R -n "mcp__gbrain__get_status_snapshot\|insufficient_scope\|admin" \
  /home/hermes/.hermes /home/hermes/.gbrain /home/hermes/.bun/bin/gbrain /tmp 2>/dev/null | head -80

curl -sS http://127.0.0.1:12787/health || echo 'GBRAIN_HEALTH_FAIL'
```

## Repair procedure
1. Confirm daemon health: `curl -sf http://127.0.0.1:12787/health` must return 200.
2. Inspect current scope and subcommand behavior with safe read-only commands:
   - `/home/hermes/.bun/bin/gbrain auth inspect`
   - `/home/hermes/.bun/bin/gbrain auth parse --bearer-file /home/hermes/.gbrain_mcp_bearer.txt || true`
   - `/home/hermes/.bun/bin/gbrain mcp cap --maintenance-dry-run`
3. Add `admin` to the allowed scopes for the gbrain MCP server config. If an allowlist/scoping field exists, add `admin`.
4. Restart the gbrain HTTP daemon in background with explicit elevated scopes.
5. Verify restoration: heartbeat must return `last_status: ok` and tool calls must succeed without `insufficient_scope`.

## Verification
- One success sample for `mcp__gbrain__get_status_snapshot`.
- Re-run ops heartbeat: no `insufficient_scope`.
- Re-run failure-sample scenario: expectation now succeeds.

## Rollback
- Restore the previous MCP/server config from backup.
- Restart daemon.
- Re-run verification.

## Known pitfalls
- `gbrain serve --http` restart without approval is forbidden unless the ops skill grants it.
- If `insufficient_scope` persists after restart, the bearer token may have been regenerated without `admin`; update token source of truth and retry.
- Some distro shells break Bun if embedded control characters appear; keep wrapper lifecycle short and capture logs to `/tmp`.
