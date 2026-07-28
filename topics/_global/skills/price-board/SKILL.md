---
name: price-board
description: Build a normalized price-board markdown surface from one or more instrument sources.
category: _global
status: active
summary: >
  Assemble a current price-board from supplied tick data with source tracking, change deltas,
  category grouping, and wiki injection bookkeeping.
---

# Price Board

Read instrument prices from the provided input, normalize them, and emit a markdown price-board artifact. Update bookmarking files when run as part of a scheduled workflow.

## Tick Behavior

- On-demand or scheduled tick.
- Load inputs, validate schema, skip stale or duplicate market sessions when applicable.
- Emit one artifact to `boards/YYYY-MM-DD-<session>.md`.
- Update `.system/injections.md` with injected artifact path.
- Update `queue.md` with follow-up row if any instrument needs rest-of-day attention.

## Required Inputs

Preferred inputs (checked in order; stop at first available):

1. `price-inputs.yaml` in the skill dir — live websocket or REST endpoints per instrument group.
2. Staged payloads under `inbox/` — JSON or CSV files named `YYYY-MM-DD-<source>.json|csv`.
3. Caller args: explicit instrument tuples `(symbol, exchange, price, currency, ts)`.

`price-inputs.yaml` entry shape:

```yaml
groups:
  - name: equity-us
    instruments:
      - symbol: AAPL
        exchange: NASDAQ
        currency: USD
    source:
      type: rest
      url: https://...
      refresh_s: 60
    stale_after_s: 300
```

## Normalization Steps

For each instrument row:

1. **Extract** symbol, exchange, price, currency, timestamp, and source name.
2. **Canonicalize** symbol case to upper; validate currency against ISO-4217 allowlist.
3. **Enrich** with session id `YYYY-MM-DD` from the max timestamp across inputs.
4. **Deduplicate** by `(symbol, exchange, session)` keeping newest price.
5. **Flag** rows where `now - ts > stale_after_s` with `stale: true`.

## Grouping and Scoring

- Group by `group name` from the yaml payload, else fallback `ungrouped`.
- Within each group, sort by `symbol` lexicographically.
- Row columns:
  - `Symbol`
  - `Exchange`
  - `Price`
  - `Currency`
  - `Change %` if previous close is available, else `-`
  - `Updated`
  - `Stale` flag when enrichment step marked it

## Output Artifact Format

```markdown
---
session: 2026-07-14
generated_at: 2026-07-14T12:04:00Z
sources: [rest,nasdaq-feed]
instrument_count: 12
stale_count: 1
---

# Price Board — 2026-07-14

## equity-us

| Symbol | Exchange | Price | Currency | Change % | Updated | Stale |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | NASDAQ | 213.25 | USD | +1.2% | 2026-07-14T12:02:00Z |  |
| MSFT | NASDAQ | 415.88 | USD | -0.4% | 2026-07-14T12:02:00Z |  |

## crypto

| Symbol | Exchange | Price | Currency | Change % | Updated | Stale |
| --- | --- | --- | --- | --- | --- | --- |
| BTCUSD | COINBASE | 104200 | USD | +2.1% | 2026-07-14T12:01:00Z | yes |

## Notes

- 1 stale instrument above refresh threshold.
```

## Follow-up Actions

After a successful run, append to:

- `.system/injections.md`
  ```
  - [price-board] /boards/2026-07-14-<session>.md | instruments=<N> | stale=<M>
  ```
- `queue.md`
  ```
  - [price-board] stale AAPL 2026-07-14T12:04:00Z | action=re-feed or mark-stale
  ```

If all rows are stale for a group, add a human-action row in `queue.md` instead of silently emitting a degenerate board.

## Duplicate Suppression and Caveats

- Persist seen `(symbol, exchange, session)` tuples in `watermark.json` under `seen`.
- On start: load watermark; skip already seen tuples unless forced by caller flag `force_refresh=true`.
- Watermark is append-only; never delete entries. Tag superseded tuples with `retired_at` and `retire_reason`.
- If the same instrument appears across multiple groups, place it in the first matching group and emit a `duplicate_group_skip` note in the artifact.
- Do not mutate exchanger-supplied timestamps; only annotate stale status.
- Preservation: keep price precision from source; do not round for display-only convenience.
- Clearing: stale-watermark pruning is manual only. Clear `seen` entries only after market hours for that exchange, and only from code paths that explicitly confirm business-day closure.
