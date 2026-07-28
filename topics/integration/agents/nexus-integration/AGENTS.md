# nexus-integration

## Status
Provisioned on 2026-07-15.

## Source
- Queue: `topics/_global/.system/queue.md` `[AGENTS] nexus-integration ...`
- Topic: `topics/integration`

## Profile
- `SOUL.md`: bridge-first identity with strict read boundary.
- `meta.yaml`: workspace-bound read scope.

## Responsibilities
- Maintain integration bridge state against Nessus/MISP/ThreatConnect-style sources.
- Avoid babysitting auth; prefer cached idempotent lookups.
- Produce findings-only summaries, never credentials.
