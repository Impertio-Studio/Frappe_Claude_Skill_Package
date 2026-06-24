#!/usr/bin/env python3
"""Quick validation script for Agent Skill folders.

Stdlib-only on purpose: contributors should be able to run this on a clean
checkout with `python3 tools/quick_validate.py skills/source --all`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_LINES = 500


def parse_frontmatter(content: str) -> tuple[dict, str | None]:
    """Parse the small YAML subset used by this repo's SKILL.md files."""
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "SKILL.md must start with YAML frontmatter (---)"

    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return {}, "Invalid YAML frontmatter format: missing closing ---"

    data: dict[str, object] = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith(" "):
            return data, f"Unexpected indented frontmatter line: {line.strip()}"
        if ":" not in line:
            return data, f"Invalid frontmatter line: {line}"

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value == ">":
            folded: list[str] = []
            i += 1
            while i < end and (lines[i].startswith(" ") or not lines[i].strip()):
                folded.append(lines[i].strip())
                i += 1
            data[key] = " ".join(x for x in folded if x).strip()
            continue

        if value == "":
            nested: dict[str, str] = {}
            i += 1
            while i < end and (lines[i].startswith(" ") or not lines[i].strip()):
                child = lines[i].strip()
                if child and ":" in child:
                    ck, cv = child.split(":", 1)
                    nested[ck.strip()] = cv.strip().strip('"\'')
                i += 1
            data[key] = nested
            continue

        data[key] = value.strip('"\'')
        i += 1

    return data, None


def validate_skill(skill_path: str | Path):
    """Validate a skill folder against repo requirements."""
    errors: list[str] = []
    warnings: list[str] = []

    skill_path = Path(skill_path).resolve()
    skill_name = skill_path.name

    skill_md_path = skill_path / "SKILL.md"
    if not skill_md_path.exists():
        errors.append("SKILL.md not found in skill root folder")
        return errors, warnings

    content = skill_md_path.read_text(encoding="utf-8")

    line_count = len(content.splitlines())
    if line_count > MAX_LINES:
        errors.append(f"SKILL.md has {line_count} lines (max {MAX_LINES})")

    frontmatter, parse_error = parse_frontmatter(content)
    if parse_error:
        errors.append(parse_error)
        return errors, warnings

    name = str(frontmatter.get("name", ""))
    if not name:
        errors.append("Missing required 'name' field in frontmatter")
    else:
        if len(name) > 64:
            errors.append(f"name '{name}' exceeds 64 characters ({len(name)})")
        if not re.match(r"^[a-z0-9-]+$", name):
            errors.append(f"name '{name}' must be kebab-case (a-z, 0-9, - only)")
        if name != skill_name:
            errors.append(f"name '{name}' must match folder name '{skill_name}'")

    desc = str(frontmatter.get("description", ""))
    if not desc:
        errors.append("Missing required 'description' field in frontmatter")
    else:
        if len(desc) > 1024:
            errors.append(f"description exceeds 1024 characters ({len(desc)})")
        if not desc.startswith("Use when"):
            errors.append("description must start with 'Use when'")

    license_value = str(frontmatter.get("license", ""))
    if license_value != "MIT":
        errors.append("Missing required 'license: MIT' field in frontmatter")

    compatibility = str(frontmatter.get("compatibility", ""))
    if not compatibility:
        errors.append("Missing required 'compatibility' field in frontmatter")
    elif not re.search(r"Frappe v\d+(?:-v\d+)?", compatibility):
        errors.append("compatibility must include a Frappe version range like 'Frappe v14-v16' or 'Frappe v15-v16'")

    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("Missing required 'metadata' block in frontmatter")
    else:
        if not metadata.get("author"):
            errors.append("Missing required 'metadata.author' field in frontmatter")
        if not metadata.get("version"):
            errors.append("Missing required 'metadata.version' field in frontmatter")

    for forbidden in ["README.md", "CHANGELOG.md"]:
        if (skill_path / forbidden).exists():
            warnings.append(f"Found {forbidden} in skill folder (not recommended)")

    refs_path = skill_path / "references"
    if refs_path.exists() and not refs_path.is_dir():
        errors.append("'references' should be a directory, not a file")

    return errors, warnings


def discover_skills(root: str | Path) -> list[Path]:
    return sorted(p.parent for p in Path(root).glob("*/*/SKILL.md"))


def print_result(path: Path, errors: list[str], warnings: list[str]) -> None:
    print(f"Validating: {path}")
    if warnings:
        print("  ⚠️  WARNINGS:")
        for warning in warnings:
            print(f"     - {warning}")
    if errors:
        print("  ❌ ERRORS:")
        for error in errors:
            print(f"     - {error}")
    else:
        print("  ✅ Skill is valid")


def main() -> int:
    if len(sys.argv) < 2 or len(sys.argv) > 3 or (len(sys.argv) == 3 and sys.argv[2] != "--all"):
        print("Usage: python3 tools/quick_validate.py <skill_folder>")
        print("       python3 tools/quick_validate.py <skills_root> --all")
        return 1

    path = Path(sys.argv[1])
    if not path.is_dir():
        print(f"Error: {path} is not a directory")
        return 1

    if len(sys.argv) == 3:
        skill_dirs = discover_skills(path)
        if not skill_dirs:
            print(f"Error: no skills found under {path} (expected */*/SKILL.md)")
            return 1
    else:
        skill_dirs = [path]

    total_errors = 0
    total_warnings = 0
    passed = 0
    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        total_errors += len(errors)
        total_warnings += len(warnings)
        if not errors:
            passed += 1
        print_result(skill_dir, errors, warnings)

    print("-" * 50)
    print(f"Validated: {len(skill_dirs)} skill(s); passed: {passed}; failed: {len(skill_dirs) - passed}; warnings: {total_warnings}; errors: {total_errors}")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
