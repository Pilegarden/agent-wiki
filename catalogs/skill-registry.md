---
title: Skill Registry
created: 2026-07-12
updated: 2026-07-28T14:06 CEST
type: catalog
tags: [goop, skills, registry]
---

# Skill Registry

| Skill | Topic | Wiki Path | Used By |
|---|---|---|---|
| portfolio-snapshot-report | trading | topics/trading/skills/portfolio-snapshot-report.md | trading-watcher |
| x-twitter-ocr-pipeline | trading | topics/trading/skills/x-twitter-ocr-pipeline.md | x-twitter-heartbeat |
| nexus-integration | integration | topics/integration/skills/nexus-integration.md | integration workflows |
| nexus-integration | _global | topics/_global/skills/nexus-integration.md | fleet mirror |
| gbrain-admin-scope-repair | ops | topics/ops/skills/gbrain-admin-scope-repair/SKILL.md | ops loops |
| thesis-fit-review-skill | trading | topics/trading/skills/thesis-fit-review-skill/SKILL.md | thesis-fit review |
| tweet-media-ocr-mandate | trading | topics/trading/skills/tweet-media-ocr-mandate/SKILL.md | tweet-media-ocr-mandate |
| paper-digest | _global | topics/_global/skills/paper-digest/SKILL.md | fleet digest |
| price-board | _global | topics/_global/skills/price-board/SKILL.md | fleet price view |
| sirvir-fleet-manager-research-sweep | _global | topics/_global/skills/sirvir-fleet-manager-research-sweep/SKILL.md | fleet research |
| cc-170-system-mandate-review | openclaw | topics/openclaw/skills/cc-170-system-mandate-review.md | cc-170-mandate-reconciler |
| system-mandate-diff | system/orm | topics/system/orm/skills/system-mandate-diff.md | orm loops |
| system-orm-governance-review | system/orm | topics/system/orm/skills/system-orm-governance-review.md | orm loops |
| consumer-upgrade-advisory | nous-girl | topics/nous-girl/skills/consumer-upgrade-advisory.md | consumer-upgrade-advisory |
| consumer-upgrade-advisory | _global | topics/_global/skills/consumer-upgrade-advisory.md | fleet mirror |

## Creating a Skill

- **Automatic:** Context → queue → Skills writes.
- **Manual:** Edit `topics/<name>/.system/queue.md` and add under `## [SKILLS] items`.
