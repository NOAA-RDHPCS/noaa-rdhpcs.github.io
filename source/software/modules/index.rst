.. meta::
   :description: How to use Lmod environment modules on RDHPCS systems
    to manage software environments, load compilers and libraries, and
    use modules correctly in batch job scripts.
   :keywords: modules, Lmod, module load, module avail, module spider,
    batch jobs, software environment, Gaea, Hera, Ursa, Jet, Orion,
    Hercules

.. _modules:

#######
Modules
#######

`Lmod <https://lmod.readthedocs.io/en/latest/>`__ is a Lua-based module
system used to manage software environments on the RDHPCS systems
Gaea, Ursa, Hera, Jet, and the MSU systems Hercules and Orion. Rather
than manually setting environment variables like ``PATH`` and
``LD_LIBRARY_PATH``, the module system handles these changes for you
when you load or unload a module.

Because many software packages depend on a specific compiler or MPI
library, Lmod uses a *hierarchical* layout: loading a compiler makes
compiler-dependent packages (MPI stacks, libraries) visible, and
loading an MPI stack makes MPI-dependent packages visible in turn.
This means ``module avail`` only shows what is compatible with your
current environment — which is intentional.

.. note::

   On Gaea (an HPE/Cray system), the recommended way to set up a
   compiler toolchain is through the Cray **Programming Environment**
   modules (``PrgEnv-cray``, ``PrgEnv-intel``, ``PrgEnv-gnu``,
   ``PrgEnv-amd``, ``PrgEnv-nvidia``). Loading a ``PrgEnv-*`` module
   selects the compiler, configures the Cray compiler wrappers (``cc``,
   ``ftn``, ``CC``), and sets up MPI and libraries automatically. See
   the :ref:`Gaea User Guide <gaea-environment-modules>` for details.


View Active Modules
===================

Use ``module list`` to see what modules are currently loaded in your
environment:

.. code-block:: shell

   $ module list

For a compact list:

.. code-block:: shell

   $ module -t list


Finding Modules
===============

Lmod provides several commands to search for available modules.

.. rubric:: module avail

``module avail`` lists modules that are compatible with your *current*
environment (i.e., given the compilers and MPI stacks already loaded):

.. code-block:: shell

   $ module avail

.. rubric:: module spider

``module spider`` searches the *entire* module hierarchy, including
modules that are not yet available because their dependencies have not
been loaded. Use this when ``module avail`` does not show a module you
expect to find:

.. code-block:: shell

   $ module spider netcdf

To find out what must be loaded first to make a specific module
available:

.. code-block:: shell

   $ module spider cray-netcdf/4.9.0.1
   ----------------------------------
   cray-netcdf: cray-netcdf/4.9.0.1
   ----------------------------------

   You will need to load all module(s) on any one of the lines below
   before the "cray-netcdf/4.9.0.1" module is available to load.

   aocc/3.2.0  cray-hdf5/1.12.2.1
   aocc/3.2.0  cray-hdf5/1.12.2.3
   gcc/10.3.0  cray-hdf5/1.12.2.1
   gcc/10.3.0  cray-hdf5/1.12.2.3

.. note::

   ``module spider`` reports all modules across the full module
   hierarchy. ``module avail`` only shows modules compatible with the
   current environment. Always use ``module spider`` when you cannot
   find a module with ``module avail``.

.. rubric:: module keyword

Search for modules using a keyword:

.. code-block:: shell

   $ module keyword netcdf

.. rubric:: module show

Before loading a module, use ``module show`` to see exactly what
environment changes it will make (paths set, variables defined,
dependencies loaded) without actually loading it:

.. code-block:: shell

   $ module show cray-netcdf/4.9.0.1


Load Modules
============

Use ``module load`` to load a module into your current environment:

.. code-block:: shell

   $ module load <module>

Use ``module unload`` to remove a loaded module:

.. code-block:: shell

   $ module unload <module>

