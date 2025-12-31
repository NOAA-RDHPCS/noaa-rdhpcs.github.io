.. _conda-basics:

************
Conda Basics
************

.. note::

   The guide is designed to be followed from start to finish, as certain steps
   must be completed in the correct order before some commands work properly.
   For those that just want a quick-reference list of common conda commands, see
   the :ref:`conda-quick` section.

Overview
========

This guide introduces a user to the basic workflow of using conda environments,
as well as providing an example of how to create a conda environment that uses
a different version of Python than the base environment. Although hera is being
used in this guide, all of the concepts still apply to other RDHPCS systems.

Inspecting and setting up an environment
========================================

First, load the python module and the gnu compiler, if available as most Python
packages assume use of GCC.

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ module use /usw/conda/modulefiles
            $ module load conda

        .. note::

            While the path to the Python module on Gaea is in a directory path
            with the name of ``conda``, the Python module will not initialize
            the Conda environment.  If you want to use Conda, you must load the
            ``miniforge`` instead (see :ref:`python-conda-modules`
            below).

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            $ module load conda

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            $ module load conda

    .. tab-item:: mercury
        :sync: mercury

        .. code-block:: bash

            $ module load conda

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            $ module load conda


This puts you in the "base" conda environment( and activates it), which is
the default Python environment after loading the module.  To see a list of
environments, use the command ``conda env list``:

.. code-block:: bash

   $ conda env list

   # conda environments:
   #
   base                  *  /contrib/miniconda3/4.12.0
   avid_verify              /contrib/miniconda3/4.12.0/envs/avid_verify
   pygraf                   /contrib/miniconda3/4.12.0/envs/pygraf
   regional_workflow        /contrib/miniconda3/4.12.0/envs/regional_workflow
   test_uwtools             /contrib/miniconda3/4.12.0/envs/test_uwtools

This also is a great way to keep track of the locations and names of all other
environments that have been created. The current environment is indicated by
``*``.

To see what packages are installed in the active environment, use ``conda
list``:

.. code-block:: bash

   $ conda list

   # packages in environment at /contrib/miniconda3/4.12.0:
   #
   # Name                    Version                   Build  Channel
   _libgcc_mutex             0.1                       main
   _openmp_mutex             4.5                       1_gnu
   brotlipy                  0.7.0         py39h27cfd23_1003
   bzip2                     1.0.8                h7f98852_4    conda-forge
   c-ares                    1.18.1               h7f98852_0    conda-forge
   ca-certificates           2022.5.18.1          ha878542_0    conda-forge
   certifi                   2022.5.18.1      py39hf3d152e_0    conda-forge
   cffi                      1.15.0           py39hd667e15_1
   charset-normalizer        2.0.4              pyhd3eb1b0_0
   .
   .
   .

You can find the version of Python that exists in this base environment by
executing:

.. code-block:: bash

   $ python --version

   Python 3.12.0

Creating a new environment
==========================

For this guide, you are going to install a different version of Python.

To do so, create a new environment using the ``conda create`` command:

.. code-block:: bash

   $ conda create -p /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/py31013 python=3.10.13

The ``-p`` flag specifies the desired path and name of your new virtual
environment. The directory structure is case sensitive, so be sure to insert
``<YOUR_PROJECT_ID>`` as lowercase. Directories will be created if they do not
exist already (provided you have write-access in that location). Instead, one
can solely use the ``--name <your_env_name>`` flag which will automatically use
your ``$HOME`` directory.

.. note::

   It is highly recommended to create new environments in the "Project Home"
   directory. This space avoids purges, allows for potential collaboration
   within your project, and works better with the compute nodes.


After executing the ``conda create`` command, you will be prompted to install
"the following NEW packages" -- type "y" then hit Enter/Return. Downloads of
the fresh packages will start and eventually you should see something similar
to:

.. code-block:: bash

   Preparing transaction: done
   Verifying transaction: done
   Executing transaction: done
   #
   # To activate this environment, use
   #
   #     $ conda activate /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/py31013
   #
   # To deactivate an active environment, use
   #
   #     $ conda deactivate

Let's activate the new environment:

.. code-block:: bash

   $ conda activate /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/py31013

The path to the environment should now be displayed in "( )" at the beginning
of your terminal lines, which indicate that you are currently using that
specific conda environment.  And if you check with ``conda env list`` again,
you should see that the ``*`` marker has moved to your newly activated
environment:

