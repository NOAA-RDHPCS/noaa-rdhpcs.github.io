.. meta::
   :description: How to contribute to RDHPCS documentation, including
    opening an issue, editing in the browser or in GitHub Codespaces,
    setting up a development environment, building and validating the
    docs, and submitting a pull request.
   :keywords: contributing, documentation, pull request, fork, Sphinx,
    reStructuredText, RST, GitHub, Codespaces, dev container

.. _Contributing:

******************************
Contributing to these docs
******************************

Overview
========

This site, `docs.rdhpcs.noaa.gov <https://docs.rdhpcs.noaa.gov>`__, is the
single source for RDHPCS user documentation.  Source files are kept in the
`NOAA-RDHPCS GitHub repository
<https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io>`__, written in
reStructuredText (RST), and rendered into HyperText Markup Language (HTML)
web pages by Sphinx.  Automated checks validate markup syntax, links, and
style on every pull request.

Before contributing, review `CONTRIBUTING.md`_ in the repository root.
It covers the Code of Conduct, issue and pull request guidelines, commit
message format, source directory structure, and code style requirements
that apply to all contributions.

Before you start
================

Every contribution starts with a GitHub issue and your own fork of the
repository.  Complete these steps before you edit any files.

#. Get a GitHub account.

   If you don't have one, `follow these steps
   <https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account>`__.

#. Find or open an issue that describes the change.

   First, search the `open issues
   <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/issues>`__ to see
   if someone has already reported the change.

   - **If an issue already exists**, read it and check whether someone is
     assigned.  If no one is assigned, leave a comment that you plan to
     work on it.  If someone is assigned, comment to ask whether you can
     help before you start.

   - **If no issue exists**, go to the `new issue page
     <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/issues/new>`__.
     Give the issue a short, descriptive title.  In the description,
     explain the change and why it's needed, and include links to any
     references.  If you plan to make the change yourself, say so in the
     description.

   If you have permission to assign issues, assign the issue to yourself.
   Write down the issue number.  You will reference it in your commits and
   pull request.

   For details, see GitHub's guides to `searching issues
   <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests>`__,
   `creating an issue
   <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue>`__,
   and `assigning issues
   <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users>`__.

   .. note::

      If you only want to suggest a change, you can stop after you open
      the issue.  The documentation team will follow up on it.

#. Fork the repository.

   You only need to do this once.  Go to
   https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io and click the
   **Fork** button in the upper-right corner.  Select your account and click
   **Create fork**.

   .. image:: /images/github_fork.png
      :width: 80.0%
      :align: center
      :alt: GitHub Fork button in the upper-right corner of the repository page

   See GitHub's guide to `forking a repository
   <https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo>`__.

#. Sync your fork.

   Do this before each new change, so your work starts from the latest
   ``main`` branch.  On the main page of your fork, click **Sync fork**,
   then click **Update branch**.  If GitHub reports that your branch is up
   to date, there is nothing to do.

   See GitHub's guide to `syncing a fork
   <https://docs.github.com/en/pull-requests/how-tos/work-with-forks/syncing-a-fork>`__.

Choose how to edit
==================

You can edit in your browser or set up a development environment.  Pick
the method that fits your change.

.. list-table::
   :header-rows: 1
   :widths: 25 25 15 35

   * - Method
     - What you need
     - Preview
     - Best for
   * - Simple editor
     - A web browser
     - No
     - A small change to a single file
   * - GitHub Codespaces in your browser
     - A web browser
     - Yes
     - Any change, without installing anything
   * - GitHub Codespaces in Visual Studio Code
     - Visual Studio Code
     - Yes
     - Any change, using your own editor and settings
   * - Dev container on your computer
     - Visual Studio Code and a container engine, such as Docker
     - Yes
     - Working offline from a local clone
   * - Python virtual environment
     - Python 3.12 or newer and ``make``
     - Yes
     - Working from the command line

GitHub Codespaces runs the repository's development container (dev
container) in the cloud.  The dev container sets up Python and all
required packages for you.  It shows a live preview of the rendered site,
and you can run the same checks as the pull request build.

