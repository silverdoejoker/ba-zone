# Tech Stack

## Type
This is a **documentation/prompt engineering project** — no application code, build system, or runtime dependencies. There is no package manager, compiler, or test runner.

## Format
All files are **Markdown (.md)**. No other file formats are used.

## AI Runtime
Designed to run as a skill inside:
- **Claude AI Projects** (upload folder to project knowledge)
- **Kiro** (place in `/mnt/skills/user/` for auto-detection)

The entry point is `SKILL.md`, which contains the full behavioral instructions for the AI.

## No Build / Test Commands
There is no build, compile, lint, or test command. Validation is done manually by testing the skill against sample prompts.

## Contribution Workflow
```
git checkout -b feat/improve-xxx
# make changes
# test skill with at least 3 different scenarios
# update references/examples.md if adding new patterns
git commit -m "..."
# submit PR with clear description
```
