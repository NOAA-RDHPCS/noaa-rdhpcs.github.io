# Contributing To RDHPCS Documentation

Thank you for taking time to contribute.

This repository contains the source for the RDHPCS Documentation located at
https://docs.rdhpcs.noaa.gov.

Contributions to this project are released to the public under the
[project's open source license](LICENSE).

What follows is a set of guidelines and how-tos for contributing to RDHPCS Documentation.
These are guidelines, not rules.  Use your best judgment and feel free to
propose changes to this document in a pull request.

Table of Contents
* [Code of Conduct](#code-of-conduct)
* [Quick start workflow](#quick-start-workflow)
* [Issues](#issues)
* [Pull requests](#pull-requests)
* [Source directory structure](#source-directory-structure)
* [Commit messages](#commit-messages)
* [Building and testing locally](#building-and-testing-locally)
* [Code style](#code-style)

## Code of Conduct

This project and everyone participating in it is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to
uphold this code. Please report unacceptable behavior to
[rdhpcs.help@noaa.gov](mailto:rdhpcs.help@noaa.gov).

## Quick start workflow

1. Create an issue that describes the change
2. Fork the project
3. Create a feature branch off an up-to-date `main` branch
4. Update and commit the changes
5. Push the commits to your fork
6. Submit a pull request to the `main` branch

## Issues

When contributing to this project, please first open an issue.  The issue title
should be short and descriptive.  The issue description should be clear and
concise.  Include enough information to help others reproduce the issue, or
understand the change requested.  Use [GitHub flavored
markdown](https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to format the
message, and include links to references.

## Pull requests

Submit pull requests for bug fixes, improvements, or issues to particular
problems in the documentation.

Please keep the changes in a single pull to be as small as possible to help
reviewer(s) quickly evaluate changes.  If you do have a large update, try to
split the update into small, logical pull requests.

Please refer to the [Contributing to these
docs](https://docs.rdhpcs.noaa.gov/contributing/) to review how to build and
test the updates.  All pull requests must pass all build tests without warnings
or errors prior to being accepted.

Once a pull request is created, a member of the RDHPCS Documentation team will
review the changes, and, if necessary, will work with the author of the pull
request to modify their changes for correctness, and format.

## Source directory structure

The `source/` directory maps directly to the site's sidebar navigation.
Each content subdirectory corresponds to a topic section on the published
site.  Do not create new top-level directories under `source/` without
first opening an issue to discuss the content architecture change.

Content directories available for new pages and edits:

| Directory | Topic |
|---|---|
| `accounts/` | Account management and access |
| `connecting/` | Connecting to RDHPCS systems |
| `data/` | Data management and storage |
| `slurm/` | Slurm workload manager |
| `software/` | Available software and modules |
| `systems/` | System descriptions and specifications |

The following directories are not content topics and should not receive
new documentation pages:

| Directory | Purpose |
|---|---|
| `help/` | Contact information for system and software support. Changes require explicit instruction from the documentation team. |
| `queue_policy/` | Policies and queue information undergoing restructuring. Changes require explicit instruction from the documentation team. |
| `FAQ/` | Deprecated. No new pages. Existing content will migrate to appropriate topic directories over time. |
| `files/` | Shared data files (CSV tables, reusable RST fragments). No `.rst` documentation pages. |
| `_static/` | Static assets (CSS, JavaScript, images). |
| `_templates/` | Sphinx HTML templates. |

## Commit messages

Write commit messages in the imperative mood, as if completing the
sentence "This commit will...".  Keep the subject line to 50 characters
or fewer and do not end it with a period.

```
Add Hera storage limits to data management page

Adds the /scratch and /work quota values confirmed by the systems team.
Closes #142.
```

The subject line should describe *what* changed.  If the reason is not
obvious, add a body separated from the subject by a blank line.  Wrap
the body at 72 characters.  Reference the related GitHub issue using
`#<issue number>` in the body or subject.

Keep one logical change per commit.  Do not bundle unrelated edits.

## Building and testing locally

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
```

On macOS and Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Build the HTML documentation:

```bash
make html
```

Run the link validator:

```bash
make linkcheck
```

Run the markup linter:

```bash
make lint
```

All commands must complete with zero errors and zero warnings before
you commit.  See [Contributing to these
docs](https://docs.rdhpcs.noaa.gov/contributing/) for a full walkthrough.

## Code style

Code updates should follow the coding style for the project, contained in
[CODE_STYLE.md](CODE_STYLE.md).
