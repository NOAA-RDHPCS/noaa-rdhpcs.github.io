
########################
Python on RDHPCS Systems
########################

Overview
========

In high-performance computing, `Python <https://www.python.org/>`__ is heavily
used to analyze scientific data on the system. Some users require specific
versions of Python or niche scientific packages to analyze their data, which
may further depend on numerous other Python packages. Because of all the
dependencies that some Python packages require, and all the types of data that
exist, it can be quite troublesome to get different Python installations to
"play nicely" with each-other, especially on an HPC system where the system
environment is complicated. Virtual environments help alleviate these issues by
isolating package installations into self-contained directory trees.

Although Python has a native virtual environment feature (``venv``), one
popular virtual environment manager is `Conda
<https://conda.io/projects/conda/en/latest/index.html>`__, a package and
virtual environment manager from the `Anaconda <https://www.anaconda.com/>`__
distribution. Conda allows users to easily install different versions of binary
software packages and any required libraries appropriate for their computing
platform.  The versatility of conda allows a user to essentially build their
own isolated Python environment, without having to worry about clashing
dependencies and other system installations of Python. Conda is available on
all RDHPCS systems, and loading the default Python module loads an Anaconda
Python distribution.  Loading this distribution automatically puts you in a
"base" conda environment, which already includes packages that one can use for
simulation, analysis, and machine learning.

For users interested in using Python with Jupyter, see our
:ref:`jupyter_on_rdhpcs_systems` page instead.

.. note::

    The RDHPCS is working on a unified Python/Conda configuration and policies
    across all NOAA-managed RDHPCS systems (hera, jet, niagara, ppan).  This
    documentation will be updated as the the configuration and policies are
    established.

.. _python-guides:

Python Guides
=============

Below is a list of guides created for using Python on RDHPCS systems.

.. toctree::
   :maxdepth: 1
   :hidden:

   conda_basics
   miniconda
   jupyter

* :doc:`Conda Basics Guide </software/python/conda_basics>`: Goes over the
  basic workflow and commands of Conda
* :doc:`Installing Miniconda Guide </software/python/miniconda>`: Teaches you
  how to install Miniconda
* :ref:`jupyter_on_rdhpcs_systems`: Instructions to install and access
  JupyterLab on the RDHPCS systems

.. note::

   For newer users to conda, it is highly recommended to view our :doc:`Conda
   Basics Guide </software/python/conda_basics>`, where a :ref:`conda-quick`
   list is provided.

.. _python-mods:

Module Usage
============

To start using Python, all you need to do is load the module:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ module load python

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            $ module load python

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            $ module load python

    .. tab-item:: niagara
        :sync: niagara

        .. code-block:: bash

            $ module load python

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            $ module load python


Base Environment
----------------

Loading the Python module on all systems will put you in a "base"
pre-configured environment. This option is recommended for users who do not
need custom environments, and only require packages that are already installed
in the base environment. This option is also recommended for users that just
need a Python interpreter or standard packages like NumPy and Scipy.

