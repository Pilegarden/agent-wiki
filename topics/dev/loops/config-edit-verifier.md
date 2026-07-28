# config-edit-verifier

| Field | Value |
|---|---|
| Name | config-edit-verifier |
| Topic | dev |
| Schedule | every 30m |
| Agent | dev |
| Mode | watcher |

## Task
When a Hermes profile `config.yaml` edit is rejected by file mutation verification, classify the failure mode and report the accepted remediation path.

## Read
- Profile `config.yaml` current contents
- Recent `hermes config set` invocation state / success indicator
- Refusal/mutation pattern from Hermes config edit path

## Write
- Status: accepted rejection / silent no-op / successfully applied by alternate path
- Exact profile config path when still stale
- Next reset/restart step when alternate path also leaves unchanged state

## Failure contract
- `max_parallel`: 1
- `backoff`: 5m
- `max_retries`: 2
- `pause_on_fail`: true

## Success criteria
- Status is classified to one of: accepted rejection / silent no-op / successfully applied by alternate path.
- If still stale after `hermes config set`, surface exact profile config path and next reset/restart step.

## Remediation guard
- Do not attempt direct patch to `/home/hermes/.hermes/profiles/*/config.yaml`.
- Accepted fallback paths: edit `~/.hermes/config.yaml` directly, or rerun `hermes config set <key> <value>` with a valid key.

## Cron Status
- Job ID: 124337b6d86a
- Schedule: 0 8 * * * (daily 08:00)
- Status: active
