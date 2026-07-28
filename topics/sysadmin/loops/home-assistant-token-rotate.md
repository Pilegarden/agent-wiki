# home-assistant-token-rotate

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `Rotate Home Assistant long-lived token`
- status: **draft/awaiting approval** — manual credential rotation required
- mode: manual
- deliver: local

## Scope

Rotate the Home Assistant long-lived token that was previously shared in
Discord chat. Canonical secret is now `homelab/home-assistant/jarvis-long-lived-token` in BWS.

## Steps

1. Generate a new long-lived token in Home Assistant UI (User Profile → Long-Lived Access Tokens).
2. Revoke the old token.
3. Update `homelab/home-assistant/jarvis-long-lived-token` in BWS.
4. Verify automations/integrations using the token continue to work.
5. Record rotation timestamp in loop doc.

## Safety

Do not expose the new token in chat. Treat BWS as the single source of truth.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
