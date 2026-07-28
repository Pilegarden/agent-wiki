---
name: paper-digest
description: "Run the Paper Digest tick: scan recent research/paper sources for new releases, prioritize by relevance, and write a digest block."
category: _global
status: active
summary: "Routine digest tick for new papers."
inputs:
  - sources: "RSS/Atom feeds, arXiv watch queries, saved research queues"
  - dedup: "Use last-digest timestamp or seen IDs"
steps:
  - Collect new items since last digest boundary.
  - Score by keywords in active research topics.
  - Select top items with a one-line why-it-matters note.
outputs:
  - path: "system/paper-digest.md"
    format: short list: title, source, relevance, link
  - injections_bullet: "New papers since last tick with top pick"
followup:
  - append `<!-- skills-factory tick ...: paper-digest done; see system/paper-digest.md -->` to queue.md
  - write digest summary into .system/injections.md
caveats:
  - Avoid duplicates across consecutive ticks.
  - If no new papers, mark tick as no-op instead of repeating prior digest.
