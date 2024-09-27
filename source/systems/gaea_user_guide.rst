.. _gaea-user-guide:

###############
Gaea User Guide
###############

.. image:: /images/Gaea_web.jpg


.. _gaea-system-overview:

***************
System Overview
***************

`Gaea
<https://www.noaa.gov/organization/information-technology/gaea>`_ is
a `NOAA Research and Development High-Performance Computing System
(RDHPCS) <https://www.noaa.gov/information-technology/hpcc>`_ operated
by the `National Climate-Computing Research Center (NCRC)
<https://www.ncrc.gov/>`_.  The NCRC is located within the `National
Center for Computational Sciences (NCCS)
<https://www.ornl.gov/division/nccs>`_ at the `Oak Ridge National
Laboratory (ORNL) <https://www.ornl.gov/>`_.   The NCRC is a
collaborative effort between the `Department of Energy
<https://www.energy.gov/>`_ and the `National Atmospheric and Oceanic
Administration <https://www.noaa.gov/>`_.

The Gaea System consists of two HPE-Cray EX 3000 systems, referred to as C5 and
C6.  Two high-capacity parallel file systems provide over 150 petabytes of fast
access storage. The center-wide filesystem is connected using FDR InfiniBand to
the center's compute and data-transfer resources. The aggregate Gaea system
contains a peak calculating capability greater than 20 petaflops (quadrillion
floating point operations per second).

NOAA research partners access data remotely through fast
interconnections to NOAA's national research network through peering
points at Atlanta and Chicago.

.. grid:: 4

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light


    C5
    ^^^

    * HPE-EX Cray X3000

    * 1,920 compute nodes (2 x AMD EPYC 7H12 2.6GHz 64-cores per socket)

    * HPE Slingshot Interconnect

    * 264GB DDR4 per node; 500TB total

    * 10.22 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    F5 File System
    ^^^

    * IBM Spectrum Scale

    * 75 PB

    * IBM Elastic Storage Server 3500 running GPFS 5.1

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C6
    ^^^

    *  HPE-EX Cray X3000

    * 1,520 compute nodes (2 x AMD EPYC 9654 2.4GHz base 96-cores per socket)

    * HPE Slingshot Interconnect

    * 384GB DDR4 per node; 584TB total

    * 11.21 PF peak (base)

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    F6
    ^^^

    * IBM Spectrum Scale

    * 75 PB

    * IBM Elastic Storage Server 3500 running GPFS 5.1

Gaea is the largest of the four NOAA RDHPCS, and is used to study the
earth's notoriously complex climate from a variety of angles by
enabling scientists:

* to understand the relationship between climate change and extreme weather,
  and the atmosphere's chemical makeup and climate
* to investigate the climate role played by the oceans that cover nearly
  three-quarters of the globe.

.. _gaea-node-types:

Node types
==========

Gaea has three node types: :term:`login <login node>` (front-end, head-node)
:term:`compute <compute node>`, and :term:`data transfer <data transfer node>`
nodes (:abbr:`DTN (data transfer node)`).  The three node types are similar in
terms of hardware, but differ in their intended use.

+---------+----------------------------------------------------------------+
| Node    |                                                                |
| Type    | Description                                                    |
+=========+================================================================+
| Login   | You are placed on a login node when you connect to Gaea. This  |
| / Front | is where you write, edit, and compile your code, manage data   |
| / Head  | submit jobs, etc. You should not launch parallel or threaded   |
|         | jobs from a login node. Login nodes are shared resources.      |
+---------+----------------------------------------------------------------+
| Compute | Most of the nodes on Gaea are compute nodes. Your parallel and |
|         | threaded jobs execute on the compute nodes, via the            |
|         | :command:`srun` command.                                       |
+---------+----------------------------------------------------------------+
| DTN     | The DTNs have F5 and F6 file systems mounted.                  |
|         | This is where extensive I/O operations,                        |
|         | large local, and all off-gaea transfers should be done.  These |
|         | nodes are accessible via the :dfn:`es` cluster and the         |
|         | :dfn:`dtn_f5_f6` partition.                                    |
+---------+----------------------------------------------------------------+

.. _gaea-compute-nodes:

Compute nodes
=============

Gaea consists of two clusters, C5 and C6.

.. tab-set::

  .. tab-item:: C5
    :sync: C5

    The C5 compute nodes consist of [2x] 64 core AMD EPYC Zen 2 CPUs, with two
    hardware threads per physical core and 256 GiB of physical memory (2 GiB
    per core). C5 supports up to the AVX-2 :abbr:`ISA (Instruction Set
    Architecture)`.

    .. figure:: /images/C5-ComputeNodeDiagram.png

      Each C5 compute node has a total of 128 cores, in eight NUMA domains
      per node.  Each group of four cores share an 16 MB L3 cache.  Each CPU
      has eight lanes to the shared 256 GiB of node memory.

  .. tab-item:: C6
    :sync: C6

    The C6 compute nodes consist of [2x] 96 core AMD EPYC Zen 4 CPUs, with two
    hardware threads per physical core and 384 GiB of physical memory (2 GiB
    per core). C6 support up to the AVX-512 :abbr:`ISA (Instruction Set
    Architecture)`.

    .. figure:: /images/C6-ComputeNodeDiagram.png

      Each C6 compute node has a total of 192 cores, in eight NUMA domains per
      node.  Each group of six cores share a 48 MB L3 cache.  Each CPU has 12
      lanes to the shared 384 GiB of physical memory (2 GiB per core).


.. _gaea-login-nodes:

Login nodes
===========

The Gaea login nodes have a similar architecture to the compute nodes.  Each
compute cluster has a dedicated set of login nodes.

+----------------------+----------------------------+--------------------+
| Host Names           | Node Configuration         | Associated Compute |
|                      |                            | Cluster            |
+======================+============================+====================+
| :regexp:`gaea5[1-8]` | 2x AMD EPYC 7662 64-core   | C5                 |
|                      | (128 cores per node) with  |                    |
|                      | 512 GiB of memory per node |                    |
+----------------------+----------------------------+--------------------+
| :regexp:`gaea6[1-8]` | 2x AMD EPYC 9654 96-core   | C6                 |
|                      | (192 cores per node) with  |                    |
|                      | 512 GiB of memory per node |                    |
+----------------------+----------------------------+--------------------+

.. _gaea-dtn-nodes:

Data transfer nodes
===================

All extensive I/O operations, large local transfers and all off-gaea transfers
should be done on a data transfer node (DTN).  The :abbr:`DTN (Data Transfer
Nodes)`\ s are accessible on the :dfn:`es` cluster, under the :dfn:`dtn_f5_f6`
partition.

The DTNs are the only systems that have both the :dfn:`f5` and :dfn:`f6`
mounted.

+----------------------+----------------------------+--------------------+
| Host Names           | Node Configuration         | File Systems       |
|                      |                            | Mounted            |
+======================+============================+====================+
| :regexp:`dtn[50-79]` | AMD EPYC 7302 16-core with || /gpfs/f5          |
|                      | 256 GiB of memory per node || /gpfs/f6          |
+----------------------+----------------------------+--------------------+

System interconnect
===================

The C5 and C6 nodes are connected with the HPE Slingshot.

+---------+--------------------------------------+-------------+
| Cluster | :abbr:`NIC (Network Interface Card)` | Total       |
|         |                                      | Bandwidth   |
+=========+======================================+=============+
| C5      | [2x] HPE Slingshot 100 Gbps (12.5    | 200 Gbps    |
|         | GB/s)                                |             |
+---------+--------------------------------------+-------------+
| C6      | [1x] HPE Slingshot 200 Gbps (25.0    | 200 Gbps    |
|         | GB/s)                                |             |
+---------+--------------------------------------+-------------+

