# session-db-repair

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[SKILLS] session-db-repair`
- status: deferred
- cadence: manual/scheduled when state.db repair path is approved
- model pin: not required

## Notes

`.hermes/sessions/state.db` is zero-byte and blocks `session_search` across all profiles due to SQLite FTS5 trigram virtual table corruption. Prior tick inserted this queue item and created continuity notes. Reproducing/corrupting the DB is unsafe. This loop is deferred until user approves manual module rebuild of state.db; factory should not recreate the artifact from scratch until approval is scoped.

## Checklist

- [ ] user approves state.db rebuild approach
- [ ] backup zero-byte `/home/hermes/.hermes/sessions/state.db`
- [ ] rebuild FTS5 tables or recreate state.db via approved Hermes maintenance flow
- [ ] verify `session_search` works in dev + nous-girl profiles
