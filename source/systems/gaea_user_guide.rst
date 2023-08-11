.. _gaea-user-guide:

***************
Gaea User Guide
***************

.. _gaea-system-overview:

.. image:: /images/Gaea_web.jpg

System Overview
===============

`Gaea <https://www.noaa.gov/organization/information-technology/gaea>`_
is an `NOAA Research and Development High-Performance Computing System
(RDHPCS) <https://www.noaa.gov/information-technology/hpcc>`_ operated
by the `National Climate-Computing Research Center (NCRC)
<https://www.ncrc.gov/>`_.  The NCRC is located within the
`National Center for Computational Sciences (NCCS)
<https://www.ornl.gov/division/nccs>`_ at the `Oak Ridge National
Laboratory (ORNL) <https://www.ornl.gov/>`_.   The NCRC is a
collaborative effort between the `Department of Energy
<https://www.energy.gov/>`_ and the `National Atmospheric and Oceanic
Administration <https://www.noaa.gov/>`_.

The Gaea System consists of two HPE Cray XC40 supercomputers and an HPE Cray EX
supercomputer.  The XC40 systems have an aggregate of more than 200 terabytes of
memory and a peak calculating capacity greater than 5.25 petaflops.  The EX system
has 482 terabytes of memory and a peak calculating capacity of 10.2 petaflops.

Gaea uses a high-capacity Lustre file system with over 32 petabytes
of storage.  The file system is connected to the Gaea system using
FDR InfiniBand.

.. csv-table:: Gaea Cluster Stats
    :file: /files/gaea_stats.csv
    :header-rows: 1

.. list-table:: Gaea Cluster Stats (list)
    :header-rows: 1

    * - C3
      - C4
      - C5
      - F2 File System
    * - Cray XC40-LC Haswell
      - Cray XC40-LC Broadwell
      - HPE EX Rome
      - DDN Lustre
    * - 1,504 compute nodes
        (2 x Intel Haswell 16-cores per node)
      - 2,656 compute nodes (2 x Intel Broadwell 18-cores per node)
      - 1,920 compute nodes (2 x AMD Rome 64-cores per node)
      - 32 PB total usable; ZFS compression
    * - 64GB DDR4 per node; 96TB total
      - 64GB DDR4 per node; 145TB total
      - 251 GB DDR5 per node; 449TB total
      - 36 OSS; 72 OST; 4 MDS
    * - 1.77 PF peak
      - 3.52 PF peak
      - 10.2 PF peak
      -

.. grid:: 4

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C3
    ^^^

    Cray XC40-LC

    1,504 compute nodes
    (2 x Intel Haswell 16-cores per node)

    64GB DDR4 per node; 96TB total

    1.77 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C4
    ^^^

    Cray XC40-LC

    2,656 compute nodes (2 x Intel Broadwell 18-cores per node)

    64GB DDR4 per node; 145TB total

    3.52 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C5
    ^^^

    HPE EX

    1,792 compute nodes (2 x AMD Rome 64-cores per node)

    251 GB DDR5 per node; 449TB total

    10.2 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    F2 File System
    ^^^

    DDN Lustre

    32 PB total usable; ZFS compression

    36 OSS; 72 OST; 4 MDS

Node Types
----------

Gaea has three node types: login, compute, and data transfer (DTN).  All are similar
in terms of hardware, but differ in their intended use.

+---------------+----------------------------------------------------------------------------------+
| Node Type     | Description                                                                      |
+===============+==================================================================================+
| Login         | When you connect to Gaea, you're placed on a login node.  This is the place to   |
|               | write, edit, and compile your code; manage data; submit jobs; etc.  You should   |
|               | not launch parallel jobs from the login nodes, nor should you run threaded jobs. |
|               | Login nodes are shared resources that are in use by many users simultaneously.   |
+---------------+----------------------------------------------------------------------------------+
| Compute       | The compute nodes are where parallel jobs are executed.  They're accessed via the|
|               | ``srun`` command.                                                                |
+---------------+----------------------------------------------------------------------------------+
| Data Transfer | The data transfer nodes are used to perform IO intensive file manipulation, e.g.,|
|               | combining multiple data files into a single file, and to transfer large files    |
|               | locally and to external sites.                                                   |
+---------------+----------------------------------------------------------------------------------+