File systems
============

Gaea compute clusters C5 and C6 have their own file system.  C5 has
access to F5 mounted at :file:`/gpfs/f5`.  C6 has access to :file:`/gpfs/f6`.
The :abbr:`DTN (Data Transfer Nodes)`\ s can access both :file:`/gpfs/f5` and
:file:`/gpfs/f6`.

Operating system
================

The C5 and C6 clusters run the Cray OS operating system.  Cray OS is based on
SUSE Linux Enterprise Server (:abbr:`SLES (SUSE Linux Enterprise Server)`).

+---------+---------+---------+
| Cluster | Cray OS | SLES    |
|         | Version | Version |
+=========+=========+=========+
| C5      | 2.5     | 15.4    |
+---------+---------+---------+
| C6      | 3.0.2-2 | 15.5    |
+---------+---------+---------+

.. _HPE Cray EX Documentation: https://support.hpe.com/connect/s/product?kmpmoid=1013083813
.. _HPE Cray Programming Environment: https://cpe.ext.hpe.com/docs/latest/index.html

.. seealso::

    `HPE Cray EX Documentation`_
        Documentation specific for the HPE Cray EX 3000 compute system.

    `HPE Cray Programming Environment`_
        Documentation that covers the HPE Cray Programming Environment.

**********
Connecting
**********

To connect to Gaea, :command:`ssh` to ``gaea-rsa.rdhpcs.noaa.gov``.  For
example,

.. code-block:: shell

    $ ssh <First.Last>@gaea-rsa.rdhpcs.noaa.gov

For more information on connecting through the Boulder or Princeton bastion,
with a :abbr:`CAC (Common Access Card)`, or for your first connection, see
:ref:`connecting-to-rdhpcs`.

By default, the bastion will automatically place a user on a random Gaea C5
login node.  If you need to access a specific login node on C6, when prompted
enter :kbd:`Ctrl-C` and type the name of a login node or ``gaea6`` for a random
C6 login node:

.. cSpell:ignore CMRS
.. code-block:: shell

    $ ssh <First.Last>@gaea-rsa.rdhpcs.noaa.gov
    Last login: Wed Sep 11 17:20:24 2024 from 140.208.2.184

    Welcome to the NOAA RDHPCS.

    Attempting to renew your proxy certificate...Proxy certificate has 720:00:00  (30.0 days) left.

            Welcome to gaea.rdhpcs.noaa.gov
    Gateway to gaea-c5.ncrc.gov and other points beyond

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !! RDHPCS Policy states that all user login sessions shall be terminated     !!
    !! after a maximum duration of seven (7) days. ALL user login sessions will  !!
    !! be dropped from the Princeton Bastions at 4AM ET / 2AM MT each Monday     !!
    !! morning, regardless of the duration. Please note: This will NOT impact    !!
    !! batch jobs, cron scripts, screen sessions, remote desktop, or data        !!
    !! transfers.                                                                !!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    Hostname            Description
    gaea                C5 head nodes
    gaea51              C5 head node
    gaea52              C5 head node
    gaea53              C5 head node
    gaea54              C5 head node
    gaea55              C5 head node
    gaea56              C5 head node
    gaea57              C5 head node
    gaea58              C5 head node
    gaea60              T6 Test access only
    gaea61              C6 head node
    gaea62              C6 head node
    gaea63              C6 head node
    gaea64              C6 head node
    gaea65              C6 head node
    gaea66              C6 head node
    gaea67              C6 head node
    gaea68              C6 head node

    You will now be connected to NOAA RDHPCS: Gaea (CMRS/NCRC) C5 system.
    To select a specific host, hit ^C within 5 seconds.
    ^CEnter a hostname, or a unique portion of a hostname []:

****************
Data and storage
****************

NFS file systems
================

Users and projects are given space on the :abbr:`NFS (Network File System)`.
These locations are ideal for storing user and project applications,
executables, and small data files.

.. list-table::
    :header-rows: 1
    :align: left

    * - Area
      - Path
      - Permissions
      - Quota
      - Backups
      - Purged
      - On Compute Nodes
    * - User Home
      - :file:`/ncrc/home[12]/<userID>`
      - User set
      - 50 GB
      - Yes
      - No
      - Yes
    * - Project Home
      - :file:`/ncrc/proj/<projID>`
      - Project set
      - 100 GB
      - Yes
      - No
      - Yes


GPFS file systems
=================

Each compute cluster, C5 and C6, has its own file system called F5 and F6
respectively, mounted at :file:`/gpfs/f5` and :file:`/gpfs/f6`.

.. list-table::
    :header-rows: 1
    :align: left

    * - Area
      - Path
      - Permissions
      - Quota
      - Backups
      - Purged
      - On compute nodes
    * - F5 Member Work
      - :file:`/gpfs/f5/<projID>/scratch/<userID>`
      - User set
      - N/A
      - No
      - No
      - C5 only
    * - F5 Project Work
      - :file:`/gpfs/f5/<projID>/proj-shared`
      - 770
      - N/A
      - No
      - No
      - C5 only
    * - F5 World Work
      - :file:`/gpfs/f5/<projID>/world-shared`
      - 775
      - N/A
      - No
      - No
      - C5 only
    * - F6 Member Work
      - :file:`/gpfs/f6/<projID>/scratch/<userID>`
      - User set
      - N/A
      - No
      - No
      - C6 only
    * - F6 Project Work
      - :file:`/gpfs/f6/<projID>/proj-shared`
      - 770
      - N/A
      - No
      - No
      - C6 only
    * - F6 World Work
      - :file:`/gpfs/f6/<projID>/world-shared`
      - 775
      - N/A
      - No
      - No
      - C6 only

Move data to and from Gaea
==========================

The suggested way to move data to and from Gaea is `Globus Online
<https://app.globus.org>`_.  Please review the additional information in
:ref:`globus_online_data_transfer` and :ref:`globus_example`.

Please review :ref:`transferring-data` for information on other transfer
methods available.

.. _gaea-programming-environment:

***********************
Programming environment
***********************

Gaea users are provided with many pre-installed software packages and
scientific libraries.  Environment management tools are used to handle
necessary changes to the shell.

Please refer to the `HPE Cray Programming Environment`_ documentation for
specifics.

.. _gaea-environment-modules:

Environment Modules
===================

Environment modules are provided through `Lmod
<https://lmod.readthedocs.io/en/latest/>`_, a Lua-based module system for
dynamically altering shell environments. By managing changes to the shell’s
environment variables (such as ``PATH``, ``LD_LIBRARY_PATH``, and
``PKG_CONFIG_PATH``), Lmod allows you to alter the software available in your
shell environment without the risk of creating package and version combinations
that cannot coexist in a single environment.

General Usage
-------------

The interface to Lmod is provided by the :command:`module` command:

  .. cSpell:ignore modulename unuse MODULESPATH
