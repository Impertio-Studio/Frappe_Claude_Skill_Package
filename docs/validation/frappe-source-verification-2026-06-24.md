# Frappe Source Verification — 2026-06-24

## Scope

Implemented structural validation and a minimal source audit for the requested official sources:

- `https://github.com/frappe/frappe_docker`
- `https://docs.frappe.io/framework/user/en/introduction`

The validator checks repo structure only. It does **not** prove Frappe API correctness or Docker operational accuracy.

## Official URLs checked

All URLs below returned HTTP 200 on 2026-06-24.

| URL | Retrieved | Used for |
|---|---:|---|
| https://docs.frappe.io/framework/user/en/introduction | 2026-06-24 | Framework overview source entry: Python/JavaScript/MariaDB, metadata-as-data, Desk, permissions, REST API |
| https://github.com/frappe/frappe_docker | 2026-06-24 | Official repository source entry for Docker/container setup |
| https://frappe.github.io/frappe_docker/ | 2026-06-24 | Published Frappe Docker docs root source entry |
| https://frappe.github.io/frappe_docker/getting-started.html | 2026-06-24 | Frappe Docker architecture/repo layout/services/images/overrides source entry |
| https://frappe.github.io/frappe_docker/01-getting-started/04-single-compose-setup.html | 2026-06-24 | Single compose `pwd.yml` services/volumes/adaptation source entry |
| https://frappe.github.io/frappe_docker/05-development/01-development.html | 2026-06-24 | Devcontainer/development workflow source entry |

## Changed factual claims

| File | Claim changed | Source URL | Reviewer check |
|---|---|---|---|
| `tools/quick_validate.py` | Validator is structural only and uses stdlib parsing, not PyYAML. | Repo-local implementation; no external Frappe claim. | Verified by code and `python3 tools/quick_validate.py skills/source --all`. |
| `CONTRIBUTING.md` | Skill line limit is maximum 500 lines measured with Python `splitlines()`. | Repo-local policy reconciliation; no external Frappe claim. | Matches `tools/quick_validate.py`. |
| `SOURCES.md` | Frappe Framework introduction is an approved source for high-level framework overview. | https://docs.frappe.io/framework/user/en/introduction | URL returned 200; source is official Frappe docs. |
| `SOURCES.md` | `frappe_docker` repo and selected Frappe Docker docs are approved sources for Docker/container setup. | https://github.com/frappe/frappe_docker and `frappe.github.io/frappe_docker` pages above | URLs returned 200; sources are official repo/docs. |
| `skills/source/ops/frappe-ops-website-deploy/SKILL.md` | Description now starts with `Use when` and keeps v15-v16 compatibility. | Repo-local skill trigger policy; no new external Frappe claim. | Verified by validator; compatibility remains `Frappe v15-v16, ERPNext v15-v16`. |
| `skills/source/core/frappe-core-database/SKILL.md` | Reference file list was condensed to meet line limit. | Repo-local formatting only; no external Frappe claim changed. | Verified line count is <= 500. |

## Docker/deployment skill review

No Docker/deployment skill body claims were changed in this implementation. The `frappe_docker` URLs were added to `SOURCES.md` for future source-backed edits and to satisfy the requested verification scope.

## Validator limitations

- Checks frontmatter shape, required metadata, line count, skill names, references directory shape.
- Allows legitimate compatibility ranges such as `Frappe v14-v16` and `Frappe v15-v16`.
- Does not crawl documentation.
- Does not prove every code example is correct.
- Does not enforce language purity with a brittle word blocklist.

## Commands run

```bash
# URL liveness checks
curl -L -s -o /dev/null -w '%{http_code}\n' <url>

# Repo validation
python3 tools/quick_validate.py skills/source --all

# Single-skill validation
python3 tools/quick_validate.py skills/source/core/frappe-core-database
```
