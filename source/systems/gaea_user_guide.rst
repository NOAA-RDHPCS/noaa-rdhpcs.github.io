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
C6.  Two high-capacity parallel filesystems provide over 150 petabytes of fast
access storage. The center-wide filesystem is connected using FDR InfiniBand to
the center's compute and data-transfer resources. The aggregate Gaea system
contains a peak calculating capability greater than 20 petaflops (quadrillion
floating point operations per second).

NOAA research partners access data remotely through speedy
interconnections. Two 10-gigabit (billion bit) lambdas, or optical
waves, pass data to NOAA's national research network through peering
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
enabling scientists to:

* understand the relationship between

  * climate change and extreme weather such as hurricanes
  * the atmosphere's chemical makeup and climate

* help unlock the climate role played by the oceans that cover nearly
  three-quarters of the globe.


.. _gaea-node-types:

Node types
==========

Gaea has three node types: :term:`login <login node>` or front-end,
:term:`compute <compute node>`, :term:`data transfer <data transfer node>`
nodes (:abbr:`DTN (data transfer node)`).  The three node types are similar in
terms of hardware, but differ in their intended use.

+---------+----------------------------------------------------------------+
| Node    |                                                                |
| Type    | Description                                                    |
+=========+================================================================+
| Login   | This is where you are placed when connecting to Gaea. This is  |
|         | the place to write, edit, and compile your code, manage data   |
|         | submit jobs, etc. You should not launch parallel or threaded   |
|         | jobs from a login node. Login nodes are shared resources.      |
+---------+----------------------------------------------------------------+
| Compute | Most of the nodes on Gaea are compute nodes. These are where   |
|         | your parallel and threaded jobs execute via the                |
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
    per core). C5 supports up to the AVX-2 :abbr:`ISA (Insturction Set
    Architechture)`.

    .. figure:: /images/C5-ComputeNodeDiagram.png

      Each C5 compute nodes has a total of 128 cores, in eight NUMA domains
      per node.  Each group of four cores share an 16 MB L3 cache.  Each CPU
      has eight lanes to the shared 256 GiB of node memory.

  .. tab-item:: C6
    :sync: C6

    The C6 compute nodes consiste of [2x] 96 core AMD EPYC Zen 4 CPUs, with two
    hardware threads per physical core and 384 GiB of physical memory (2 GiB
    per core). C6 support up to the AVX-512 :abbr:`ISA (Insturction Set
    Architechture)`.

    .. figure:: /images/C6-ComputeNodeDiagram.png

      Each C6 compute node has a total of 192 cores, in eight NUMA domains per
      node.  Each group of six cores share a 48 MB L3 cache.  Each CPU has 12
      lanes to the shared 384 GiB of physical memory (2 GiB per core).


.. _gaea-login-nodes:

Login nodes
===========

The Gaea login nodes have a similar architecture to the compute nodes.  Each
compute cluster, C5 and C6, have a dedicated set of login nodes.

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

The data transfer nodes (DTN) is where extensive I/O operations, large local,
and all off-gaea transfers should be done.  The :abbr:`DTN (Data Transfer
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

Each Gaea compute cluster, C5 and C6, have their own file system.  C5 has
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

.. seealso::

    `HPE Cray EX Documentation <https://support.hpe.com/connect/s/product?language=en_US&kmpmoid=1013083813>`_
        Documentation specific for the HPE Cray EX 3000 compute system.

**********
Connecting
**********

To connect to Gaea, :command:`ssh` to ``gaea-rsa.rdhpcs.noaa.gov``.  For
example,

.. code-block:: shell

    $ ssh <First.Last>@gaea-rsa.rdhpcs.noaa.gov

For more information on connecting through the Boulder or Princeton bastion,
with a :abbr:`CAC (Common Access Card)`, or for your first connection, see
:ref:`logging_in`.

By default, the bastion will automatically place a user on a random Gaea C5
login node.  If you need to access a specific login node ro C6, when prompted
enter :kbd:`Ctrl-C` and type the name of a login node or ``gaea6`` for a random
C6 login node:

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

NFS filesystems
===============

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


GPFS filesystems
================

Each compute cluster, C5 and C6, have their own file system called F5 and F6
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

The suggested way to move data to and from Gaea is to use `Globus Online
<app.globus.org>`_.  Please review the additional information in
:ref:`globus_online_data_transfer` and :ref:`globus_example`.

Please review :ref:`transferring-data` for information on other transfer
methods available.

***********************
Programming environment
***********************

Gaea users are provided with many pre-installed software packages and
scientific libraries. To facilitate this, environment management tools are used
to handle necessary changes to the shell.

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
|                                | ``<modulename>`` modulefile                |
+--------------------------------+--------------------------------------------+
| ``module spider <string>``     | Searches all possible modules according to |
|                                | <string>                                   |
+--------------------------------+--------------------------------------------+
| ``module load <modulename>     | Loads the given ``<modulename>``\ (s) into |
| [...]``                        | the current environment                    |
+--------------------------------+--------------------------------------------+
| ``module use <path>``          | Adds ``<path>`` to the modulefile search   |
|                                | cache and ``MODULESPATH``                  |
+--------------------------------+--------------------------------------------+
| ``module unuse <path>``        | Removes ``<path>`` from the modulefile     |
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
see the following :ref:`gaea-compiling` section for more detailed inforation on
how to compile using these modules.

Cray programming environment and compiler wrappers
--------------------------------------------------

Cray provides ``PrgEnv-<compiler>`` modules (for example, ``PrgEnv-cray``) that
load compatible components of a specific compiler toolchain. The components
include the specified compiler as well as MPI, LibSci, and other libraries.
Loading the ``PrgEnv-<compiler>`` modules also defines a set of compiler
wrappers for that compiler toolchain that automatically add include paths and
link in libraries for Cray software. Compiler wrappers are provided for C
(:command:`cc`), C++ (:command:`CC`), and Fortran (:command:`ftn`).

.. note::

    Use the ``-craype-verbose`` flag to display the full include and link
    information used by the Cray compiler wrappers. This must be called on a
    file to see the full output (for example, ``CC -craype-verbose test.cpp``).

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
There is also a system/OS versions of GCC available in :file:`/usr/bin`. The
table below lists details about each of the module-provided compilers.

.. important::

    It is highly recommended to use the Cray compiler wrappers (:command:`cc`,
    :command:`CC`, and :command:`ftn`) whenever possible. See the next section
    for more details.

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

    Use the ``-craype-verbose`` flag to display the full include and link
    information used by the Cray compiler wrappers. This must be called on a
    file to see the full output (for example, ``CC -craype-verbose test.cpp``).

.. _gaea-running:

************
Running jobs
************

Computational work on Gaea is performed by *jobs*. Jobs typically consist of
several componenets:

-  A batch submission script
-  A binary executable
-  A set of input files for the executable
-  A set of output files created by the executable

In general, the process for running a job is to:

#. Prepare executables and input files.
#. Write a batch script.
#. Submit the batch script to the batch scheduler.
#. Optionally monitor the job before and during execution.

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

Gaea uses `SchedMD <https://www.schedmd.com/>`_\ 's Slurm Workload Manager for
scheduling and managing jobs. A few items related to Slurm are below.  See our
:ref:`rdhpcs_slurm` documentation for more information.  You may also want to
use the `Slurm documentation <https://slurm.schedmd.com/documentation.html>`_.

Slurm documentation is also available for each command via the :command:`man`
utility, and on the web at `<https://slurm.schedmd.com/man_index.html>`__.


Batch Scripts
-------------

The most common way to interact with the batch system is via batch scripts. A
batch script is simply a shell script with added directives to request various
resoruces from or provide certain information to the scheduling system.  Aside
from these directives, the batch script is simply the series of commands needed
to set up and run your job.

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
|    3 | OLCF project to charge                                               |
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

Since all compute resources are managed and scheduled by Slurm, it is not
possible to simply log into the system and immediately begin running parallel
codes interactively. Rather, you must request the appropriate resources from
Slurm and, if necessary, wait for them to become available. This is done
through an "interactive batch" job. Interactive batch jobs are submitted with
the :command:`salloc` command. Resources are requested via the same options
that are passed via ``#SBATCH`` in a regular batch script (but without the
``#SBATCH`` prefix). For example, to request an interactive batch job with the
same resources that the batch script above requests, you would use ``salloc -A
ABC123 -J RunSim123 -t 1:00:00 -p batch -N 1024``. Note there is no option for
an output file...you are running interactively, so standard output and standard
error will be displayed to the terminal.

.. warning::

    Indicating your shell in your :command:`salloc` command is NOT recommended
    (for example, ``salloc ... /bin/bash``). Doing so causes your compute job
    to start on a login node by default rather than automatically moving you to
    a compute node.

.. _common-slurm-options:

Common Slurm Options
--------------------

