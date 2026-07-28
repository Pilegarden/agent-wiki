# Travel

## Dashboard
- Status: idle
- Active destination: none
- Upcoming trips: STN → GOT on Sun 19 Jul (booking XX3ESQ)
- Bookings: Ryanair leg DBV → STN completed; return STN → GOT Sun 19 Jul
- Open items: travel profile Telegram wiring missing

## Notes
Telegram is not wired to the `travel` Hermes profile. Evidence:
- `channel_directory.json` → `telegram: []`
- No `telegram-topics.yaml` under `~/.hermes/profiles/travel/`
- Travel config only has Discord settings
Latest tick: 2026-07-15 08:06 CEST — platform connectivity audited.

## Files
- `topics/travel/.system/continuity.md` — append-only continuity log
- `topics/travel/.system/queue.md` — [SKILLS]/[AGENTS]/[LOOPS] queue
- `topics/travel/.system/injections.md` — agents/loops factory status
