
***********************
Python on OLCF Systems
***********************

.. warning::
    Currently, Crusher and Frontier do **NOT** have Anaconda/Conda modules.
    To use conda, you will have to download and install Miniconda on your own
    (see our :doc:`Installing Miniconda Guide </software/python/miniconda>`).
    Alternatively, you can use Python's native virtual environments ``venv``
    feature with the ``cray-python`` module.  For more details on ``venv``,
    see `Python's Official Documentation <https://docs.python.org/3/tutorial/venv.html>`__.
    Contact help@olcf.ornl.gov if conda is required for your workflow, or if you
    have any issues.

Overview
========

In high-performance computing, `Python <https://www.python.org/>`__ is heavily
used to analyze scientific data on the system. Some users require specific
versions of Python or niche scientific packages to analyze their data, which
may further depend on numerous other Python packages. Because of all the
dependencies that some Python packages require, and all the types of data that
exist, it can be quite troublesome to get different Python installations to
"play nicely" with each-other, especially on an HPC system where the system
environment is complicated. "Virtual environments" help alleviate these issues
by isolating package installations into self-contained directory trees.

Although Python has a native virtual environment feature (``venv``), one
popular virtual environment manager is `Conda
<https://conda.io/projects/conda/en/latest/index.html>`__, a package and
virtual environment manager from the `Anaconda <https://www.anaconda.com/>`__
distribution. Conda allows users to easily install different versions of binary
software packages and any required libraries appropriate for their computing
platform.  The versatility of conda allows a user to essentially build their
own isolated Python environment, without having to worry about clashing
dependencies and other system installations of Python. Conda is available on
select OLCF systems (Summit and Andes), and loading the default Python module
on Summit and Andes loads an Anaconda Python distribution.  Loading this
distribution automatically puts you in a "base" conda environment, which
already includes packages that one can use for simulation, analysis, and
machine learning.

For users interested in using Python with Jupyter, see our `Jupyter at OLCF
<https://docs.olcf.ornl.gov/services_and_applications/jupyter/overview>`_ page instead.

For users interested in using the machine learning ``open-ce`` module (formerly
``ibm-wml-ce``) on Summit, see our `OpenCE
<https://docs.olcf.ornl.gov/software/analytics/ibm-wml-ce>`_ page.

.. warning::
    Currently, Crusher and Frontier do **NOT** have Anaconda/Conda modules
    (see warning at top of this page).
    If you decide to :doc:`install a personal Miniconda on Frontier </software/python/miniconda>`,
    the conda workflow described on this page (and others) still applies.
    Otherwise, you will have to use the ``venv`` workflow described below.

.. _python-guides:

OLCF Python Guides
==================

Below is a list of guides created for using Python on OLCF systems.

.. toctree::
   :maxdepth: 1
   :hidden:

   conda_basics
   parallel_h5py
   cupy
   miniconda

* :doc:`Conda Basics Guide </software/python/conda_basics>`: Goes over the basic workflow and commands of Conda **(Summit/Andes/Frontier)**
* :doc:`Installing mpi4py and h5py Guide </software/python/parallel_h5py>`: Teaches you how to install parallel-enabled h5py and mpi4py **(Summit/Andes/Frontier)**
* :doc:`Installing CuPy Guide </software/python/cupy>`: Teaches you how to install CuPy **(Summit/Frontier)**
* :doc:`Installing Miniconda Guide </software/python/miniconda>`: Teaches you how to install Miniconda **(Frontier only)**

.. note::
   For newer users to conda, it is highly recommended to view our :doc:`Conda
   Basics Guide </software/python/conda_basics>`, where a :ref:`conda-quick`
   list is provided.

.. note::
   The Frontier sections below assume you are not using a :doc:`personal Miniconda on Frontier </software/python/miniconda>`.

.. _python-mods:

Module Usage
============

To start using Python, all you need to do is load the module:

.. tab-set::

    .. tab-item:: Summit
        :sync: summit

        .. code-block:: bash

            $ module load python

    .. tab-item:: Andes
        :sync: andes

        .. code-block:: bash

            $ module load python

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            $ module load cray-python


Base Environment
----------------

Loading the Python module on all systems will put you in a "base"
pre-configured environment. This option is recommended for users who do not
need custom environments, and only require packages that are already installed
in the base environment. This option is also recommended for users that just
need a Python interpreter or standard packages like NumPy and Scipy.  Although
Frontier does not use conda environments in its Python module, the base set of
packages provided by the ``cray-python`` module can still be thought of as a
"base environment".