The table below summarizes options for submitted jobs. Unless otherwise noted, they can be used for either batch scripts or interactive batch jobs. For scripts, they can be added on the ``sbatch`` command line or as a ``#BSUB`` directive in the batch script. (If they're specified in both places, the command line takes precedence.) This is only a subset of all available options. Check the `Slurm Man Pages <https://slurm.schedmd.com/man_index.html>`__ for a more complete list.

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
    |                        |                                  | hours:minuts:seconds, days-hours,         |
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
    | ``-C``                 | ``#SBATCH -C nvme``              | Request the burst buffer/NVMe on each     |
    |                        |                                  | node be made available for your job. See  |
    |                        |                                  | the Burst Buffers section for more        |
    |                        |                                  | information on using them.                |
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
you to have everything self-contained within the job submission script (rather
than having to remember what options you set for a given job).

Slurm also provides a number of environment variables within your running job.
The following table summarizes those that may be particularly useful within
your job (e.g. for naming output log files):

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
| ``$SLURM_JOBID``         | The job’s full identifier. A common use for      |
|                          | ``$SLURM_JOBID`` is to append the job’s ID       |
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
| ReqNodeNotAvail   | The requested a particular node, but it's currently     |
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

Slurm on Gaea uses the `priority/multifactor plugin
<https://slurm.schedmd.com/priority_multifactor.html>`_ to calculate a job's
priority.  The factors used are:

Age
    the length of time ajob has been waiting in the queue, elgible to be
    scheduled

Fair-share
    the difference between the portion of the computing resource that has been
    promised (allocation) and the amount of resources that has been consumed.
    Gaea uses the `classic fairshare algorithm
    <https://slurm.schedmd.com/classic_fair_share.html>`_


:abbr:`QOS (Quality of Service)`
    a factor associated with each Quality Of Service (QOS)

.. note::

    Only the compute clusters' QOSes will affect a job's priority value.  ES
    cluster QOSes (the login nodes and the DTNs) QOSes specific to the login
    nodes and DTNs do not affect the job's prioities.


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
| urgent   | 0.95     | 1.00   | 16 hours | QOS to allow groups to prioitize  |
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
    *debug* QOS.  However, users can only have a single *interative* job at any
    time.

.. note::

    The priority and usage factors for all QOSes can be found using the command
    :command:`sacctmgr show qos format=name,priority,usagefactor,maxwall`.

    The command :command:`sprio` can be used to see the current priority, and
    the age, fair-share, and qos factors for a specific jobs.

    The command :command:`sshare` will show the current shares (allocation),
    usage, and fair-share factors for all projects (allocations).

Partitions

C6 "batch" max nodes 512 "novel" all jobs over 512 nodes.  Only enabled after
maintenance.  Please contact the HD if you need to run large jobs, so we can
ensure the partition is enabled.


Job Dependencies
----------------

Oftentimes, a job will need data from some other job in the queue, but it's
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


Monitoring and Modifying Batch Jobs
-----------------------------------

