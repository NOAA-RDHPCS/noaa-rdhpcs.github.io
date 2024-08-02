.. _Contributing:

******************************
Contributing to these docs
******************************

Overview
========

To improve the appearance and functionality of our user documentation,
as of Summer 2024 we’ve transferred the MediaWiki-based documentation
spread across multiple instances to this single site
`docs.rdhpcs.noaa.gov <https://docs.rdhpcs.noaa.gov>`_ The files are
kept in the `NOAA-RDHPCS Github repository
<https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/issues/new>`_,
edited either in your browser or favorite editor, using
reStructuredText (RST) as the markup language and rendered into HTML
by Sphinx.  All these steps including checks for correct markup
syntax, valid links, and others, are automated using Github flows.

Process
-------

Changes are tracked using Github issues, submitted using Pull Requests
(PRs), and reviewed for approval and syntax by members of the Docs
team prior to publication.  Issues are reviewed regularly and the team
aims for a timely response.

Issues will have labels to help guide the focus -- eg, an HPCS
specific item vs a general question.  Additional labels will be
created as needed.

Submitting suggestions
----------------------

Have a suggestion for improvement? Start the conversation by using
Github to `open an issue
<https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/issues/new>`_.

If a Github account is needed, `follow these steps
<https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account>`_

Contributing changes
--------------------

The most direct method to contribute changes is to use the Github web
browser interface to create and submit changes via a Pull Request
(PR).

For those unfamiliar with these tools and flows, we have created a
webcast tutorial for this!  Please make sure you are logged into your
Google NOAA account, then access this `webcast tutorial
<https://drive.google.com/file/d/1MdCbUExf3prY0OF-6CRc3EY1-UPSSwCE>`_

For those comfortable with the command line and wanting to edit or
preview changes on your own system, please see :ref:`Contributing via the
CLI <via_cli>` for details on how to install the Python based
Sphinx tools and use the `git` commands for the fork, clone, commit,
and push actions that comprise the Docs workflow.

GitHub Guidelines
===================

Here are some guidelines and common practices that we use in this project.

- When you want to work on an issue, assign it to yourself if no one
  is assigned yet. If there is somebody assigned, check in with that
  person about collaborating.
- Reference the issue(s) that your PR addresses with GitHub's '#' notation.
- Use "WIP" in your PR title to indicate that it should not be merged yet.
  Remove just the WIP when you are ready for it to be merged.
- If you think certain individuals should be aware of your proposed changes,
  suggest them as reviewers on the PR.
- You do not need to assign labels to your PR, but you may do so if you have
  suggestions. However, be aware that the labels might get changed.


Workflow for contributions to the documentation repository
===============================================================

1. Open an issue in the NOAA-RDHPCS/noaa-rdhpcs.github.io repository

   The issue should describe the issue with the documentation, the
   desired change, etc.

2. Fork and clone, or just clone the repository.

   The choice depends on whether the person making the change is a
   member of the NOAA-RDHPCS GitHub organization or not:

   a. If a member: Clone the repository
        (git clone git@github.com:NOAA-RDHPCS/noaa-rdhpcs.github.io.git).
   b. If not a member: Use the "fork and pull request" workflow:
        https://docs.github.com/en/pull-requests/collaborating-with-pull-requests

3. Create a new git branch in the local clone.

   The name of the branch doesn't matter, but it should be enough to
   indicate what is being done. Generic names (e.g., "updates",
   "fixes", etc.) do not help the developer or the reviewer recognize
   what is included. (git checkout -b new.branch.name).

4. Modify the documentation.

   As mentioned previously, and as a good best-practice, only include
   one set of changes in each branch. That is, do not update multiple
   pages with new, unrelated text.

5. Commit the change.

   The commit message should describe what is changed, why, etc.  (see
   https://cbea.ms/git-commit/). The standard is to use at least two
   lines. The first line is a subject line, somewhat terse but
   descriptive (e.g., "Add scp transfer to data page"). The other
   line(s) should be more specific about what changes (e.g., added
   info for uses to scp data to the external DTNs).

6. Push the branch.

   Where will determine if a member of the organization or not, but
   is typically: git push origin new.branch.name

7. Open a pull request (PR) in NOAA-RDHPCS/noaa-rdhpcs.github.io.

   Add any additional information the reviewer(s) will need in the PR
   description. If the PR is tied to any issues, mention the issues
   using the #. You can even `use keywords
   <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests>`_
   to perform other automated workflow items (e.g., automatically
   close issues).

8. Work with the reviewers to refine the update as needed.

   This will typically be to help refine the text to make it easier to
   understand, flow better, or adjust the layout. They may also
   request changes to allow the automated testing to pass as there are
   automated checks (CI) tests to ensure the `NOAA-RDHPCS Docs
   flexible style guide
   <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/CODE_STYLE.md>`_
   is followed.



Resources
===================

| `Sphinx Quickstart <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_
| `restructuredText Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
| `restructuredText Reference <http://docutils.sourceforge.net/rst.html>`_
| `NOAA-RDHPCS Docs flexible style guide <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/CODE_STYLE.md>`_

