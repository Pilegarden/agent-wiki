---
title: Tweet Media OCR Mandate
topic: trading
status: active
created: 2026-07-13
---

# Tweet Media OCR Mandate

## Purpose

Hard guardrail: any tweet containing media must be processed through browser fetch + OCR. `web_extract` alone drops image content and is forbidden when media is present.

## When it applies

- Input tweet metadata indicates images, GIFs, video thumbnails
- Tweet URL is being retrieved for signal extraction
- Pipeline stage: tweet ingestion → media assessment

## Decision tree

1. Fetch tweet with browser fetch (`browser_navigate` to tweet URL).
2. If `browser_get_images` returns non-empty image list:
   - Proceed to OCR via browser screenshot + `vision_analyze` or tesseract path.
   - Do not call `web_extract` for the tweet.
3. If no media:
   - Standard text path is allowed.

## Required path

```
browser_navigate(tweet_url) -> browser_get_images -> if images: browser_vision -> OCR -> append OCR text to payload
```

## Failure behavior

- If browser fetch fails twice, mark tweet status `ocr-failed` and skip media block.
- Log image URLs for manual retry in next run.
- Never substitute `web_extract` for missing browser coverage.

## Output contract

Each tweet payload with media must include:
- `text`: extracted text
- `ocr`: OCR block from vision
- `images`: count + raw URLs
- `media_status`: ocr | skipped | failed

## Definition of Done

- All tweets with media have non-empty OCR output or explicit `media_status`
- No tweet with images passed through text-only path
