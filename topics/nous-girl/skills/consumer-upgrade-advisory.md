---
name: consumer-upgrade-advisory
description: "Product upgrade advice from usage data and market research."
wiki_path: topics/nous-girl/skills/consumer-upgrade-advisory.md
factory: context-factory
created: 2026-07-26
tags: [Research, Decision Support]
---

# consumer-upgrade-advisory

## Role
Supports evidence-backed upgrade recommendations by combining real usage data with specs, pricing, timing signals, and media math. Avoids instinct-first advice.

## Trigger Conditions
- User asks "should I upgrade to X or Y"
- Comparing devices, laptops, phones, tablets, or similar consumer hardware
- User has usage data, habits, or constraints (budget, region, refurbished market)
- Timing questions: buy now vs wait for next release

## Canonical Artifact
- Hermes `SKILL.md`: `productivity/consumer-upgrade-advisory`
- Use `skill_view(name='consumer-upgrade-advisory')` for the full canonical workflow
