---
name: sirvir-fleet-manager-research-sweep
description: "Sirvir fleet manager research sweep: scan model/provider fleet state, benchmark shifts, pricing changes, and migration risks."
category: _global
status: active
summary: "Research sweep across model fleet signals."
inputs:
  - fleet: "Current registered models, providers, routing table"
  - telemetry: "Recent usage, latency, error rate signals if available"
  - benchmarks: "Community/changelog benchmark deltas"
steps:
  - Review provider/model changelog for capabilities, pricing, or deprecation flags.
  - Compare current routing against newest benchmark data.
  - Classify findings as action_required, watch, or info_only.
outputs:
  - path: "system/sirvir-fleet-manager-research-sweep.md"
    format: categorized findings with source, date, and 1-line impact
  - injections_bullet: "Highest-signal finding and recommended next action"
followup:
  - append `<!-- skills-factory tick ...: sirvir-fleet-manager research sweep done; see system/sirvir-fleet-manager-research-sweep.md -->` to queue.md
  - append findings summary to .system/injections.md
caveats:
  - Do not change routing/permissions directly; report only until explicit approval.
  - Limit sweep to actionable signal; avoid long logs in injections.
