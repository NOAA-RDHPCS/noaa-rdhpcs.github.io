
########################
Python on RDHPCS Systems
########################

Overview
========

In high-performance computing (HPC), `Python <https://www.python.org/>`_ is an
essential tool for analyzing scientific data. Many users need specific versions
of Python or specialized scientific packages for their analyses, and these
often come with a range of dependencies. Managing different Python
installations can be problematic, particularly in the complex environment of
HPC systems. Virtual environments are a crucial solution, effectively isolating
package installations into distinct directories.

While Python includes a native virtual environment feature called `venv
<https://docs.python.org/3/library/venv.html>`_, `Conda
<https://docs.conda.io/projects/conda/en/latest/index.html>`_ stands out as a
powerful package and environment manager. Conda empowers users to effortlessly
install various binary software packages and the necessary libraries, enabling
the creation of isolated Python environments without the hassle of conflicting
dependencies or complications from other Python installations.  Conda is fully
supported on all RDHPCS systems.

.. caution::

    The RDHPCS does not have a license with the `Anaconda Python
    <https://www.anaconda.com/>`_ distribution. As the NOAA RDHPCS systems do
    not fit within the 200-employee limit as defined in `Anaconda Terms of
    Service <https://legal.anaconda.com/policies>`_, use of the Anaconda, which
    includes `Miniconda <https://docs.anaconda.com/miniconda/>`_, on RDHPCS
    systems is prohibited.

    For more information, please refer to the `Anaconda Terms of Service`_
    and Anaconda's blog posting `Update on Anaconda's Terms of Service for
    Academia and Research
    <https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research>`_.

.. note::

    The only conda channel approved for use on the NOAA RDHPCS systems is
    `conda-forge <https://conda-forge.org>`_.  The conda-forge installer,
    `Miniforge <https://conda-forge.org/download/>`_, includes the `conda`_
    package manager and will use the `conda-forge`_ channel.

If you want to leverage Python with Jupyter, we direct you to our
:ref:`jupyter_on_rdhpcs_systems` page for comprehensive guidance.

.. note::

    The RDHPCS is diligently working to implement a unified Python/Conda
    configuration and policies across all NOAA-managed RDHPCS systems (Hera,
    Jet, Niagara, Pan). Rest assured, this documentation will be updated as
    these configurations and policies are implemented.

.. _python-guides:

Python Guides
=============

Explore our guides designed to empower you in using Python and Conda on RDHPCS
systems:

.. toctree::
   :maxdepth: 1
   :hidden:

   conda_basics
   miniforge
   jupyter

* :doc:`Conda Basics Guide </software/python/conda_basics>`:
    Master the essential workflow and commands of Conda to enhance your
    productivity.
* :doc:`Installing Miniforge Guide </software/python/miniforge>`:
    Get step-by-step instructions for installing Miniconda on RDHPCS systems.
* :ref:`jupyter_on_rdhpcs_systems`:
    Access detailed directions for installing and utilizing JupyterLab on
    RDHPCS systems.

.. note::

   If you're new to Conda, don't miss our :doc:`Conda Basics Guide
   </software/python/conda_basics>`. It's the perfect starting point, providing
   you with a handy :ref:`quick-reference <conda-quick>` list of commands to
   accelerate your learning.

.. _python-mods:

Module Usage
============

.. _python-python-modules:

Python
------

To start using Python, load the ``python`` module.

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ module use /usw/conda/modulefiles
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

Run the ``module avail python`` command to see the available versions of
Python.

.. _python-conda-modules:

Conda
-----

Some RDHPCS systems have Conda installed for all users.  To start using Conda
on these systems, add the module file path to modules, and load the module.

.. tab-set::

    .. tab-item:: Gaea
        :sync: gaea

        .. code-block:: bash

            $ module use /usw/conda/modulefiles
            $ module load miniforge

    .. tab-item:: PPAN
        :sync: ppan

        .. code-block:: bash

            $ module load miniforge



Conda Environments
==================

Some RDHPCS systems offer Conda for all users. The maintainers have created
several environments besides the `base` one. If those don't work for you,
create your own :ref:`custom environment <python-custom-envs>`.

Base Environment
----------------

At the heart of every Conda installation is the `base` environment, which comes
equipped with the Conda package manager and a selection of additional packages.

Loading the :ref:`conda module <python-conda-modules>` will activate the `base`
environment. This option is ideal for users who don't require custom
environments or who simply need a Python interpreter.

To explore the full range of packages included in the base environment, just
use the command ``conda list``.

.. cSpell:disable

.. code-block:: bash

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

.. cSpell: enable

.. warning::

   It is not recommended to try to install new packages into the base
   environment.  Instead, you can either clone the base environment for
   yourself and install packages into the clone, or create a brand new (empty)
   environment and install packages into it.  An example for cloning the base
   environment is provided in :ref:`python-best-practices` below, while
   creating new environments is covered directly below in
   :ref:`python-custom-envs`.

.. _python-custom-envs:

Custom Environments
-------------------

After loading the :ref:`Python <python-python-modules>` or :ref:`Conda
<python-conda-modules>` module, you can create custom environments tailored to
your specific requirements. This is particularly beneficial if you need a
specific version of Python or packages. This can be accomplished using either
``conda`` or Python's built-in `venv`_ functionality.

.. note::

    The :doc:`Conda Basics Guide </software/python/conda_basics>` provides a
    list of `conda` commands. `Python's Official Documentation
    <https://docs.python.org/3/>`_ provides detailed instructions on using
    `venv`_.

To create and activate an environment:

.. tab-set::

    .. tab-item:: Conda
        :sync: conda

        .. code-block:: bash

            #1. Create the "my_env" environment with Python version X.Y
            $ conda create --name my_env python=X.Y

            #2. Activate "my_env"
            $ conda activate /path/to/my_env

            #3. Install additional packages in the "my_env" environment
            $ conda install <package_name> [<package_name> ...]

    .. tab-item:: Python Venv
        :sync: venv

        .. code-block:: bash

            #1. Create the virtual environment in the desired path
            $ python -m venv /path/to/my_env

            #2. Activate the virtual environment
            $ source /path/to/my_env/bin/activate

            #3. Install additional packages
            $ pip install <package_name> [<package_name> ...]

Following these procedures enables efficient management of package dependencies
and Python versions tailored to project needs.

To ensure optimal performance and collaboration on your project, we highly
recommend creating new environments in the "Project Home" directory (refer to
the :ref:`file system summary <data-filesystem-summary>`). This approach not
only prevents potential purges but also enhances teamwork within your project
and interacts seamlessly with the compute nodes. For added convenience, please
use environment names that reflect the hostname; this practice is crucial, as
virtual environments designed on one system may not operate correctly on
others.

Moreover, always remember to deactivate your current environment before
switching to a new one. You can easily deactivate an environment by using the
following command:

.. tab-set::

    .. tab-item:: Conda
        :sync: conda

        .. code-block:: bash

            $ conda deactivate

    .. tab-item:: Python Venv
        :sync: venv

        .. code-block:: bash

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


.. _python-best-practices:

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

       $ conda create -p <project_home>/<project_id>/<user_id>/envs/baseClone --clone base
       $ conda activate <project_home>/<project_id>/<user_id>/envs/baseClone

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
* `Anaconda Package List <https://docs.anaconda.com/anaconda/pkg-docs/>`__
* `Using Pip In A Conda Environment <https://www.anaconda.com/blog/using-pip-in-a-conda-environment>`__
