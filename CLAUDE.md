# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation project providing guides for building "AI virtual companies" using Claude Code Skills. It contains Chinese-language guides (in `docs/`) that teach users how to organize AI team members as Skills with `SKILL.md` files, set up task orchestration workflows, and integrate AI teams into existing codebases.

Licensed under Apache 2.0.

## Repository Structure

```
docs/
├── virtual-company-guide.md    # How to set up a virtual company with departments and Skills
├── integrate-ai-team-guide.md  # How to integrate an AI team into an existing project
└── auto-workflow-guide.md      # How to orchestrate multi-step workflows (CTO Skill, CLAUDE.md rules, shell scripts)
```

There is no source code, build system, or test suite — this repo is purely documentation.

## Key Concepts

- **Skill = Employee**: Each AI "employee" is defined by a `SKILL.md` file (YAML frontmatter for trigger conditions + Markdown body for work instructions) plus optional `references/`, `scripts/`, and `assets/` directories
- **Three-layer context loading**: (1) name + description always loaded, (2) SKILL.md body loaded on trigger, (3) references loaded on demand
- **Orchestration patterns**: CTO/PM Skill for task decomposition, CLAUDE.md for global rules, shell scripts (`claude -p`) for fully automated pipelines
- **Project integration**: Add `.ai-team/` directory + `CLAUDE.md` + `.claude/settings.json` to any existing project

## Writing Guidelines

- All documentation is written in Chinese (Simplified)
- Guides use practical examples with concrete directory structures and code snippets
- Each guide is self-contained and can be read independently