Login Nodes
-----------

The C3/C4 and C5 clusters have different login nodes.  The C3/C4 login nodes are
named gaea10-gaea15.  The C5 login nodes are named gaea51-gaea58.  Each cluster
specific login node has hardware similar the cluster they serve.

.. tab-set::

  .. tab-item:: C3/C4 Login Nodes

    +-----------------+----------------------------+
    | CPU Type        | Intel Haswell (E5-2690 v3) |
    +-----------------+----------------------------+
    | CPU Speed       | 2.6 GHz                    |
    +-----------------+----------------------------+
    | Number of Nodes | 5                          |
    +-----------------+----------------------------+
    | Cores per Node  | 48                         |
    +-----------------+----------------------------+
    | Memory per Node | 251 GiB                    |
    +-----------------+----------------------------+

  .. tab-item:: C5 Login Nodes

    +-----------------+----------------------------+
    | CPU Type        | AMD Rome (7662)            |
    +-----------------+----------------------------+
    | CPU Speed       | 2.0 GHz                    |
    +-----------------+----------------------------+
    | Number of Nodes | 8                          |
    +-----------------+----------------------------+
    | Cores per Node  | 128                        |
    +-----------------+----------------------------+
    | Memory per Node | 503 GiB                    |
    +-----------------+----------------------------+

Data Transfer Nodes (DTN)
-------------------------

+-----------------+----------------------------+
| CPU Type        | AMD Rome (7702)            |
+-----------------+----------------------------+
| CPU Speed       | 2.0 GHz                    |
+-----------------+----------------------------+
| Number of Nodes | 16                         |
+-----------------+----------------------------+
| Cores per Node  | 128                        |
+-----------------+----------------------------+
| Memory per Node | 503 GiB                    |
+-----------------+----------------------------+

Compute Nodes
-------------

+------------------------+----------------------------+------------------------------+------------------+
|                        | C3                         | C4                           | C5               |
+========================+============================+==============================+==================+
| CPU Type               | Intel Haswell (E5-2698 v3) | Intel Broadwell (E5-2697 v4) | AMD Rome (7H12)  |
+------------------------+----------------------------+------------------------------+------------------+
| CPU Speed              | 2.3 GHz                    | 2.3 GHz                      | 2.6 GHz          |
+------------------------+----------------------------+------------------------------+------------------+
| Number of Nodes        | 1,504                      | 2,656                        | 1,920            |
+------------------------+----------------------------+------------------------------+------------------+
| Number of Sockets      | 2                          | 2                            | 2                |
+------------------------+----------------------------+------------------------------+------------------+
| Cores per Socket       | 16                         | 18                           | 16               |
+------------------------+----------------------------+------------------------------+------------------+
| Threads per Core       | 2                          | 2                            | 2                |
+------------------------+----------------------------+------------------------------+------------------+
| Total Cores per Node   | 32                         | 36                           | 128              |
+------------------------+----------------------------+------------------------------+------------------+
| Total Threads per Node | 64                         | 72                           | 256              |
+------------------------+----------------------------+------------------------------+------------------+
| Total Cores            | 48,128                     | 95,616                       | 245,760          |
+------------------------+----------------------------+------------------------------+------------------+
| Memory per Node        | 64 GiB                     | 64 GiB                       | 251 GiB          |
+------------------------+----------------------------+------------------------------+------------------+
| Total Memory           | 96,256 GiB                 | 169,984 GiB                  | 481,902 GiB      |
+------------------------+----------------------------+------------------------------+------------------+
| Interconnect           | Cray Aires                 | Cray Aires                   | HPE Slingshot 10 |
+------------------------+----------------------------+------------------------------+------------------+
| Total Flops            | 1.77 PF                    | 3.52 PF                      | 10.2 PF          |
+------------------------+----------------------------+------------------------------+------------------+

Connecting
==========

Connecting with a CAC
---------------------

The preferred method to to access Gaea is to use the CAC bastion.  This will use
your CAC for authentication.  This method requires the TECTIA SSH client. RDHPCS
has obtained licenses for all RDHPCS users.  Please follow the
:ref:`instructions <cac_instructions>` to obtain the TECTIA client and license.

