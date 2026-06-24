# Agent Harness Installation Guide

Install the Frappe skill package in OpenCode, Codex, Claude Code, or any tool that consumes Agent Skills (`SKILL.md` folders).

Canonical source used in commands:

```text
Impertio-Studio/Frappe_Claude_Skill_Package
```

## Recommended: skills.sh / npx skills

First list the skills. This is safe and does not install anything:

```bash
npx skills@1.5.13 add Impertio-Studio/Frappe_Claude_Skill_Package --list
```

Install one skill for Codex:

```bash
npx skills@1.5.13 add Impertio-Studio/Frappe_Claude_Skill_Package \
  --skill frappe-core-database \
  --agent codex
```

Install one skill for OpenCode:

```bash
npx skills@1.5.13 add Impertio-Studio/Frappe_Claude_Skill_Package \
  --skill frappe-core-database \
  --agent opencode
```

Install all skills only after reviewing the list:

```bash
npx skills@1.5.13 add Impertio-Studio/Frappe_Claude_Skill_Package \
  --skill '*' \
  --agent codex \
  --agent opencode
```

### Global/unattended install warning

`--global` writes into global agent config. `--yes` skips prompts. Use them only when you are comfortable overwriting or merging existing skill links/copies.

```bash
npx skills@1.5.13 add Impertio-Studio/Frappe_Claude_Skill_Package \
  --skill frappe-core-database \
  --global \
  --agent codex \
  --yes
```

## Manual fallback: OpenCode

OpenCode reads project and global skill folders including `.opencode/skills`, `.claude/skills`, and `.agents/skills`.

Global shared Agent Skills path:

```bash
mkdir -p ~/.agents/skills
cp -R skills/source/*/* ~/.agents/skills/
```

OpenCode-native global path:

```bash
mkdir -p ~/.config/opencode/skills
cp -R skills/source/*/* ~/.config/opencode/skills/
```

Project-local OpenCode path:

```bash
mkdir -p .opencode/skills
cp -R /path/to/Frappe_Claude_Skill_Package/skills/source/*/* .opencode/skills/
```

## Manual fallback: Codex

Codex reads Agent Skills from `.agents/skills` in repo/user scopes.

Global:

```bash
mkdir -p ~/.agents/skills
cp -R skills/source/*/* ~/.agents/skills/
```

Project-local:

```bash
mkdir -p .agents/skills
cp -R /path/to/Frappe_Claude_Skill_Package/skills/source/*/* .agents/skills/
```

## Manual fallback: Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/source/*/* ~/.claude/skills/
```

## Updating and uninstalling

Manual `cp -R` installs are flat copies. Re-running the copy command can overwrite local edits in installed skill folders.

To update manual installs:

```bash
cd Frappe_Claude_Skill_Package
git pull
cp -R skills/source/*/* ~/.agents/skills/
```

To uninstall manual installs, delete the copied `frappe-*` folders from the target directory:

```bash
rm -rf ~/.agents/skills/frappe-*
```

For `skills.sh`, prefer the CLI's own update/remove commands when available:

```bash
npx skills@1.5.13 update
npx skills@1.5.13 remove frappe-core-database
```

## Troubleshooting

- Skill not visible: verify the folder contains `SKILL.md` directly, e.g. `~/.agents/skills/frappe-core-database/SKILL.md`.
- Wrong copy depth: use `skills/source/*/*`, not `skills/source/*`.
- Duplicates: remove older copies from other global paths (`~/.agents/skills`, `~/.claude/skills`, `~/.config/opencode/skills`).
- `npx skills` failure: use the manual OpenCode/Codex paths above.

See [`../validation/agent-harness-support-2026-06-24.md`](../validation/agent-harness-support-2026-06-24.md) for the source and command verification behind this guide.
