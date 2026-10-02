# Disney Architect

[![CI](https://img.shields.io/badge/CI-Passing-brightgreen?style=flat-square)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://python.org)
[![MCP Server](https://img.shields.io/badge/MCP-Compatible-purple?style=flat-square)](#)
[![Agents Supported](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Copilot%20%7C%20Zed%20%7C%20Cline%20%7C%20Aider-orange?style=flat-square)](#)

A polyglot, multi-stage software architecture and scaffolding framework for AI coding assistants, implementing the **Disney Creative Strategy** (Robert Dilts) to bridge high-leverage product vision, pragmatic technical architecture, and adversarial reliability auditing.

---

## The Workflow

```text
[Raw User Concept / Issue / Feature Request]
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 1. THE DREAMER  (<DREAMER_STAGE>)             │
│    - Unconstrained visionary thinking         │
│    - Core value proposition & aha-moments     │
│    - 3 killer competitive differentiators     │
└───────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 2. THE REALIST  (<REALIST_STAGE>)             │
│    - Prunes scope to lean 48h MVP (Veto power)│
│    - Auto-detects domain (Web/CLI/Sys/Mobile) │
│    - Generates DB schemas & API contracts     │
│    - Scaffolds runnable code & smoke tests    │
└───────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 3. THE CRITIC   (<CRITIC_STAGE>)              │
│    - Adversarial security & OWASP audit       │
│    - Performance, memory & failure modes      │
│    - Deterministic AST & syntax linter gate   │
└───────────────────────────────────────────────┘
                     │
          ┌──────────┴───────────────────────────────┐
          ▼ [Score < 80 OR Syntax Error]             ▼ [Score >= 80 & Valid Syntax]
┌───────────────────────────────┐          ┌───────────────────────────────┐
│ REVISION LOOP (Max 2 Rounds)  │          │ VERIFIED RUNNABLE SCAFFOLD    │
│ Realist fixes audit findings  │          │ Output: Codebase ready to run │
└───────────────────────────────┘          └───────────────────────────────┘
```

---

## Ecosystem Support Matrix

| Category | Agents & Clients | Integration Mechanism |
| :--- | :--- | :--- |
| **CLI Agents** | Google Antigravity, Claude Code, Aider, OpenHands | `.agents/`, `CLAUDE.md`, `.aider.conf.yml`, `.openhands_instructions` |
| **IDE Extensions** | Cursor, Windsurf, Cline / Roo Code, GitHub Copilot, Continue.dev | `.cursor/rules/`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `.prompts/` |
| **MCP Clients** | Claude Desktop, Zed Editor, Sourcegraph Cody | Native JSON-RPC stdio MCP Server (`scripts/mcp_server.py`) |
| **Open Standards** | Autonomous Frameworks, SWE-agent | `AGENTS.md` |
| **Sandboxes** | Devin, GitHub Codespaces | `.devcontainer/devcontainer.json` |

---

## Quick Start: Universal Installation

Run the universal installer to mount the skill across your active agent environments in one command:

```bash
python scripts/install_harness.py .
```

### MCP Server Setup (Claude Desktop & Zed Editor)
Add this entry to your `claude_desktop_config.json` or Zed `settings.json`:

```json
{
  "mcpServers": {
    "disney-architect": {
      "command": "python",
      "args": ["<absolute-path-to-disney-architect>/scripts/mcp_server.py"]
    }
  }
}
```

---

## Key Capabilities

- **Zero-Hallucination Gatekeeper**: Enforces deterministic AST parsing (`python scripts/critic_linter.py`) before code authorization. Broken syntax automatically caps the audit score at `0/100`.
- **Domain & Language Agnostic**: Dynamically calibrates to any domain (Web, CLI, Systems, Mobile, Microservices) and language (Rust, Go, Python, TypeScript, C++, Zig, Flutter).
- **Model-Degradation Resistant**: Uses strict XML boundary delimiters (`<DREAMER_STAGE>`, `<REALIST_STAGE>`, `<CRITIC_STAGE>`) and few-shot golden examples to ensure reliable execution across both lightweight (7B/8B) and frontier (o1, Sonnet) models.
- **Language Directive**: Converses dynamically in the user's natural language while keeping all technical artifacts, schemas, and source code strictly in standard English.
- **TDD Baseline Mandate**: Every scaffolded project includes at least one runnable smoke test verifying startup and healthcheck endpoints.

---

## Execution Modes

| Flag | Name | Behavior |
| :--- | :--- | :--- |
| *(default)* | **Autonomous** | Executes continuously from prompt to verified codebase without interruption. |
| `--interactive` | **Human-in-the-Loop** | Pauses after Dreamer stage for user feedback on features before drafting architecture. |

---

## Repository Structure

```text
disney-architect/
├── AGENTS.md                          # Open Multi-Agent Standard
├── SKILL.md                          # Antigravity master controller & state machine directives
├── README.md                         # Project documentation
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Development & testing guide
├── .github/
│   ├── workflows/ci.yml              # GitHub Actions CI matrix
│   └── copilot-instructions.md       # GitHub Copilot directives
├── .devcontainer/devcontainer.json    # DevContainer sandbox environment
├── .aider.conf.yml                    # Aider auto-load configuration
├── .openhands_instructions            # OpenHands runner instructions
├── .prompts/disney.prompt             # Continue.dev slash command
├── references/
│   ├── 01-dreamer-protocol.md        # Visionary ideation protocol
│   ├── 02-realist-protocol.md        # Pragmatic architecture & scaffold protocol
│   ├── 03-critic-protocol.md         # Adversarial audit & scoring protocol
│   └── templates/
│       └── disney-spec-template.md   # Consolidated architecture document template
├── examples/
│   └── golden-sample.md              # End-to-end few-shot execution sample
└── scripts/
    ├── mcp_server.py                 # Zero-dependency Model Context Protocol stdio server
    ├── critic_linter.py              # Deterministic AST and syntax validator
    ├── install_harness.py            # Universal multi-agent configuration installer
    └── verify_scaffold.py            # Polyglot scaffold integrity auditor
```

---

## License

This project is licensed under the [MIT License](LICENSE).