With the TECTIA client, use the CAC bastion hosts are at the URLs
``gaea.princeton.rdhpcs.noaa.gov`` and ``gaea.boulder.rdhpcs.noaa.gov``.  Follow
the :ref:`CAC instructions <cac_instructions>` on additional configuration
settings.  Once the Gaea host is configured in TECTIA, open a connection with

.. code-block:: shell

    sshg3 gaea.princeton.rdhpcs.noaa.gov

or

.. code-block:: shell

    sshg3 gaea.boulder.rdhpcs.noaa.gov

When propted, enter your CAC PIN.

Connecting with an RSA token
----------------------------

Users who do not have a CAC, or are connecting using a system that does not have
a TECTIA client (e.g., Mac OS, Android, ChromeOS, etc.) will need to use the RSA
bastion.  The RSA bastion hosts are at the URLs
``gaea-rsa.princeton.rdhpcs.noaa.gov`` and ``gaea-rsa.boulder.rdhpcs.noaa.gov``.

.. code-block:: shell

    ssh gaea-rsa.princeton.rdhpcs.noaa.gov

or

.. code-block:: shell

    ssh gaea-rsa.boulder.rdhpcs.noaa.gov

When propted, enter your PASSCODE which consists of your PIN+RSA_CODE.  The
RSA_CODE is the 6-8 digit code from the RSA fob or RSA app.

.. note::

    The first connection with an RSA token, you will be requested for a new PIN
    which must be at least 6 alphanumeric characters.

Data and Storage
================

Software
========

Shell & Programming Environments
================================

Gaea is implemented using the Environment Modules system. This tool helps users
manage their Unix or Linux shell environment. It allows groups of related
environment variable settings to be made or removed dynamically.  Modules
provide commands to dynamically load, remove and view software.

More information on using modules is available at :ref:`modules <modules>`.

.. gaea_compiling:

Compiling
=========

Compiling code on Cray machines is different than compiling code for commodity
or beowulf-style HPC linux clusters. Among the most prominent differences:

- Cray provides a sophisticated set of compiler wrappers to ensure that the
  compile environment is setup correctly. Their use is highly encouraged.
- In general, linking/using shared object libraries on compute partitions is not
  supported.

Available Compilers
-------------------

The following compilers are available:

- The Intel Classic Compiler Suite
- The Intel OneAPI Compiler Suite
- GCC, the GNU Compiler Collection
- The Cray Compiler Suite

Cray Compiler wrappers
----------------------

Cray provides a number of compiler wrappers that substitute for the traditional
compiler invocation commands. The wrappers call the appropriate compiler, add
the appropriate header files, and link against the appropriate libraries based
on the currently loaded programming environment module. To build codes for the
compute nodes, you should invoke the Cray wrappers via:

cc
  To use the C compiler
CC
  To use the C++ compiler
ftn
  To use the Fortran compiler

These wrappers are provided by ``PrgEnv-[intel|gnu|pgi|cray]`` modules.
``PrgEnv-intel`` is the default module when you login to Gaea.

Compiling for Compute Nodes
---------------------------

Cray compute nodes are the nodes that carry out the vast majority of
computations on the system.  Using the Cray compiler wrappers, your
code will be built targeting the compute nodes. All parallel codes should run on
the compute nodes.

.. note::

  We highly recommend that the Cray-provided cc, CC, and ftn compiler wrappers be
  used when compiling and linking source code for use on the compute nodes.

.. warning::
  Always compile on the login nodes. Never compile on the compute nodes.

.. note::

  Gaea also has LDTN and RDTN nodes. These are for combining model output
  (LDTN) and data transfer (RDTN) only, not compiling.

.. warning::

  Long-running or memory-intensive codes should not be compiled for use on login
  nodes.


Support for Shared Object Libraries
-----------------------------------

Cray systems support linking with both static and dynamic libraries.  The Cray
compiler wrappers use an environment variable ``SOME_ENV_VAR`` to determine how
to link external libraries.  The default link method for the C3 and C4 clusters
is static, while C5's default is dynamic.

.. note::

  Dynamic linking will create smaller executalbe.  However, the environment must
  be identical when running the executalbe as was configured when building.
  Static binaries are larger, but do not require the build and runtime
  environments to be identical.

