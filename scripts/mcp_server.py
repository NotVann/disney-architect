#!/usr/bin/env python3
"""
Zero-Dependency MCP (Model Context Protocol) Server for Disney Architect.
Exposes Disney Architect workflows, protocols, and validation tools via standard
JSON-RPC 2.0 stdio protocol. Compatible with Claude Desktop, Zed Editor, Sourcegraph Cody,
and any MCP-compliant client.
"""

from __future__ import annotations

import json
import sys
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

SKILL_DIR: Path = Path(__file__).resolve().parent.parent
REFERENCES_DIR: Path = SKILL_DIR / "references"


def read_protocol(filename: str) -> str:
    path = REFERENCES_DIR / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"Error: Protocol file {filename} not found."


def handle_initialize(msg_id: Any) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {},
                "prompts": {},
            },
            "serverInfo": {
                "name": "disney-architect-mcp",
                "version": "1.0.0",
            },
        },
    }


def handle_tools_list(msg_id: Any) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "tools": [
                {
                    "name": "get_dreamer_protocol",
                    "description": "Returns the Dreamer visionary ideation protocol and output schema.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_realist_protocol",
                    "description": "Returns the Realist pragmatic architecture, polyglot stack, and scaffold protocol.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_critic_protocol",
                    "description": "Returns the Critic adversarial audit, OWASP checklist, and scoring rubric.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "run_critic_linter",
                    "description": "Executes deterministic syntax and AST validation across target project directory.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "target_dir": {
                                "type": "string",
                                "description": "Absolute or relative path to project directory to audit.",
                            },
                        },
                        "required": ["target_dir"],
                    },
                },
                {
                    "name": "verify_scaffold_integrity",
                    "description": "Verifies build manifest presence and scaffold completeness across any language.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "target_dir": {
                                "type": "string",
                                "description": "Path to scaffolded project to verify.",
                            },
                        },
                        "required": ["target_dir"],
                    },
                },
            ],
        },
    }


def handle_tools_call(msg_id: Any, params: Dict[str, Any]) -> Dict[str, Any]:
    tool_name = params.get("name")
    args = params.get("arguments", {})

    if tool_name == "get_dreamer_protocol":
        content = read_protocol("01-dreamer-protocol.md")
    elif tool_name == "get_realist_protocol":
        content = read_protocol("02-realist-protocol.md")
    elif tool_name == "get_critic_protocol":
        content = read_protocol("03-critic-protocol.md")
    elif tool_name == "run_critic_linter":
        target = args.get("target_dir", ".")
        linter_script = SKILL_DIR / "scripts" / "critic_linter.py"
        res = subprocess.run([sys.executable, str(linter_script), target], capture_output=True, text=True)
        content = res.stdout + ("\n" + res.stderr if res.stderr else "")
    elif tool_name == "verify_scaffold_integrity":
        target = args.get("target_dir", ".")
        verify_script = SKILL_DIR / "scripts" / "verify_scaffold.py"
        res = subprocess.run([sys.executable, str(verify_script), target], capture_output=True, text=True)
        content = res.stdout + ("\n" + res.stderr if res.stderr else "")
    else:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [
                {
                    "type": "text",
                    "text": content,
                }
            ],
        },
    }


def handle_prompts_list(msg_id: Any) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "prompts": [
                {
                    "name": "disney_architect",
                    "description": "Execute the 3-stage Disney Creative Strategy to design and scaffold an application.",
                    "arguments": [
                        {
                            "name": "concept",
                            "description": "The application concept or requirements.",
                            "required": True,
                        },
                        {
                            "name": "language",
                            "description": "Target programming language (e.g. Rust, Go, Python, TypeScript).",
                            "required": False,
                        },
                    ],
                }
            ],
        },
    }


def handle_prompts_get(msg_id: Any, params: Dict[str, Any]) -> Dict[str, Any]:
    args = params.get("arguments", {})
    concept = args.get("concept", "Application")
    lang = args.get("language", "Idiomatic Best-Fit")

    prompt_text = (
        f"You are executing the Disney Architect framework for: '{concept}' in '{lang}'.\n"
        "Follow these 3 phases sequentially:\n"
        "1. <DREAMER_STAGE>: Unconstrained vision, core value prop, 3 killer differentiators.\n"
        "2. <REALIST_STAGE>: Prune to 48h MVP, select idiomatic stack, generate complete schemas and directory tree including smoke tests.\n"
        "3. <CRITIC_STAGE>: Adversarial security/OWASP audit, failure vectors, passing score >= 80/100.\n"
    )

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "description": f"Disney Architect execution for {concept}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": prompt_text,
                    },
                }
            ],
        },
    }


def serve_stdio() -> None:
    """
    Main loop reading line-delimited JSON-RPC messages from stdin and replying to stdout.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = handle_initialize(msg_id)
        elif method == "notifications/initialized":
            continue
        elif method == "ping":
            res = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
        elif method == "tools/list":
            res = handle_tools_list(msg_id)
        elif method == "tools/call":
            res = handle_tools_call(msg_id, req.get("params", {}))
        elif method == "prompts/list":
            res = handle_prompts_list(msg_id)
        elif method == "prompts/get":
            res = handle_prompts_get(msg_id, req.get("params", {}))
        else:
            if msg_id is not None:
                res = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"Method '{method}' not found"},
                }
            else:
                continue

        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    serve_stdio()
