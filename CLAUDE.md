# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation + reference implementation project for building "AI virtual companies" using Claude Code Skills. It contains Chinese-language guides (in `docs/`) and a working virtual company structure (in `departments/` and `shared/`) with 10 English-language employee Skills across 5 departments.

Licensed under Apache 2.0.

## Repository Structure

- `docs/` — Chinese-language guides (numbered, self-contained)
  - `1.virtual-company-guide[DONE].md` — Setting up a virtual company from scratch
  - `2.auto-workflow-guide.md` — Multi-step workflow orchestration
  - `3.integrate-ai-team-guide.md` — Adding an AI team to an existing project
- `departments/` — Working virtual company with SKILL.md definitions (all in English)
  - `product/` — product-manager, ux-designer
  - `engineering/` — frontend-dev, backend-dev, code-reviewer
  - `marketing/` — content-writer, seo-specialist
  - `operations/` — data-analyst, project-manager
  - `hr/` — hr-specialist
- `shared/` — Company-wide resources referenced by all employees: `company-context.md`, `tone-guide.md`, `glossary.md`

There is no build system or test suite — this repo is documentation and Skill definitions.

## Key Concepts

- **Skill = Employee**: Each AI "employee" is a `SKILL.md` file (YAML frontmatter for trigger conditions + Markdown body for work instructions) plus optional `references/`, `scripts/`, and `assets/` directories
- **Three-layer context loading**: (1) name + description always loaded, (2) SKILL.md body loaded on trigger, (3) references loaded on demand
- **Orchestration patterns**: CTO/PM Skill for task decomposition, CLAUDE.md for global rules, shell scripts (`claude -p`) for fully automated pipelines
- **Cross-referencing**: Skills reference each other by name in their "Collaboration" sections and reference `shared/` resources for company context

## Writing Guidelines

- **Guides** (`docs/`): Written in Chinese (Simplified), each guide is self-contained with practical examples and concrete directory structures
- **SKILL.md files and references** (`departments/`, `shared/`): Written in English
- Both READMEs (EN + ZH) exist and should be kept in sync when adding content that appears in both
