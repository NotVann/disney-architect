#!/usr/bin/env python3
"""
Universal Agent Harness Installer
Configures and mounts the Disney Architect skill across all major AI agent environments:
- Google Antigravity CLI (Global & Local)
- Anthropic Claude Code (.claude/ & CLAUDE.md)
- Cursor IDE (.cursor/rules/)
- Windsurf IDE (.windsurfrules)
- Cline / Roo Code (.clinerules)
- Aider CLI (CONVENTIONS.md & .aider.conf.yml)
- GitHub Copilot (.github/copilot-instructions.md)
- OpenHands (.openhands_instructions)
- Continue.dev (.prompts/disney.prompt)
- Open Agent Standard (AGENTS.md)
- DevContainer Sandbox (.devcontainer/devcontainer.json)
- Model Context Protocol (MCP Server configuration snippet)
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

SKILL_DIR: Path = Path(__file__).resolve().parent.parent

CURSOR_RULE_CONTENT: str = """---
description: Universal Disney Architect multi-stage software engineering framework
globs: *
alwaysApply: false
---

# Disney Architect Framework (Dreamer, Realist, Critic)

When designing, architecting, or scaffolding full-stack software, CLI utilities, or systems:
1. **The Dreamer**: Formulate core value prop and 3 killer differentiator features without constraints.
2. **The Realist**: Prune to 48-hour MVP, select idiomatic stack for the target language, define schemas and API contracts.
3. **The Critic**: Audit against security, performance bottlenecks, and operational costs. Enforce score >= 80/100 before writing code.

Reference: `disney-architect` skill.
"""

CLINERULE_CONTENT: str = """# Disney Architect Framework
Apply the 3-stage Disney Creative Strategy (Dreamer -> Realist -> Critic) when planning and scaffolding code:
- Stage 1 <DREAMER_STAGE>: Unconstrained vision, killer differentiators, UX journey.
- Stage 2 <REALIST_STAGE>: 48h MVP pruning, idiomatic stack selection, complete schemas & file tree.
- Stage 3 <CRITIC_STAGE>: Adversarial security audit, failure vectors, passing score >= 80/100.
"""

COPILOT_INSTRUCTIONS: str = """# GitHub Copilot Instructions: Disney Architect
Structure design through the 3-stage Disney Creative Strategy:
- <DREAMER_STAGE>: Unconstrained user delight, viral mechanics, 3 killer features.
- <REALIST_STAGE>: 48h MVP boundary, DB schemas, API contracts, and physical file tree with >= 1 smoke test.
- <CRITIC_STAGE>: Adversarial security/OWASP audit. Enforce score >= 80/100 before finalizing code.
"""

AIDER_CONFIG: str = """# Aider CLI Configuration
read:
  - CONVENTIONS.md
auto-commits: false
stream: true
"""

CONTINUE_PROMPT: str = """---
name: disney
description: Universal Disney Architect multi-stage software engineering framework
---