``scontrol hold`` and ``scontrol release``: Holding and Releasing Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you may need to place a hold on a job to keep it from starting. For
example, you may have submitted it assuming some needed data was in place but
later realized that data is not yet available. This can be done with the
``scontrol hold`` command. Later, when the data is ready, you can release the
job (i.e. tell the system that it's now OK to run the job) with the ``scontrol
release`` command. For example:

+----------------------------+------------------------------------------------+
| ``scontrol hold 12345``    | Place job 12345 on hold                        |
+----------------------------+------------------------------------------------+
| ``scontrol release 12345`` | Release job 12345 (i.e. tell the system it's   |
|                            | OK to run it)                                  |
+----------------------------+------------------------------------------------+


``scontrol update``: Changing Job Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


``scancel``: Cancel or Signal a Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the ``--signal`` option for the ``sbatch``/``salloc`` commands
described :ref:`above <common-slurm-options>`, the ``scancel`` command can be
used to manually signal a job. Typically, this is used to remove a job from the
queue. In this use case, you do not need to specify a signal and can simply
provide the jobid (i.e. ``scancel 12345``). If you want to send some other
signal to the job, use ``scancel`` the with the ``-s`` option. The ``-s``
option allows signals to be specified either by number or by name. Thus, if you
want to send ``SIGUSR1`` to a job, you would use ``scancel -s 10 12345`` or
``scancel -s USR1 12345``.


``squeue``: View the Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``squeue`` command is used to show the batch queue. You can filter the
level of detail through several command-line options. For example:

+--------------------------+------------------------------------------------+
| ``squeue -l``            | Show all jobs currently in the queue           |
+--------------------------+------------------------------------------------+
| ``squeue -l -u $USER``   | Show all of *your* jobs currently in the queue |
+--------------------------+------------------------------------------------+


``sacct``: Get Job Accounting Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

``scontrol show job``: Get Detailed Job Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to holding, releasing, and updating the job, the ``scontrol``
command can show detailed job information via the ``show job`` subcommand. For
example, ``scontrol show job 12345``.


.. _frontier-srun:

Srun
----------------------

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
    |                                                | Currently, the distribution setting for    |
    |                                                | cores (the third "<value>" entry) has no   |
    |                                                | effect on Frontier                         |
    +------------------------------------------------+--------------------------------------------+
    |  ``--ntasks-per-node=<ntasks>``                | If used without ``-n``: requests that a    |
    |                                                | specific number of tasks be invoked on     |
    |                                                | each node.                                 |
    |                                                | If used with ``-n``: treated as a          |
    |                                                | *maximum* count of tasks per node.         |
    +------------------------------------------------+--------------------------------------------+








***************
GAEA Quickstart
***************

This simple overview explains the elements of a basic job in Gaea. It
includes compiling, running, combining, data transfer, and allocation.

.. Note::

  Ensure that you have done your first login to Gaea and generated a
  certificate.

Connecting and General Info
----------------------------

There are two ways to access Gaea. The oldest is to use PuTTY or ssh
to gaea-rsa.rdhpcs.noaa.gov and authenticate using your RDHPCS-issued
RSA token. Alternatively, use Tectia sshg3 to gaea.rdhpcs.noaa.gov and
authenticate with your CAC and CAC PIN. The :ref:'login' section
describes this in detail, with additional useful information like how
to set up port tunnels to Gaea (needed to use X-windows applications
like DDT.) You can also use the RDHPCS login documentation at
:ref:`Logging_in`, but in that case you will want to know that the
port tunnel ranges for Gaea are 20000 + your UID number for
LocalForward and 30000 + your UID number for RemoteForward (in ssh
config file language.)

- If you want more information on using your CAC to authenticate to
  RDHPCS systems, see **CAC_Login**.
- If you want more information on configuring PuTTY, see
  **Configuring_PuTTY**.

Gaea uses modules software to let users change which software is
accessible to their environment. There is no module man page. Instead
use the command:

.. code-block:: shell

  module help

Gaea uses Slurm as its batch scheduler.

Compiling
---------

Gaea offers PrgEnv-intel, Prg-Env-aocc, Prg-Env-nvhpc, and several
other modules that make it as easy as possible to get your programs
running. To compile, call either cc or ftn, according to the language
your code is written in. See **Compilers** for more detail, especially
for compiling multithreaded applications.

You may compile live in your login shell on a Gaea login node, or in a
job in the eslogin queue in the es partition of Gaea's batch system.
To tell a job script to run on the login nodes, specify the following
in your script:

.. code-block:: shell

  #SBATCH --clusters=es
  #SBATCH --partition=eslogin_c#
  #SBATCH --ntasks=1

or, from the sbatch command line:

.. code-block:: shell

  sbatch --clusters=es --partition=eslogin_c# --ntasks=1 /path/to/compile_script

.. note::

  c# refers to a computer cluster.

Running
-------

Once your executable is compiled and in place with your data on a
given file system (f5 for example), you are ready to submit your
compute job. Submit your job to c#

.. note::

  c# refers to a computer cluster. The current clusters are c5 and c6,
  but this is subject to change.

.. code-block:: shell

  #SBATCH --clusters=c#
  #SBATCH --nodes=4
  #SBATCH --ntasks-per-node=32 # Gaea charges for node use.  Nodes are 128 core on c5.  This example will get charged for 4 nodes.

or, from the sbatch command line:

.. code-block:: shell

  sbatch --clusters=c# --nodes=4 --ntasks-per-node=128 /path/to/run_script

Your compute job script will run on one of the compute nodes allocated
to your job. To run your executable on them use the srun or srun-multi
command. A simple example is shown here:

.. code-block:: shell

  cd /gpfs/f5/<project>/scratch/$USER
  srun --nodes=128 --ntasks-per-node=32
  /gpfs/f5/<project>/$USER/path/to/executable


Staging/Combining
-----------------

Staging data to and from model run directories is a common task on
Gaea. So is combining model output when your model uses multiple
output writers for scalability of your MPI communications. The Local
Data Transfer Nodes (LDTNs) are the resource provided for these tasks.
Please keep these tasks off the compute nodes and eslogin nodes. There
is a NOAA-developed tool called **gcp** which is available for data
transfers on Gaea.

To tell a job script to run on the LDTN nodes, specify the following
in your script:

.. code-block:: shell

  #SBATCH --clusters=es
  #SBATCH --partition=ldtn_c#
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1 #set ntasks-per-node to the number of cores your job will need, up to 16

or, from the sbatch command line:

.. code-block:: shell

  sbatch --clusters=es --partition=ldtn_c# --nodes=1 --ntasks-per-node=1 /path/to/staging_script

The data transfer nodes are assigned to a site specific partition on
the **es cluster**. Use the following command to view current and/or
available partitions:

 .. code-block:: shell

     $ scontrol show partitions

     or

  .. code-block:: shell

     $ scontrol show partitions | grep dtn



Transferring Data to/from Gaea
------------------------------

Data transfers between Gaea and the world outside of Gaea should be
performed on the Remote Data Transfer Nodes (RDTNs). There is a
NOAA-developed tool called **gcp**, which is available for data
transfers on Gaea. HPSS users are only able to access HPSS from jobs
on the RDTNs. To tell a job script to run on the login nodes, specify
the following in your script:

.. code-block:: shell

  #SBATCH --clusters=es
  #SBATCH --partition=rdtn_c#
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1 #set ntasks-per-node to the number of cores your job will need, up to 8

or, from the sbatch command line:

.. code-block:: shell

  sbatch --clusters=es --partition=rdtn --nodes=1 --ntasks-per-node=1 /path/to/trasfer_script

.. note::

  The data transfer nodes are assigned to a site specific partition on
  the es cluster.

  Use the following command to view current and, or available
  partitions:

  .. code-block:: shell

    $ scontrol show partitions

  or

  .. code-block:: shell

    $ scontrol show partitions | grep dtn

Allocation
----------

Gaea users have default projects. If you are only a member of a single
project, or if your experiments always run under your default project,
you don't need to do anything special to run. Users who are members of
more than one project need to enter their preferred project via the
--account option to sbatch to correctly charge to each experiment's
project.

You can use AIM to request access to new projects. Once access is
granted in AIM, it can take up to two days to be reflected in Gaea's
Slurm scheduler. If you still don't have the granted access after two
days, please submit a help desk ticket so administrators can
investigate your issue.

To determine your Slurm account memberships, run the following
command:

.. code-block:: shell

  sacctmgr list associations user=First.Last

To submit jobs to the scheduler under a specific account enter the
following from the sbatch command line:

.. code-block:: shell

  sbatch --account=gfdl_z

or add the following to your job script's #SBATCH headers:

.. code-block:: shell

  #SBATCH --account=gfdl_z

Running a Simple Job Script
---------------------------

This script assumes that the data and executable are staged to
/gpfs/f5/<project>/scratch/$USER. The scripts and data are located at
/usw/user_scripts/.

1. Use gcp to get the skeleton script from /usw/user_scripts/runscript
   to your local home directory.

.. code-block:: shell

  gcp /usw/user_scripts/runscript ~$USER/

2. Use gcp to get other files from /usw/user_scripts/ to your gpfs directory.

.. code-block:: shell

  gcp -r /usw/user_scripts/ /gpfs/f5/<project>/scratch/$USER/runscript

3. Open the runscript.

.. code-block:: shell

  vim ~$/gpfs/f5/<project>/scratch/$USER/runscript

The comments in the script will help you understand what each item does.

4. Return to the directory where you copied the run script, and submit
   your job.

.. code-block:: shell

  sbatch /gpfs/f5/<project>/scratch/$USER/runscript

Make sure that the sbatch directives (--account, --walltime) have been
changed.

**Once the job is submitted**, you can use the following commands to
check on your job.

- To view job status:

.. code-block:: shell

  squeue -u $USER

- For a detailed status check, use the scontrol commnand, and replace
  "jobid" with your job's id.

.. code-block:: shell

  scontrol show job <jobid>

For example:

.. code-block:: shell

  scontrol show job 123456789

Once the job is finished, it should produce an output file.

System Architechture
====================

Gaea is the largest of the NOAA research and development HPC systems,
and is operated by DOE/ORNL.


.. figure:: /images/GaeaC5.png

The aggregate Gaea system:

- consists of 245,760 AMD cores;
- contains 646 TiB of memory
- can perform 13.7 petaflops, or 13,700 trillion calculation each
  second.

Node Types
----------

- **Compute Nodes (C5):** 128 cores, HPE EX Rome, 251GB memory, run
  model executable, filesystem mount - F5
- **Batch Nodes:** 2 cores, 8GB memory, run scripts only (cores are
  not charged)

.. Note::

  Batch Nodes are not very powerful. Do not write code/jobs that will use Batch nodes to do CPU intensive work

- **ESLogin Nodes:**  32 cores, 512GB memory, run interactive
  sessions, Matlab, compiles
- **LDTN Nodes:** 16 cores, 24GB memory, I/O intensive jobs (combines,
  etc.)
- **RDTN Nodes:** 8 cores, 48GB memory, Data transfer jobs

Clusters
--------
- **C5** Gaea compute partition. Please see "System Architecture" and
  "Hardware" for details.
- **es** login nodes, local data transfer node queue (ldtn) and remote
  data transfer node queue (rdtn)


Examples:

.. code-block:: shell

  sbatch --clusters=c5 scriptname
  #SBATCH --clusters=c5

.. code-block:: shell

  sbatch --clusters=es scriptname
  #SBATCH --clusters=es


What is C5?
-----------

C5 is an HPE Cray EX with 482 terabytes of memory and a peak
calculating capacity of 10.2 petaflops. There are an additional 8
login nodes with 128 cores and 503GB of memory each. The total cores
for c5 and its login nodes are 245,760.

**Accessing the C5 login nodes**

C5 is available from all Gaea login nodes. To access these login
nodes, ssh or sshg3 (Tectia CAC card authenticated SSH) to the Gaea
bastion of your choice (sshg3 gaea.rdhpcs.noaa.gov, ssh
gaea-rsa.princeton.rdhpcs.noaa.gov, sshg3
gaea.boulder.rdhpcs.noaa.gov, or ssh
gaea-rsa.boulder.rdhpcs.noaa.gov). If you want a specific Gaea login
node, wait for the list of nodes and press 'ctrl'+'c', then enter the
name of the login node you would like to use and press return. Your
ssh session will be forwarded to that gaea login node.

You can use C5 in batch or software mode.

**Batch System**

From gaea9-15 you caninteract with c5's Slurm cluster. See Slurm Tips
for details.

Your C5 job scripts will usually call srun or srun-multi if you have a
multi-executable model e.g. a coupled model with different ocean and
atmospheric model executables.

**C5 Known Issues**

- Known Module Incompatibility on C5

There is a known incompatibility with the cray-libsci module and the
following intel modules:

.. code-block:: shell

  intel-classic/2022.0.2
  intel-oneapi/2022.0.2

A recommended workaround to this issue is to either module unload
cray-libsci or use another intel compiler.

**Site Specific Documentation for C5**

See the C5 On-boarding Guide.

.. code-block:: shell

  C5 cpuinfo and memory
  processor	: 208
  vendor_id	: AuthenticAMD
  cpu family	: 23
  model		: 49
  model name	: AMD EPYC 7662 64-Core Processor
  stepping	: 0
  microcode	: 0x830107a
  cpu MHz		: 2000.000
  cache size	: 512 KB
  physical id	: 1
  siblings	: 128
  core id		: 16
  cpu cores	: 64
  apicid		: 161
  initial apicid	: 161
  fpu		: yes
  fpu_exception	: yes
  cpuid level	: 16
  wp		: yes
  flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca
  bugs		: sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass retbleed smt_rsb
  bogomips	: 3985.40
  TLB size	: 3072 4K pages
  clflush size	: 64
  cache_alignment	: 64
  address sizes	: 48 bits physical, 48 bits virtual
  power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

Job Submission
---------------
There are two job types:

- Batch
  -Regular jobs - use sbatch

- Interactive/Debug
  -salloc --x11 --clusters=c# --nodes=2 --ntasks-per-node=32

Queues
------
There are four different queues.

- batch - no specification needed
- eslogin - compiles and data processing jobs
- ldtn - data movement queue (local)
- rdtn - data movement (remote)

Examples:

.. code-block:: shell

  sbatch --clusters=es --partition=eslogin_c# scriptname
  sbatch --clusters=es --partition=ldtn_c# scriptname

Job Monitoring
--------------

The following are job monitoring commands with examples:

- squeue: displays the queues. All jobs are commingled.

.. code-block:: shell

  squeue -u $USER

- scontrol show job: provides job information.

.. code-block:: shell

  scontrol show job <jobid>

- sinfo: system state information

.. code-block:: shell

  sinfo

- scontrol: control holds on jobs

.. code-block:: shell

  scontrol hold jobid
  scontrol release jobid

- scancel: cancel jobs

.. code-block:: shell

  scancel jobid

Terminology
-----------

+---------------+---------------------------------------------------+
| **Slurm**     | The scheduler for all new NOAA research and       |
|               | development systems.                              |
+---------------+---------------------------------------------------+
| **Cluster**   | A section of Gaea that has its own scheduler. It  |
|               | is a logical unit in Slurm.                       |
+---------------+---------------------------------------------------+
| **Partition** | A group of nodes with a specific purpose. It is a |
|               | logical unit in Slurm.                            |
+---------------+---------------------------------------------------+
| **DTN**       | Data transfer node                                |
+---------------+---------------------------------------------------+
| **CMRS**      | Climate Modeling and Research System; an          |
|               | alternate name for Gaea.                          |
+---------------+---------------------------------------------------+


Environment
------------

Gaea is implemented to use the Environment Modules system. This tool
helps users manage their Unix or Linux shell environment. It allows
groups of related environment-variable settings to be made or removed
dynamically. Modules provides commands to dynamically load, remove and
view software.

More information on using modules is available at Gaea Modules.

Do's and Don'ts
---------------

**Do**

- Compile on login nodes
- Put transient data in /gpfs/f5/<project>/scratch/$USER
- Copy data back to archive location (off gaea) using RDTN's
- Use gcp for transfers

**Don't** use the following on Gaea:

- combines on compute nodes
- combines on batch (they will be killed)
- compile on batch
- cp
- cron jobs (not permitted)
- deep large scale use of "find" on the F5 filesystem (please use 'lfs
  find' instead)
- fs as permanent storage
- module purge
- recursive operations like ls -R
- run applications natively
- transfers on batch nodes
- unalias*

File Systems
============

Gaea has three filesystems: Home, F2 (a parallel file system based on
Lustre, **decommissioned**), and F5 (a General Parallel File System).

Summary of Storage Areas
------------------------

**NFS File System**

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Area
     - Path
     - Type
     - Permissions
     - Quota
     - Backedup
   * - User Home
     - ``/ncrc/home[12]/$USER``
     - NFS
     - User Set
     - 50 GB
     - Yes
   * - Project Home
     - ``/ncrc/proj/<project>``
     - NFS
     - Project Set
     - N/A
     - Yes


**GPFS (F5)**

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Area
     - Path
     - Type
     - Permissions
     - Quota
     - Backedup
     - Purged
   * - Member Work
     - ``/gpfs/f5/<project>/$USER``
     - GPFS
     - User Set
     - Project-Based
     - No
     - No
   * - Project Work
     - ``/gpfs/f5/<project>/proj-shared``
     - GPFS
     - 750
     - Project-Based
     - No
     - No
   * - World Work
     - ``/gpfs/f5/<project>/world-shared``
     - GPFS
     - 755
     - Project-Based
     - No
     - No


HOME
----

The home filesystem is split into two sections both of which are
backed up. For load balance purposes, there is a home1 and home2.
Note:

.. note::

  Each user has a 50 GB limit.

Home is mounted on:

- Batch nodes
- LDTN
- RDTN
- Login nodes

A snapshot can be accessed at

.. code-block:: shell

  /ncrc/home1|2/.snapshot/{daily or hourly}/$USER

You can use this path to restore files or subdirectories. The
permissions will be the same as the originals and users can simply
copy from that location to any destination.

**General Parallel File System**

F5 is a 50 PB General Parallel File System. F5 will not be swept. Any
project jobs will be blocked if the project is significantly over
quota.

F5 will be mounted on:

- Login nodes (gaea51-gaea58)
- Compute nodes
- LDTN
- RDTN

**Directory Hierarchy**

.. code-block:: shell

  /gpfs/f5/<project>/scratch/$USER
  /gpfs/f5/<project>/proj-shared
  /gpfs/f5/<project>/world-shared

Where <project> is the Slurm project

Example:

.. code-block:: shell

  /gpfs/f5/epic
  /gpfs/f5/gfdl_sd


Allocations and Quotas
======================

CPU allocations on Gaea are defined by the allocation board, with
allocations allotted among different groups and systems. Each of these
currently has a portion of time allocated. Dual running is done within
the standard allocations under a QOS (Quality of Service) tag of
"dual." Windfall is a catch-all quality of service account for users
who have exhausted their groups monthly CPU allocation, or who wish to
run without charging to their groups CPU allocation and forfeit job
priority factors.

SLURM is a Resource Manager and Scheduler. For Gaea-specific SLURM
information, see SLURM Tips. For a general introduction to SLURM, see
SLURM.


Modules
=======

The Environment Modules system is a tool to help users manage their
Unix or Linux shell environment, by allowing groups of related
environment-variable settings to be made or removed dynamically.
Modules provides commands to dynamically load, remove and view
software.

LMOD
----

LMOD is the modules software management system used on C5 and the C5
login nodes. Unlike the module system on C3/C4, LMOD employs a
hierarchical system that, when used properly, considers dependencies
and prerequisites for a given software package. For example, the
cray-netcdf module depends on the cray-hdf5 module and cannot be seen
by the standard module avail commands, nor can it be loaded until the
cray-hdf5 module is loaded.

The LMOD hierarchical system will automatically deactivate or swap an
upstream module dependency. Two examples are given below.

Another feature of LMOD is swapping or unloading an upstream
dependency. In these cases, any downstream module will still be loaded
but inactivated.

.. code-block:: shell

  $> module load cray-hdf5
  $> module load cray-netcdf
  $> module unload cray-hdf5

LMOD Search Commands
--------------------

To find a specific module, use module spider. This command will show
all modules and versions with the specified name. This includes
modules that cannot be loaded in the current environment.

.. code-block:: shell

  $> module spider <module>

.. code-block:: shell

 module avail

will show only modules that can be loaded in the current environment.

Adding Additional Module Paths
------------------------------

Do not manually set the MODULESPATH environment variable. Manually
setting the MODULESPATH environment variable will produce unknown
behavior. Instead, use module use <path> or module use -a <path> to
add more module paths.

Module Commands
---------------
Module Command line variables and descriptions

**module help [module]:** Print the usage of each sub-command. If an
argument is given, print the Module-specific help information for the
module file(s)

.. code-block:: shell

  > module help gcp

  ----------- Module Specific Help for 'gcp/2.2' --------------------

  Sets up the shell environment for gcp


**module avail:** List all available modulefiles in the current
MODULEPATH.

.. code-block:: shell

  ------------------------------------------ /opt/cray/ss/modulefiles ---------------------------------------
  portals/2.2.0-1.0301.22039.18.1.ss(default) rca/1.0.0-2.0301.21810.11.20.ss(default)
  ------------------------------------------ /opt/cray/xt-asyncpe/default/modulefiles -----------------------
  xtpe-accel-nvidia20  xtpe-barcelona       xtpe-istanbul        xtpe-mc12            xtpe-mc8             xtpe-network-gemini
  xtpe-network-seastar xtpe-shanghai        xtpe-target-native
  ------------------------------------------ /opt/cray/modulefiles ------------------------------------------
  atp/1.0.2(default)                   perftools/5.1.0(default)             portals/2.2.0-1.0300.20621.14.2.ss   trilinos/10.2.0(default)
  atp/1.1.1                            perftools/5.1.2                      rca/1.0.0-2.0300.20198.8.26.ss       trilinos/10.6.2.0
  ga/4.3.3(default)                    pmi/1.0-1.0000.7628.10.2.ss          rca/3.0.20                           xt-mpich2/5.0.1(default)
  gdb/7.2(default)                     pmi/1.0-1.0000.7901.22.1.ss(default) stat/1.0.0(default)                  xt-mpich2/5.2.0
  iobuf/2.0.1(default)                 pmi/1.0-1.0000.8256.50.1.ss          stat/1.1.3                           xt-mpt/5.0.1(default)
  xt-mpt/5.2.0                         xt-shmem/5.0.1(default               xt-shmem/5.2.0

.. note::

  Your shell might print out something more, or something different.

**module add module_file:** Load module file(s) into the shell
environment

**module load module_file:** Load module file(s) into the shell
environment

.. code-block:: shell

  > module load gcp/1.1


**module list:** List of Loaded modules.

.. code-block:: shell

  > module list
  1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
  2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
  3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
  4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
  5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
  6)  TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.4.3

  note gcp/1.4.3 is now Loaded at no.18

**module rm module_file:** unload the module

**module unload module_file:** unload the module

.. code-block:: shell

  > module unload gcp/1.4.3
  module list
  1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
  2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
  3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
  4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
  5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
  16) TimeZoneEDT                              17) CmrsEnv

  note gcp/1.4.3 is not Loaded


