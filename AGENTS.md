# AGENTS.md

> **Design principle:** This file contains only information you cannot infer by
> reading the repository. It deliberately omits workflow checklists, architectural
> overviews, and general best-practice reminders. See the research basis below.

**Project:** RDHPCS Documentation — published at <https://docs.rdhpcs.noaa.gov>

---

## Research basis for this file's scope

This file follows the recommendations of Gloaguen et al. (ETH Zurich, 2026),
"Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding
Agents?" (arXiv:2602.11988). Key findings:

- LLM-generated context files reduce task success rates and raise inference
  costs by over 20% by encouraging unnecessary exploration.
- Human-written files provide a marginal positive effect only when limited to
  requirements the agent cannot infer independently.
- General instructions (architecture overviews, standard tooling guidance,
  common best practices) produce no measurable benefit and increase cost.

**Everything in this file is here because it cannot be inferred from reading
the repository.** If a rule feels obvious, it does not belong here.

---

## Non-inferable project rules

### Authority chain for conflicts
When `WRITING_GUIDE.md` and `CODE_STYLE.md` contradict each other:
- Prefer `WRITING_GUIDE.md` for prose decisions.
- Prefer `CODE_STYLE.md` for markup decisions.

### US government plain language obligation
This site documents federal HPC systems and is subject to the **Plain Writing
Act of 2010** (Pub. L. 111-274). Every page you write or edit must satisfy
[PlainLanguage.gov](https://www.plainlanguage.gov) guidelines. The most
task-relevant requirements are:

- Active voice; address the reader as "you."
- Sentence target: ≤ 20 words on average.
- Expand every acronym on first use per page.
- Use numbered lists for sequential steps; bulleted lists for non-sequential
  items of three or more.
- Page titles for task pages must be actionable phrases
  (for example, "Connect to the login nodes" not "Login node connectivity").

### Do not fabricate system-specific values
Never invent queue names, partition names, node counts, memory limits, storage
paths, module names, software versions, or environment variable names. If a
required value is unavailable, insert a `.. todo::` directive with a specific
description of what is missing.

### Never commit `build/` output
The `build/` directory is generated content. It must not be committed.

### Contribution workflow
The workflow requirements in [CONTRIBUTING.md](CONTRIBUTING.md) apply equally
to agent actions and are non-negotiable. Key constraints:

- Open a GitHub issue describing the change before starting any work.
- Branch off an up-to-date `main` branch; submit changes via pull request to `main`.
- Keep each pull request as small as possible. Split large changes into separate,
  logical PRs.
- A PR must pass all build tests with zero warnings or errors before it can be
  accepted.

---

## Permitted autonomous actions

| Action | Scope |
|---|---|
| Edit existing documentation pages | Content directories only (see Source Directory Reference below) |
| Create new documentation pages | Content directories only (see Source Directory Reference below). Add the new filename to the `.. toctree::` directive in that directory's `index.rst`. |
| Run linters and validators | `doc8`, `sphinx-build` |
| Commit, push, and open PR | Commit and push to current feature branch only; changes reach `main` via pull request |

### Source directory reference

The directories under `source/` map to the site's sidebar navigation topics.

**Content directories** — permitted for new pages and edits:

| Directory | Topic |
|---|---|
| `accounts/` | Account management and access |
| `connecting/` | Connecting to RDHPCS systems |
| `data/` | Data management and storage |
| `slurm/` | Slurm workload manager |
| `software/` | Available software and modules |
| `systems/` | System descriptions and specifications |

**Restricted directories** — do not create new `.rst` pages; specific rules apply:

| Directory | Rule |
|---|---|
| `help/` | Edit only when explicitly instructed by the user. |
| `queue_policy/` | Edit only when explicitly instructed by the user. |
| `FAQ/` | Deprecated. Do not add new pages. |
| `files/` | Shared data files only (CSV, reusable RST fragments). No `.rst` documentation pages. |
| `_static/`, `_templates/`, `_templates_github/` | Hard stop — see below. |

---

## Hard stops — always ask before proceeding

Stop and ask the user if any task requires:

- Renaming or deleting an `.rst` file
- Changing a heading or `.. _label:` anchor in an existing page
- Editing `conf.py`, `_static/`, or `_templates/`
- Adding a Sphinx extension or Python dependency
- Pushing to `main`, `master`, `release/*`, or `stable/*`, or merging a pull request
- Any CI/CD pipeline change
- Creating a new top-level topic directory under `source/` — topic structure is a content architecture decision
- Editing any file under `help/` or `queue_policy/` without explicit user instruction

---

## Custom build commands

Commands use explicit `.venv/bin/` prefixes rather than relying on shell
activation. Shell `source` commands may not persist across discrete tool
calls — using the venv binary path directly is safer and more explicit.

If `.venv/` does not exist, create it first:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

```bash
# Full HTML build
.venv/bin/sphinx-build -b html source build/html

# Link validation
.venv/bin/sphinx-build -b linkcheck source build/linkcheck

# Markup linter
.venv/bin/doc8 source
```

Build must produce zero errors and zero warnings before committing.

---

## Escalation

Stop and report to the user if:

- A linter error requires changing project-level configuration to resolve.
- A factual inconsistency between pages cannot be resolved from the repository.
- Any required system-specific value (queue name, path, module version) is
  absent from the repository — use `.. todo::` and report what is missing.
