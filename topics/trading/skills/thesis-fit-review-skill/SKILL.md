---
title: Thesis Fit Review
topic: trading
status: active
created: 2026-07-13
---

# Thesis Fit Review

## Purpose

Review every new thesis-hoard artifact before entity-registry integration. If it is off-thesis, quarantine it, log a FAILED table row, and produce a shelved artifact without touching the entity registry.

## Inputs

- New thesis-hoard artifact path or Wikilink
- Entity-registry skip/read-only context
- Active thesis list for the topic

## Workflow

1. Load artifact content and active thesis list.
2. Compare artifact claims against active thesis criteria.
3. If off-thesis:
   - Add quarantine banner at top of the artifact or note body.
   - Append a FAILED table row with `artifact`, `reason`, `timestamp`, and `verb=note`.
   - Produce a shelved artifact in the `review/shelved/` area with no entity-registry tie.
   - Do not update entity registry.

## FAILED table format

| artifact | reason | timestamp | verb | tags |

Example:

| [[thesis-hoard/2026-07-13-pesi.md]] | off-thesis; $PESI override | 2026-07-13T23:00:00+02:00 | note | off-thesis, quarantine |
| | | | | |

## Quarantine banner

Use exactly:
```
> ⛔ QUARANTINE — off-thesis artifact, not admitted to entity registry.
```

## Outputs

- Shelved note with quarantine banner + FAILED row appended
- No registry mutation

## Definition of Done

- Quarantine banner present
- FAILED row appended
- Shelved note exists with `note` verb
- Entity registry unchanged