.. code-block:: bash

   $ conda env list

   # conda environments:
   #
   base                     /contrib/miniconda3/4.12.0
   avid_verify              /contrib/miniconda3/4.12.0/envs/avid_verify
   pygraf                   /contrib/miniconda3/4.12.0/envs/pygraf
   regional_workflow        /contrib/miniconda3/4.12.0/envs/regional_workflow
   test_uwtools             /contrib/miniconda3/4.12.0/envs/test_uwtools
                         *  /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/py31013

Installing packages
===================

Next, let's install a package (`NumPy <https://numpy.org/>`__).
There are a few different approaches.

Installing with pip
-------------------

One way to install packages into your conda environment is to build packages
from source using `pip <https://pip.pypa.io/en/stable/>`__. This approach is
useful if a specific package or package version is not available in the conda
repository, or if the pre-compiled binaries don't work on the HPC resources
(which is common). However, building from source means you need to take care of
some of the dependencies yourself, especially for optimization. Pip is
available to use after installing Python into your conda environment, which you
have already done.

.. warning::

   Because issues can arise when using conda and pip together (see link in
   :ref:`conda-refs`), it is recommended to do this only if absolutely
   necessary.

To build a package from source, use ``pip install --no-binary=<package_name>
<package_name>``:

.. code-block:: bash

   $ CC=gcc pip install --no-binary=numpy numpy

The ``CC=gcc`` flag will ensure that you are using the proper compiler and
wrapper. Building from source results in a longer installation time for
packages, so you may need to wait a few minutes for the install to finish.

You have successfully built NumPy from source in your conda environment;
however, you did not link in any additional linear algebra packages, so this
version of NumPy is not optimized. Let's install a more optimized version using
a different method instead, but first you must uninstall the pip-installed
NumPy:

.. code-block:: bash

   $ pip uninstall numpy

Installing with conda commands
------------------------------

The traditional, and more basic, approach to installing/uninstalling
packages into a conda environment is to use the commands ``conda
install`` and ``conda remove``. Installing packages with this method
checks the `Anaconda Distribution Repository
<https://www.anaconda.com/docs/main>`__
for pre-built binary packages to install. Let's do this to install
NumPy:

.. code-block:: bash

   $ conda install numpy

Because NumPy depends on other packages for optimization, this will also
install all of its dependencies. You have just installed an optimized version
of NumPy, now let's test it.

.. warning::

   It is possible you could fill your home disk quota as the default location
   for conda's cache directory.  See :ref:`managing_conda_cache` to change the
   cache location.

Testing your new environment
============================

Let's run a test to make sure everything installed properly. Since you are
running a small test, you can do this without having to run on a compute node.

.. warning::

   Remember, at larger scales both your performance and your fellow users'
   performance will suffer if you do not run on the compute nodes. It is always
   highly recommended to run on the compute nodes (through the use of a batch
   job or interactive batch job).

Make sure you're in a Python shell first, then print out the versions of Python
and NumPy:

.. code-block:: bash

   $ python3

.. code-block:: python

   >>> import platform
   >>> import numpy
   >>> py_vers = platform.python_version()
   >>> np_vers = numpy.__version__
   >>> print("Hello from Python", py_vers)
   Hello from Python 3.10.13
   >>> print("You are using NumPy", np_vers)
   You are using NumPy 1.26.3

Additional Tips
===============

Cloning the base environment
----------------------------

It is not recommended to try to install new packages into the base environment.
Instead, you can clone the base environment for yourself and install packages
into the clone. To clone an environment, you must use the ``--clone
<env_to_clone>`` flag when creating a new conda environment. An example for
cloning the base environment into your Project Home directory on Summit is
provided below:

.. code-block:: bash

   $ conda create -p /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/baseclone --clone base
   $ conda activate /scratch[34]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/baseclone

Adding known environment locations
----------------------------------

For a conda environment to be callable by a "name", it must be installed in one
of the ``envs_dirs`` directories. The list of known directories can be seen by
executing:

.. code-block:: bash

   $ conda config --show envs_dirs

On RDHPCS systems, the default location is your ``$HOME`` directory. If you
plan to frequently create environments in a different location other than the
default, then there is an option to add directories to the ``envs_dirs`` list.

For example, to track conda environments in a subdirectory called in
Project Home you would execute:

.. code-block:: bash

   $ conda config --append envs_dirs <project_home>/<PROJECT_ID>/<USER_ID>/envs/

