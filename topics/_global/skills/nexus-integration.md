---
name: nexus-integration
description: Bridge Hermes shell runtime to upstream intel platforms with durable auth handling, read-only probing, and recoverable recurring-loop support.
wiki_path: topics/integration/skills/nexus-integration.md
factory: skills-factory
created: 2026-07-20
---

# nexus-integration

## Role
Supports Hermes-to-intel-platform integration workflows so sessions do not need to re-auth on restart.

## Trigger Conditions
- A topic or agent needs integration with Nessus/MISP/ThreatConnect-style platforms
- Recurring enrichment or ingestion fails when Hermes restarts without a persistent auth path
- A run must resume from an interruption without repeating the entire handshake

## Canonical Artifact
- Hermes `SKILL.md`: `/home/hermes/.hermes/wiki/topics/integration/skills/nexus-integration.md`
- Use `skill_view(name='nexus-integration')` for the full canonical workflow
