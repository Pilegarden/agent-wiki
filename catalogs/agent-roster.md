---
title: Agent Roster
created: 2026-07-12
updated: 2026-07-28T15:04+02:00
type: catalog
tags: [goop, agents, roster]
---

# Agent Roster

| Agent | Topic | Wiki Path | Loop | Status |
|---|---|---|---|---|
| [trading-infra-watcher](../trading/agents/trading-infra-watcher.md) | `trading` | `topics/trading/agents/trading-infra-watcher.md` | [trading-infra-watcher](../trading/loops/trading-infra-watcher.md) — cron `b5aa5e1f418c` (active) | Active (profile missing) |
| [trading-watcher](../trading/agents/trading-watcher.md) | `trading` | `topics/trading/agents/trading-watcher.md` | none — resolved/superseded | Active |
| [nexus-integration](../integration/agents/nexus-integration.md) | `integration` | `topics/integration/agents/nexus-integration.md` | [nexus-intel-sync](../integration/loops/nexus-intel-sync.md) — cron `da64be0fe62c` live/runtime-error | Active |
| [nexus-integration](../_global/agents/nexus-integration.md) | `_global` | `topics/_global/agents/nexus-integration.md` | [nexus-intel-sync](../integration/loops/nexus-intel-sync.md) — cron `da64be0fe62c` live/runtime-error | Active |
| [openclaw-system-agent](../openclaw/agents/openclaw-system-agent.md) | `openclaw` | `topics/openclaw/agents/openclaw-system-agent.md` | [cc-170-mandate-reconciler](../openclaw/loops/cc-170-mandate-reconciler.md) — cron `f9aefeca065b` | Active |
| [dev-ops-helper](../dev/agents/dev-ops-helper.md) | `dev` | `topics/dev/agents/dev-ops-helper.md` | none — pending [LOOPS] direction | Active |
| [vault-sync-checker](../dev/agents/vault-sync-checker.md) | `dev` | `topics/dev/agents/vault-sync-checker.md` | none — pending [LOOPS] direction | Active |
| [orm-governance-agent](../system/orm/agents/orm-governance-agent.md) | `system/orm` | `topics/system/orm/agents/orm-governance-agent.md` | [orm-mandate-reconciler](../system/orm/loops/orm-mandate-reconciler.md) — cron `97aff819f7ca` | Active |
| [nous-girl-system](../_global/agents/nous-girl-system.md) | `_global` | `topics/_global/agents/nous-girl-system.md` | [nous-girl-system](../_global/loops/nous-girl-system.md) | Active |

→ SOUL.md: `~/.hermes/profiles/nous-girl/SOUL.md`

## Creating an Agent

- **Automatic:** Context → queue → Agents provisions from `[AGENTS]` queue items.
- **Manual:** Edit `topics/_global/.system/queue.md` and add under `## [AGENTS] items`.