.. important::

   **Always specify the module version in batch scripts and production
   workflows.** Loading a module without a version loads the current
   system default, which can change during system maintenance. Silent
   version changes break reproducibility and are difficult to debug.

   .. code-block:: shell

      # Avoid in production scripts — default version may change:
      $ module load intel

      # Preferred — version is explicit and reproducible:
      $ module load intel/2023.2.1

Lmod's hierarchical system considers dependencies and prerequisites.
For example, ``cray-netcdf`` depends on ``cray-hdf5`` and cannot be
seen by ``module avail`` nor loaded until ``cray-hdf5`` is first
loaded.

When an upstream dependency is unloaded, downstream modules become
*inactive* (still listed, but not functional):

.. code-block:: shell

   $ module load cray-hdf5
   $ module load cray-netcdf
   $ module unload cray-hdf5

   Inactive Modules:
     cray-netcdf

Reloading ``cray-hdf5`` will reactivate ``cray-netcdf``.

.. rubric:: Swapping Module Versions

Use ``module swap`` to switch from one version of a module to another.
In a hierarchical system, ``module swap`` properly cascades the change
through dependent modules. Manually unloading and reloading does not
reliably propagate the change.

.. code-block:: shell

   $ module swap intel intel/2021.4.0

.. warning::

   Only unload modules that you explicitly loaded. Do not manually
   unload modules that were automatically loaded as dependencies —
   they are managed automatically by Lmod and removing them directly
   can leave your environment in an inconsistent state.


Module Collections
==================

Lmod can save and restore named sets of modules, called *collections*.
This is useful for complex environments you use regularly.

.. code-block:: shell

   $ module save myenv        # Save the current module state as "myenv"
   $ module restore myenv     # Restore the "myenv" collection
   $ module savelist          # List all saved collections

.. note::

   Module collections are saved per-system. A collection saved on one
   RDHPCS system will not be available on another system.


Adding Additional Module Paths
==============================

Do not manually set the ``MODULESPATH`` environment variable.
Manually setting ``MODULESPATH`` will produce unknown behavior.

Use ``module use <path>`` to prepend a path to the module search path,
or ``module use -a <path>`` to append it:

.. code-block:: shell

   $ module use /path/to/my/modulefiles

To remove a path from the module search:

.. code-block:: shell

   $ module unuse /path/to/my/modulefiles

Known community and project module paths on specific systems:

- **Jet**: ``module use /contrib/modulefiles``
- **Gaea (GFDL FRE)**: ``module use /ncrc/home2/fms/local/modulefiles``


Using Modules in Batch Jobs
============================

Modules must be explicitly initialized inside batch job scripts. The
scheduler does not automatically replicate your interactive login
environment inside a job.

.. warning::

   **Do not use** ``#!/bin/bash -l`` **(a login shell) in job
   scripts.** A login shell re-sources ``/etc/profile``,
   ``.bash_profile``, and similar startup files, which overrides the
   environment the scheduler has set up for your job. This causes
   mysterious and intermittent failures that are difficult to diagnose.

To make the ``module`` command available inside a job script, source
the appropriate initialization file near the top of your script,
before any ``module load`` commands:

.. code-block:: bash

   #!/bin/bash
   source $MODULESHOME/init/bash       # For bash scripts
   module load intel/2023.2.1
   module load impi/2021.10

For other shells:

.. code-block:: shell

   source $MODULESHOME/init/csh        # For csh/tcsh scripts
   source $MODULESHOME/init/sh         # For sh/ksh scripts

Other shells may be supported; inspect the ``$MODULESHOME/init/``
directory for the full list.

.. rubric:: Best Practices for Batch Jobs

- **Pin module versions** (see `Load Modules`_). The system default
  version can change between when you develop a workflow and when you
  run it in production.

- **Log your loaded modules** near the top of your job script. When a
  job fails, knowing exactly which modules were loaded is essential
  for debugging:

  .. code-block:: bash

     module list 2>&1

