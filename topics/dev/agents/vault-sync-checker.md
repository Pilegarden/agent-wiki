# vault-sync-checker

## Status
Provisioned (2026-07-27)

## Source/Queue Reference
- Queue: `topics/dev/.system/queue.md`
- Item: `vault-sync-checker — verify vault sync health and NFS permission drift on /mnt/obsidian-vault`

## Profile Location and Key Files
- Profile path: `~/.hermes/profiles/vault-sync-checker/`
- Identity: `SOUL.md`
- Config: `config.yaml`

## Summary of Responsibilities
Vault sync health inspector. Compares `/opt/obsidian-vault` (source) against `/mnt/obsidian-vault` (NFS mirror) via rsync dry-run. Inspects NFS export permissions from Box `.104`. Detects root-owned files blocking `rsync --delete`. Reports exact failing path, owner/group, and remediation command. No mutations without explicit approval.

## Checks Performed
- Rsync dry-run for path divergence
- `find /mnt/obsidian-vault -nouser -nogroup` for orphan file detection
- `getfacl` on NFS mount for permission review
- `stat` comparison for owner/group mismatches
- `mount | grep /mnt/obsidian-vault` for mount options

## Next Actions
- Configure model/toolsets in `config.yaml` if needed
- Verify profile loads correctly: `vault-sync-checker chat`
