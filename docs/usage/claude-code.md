# Claude Code Installation Guide

Install the Frappe Claude Skill Package in Claude Code for terminal-based development.

For OpenCode, Codex, and `skills.sh`, see [Agent Harnesses](agent-harnesses.md).

## Installation Methods

### Method 1: Personal Skills (Recommended)

Personal skills are available across all your projects.

```bash
# Clone the repository
git clone https://github.com/Impertio-Studio/Frappe_Claude_Skill_Package.git

# Copy skill folders to personal directory
mkdir -p ~/.claude/skills
cp -R Frappe_Claude_Skill_Package/skills/source/*/* ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/frappe-*/SKILL.md
```

Expected output includes:

```text
~/.claude/skills/frappe-syntax-serverscripts/SKILL.md
~/.claude/skills/frappe-core-database/SKILL.md
~/.claude/skills/frappe-impl-serverscripts/SKILL.md
... (61 skill folders)
```

### Method 2: Project Skills (Team Sharing)

Project skills are committed to version control and shared with your team.

```bash
# In your ERPNext project directory
mkdir -p .claude/skills

# Copy skill folders
cp -R /path/to/Frappe_Claude_Skill_Package/skills/source/*/* .claude/skills/

# Commit to version control
git add .claude/skills
git commit -m "Add Frappe development skills"
```

### Method 3: Selective Installation

Install only the skills you need:

```bash
# Example: install only Server Script related skills
cp -R skills/source/syntax/frappe-syntax-serverscripts ~/.claude/skills/
cp -R skills/source/impl/frappe-impl-serverscripts ~/.claude/skills/
cp -R skills/source/errors/frappe-errors-serverscripts ~/.claude/skills/
```

## Verification

Start Claude Code:

```bash
claude
```

Then ask:

```text
What Frappe skills do you have access to?
```

Claude should list installed `frappe-*` skills with descriptions.

## Skill Priority

If the same skill exists in multiple locations, priority is usually:

1. **Managed** - Organization admin settings
2. **Personal** - `~/.claude/skills/`
3. **Project** - `.claude/skills/`
4. **Plugin** - Marketplace plugins

## Using with CLAUDE.md

Create a `CLAUDE.md` in your project root for project-specific context:

```markdown
# Frappe Project Configuration

## Framework Version
This project uses Frappe/ERPNext v15.

## Coding Standards
- Use Server Scripts only for simple validations
- Prefer Controllers for complex business logic
- Always handle permissions explicitly

## Custom Apps
- `custom_app/` - Our custom Frappe app
```

## Troubleshooting

### Skills not appearing

1. Check the copy depth. `SKILL.md` must be directly inside each skill folder:
   ```bash
   ls ~/.claude/skills/frappe-syntax-serverscripts/SKILL.md
   ```
2. Run Claude with debug mode:
   ```bash
   claude --debug
   ```
3. Verify file permissions:
   ```bash
   ls -la ~/.claude/skills/
   ```

### Wrong skill triggered

Make your request more specific. Instead of:

```text
Help me with a script
```

Use:

```text
Help me create a Server Script for Sales Order validation
```

### Scripts not executing

Ensure execute permissions:

```bash
chmod +x ~/.claude/skills/*/scripts/*.py 2>/dev/null
```

## Updating Skills

```bash
cd Frappe_Claude_Skill_Package
git pull
cp -R skills/source/*/* ~/.claude/skills/
```

Re-copying can overwrite local edits in installed skill folders. If you edit installed copies, back them up first.

## Monorepo Support

Claude Code can discover project skills in nested `.claude/skills/` directories. Keep each skill as `<name>/SKILL.md` directly under that directory.

## Next Steps

- Read [USAGE.md](../../USAGE.md) for skill overview
- Check individual skill documentation in `skills/source/*/*/SKILL.md`
- Review [LESSONS.md](../../LESSONS.md) for common pitfalls