Apply the 3-stage Disney Creative Strategy (Dreamer -> Realist -> Critic) to the following request:
{{{ input }}}
"""

DEVCONTAINER_JSON: str = """{
  "name": "Disney Architect Sandbox",
  "image": "mcr.microsoft.com/devcontainers/universal:2-linux",
  "features": {
    "ghcr.io/devcontainers/features/rust:1": {},
    "ghcr.io/devcontainers/features/go:1": {}
  },
  "postCreateCommand": "python3 scripts/critic_linter.py . && python3 scripts/install_harness.py ."
}
"""


def install_all(target_workspace: str = ".") -> None:
    ws = Path(target_workspace).resolve()
    print(f"[*] Installing universal agent harnesses into: {ws}")

    ignore_patterns = shutil.ignore_patterns(
        ".agents", ".claude", ".cursor", ".git",
        "__pycache__", "node_modules", "target", "build"
    )

    # 1. Antigravity Local Workspace
    if ws != SKILL_DIR:
        ag_dir = ws / ".agents" / "skills" / "disney-architect"
        ag_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, ag_dir, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Antigravity CLI: Mounted at {ag_dir}")

    # 2. Antigravity Global
    home = Path.home()
    global_ag = home / ".gemini" / "config" / "skills" / "disney-architect"
    try:
        global_ag.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, global_ag, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Antigravity Global: Mounted at {global_ag}")
    except Exception as e:
        print(f"[-] Antigravity Global skipped: {e}")

    # 3. Claude Code (.claude/ & CLAUDE.md)
    if ws != SKILL_DIR:
        claude_skills = ws / ".claude" / "skills" / "disney-architect"
        claude_skills.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, claude_skills, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Claude Code: Mounted at {claude_skills}")

    claude_md = ws / "CLAUDE.md"
    claude_entry = "\n\n## Skills\n- `/disney`: Invoke the Disney Architect framework (Dreamer, Realist, Critic) for software design and scaffolding.\n"
    if not claude_md.exists() or "/disney" not in claude_md.read_text(encoding="utf-8", errors="ignore"):
        with open(claude_md, "a", encoding="utf-8") as f:
            f.write(claude_entry)
        print(f"[+] Claude Code: Configured {claude_md}")

    # 4. Cursor IDE (.cursor/rules/)
    cursor_dir = ws / ".cursor" / "rules"
    cursor_dir.mkdir(parents=True, exist_ok=True)
    (cursor_dir / "disney-architect.mdc").write_text(CURSOR_RULE_CONTENT, encoding="utf-8")
    print(f"[+] Cursor: Configured {cursor_dir / 'disney-architect.mdc'}")

    # 5. Windsurf (.windsurfrules)
    windsurf_file = ws / ".windsurfrules"
    if not windsurf_file.exists() or "Disney Architect" not in windsurf_file.read_text(encoding="utf-8", errors="ignore"):
        with open(windsurf_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Windsurf: Configured {windsurf_file}")

    # 6. Cline / Roo Code (.clinerules)
    cline_file = ws / ".clinerules"
    if not cline_file.exists() or "Disney Architect" not in cline_file.read_text(encoding="utf-8", errors="ignore"):
        with open(cline_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Cline / Roo Code: Configured {cline_file}")

    # 7. Aider (CONVENTIONS.md & .aider.conf.yml)
    aider_file = ws / "CONVENTIONS.md"
    if not aider_file.exists() or "Disney Architect" not in aider_file.read_text(encoding="utf-8", errors="ignore"):
        with open(aider_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Aider: Configured {aider_file}")

    (ws / ".aider.conf.yml").write_text(AIDER_CONFIG, encoding="utf-8")
    print(f"[+] Aider: Configured {ws / '.aider.conf.yml'}")

    # 8. GitHub Copilot (.github/copilot-instructions.md)
    github_dir = ws / ".github"
    github_dir.mkdir(parents=True, exist_ok=True)
    (github_dir / "copilot-instructions.md").write_text(COPILOT_INSTRUCTIONS, encoding="utf-8")
    print(f"[+] GitHub Copilot: Configured {github_dir / 'copilot-instructions.md'}")

    # 9. OpenHands (.openhands_instructions)
    (ws / ".openhands_instructions").write_text(CLINERULE_CONTENT, encoding="utf-8")
    print(f"[+] OpenHands: Configured {ws / '.openhands_instructions'}")

    # 10. Continue.dev (.prompts/disney.prompt)
    prompts_dir = ws / ".prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    (prompts_dir / "disney.prompt").write_text(CONTINUE_PROMPT, encoding="utf-8")
    print(f"[+] Continue.dev: Configured {prompts_dir / 'disney.prompt'}")

    # 11. DevContainer (.devcontainer/devcontainer.json)
    devcontainer_dir = ws / ".devcontainer"
    devcontainer_dir.mkdir(parents=True, exist_ok=True)
    (devcontainer_dir / "devcontainer.json").write_text(DEVCONTAINER_JSON, encoding="utf-8")
    print(f"[+] DevContainer: Configured {devcontainer_dir / 'devcontainer.json'}")

    # 12. Open Agent Standard (AGENTS.md)
    agents_file = ws / "AGENTS.md"
    if not agents_file.exists():
        agents_file.write_text(f"# AGENTS.md\n\n{CLINERULE_CONTENT}", encoding="utf-8")
        print(f"[+] AGENTS.md: Configured {agents_file}")

    # Print MCP Server JSON config snippet
    mcp_script_path = str((SKILL_DIR / "scripts" / "mcp_server.py").resolve()).replace("\\", "\\\\")
    python_exe = sys.executable.replace("\\", "\\\\")
    
    print("\n--- MCP Server Configuration (Claude Desktop / Zed / Cody) ---")
    print("Add this snippet to your 'claude_desktop_config.json' or Zed 'settings.json':")
    mcp_config = {
        "mcpServers": {
            "disney-architect": {
                "command": python_exe,
                "args": [mcp_script_path],
            }
        }
    }
    print(json.dumps(mcp_config, indent=2))
    print("\n[OK] All Agent CLI, IDE rules, and MCP endpoints configured successfully.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    install_all(target)