To see a full list of the packages installed in the base environment, use
``conda list``.
A small preview is provided below:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at ...:
            #
            # Name                    Version                   Build  Channel
            _ipyw_jlab_nb_ext_conf    0.1.0                    py38_0
            _libgcc_mutex             0.1                        main
            alabaster                 0.7.12                     py_0
            anaconda                  2020.07                  py38_0
            anaconda-client           1.7.2                    py38_0
            anaconda-project          0.8.4                      py_0
            asn1crypto                1.3.0                    py38_0
            astroid                   2.4.2                    py38_0
            astropy                   4.0.1.post1      py38h7b6447c_1
            .
            .
            .

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at ...:
            #
            # Name                    Version                   Build  Channel
            _ipyw_jlab_nb_ext_conf    0.1.0                    py37_0
            _libgcc_mutex             0.1                        main
            absl-py                   0.11.0                   pypi_0    pypi
            alabaster                 0.7.12                   py37_0
            anaconda                  2020.02                  py37_0
            anaconda-client           1.7.2                    py37_0
            anaconda-navigator        1.9.12                   py37_0
            anaconda-project          0.8.4                      py_0
            argh                      0.26.2                   py37_0
            .
            .
            .

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at ...:
            #
            # Name                    Version                   Build  Channel
            _ipyw_jlab_nb_ext_conf    0.1.0                    py37_0
            _libgcc_mutex             0.1                        main
            absl-py                   0.11.0                   pypi_0    pypi
            alabaster                 0.7.12                   py37_0
            anaconda                  2020.02                  py37_0
            anaconda-client           1.7.2                    py37_0
            anaconda-navigator        1.9.12                   py37_0
            anaconda-project          0.8.4                      py_0
            argh                      0.26.2                   py37_0
            .
            .
            .

    .. tab-item:: niagara
        :sync: niagara

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at ...:
            #
            # Name                    Version                   Build  Channel
            _ipyw_jlab_nb_ext_conf    0.1.0                    py37_0
            _libgcc_mutex             0.1                        main
            absl-py                   0.11.0                   pypi_0    pypi
            alabaster                 0.7.12                   py37_0
            anaconda                  2020.02                  py37_0
            anaconda-client           1.7.2                    py37_0
            anaconda-navigator        1.9.12                   py37_0
            anaconda-project          0.8.4                      py_0
            argh                      0.26.2                   py37_0
            .
            .
            .

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at ...:
            #
            # Name                    Version                   Build  Channel
            _ipyw_jlab_nb_ext_conf    0.1.0                    py37_0
            _libgcc_mutex             0.1                        main
            absl-py                   0.11.0                   pypi_0    pypi
            alabaster                 0.7.12                   py37_0
            anaconda                  2020.02                  py37_0
            anaconda-client           1.7.2                    py37_0
            anaconda-navigator        1.9.12                   py37_0
            anaconda-project          0.8.4                      py_0
            argh                      0.26.2                   py37_0
            .
            .
            .


.. warning::
   It is not recommended to try to install new packages into the base
   environment.  Instead, you can either clone the base environment for yourself
   and install packages into the clone, or create a brand new (empty) environment
   and install packages into it.  An example for cloning the base environment is
   provided in :ref:`python-best-pract` below, while creating new environments
   is covered directly below in :ref:`python-custom-envs`.

.. _python-custom-envs:

Custom Environments
-------------------

You can also create your own custom environments after loading the Python
module. This option is recommended for users that require a different version
of Python than the default version available, or for users that want a personal
environment to manage specialized packages. This is possible via ``conda`` or
using Python's native ``venv`` feature instead.

.. note::

   A more complete list of ``conda`` commands is provided in the :ref:`conda-quick`
   section of the :doc:`Conda Basics Guide </software/python/conda_basics>`. More
   information on using the ``venv`` command can be found in
   `Python's Official Documentation <https://docs.python.org/3/tutorial/venv.html>`__.

To create and activate an environment:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            #1. Load the module
            $ module load python

            #2a. Create "my_env" with Python version X.Y at the desired path
            $ conda create -p /path/to/my_env python=X.Y

            #2b. Create "my_env" with Python version X.Y with a specific name (defaults to $HOME directory)
            $ conda create --name my_env python=X.Y

            #3. Activate "my_env"
            $ conda activate /path/to/my_env

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            #1. Load the module
            $ module load python

            #2a. Create "my_env" with Python version X.Y at the desired path
            $ conda create -p /path/to/my_env python=X.Y

            #2b. Create "my_env" with Python version X.Y with a specific name (defaults to $HOME directory)
            $ conda create --name my_env python=X.Y

            #3. Activate "my_env"
            $ conda activate /path/to/my_env

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            #1. Load the module
            $ module load cray-python

            #2. Create "my_env" at the desired path (uses same Python version as module)
            $ python3 -m venv /path/to/my_env

            #3. Activate "my_env"
            $ conda /path/to/my_env/bin/activate

    .. tab-item:: Niagara
        :sync: niagara

        .. code-block:: bash

            #1. Load the module
            $ module load cray-python

            #2. Create "my_env" at the desired path (uses same Python version as module)
            $ python3 -m venv /path/to/my_env

            #3. Activate "my_env"
            $ conda /path/to/my_env/bin/activate

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            #1. Load the module
            $ module load cray-python

            #2. Create "my_env" at the desired path (uses same Python version as module)
            $ python3 -m venv /path/to/my_env

            #3. Activate "my_env"
            $ conda /path/to/my_env/bin/activate

