# Disney Architect Skill

A polyglot, multi-stage software architecture and scaffolding framework for AI coding assistants (Google Antigravity, Anthropic Claude Code, Cursor, Windsurf, Cline, Aider), implementing the **Disney Creative Strategy** (Dreamer, Realist, Critic).

---

## Architectural Stages

1. **The Dreamer (`<DREAMER_STAGE>`)**: Explores unconstrained product vision, core value propositions, and 3 killer differentiators without technical limitations.
2. **The Realist (`<REALIST_STAGE>`)**: Prunes to a 48-hour MVP, auto-detects the domain archetype (Web, CLI, Systems, Mobile, Microservices), selects an idiomatic toolchain, outputs complete schemas, and scaffolds a runnable project tree including smoke tests.
3. **The Critic (`<CRITIC_STAGE>`)**: Executes an adversarial security and reliability audit (OWASP, memory safety, data races, signal handling). Enforces a hard deterministic AST/syntax linter gate before authorizing code commits.

---

## Execution Modes

- **Autonomous Mode (`--auto` / Default)**: Continuous pipeline execution from raw user concept to verified runnable scaffold on disk.
- **Interactive Mode (`--interactive`)**: Pauses after `<DREAMER_STAGE>` to align on killer features and scope before schema compilation.

---

## Universal Multi-Agent Installation

Run the universal installer script to mount the skill across all installed agent CLIs and IDE rules simultaneously:

```bash
python scripts/install_harness.py [optional_workspace_path]
```

### Supported Environments
- **Google Antigravity**: Configured in `~/.gemini/config/skills/disney-architect` and `.agents/skills/`.
- **Claude Code**: Configured in `.claude/skills/` and referenced in `CLAUDE.md`.
- **Cursor IDE**: Generates `.cursor/rules/disney-architect.mdc`.
- **Windsurf IDE**: Appends to `.windsurfrules`.
- **Cline / Roo Code**: Appends to `.clinerules`.
- **Aider**: Appends to `CONVENTIONS.md`.

---

## Verification & Tooling

```bash
# Run deterministic syntax/AST audit across generated source code
python scripts/critic_linter.py <target_directory>

# Verify polyglot build manifest and scaffold completeness
python scripts/verify_scaffold.py <target_directory>
```

---

## Trigger Examples

Invoke naturally in any supported language:
- *"Architect a real-time collaborative canvas using the disney method."*
- *"Rancang CLI file vault di Rust pakai disney architect --interactive."*
- *"Plan and scaffold a distributed task queue with disney architect."*
