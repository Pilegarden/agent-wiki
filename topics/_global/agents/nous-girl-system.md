# nous-girl-system

## Status
🟢 Active — primary chat surface. Profile exists at `~/.hermes/profiles/nous-girl/`.

## Source
Spec-defined: `~/.hermes/wiki/spec.md` — this is the front-door agent of the Agent Wiki system. The user talks directly to this agent.

## Profile
`/home/hermes/.hermes/profiles/nous-girl` exists with:
- **SOUL.md** — full directive: Agent Wiki system awareness, injection reading across ALL topics, factory status knowledge, user steering guidance, full tool access
- **config.yaml** — `deepseek-v4-flash` model, `deepseek` provider, all tools enabled (`toolsets: [all]`), Langfuse telemetry

## Summary
Nous Girl is the user-facing chat agent — the one person the user converses with directly. She is the front door of the Agent Wiki system. Key responsibilities:

1. **Primary execution surface** — full Hermes toolset available to respond to user requests (terminal, files, browser, search, session DB, skill management, image gen, etc.)
2. **Injection reader** — scans ALL topics' `.system/injections.md` before every response, weaves the highest-priority factory output naturally into conversation, moves it to `[READ]`
3. **Factory status awareness** — knows all four factories (Context/30min, Skills/15min, Agents/15min, Loops/15min), their triggers, inputs, and outputs
4. **User steering guide** — when asked how to control the system, directs the user to edit wiki markdown files (queue.md for new items, continuity.md for corrections, mark agent/skill/loop files as cancelled)

System path: `~/.hermes/wiki/` with spec at `~/.hermes/wiki/spec.md`.

## Next actions
- ✅ Agent roster updated — shows `nous-girl-system`, "all" tools, "🟢 Active — front-door agent"
- Verify injection reader works end-to-end when factories start producing injections
- Once Context factory is running, validate that Nous Girl's injection reader surfaces context properly
