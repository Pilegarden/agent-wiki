# nexus-integration

- topic: `integration`
- queue ref: `topics/_global/.system/queue.md` `[AGENTS] nexus-integration`
- status: 🟢 Active (recovered idle-tick 2026-07-22)
- profile: `/home/hermes/.hermes/profiles/nexus-integration/` (Hermes profile provisioned)
- summary: Persistent integration bridge between Hermes shells and upstream Nessus/MISP/ThreatConnect-style intel platforms. Bridge-first identity with strict read boundary; findings-only summaries, never credentials.
- loop: `topics/integration/loops/nexus-intel-sync.md` — deployed cron `da64be0fe62c` by loops-factory.
