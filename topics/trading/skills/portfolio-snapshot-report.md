---
name: portfolio-snapshot-report
description: Lightweight daily active-positions summary regenerated from portfolio.json. Cron-friendly companion to portfolio-summary. Extracts positions, computes snapshot balance, produces chat-safe numbered output.
tags: [trading, portfolio, snapshot, cron]
related_skills: [portfolio-summary, portfolio-snapshot-label, portfolio-rebalancing]
wiki_path: topics/trading/skills/portfolio-snapshot-report.md
created: 2026-07-12
factory: skills
---

# Portfolio Snapshot Report

> Canonical SKILL.md lives at `/home/hermes/.hermes/skills/trading/portfolio-snapshot-report/SKILL.md`
> Wiki mirror for human-readable discovery.

## Trigger

Cron job (daily 06:00), or explicit request to "regenerate active-positions summary", "run snapshot report", "daily portfolio digest".

## Canonical Source

- **Primary (speed):** `/srv/trading/data/portfolio.json` — compact Schema B (~200 lines), `active_positions[]` + `totals{}`. Preferred for cron runs.
- **Fallback (detail):** `/srv/trading/portfolio.json` — full Schema A (~2900 lines), funds + stocks + trade history.

## Position Derivation

1. Read portfolio.json from the primary source.
2. For Schema B: extract from `active_positions[]` array.
3. For Schema A: combine `accounts.ISK.funds_sek` (array) + `accounts.ISK.stocks` (object/dict).
4. **Filter out** entries where `status in ('archived', 'sold')`. Entries without a `status` field are active.
5. Each position must include: ticker, type (Fund/Equity), qty, avg cost SEK, value SEK, P/L SEK, return %, layer (if available), thesis note (if available).
6. For Schema A stocks: `qty = shares`, `avg_cost = avg_price_sek`, `value = value_sek`, `pl = profit_sek`, `return_pct = return_pct`.

## Snapshot Balance

- Compute as sum of `value_sek` for all active (non-filtered) positions.
- Label: **Snapshot balance (YYYY-MM-DD): N SEK**
- Use the latest NAV/prices from the file — note the `last_updated` date.
- Do NOT include `free_cash_sek` or `cash_available_sek` (liquidity, not positions).

## Output Format (Chat Delivery)

**NEVER use pipe tables.** Output as numbered lists with emoji indicators:

```
1. ✅ SIVE — 25 @ 65.91 SEK = 1,652 SEK (+4.75 / +0.29%) [L4]
2. ⚠️ XFAB — 10 @ 10.19 EUR (111.18 SEK) = 1,062 SEK (−49.70 / −4.47%) [L3]
```

Prefix: ✅ positive/neutral, ⚠️ negative return, 🔴 guard breach. Include layer tag.

**Delivery order:**
1. **Header:** Date, account, active position count, snapshot balance, data freshness
2. **Positions:** Numbered list with indicators
3. **Layer Exposure:** One line per layer
4. **Notes:** Staleness warnings, schema source, special flags

## Mirror Output

Write identical content to both paths (create parent dirs if missing):
- `~/.hermes/profiles/trading/research/active-positions-summary-<today>.md`
- `/opt/obsidian-vault/trading/portfolio/active-positions-<today>.md`

## Full Reference

See the canonical SKILL.md for pitfalls, validation steps, cron safety, and detailed edge-case handling.

- **Hermes load:** `skill_view(name='portfolio-snapshot-report')`
- **Canonical path:** `~/.hermes/skills/trading/portfolio-snapshot-report/SKILL.md`
