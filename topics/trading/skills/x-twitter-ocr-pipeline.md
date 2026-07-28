---
name: x-twitter-ocr-pipeline
description: Automated pipeline for X/Twitter tweets with media — downloads images, runs OCR/vision extraction, maps extracted entities to thesis layers, and produces structured SIVE/AI signal blocks. Bridges tweet media ingestion with thesis signal detection.
tags: [trading, twitter, ocr, thesis, sive, ai, signal]
related_skills: [x-twitter-ingestion, x-image-pipeline, thesis-evidence-model, social-media-intel]
wiki_path: topics/trading/skills/x-twitter-ocr-pipeline.md
created: 2026-07-12
factory: skills
---

# X/Twitter OCR → Vision → Thesis Signal Pipeline

> Canonical SKILL.md lives at `/home/hermes/.hermes/skills/trading/x-twitter-ocr-pipeline/SKILL.md`
> Wiki mirror for human-readable discovery.

## Trigger

A tweet with media (images/charts/tables) is ingested, or explicit request to "OCR this tweet for thesis signals".

## Pipeline Steps (Overview)

1. **Fetch tweet + media URLs** — spectre-mcp → fxTwitter → browser fallback
2. **Download media** — local cache at `/tmp/spectre-media/`
3. **OCR / Vision extraction** — `vision_analyze` with full-transcription prompt
4. **Structured extraction** — tickers, entities, numbers, dates, signals
5. **Entity → Layer mapping** — against `/srv/trading/research/entity-registry.yaml`
6. **Holdings correlation** — direct/indirect overlap with portfolio
7. **Generate signal block** — structured SIVE/AI thesis block
8. **Save and log** — hoarding vault, thesis notes, brain log

## Dependencies

- **x-twitter-ingestion** — tweet fetch layer
- **x-image-pipeline** — image URL extraction
- **thesis-evidence-model** — 6-tier evidence classification

## Full Reference

See the canonical SKILL.md for the complete pipeline details, fallback chains, pitfalls, and example output.

- **Hermes load:** `skill_view(name='x-twitter-ocr-pipeline')`
- **Canonical path:** `~/.hermes/skills/trading/x-twitter-ocr-pipeline/SKILL.md`