**module Switch [available_module] replacement_module:** Switch loaded
modulefile1 with modulefile2. If modulefile1 is not specified, then it
is assumed to be the currently loaded module with the same root name
as modulefile2

**module swap [available_module] replacement_module:** Switch loaded
modulefile1 with modulefile2. If modulefile1 is not specified, then it
is assumed to be the currently loaded module with the same root name
as modulefile2

.. code-block:: shell

  > module load gcp/1.1
  module list
  Currently Loaded Modulefiles:
  1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
  2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
  3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
  4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
  5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
  16) TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.1

  module swap gcp/1.1 gcp/1.5.0
  1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
  2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
  3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
  4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
  5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
  16) TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.5.0

  Note: the gcp is now version 1.5.0

**module show modulefile:** Display information about one or more
modulefiles. The display sub-command will list the full path of the
modulefile(s) and all (or most) of the environment changes the
modulefile(s) will make if loaded. (It will not display any
environment changes found within conditional statements.)

**module display modulefile** Display information about one or more
modulefiles. The display sub-command will list the full path of the
modulefile(s) and all (or most) of the environment changes the
modulefile(s) will make if loaded. (It will not display any
environment changes found within conditional statements.)

.. code-block:: shell

  > module show CmrsEnv
  -------------------------------------------------------------------
  /sw/eslogin/modulefiles/CmrsEnv:
  module-whatis    Sets up environment variables for the NCRC CMRS.
  setenv           CSCRATCH /lustre/fs/scratch
  setenv           CSTAGE /lustre/ltfs/stage
  setenv           CWORK /lustre/ltfs/scratch
  setenv           CHOME /ncrc/home1/John.Smith
  -------------------------------------------------------------------


