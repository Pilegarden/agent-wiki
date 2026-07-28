# nordnet-watchdog (deprecated)

- topic: `trading`
- status: **deprecated — superseded by avanza-mcp-watchdog**
- superseded-by: `trading/loops/avanza-mcp-watchdog.md`

## History

This file was originally created as a copy of `avanza-mcp-watchdog.md` during initial factory seeding. The original nordnet-watchdog concept (Nordnet screenshot-based price monitoring) was replaced by the Avanza MCP-based hard-stop watchdog before deployment.

The active loop is `avanza-mcp-watchdog` — hourly hard-stop breach checks via Avanza MCP for SIVE.

## Removal

To delete this file when confident no references remain: remove this file and cross-reference from both `_global/loop-registry.md` and `catalogs/loop-registry.md`.