.. note::

   You can also use GitHub Codespaces for simple changes.  It takes a few
   minutes to start the first time, but you can then see the rendered
   page before you submit a pull request.

.. note::

   GitHub Codespaces includes a monthly amount of free use for personal
   accounts.  When you finish, stop or delete your codespace from
   https://github.com/codespaces so it does not use your free hours.
   See GitHub's guides to `Codespaces billing
   <https://docs.github.com/en/billing/concepts/product-billing/github-codespaces>`__,
   `stopping a codespace
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace>`__,
   and `deleting a codespace
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace>`__.

Edit in your browser
====================

Use these steps with the simple editor or GitHub Codespaces in your
browser.  First complete the steps in `Before you start`_.

#. Open an editor in your fork.

   **Simple editor**: Navigate to the file you want to edit, then click the
   **pencil icon** (Edit this file) in the upper-right corner of the file
   view.  See GitHub's guide to `editing files
   <https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files>`__.

   **GitHub Codespaces**: On the main page of your fork, click the green
   **Code** button, select the **Codespaces** tab, and click **Create
   codespace on main**.  Wait for the first build to finish.  It creates
   the ``.venv`` virtual environment and installs the required packages.
   See GitHub's guide to `creating a codespace
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository>`__.

#. Create a new branch for your changes.

   .. note::

      Always create a new branch rather than committing directly to ``main``.
      This keeps your default branch clean and lets you have multiple
      contributions open at once.

   **Simple editor**: You create the branch when you commit your changes
   — no action needed here.

   **GitHub Codespaces**: Click the branch name in the bottom status bar.
   Select **Create new branch**, type a short descriptive branch name, and
   press ``Enter``.  See GitHub's guide to `using source control in your
   codespace
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace>`__.

#. Edit the file.

   Make your changes in the editor.  The simple editor has a **Preview** tab,
   but it renders raw RST — not the final built HTML.

#. Preview and check your changes.

   **Simple editor**: You can't preview or check the rendered pages.  The
   automated checks catch markup errors after you open a pull request.

   **GitHub Codespaces**: When the codespace starts, it runs a live preview
   of the site on port 8000.  Click **Open in Browser** in the notification,
   or open the **Ports** tab and click the globe icon next to port 8000.
   When you save a file, the preview rebuilds and the page reloads.  See
   GitHub's guide to `forwarding ports in your codespace
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace>`__.

   The live preview doesn't run the same checks as the pull request build.
   Before you commit, run these commands in the codespace terminal
   (**Terminal** > **New Terminal**).  See `Build and validate`_ for
   details.

   .. code-block:: shell

      $ make html
      $ make linkcheck
      $ make lint

#. Commit your changes.

   **Simple editor**: Scroll to the top and click **Commit changes**.  Enter
   a commit message, select **Create a new branch for this commit**, give the
   branch a short descriptive name, and click **Propose changes**.

   **GitHub Codespaces**: Click the **Source Control icon** in the left
   sidebar (or press ``Ctrl+Shift+G``).  Click **+** next to each changed
   file to stage it.  Enter a commit message and click **Commit**.  Then
   click **Publish Branch** to push your branch to your fork.

#. Open a pull request.

   After proposing changes in the simple editor, GitHub takes you directly
   to the **Open a pull request** page.  After you publish a branch from
   GitHub Codespaces, go to your fork on GitHub and click **Compare & pull
   request**.

   Fill in a descriptive title and description.  Reference your issue using
   ``#<issue number>``.  Click **Create pull request**.  See GitHub's guide
   to `creating a pull request from a fork
   <https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork>`__.

   .. image:: /images/github_pr.png
      :width: 80.0%
      :align: center
      :alt: GitHub prompt to open a pull request after pushing a branch

#. Work with the reviewers to refine the update as needed.

Set up a development environment
================================

Set up a development environment if you prefer to work in Visual Studio
Code (VS Code) on your computer or from the command line.  First complete
the steps in `Before you start`_.  Then choose one of the options below.
After setup, follow `Build and validate`_ and `Edit and submit`_.

Option A: Use a codespace from VS Code
--------------------------------------

This option runs the dev container in GitHub Codespaces, but you edit in
VS Code on your computer.  You don't need Docker or Python.

#. Install `VS Code <https://code.visualstudio.com/>`__ and the `GitHub
   Codespaces extension
   <https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces>`__.

#. Sign in to GitHub from VS Code when the extension prompts you.

#. Open the Command Palette (``Ctrl+Shift+P``, or ``Cmd+Shift+P`` on
   macOS) and run **Codespaces: Create New Codespace**.

#. Select your fork of ``noaa-rdhpcs.github.io``, then the ``main``
   branch.  Wait for the first build to finish.

#. Add the upstream remote in the VS Code terminal.  See
   `Add the upstream remote`_.

To reopen the codespace later, run **Codespaces: Connect to Codespace**
from the Command Palette.  See GitHub's guide to `using GitHub Codespaces
in Visual Studio Code
<https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code>`__.

Option B: Use the dev container on your computer
------------------------------------------------

This option runs the dev container on your computer.  You need VS Code,
the `Dev Containers extension
<https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`__,
and a container engine, such as `Docker <https://www.docker.com/>`__.