.. note::

   It is highly recommended to create new environments in the "Project Home"
   directory (see :ref:`file system summary <data-filesystem-summary>`). This
   space avoids purges, allows for potential collaboration within your project,
   and works better with the compute nodes. It is also recommended, for
   convenience, that you use environment names that indicate the hostname, as
   virtual environments created on one system will not necessarily work on
   others.

It is always recommended to deactivate an environment before activating a new
one. Deactivating an environment can be achieved through:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            # Deactivate the current environment
            $ conda deactivate

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            # Deactivate the current environment
            $ conda deactivate

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            # Deactivate the current environment
            $ conda deactivate

    .. tab-item:: Niagara
        :sync: niagara

        .. code-block:: bash

            # Deactivate the current environment
            $ conda deactivate

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            # Deactivate the current environment
            $ conda deactivate

How to Run
==========

.. warning::
   Remember, at larger scales both your performance and your fellow users'
   performance will suffer if you do not run on the compute nodes. It is always
   highly recommended to run on the compute nodes (through the use of a batch job
   or interactive batch job).

The OS-provided Python is no longer accessible as ``python`` (including
variations like ``/usr/bin/python`` or ``/usr/bin/env python``); rather, you
must specify it as ``python2`` or ``python3``. If you are using python from one
of the module files rather than the version in ``/usr/bin``, this change should
not affect how you invoke python in your scripts, although we encourage
specifying ``python2`` or ``python3`` as a best practice.

RDHPCS Compute Nodes
--------------------

Before jumping into batch scripts, remember to check out the :ref:`python-mods`
section first, which details the differences between Python modules and
environments on our different systems.

Batch Script
^^^^^^^^^^^^

On most RDHPCS systems, you are already on a compute node once you are in a
batch job.  Therefore, you only need to use ``srun`` if you plan to run
parallel-enabled Python, and you *do not* need to specify ``srun`` if you are
running a serial application.

Additionally, ``$PATH`` issues are known to occur if not submitting from a
fresh login shell, which can result in the wrong environment being detected. To
avoid this, you must use the ``--export=NONE`` flag, which ensures that no
previously set environment variables are passed into the batch job:

.. code-block:: bash

   $ sbatch --export=NONE submit.sl

This means you will have to load your modules and activate your environment
inside the batch script. An example batch script for is provided below:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load python
            conda activate my_env

            python3 script.py


    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load python
            conda activate my_env

            python3 script.py

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load python
            conda activate my_env

            python3 script.py

    .. tab-item:: Niagara
        :sync: niagara

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load python
            conda activate my_env

            python3 script.py

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load python
            conda activate my_env

            python3 script.py

Interactive Job
^^^^^^^^^^^^^^^

To use Python in an interactive session on RDHPCS systems:

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ conda activate my_env
            $ python3 script.py

    .. tab-item:: Hera
        :sync: hera

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ conda activate my_env
            $ python3 script.py

    .. tab-item:: Jet
        :sync: jet

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ conda activate my_env
            $ python3 script.py

    .. tab-item:: Niagara
        :sync: niagara

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ conda activate my_env
            $ python3 script.py

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ conda activate my_env
            $ python3 script.py

