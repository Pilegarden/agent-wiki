# thesis-fit-review

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[LOOPS] thesis-fit review loop`
- status: active
- cadence: Mon–Fri 09:00, 14:00
- deliver: `telegram:-1004376316450:8`
- model pin: unpinned (no-agent script)
- job id: `115b88c1d5fd`

## Scope

Runs on every trading weekday cycle. Scans new thesis-hoard artifacts under `topics/trading/thesis` and gates off-thesis names before entity-registry integration. Outputs a shelved artifact review list with quarantine metadata. When no new artifacts exist, emits `NO_ARTIFACTS`.

## Cron Details

```bash
hermes cron create \
  --name "thesis-fit-review" \
  --deliver "telegram:-1004376316450:8" \
  --repeat 999 \
  --no-agent \
  --script "thesis-fit-review.sh" \
  --workdir "/srv/trading" \
  "0 9,14 * * 1-5" \
  "Scan ${HOME}/.hermes/wiki/topics/trading/thesis for new thesis-hoard artifacts and gate off-thesis names before entity-registry integration. Emit a shelved artifact review list. NO_ARTIFACTS is acceptable."
```

- **Job ID**: `115b88c1d5fd`
- **Script**: `~/.hermes/scripts/thesis-fit-review.sh`
- **Workdir**: `/srv/trading` (resolved path `/home/hermes/trading`)
- **Created**: 2026-07-19 by loops-factory phantom recovery

## Output

Markdown artifact review list:
- `status`: scanned / NO_ARTIFACTS / draft
- `scanned`: artifact path
- `timestamp`: ISO-8601 run time
- `## Off-thesis quarantine`: shelved names + quarantine metadata

## Failure Mode

- No thesis artifacts path → `NO_ARTIFACTS` + empty quarantine block
- Script path permissions `755` enforced at creation; re-add if missing
- If Telegram delivery fails, retry on next 09:00/14:00 run

## State

- last_status: ok
- last_run: 2026-07-28 14:00 CEST (verified live)
- failure_count: 0
- max_retries: 3
- pause_on_fail: false