Changing Compilers
------------------

If a different compiler is required, it is important to use the correct
environment for each compiler. To aid users in pairing the correct compiler and
environment, programming environment modules are provided. The programming
environment modules will load the correct pairing of compiler version, message
passing libraries, and other items required to build and run. We highly
recommend that the programming environment modules be used when changing
compiler vendors. The following programming environment modules are available:

- PrgEnv-gnu
- PrgEnv-cray
- PrgEnv-intel

To change the compiler, use the ``module swap`` command.  For example, to change
from the Intel compiler to the GNU compiler run the command:

.. code-block:: shell

  module swap PrgEnv-intel Prgenv-gnu

Changing Versions of the Same Compiler
--------------------------------------

To use a specific compiler version, you must first ensure the compiler's PrgEnv
module is loaded, and then use ``module swap`` to the desired version.

.. code-block:: shell

  module swap gcc/12.0.2

.. danger::

  Do not run ``module purge`` on any Gaea node.  The Cray Operating System (COS)
  requires several modules to be loaded to work properly, and several of the
  modules will not reload properly if unloaded.

Running Jobs
============

Debugging
=========

Optimizing and Profiling
========================

Known Issues
============

CAC bastions refusing login attempts without asking for PIN
-----------------------------------------------------------

We have had reports of users being unable to connect to the CAC bastions via
TECTIA client. As documented, CAC bastions are the servers you connect to with
the ``sshg3 gaea.rdhpcs.noaa.gov``.  They maintain your Globus certificate and
put your connection through to the Gaea login nodes. On Linux clients one
workaround is to kill the ssh-broker-g3 process and try your login again.

.. code-block: shell

  > ps -ef | grep ssh-broker-g3
  4060     15451 15184  0 14:05 pts/4    00:00:00 grep ssh-broker-g3
  4060     29775 29765  0 Dec22 ?        00:00:42 /opt/tectia/bin/ssh-broker-g3 --run-on-demand
  > kill -9 29775
  sshg3 gaea

Shell hang on login
-------------------

Users have often reported issues where their sessions freeze or hang on C3 login
nodes unless Ctrl+c is pressed.  This issue can also result in your jobs timing
out either at the start of the job or the end.  This hang might be due to a
corrupted tcsh ``~/.history`` file.  The current workaround is to delete the
``~/.history`` file.

Lustre (F2) Performance
-----------------------

The Gaea system intermittently has issues with the Lustre F2 performance.  This
typically appears as file operations hangs in interactive sessions, and as jobs
taking longer than normal to complete, or timming out. Many jobs on Gaea are
currently experiencing longer than normal run times.  While we do not yet have
an underlying cause for this, we have found certain changes to the user's
interactions and workflows that use the Lustre F2 file system help alleviate the
problem.

Files Accesses by Multiple Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users should not have multiple batch jobs access the same files.  This is
typically done using hard- or soft-links.  Access the same file from multiple
batch jobs increases the load on the Lustre metadata servers (MDS), and can lead
to a MDS locking up affecting all files served on that MDS.

Another method used for sharing files is referencing files stored in pdata
(*/lustre/f2/pdata*) directly.  Users should copy files out of pdata for each
batch job that will use the file.

Users should clean up files after the job runs successfully to ensure the Lustre
file system has enough free space for all user's jobs.

Software Environments
^^^^^^^^^^^^^^^^^^^^^

Users should not store software environments, e.g., conda, spack, on the Lustre
file system.  These environments have many small files that will be accessed
from multiple compute nodes when used in batch jobs.

These environments should be stored in user's home space.  If the environment is
to be shared by several users or groups, the environment can be installed in
either the /ncrc/proj space, or /usw.

Development
^^^^^^^^^^^

Lustre F2 should not be used for development.  Development should be done in the
user's home space.  This is especially true if using a source code management
system (e.g., git).

Users should remember that Lustre F2 is not backed up.  Data loss on Lustre F2
is rare, but Gaea has suffered two data losses on F2.  The user home area is
backed up, with hourly and daily snapshots.

Additional Resources
====================

.. toctree::
  :maxdepth: 1

  gaea/quickstart
  gaea/accounts
