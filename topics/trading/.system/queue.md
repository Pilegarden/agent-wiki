## [SKILLS] items
- [x] daily-brief-pipeline — ensure `/home/hermes/.hermes/profiles/dev/market/daily-brief.md` is generated before Market Daily Snapshot runs.

## [LOOPS] items
- [x] daily-brief-watcher — watch daily-brief generation health; cron cfa9d1137d7f `30 6 * * 1-5`, loop doc `trading/loops/daily-brief-watcher.md`.
<!-- skills-factory receipt 2026-07-15T14:58:00+0200: inspected queue trading; no open [SKILLS]; no skills created; queue metadata appended -->
<!-- skills-factory receipt 2026-07-15 19:01 CEST: inspected queue trading; no open [SKILLS]; no skills created; queue metadata appended -->

<!-- skills-factory receipt 2026-07-20 01:16 CEST: inspected queue; no open [SKILLS]; idle-tick skill-registry/topic-index/fleet-dashboard drift repaired; catalogs synced -->
<!-- skills-factory receipt 2026-07-20 07:16 CEST: inspected queue trading; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced, queue metadata appended -->
<!-- skills-factory receipt 2026-07-20 03:29 CEST: inspected queue trading; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, skill-registry malformed rows repaired; catalogs synced -->
<!-- skills-factory receipt 2026-07-20 04:52 CEST: inspected queue; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced, queue metadata appended --><!-- skills-factory receipt 2026-07-20 07:46 CEST: inspected queue trading; no open [SKILLS]; no skills created; idle-tick counts verified against catalog tables, catalogs synced -->
<!-- loops-factory receipt 2026-07-20 08:27 CEST: inspected queues trading/ops/travel/sysadmin/_global/integration; no open [LOOPS]; phantom-loop audit applied; loop-registry verified; queues metadata appended; no new artifacts or crons created -->

<!-- loops-factory receipt 2026-07-20 09:34 CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; queue metadata appended; no new artifacts or crons created --><!-- loops-factory receipt 2026-07-20 09:34 CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; queues metadata appended; no new artifacts or crons created -->

<!-- skills-factory receipt 2026-07-20 10:36 CEST: inspected queue; no open [SKILLS]; no skills created; idle-tick counts verified against disk, catalogs checked -->
<!-- loops-factory receipt 2026-07-20 14:29 CEST: inspected queue trading; no open [LOOPS]; phantom-loop audit applied; loop-registry verified; no new artifacts or crons created -->
<!-- loops-factory receipt 2026-07-20 19:xx CEST: inspected queue wiki; no open [LOOPS]; phantom-loop audit applied; loop-registry runtime-error/live-state notes refreshed; queues metadata appended -->

## [OPS] items
- [ ] portfolio-json-reconcile — user reports FORTUM + other ticker positions missing from `/home/hermes/trading/portfolio.json`; reconcile against live Nordnet screenshot/CSV and verify thesis-layer alignment for any undisclosed exposure.
- [ ] insider-dataset-path-resolve — primary 2026-07-22 SIVE insider transaction CSVs expected under `/mnt/download` (hoarding vault); directory does not exist; `/mnt/downloads` unrelated, `/mnt/vault/downloads` empty. Blocking consolidated insider hoard finalization. Need correct mount path or paste upload.
- [ ] Ingest focus topic assets: SIVE 32.8 SEK price update, YouTube video, 3 X statuses (aleabitoreddit), odaily article.
- [ ] Verify Obducat Q2 2026 report ingestion from cron `29bbf060bd7d` (scheduled 2026-07-24 07:30 CEST).
- [ ] Reconcile OBDU position discrepancy (100 vs 609 shares) against live Nordnet data.
- [ ] Confirm Nokia board member identity (not Todd Thomson) with publicly verifiable source.

|- [x] x-twitter-heartbeat empty payload regression — cron job `e0260ed247a1` deliberately removed by user [Stop] 2026-07-27 16:06 CEST. Residual script/investigation retained; investigation remains complete/superseded.

<!-- agents-factory receipt 2026-07-28 06:03 CEST: inspected queue; no open [AGENTS]; idle-tick agent-roster/topic-index/fleet-dashboard counts verified against disk=9; no malformed rows; catalogs in sync; no new artifacts or profiles created -->