+--------------------------------+--------------------------------------------+
| Command                        | Description                                |
+================================+============================================+
| ``module -t list``             | Shows a terse list of the currently loaded |
|                                | modules                                    |
+--------------------------------+--------------------------------------------+
| ``module avail``               | Shows a table of the currently available   |
|                                | modules                                    |
+--------------------------------+--------------------------------------------+
| ``module help <modulename>``   | Shows help information about               |
|                                | ``<modulename>``                           |
+--------------------------------+--------------------------------------------+
| ``module show <modulename>``   | Shows the environment changes made by the  |
|                                | ``<modulename>`` module file               |
+--------------------------------+--------------------------------------------+
| ``module spider <string>``     | Searches all possible modules according to |
|                                | <string>                                   |
+--------------------------------+--------------------------------------------+
| ``module load <modulename>     | Loads the given ``<modulename>``\ (s) into |
| [...]``                        | the current environment                    |
+--------------------------------+--------------------------------------------+
| ``module use <path>``          | Adds ``<path>`` to the module file search  |
|                                | cache and ``MODULESPATH``                  |
+--------------------------------+--------------------------------------------+
| ``module unuse <path>``        | Removes ``<path>`` from the module file    |
|                                | search cache and ``MODULESPATH``           |
+--------------------------------+--------------------------------------------+
| ``module purge``               | Unloads all modules                        |
+--------------------------------+--------------------------------------------+
| ``module reset``               | Resets loaded modules to system defaults   |
+--------------------------------+--------------------------------------------+
| ``module update``              | Reloads all currently loaded modules       |
+--------------------------------+--------------------------------------------+

Searching for Modules
---------------------

Modules with dependencies are only available when the underlying dependencies,
such as compiler families, are loaded. Thus, module avail will only display
modules that are compatible with the current state of the environment. To
search the entire hierarchy across all possible dependencies, the ``spider``
sub-command can be used as summarized in the following table.

+-----------------------------------------+-----------------------------------+
| Command                                 | Description                       |
+=========================================+===================================+
| ``module spider``                       | Shows the entire possible graph   |
|                                         | of modules                        |
+-----------------------------------------+-----------------------------------+
| ``module spider <modulename>``          | Searches for modules named        |
|                                         | ``<modulename>`` in the graph of  |
|                                         | possible modules                  |
+-----------------------------------------+-----------------------------------+
|``module spider <modulename>/<version>`` | Searches for a specific version   |
|                                         | of ``<modulename>`` in the graph  |
|                                         | of possible modules               |
+-----------------------------------------+-----------------------------------+
| ``module spider <string>``              | Searches for modulefiles          |
|                                         | containing ``<string>``           |
+-----------------------------------------+-----------------------------------+


Compilers
=========

Cray, AMD, NVIDIA, and GCC compilers are provided through modules on Gaea.
There is also a system/OS versions of GCC available in :file:`/usr/bin`. The
table below lists details about each of the module-provided compilers. Please
see the :ref:`gaea-compiling` section for more detailed information on
how using these modules to compile.

MPI
====

The MPI implementation available on Gaea is Cray's MPICH.


.. _gaea-compiling:

*********
Compiling
*********

.. _gaea-compilers:

Compilers
=========

Cray, AMD, NVIDIA, and GCC compilers are provided through modules on Gaea.
There is also a system/OS version of GCC available in :file:`/usr/bin`. The
table below lists details about each of the module-provided compilers.

.. important::

    It is highly recommended to use the Cray compiler wrappers (:command:`cc`,
    :command:`CC`, and :command:`ftn`) whenever possible. See the next section
    for more details.

.. cSpell:ignore aocc nvhpc oneapi craycc craycxx crayftn flang gfortran
.. cSpell:ignore icpx icc icpc ifort nvfortran craype
.. The following are substitutions to keep the table below the line length
   limit
.. |pe_aocc| replace:: ``PrgEnv-aocc``
.. |pe_cray| replace:: ``PrgEnv-cray``
.. |pe_gnu| replace:: ``PrgEnv-gnu``
.. |pe_intel| replace:: ``PrgEnv-intel``
.. |pe_nvhpc| replace:: ``PrgEnv-nvhpc``
.. |intel_cl| replace:: ``intel-classic``
.. |intel_oa| replace:: ``intel-oneapi``

+--------+-------------+----------------+----------+----------+---------------+
| Vendor | Programming | Compiler       | Language | Compiler | Compiler      |
|        | Environment | Module         |          | Wrapper  |               |
+========+=============+================+==========+==========+===============+
| AMD    | |pe_aocc|   | ``aocc``       | C        | ``cc``   | ``clang``     |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``clang++``   |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``flang``     |
+--------+-------------+----------------+----------+----------+---------------+
| Cray   | |pe_cray|   | ``cce``        | C        | ``cc``   | ``craycc``    |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``craycxx``   |
|        |             |                |          |          | or            |
|        |             |                |          |          | ``crayCC``    |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``crayftn``   |
+--------+-------------+----------------+----------+----------+---------------+
| GNU    | |pe_gnu|    | ``gcc-native`` | C        | ``cc``   | ``gcc``       |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``g++``       |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``gfortran``  |
+--------+-------------+----------------+----------+----------+---------------+
| Intel  | |pe_intel|  | ``intel``      | C        | ``cc``   | ``icx``       |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``icpx``      |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``ifort``     |
|        |             +----------------+----------+----------+---------------+
|        |             | |intel_cl|     | C        | ``cc``   | ``icc``       |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``icpc``      |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``ifort``     |
|        |             +----------------+----------+----------+---------------+
|        |             | |intel_oa|     | C        | ``cc``   | ``icx``       |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``icpx``      |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``ifx``       |
+--------+-------------+----------------+----------+----------+---------------+
| NVIDIA | |pe_nvhpc|  | ``nvhpc``      | C        | ``cc``   | ``nvc``       |
|        |             |                +----------+----------+---------------+
|        |             |                | C++      | ``CC``   | ``nvc++``     |
|        |             |                +----------+----------+---------------+
|        |             |                | Fortran  | ``ftn``  | ``nvfortran`` |
+--------+-------------+----------------+----------+----------+---------------+

.. note::

    The ``gcc-native`` compiler module was introduced in the December 2023
    release of the HPE/Cray Programming Environment (CrayPE) and replaces
    ``gcc``. ``gcc`` provides GCC installations that were packaged within
    CrayPE, while ``gcc-native`` provides GCC installations outside of CrayPE.

Cray programming environment and compiler wrappers
--------------------------------------------------

Cray provides ``PrgEnv-<compiler>`` modules (for example, ``PrgEnv-cray``) that
load compatible components of a specific compiler toolchain. The components
include the specified compiler as well as MPI, LibSci, and other libraries.
Loading the ``PrgEnv-<compiler>`` modules also defines a set of compiler
wrappers for that compiler toolchain that automatically add include paths and
link in libraries for Cray software. Compiler wrappers are provided for C
(:command:`cc`), C++ (:command:`CC`), and Fortran (:command:`ftn`).

For example, to load the Intel programming environment do:

.. code-block:: shell

    $ module load PrgEnv-intel

This module will setup your programming environment with paths to software and
libraries that are compatible with Intel host compilers.

.. note::

    Use the ``-craype-verbose`` compiler flag to display the full include and link
    information used by the Cray compiler wrappers. This must be called on a
    file, for example ``CC -craype-verbose test.cpp``.

.. _gaea-running:

************
Running jobs
************

Computational work on Gaea is performed by *jobs*. Jobs typically consist of
several components:

-  A batch submission script
-  A binary executable
-  A set of input files for the executable
-  A set of output files created by the executable

In general, the process for running a job is:

#. prepare executables and input files
#. write a batch script
#. submit the batch script to the batch scheduler
#. optionally monitor the job before and during execution

The following sections describe in detail how to create, submit, and manage
jobs for execution on Frontier. Frontier uses SchedMD's Slurm Workload Manager
as the batch scheduling system.


