
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


.. _python-python-and-conda-environments:

Python and Conda Environments
=============================

The Python ecosystem is vast, with a multitude of packages and dependencies.
The environments the system admins have made available have only a few standard
packages available (e.g., `matplotlib <https://matplotlib.org/>_`, `netcdf4
<https://unidata.github.io/netcdf4-python/>`_, `numpy <https://numpy.org/>`_,
`scipy <https://scipy.org/>`_, and `xarray
<https://docs.xarray.dev/en/stable/>`_.)  If the packages you need are not in the
available environments, you can create your own custom environment.

.. hint::

    Only install the minimum number of packages you need in your environment.
    The best practice is to have multiple, purposely created environments than
    one large environment with many packages.

.. _python-conda-environments:

Conda Environments
------------------

Some RDHPCS systems offer Conda for all users. The maintainers have created
several environments besides the `base` one. If those don't work for you,
create your own :ref:`custom environment <python-custom-environments>`.

Base Environment
^^^^^^^^^^^^^^^^

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

   It is not recommended to install new packages into the base environment.
   Instead, you should clone the base environment for yourself and install
   packages into the clone, or create a new environment and install the
   required packages into it.  An example for cloning the base environment is
   provided in :ref:`python-python-best-practices` below, while creating new
   environments is covered directly below in :ref:`python-custom-environments`.

.. _python-custom-environments:

Custom environments
^^^^^^^^^^^^^^^^^^^

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

.. _python-running-python:

Running Python
==============

While the running Python scripts on RDHPCS systems, you must consider the node
type you are using, and if you are in an interactive shell or in a batch job.
The following sections provide guidance on running Python scripts in these
scenarios.

.. caution::

    Running large-scale Python scripts on head nodes (i.e., login nodes)
    negatively impacts performance for all users. Therefore, we recommend
    utilizing the compute nodes.

.. important::

    The OS-provided Python is no longer accessible as ``python`` (including
    variations like ``/usr/bin/python`` or ``/usr/bin/env python``); rather, you
    must specify it as ``python2`` or ``python3``. If you are using python from one
    of the module files rather than the OS-provided version, this change should
    not affect how you invoke Python in your scripts, although we encourage
    specifying ``python2`` or ``python3`` as a best practice.


RDHPCS compute nodes
--------------------

Running Python on RDHPCS compute nodes requires understanding the environment
and the job scheduling system. Compute nodes are designed for executing
large-scale computations and should be used instead of head nodes to avoid
performance issues. Users can run Python scripts on compute nodes either
through batch scripts or interactive jobs. Below, we provide detailed
instructions and best practices for both methods to ensure efficient and
effective use of Python on RDHPCS systems.

.. hint::

    Before diving into batch scripts, make sure to review the
    :ref:`python-mods` section, which explains the distinctions between Python
    modules and the available Python environments on RDHPCS systems.

Batch script
^^^^^^^^^^^^

On most RDHPCS systems, you automatically find yourself on a compute node once
you enter a batch job. This means that using ``srun`` is necessary only if
you're executing a parallel-enabled Python application; for serial
applications, there's no need to specify it at all.

To ensure a smooth experience, be aware that ``$PATH`` issues often occur if
you don't submit your job from a fresh login shell, leading to incorrect
environment detection. To prevent this, utilize the ``--export=NONE``
``sbatch`` flag. This guarantees that no previously set environment variables
carry over into your batch job, resulting in a cleaner setup. The command to
submit your job will appear as follows:

.. code-block:: bash

   $ sbatch --export=NONE submit.sl

By following this approach, you'll need to load your modules and activate your
environment directly within the batch script, ensuring everything runs
seamlessly. Below is an example of an effective batch script:

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

    srun -n 5 python3 script.py

Interactive job
^^^^^^^^^^^^^^^

Running Python in an interactive batch session is similar to using python in an
interactive shell.  However, when on a compute node you can use the ``srun``
command to launch a parallel python job.

.. code-block:: bash

    $ salloc -A <PROJECT_ID> -N 1 -t 0:05:00
    $ module load miniforge
    $ conda activate my_env
    $ srun -n 20 python3 script.py

When in an interactive job, if you want to use an interactive Python prompt and
``srun`` at the same time, use the ``--pty`` flag (useful when running with
multiple tasks):

.. code-block:: bash

    $ srun --pty python3
    >>>>

.. _python-python-best-practices:

Python best practices
=====================

To ensure a smooth Python experience on RDHPCS systems, we've compiled a list
of best practices to help you navigate the Python ecosystem with ease.

Cloning the base environment using conda
----------------------------------------

It is not recommended to install new packages into the base environment.
Instead, you should clone the base environment and install packages into the
clone. To clone an environment, use the ``--clone <env_to_clone>`` flag when
creating a new conda environment. Below is an example of cloning the base
environment into a specific directory called ``envs/`` in your "Project Home":

.. tab-set::

    .. tab-item:: Conda
        :sync: conda

        .. code-block:: bash

            $ conda create -p <project_home>/<project_id>/<user_id>/envs/baseClone --clone base
            $ conda activate <project_home>/<project_id>/<user_id>/envs/baseClone

    .. tab-item:: Python Venv
        :sync: venv

        .. code-block:: bash

            $ python3 -m venv /path/to/new_env --system-site-packages
            $ source /path/to/new_env/bin/activate

Environment locations (storage)
-------------------------------

It is highly recommended to create new environments in the :ref:`Project Home
<data-filesystem-summary>`. This space avoids purges, facilitates collaboration
within your project, and ensures better compatibility with the compute nodes.

Adding known conda environment locations
----------------------------------------

Adding known conda environment locations
----------------------------------------

For a conda environment to be callable by a `name`, it must be installed in one
of the ``envs_dirs`` directories. You can view the list of known directories by
executing:

.. code-block:: bash

    $ conda config --show envs_dirs

On RDHPCS systems, the default location is your ``$HOME`` directory. If you
frequently create environments in a different location, you can add directories
to the ``envs_dirs`` list.

For example, to track conda environments in a subdirectory in the Project Home,
execute:

.. code-block:: bash

    $ conda config --append envs_dirs <project_home>/<project_id>/<user_id>/envs

This command creates a ``.condarc`` file in your ``$HOME`` directory (if it
doesn't already exist) and adds the new ``envs_dirs`` location. This allows you
to use the ``--name env_name`` flag for environments stored in the specified
directory, instead of specifying the full path with the ``-p
<project_home>/<project_id>/<user_id>/envs/env_name`` flag. For example, you
can use ``conda activate my_env`` instead of ``conda activate
<project_home>/<project_id>/<user_id>/envs/my_env``.

Keep you Python and Conda caches trimmed
----------------------------------------

To avoid quota issues, it is highly recommended to occasionally clean your
Python and Conda caches.

.. tab-set::

    .. tab-item:: Conda
        :sync: conda

        The Conda cache is typically found in the ``$HOME/.conda`` directory.
        To clean your Conda cache, use:

        .. code-block:: bash

            $ conda clean -a

    .. tab-item:: Python Venv
        :sync: venv

        * To find where your cache location is, use:

            .. code-block:: bash

                $ pip cache info

        * To clean your cache, use:

            .. code-block:: bash

                $ pip cache purge

Deactivate your environments before running batch jobs
------------------------------------------------------

To avoid ``$PATH`` issues, it is highly recommended to submit batch jobs or
enter interactive jobs without an already activated environment. Therefore,
deactivating your environment before submitting jobs is recommended. Alternatively,
you can submit your jobs from a fresh login shell.

Unbuffered input
----------------

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
