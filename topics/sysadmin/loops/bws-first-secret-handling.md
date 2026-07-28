# bws-first-secret-handling

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `BWS-first secret handling`
- status: **draft/awaiting approval** — operational policy enforcement required
- mode: manual
- deliver: local

## Scope

Enforce BWS/BSM secret push in active sysadmin sessions. Never paste live
tokens in chat. Update session runbooks and verify all active operations use
BWS-pulled secrets.

## Steps

1. Audit active sysadmin sessions and configs for plaintext tokens.
2. Migrate any plaintext secrets to BWS.
3. Update runbooks to reference `bws secret get` / `bws lookup` patterns.
4. Add terminal secret-scanning / gitignore guards to prevent future leaks.
5. Record outcome in loop doc.

## Safety

Rotate any token that was previously exposed in chat before promoting BWS to canonical.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
