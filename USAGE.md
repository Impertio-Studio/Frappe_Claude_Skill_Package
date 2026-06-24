# Using the Frappe Skills Package

This guide shows how to install and use the 61 Frappe/ERPNext Agent Skills across Claude platforms and other agent harnesses.

## Quick Start

| Platform | Installation Time | Difficulty |
|----------|:-----------------:|:----------:|
| Claude Code | 2 minutes | Easy |
| OpenCode / Codex | 2 minutes | Easy |
| Claude.ai Web/Desktop | 5 minutes | Easy |
| Claude Mobile | ❌ Not supported | - |

## Prerequisites

- **Claude Code**: active Claude Code installation
- **OpenCode/Codex**: agent with Agent Skills support
- **Claude.ai / Desktop**: Pro, Max, Team, or Enterprise plan with Code Execution enabled

## Platform-Specific Guides

- [Agent Harnesses: OpenCode, Codex, skills.sh](docs/usage/agent-harnesses.md)
- [Claude Code Installation](docs/usage/claude-code.md)
- [Claude.ai Web Installation](docs/usage/claude-web.md)
- [Claude Desktop Installation](docs/usage/claude-desktop.md)

## What's Included

This package contains 61 skills organized by category:

| Category | Count | Examples |
|---|:---:|---|
| Syntax | 13 | `frappe-syntax-serverscripts`, `frappe-syntax-doctypes`, `frappe-syntax-query-builder` |
| Core | 11 | `frappe-core-database`, `frappe-core-permissions`, `frappe-core-api` |
| Implementation | 14 | `frappe-impl-serverscripts`, `frappe-impl-customapp`, `frappe-impl-workflow` |
| Error Handling | 7 | `frappe-errors-serverscripts`, `frappe-errors-database`, `frappe-errors-api` |
| Operations | 9 | `frappe-ops-deployment`, `frappe-ops-backup`, `frappe-ops-bench` |
| Agents | 5 | `frappe-agent-validator`, `frappe-agent-architect`, `frappe-agent-debugger` |
| Testing | 2 | `frappe-testing-unit`, `frappe-testing-cicd` |

## Version Compatibility

All skills document version-specific behavior for:

- **Frappe/ERPNext v14** ✅
- **Frappe/ERPNext v15** ✅
- **Frappe/ERPNext v16** ✅

Version-specific differences are documented within each skill.

## How Skills Work

When you start a conversation, the agent loads only skill names and descriptions. When your request matches a skill description, it loads the full instructions. This progressive disclosure keeps the 61-skill package usable without loading every full skill into context.

### Triggering Skills

Skills activate automatically based on your request:

```text
You: "Help me create a Server Script that validates Sales Orders"
Agent: [Loads frappe-syntax-serverscripts and frappe-impl-serverscripts when relevant]
```

You can also reference skills explicitly:

```text
You: "Using frappe-syntax-serverscripts, show me the sandbox limitations"
```

### Checking Available Skills

Ask your agent:

```text
What Frappe skills do you have access to?
```

## Global Installation (Claude Code CLI)

Copy all skill folders to your global skills directory so they're available in every project:

```bash
mkdir -p ~/.claude/skills
cp -R skills/source/*/* ~/.claude/skills/
```

The skills use progressive disclosure: at startup the agent only loads each name and description. Full instructions are loaded only when a skill is relevant to your request.

## Critical: Server Script Sandbox

The most important thing to know about ERPNext development:

**Server Scripts run in a RestrictedPython sandbox. ALL imports are blocked.**

```python
# ❌ WRONG - Will fail
from frappe.utils import nowdate
import json

# ✅ CORRECT - Use frappe namespace
date = frappe.utils.nowdate()
data = frappe.parse_json(json_string)
```

This is the #1 cause of AI-generated ERPNext code failures. All skills in this package are designed with this limitation in mind.

## Support

- **Issues**: [GitHub Issues](https://github.com/Impertio-Studio/Frappe_Claude_Skill_Package/issues)
- **Documentation**: [Full Documentation](docs/)

## License

MIT License - See [LICENSE](LICENSE.md) for details.
