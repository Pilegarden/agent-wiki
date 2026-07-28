# trading-daily-snapshot-fix

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[SKILLS] trading-daily-snapshot-fix`
- status: queued
- cadence: on-demand when snapshot job fails
- model pin: used to stabilize job to `stepfun/step-3.7-flash:free` on provider=nous

## Notes

Skill body drafted from continuity.md failure mode (Nous OAuth expired), root-cause list includes expired token, missing model pin, uncontrolled fallback provider routing, gateway token state, and schema-mismatched provider names.

Skill artifact exists in `/home/hermes/.hermes/skills/trading-daily-snapshot-fix/SKILL.md`. Next action is reproduction on the trading cron job during approved infra maintenance.

## Checklist

- [ ] identify broken snapshot job via profile inventory
- [ ] inspect `auth.json` provider token presence and expiry
- [ ] pin job to `provider=nous` and `model=stepfun/step-3.7-flash:free`
- [ ] clear fallback_providers off this job path
- [ ] refresh token if 401 persists, then gate gateway restart once
- [ ] smoke-test job and update queue `[x]` on success