.. note::

   The dev container has only been tested with Docker.  Other container
   engines that the Dev Containers extension supports, such as Podman,
   should also work.  See `Alternate ways to install Docker
   <https://code.visualstudio.com/remote/advancedcontainers/docker-options>`__
   for the engines the extension supports.

#. Clone your fork and add the upstream remote.  See `Clone your fork`_
   and `Add the upstream remote`_.

#. Open the cloned folder in VS Code.

#. When prompted, select **Reopen in Container**.  You can also run
   **Dev Containers: Reopen in Container** from the Command Palette.

#. Wait for the first build to finish.  It creates the ``.venv`` virtual
   environment and installs the required packages.

When the container starts, it runs a live preview of the site on port
8000.  Open ``http://localhost:8000`` in your browser.  When you save a
file, the preview rebuilds and the page reloads.  If the preview stops,
restart it in the VS Code terminal:

.. code-block:: shell

   $ .devcontainer/start-preview.sh

Option C: Use a Python virtual environment
------------------------------------------

This option requires `Python <https://www.python.org/downloads/>`__ 3.12
or newer, ``git``, and ``make``.  The site is built and tested with
Python 3.12, and the version of Sphinx it uses requires Python 3.12 or
newer.

#. Clone your fork and add the upstream remote.  See `Clone your fork`_
   and `Add the upstream remote`_.

#. Create the virtual environment and install the required packages.

   .. code-block:: shell

      $ make venv

   This creates the ``.venv`` directory from `requirements.txt
   <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/requirements.txt>`__.
   You only need to do this once.  The ``make`` commands use the
   programs in ``.venv`` directly, so you don't need to activate the
   virtual environment.

Clone your fork
---------------

Options B and C need a copy of your fork on your computer.

.. code-block:: shell

   $ git clone https://github.com/<your-github-id>/noaa-rdhpcs.github.io.git
   $ cd noaa-rdhpcs.github.io

Replace ``<your-github-id>`` with your GitHub username.  See GitHub's
guide to `cloning a repository
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`__.

Add the upstream remote
-----------------------

The upstream remote points to the official repository, so you can get
the latest changes from it.  Run these commands from the repository
root.

.. code-block:: shell

   $ git remote add upstream https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io.git
   $ git fetch upstream

If ``git`` reports that the ``upstream`` remote already exists, you can
skip this step.  See GitHub's guide to `configuring a remote repository
for a fork
<https://docs.github.com/en/pull-requests/how-tos/work-with-forks/configuring-a-remote-repository-for-a-fork>`__.

Build and validate
==================

After setup, use these commands from the repository root.  All must complete
with zero errors and zero warnings before you commit or submit a pull request.

