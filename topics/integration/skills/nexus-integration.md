---
name: nexus-integration
description: >
  Persistent integration bridge between Hermes shells and upstream Nessus/MISP/ThreatConnect-style intel platforms
  without babysitting auth state. Use this skill when wiring intel enrichment, cross-context incident pivoting,
  or automated feed ingestion that must survive config changes and shell restarts.
tags:
  - integration
  - nexus
  - intel
  - automation
---

# nexus-integration

## When to Use
Run this skill when a session needs a durable integration path from Hermes to an external intel platform. If the workload is exploratory, start in read-only mode; if it is operational, use the configurable recurring loop path with recovery policies.

## Prerequisites
- Hermes profile with network access to the target platform
- Platform auth method configured outside the session lifecycle so restarts do not require re-auth
- Verify whether the environment blocks hostname policy, TLS inspection, or proxy routing before first live call

## Procedure
1. Establish the platform endpoint and auth envelope that does not depend on an active chat session.
2. Confirm transport and policy exceptions are recorded in the project profile so future sessions inherit them.
3. Model the minimum viable handshake: what query is needed, what result shape is accepted, and what fail mode applies.
4. Run a single read-only probe before adding any write or mutation path.
5. If the probe succeeds, wire a recurring loop only if tasks will repeat with bounded failure modes.

## Read Contract
- Current project config for target platform selection and auth metadata
- Prior session notes for already-attempted endpoints or auth methods

## Write Contract
- Platform request objects with retry and backoff state if applicable
- Event or log records tied to a run ID so later failures can be resumed without context loss

## Verification
- Successful read-only probe with expected result shape
- Auth state survives Hermes shell restart or profile reload
- Recurring loop has pause_on_fail and retry behavior set

## Failure Recovery
- If auth expires, reset through the platform's non-interactive path and restart from handshake verification
- If a prior run is interrupted, resume from the last known run ID instead of repeating from scratch
