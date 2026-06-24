# Claude.ai Web Installation Guide

Install the Frappe Skills Package in the Claude.ai web interface.

## Prerequisites

- **Plan**: Pro, Max, Team, or Enterprise
- **Feature**: Code Execution must be enabled

## Step 1: Enable Code Execution

1. Go to **Settings** (gear icon)
2. Navigate to **Capabilities**
3. Enable **Code execution and file creation**

## Step 2: Download Skills

### Option A: Download Pre-packaged Skills

Download `.skill` files from the repository if packaged artifacts are published:

```text
skills/packaged/
├── frappe-syntax-serverscripts.skill
├── frappe-core-database.skill
├── frappe-impl-serverscripts.skill
... (61 .skill files)
```

Each `.skill` file is a ZIP archive ready for upload.

### Option B: Create ZIP Files Manually

For each skill you want to install:

1. Download the skill folder, e.g. `skills/source/syntax/frappe-syntax-serverscripts/`
2. Create a ZIP file with the folder as root:
   ```text
   frappe-syntax-serverscripts.zip
   └── frappe-syntax-serverscripts/
       ├── SKILL.md
       └── references/
           └── ...
   ```

**Important**: the ZIP must contain the skill folder, not just its contents.

## Step 3: Upload Skills

1. Go to **Settings** > **Capabilities**
2. Scroll to the **Skills** section
3. Click **Upload skill**
4. Select your `.skill` or `.zip` file
5. Repeat for each skill you want to install

## Step 4: Verify Installation

1. Start a new conversation
2. Ask: "What Frappe skills do you have access to?"
3. Claude should list your installed skills

## Recommended Installation Order

For most Frappe development work, install these skills first:

### Essential

1. `frappe-syntax-serverscripts` - Server Script sandbox rules
2. `frappe-core-database` - Database operations
3. `frappe-impl-serverscripts` - Server Script workflows

### Extended

4. `frappe-syntax-clientscripts` - Client Script patterns
5. `frappe-syntax-controllers` - Controller methods
6. `frappe-core-permissions` - Permission system
7. `frappe-errors-serverscripts` - Server error handling

### Full Package

Install all 61 skills for comprehensive coverage.

## Skill Name Requirements

If you're creating ZIPs manually, ensure:

- Folder name is **lowercase**
- Only letters, numbers, and **hyphens** allowed
- Example: `frappe-syntax-serverscripts` ✅
- Example: `Frappe_Syntax_ServerScripts` ❌

## Managing Skills

### Toggle Skills On/Off

In **Settings** > **Capabilities** > **Skills**, use the toggle switch next to each skill.

### Remove a Skill

1. Go to **Settings** > **Capabilities** > **Skills**
2. Find the skill you want to remove
3. Click the delete/remove option
4. Confirm deletion

## Team and Enterprise Plans

Admins can provision skills for all users from admin capability settings. Users can still upload personal skills when allowed by organization policy.

## Troubleshooting

### "Skills appear greyed out"

- Check that Code Execution is enabled
- For Team/Enterprise: check with your admin that Skills are enabled org-wide

### Upload fails

1. Check ZIP structure: folder must be at root
2. Verify `SKILL.md` starts with `---` on line 1
3. Ensure skill name is lowercase with hyphens

### Skill doesn't trigger

- Make your request more specific
- Mention the skill name: "Using `frappe-syntax-serverscripts`..."
- Check that the skill is toggled ON in settings

## Storage and Privacy

- Custom skills are private to your account unless provisioned by an organization admin
- Skills run in Claude's sandboxed environment
- No data persists between sessions unless explicitly saved by the platform

## Next Steps

- Read [USAGE.md](../../USAGE.md) for skill overview
- Check individual skill documentation in `skills/source/*/*/SKILL.md`
- Review [LESSONS.md](../../LESSONS.md) for common pitfalls