**Build HTML**
   .. code-block:: shell

      $ make html

**Preview**
   In a codespace or the dev container, use the live preview on port
   8000.  It is already running.

   With a Python virtual environment, build the site and start a local
   web server:

   .. code-block:: shell

      $ make serve

   Open ``http://localhost:8000``.  Press ``Ctrl+C`` to stop.  If port
   8000 is in use, run ``make serve PORT=8080`` and open
   ``http://localhost:8080`` instead.

**Check links**
   .. code-block:: shell

      $ make linkcheck

**Lint markup**
   .. code-block:: shell

      $ make lint


Edit and submit
===============

After your environment is set up, follow these steps for each contribution.

.. note::

   In VS Code, you can use the **Source Control** view (``Ctrl+Shift+G``)
   instead of the ``git`` commands to create branches, stage files,
   commit, and push.

#. Update your local copy from upstream.

   .. code-block:: shell

      $ git checkout main
      $ git pull upstream main

#. Create a new branch for your changes.

   .. code-block:: shell

      $ git checkout -b my-edits-branch

#. Make your edits to the relevant ``.rst`` files.

   Keep one logical change per branch — don't bundle unrelated edits.
   See `CONTRIBUTING.md`_ for guidance on which directories to edit
   and which to avoid.

#. Rebuild and preview your changes (see `Build and validate`_ above).

#. Stage and commit your changes.

   .. code-block:: shell

      $ git add <file1.rst> <file2.rst>
      $ git commit -m "Add scp transfer to data page"

   Replace ``<file1.rst> <file2.rst>`` with the actual filenames you changed.

   Write commit messages in the imperative mood with a subject line of 50
   characters or fewer.  Add a body if the reason for the change is not
   obvious.  Reference the related issue with ``#<issue number>``.  See
   `CONTRIBUTING.md`_ for the full commit message guidelines.

#. Push your branch to your fork.

   .. code-block:: shell

      $ git push -u origin my-edits-branch

   The ``-u`` flag links your local branch to the remote so that
   future pushes on this branch only need ``git push``.

#. Open a pull request on GitHub.

   After pushing, GitHub displays a prompt to open a pull request.

   .. image:: /images/github_pr.png
      :width: 80.0%
      :align: center
      :alt: GitHub prompt to open a pull request after pushing a branch

   Include a description of your changes and reference your issue.
   The automated checks must pass before the PR can be merged.  See
   GitHub's guide to `creating a pull request from a fork
   <https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork>`__.

#. Work with the reviewers to refine the update as needed.


Pull request tips
=================

- Reference the issue(s) your pull request (PR) addresses using GitHub's
  ``#`` notation.  See GitHub's guide to `linking a pull request to an
  issue
  <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`__.
- If your changes aren't ready for review, open a draft PR.  When you
  create the PR, click the arrow next to **Create pull request** and
  select **Create draft pull request**.  GitHub doesn't allow a draft PR
  to be merged.  When your changes are ready, click **Ready for review**
  on the PR.  See GitHub's guides to `draft pull requests
  <https://docs.github.com/en/pull-requests/reference/pull-requests#draft-pull-requests>`__
  and `changing the stage of a pull request
  <https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-stage-of-a-pull-request>`__.
- If specific individuals should be aware of your changes, suggest them as
  reviewers on the PR.  See GitHub's guide to `requesting a pull request
  review
  <https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/requesting-a-pull-request-review>`__.
- You don't need to assign labels to your PR. The team may adjust them.


Resources
=========

| `Sphinx Quickstart <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_
| `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
| `reStructuredText Reference <https://docutils.sourceforge.net/rst.html>`_
| `GitHub Codespaces documentation <https://docs.github.com/en/codespaces>`_
| `NOAA-RDHPCS Docs style guide <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/CODE_STYLE.md>`_
| `NOAA-RDHPCS Docs writing guide <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/WRITING_GUIDE.md>`_

.. _CONTRIBUTING.md: https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/CONTRIBUTING.md
