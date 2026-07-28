import json, re
from datetime import datetime
from pathlib import Path

vault = Path.home() / '.hermes/wiki'

def now_local():
    return datetime.now().astimezone().isoformat()

# 1. Collect all loop docs (flat, maxdepth-1 under topics/*/loops/*.md)
loop_docs = []
for p in (vault / 'topics').glob('*/loops/*.md'):
    # exclude factory receipts
    if p.name in ('loop-factory-summary.md', 'ops-factory-summary.md', 'sysadmin-loop-factory-summary.md'):
        continue
    loop_docs.append(p)
loop_docs.sort()

print(f'Loop docs on disk: {len(loop_docs)}')

# 2. Collect all agent docs (flat summaries under topics/*/agents/*.md)
agent_flat = []
agent_nested = []
for p in (vault / 'topics').rglob('agents/*'):
    if not p.is_file() or p.suffix != '.md':
        continue
    # flat if directly under agents/ and not AGENTS.md/SOUL.md
    if p.parent.name == 'agents' and p.name not in ('AGENTS.md', 'SOUL.md'):
        agent_flat.append(p)
    else:
        agent_nested.append(p)

agent_flat.sort()
agent_nested.sort()
print(f'Agent flat summaries: {len(agent_flat)}')
print(f'Agent nested artifacts (SOUL/AGENTS): {len(agent_nested)}')

# 3. Extract claimed job IDs from loop docs
claimed = {}
for p in loop_docs:
    text = p.read_text()
    matches = re.findall(r'(?:Job ID|job id|cron job):\s*`?([^`)\s\n]+)`?', text)
    for m in matches:
        if m == 'none':
            continue
        claimed.setdefault(m, []).append(str(p.relative_to(vault)))

print('\nClaimed job IDs (deduplicated per doc):')
for jid, paths in sorted(claimed.items()):
    print(f'  {jid}: {len(paths)} doc(s)')

# 4. Collect live jobs from all profiles
live_jobs = {}
for profile_json in Path.home().joinpath('.hermes/profiles').glob('*/cron/jobs.json'):
    profile = profile_json.parent.parent.name
    try:
        data = json.loads(profile_json.read_text())
        jobs = data.get('jobs', [])
        for j in jobs:
            jid = j.get('id','')
            live_jobs[jid] = {
                'profile': profile,
                'name': j.get('name','?'),
                'script': j.get('script'),
                'last_status': j.get('last_status'),
                'last_error': j.get('last_error'),
                'last_run_at': j.get('last_run_at'),
                'schedule': j.get('schedule', {})
            }
    except Exception as e:
        print(f'Error reading {profile_json}: {e}')

print(f'\nLive cron jobs across all profiles: {len(live_jobs)}')

# 5. Cross-reference claimed vs live
print('\nPhantom audit:')
phantoms = []
for jid, paths in claimed.items():
    if jid == 'none':
        print(f'  {jid}: no job claimed (fine)')
        continue
    if jid in live_jobs:
        info = live_jobs[jid]
        print(f'  {jid}: LIVE in {info["profile"]} - last_status={info["last_status"]} last_run={info["last_run_at"]}')
    else:
        print(f'  {jid}: PHANTOM - absent from all stores! paths={paths}')
        phantoms.append((jid, paths))

# 6. Check for live jobs not in claimed
print('\nLive jobs with no loop doc claim (factory/unrelated):')
for jid, info in live_jobs.items():
    if jid not in claimed:
        print(f'  {jid}: {info["name"]} in {info["profile"]}')

# 7. Check runtime-erroring
print('\nLive but potentially erroring:')
for jid, info in live_jobs.items():
    if info.get('last_status') and 'error' in info.get('last_status','').lower():
        print(f'  {jid}: {info["name"]} - {info["last_status"]} err={info.get("last_error","")}')

# 8. Agent -> loop map (per topic, from flat summaries)
agent_loop_map = {}
for p in agent_flat:
    agent_name = p.stem
    topic = p.parent.parent.name
    loops_dir = p.parent.parent / 'loops'
    if loops_dir.exists():
        loops = [f.name for f in loops_dir.glob('*.md') if f.name not in ('loop-factory-summary.md',)]
        agent_loop_map[f'{topic}/{agent_name}'] = loops
    else:
        agent_loop_map[f'{topic}/{agent_name}'] = []

print('\nAgent -> loop map:')
for agent, loops in sorted(agent_loop_map.items()):
    print(f'  {agent}: {len(loops)} loops ({loops})')

# 9. Loopless agents
loopless = [agent for agent, loops in agent_loop_map.items() if not loops]
print(f'\nLoopless agents: {loopless}')

# 10. Registry check
registry_path = vault / 'topics/_global/loop-registry.md'
text = registry_path.read_text()
lines = text.split('\n')
in_table = False
data_rows = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith('|--'):
        in_table = True
        continue
    if in_table and stripped.startswith('|'):
        data_rows.append(stripped)
    if in_table and not stripped.startswith('|'):
        in_table = False

print(f'\nRegistry data rows in table: {len(data_rows)}')
malformed = [r for r in data_rows if r.startswith('||')]
print(f'Registry malformed rows (start with ||): {len(malformed)}')

print(f'\nTimestamp: {now_local()}')