Login vs Compute Nodes
======================

Recall from the `System Overview <#system-overview>`_ that Gaea contains two
node types: Login and Compute. When you connect to the system, you are placed
on a *login* node. Login nodes are used for tasks such as code editing,
compiling, etc. They are shared among all users of the system, so it is not
appropriate to run tasks that are long or computationally intensive on login
nodes. Users should also limit the number of simultaneous tasks on login nodes
(e.g. concurrent tar commands, parallel make).

Compute nodes are the appropriate place for long-running,
computationally-intensive tasks. When you start a batch job, your batch script
(or interactive shell for batch-interactive jobs) runs on one of your allocated
compute nodes.

.. warning::

  Compute-intensive, memory-intensive, or other disruptive processes running on
  login nodes may be killed without warning.

Slurm
=====

Gaea uses `SchedMD <https://www.schedmd.com/>`_\ 's Slurm Workload Manager to
schedule and manage jobs. A few items related to Slurm are below.  See
:ref:`our local Slurm overview<slurm-scheduler>` or the official `Slurm
documentation <https://slurm.schedmd.com/documentation.html>`_ for more
information.

Slurm documentation is also available for each command via the :command:`man`
utility, and on the web at `<https://slurm.schedmd.com/man_index.html>`__.

.. seealso::

    `Slurm documentation`_
        The official SchedMD Slurm documentation.

Batch Scripts
-------------

The most common way to interact with the batch system is via batch scripts. A
batch script is simply a shell script with added directives to request various
resources from or provide certain information to the scheduling system.  Aside
from these directives, the batch script is simply the series of commands needed
to set up and run your job.

.. cSpell:ignore myjob.sl

To submit a batch script, use the command ``sbatch myjob.sl``, where
``myjob.sl`` is the bach script.

Consider the following batch script:

.. code-block:: bash
   :linenos:

   #!/bin/bash
   #SBATCH -M c5
   #SBATCH -A ABC123
   #SBATCH -J RunSim123
   #SBATCH -o %x-%j.out
   #SBATCH -t 1:00:00
   #SBATCH -p batch
   #SBATCH -N 1024

   cd /gpfs/f5/${SBATCH_ACCOUNT}/scratch/$USER/abc123/Run.456
   cp /gpfs/f5/${SBATCH_ACCOUNT/proj-shared/abc123/RunData/Input.456 ./Input.456
   srun ...
   cp my_output_file /gpfs/f5/${SBATCH_ACCOUNT}/proj-shared/abc123/RunData/Output.456

In the script, Slurm directives are preceded by ``#SBATCH``, making them appear
as comments to the shell. Slurm looks for these directives through the first
non-comment, non-whitespace line. Options after that will be ignored by Slurm
(and the shell).

+------+----------------------------------------------------------------------+
| Line | Description                                                          |
+======+======================================================================+
|    1 | Shell interpreter line                                               |
+------+----------------------------------------------------------------------+
|    2 | Gaea cluster to use                                                  |
+------+----------------------------------------------------------------------+
|    3 | RDHPCS project to charge                                             |
+------+----------------------------------------------------------------------+
|    4 | Job name                                                             |
+------+----------------------------------------------------------------------+
|    5 | Job standard output file (``%x`` will be replaced with the job name  |
|      | and ``%j`` with the Job ID)                                          |
+------+----------------------------------------------------------------------+
|    6 | Walltime requested (in ``HH:MM:SS`` format). See the table below for |
|      | other formats.                                                       |
+------+----------------------------------------------------------------------+
|    7 | Partition (queue) to use                                             |
+------+----------------------------------------------------------------------+
|    8 | Number of compute nodes requested                                    |
+------+----------------------------------------------------------------------+
|    9 | Blank line                                                           |
+------+----------------------------------------------------------------------+
|   10 | Change into the run directory                                        |
+------+----------------------------------------------------------------------+
|   11 | Copy the input file into place                                       |
+------+----------------------------------------------------------------------+
|   12 | Run the job ( add layout details )                                   |
+------+----------------------------------------------------------------------+
|   13 | Copy the output file to an appropriate location.                     |
+------+----------------------------------------------------------------------+

.. _frontier-interactive:

Interactive Jobs
----------------

Most users will find batch jobs an easy way to use the system, as they allow
you to "hand off" a job to the scheduler, allowing them to focus on other tasks
while their job waits in the queue and eventually runs. Occasionally, it is
necessary to run interactively, especially when developing, testing, modifying
or debugging a code.

Since all compute resources are managed and scheduled by Slurm, you can't
simply log into the system and immediately begin running parallel codes
interactively. Rather, you must request the appropriate resources from Slurm
and, if necessary, wait for them to become available. This is done through an
"interactive batch" job. Interactive batch jobs are submitted with the
:command:`salloc` command.  You request resources using the same options that
are passed via ``#SBATCH`` in a regular batch script (but without the
``#SBATCH`` prefix). For example, to request an interactive batch job with the
same resources that the batch script above requests, you would use ``salloc -A
ABC123 -J RunSim123 -t 1:00:00 -p batch -N 1024``. Note there is no option for
an output file if you are running interactively, so standard output and
standard error will be displayed to the terminal.

.. warning::

    Indicating your shell in your :command:`salloc` command, for example
    ``salloc ... /bin/bash``, is NOT recommended. This will cause your
    compute job to start on a login node, rather than automatically moving you
    to a compute node.

.. _common-slurm-options:

Common Slurm Options
--------------------

The table below summarizes options for submitted jobs. Unless otherwise noted,
they can be used for either batch scripts or interactive batch jobs. For
scripts, they can be added on the :command:`sbatch` command line or as a
``#SBATCH`` directive in the batch script. (If they're specified in both
places, the command line takes precedence.) This is only a subset of all
available options. Check the `Slurm Man Pages
<https://slurm.schedmd.com/man_index.html>`_ for a more complete list.

