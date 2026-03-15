# AI Team — Build Your AI Virtual Team with Claude Code

[中文版](README_zh.md)

Use Claude Code's Skill mechanism to organize AI into a virtual team with **clear roles, seamless collaboration, and orchestrated workflows**.

## What Is This

A set of practical guides that teach you how to:

- Define AI "employees" for different roles (product manager, frontend developer, code reviewer, data analyst, etc.)
- Enable automatic collaboration between employees to chain complex tasks
- Seamlessly integrate an AI team into your existing projects

Each "employee" is essentially a **Skill**, composed of a `SKILL.md` (job description) + supporting resources (reference docs, scripts, templates).

## Guides

| Guide | Description | Best For |
|-------|-------------|----------|
| [Virtual Company Setup](docs/virtual-company-guide.md) | Build a complete virtual company from scratch, including departments, employee definitions, and collaboration mechanisms | Users starting from zero |
| [Integrate into Existing Projects](docs/integrate-ai-team-guide.md) | Add an AI team to an existing codebase so employees understand your code and conventions | Developers with existing projects |
| [Automated Workflows](docs/auto-workflow-guide.md) | Three automation approaches: orchestrator Skill, CLAUDE.md global rules, and script-driven pipelines | Users who want the team to work autonomously |

> Note: The guides are currently written in Chinese (Simplified).

## Core Concepts

### Skill = Employee

```
departments/engineering/frontend-dev/
├── SKILL.md              # YAML frontmatter (trigger conditions) + Markdown body (work instructions)
├── references/           # Reference docs (coding standards, templates, etc.)
├── scripts/              # Automation scripts
└── assets/               # Template files
```

### Three-Layer Context Loading

| Layer | Content | When Loaded |
|-------|---------|-------------|
| Layer 1 | name + description | Always in context |
| Layer 2 | SKILL.md body | Loaded on trigger |
| Layer 3 | references / scripts | Loaded on demand |

### Orchestration

Three approaches, from conversational to fully automated, that can be combined:

1. **Orchestrator Skill** (CTO) — Decompose tasks, assign employees, chain workflows
2. **CLAUDE.md Global Rules** — Define company rules and employee roster, auto-loaded on startup
3. **Script-Driven** — `run-workflow.sh` to launch a full pipeline with one command

## Team Roster

| Department | Employee | Key References / Scripts |
|-----------|----------|------------------------|
| **Product** | product-manager | `prd-template.md`, `user-story-guide.md` |
| | ux-designer | `design-principles.md` |
| **Engineering** | frontend-dev | `code-standards.md` |
| | backend-dev | `api-conventions.md` |
| | code-reviewer | `lint-check.sh` |
| **Marketing** | content-writer | `brand-voice.md` |
| | seo-specialist | `seo-checklist.md` |
| **Operations** | data-analyst | `report-generator.py` |
| | project-manager | `sprint-template.md` |
| **HR** | hr-specialist | — |

## Quick Start

1. Pick a guide and start reading
2. Create your first employee `SKILL.md`
3. Test with a small task (e.g., "build a button component")
4. Iterate based on results, gradually adding more employees

## License

[Apache License 2.0](LICENSE)
