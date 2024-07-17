###########################
Contributing to these docs
###########################

Submitting suggestions
====================================

Have a suggestion for improvement? To share it with us, `open an issue
<https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/issues/new>`_.

Getting Started with GitHub
=============================

If you need a GitHub account, `follow these steps
<https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account>`_

If you're not sure how to get started, `we have an Overview
<https://drive.google.com/file/d/1MdCbUExf3prY0OF-6CRc3EY1-UPSSwCE/view>`_

Authoring content
==================

Setup authoring environment
----------------------------

#. Install Sphinx and the ReadTheDocs theme locally::

        $ pip3 install sphinx sphinx_rtd_theme sphinx-panels

   This can be in your home area, a virtual environment, container, etc.


#. Fork the documentation repository on GitHub

    Go to https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io, and click the "Fork"
    button in the upper right corner.

    .. image:: /images/github_fork.png
       :width: 80.0%
       :align: center


#. Clone your fork of the documentation repository::

    $ git clone https://github.com/<your-github-id>/noaa-rdhpcs.github.io.git

#. Point your master branch to track upstream::

    $ cd noaa-rdhpcs.github.io
    $ git remote add rdhpcs https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io.git
    $ git fetch rdhpcs
    $ git branch --set-upstream-to=rdhpcs/main

#. Build the docs::

    $ make html

#. Locally preview the generated web pages

   Start a webserver on something like ``localhost:8080`` that points at
   your ``noaa-rdhpcs.github.io/build/html`` directory. For example, using busybox::

        $ busybox httpd -p 127.0.0.1:8080 -h /home/ubuntu/noaa-rdhpcs.github.io/build/html

   or a python webserver (from inside the document root, i.e., ``build/html`` directory)::

        $ cd build/html
        $ python3 -m http.server 8080
        ## you may add the option --bind 127.0.0.1 to bind only on the localhost address

   Open a broswer and type ``localhost:8080`` into the address bar to view the web pages.

Edit the docs
-------------------------

After having set up your environment as described above, you can reuse your
local environment to make multiple changes.

#. Update your local clone from the upstream repository::

      $ git checkout main
      $ git pull

#. Make your edits in a new git branch::

      $ git checkout -b my-edits-branch
      ## make edits to *.rst files, using an editor like vi
      ## after my-edits-branch is created, omit the -b flag to switch to it from the master

#. Preview your edits

    Follow the steps in the previous section to rebuild and locally
    view changes

#. Add and commit your edits to your branch::

      $ git add edited_file1.rst edited_file2.rst
      $ git commit -m "message summarizing your edits"


#. Push your edits to your GitHub fork::

      $ git push -u origin my-edits-branch

#. Open a pull request on github

    After you push your branch, you should see a button to open a pull request.

    .. image:: /images/github_pr.png
       :width: 80.0%
       :align: center

Resources
---------------

| `Sphinx Quickstart <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_
| `restructuredText Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
| `restructuredText Reference <http://docutils.sourceforge.net/rst.html>`_

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