.. cSpell:ignore jobout joberr SIGUSR NODELIST usagefactor maxwall
.. table::
    :widths: 15 28 57

    +------------------------+----------------------------------+-------------------------------------------+
    | Option                 | Example Usage                    | Description                               |
    +========================+==================================+===========================================+
    | ``-A``                 | ``#SBATCH -A ABC123``            | Specifies the project to which the job    |
    |                        |                                  | should be charged                         |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-N``                 | ``#SBATCH -N 1024``              | Request 1024 nodes for the job            |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-t``                 | ``#SBATCH -t 4:00:00``           | Request a walltime of 4 hours.            |
    |                        |                                  | Walltime requests can be specified as     |
    |                        |                                  | minutes, hours:minutes,                   |
    |                        |                                  | hours:minutes:seconds, days-hours,        |
    |                        |                                  | days-hours:minutes, or                    |
    |                        |                                  | days-hours:minutes:seconds                |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``--threads-per-core`` | ``#SBATCH --threads-per-core=2`` | Number of active hardware threads per     |
    |                        |                                  | core. Can be 1 or 2 (1 is default).       |
    |                        |                                  |                                           |
    |                        |                                  | **Must** be used if using                 |
    |                        |                                  | ``--threads-per-core=2`` in your ``srun`` |
    |                        |                                  | command.                                  |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-d``                 | ``#SBATCH -d afterok:12345``     | Specify job dependency (in this example,  |
    |                        |                                  | this job cannot start until job 12345     |
    |                        |                                  | exits with an exit code of 0. See the Job |
    |                        |                                  | Dependency section for more information.  |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-J``                 | ``#SBATCH -J MyJob123``          | Specify the job name (this will show up   |
    |                        |                                  | in queue listings)                        |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-o``                 | ``#SBATCH -o jobout.%j``         | File where job STDOUT will be directed    |
    |                        |                                  | (%j will be replaced with the job ID). If |
    |                        |                                  | no `-e` option is specified, job STDERR   |
    |                        |                                  | will be placed in this file, too.         |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-e``                 | ``#SBATCH -e joberr.%j``         | File where job STDERR will be directed    |
    |                        |                                  | (%j will be replaced with the job ID). If |
    |                        |                                  | no `-o` option is specified, job STDOUT   |
    |                        |                                  | will be placed in this file, too.         |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``--mail-type``        | ``#SBATCH --mail-type=END``      | Send email for certain job actions. Can   |
    |                        |                                  | be a comma-separated list. Actions        |
    |                        |                                  | include BEGIN, END, FAIL, REQUEUE,        |
    |                        |                                  | INVALID_DEPEND, STAGE_OUT, ALL, and more. |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``--mail-user``        | ``#SBATCH                        | Email address to be used for              |
    |                        | --mail-user=user@somewhere.com`` | notifications.                            |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``--reservation``      | ``#SBATCH                        | Instructs Slurm to run a job on nodes     |
    |                        | --reservation=MyReservation.1``  | that are part of the specified re         |
    |                        |                                  | reservation                               |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``-S``                 | ``#SBATCH -S 8``                 | Instructs Slurm to reserve a specific     |
    |                        |                                  | number of cores per node (default is 8).  |
    |                        |                                  | Reserved cores cannot be used by the      |
    |                        |                                  | application.                              |
    +------------------------+----------------------------------+-------------------------------------------+
    | ``--signal``           | ``#SBATCH --signal=USR1@300``    || Send the given signal to a job the       |
    |                        |                                  | specified time (in seconds) seconds       |
    |                        |                                  | before the job reaches its walltime. The  |
    |                        |                                  | signal can be by name or by number (i.e.  |
    |                        |                                  | both 10 and USR1 would send SIGUSR1).     |
    |                        |                                  ||                                          |
    |                        |                                  || Signaling a job can be used, for         |
    |                        |                                  | example, to force a job to write a        |
    |                        |                                  | checkpoint just before Slurm kills the    |
    |                        |                                  | job (note that this option only sends the |
    |                        |                                  | signal; the user must still make sure     |
    |                        |                                  | their job script traps the signal and     |
    |                        |                                  | handles it in the desired manner).        |
    |                        |                                  ||                                          |
    |                        |                                  || When used with ``sbatch``, the signal    |
    |                        |                                  | can be prefixed by "B:" (e.g.             |
    |                        |                                  | ``--signal=B:USR1@300``) to tell Slurm to |
    |                        |                                  | signal only the batch shell; otherwise    |
    |                        |                                  | all processes will be signaled.           |
    +------------------------+----------------------------------+-------------------------------------------+


Slurm Environment Variables
---------------------------

Slurm reads a number of environment variables, many of which can provide the
same information as the job options noted above. We recommend using the job
options rather than environment variables to specify job options, as it allows
you to have everything self-contained within the job submission script, instead
than having to remember what options you set for a given job.

Slurm also provides a number of environment variables within your running job.
The following table summarizes those that may be particularly useful within
your job:

+--------------------------+--------------------------------------------------+
| Variable                 | Description                                      |
+==========================+==================================================+
| ``$SLURM_SUBMIT_DIR``    | The directory from which the batch job was       |
|                          | submitted. By default, a new job starts in your  |
|                          | home directory. You can get back to the          |
|                          | directory of job submission with                 |
|                          | ``cd $SLURM_SUBMIT_DIR``. Note that this is not  |
|                          | necessarily the same directory in which the      |
|                          | batch script resides.                            |
+--------------------------+--------------------------------------------------+
| ``$SLURM_ACCOUNT``       | The account name supplied by the user.           |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOBID``         | The job's full identifier. A common use for      |
|                          | ``$SLURM_JOBID`` is to append the job's ID       |
|                          | to the standard output and error files.          |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOB_NUM_NODES`` | The number of nodes requested.                   |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOB_NAME``      | The job name supplied by the user.               |
+--------------------------+--------------------------------------------------+
| ``$SLURM_NODELIST``      | The list of nodes assigned to the job.           |
+--------------------------+--------------------------------------------------+


Job States
----------

A job will transition through several states during its lifetime. Common ones
include:

+-------+------------+--------------------------------------------------------+
| State | State      | Description                                            |
| Code  |            |                                                        |
+=======+============+========================================================+
| CA    | Canceled   | The job was canceled (could've been by the user or an  |
|       |            | administrator)                                         |
+-------+------------+--------------------------------------------------------+
| CD    | Completed  | The job completed successfully (exit code 0)           |
+-------+------------+--------------------------------------------------------+
| CG    | Completing | The job is in the process of completing (some          |
|       |            | processes may still be running)                        |
+-------+------------+--------------------------------------------------------+
| PD    | Pending    | The job is waiting for resources to be allocated       |
+-------+------------+--------------------------------------------------------+
| R     | Running    | The job is currently running                           |
+-------+------------+--------------------------------------------------------+


Job Reason Codes
----------------

In addition to state codes, jobs that are pending will have a *reason code* to
explain why the job is pending. Completed jobs will have a reason describing
how the job ended. Some codes you might see include:

+-------------------+---------------------------------------------------------+
| Reason            | Meaning                                                 |
+===================+=========================================================+
| Dependency        | Job has dependencies that have not been met             |
+-------------------+---------------------------------------------------------+
| JobHeldUser       | Job is held at user's request                           |
+-------------------+---------------------------------------------------------+
| JobHeldAdmin      | Job is held at system administrator's request           |
+-------------------+---------------------------------------------------------+
| Priority          | Other jobs with higher priority exist for the           |
|                   | partition/reservation                                   |
+-------------------+---------------------------------------------------------+
| Reservation       | The job is waiting for its reservation to become        |
|                   | available                                               |
+-------------------+---------------------------------------------------------+
| AssocMaxJobsLimit | The job is being held because the user/project has hit  |
|                   | the limit on running jobs                               |
+-------------------+---------------------------------------------------------+
| ReqNodeNotAvail   | The job requested a particular node, but it's currently |
|                   | unavailable (it's in use, reserved, down, draining,     |
|                   | etc.)                                                   |
+-------------------+---------------------------------------------------------+
| JobLaunchFailure  | Job failed to launch (could due to system problems,     |
|                   | invalid program name, etc.)                             |
+-------------------+---------------------------------------------------------+
| NonZeroExitCode   | The job exited with some code other than 0              |
+-------------------+---------------------------------------------------------+

Many other states and job reason codes exist. For a more complete description,
see the :manpage:`squeue(1)` man page.


Scheduling Policy
-----------------

In a simple batch queue system, jobs run in a first-in, first-out (FIFO) order.
This can lead to inefficient use of the system. If a large job is the next to
run, a strict FIFO queue can cause nodes to sit idle while waiting for the
large job to start. *Backfilling* would allow smaller, shorter jobs to use
those resources that would otherwise remain idle until the large job starts.
With the proper algorithm, they would do so without impacting the start time of
the large job. While this does make more efficient use of the system, it
encourages the submission of smaller jobs.


Job priority
------------

Slurm on Gaea uses the `Slurm priority/multifactor plugin
<https://slurm.schedmd.com/priority_multifactor.html>`_ to calculate a job's
priority.  The factors used are:

