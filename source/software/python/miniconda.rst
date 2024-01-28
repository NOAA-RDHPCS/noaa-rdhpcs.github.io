********************
Installing Miniconda
********************

While the RDHPCS system have Anaconda/Conda available, you can install your own
`Miniconda <https://docs.conda.io/en/main/miniconda.html>`__.

The install process is rather simple (with a few notable warnings, see
:ref:`Cautionary Notes <miniconda-notes>` further below):

.. code-block:: bash

   $ mkdir miniconda/
   $ cd miniconda/
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   chmod u+x Miniconda3-latest-Linux-x86_64.sh
   ./Miniconda3-latest-Linux-x86_64.sh -u -p ~/miniconda

* The ``-p`` flag specifies the prefix path for where to install miniconda.
* The ``-u`` updates any current installations at the ``-p`` location (not
  necessary if you didn't do a ``mkdir`` beforehand)

.. _miniconda-notes:

Cautionary Notes
================

While running the installer, you will be prompted with something like this:

``Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]``

If "yes", your ``.bashrc`` (or equivalent shell configuration file) will be
updated with something like this:

.. code-block:: bash

   # >>> conda initialize >>>
   # !! Contents within this block are managed by 'conda init’ !! .
   .
   .
   .
   .
   #unset __conda_setup
   # <<< conda initialize <<<

.. warning::

   By default, this will always initialize conda upon login, which clashes with
   other Python installations (e.g., if you use the other anaconda modules).

It is **MUCH SAFER** to say "no" and to just export the ``PATH`` manually to
avoid clashing:

.. tab-set::

   .. tab-item:: Bourne-like Shells

      .. code-block:: bash

         $ export PATH="/path/to/your/miniconda/bin:$PATH"

   .. tab-item:: Csh-like Shells

      .. code-block:: bash

         $ setenv PATH "/path/to/your/miniconda/bin:$PATH"

.. note::

   If your ``.bashrc`` already has a similar block of code, then it will **NOT**
   modify your ``.bashrc``

An additional recommendation is to set things to not activate your base
environment by default (to help with the potential clashing):

.. code-block:: bash

   # Only needs to be run once after exporting conda into your PATH
   conda config --set auto_activate_base false

As always, if you encounter issue, don't hesitate to contact :ref:`help
<getting_help>`.