**module use [-a]–append] directory:** Prepend one or more directories
to the MODULEPATH environment variable. The –append flag will append
the directory to MODULEPATH.

.. warning::

  Please DO NOT use the command module purge. This will remove all
  modules currently loaded by default in your environment and will
  lead to major errors. If you have accidentally used the command
  purge, log out of GAEA and log in. This will give you the default
  environment with the default modules loaded.

Compilers
=========

Compiling code on Cray machines is different from compiling code for
commodity or beowulf-style HPC linux clusters. Among the most
prominent differences:

- Cray provides a sophisticated set of compiler wrappers to ensure
  that the compile environment is setup correctly. Their use is highly
  encouraged.
- In general, linking/using shared object libraries on compute
  partitions is not supported.

Available Compilers
-------------------

The following compilers are available:

- NVHPC Compiler Suite (8.3.3)
- AOCC Compiler Suite (8.3.3)
- PGI, the Portland Group Compiler Suite (default) (12.5.0)
- GCC, the GNU Compiler Collection (4.7.0)
- The Cray Compiler Suite (8.1.3)
- The Intel Compiler Suite (12.1.3.293)

Compilers on C5
---------------

NVHPC replaces the PGI compiler. AOCC is the AMD Optimizing C/C++ and
Fortran Compiler. The following compilers and programming environments
are available on C5 as modules:

- PrgEnv-aocc/8.3.3 aocc/3.2.0
- PrgEnv-cray/8.3.3 cce/14.0.4
- PrgEnv-cray/8.3.3 cce/15.0.1
- PrgEnv-gnu/8.3.3 gcc/10.3.0
- PrgEnv-gnu/8.3.3 gcc/11.2.0
- PrgEnv-gnu/8.3.3 gcc/12.1.0
- PrgEnv-gnu/8.3.3 gcc/12.2.0
- PrgEnv-intel/8.3.3 intel-classic/2022.0.2
- PrgEnv-intel/8.3.3 intel-classic/2022.2.1
- PrgEnv-intel/8.3.3 intel-oneapi/2022.0.2
- PrgEnv-intel/8.3.3 intel-oneapi/2022.2.1
- PrgEnv-intel/8.3.3 intel/2022.0.2
- PrgEnv-intel/8.3.3 intel/2022.2.1
- PrgEnv-nvhpc/8.3.3 nvhpc/22.7

With Intel 2022 compilers on C5 users should replace the -xsse2
compiler option with one of the following:

- march=core-axv-i: Recommended for production. MSD uses this for
  regression testing. A limited number of MOM6-solo tests on t5 even
  bitwise produce c4 answers with this option. MSD has found no
  reproducibility issues with this option so far. This option is used
  for FRE targets prod and repro.
- march=core-avx2: Not Recommended at this time for production for
  GFDL climate models. It should only be used for exploratory testing
  with advanced AVX optimizations. There are known restart
  reproducibility issues with GFDL climate models potentially
  affecting multi-segment runs, but no repeatability issues have been
  seen so far for single-segment runs.

.. caution::

  When building a production executable, please review the compilation
  output to ensure that -march=core-avx-iis used.

**Intel Compilers (mixed compiler modules)**

LMOD uses hierarchical modules. This helps ensures that only one
module in a hierarchical level is loaded, and that modules depending
on a given hierarchy are loaded properly, thus reducing module
conflicts. The compiler modules are one of the hierarchical levels.
However, some compilers (e.g., the Intel compilers) rely on the GNU
Compiler Collection (GCC) compilers to know which C and Fortran
standards to support. HPE has included the <compiler>-mixed modules to
address this. These mixed modules will allow multiple compiler modules
to be loaded. This is typically not needed in GFDL workflows but is
available. MSD recommends loading the compiler module that does not
have -mixed on the end.

Cray Compiler Wrappers
----------------------

traditional compiler invocation commands. The wrappers call the
Cray provides a number of compiler wrappers that substitute for the
appropriate compiler, add the appropriate header files, and link
against the appropriate libraries based on the currently loaded
programming environment module. To build codes for the compute nodes,
you should invoke the Cray wrappers via:

- cc To use the C compiler
- CC To use the C++ compiler
- ftn To use the FORTRAN 90 compiler

PrgEnv-pgi is the default module when you login to Gaea.
These wrappers are provided by PrgEnv-[intel|gnu|pgi|cray] modules.

Compiling and Node Types
------------------------

Cray systems are comprised of different types of nodes:

- Login nodes running traditional Linux
- Batch nodes running traditional Linux
- Compute nodes running the Cray Node Linux (CNL) microkernel
  - Your code will run on these nodes.

.. warning::

  Always compile on the login nodes. Never compile on the batch nodes.

.. note::

  Gaea also has LDTN and RDTN nodes. These are for combining model
  output (LDTN) and data transfer (RDTN) only, not compiling. They are
  not Cray nodes.

**Compiling for Compute Node**

Cray compute nodes are the nodes that carry out the vast majority of
computations on the system. Compute nodes are running the CNL
microkernel, which is markedly different than the OS running on the
login and batch nodes. Your code will be built targeting the compute
nodes. All parallel codes should run on the compute nodes. Compute
nodes are accessible only by invoking aprun within a batch job. To
build codes for the compute nodes, you should use the Cray compiler
wrappers.

.. note::

  We highly recommend that the Cray-provided cc, CC, and ftn compiler
  wrappers be used when compiling and linking source code for use on
  the compute nodes.

**Support for Shared Object Libraries**

Cray systems support linking with both static and dynamic libraries.

The Cray compiler wrappers use an environment variable SOME_ENV_VAR to
determine how to link external libraries. The default link method for
the C3 and C4 clusters is static, while C5's default is dynamic.

.. note::

  Dynamic linking will create a smaller executable. However, the run
  environment configuration must be identical to the environment where
  the executable was built. Static binaries are larger, but do not
  require the build and runtime environments to be identical.

Within C5, the Cray Programming Environment (CrayPE) now defaults to
dynamically linked libraries. The executable will not include copies
of the associated libraries at link time but will look for the
libraries using the LD_LIBRARY_PATH variable, and load them when
executed. For this reason, batch scripts must load the appropriate
modules for a given executable. If not loaded, the executable will
issue an error similar to shell <executable> error while loading
shared libraries:

.. code-block:: shell

  cannot open shared object file: No such file or directory

**Do Not Compile on Batch Nodes**

When you log into a Cray system you are placed on a login node. When
you submit a job for execution on c1/c2, your job script is launched
on one of a small number of shared batch nodes. To run your
application, use the Cray utility aprun. aprun will run your
application on the compute nodes associated with your job. All tasks
not launched through aprun will run on a batch node. Users should note
that there are a small number of these login and batch nodes, and they
are shared by all users. Because of this, long-running or
memory-intensive work should not be performed on login nodes or batch
nodes.

.. warning::

  Long-running or memory-intensive codes should not be compiled for
  use on login nodes nor batch nodes.

.. warning::

  Always compile on the login nodes. Never compile on the batch
  nodes.

Controlling the Programming Environment
---------------------------------------

Message Passing Interface (MPI) libraries are added to each user's
Upon login, the default versions of the PGI compiler and associated
environment through a programming environment module. Users do not
need to make any environment changes to use the default version of PGI
and MPI.

**Changing Compilers**

If a different compiler is required, it is important to use the
correct environment for each compiler. To aid users in pairing the
correct compiler and environment, programming environment modules are
provided. The programming environment modules will load the correct
pairing of compiler version, message passing libraries, and other
items required to build and run. We highly recommend that the
programming environment modules be used when changing compiler
vendors. The following programming environment modules are available:

- PrgEnv-pgi
- PrgEnv-gnu
- PrgEnv-cray
- PrgEnv-intel

To change the default loaded PGI environment to the default version of
GNU use:

.. code-block:: shell

  $ module unload PrgEnv-pgi $ module load PrgEnv-gnu

**Changing Versions of the Same Compiler**

To use a specific compiler version, you must first ensure the
compiler's PrgEnv module is loaded, and then swap to the correct
compiler version. For example, the following will configure the
environment to use the GCC compilers, then load a non-default GCC
compiler version:

.. code-block:: shell

  $ module swap PrgEnv-pgi PrgEnv-gnu
  $ module swap gcc gcc/4.6.2

**General Programming Environment Guidelines**

We recommend the following general guidelines for using the
programming environment modules:

- Do not purge all modules; rather, use the default module environment
  provided at the time of login, and modify it.
- Do not swap or unload any of the Cray provided modules (those with
  names like xt-'*').