Age
    the length of time a job has been waiting in the queue, eligible to be
    scheduled

Fair-share
    the difference between the portion of the computing resources that has been
    promised (allocation) and the amount of resources that has been consumed.
    Gaea uses the `classic fairshare algorithm
    <https://slurm.schedmd.com/classic_fair_share.html>`_


:abbr:`QOS (Quality of Service)`
    a factor associated with each Quality Of Service (QOS)

.. note::

    Only the QOSes on the compute clusters will affect a job's priority value.


+----------+----------+--------+----------+-----------------------------------+
| QOS      | Priority | Usage  | Max      | Description                       |
|          | Factor   | Factor | Walltime |                                   |
+==========+==========+========+==========+===================================+
| normal   | 0.85     | 1.00   | 16 hours | The default QOS for compute       |
|          |          |        |          | cluster jobs                      |
+----------+----------+--------+----------+-----------------------------------+
| debug    | 1.00     | 1.00   | 1 hour   | The highest priority QOS.  Useful |
|          |          |        |          | for short, non-production work.   |
+----------+----------+--------+----------+-----------------------------------+
| urgent   | 0.95     | 1.00   | 16 hours | QOS to allow groups to prioritize |
|          |          |        |          | their project's jobs              |
+----------+----------+--------+----------+-----------------------------------+
| windfall | 0.00     | 0.00   | 16 hours | Lowest priority as only age and   |
|          |          |        |          | fair-share are used in priority   |
|          |          |        |          | calculation.  The windfall QOS    |
|          |          |        |          | will also keep jobs from          |
|          |          |        |          | affecting the project's overall   |
|          |          |        |          | fair-share                        |
+----------+----------+--------+----------+-----------------------------------+

.. note::

    Interactive jobs, that is jobs started with the :command:`salloc` command,
    will have the QOS *interactive* automatically added unless the ``--qos``
    option is used.  The *interactive* QOS has the same priority factor as the
    *debug* QOS.  However, users can only have a single *Interactive* job at
    any time.

.. note::

    The priority and usage factors for all QOSes can be found using the command
    :command:`sacctmgr show qos format=name,priority,usagefactor,maxwall`.

    The command :command:`sprio` can be used to see the current priority, and
    the age, fair-share, and qos factors for a specific jobs.

    The command :command:`sshare` will show the current shares (allocation),
    usage, and fair-share factors for all projects (allocations).

Partitions
----------

+---------+------------+-----+-------+----------+----------+------------------+
|         | Name       | Nodes       | Time                | Description      |
+         +            +-----+-------+----------+----------+                  +
| Cluster | Name       | Min | Max   | Default  | Maximum  |                  |
+=========+============+=====+=======+==========+==========+==================+
| C5 and  | batch      | 1   | 512   | 12:00:00 | 16:00:00 | Default for jobs |
| C6      |            |     |       |          |          | under the max    |
|         |            |     |       |          |          | node count.      |
+         +------------+-----+-------+----------+----------+------------------+
|         | novel      | 513 | *max* | 12:00:00 | 16:00:00 | Default for jobs |
|         |            |     |       |          |          | above the        |
|         |            |     |       |          |          | minimum node     |
|         |            |     |       |          |          | count.  This     |
|         |            |     |       |          |          | partition is     |
|         |            |     |       |          |          | only enabled     |
|         |            |     |       |          |          | after a system   |
|         |            |     |       |          |          | maintenance.     |
|         |            |     |       |          |          | Please alert the |
|         |            |     |       |          |          | HD if you need   |
|         |            |     |       |          |          | to run a job in  |
|         |            |     |       |          |          | this partition.  |
+---------+------------+-----+-------+----------+----------+------------------+
| ES      | eslogin_c5 | 1   | *max* | 12:00:00 | 16:00:00 | These jobs will  |
|         |            |     |       |          |          | run on the C5    |
|         |            |     |       |          |          | login nodes.     |
+         +------------+-----+-------+----------+----------+------------------+
|         | eslogin_c6 | 1   | *max* | 12:00:00 | 16:00:00 | These jobs will  |
|         |            |     |       |          |          | run on the C6    |
|         |            |     |       |          |          | login nodes.     |
+         +------------+-----+-------+----------+----------+------------------+
|         | dtn_f5_f6  | 513 | *max* | 12:00:00 | 16:00:00 | These jobs will  |
|         |            |     |       |          |          | run on the DTN   |
|         |            |     |       |          |          | nodes.  The DTN  |
|         |            |     |       |          |          | nodes have both  |
|         |            |     |       |          |          | F5 and F6        |
|         |            |     |       |          |          | mounted.         |
+         +------------+-----+-------+----------+----------+------------------+
|         | cron_c5    | 1   | *max* | 12:00:00 | 16:00:00 | Required         |
|         |            |     |       |          |          | partition for    |
|         |            |     |       |          |          | jobs run under   |
|         |            |     |       |          |          | scron on the C5  |
|         |            |     |       |          |          | login nodes.     |
+         +------------+-----+-------+----------+----------+------------------+
|         | cron_c6    | 1   | *max* | 12:00:00 | 16:00:00 | Required         |
|         |            |     |       |          |          | partition for    |
|         |            |     |       |          |          | jobs run under   |
|         |            |     |       |          |          | scron on the C6  |
|         |            |     |       |          |          | login nodes.     |
+---------+------------+-----+-------+----------+----------+------------------+

.. note::

    The partition information above, and additional information can be listed
    using the :command:`scontrol --cluster <cluster> show partition` where
    :command:`<cluster>` is the name of one of the available clusters.

Job Dependencies
----------------

