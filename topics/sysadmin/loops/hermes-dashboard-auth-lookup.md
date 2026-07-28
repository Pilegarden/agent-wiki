# hermes-dashboard-auth-lookup

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `[LOOPS] hermes-dashboard-auth-lookup`
- status: **completed** — lookup executed 2026-07-25
- mode: manual
- deliver: local

## Scope

One-time lookup for the Hermes dashboard authentication source. Document where
credentials are set, reset, and overridden so future ops can recover or rotate
without guessing.

## Findings

| Path / Surface | Role | Reset mechanism |
|---|---|---|
| `.hermes/config.yaml` → `dashboard.basic_auth` | **Primary canonical config** | Edit YAML directly (`username`, `password_hash` or `password`, optional `secret`, `session_ttl_seconds`). Preferred at-rest form is `password_hash`. |
| `HERMES_DASHBOARD_BASIC_AUTH_USERNAME` env | Override username | Unset or edit env source. |
| `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD` env | Override plaintext password (hashed in-memory) | Unset or change env source. |
| `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD_HASH` env | Override scrypt hash preferred | Set to new scrypt hash. |
| `HERMES_DASHBOARD_BASIC_AUTH_SECRET` env | Token-signing key override | Set new 32+ byte key; sessions persist restarts if set. |
| `HERMES_DASHBOARD_BASIC_AUTH_TTL_SECONDS` env | Session access-token TTL | Unset or edit env. |

- **Live source on this host:** `.hermes/config.yaml` contains the active `hermes` user + scrypt password_hash. No `dashboard.basic_auth` block exists under any profile-specific config.
- **Password rotation:** precompute `password_hash` via `python -c "from plugins.dashboard_auth.basic import hash_password; print(hash_password('NEW_PW'))"` and paste into config. Alternative: set the plaintext via env var (hashed at startup, overrides config hash for that run).
- **Secret for stable sessions:** when `secret` is unset, the provider generates a random per-process key; sessions are invalidated on every dashboard restart. Set `dashboard.basic_auth.secret` (or env) to persist sessions across restarts.
- **Reset path:** edit `.hermes/config.yaml`; restart dashboard process after config changes.

## Safety

Do not log or echo the plaintext password. The scrypt hash is safe to keep in config. If a plaintext password is discovered in config, rotate it to a `password_hash` immediately.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
