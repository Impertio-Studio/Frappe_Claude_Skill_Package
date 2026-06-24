# Agent Harness Support Verification — 2026-06-24

This report backs the install paths and commands added for OpenCode, Codex, and `skills.sh` / `npx skills` support.

## Sources checked

| Claim | URL | Retrieved | Result |
|---|---|---:|---|
| OpenCode discovers `SKILL.md` folders from `.opencode/skills`, `.claude/skills`, and `.agents/skills`, including global paths. | https://opencode.ai/docs/skills/ | 2026-06-24 | Confirmed. |
| OpenCode recognizes required `name` and `description`, optional `license`, `compatibility`, and `metadata`; unknown fields are ignored. | https://opencode.ai/docs/skills/ | 2026-06-24 | Confirmed. Current skill frontmatter is compatible. |
| Codex skills are folders containing `SKILL.md`; Codex scans `.agents/skills` in repo/user scopes. | https://developers.openai.com/codex/skills | 2026-06-24 | Confirmed. |
| Codex supports explicit skill invocation with `/skills` / `$skill-name` and loads full `SKILL.md` on demand. | https://developers.openai.com/codex/skills | 2026-06-24 | Confirmed. |
| `npx skills add <source> --list`, `--skill`, `--agent`, `--global`, `--copy`, and `--yes` are supported options. | https://github.com/vercel-labs/skills | 2026-06-24 | Confirmed. |
| `skills` CLI supports OpenCode and Codex as target agents. | https://github.com/vercel-labs/skills | 2026-06-24 | Confirmed by docs and local command smoke test. |

## Commands run

| Command | Result | Notes |
|---|---|---|
| `npx skills@1.5.13 add . --list` | Passed; found 61 skills and listed `frappe-*` skills. | Run from repo root. Output saved during implementation at `/tmp/frappe-skills-list.txt`. |
| `HOME=$(mktemp -d) npx skills@1.5.13 add /Users/dwk/Projects/Frappe_Claude_Skill_Package --skill frappe-core-database --agent codex --yes --copy` | Passed; installed one copied skill to `./.agents/skills/frappe-core-database`. | First run used repo CWD and created temporary untracked `.agents/` + `skills-lock.json`; both were removed. |
| `cd $(mktemp -d) && HOME=$(mktemp -d) npx skills@1.5.13 add /Users/dwk/Projects/Frappe_Claude_Skill_Package --skill frappe-core-database --agent codex --yes --copy` | Passed; installed `frappe-core-database/SKILL.md` in the temp workdir's `.agents/skills`. | Isolated smoke test; did not touch repo/global config. Output saved at `/tmp/frappe-skills-temp-install-isolated.txt`. |

## Claims backed

| File/section | Claim | Evidence |
|---|---|---|
| `docs/usage/agent-harnesses.md` / `skills.sh` | `npx skills@1.5.13 add <source> --list` lists available skills. | `vercel-labs/skills` docs and local `npx skills@1.5.13 add . --list` run. |
| `docs/usage/agent-harnesses.md` / OpenCode | OpenCode can read `~/.agents/skills` and `~/.config/opencode/skills`. | OpenCode docs. |
| `docs/usage/agent-harnesses.md` / Codex | Codex can read `.agents/skills` and `$HOME/.agents/skills`. | OpenAI Codex skills docs. |
| `README.md`, `USAGE.md`, `docs/usage/claude-code.md` | Correct copy depth is `skills/source/*/*`, because each skill folder is under `skills/source/<category>/<skill>/SKILL.md`. | Repo structure: 61 `skills/source/*/*/SKILL.md` files. |
| `tools/quick_validate.py` | `package.json agents.skills` should stay in sync with discovered skills. | `package.json` contains 61 manifest entries and repo contains 61 skills. |

## Unsupported / not claimed

- No Codex plugin package is built in this change.
- No `npx skills` command is added to CI.
- No generated `.agents/`, `.opencode/`, or `.claude/` skill tree is committed.
- No guarantee is made that unattended `--global --yes` installs are safe for every user's existing agent configuration; docs warn before showing that command.