Frequently, a job will need data from some other job in the queue, but it's
nonetheless convenient to submit the second job before the first finishes.
Slurm allows you to submit a job with constraints that will keep it from
running until these dependencies are met. These are specified with the ``-d``
option to Slurm. Common dependency flags are summarized below. In each of these
examples, only a single jobid is shown but you can specify multiple job IDs as
a colon-delimited list (i.e. ``#SBATCH -d afterok:12345:12346:12346``). For the
``after`` dependency, you can optionally specify a ``+time`` value for each
jobid.

.. table::
    :widths: 25 75

    +-----------------------------------+------------------------------------------------+
    | Flag                              | Meaning (for the dependent job)                |
    +===================================+================================================+
    | ``#SBATCH -d after:jobid[+time]`` | The job can start after the specified jobs     |
    |                                   | start or are canceled. The optional ``+time``  |
    |                                   | argument is a number of minutes. If specified, |
    |                                   | the job cannot start until that many minutes   |
    |                                   | have passed since the listed jobs start/are    |
    |                                   | canceled. If not specified, there is no delay. |
    +-----------------------------------+------------------------------------------------+
    | ``#SBATCH -d afterany:jobid``     | The job can start after the specified jobs     |
    |                                   | have ended (regardless of exit state)          |
    +-----------------------------------+------------------------------------------------+
    | ``#SBATCH -d afternotok:jobid``   | The job can start after the specified jobs     |
    |                                   | terminate in a failed (non-zero) state         |
    +-----------------------------------+------------------------------------------------+
    | ``#SBATCH -d afterok:jobid``      | The job can start after the specified jobs     |
    |                                   | complete successfully (i.e. zero exit code)    |
    +-----------------------------------+------------------------------------------------+
    | ``#SBATCH -d singleton``          | Job can begin after any previously-launched    |
    |                                   | job with the same name and from the same user  |
    |                                   | have completed. In other words, serialize the  |
    |                                   | running jobs based on username+jobname pairs.  |
    +-----------------------------------+------------------------------------------------+


Monitoring and modifying batch jobs
-----------------------------------

Holding and releasing jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you may need to place a hold on a job to keep it from starting. For
example, you may have submitted it assuming some needed data was in place but
later realized that data is not yet available. You can do this with the
``scontrol hold`` command. Later, when the data is ready, you can release the
job (i.e. tell the system that it's now OK to run the job) with the ``scontrol
release`` command. For example:

+----------------------------+------------------------------------------------+
| ``scontrol hold 12345``    | Place job 12345 on hold                        |
+----------------------------+------------------------------------------------+
| ``scontrol release 12345`` | Release job 12345 (i.e. tell the system it's   |
|                            | OK to run it)                                  |
+----------------------------+------------------------------------------------+


Changing job parameters
^^^^^^^^^^^^^^^^^^^^^^^

There may also be occasions where you want to modify a job that's waiting in
the queue. For example, perhaps you requested 2,000 nodes but later realized
this is a different data set and only needs 1,000 nodes. You can use the
``scontrol update`` command for this. For example:

+-------------------+-----------------------------------------------+
| ``scontrol update | Change job 12345's node request to 1000 nodes |
| NumNodes=1000     |                                               |
| JobID=12345``     |                                               |
+-------------------+-----------------------------------------------+
| ``scontrol update | Change job 12345's max walltime to 4 hours    |
| TimeLimit=4:00:00 |                                               |
| JobID=12345``     |                                               |
+-------------------+-----------------------------------------------+


Cancel or signal a job
^^^^^^^^^^^^^^^^^^^^^^

In addition to the ``--signal`` option for the ``sbatch``/``salloc`` commands
described :ref:`above <common-slurm-options>`, the ``scancel`` command can be
used to manually signal a job. Typically, this is used to remove a job from the
queue. In this use case, you do not need to specify a signal and can simply
provide the jobid (i.e. ``scancel 12345``). If you want to send some other
signal to the job, use ``scancel`` the with the ``-s`` option. The ``-s``
option allows signals to be specified either by number or by name. Thus, if you
want to send ``SIGUSR1`` to a job, you would use ``scancel -s 10 12345`` or
``scancel -s USR1 12345``.


View the queue
^^^^^^^^^^^^^^

The ``squeue`` command is used to show the batch queue. You can filter the
level of detail through several command-line options. For example:

+--------------------------+------------------------------------------------+
| ``squeue -l``            | Show all jobs currently in the queue           |
+--------------------------+------------------------------------------------+
| ``squeue -l -u $USER``   | Show all of *your* jobs currently in the queue |
+--------------------------+------------------------------------------------+


Get job accounting information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``sacct`` command gives detailed information about jobs currently in the
queue and recently-completed jobs. You can also use it to see the various steps
within a batch jobs.

+------------------------------------------+----------------------------------+
| ``sacct -a -X``                          | Show all jobs (``-a``) in the    |
|                                          | queue, but summarize the whole   |
|                                          | allocation instead of showing    |
|                                          | individual steps (``-X``)        |
+------------------------------------------+----------------------------------+
| ``sacct -u $USER``                       | Show all of your jobs, and show  |
|                                          | the individual steps (since      |
|                                          | there was no ``-X`` option)      |
+------------------------------------------+----------------------------------+
| ``sacct -j 12345``                       | Show all job steps that are part |
|                                          | of job 12345                     |
+------------------------------------------+----------------------------------+
| ``sacct -u $USER -S 2022-07-01T13:00:00  | Show all of your jobs since 1 PM |
| -o "jobid%5,jobname%25,nodelist%20" -X`` | on July 1, 2022 using a          |
|                                          | particular output format         |
+------------------------------------------+----------------------------------+

Get detailed job information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to holding, releasing, and updating the job, the ``scontrol``
command can show detailed job information via the ``show job`` subcommand. For
example, ``scontrol show job 12345``.


.. _slurm-srun:

Srun
----

The default job launcher for Gaea is `srun
<https://slurm.schedmd.com/srun.html>`__ . The :command:`srun` command is used
to execute an MPI binary on one or more compute nodes in parallel.

Srun Format
^^^^^^^^^^^

.. code-block:: shell

    $ srun [OPTIONS... [executable [args...]]]

Single Command (non-interactive)

.. code-block:: bash

    $ srun -A <project_id> -t 00:05:00 -p <partition> -N 2 -n 4 --ntasks-per-node=2 ./a.out
    <output printed to terminal>

The job name and output options have been removed since stdout/stderr are
typically desired in the terminal window in this usage mode.


:command:`srun` accepts the following common options:

.. cSpell:ignore ncpus
.. table::
    :widths: 30 70

    +------------------------------------------------+--------------------------------------------+
    | ``-N``                                         | Number of nodes                            |
    +------------------------------------------------+--------------------------------------------+
    | ``-n``                                         | Total number of MPI tasks (default is 1)   |
    +------------------------------------------------+--------------------------------------------+
    | ``-c, --cpus-per-task=<ncpus>``                | Logical cores per MPI task (default is 1). |
    |                                                | When used with ``--threads-per-core=1``:   |
    |                                                | ``-c`` is equivalent to *physical* cores   |
    |                                                | per task. By default, when ``-c > 1``,     |
    |                                                | additional cores per task are distributed  |
    |                                                | within one L3 region first before filling  |
    |                                                | a different L3 region.                     |
    +------------------------------------------------+--------------------------------------------+
    | ``--cpu-bind=threads``                         | Bind tasks to CPUs.                        |
    |                                                | ``threads`` - (default, recommended)       |
    |                                                | Automatically generate masks binding tasks |
    |                                                | to threads.                                |
    +------------------------------------------------+--------------------------------------------+
    | ``--threads-per-core=<threads>``               | In task layout, use the specified maximum  |
    |                                                | number of hardware threads per core        |
    |                                                | (default is 1; there are 2 hardware        |
    |                                                | threads per physical CPU core).            |
    |                                                | Must also be set in ``salloc`` or          |
    |                                                | ``sbatch`` if using                        |
    |                                                | ``--threads-per-core=2`` in your ``srun``  |
    |                                                | command.                                   |
    +------------------------------------------------+--------------------------------------------+
    | ``-m, --distribution=<value>:<value>:<value>`` | Specifies the distribution of MPI ranks    |
    |                                                | across compute nodes, sockets (L3          |
    |                                                | regions), and cores, respectively.         |
    |                                                | The default values are                     |
    |                                                | ``block:cyclic:cyclic``, see ``man srun``  |
    |                                                | for more information.                      |
    +------------------------------------------------+--------------------------------------------+
    |  ``--ntasks-per-node=<ntasks>``                | If used without ``-n``: requests that a    |
    |                                                | specific number of tasks be invoked on     |
    |                                                | each node.                                 |
    |                                                | If used with ``-n``: treated as a          |
    |                                                | *maximum* count of tasks per node.         |
    +------------------------------------------------+--------------------------------------------+

********
Software
********

Gaea has several software and libraries available.  These are accessible using
the :ref:`Lmod module system <gaea-environment-modules>`.  Use the `module
avail` and `module spider` commands to see the list of software.  Only modules
in the :file:`/opt` and :file:`/sw` areas are supported at the RDHPCS level.
Projects and users can install software and software stacks in their user or
project spaces, that is in :file:`/ncrc/home[12]/$USER/`, :file:`/usw`, and
:file:`/ncrc/proj` locations. Those projects and users then maintain and
support the software and software stacks.

*********
Debugging
*********

Linaro DDT
==========

Linaro DDT is an advanced debugging tool used for scalar, multi-threaded, and
large-scale parallel applications. In addition to traditional debugging
features (setting breakpoints, stepping through code, examining variables), DDT
also supports attaching to already-running processes and memory debugging.
In-depth details of DDT can be found in the official `DDT User Guide
<https://docs.linaroforge.com/latest/html/forge/forge/introduction_to_forge/ddt.html>`_,
and instructions for how to use it on RDHPCS systems can be found on the
:doc:`Debugging Software </software/debuggers/index>` page. DDT is the RDHPCS's
recommended debugging software for large parallel applications.

One of the most useful features of DDT is its remote debugging feature. This
allows you to connect to a debugging session on RDHPCS systems from a client
running on your workstation. The local client provides much faster interaction
than you would have if you use the graphical client on RDHPCS systems. For
guidance in setting up the remote client see the :doc:`Debugging Software
</software/debuggers/index>` page.

GDB
====

`GDB <https://www.gnu.org/software/gdb/>`__, the GNU Project Debugger (GDB), is
a command-line debugger useful for traditional debugging and investigating code
crashes. GDB lets you debug programs written in Ada, C, C++, Objective-C,
Pascal (and many other languages).

GDB is available on Gaea under all compiler families:

.. code::

    module load gdb

To use GDB to debug your application run:

.. code::

    gdb ./path_to_executable

Additional information about GDB usage can be found in the `GDB Documentation
<https://www.sourceware.org/gdb/documentation/>`_.

GDB4HPC
=======

:command:`gdb4hpc` is a GDB-based parallel debugger, developed by HPE Cray. It
allows programmers to either launch an application or attach to an
already-running application that was launched with srun, to debug the parallel
code in command-line mode.

Information on GDB4HPC and other tools available in the `HPE Cray Programming
Environment`_ is `available
<https://cpe.ext.hpe.com/docs/latest/debugging-tools/index.html>`__, including
a `tutorial
<https://cpe.ext.hpe.com/docs/latest/debugging-tools/gdb4hpc/guides/tutorial.html>`__.

Valgrind4hpc
============

Valgrind4hpc is a Valgrind-based debugging tool to aid in the detection of
memory leaks and errors in parallel applications. Valgrind4hpc aggregates any
duplicate messages across ranks to help provide an understandable picture of
program behavior. Valgrind4hpc manages starting and redirecting output from
many copies of Valgrind, as well as deduplicating and filtering Valgrind
messages. If your program can be debugged with Valgrind, it can be debugged
with Valgrind4hpc.

Valgrind4hpc is available on Gaea under all compiler families:

.. code::

    module load valgrind4hpc

Additional information about Valgrind4hpc usage can be found in the `HPE Cray
Programming Environment User Guide
<https://support.hpe.com/hpesc/public/docDisplay?docId=a00115110en_us&page=Debug_Applications_With_valgrind4hpc_To_Find_Common_Errors.html>`__.


*********
Profiling
*********

HPE Performance Analysis Tools
==============================

.. _HPC Performance Analysis Tools: https://support.hpe.com/hpesc/public/docDisplay?docId=a00114942en_us&page=About_the_Performance_Analysis_Tools_User_Guide.html

.. cSpell:ignore Perftools

The `HPE Performance Analysis Tools` are a suite of utilities that enable users
to capture and analyze performance data generated during program execution.
These tools provide an integrated infrastructure for measurement, analysis, and
visualization of computation, communication, I/O, and memory utilization to
help users optimize programs for faster execution and more efficient computing
resource usage.

There are three programming interfaces available: (1) ``Perftools-lite``, (2)
``Perftools``, and (3) ``Perftools-preload``.

Below are two examples that generate an instrumented executable using
``Perftools``, which is an advanced interface that provides full-featured data
collection and analysis capability, including full traces with timeline
displays.

The first example generates an instrumented executable using a ``PrgEnv-amd``
build:

.. cSpell:ignore ggdb jobstep

.. code-block:: bash

    module load PrgEnv-amd
    module load perftools

    export CXXFLAGS='-ggdb -O3 -std=c++17 –Wall'
    export LD='CC'
    export LDFLAGS="${CXXFLAGS}

    make clean
    make

    pat_build -g io,mpi -w -f <executable>

The ``pat_build`` command in the above examples generates an instrumented
executable with ``+pat`` appended to the executable name (e.g.,
``hello_jobstep+pat``).

When run, the instrumented executable will trace HIP, I/O, MPI, and all user
functions and generate a folder of results (e.g.,
``hello_jobstep+pat+39545-2t``).

To analyze these results, use the ``pat_report`` command, e.g.:

.. code:: bash

    pat_report hello_jobstep+pat+39545-2t

The resulting report includes profiles of functions, profiles of maximum
function times, details on load imbalance, details on program energy and power
usages, details on memory high water mark, and more.

More detailed information on the HPE Performance Analysis Tools can be found in
the `HPE Performance Analysis Tools User Guide
<https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00123563en_us>`__.


***************
Tips and tricks
***************

GPFS (F5) Performance
=====================

The Gaea system intermittently has issues with the GPFS F5 performance.  This
typically appears as file operations hangs in interactive sessions, and as jobs
taking longer than normal to complete, or time out, as any jobs on Gaea
currently experience longer than normal run times.  While we do not yet have an
underlying cause for this, we have found certain changes to the user's
interactions and workflows that use the GPFS F5 file system help alleviate the
problem.

Files accesses by multiple jobs
-------------------------------

Users should not have multiple batch jobs access the same files.  This is
typically done using hard- or soft-links.  Accessing the same file from
multiple batch jobs increases the load on the metadata servers (MDS), and can
lead to a MDS locking up that affecting all files served on that MDS.

Users should clean up files after the job runs successfully to ensure the file
system has enough free space for all user's jobs.

Software Environments
---------------------

Users should not store software environments, for example Conda, Python, and
Spack, on the GPFS file system.  These environments have many small files that
will be accessed from multiple compute nodes when used in batch jobs.

These environments should be stored in user's or project's home space,
:file:`/ncrc/home[12]/$USER` and :file:`/ncrc/proj/<project>` respectively.  If
the environment is to be shared by several users or groups, the environment can
in the :file:`/usw`.  Please open a :ref:`help desk request <getting_help>` to
establish a location under :file:`/usw`.

Development
-----------

GPFS F5 should not be used for development.  Development should be done in the
user's home space.  This is especially true if using a source code management
system (e.g., git).

Users should remember that GPFS F5 is not backed up. The user home area is
backed up, with hourly and daily snapshots.

************
Known issues
************

The following is a list of issues we are currently investigating on the Gaea
system.  Please contact the :ref:`RDHPCS support team <getting_help>` for new
updates.

Open issues
===========

GPFS file system performance
----------------------------

We are investigating several GPFS (F5 and F6) performance issues.  We have
discovered that some slow read performance is likely tied to the GPFS file
compression.  We are working with ORNL and IBM to gather more information and
for a resolution.

Data transfer performance
-------------------------

We are investigating an issue with transfers from Gaea to the GFDL archive
system.  This affects large transfers (files larger than 2TB), and the overall
transfer performance.  At this time, we believe transfers initiated using the
:ref:`Globus transfer app <globus>` are not affected.  We suggest users
transferring large files to use Globus until a resolution is discovered.