- **Test your module environment** in a short interactive or debug job
  before submitting long production runs.

.. rubric:: Modules in Cron Jobs

.. note::

   This section applies to Ursa, Hera, Mercury, and Jet only. On
   Gaea, use ``scrontab`` for recurring scheduled jobs.

Cron starts with a minimal environment and runs no system
initialization scripts, so the ``module`` command will not be defined.
Source the system modules initialization file before using ``module``:

.. code-block:: shell

   source /etc/profile.d/modules.sh       # For bash cron scripts
   source /etc/profile.d/modules.csh      # For csh/tcsh cron scripts

.. rubric:: Gaea-Specific Notes

.. warning::

   **Do not use** ``module purge`` **on Gaea.** Gaea loads critical
   system modules into your environment by default. Purging all modules
   will remove these and may make your session unusable.

   Use ``module reset`` to return to the system default module set
   without logging out:

   .. code-block:: shell

      $ module reset

On Gaea, use the Cray Programming Environment modules to set up your
compiler toolchain rather than loading individual compiler modules
directly. Loading a ``PrgEnv-*`` module selects the compiler and
configures the full software stack:

.. code-block:: shell

   $ module load PrgEnv-intel    # Intel compiler + Cray MPI wrappers
   $ module load PrgEnv-gnu      # GNU compiler + Cray MPI wrappers
   $ module load PrgEnv-cray     # Cray compiler + Cray MPI wrappers

See the :ref:`Gaea User Guide <gaea-environment-modules>` for full
details on the Gaea programming environment.


Command Summary
===============

+-------------------------------------------+------------------------------------------+
| Command                                   | Description                              |
+===========================================+==========================================+
| ``module list``                           | List active modules in the user          |
|                                           | environment                              |
+-------------------------------------------+------------------------------------------+
| ``module -t list``                        | Terse (one-per-line) list of active      |
|                                           | modules                                  |
+-------------------------------------------+------------------------------------------+
| ``module avail [module]``                 | List available modules compatible with   |
|                                           | the current environment                  |
+-------------------------------------------+------------------------------------------+
| ``module spider [module]``                | Search all modules in the full           |
|                                           | hierarchy, including those not yet       |
|                                           | available                                |
+-------------------------------------------+------------------------------------------+
| ``module keyword <term>``                 | Search all modules for a keyword         |
+-------------------------------------------+------------------------------------------+
| ``module show <module>``                  | Show environment changes a module would  |
|                                           | make, without loading it                 |
+-------------------------------------------+------------------------------------------+
| ``module load <module>[/version]``        | Load a module into the user environment  |
+-------------------------------------------+------------------------------------------+
| ``module unload <module>``                | Remove a loaded module from the user     |
|                                           | environment                              |
+-------------------------------------------+------------------------------------------+
| ``module swap <module1> <module2>``       | Replace module1 with module2, cascading  |
|                                           | dependency changes                       |
+-------------------------------------------+------------------------------------------+
| ``module use [-a] <path>``                | Prepend (or append with ``-a``) a path   |
|                                           | to MODULESPATH                           |
+-------------------------------------------+------------------------------------------+
| ``module unuse <path>``                   | Remove a path from MODULESPATH           |
+-------------------------------------------+------------------------------------------+
| ``module save [name]``                    | Save the current module set as a named   |
|                                           | collection                               |
+-------------------------------------------+------------------------------------------+
| ``module restore [name]``                 | Restore a previously saved collection    |
+-------------------------------------------+------------------------------------------+
| ``module savelist``                       | List all saved module collections        |
+-------------------------------------------+------------------------------------------+
| ``module reset``                          | Reset loaded modules to system defaults  |
+-------------------------------------------+------------------------------------------+
| ``module purge``                          | Unload **all** modules (**do not use     |
|                                           | on Gaea**)                               |
+-------------------------------------------+------------------------------------------+
| ``module update``                         | Reload all currently loaded modules      |
+-------------------------------------------+------------------------------------------+