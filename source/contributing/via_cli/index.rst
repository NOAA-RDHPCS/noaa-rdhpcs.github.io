.. _via_cli:

******************************
Contributing via the CLI
******************************

The instructions below are focused on Linux and Mac systems, with a
prerequisite that you have a recent version of Python installed on
your system.

Setup authoring environment
==============================

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

#. Install Sphinx and the ReadTheDocs theme locally::

        $ pip3 install -r requirements.txt

   This can be in your home area, a virtual environment, container, etc.

    Go to https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/requirements.txt
    to see the list of Python packages inside ``requirements.txt``.


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

   Open a browser and type ``localhost:8080`` into the address bar to view the web pages.

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

| `Sphinx Quickstart <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_
| `restructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
| `restructuredText Reference <https://docutils.sourceforge.net/rst.html>`_
| `NOAA-RDHPCS Docs flexible style guide <https://github.com/NOAA-RDHPCS/noaa-rdhpcs.github.io/blob/main/CODE_STYLE.md>`_