When in an interactive job, if you want to use an interactive Python prompt and
``srun`` at the same time, use the ``--pty`` flag (useful when running with
multiple tasks):

.. code-block:: bash

   $ srun --pty python3


.. _python-best-pract:

Best Practices
==============

* **Cloning the base environment using conda**:

    It is not recommended to try to install new packages into the base
    environment. Instead, you can clone the base environment for yourself and
    install packages into the clone. To clone an environment, you must use the
    ``--clone <env_to_clone>`` flag when creating a new conda environment. An
    example for cloning the base environment into a specific directory called
    ``envs/`` in your "Project Home" is provided below:

    .. code-block:: bash

       $ conda create -p <project_home>/<project_id>/<user_id>/envs/baseclone --clone base
       $ conda activate <project_home>/<project_id>/<user_id>/envs/baseclone

* **Cloning the "base environment" using venv**:

    .. code-block:: bash

       $ python3 -m venv /path/to/new_env --system-site-packages

* **Environment locations (storage)**:

    It is highly recommended to create new environments in the "Project Home"
    directory (see :ref:`file system summary <data-filesystem-summary>`). This
    space avoids purges, allows for potential collaboration within your
    project, and works better with the compute nodes.

* **Adding known conda environment locations**:

    For a conda environment to be callable by a "name", it must be installed in
    one of the ``envs_dirs`` directories. The list of known directories can be
    seen by executing:

    .. code-block:: bash

       $ conda config --show envs_dirs

    On RDHPCS systems, the default location is your ``$HOME`` directory.  If you
    plan to frequently create environments in a different location other than
    the default, then there is an option to add directories to the ``envs_dirs``
    list.

    For example, to track conda environments in a subdirectory in the Project Home
    you would execute:

    .. code-block:: bash

       $ conda config --append envs_dirs <project_home>/<project_id>/<user_id>/envs

    This will create a ``.condarc`` file in your ``$HOME`` directory if you do
    not have one already, which will now contain this new envs_dirs location.
    This will now enable you to use the ``--name env_name`` flag when using
    conda commands for environments stored in the personal environments
    directory, instead of having to use the ``-p
    <project_home>/<project_id>/<user_id>/envs/env_name`` flag and specifying
    the full path to the environment.  For example, you can do ``conda activate
    my_env`` instead of ``conda activate
    <project_home>/<project_id>/<user_id>/envs/my_env``.

* **Make note of and clean your pip cache location**:

    To avoid quota issues, it is highly recommended to occasionally clean your
    ``pip`` cache location.

    * To find where your cache location is, use:

        .. code-block:: bash

           $ pip cache info

    * To clean your cache, use:

        .. code-block:: bash

           $ pip cache purge

* **Clean your conda cache**:

    To avoid quota issues, it is highly recommended to occasionally clean your
    ``conda`` cache location (in your ``.conda`` directory). To do so, run:

    .. code-block:: bash

       $ conda clean -a

* **Deactivate your environments before running batch jobs**:

    To avoid ``$PATH`` issues, it is highly recommended to submit batch jobs or
    enter interactive jobs without an already activated environment -- so,
    deactivating your environment is recommended. Alternatively, you can submit
    your jobs from a fresh login shell.

* **Unbuffered input**:

    To enable unbuffered input when running Python jobs or scripts on our
    systems, it is recommended to use the ``-u`` flag. For example:

    .. code-block:: bash

       $ python3 -u script.py


Additional Resources
====================

* `pip User Guide <https://pip.pypa.io/en/stable/user_guide/>`__
* `venv Documentation <https://docs.python.org/3/tutorial/venv.html>`__
* `Conda User Guide <https://conda.io/projects/conda/en/latest/user-guide/index.html>`__
* `Anaconda Package List <https://docs.anaconda.com/anaconda/packages/pkg-docs/>`__
* `Using Pip In A Conda Environment <https://www.anaconda.com/blog/using-pip-in-a-conda-environment>`__