- Do not swap moab, torque, or MySQL modules after loading a
  programming environment modulefile.

Compiling Threaded Codes
------------------------

When building threaded codes, you may need to take additional steps to
ensure a proper build.

**OpenMP**

For PGI, add "-mp" to the build line:

.. code-block:: shell

  $ cc -mp test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

For Cray and GNU no additional flags are required:

.. code-block:: shell

  $ module swap PrgEnv-pgi PrgEnv-cray $ cc test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

For Intel:

.. code-block:: shell

  $ module swap PrgEnv-pgi PrgEnv-intel $ cc -openmp test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

**SHMEM**

For SHMEM codes, users must load the xt-shmem module before compiling:

.. code-block:: shell

  $ module load xt-shmem

Hardware
========

c5 partition
------------

- 10.2 petaflop HPE Cray Ex
- 245,760 cores
- 128 cores/node
- 1,920 nodes
- 449 TB of memory
- AMD Rome processors
- 8 Login Nodes


es partition
------------

**rdtn queue**

- Remote Data Transfer Nodes - used for transferring data to/from the
  world outside of Gaea
- 8 nodes (rdtn01-08)
- 8 slots per node
- 64 total slots

**ldtn queue**

- Local Data Transfer Nodes - used for I/O intensive operations, like
  model output combining
- 16 nodes (ldtn1-16)
- 8 cores/node
- 128 cores

**eslogin queue**

- login nodes - used for compiling
- 8 total
- gaea51-58 = c5
- 24 cores
- 256 GB memory

Queue Policy
============

**Some overall points**

The queuing system should allow groups/projects to spend their
allocation each month. The contest between keeping urgent jobs in the
system and running very large jobs suggests that, in general, there
should be a limit on the number of cores a job may use, but with a
capability to make exceptions for “novel” jobs that may require up to
the entire system. This will promote consideration of whether a job
requires a large number of cores due to, for example, memory or
schedule constraints, or whether it is simply desired.

Queues should exist with different priority levels usable by the
scheduling algorithm. At the very least, run-time variability would
need to be assessed before we could even think of implementing this.

**Recommendations**

1. Use a fair-share algorithm that can throttle scheduling priority by
   comparing how much of a particular allocation has been used at a
   given time with how much should have been used, assuming constant
   proportional usage. This will promote steady usage throughout the
   month.
2. Use two separate allocations, renewed monthly, with multiple queues
   drawing down each of them:

   - 50% of the available time for high-priority and urgent work. That
     should minimize queue wait time. Queues are:

     - Urgent, for schedule-driven work that must be completed ASAP.
     - Novel, for jobs that have unusual resource requirements,
       typically needing more than 25% of the system's cores. These
       can be run during an 8-hour period immediately after
       Preventative Maintenance is complete, since no other jobs will
       be running at that time.

  - 50% for all other **normal-priority** allocated work. Queues would
    be:

    - Batch, for regular allocated jobs
    - Debugging/Interactive work
    - Windfall, a quality of service (QOS) tag, for work that will not
      be charged against an allocation.

Windfall can be specified with '-l qos=' directive, as:

.. code-block:: shell

  > sbatch –-qos=windfall

or in your job script:

.. code-block:: shell

  #SBATCH -–qos=windfall

**Priorities between queues**

Normally, the Urgent queue will have the highest priority but remain
subject to the fair-share algorithm. This will discourage groups from
hoarding high-priority time for the end of the month. Within a
group/project, jobs in the Urgent queue are higher priority than jobs
in the Normal queue, with each group expected to manage the
intra-group mix per their allocation. At any given time, the suite of
jobs drawn from the Urgent queue and running on the system should use
about 50% of the available cores (per the fair-share algorithm), but
that suite is permitted to use more than 50% as needed (with the
implication that less than 50% will be used at other times of the
month).

- Limit the largest job to 25% of the available cores except in the
  Novel queue.
- Limit time requested for individual job segments to 12 hours.
- Interactive/debugging jobs have a tiered limit:

  - < or = 72 cores (3 nodes) 12 hour limit
  - < or = 504 cores (21 nodes) 6 hour limit
  - can't go over 504

**Partitions**

Users are encouraged to add the following to their job submissions
and/or job script cluster=<cluster>

.. code-block:: shell

  sbatch --cluster=<cluster> /path/to/job/script

or in your job script:

.. code-block:: shell

  #SBATCH --cluster=<cluster>

where ``<cluster>`` is the cluster name (e.g., ``es``, ``c5``, or
``c6``)

Debug & Batch Queues
--------------------

**Interactive / Debug** The interactive queue may have different time
limits based on the size of the submitted job. To see the current
queue wallclock limits, run

.. code-block:: shell

 sacctmgr show qos format=Name,MaxWall

Note that each cluster may have different wallclock restrictions.

**Interactive queue job time limits**

- 24-72 processors = 12 hours
- 96-504 processors = 6 hours
- Over 528 processors = 4 hours

**Debug queue job time limits:**  1 hour

**Batch:** Default queue for all compute partitions.

**Novel:** Jobs larger than roughly 25% of the total nodes on a given
cluster will automatically be added to the novel queue. The novel
queue does not run until after a periodic maintenance in order to
prevent large amounts of the system being idled as jobs complete
naturally to make room for the novel jobs.

Priority Queues
---------------

Priority queues are allocated one per group, and allow for a single
eligible job per user. These only work for compute partitions. They do
not work on the es partition (eslogin, ldtn, and rdtn queues).

**Urgent:** The urgent queue is for work of the highest priority and
holds the highest weight. It is for schedule-driven work that must be
completed ASAP.

Queues per Partition
--------------------

**es**

- eslogn (compiling)
- ldtn (combining model output, other postprocessing)
- rdtn (data transfers to/from non-Gaea resources)
- compute

**batch**

- interactive
- debug (1 hour limit)
- persistent
- urgent
- novel

Scheduler/Priority Specifics
----------------------------

+------------+------------+------------+------------------------------+
| Factor     | Unit of    | Actual     | Value                        |
|            | Weight     | Weight     |                              |
|            |            | (Minutes)  |                              |
+============+============+============+==============================+
| Class      | # of days  | 1440       | Urgent (10),                 |
|            |            |            +------------------------------+
|            |            |            | Persistent (1),              |
|            |            |            +------------------------------+
|            |            |            | Debug/Interactive (2),       |
|            |            |            +------------------------------+
|            |            |            | Batch (1),                   |
|            |            |            +------------------------------+
|            |            |            | Windfall (-365)              |
+------------+------------+------------+------------------------------+
| Account    | # of days  | 1440       | Allocated project (1),       |
| Priority   |            |            +------------------------------+
|            |            |            | No hours (-365)              |
+------------+------------+------------+------------------------------+
| Fairshare  | # of       | 1          | (<>) 5% user (+/-) 30 mins,  |
|            | minutes    |            +------------------------------+
|            |            |            | (<>) 5% user (+/-) 60 mins   |
+------------+------------+------------+------------------------------+
| Queue Time | 1 Minute   | 1          |                              |
+------------+------------+------------+------------------------------+


Slurm Queueing System
=====================

Please be aware that Gaea is not like a usual Slurm cluster. Slurm
expects that all nodes are homogeneous and capable of being used for
any purpose. Gaea is a heterogeneous set of clusters (hence the need
to specify a cluster as shown below.) This also means that partitions
(queues) for resources with different purposes will need to set up
your job's environment to provide access to the software for that
purpose.(data transfer nodes being chief among these.) Under Slurm
your job will only have the system shell init scripts run if you
specify --export=NONE. The result is that --export=NONE is a required
argument to get your job to see software specific to a given node
type, e.g. HSI/HTAR for HPSS on the data transfer nodes.

Useful Commands
-----------------

- To find the accounts to which you belong:

.. code-block:: shell

  sacctmgr show assoc user=$USER format=cluster,partition,account,user%20,qos%60

- To submit a job to a compute cluster c#:

.. code-block:: shell

  sbatch --clusters=c# --nodes=1 --account=gfdl_z --qos=normal --export=NONE /path/to/job/script

- To submit interactive work to c#:

.. code-block:: shell

  salloc --x11 --clusters=c# --qos=interactive --nodes=1

- View accounting data for a specifc job

.. code-block:: shell

  sacct -j <jobid> --format=jobid,jobname,submit,exitcode,elapsed,reqnodes,reqcpus,reqmem

- To cancel a job

.. code-block:: shell

  scancel <jobid>

- To cancel a jobs on a specific partition

.. code-block:: shell

  scancel -u $USER -p <partition>

Running your models
-------------------

In your compute job scripts or interactive sessions you will want to
run your model executable. If your model is simple (single component,
etc) then use srun. If it is a coupled model or otherwise has multiple
execution contexts and/or executables, you will need to use
srun-multi.

.. code-block:: shell

  srun ./executable

  srun-multi --ntasks 128 --cpus-per-task=1 ./executable

Monitoring your jobs: Shell Setup
---------------------------------

Do not set these in jobs/shells you intend to submit work from, as
they will override your job submission script #SBATCH directives,
causing warnings and errors. Use them in shells you intend to monitor
jobs from.