To see a full list of the packages installed in the base environment, use
``conda list`` on Summit and Andes or ``pip list`` on Frontier.
A small preview is provided below:

.. tab-set::

    .. tab-item:: Summit
        :sync: summit

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at /sw/summit/python/3.8/anaconda3/2020.07-rhel8:
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

    .. tab-item:: Andes
        :sync: andes

        .. code-block:: bash

            $ module load python
            $ conda list

            # packages in environment at /sw/andes/python/3.7/anaconda-base:
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

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            $ module load cray-python
            $ pip list

            Package            Version
            ------------------ ---------
            atomicwrites       1.4.0
            attrs              21.2.0
            Cython             0.29.24
            dask               2021.10.0
            fsspec             2022.3.0
            importlib-metadata 0.0.0
            iniconfig          1.1.1
            locket             0.2.1
            more-itertools     8.10.0
            mpi4py             3.1.3
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
environment to manage specialized packages. This is possible via ``conda``
commands on Summit and Andes, while Frontier uses Python's native ``venv``
feature instead.

.. note::
   A more complete list of ``conda`` commands is provided in the :ref:`conda-quick`
   section of the :doc:`Conda Basics Guide </software/python/conda_basics>`. More
   information on using the ``venv`` command can be found in
   `Python's Official Documentation <https://docs.python.org/3/tutorial/venv.html>`__.

To create and activate an environment:

.. tab-set::

    .. tab-item:: Summit
        :sync: summit

        .. code-block:: bash

            #1. Load the module
            $ module load python

            #2a. Create "my_env" with Python version X.Y at the desired path
            $ conda create -p /path/to/my_env python=X.Y

            #2b. Create "my_env" with Python version X.Y with a specific name (defaults to $HOME directory)
            $ conda create --name my_env python=X.Y

            #3. Activate "my_env"
            $ source activate /path/to/my_env

    .. tab-item:: Andes
        :sync: andes

        .. code-block:: bash

            #1. Load the module
            $ module load python

            #2a. Create "my_env" with Python version X.Y at the desired path
            $ conda create -p /path/to/my_env python=X.Y

            #2b. Create "my_env" with Python version X.Y with a specific name (defaults to $HOME directory)
            $ conda create --name my_env python=X.Y

            #3. Activate "my_env"
            $ source activate /path/to/my_env

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            #1. Load the module
            $ module load cray-python

            #2. Create "my_env" at the desired path (uses same Python version as module)
            $ python3 -m venv /path/to/my_env

            #3. Activate "my_env"
            $ source /path/to/my_env/bin/activate


.. note::
   It is highly recommended to create new environments in the "Project Home"
   directory (``/ccs/proj/<project_id>/<user_id>``). This space avoids purges,
   allows for potential collaboration within your project, and works better with
   the compute nodes. It is also recommended, for convenience, that you use
   environment names that indicate the hostname, as virtual environments created
   on one system will not necessarily work on others.

It is always recommended to deactivate an environment before activating a new one.
Deactivating an environment can be achieved through:

.. tab-set::

    .. tab-item:: Summit
        :sync: summit

        .. code-block:: bash

            # Deactivate the current environment
            $ source deactivate

    .. tab-item:: Andes
        :sync: andes

        .. code-block:: bash

            # Deactivate the current environment
            $ source deactivate

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            # Deactivate the current environment
            $ deactivate


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

Summit
------

Before jumping into batch scripts, remember to check out the :ref:`python-mods`
section first, which details the differences between Python modules and
environments on our different systems.

Batch Script - Summit
^^^^^^^^^^^^^^^^^^^^^

To use Python on a Summit compute node, you **must** use ``jsrun``, even if
running in serial.

Additionally, ``$PATH`` issues are known to occur after having loaded multiple
conda environments before submitting a batch script. Therefore, it is
recommended to use a fresh login shell before submission. The ``-L`` flag for
``bsub`` ensures that no previously set environment variables are passed into
the batch job.

.. code-block:: bash

   $ bsub -L $SHELL submit.lsf

This means you will have to load your modules and activate your environment
inside the batch script. An example batch script for Summit is provided below:

.. code-block:: bash

   #!/bin/bash
   #BSUB -P PROJECT_ID
   #BSUB -W 00:05
   #BSUB -nnodes 1
   #BSUB -J python
   #BSUB -o python.%J.out
   #BSUB -e python.%J.err

   cd $LSB_OUTDIR
   date

   module load python
   source activate my_env

   jsrun -n1 -r1 -a1 -c1 python3 script.py

