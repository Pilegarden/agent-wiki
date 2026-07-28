# Trading

Live trading automation: ISK/TJP accounts, portfolio watchers, infra watchers, thesis intelligence.

## Status
🟡 Partial — active infrastructure, blocked by missing daily-brief.md.

## Active Issues
- `daily-brief.md` missing at `/home/hermes/.hermes/profiles/dev/market/daily-brief.md`.
  - Impact: Market Daily Snapshot cron cannot post telegram summary.
- Primary SIVE insider datasets expected under `/mnt/download`; directory absent. `/mnt/downloads` unrelated, `/mnt/vault/downloads` empty. Blocks consolidated insider hoard finalization.

## SIVE insider development (July 21)
- Lock-up expired July 16, 2026.
- CEO bought 70K additional shares (now 4.54M + 3.7M options); genuine insider conviction.
- Board sales: lock-up expiry flows + VC fund distributions (Kairos Ventures Mixcomm legacy), not coordinated exodus.
- Chairman Bastani: retained 381K shares + 625K options after partial sale and charitable gifts.
- Closed period July 28 — Aug 27 (Q2 interim report). Limited insider trades expected in that window.
- Thesis verdict: neutral; removes bearish overhang. No position change required. Existing frameworks (CPO demand/yield, hard stop 30 SEK, Q2 print Aug 27) remain primary.

## SIVE insider export blocker (July 22)
- User submitted 4 FI.SE `.csv` insider exports via Discord.
- Initial verification: all 4 files appeared workbook/binary despite `.csv` extension.
- Resolved: user provided copied page 1–7 content as plain text; consolidated insider analysis written to `/mnt/obsidian-vault/research/thesis-hoard/2026-07-22_sive-insider-register-consolidated.md` and cross-indexed.

## AI Infrastructure Corridor (July 23)
- Nokia Q2 2026 note published: EUR 4.8B sales, Optical +20%, IP +16%, AI/Cloud order intake +105% to EUR 2.8B.
- Sivers connection: governance/credibility link via ex-Nokia board member (not Todd Thomson); no confirmed commercial deal.
- Obducat Q2 2026 interim report watcher scheduled: one-shot cron 2026-07-24 07:30 CEST.
- Corridor crosslinks active: AAOI (optics/compute), Samsung-NAND (storage/memory), AMD-Helios (compute/inference), Nokia (optical expansion).

## Related Topics
- Ops: gbrain MCP heartbeat DOWN

## Tooling & vault updates (2026-07-24)
- `/opt/obsidian-vault/research/trading/INDEX.md` normalized to clean `[[filename]]` wikilinks (no `.md` extension).
- New canonical origin docs ingested: `ai-infra-supply-chain-thesis-2026-05-25.md` (May 25), `acmr-besi-chinese-memory-2026-05-27.md` (May 27).
- Position reconciliation note `sive-position-reconciliation-2026-07-23.md` created mapping SIVE/OBDU position trails.
- `allspace-sivers-8-2m-ka-band-order.md` upgraded to confirmed $8.2M production order + $16.4M SES strategic agreement.
- Nokia board attribution corrected (not Todd Thomson; actual board member unidentified).
- Blockers: focus topic assets (SIVE 32.8 SEK, YouTube, X statuses, odaily article) pending ingestion; Obducat Q2 watcher cron `29bbf060bd7d` status unknown; portfolio.json stale (user dropped refresh); OBDU position discrepancy (100 vs 609 shares); live pricing unavailable (Avanza last-close only).