This will create a ``.condarc`` file in your ``$HOME`` directory if you do not
have one already, which will now contain this new envs_dirs location. This will
now enable you to use the ``--name env_name`` flag when using conda commands,
instead of having to use the ``-p
<project_home>/<PROJECT_ID>/<USER_ID>/envs/summit/env_name`` flag and
specifying the full path to the environment. For example, you can do ``conda
activate py31013`` instead of ``conda activate
<project_home>/<PROJECT_ID>/<USER_ID>/envs/py31013``.

Exporting (sharing) an environment
----------------------------------

You may want to share your environment with someone else. One way to do this is
by creating your environment in a shared location where other users can access
it. A different way (the method described below) is to export a list of all the
packages and versions of your environment (an ``environment.yml`` file). If a
different user provides conda the list you made, conda will install all the
same package versions and recreate your environment for them -- essentially
"sharing" your environment. To export your environment list:

.. code-block:: bash

   $ conda activate my_env
   $ conda env export > environment.yml

You can then email or otherwise provide the ``environment.yml`` file to the
desired person. The person would then be able to create the environment like
so:

.. code-block:: bash

   $ conda env create -f environment.yml

.. _managing_conda_cache:

Managing Conda Cache
--------------------

The default location for Conda to cache files is the user's ``$HOME``
directory, which can rapidly fill and cause issues. This behavior can be
changed by setting the ``pkgs_dirs`` entry in the ``.condarc`` file or setting
the ``CONDA_PKGS_DIRS`` environment variable. First, to see the current cache
directory, issue:

.. code-block:: bash

   $ conda info

The package cache entry will display the current package cache directories. The
config file entry displays the location of the user ``.condarc`` file.
Editing/creating the ``pkgs_dirs`` entry in the ``.condarc`` file will change
the cache directory:

* Open the user ``.condarc`` file.  By default it is located at
  ``$HOME/.condarc`` and add the ``pkgs_dirs`` entry with desired cache
  directory:

  .. code-block:: bash

      pkgs_dirs:
         - /path/to/desired/cache/directory

* Use ``conda config`` to add ``pkgs_dirs`` entry:

  .. code-block:: bash

      $ conda config --add pkgs_dirs /path/to/desired/cache/directory

Use conda info to confirm change:

.. code-block:: bash

   $ conda info

Another method to adjust the cache directory is by setting the
``CONDA_PKGS_DIRS`` environment variable. To do this, issue:

.. tab-set::

   .. tab-item:: Bourne-like Shells

      .. code-block::

         $ export CONDA_PKGS_DIRS=/path/to/desired/cache/directory

   .. tab-item:: Csh-like Shells

      .. code-block::

         $ setenv CONDA_PKGS_DIRS /path/to/desired/cache/directory

.. _conda-quick:

Quick-Reference Commands
========================

* List environments:

    .. code-block:: bash

       $ conda env list

* List installed packages in current environment:

    .. code-block:: bash

       $ conda list

* Creating an environment with Python version X.Y:

    For a **specific path**:

    .. code-block:: bash

       $ conda create -p /path/to/your/my_env python=X.Y

    For a **specific name**:

    .. code-block:: bash

       $ conda create -n my_env python=X.Y

* Deleting an environment:

    For a **specific path**:

    .. code-block:: bash

       $ conda env remove -p /path/to/your/my_env

    For a **specific name**:

    .. code-block:: bash

       $ conda env remove -n my_env

* Copying an environment:

    For a **specific path**:

    .. code-block:: bash

       $ conda create -p /path/to/new_env --clone old_env

    For a **specific name**:

    .. code-block:: bash

       $ conda create -n new_env --clone old_env

* Activating/Deactivating an environment:

    .. code-block:: bash

       $ conda activate my_env
       $ conda deactivate # deactivates the current environment

* Installing/Uninstalling packages:

    Using **conda**:

    .. code-block:: bash

       $ conda install package_name
       $ conda remove package_name

    Using **pip**:

    .. code-block:: bash

       $ pip install package_name
       $ pip uninstall package_name
       $ pip install --no-binary=package_name package_name # builds from source

.. _conda-refs:

Additional Resources
====================

* `Conda User Guide <https://conda.io/projects/conda/en/latest/user-guide/index.html>`__
* `Pip User Guide <https://pip.pypa.io/en/stable/user_guide/>`__
* `Using Pip In A Conda Environment <https://www.anaconda.com/blog/using-pip-in-a-conda-environment>`__