Interactive Job - Summit
^^^^^^^^^^^^^^^^^^^^^^^^

To use Python in an interactive session on Summit:

.. code-block:: bash

   $ module load python
   $ bsub -W 0:05 -nnodes 1 -P <PROJECT_ID> -Is $SHELL
   $ source activate my_env
   $ jsrun -n1 -r1 -a1 -c1 python3 script.py

Frontier / Andes
----------------

Before jumping into batch scripts, remember to check out the :ref:`python-mods`
section first, which details the differences between Python modules and
environments on our different systems.

Batch Script - Frontier / Andes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Frontier and Andes, you are already on a compute node once you are in a
batch job.  Therefore, you only need to use ``srun`` if you plan to run
parallel-enabled Python, and you *do not* need to specify ``srun`` if you are
running a serial application.

Similar to Summit (see above), ``$PATH`` issues are known to occur if not
submitting from a fresh login shell, which can result in the wrong
environment being detected. To avoid this, you must use the ``--export=NONE``
flag, which ensures that no previously set environment variables are passed
into the batch job:

.. code-block:: bash

   $ sbatch --export=NONE submit.sl

This means you will have to load your modules and activate your environment
inside the batch script. An example batch script for is provided below:

.. tab-set::

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            #!/bin/bash
            #SBATCH -A <PROJECT_ID>
            #SBATCH -J python
            #SBATCH -N 1
            #SBATCH -p batch
            #SBATCH -t 0:05:00

            cd $SLURM_SUBMIT_DIR
            date

            module load cray-python
            source /path/to/my_env/bin/activate

            python3 script.py


    .. tab-item:: Andes
        :sync: andes

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
            source activate my_env

            python3 script.py


Interactive Job - Frontier / Andes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use Python in an interactive session on Frontier and Andes:

.. tab-set::

    .. tab-item:: Frontier
        :sync: frontier

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load cray-python
            $ source /path/to/my_env/bin/activate
            $ python3 script.py

    .. tab-item:: Andes
        :sync: andes

        .. code-block:: bash

            $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
            $ module load python
            $ source activate my_env
            $ python3 script.py


When in an interactive job, if you want to use an interactive Python prompt and
``srun`` at the same time, use the ``--pty`` flag (useful when running with multiple tasks):

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
    ``envs/summit/`` in your "Project Home" on Summit is provided below:

    .. code-block:: bash

       $ conda create -p /ccs/proj/<project_id>/<user_id>/envs/summit/baseclone-summit --clone base
       $ source activate /ccs/proj/<project_id>/<user_id>/envs/summit/baseclone-summit

* **Cloning the "base environment" using venv**:

    .. code-block:: bash

       $ python3 -m venv /path/to/new_env --system-site-packages

* **Environment locations (storage)**:

    It is highly recommended to create new environments in the "Project Home"
    directory (``/ccs/proj/<project_id>/<user_id>``). This space avoids purges,
    allows for potential collaboration within your project, and works better with
    the compute nodes. It is also recommended, for convenience, that you use
    environment names that indicate the hostname, as virtual environments created
    on one system will not necessarily work on others.

* **Adding known conda environment locations**:

    For a conda environment to be callable by a "name", it must be installed in
    one of the ``envs_dirs`` directories. The list of known directories can be seen
    by executing:

    .. code-block:: bash

       $ conda config --show envs_dirs

    On OLCF systems, the default location is your ``$HOME`` directory.  If you
    plan to frequently create environments in a different location other than the
    default (such as ``/ccs/proj/...``), then there is an option to add directories
    to the ``envs_dirs`` list.

    For example, to track conda environments in a subdirectory called ``summit``
    in Project Home you would execute:

    .. code-block:: bash

       $ conda config --append envs_dirs /ccs/proj/<project_id>/<user_id>/envs/summit

    This will create a ``.condarc`` file in your ``$HOME`` directory if you do not have
    one already, which will now contain this new envs_dirs location.  This will now
    enable you to use the ``--name env_name`` flag when using conda commands for
    environments stored in the ``summit`` directory, instead of having to use the
    ``-p /ccs/proj/<project_id>/<user_id>/envs/summit/env_name``
    flag and specifying the full path to the environment.  For example, you can do
    ``source activate my_env`` instead of ``source activate
    /ccs/proj/<project_id>/<user_id>/envs/summit/my_env``.

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