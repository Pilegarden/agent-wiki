# nous-girl-system loop

## Status
🟢 Active — front-door agent loop.

## Associated agent
`/home/hermes/.hermes/wiki/topics/_global/agents/nous-girl-system.md`

## Trigger
Injection reader loop: before every response, scan ALL topics' `.system/injections.md` and surface highest-priority factory output naturally in conversation, then move matched entries from `[UNREAD]` to `[READ]`.

## Cadence
Continuous / per-turn.

## Health checks
- Verify injection reader surfaces new injections from any topic.
- Validate cross-topic aggregation order by priority.
- Once Context factory starts, validate context block delivery.
