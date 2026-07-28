# discord-preview-watchdog

## Status
- **Active** — verified live in `profiles/dev/cron/jobs.json` on 2026-07-28.
- Job ID: `f5b553f70ca0`
- Schedule: `*/30 * * * *` (every 30m)
- last_status: ok

## Task
After Hermes Discord gateway restarts or Discord config changes, confirm preview/streaming behavior is actually active and compact in Discord.

## Read
- Active profile `config.yaml`
- Discord gateway delivery path / recent delivery behavior

## Write
- Outcome marker: Pass / Fail with exact mismatch
- Remediation path when behavior is wrong

## Failure contract
- `max_parallel`: 1
- `backoff`: 5m
- `max_retries`: 2
- `pause_on_fail`: true

## Success criteria
- Pass = `discord.tool_progress_command` / `tool_preview_length` / `streaming` values are set in profile config **and** a low-risk Discord action shows compact command/action output in chat.
- Fail = exact expected-vs-actual Discord output mismatch, with fix path.
