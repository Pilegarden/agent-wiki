# nordnet-position-reconciler

- topic: `trading`
- status: **stale/draft — never deployed**
- This file originally contained deprecated nordnet-watchdog content (copy-paste error).
- No cron job was ever created for this loop.
- The actual nordnet reconciliation workflow exists as a skill: `nordnet-position-reconciler`.

## Notes

The Nordnet transaction export reconciliation pipeline lives in skill form only.
No cron loop is wired — it's manual/on-demand. If a cron schedule is desired,
add `[LOOPS] nordnet-position-reconciler — wire reconciliation to weekly schedule`
to a topic's `.system/queue.md`.