- In [t]csh

.. code-block:: shell

  setenv SLURM_CLUSTERS t#,c#,gfdl,es
  - In bash

.. code-block:: shell

  export SLURM_CLUSTERS=t#,c#,gfdl,es

- Jobs in the queue

The squeue command is used to pull up information about the jobs in a
queue. By default, squeue will print out the Job ID, partition,
username, job status, and number of nodes.

Example:

.. code-block:: shell

  $squeue  -u $USER

Use man squeue for more information.

- The sstat command allows users to pull up status information about a
  currently running job/step

Example:

.. code-block:: shell

  $sstat --jobs=job-id

Use man sstat for more information.

- Completed Jobs

Slurm does not keep completed jobs in squeue.

.. code-block:: shell

  sacct -S 2019-03-01 -E now -a

If you don't specify -S and -E options, sacct gives you data from
today.

- Getting details about a job

Slurm only keeps information about completed jobs available via
scontrol for 5 minutes after completion. After that time, sacct is the
currently available way of getting information about completed jobs.

.. code-block:: shell

  scontrol show job --clusters=es 5978

Fair Share Reporting
--------------------

- Summary of all accounts

.. code-block:: shell

  sshare

- Summary of one account

.. code-block:: shell

  sshare -A aoml

- Details by user of one account

.. code-block:: shell

  sshare -a -A gefs

- Details by user of all accounts

.. code-block:: shell

  sshare -a

- Priority Analysis of Your Job: sprio

.. code-block:: shell

  sprio -j 12345

Data Transfers
==============

Available on Gaea is a tool called GCP, which allows for internal
transfers on Gaea and to/from other NOAA RDHPCS resources (ZEUS and
GFDL PPAN). Please reference System Details if you are unfamiliar with
the filesystems or expected use of each variety of node on Gaea.

.. note::

  The data transfer nodes are assigned to a site specific partition on
  the es cluster.

  Use the following command to view current and, or available
  partitions:

  .. code-block:: shell

    $ scontrol show partitions

  or

  .. code-block:: shell

    $ scontrol show partitions | grep dtn

Available Tools
---------------

- GCP
- spdcp - lustre to lustre specific
- globus-url-copy (GridFTP)
- scp
- rsync
- cp
- hsi and htar (for Zeus' HPSS)

We suggest all users use GCP as the primary data transfer tool.
Examples are presented below.

f5 <-> f5
----------

Users can transfer data between the F5 filesystem using GCP. This can
be done on the login nodes, and ldtns. Gcp commands issued on the
compute nodes will result in a [L|R]DTN job being created and gcp will
block until that job is completed by default.

.. code-block:: shell

  module load gcp
  gcp /gpfs/f5/<project>/world-shared/file /gpfs/f5/<project>/scratch/$USER/path/file

Gaea <-> GFDL
--------------

Users can transfer data between GFDL and Gaea filesystems with GCP.
This can be done on the login nodes and rdtn's only. Users can
interactively run gcp commands from a login node or submit gcp calls
in scripts to run in the rdtn queue.

.. code-block:: shell

  module load gcp
  gcp gaea:/gpfs/f5/<project>/scratch/$USER/file gfdl:/gfdl/specific/path/file
  gcp gfdl:/gfdl/specific/path/file gaea:/gpfs/f5/<project>/scratch/$USER/path/file

Gaea <-> Remote NOAA Site
-------------------------

Users can transfer data between GFDL and Gaea filesystems with
GridFTP, rsync or scp. This can be done on the login nodes and RDTNs
only. Please place large transfers (>1GB) in batch jobs on the RDTN
queue. This will respect other users on the login nodes by reducing
interactive impact.

.. code-block:: shell

  scp /gpfs/f5/<project>/scratch/$USER/path/name/here some.remote.site:/a/path/over/there
  globus-url-copy file:/path/on/Gaea/file gsiftp://some.remote.site/path/to/destination/file
  globus-url-copy gsiftp://some.remote.site/path/to/remote/file file:/destination/path/on/Gaea/file

Gaea <-> External
-----------------

1. Find Local Port Number
To find your unique local port number, log onto your specified HPC
system (Gaea). Make a note of this number, and once you've recorded
it, close all sessions.

.. code-block:: shell

  You will now be connected to NOAA RDHPCS: Gaea (CMRS/NCRC) C5 system.
  To select a specific host, hit ^C within 5 seconds.
  Local port XXXXX forwarded to remote host.
  Remote port XXXXX forwarded to local host.

.. note::

  Open two terminal windows for this process.

**Local Client Window #1**

Enter the following (remember to replace XXXXX with the local port
number identified in Step 1 or as needed):

.. code-block:: shell

  ssh-LXXXXX:localhost:XXXXX
  First.Last@gaea-rsa.rdhpcs.noaa.gov

Once you have established the port tunnel it is a good idea to verify
that the tunnel is working. To verify, use another local window from
your local machine, and enter the following:

.. code-block:: shell

  ssh -p <port> First.Last@localhost

2. Complete the Transfer using SCP

**Local Client Window #2**

Once the session is open, you will be able to use this forwarded port
for data transfers, as long as this ssh window is kept open. After the
first session has been opened with the port forwarding, any further
connections (login via ssh, copy via scp) will work as expected.

**To transfer a file to HPC Systems**

.. code-block:: shell

  >> scp -P XXXXX /local/path/to/file $USER@localhost:/path/to/file/on/HPCSystems

  >> rsync <put rsync options here> -e 'ssh -l $USER -p XXXXX' /local/path/to/files $USER@localhost:/path/to/files/on/HPCSystems


.. note::

  Your username is case sensitive when used in the scp command. For
  example, username should be in the form of John.Smith rather than
  john.smith.

**To transfer a file from HPC Systems**

.. code-block:: shell

  $ scp -P XXXXX $USER@localhost:/path/to/file/on/HPCSystems /local/path/to/file
  $ rsync <put rsync options here> -e 'ssh -l $USER -p XXXXX' $USER@localhost:/path/to/files/on/HPCSystems /local/path/to/files

In either case, you will be asked for a password. Enter the password
you from your RSA token (not your passphrase). Your response should be
your PIN+Token code.

Gaea <-> Fairmont HPSS
----------------------

Users can transfer data between Gaea and Zeus' High Performance
Storage System (HPSS) through the use of the HSI and HTAR commands.
These commands are only available on Gaea's Remote Data Transfer Nodes
(RDTNs). A user can submit a script to run on the RDTNs.

- Minimum Headers for a submitted RDTN job.

.. code-block:: shell

  #SBATCH --clusters=es
  #SBATCH --partition=rdtn_c#

- Load the HSI module and list the contents of your directory

.. code-block:: shell

  module use -a /sw/rdtn/modulefiles
  module load hsi

- Check connectivity to the hsi, replacing the below file path with
  yours on HPSS

.. code-block:: shell

  hsi "ls -P /BMC/nesccmgmt/$USER/"

- Retrieve Files using HSI into the current directory on the RDTN. The
  -q option limits output spam.

.. code-block:: shell

  hsi -q "get /BMC/nesccmgmt/Karol.Zieba/sample_file"

- Upload Files using HSI

.. code-block:: shell

  hsi -q "put /gpfs/f5/<project>/scratch/$USER/file_to_upload : /BMC/nesccmgmt/$USER/file_to_upload"

- Tar many small files from the RDTN using HTAR. (Note that using
  asterisk will not work.)

.. code-block:: shell

  htar cf /BMC/nesccmgmt/$USER/tarred_file.tar file1 file2 path/file3

- Untar many small files into your current directory on the RDTN using
  HTAR

.. code-block:: shell

  htar xf /BMC/nesccmgmt/$USER/tarred_file.tar


External (Untrusted) Data Transfers
------------------------------------

To support external data transfers with methods that are faster and
simpler than the port tunnel method, NOAA RDHPCS has a data transfer
node. This means data can be transferred to Gaea without the use of
the port tunnel or existing ssh connection. Not only is this simpler,
but provides for much faster transfers. The difference between the
eDTN and the DTN as described above is that the eDTN does not mount
the Gaea filesystems.

Transferring through the eDTN to Gaea requires a two step process.
First, files are transferred from external hosts to the eDTN. Second,
from Gaea, the files are pulled back from the eDTN.

For authentication, use of your token is required from external
transfers to the eDTN. From within Gaea, use of your token is not
required.

The eDTN supports the use of scp, sftp, bbcp, and ssh based
globus-url-copy.

**Copying files from external systems to the eDTN**

.. code-block:: shell

  jsmith# scp WRF.tar.gz John.Smith@edtn.fairmont.rdhpcs.noaa.gov:

  Access is via First.Last username only.  Enter RSA PASSCODE:

The trailing colon (':') is critical. You can also specify
":/home/John.Smith/"

Your response should be your pin+PASSCODE.

**Retrieving files on Gaea from the eDTN**

To transfer files from the eDTN server to Gaea without requiring your
token, you must use GSI enabled transfer methods. For scp, sftp, and
bbcp, this mean appending "gsi" to the front of the command. So the
commands that are best to use are gsiscp, gsisftp, and gsibbcp.

To pull the files back from the eDTN, initiate on of these commands:

.. code-block:: shell

  John.Smith# gsiscp -S `which gsissh` edtn.fairmont.rdhpcs.noaa.gov:WRF.tar.gz .

**eDTN Purge Policy**

Files older than 7 days will be automatically removed. This policy may
change based on disk space and management needs.

**Managing files on the eDTN**

If you need to login and manage any files, create or remove
directories, or any other tasks on the eDTN, use gsisftp from Gaea.
This provides and FTP like interface through ssh.

.. code-block:: shell

  # sftp -S `which gsissh` John.Smith@edtn.fairmont.rdhpcs.noaa.gov
  Access is via First.Last username only. Enter RSA PASSCODE:
  Connected to edtn.fairmont.rdhpcs.noaa.gov.
  sftp> ls
  bigfile    bigfile1   bigfileA
  sftp> rm bigfile
  Removing /home/Craig.Tierney/bigfile
  sftp> rm bigfile*
  Removing /home/Craig.Tierney/bigfile1
  Removing /home/Craig.Tierney/bigfileA
  sftp> ls
  sftp> mkdir newdir1
  sftp> ls
  newdir1
  sftp> cd newdir1
  sftp> pwd
  Remote working directory: /home/Craig.Tierney/newdir1
  sftp> cd ..
  sftp> rmdir newdir1
  sftp> ls

  sftp> help
  Available commands:
  bye                                Quit sftp
  cd path                            Change remote directory to 'path'
  chgrp grp path                     Change group of file 'path' to 'grp'
  chmod mode path                    Change permissions of file 'path' to 'mode'
  chown own path                     Change owner of file 'path' to 'own'
  df [-hi] [path]                    Display statistics for current directory or
                                    filesystem containing 'path'
  exit                               Quit sftp
  get [-Ppr] remote [local]          Download file
  help                               Display this help text
  lcd path                           Change local directory to 'path'
  lls [ls-options [path]]            Display local directory listing
  lmkdir path                        Create local directory
  ln oldpath newpath                 Symlink remote file
  lpwd                               Print local working directory
  ls [-1afhlnrSt] [path]             Display remote directory listing
  lumask umask                       Set local umask to 'umask'
  mkdir path                         Create remote directory
  progress                           Toggle display of progress meter
  put [-Ppr] local [remote]          Upload file
  pwd                                Display remote working directory
  quit                               Quit sftp
  rename oldpath newpath             Rename remote file
  rm path                            Delete remote file
  rmdir path                         Remove remote directory
  symlink oldpath newpath            Symlink remote file
  version                            Show SFTP version
  !command                           Execute 'command' in local shell
  !                                  Escape to local shell
  ?                                  Synonym for help


GCP
===

GCP (general copy) is a convenience wrapper for copying data between
the Gaea and PPAN Analysis NOAA RDHPCS sites, as well as the NOAA GFDL
site. GCP abstracts away the complexities of transferring data
efficiently between the various NOAA sites and their filesystems. Its
syntax is similar to the standard UNIX copy tool, cp.

GCP 2.3.30 is available on Gaea, PPAN, and GFDL Linux Workstations. It
is obtainable via “module load gcp” or “module load gcp/2.3”, This
version is the latest on systems as of 2023-12-01; all other versions
are considered obsolete and will not function properly due to system
updates.

User Guide
-----------

Using GCP is simple – just use a variant of the commands below to
perform a transfer:

.. code-block:: shell

  module load gcp
  gcp -v /path/to/some/source/file /path/to/some/destination/file

The -v option enables verbose output, including some very useful
information for debugging.

You can obtain a detailed list of all of the available options with:

.. code-block:: shell

  gcp --help

Smartsites
----------

GCP introduces a concept known as smartsites. This concept enables the
transfer of files from one NOAA system to another. Each NOAA site has
its own smartsite. The currently supported smartsites in GCP are:

.. code-block:: shell

  - gfdl - gaea

To transfer data from one site to another, simple prepend the
smartsite and a colon to your file location (example:
gaea:/path/to/file).

This smartsite example pushes data from a source site (GFDL) to a
remote site (Gaea). Note that we are not required to use a smartsite
for the local site we are currently operating from (but it is not an
error to include it). The following commands are equivalent:

.. code-block:: shell

   $ gcp -v /path/to/some/file gaea:/path/to/remote/destination
   $ gcp -v gfdl:/path/to/some/file gaea:/path/to/remote/destination

The smartsite needn't always be part of the destination file path, as
gcp is capable of pulling data from a remote site as well as pushing
it:

.. code-block:: shell

  gcp -v gaea:/path/to/a/file /path/to/a/local/destination

**Log Session ID**

GCP includes a comprehensive logging system. Each transfer is recorded
and is easily searchable by the GCP development team in the event that
debugging is needed.

Each transfer is given a unique log session id, but this session id is
only visible if the -v option is used. It is highly recommended that
this option always be enabled in your transfers. A sample of the
expected output is below:

.. code-block:: shell

  gcp -v /path/to/source/file /path/to/destination
  gcp 2.3.26 on an204.princeton.rdhpcs.noaa.gov by Chandin.Wilson at Mon Aug 8 16:39:28 2022
  Unique log session id is 07f6dd51-6c4d-4e51-86b4-e3344c01c3ae at 2022-08-08Z20:39

If you experience any problems while using GCP, please re-run your
transfer using the -v option and provide the session id with your help
desk ticket.

**Supported Filesystems**

GCP can copy data from many filesystems, but not all. Below is a list
of supported filesystems for each site. Note that sometimes GCP is
able to support a filesystem from within the local site, but not from
external sites.

**GFDL Workstations**

.. note::

  You cannot transfer files from a GFDL workstation to any remote
  site. You must use GFDL's PAN cluster to push or pull files to a
  remote site.

Filesystems that GCP supports locally from GFDL workstations:

- /net
- /net2
- /home
- /work
- /archive

Filesystems that GCP supports remotely from other sites:

- /home
- /ptmp
- /work
- /archive

**Gaea**

The Gaea site contains multiple node types. The nodes that are used
for interactive work are called the eslogin nodes. Different
filesystems are supported on each node type, so please refer to the
list below.

Filesystems that GCP supports locally from Gaea:

- eslogin

.. note::

  Please verify that both the operating system and the processor
  support Intel(R) X87, CMOV, MMX, FXSAVE, SSE, SSE2, SSE3, SSSE3,
  SSE4_1, SSE4_2, MOVBE, POPCNT, AVX, F16C, FMA, BMI, LZCNT and AVX2
  instructions.

CAC bastions refusing login attempts without asking for PIN
-----------------------------------------------------------

We have had reports of users being unable to connect to the CAC
bastions via TECTIA client. As documented, CAC bastions are the
servers you connect to with the ``sshg3 gaea.rdhpcs.noaa.gov``.  They
maintain your Globus certificate and put your connection through to
the Gaea login nodes. On Linux clients one workaround is to kill the
ssh-broker-g3 process and try your login again.

.. code-block:: shell

   $ ps -ef | grep ssh-broker-g3
   4060     15451 15184  0 14:05 pts/4    00:00:00 grep ssh-broker-g3
   4060     29775 29765  0 Dec22 ?        00:00:42 /opt/tectia/bin/ssh-broker-g3 --run-on-demand
   $ kill -9 29775
   sshg3 gaea

Shell hang on login
-------------------

Users have often reported issues where their sessions freeze or hang
on C3 login nodes unless Ctrl+c is pressed.  This issue can also
result in your jobs timing out either at the start of the job or the
end.  This hang might be due to a corrupted tcsh ``~/.history`` file.
The current workaround is to delete the ``~/.history`` file.

GPFS (F5) Performance
---------------------

The Gaea system intermittently has issues with the GPFS F5
performance.  This typically appears as file operations hangs in
interactive sessions, and as jobs taking longer than normal to
complete, or timming out. Many jobs on Gaea are currently experiencing
longer than normal run times.  While we do not yet have an underlying
cause for this, we have found certain changes to the user's
interactions and workflows that use the GPFS F5 file system help
alleviate the problem.

Files Accesses by Multiple Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users should not have multiple batch jobs access the same files.  This
is typically done using hard- or soft-links.  Access the same file
from multiple batch jobs increases the load on the Lustre metadata
servers (MDS), and can lead to a MDS locking up affecting all files
served on that MDS.

Users should clean up files after the job runs successfully to ensure
the Lustre file system has enough free space for all user's jobs.

Software Environments
^^^^^^^^^^^^^^^^^^^^^

Users should not store software environments, e.g., conda, spack, on
the Lustre file system.  These environments have many small files that
will be accessed from multiple compute nodes when used in batch jobs.

These environments should be stored in user's home space.  If the
environment is to be shared by several users or groups, the
environment can be installed in either the /ncrc/proj space, or /usw.

Development
^^^^^^^^^^^

GPFS F5 should not be used for development.  Development should be
done in the user's home space.  This is especially true if using a
source code management system (e.g., git).

Users should remember that GPFS F5 is not backed up. The
user home area is backed up, with hourly and daily snapshots.


