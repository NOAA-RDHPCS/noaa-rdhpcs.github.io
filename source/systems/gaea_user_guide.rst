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
| Cores per Socket       | 16                         | 18                           | 64               |
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

C5 Nodes and Cores 
------------------

Login Nodes 
~~~~~~~~~~~

There are eight new login nodes for the C5 cluster. You may submit batch jobs to the C5 login nodes using eslogin_c5 partition name. 

.. code-block:: shell

   sbatch --cluster=es --partition=eslogin_c5

Slurm allows batch jobs to request hardware resources in addition to nodes and cores, such as memory. If not explicitly set with sbatch options (e.g., sbatch --mem=20G), batch jobs request a default memory per requested (logical) core (e.g., sbatch --ntasks=8). The default memory per core for the C5 login nodes is 2GB. 


Compute Nodes 
~~~~~~~~~~~~~

Each C5 compute node consists of [2x] 64-core AMD Rome EPYC Rome "Zen 2" 7H12 CPUs (with 2 hardware threads per physical core) with access to 251 GB of DDR4 memory. The nodes are dual socket systems with eight memory channels per socket. AMD has technology known as Simultaneous Multithreading, similar to Intel's Hyper-Threading technology, which doubles the number of logical CPUs on a node allowing for 256 logical cores. 

The compute nodes are configured in high-bandwidth mode in order to minimize local memory latency for NUMA-aware or highly parallelizable workloads by defining multiple NUMA zones per socket.
* 4 memory "NUMANodes" per socket
* Allocates memory channels to core groups 
* 16 cores per memory "node"

Applications runnnig with OpenMP are supported and run well on C5. On C3 and C4 clusters, OpenMP appplications have been able to utilize HyperThreads for a slight performance benefit. 


System Interconnect 
-------------------
The C5 nodes are connected using the HPE Slingshot Interconnect (version 10) 


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

Modules and Software
===================

LMOD
----
LMOD is the modules software management system used on C5 and the C5 login nodes. Unlike the module system on C3/C4, LMOD employs a hierarchical system that, when used properly, considers dependencies and prerequisites for a given software package. For example, the **cray-netcdf** module depends on the **cray-hdf5** module and cannot be seen by the standard **module avail** commands nor be loaded until the **cray-hdf5** module is loaded. 

The LMOD hierarchical system will automatically deactivate or swap an upstream module dependency. Two examples are given below. Another feature of LMOD is swapping or unloading an upstream dependency. When that happens, any downstream module will still be loaded but inactivated.

.. code-block:: shell

    prompt> module load cray-hdf5
    prompt> module load cray-netcdf
    prompt> module unload cray-hdf5

    Inactive Modules:
  	    1) cray-netcdf

LMOD Search Commands
--------------------

To find a specific module, use ``module spider``. The command will show all modules and versions with the name. This includes modules that cannot be loaded in the current environment. 

.. code-block:: shell

    module spider <module> 
    
  
``module avail`` will show only modules that can be loaded in the current environment. 

Adding Additional Module Paths
------------------------------

**Do not manually set the MODULESPATH environment variable.** Manually setting the MODULESPATH environment variable will produce unknown behavior. Use ``module use <path>`` or ``module use -a <path>`` to add more module paths. 

Data and Storage
================

Filesystems
-----------

Gaea has two filesystems: Home and F2, a parallel filesystem based on Lustre.

Home Filesystem
---------------

The home filesystem is split into two sections both of which are backed up. For load balance purposes, there is a home1 and home2. 

.. note::

    Each user has a 5GB limit.

Home is mounted on:

- Batch nodes
- LDTN
- RDTN
- Login nodes


A snapshot can be accessed at ``/ncrc/home1|2/.snapshot/{daily or hourly}/$USER``

You can use this path to restore files or subdirectories. The permissions will be the same as the originals and users can simply copy from that location to any destination. 



Lustre Filesystems (F2)
-----------------------

F2 is a 33PB Lustre Filesystem. Certain limitations apply to F2. For instance, performance will start to degrade after utilization exceeds 80% on a file system. Therefore, using well-formed I/O, managing the quota, and using lustre storage tools (when searching your files or managing your spcae) is important. 

User directories are available at:

.. code-block:: shell

    lustre/f2/scratch/$USER/

and

.. code-block:: shell

    lustre/f2/dev/$USER


NCEP users' directories are available at:

.. code-block:: shell

    lustre/f2/scratch/ncep/$USER

and

.. code-block:: shell

   lustre/f2/dev/ncep/$USER
   

All files over 2 weeks old will be scrubbed within the ``lustre/f2/scratch/$USER`` and ``lustre/f2/scratch/ncep/$USER`` directories. Directories under /lustre/f2/dev are not swept. Files that have not been accessed or used within 2 weeks will be scrubbed. 

.. note::

  F2 is **NOT** backed up. Users are responsible for monitoring their files and transferring what they do not want to lose to a location without a scrubbing policy and with data back-ups.

F2 is mounted on:

- C4 (batch and compute nodes)
- C5 (batch and compute nodes)
- LDTN
- RDTN
- Login nodes

You should have directories in the following locations:

- ``lustre/f2/scratch/$USER`` (symlinked from ``lustre/f2/scratch/<YOUR_CENTER>/$USER``)
- ``lustre/f2/dev$USER`` (symlinked from ``lustre/f2/dev/<YOUR_CENTER>/$USER``)

F2 Specs
--------

- Improved I/O performance
- 33 PB of usable storage
- Automatic lossless compression of files
- Additional metadata capacity

Environment Variables for F2 locations
--------------------------------------

- PDATA = ``/lustre/f2/pdata``
- DEV = ``/lustre/f2/dev``
- SCRATCH = ``/lustre/f2/scratch``


Software
========

Python
------

PythonEnv
~~~~~~~~~

Conda
~~~~~

Jupyter Notebooks
~~~~~~~~~~~~~~~~~

Cron
----

.. warning::

  Cron is only functional on C4.


Cron is a job scheduler that allows users to run commands at specifically chosen, time-based intervals. Gaea's login nodes can access and modify a central crontab. Each user has an individual crontab which can be accessed using the ``crontab -e`` command-line tool from any of the Gaea login nodes. 

By default, ``crontab -e`` command will open a vi-based editor environment. A user can set the ``VISUAL`` or ``EDITOR`` environment variables. See ``man crontab`` for more information. 

Scrontab
--------

Traditionaly cron functionality has been replaced on C5 with the the Slurm crontab tool called ``scrontab``. Scrontab is used to set, edit, and remove a user's Slurm-managed crontab. This combines the same functionality as cron with the resiliency of the batch system. Jobs are run on a pool of nodes, so unlike regular cron, a single node going down will not keep you scrontab job from running. 

You can edit your scrontab script with:

.. code-block:: shell

   $ scrontab -e

You can view existing scripts with:

.. code-block:: shell

   $ scrontab -l

.. note::

  By default, vi is the editor for scrontab. For a different editor, you can set the ``EDITOR`` environment variable (e.g. ``export      
  EDITOR=/usr/bin/emacs).

For more information on scrontab, use ``man scrontab``.

Other Software
--------------

- Debuggers
- X2go
- Shpcrpt
- Lustre Filesystem Tools
- Software Requests

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

New Compilers on C5 
~~~~~~~~~~~~~~~~~~~

NVHPC is the replacement for the PGI compiler. 
AOCC is the AMD Optimizing C/C++ and Fortran Compiler.
All of MSD's testing has been experimental and limited with these compilers. 

The following compilers and programming environments are available on C5 as modules:

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


With Intel 2022 compilers on C5 users should replace the -xsse2 compiler option with one of the following: 

- ``-march=core-axv-i``: **Recommended** for production. MSD is using this for regression testing. A limited number of MOM6-solo tests on t5 even bitwise produce c4 answers with this option unlike the next. MSD has found no reproducibility issues with this option so far. This option is used for FRE targets prod and repro

- ``-march=core-avx2``: **Not Recommended** for production, at the moment, for GFDL climate models. Should only be used for exploratory testing with advanced AVX optimizations. There are known restart reproducibility issues with GFDL climate models potentially affecting multi-segment runs, but no repeatability issues have been seen so far for single-segement runs. 

**Caution**: When building a production executable, please review the compilation output to ensure that ``-march=core-avx-i`` is used. 


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

  Dynamic linking will create smaller executable.  However, the environment must
  be identical when running the executable as was configured when building.
  Static binaries are larger, but do not require the build and runtime
  environments to be identical.

Within C5, the Cray Programming Environement (CrayPE) now defaults to dynamically linked libraries. The executable will not include copies of the assocaited libraries at link time but will look for the libraries using the LD_LIBRARY_PATH variable and load them when executed. For this reason, batch scripts must load the appropriate modules for a given executable. If not loaded, the executable will issue an error similar to: 

.. code-block:: shell

   <executable>: error while loading shared libraries: cannot open shared object file: No such file or directory

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

Slurm
-----

Gaea uses a batch scheduling system known as SchedMD’s Slurm Workload Manager for scheduling and managing jobs. Users can run programs by submitting scripts to the Slurm job scheduler. 

A runscript must do the following:

1. Set the environment
2. Apply directives in order to specify instructions on setting up a job
3. Specify the work to be carried out in the form of shell commands


Login v. Compute Nodes
----------------------

As previously stated in 'System Overview', Gaea contains two node types: Login and Compute. When you connect to the system, you are placed on a login node. On a login node you can submit jobs, edit files, and monitor your jobs. These nodes are not intended for real computation. Running computationally intensive processes on the login nodes is discouraged. 

.. warning::

  Do not run heavy computation on login nodes. Doing so may negatively impact other users who interact with the cluster. 


In constrast, a compute node is intended for heavy computation. All of the real computation occurs on compute nodes and most of the nodes fall into this category. When starting a batch job, your batch script runs on one of the allocated compute nodes.


Basic Job Submission
--------------------

Generally, users submit jobs by writing a batch script and submitting the job to Slurm with the ``sbatch`` command. The ``sbatch`` command takes a number of options. The options you are allowed to specify are the set of options used for the SLURM batch system. For a list of options, use the ``man sbatch`` page. 


It is also possible to submit an interactive job, but that is usually most useful for debugging purposes. 


Batch Scripts
-------------

Batch jobs require a batch script that runs the commands and applications you want to execute. A batch script is essentially a shell script with added directives. Directives specify the resources requirements of your jobs and provide certain information to the scheduling system. The sbatch command is used to submit batch jobs.


.. code-block:: shell

    $ sbatch <options> <script>

Typical options include:

- The account to charge the run to 
- The number of nodes/tasls for the job
- The time limit for the job
- The location of stdout/stderr
- A name for the job

Job files usually have Slurm directives at the top. The directives are of the form:

.. code-block:: shell

    #SBATCH <options>
    #SBATCH <options>


These directives can be used instead of specifiying options on the command line. If an option is specified both as a directive and on the command line, the command line option takes precedence. 


Interactive Jobs
----------------

Individual compute nodes do not allow direct shell access except when the node is allocated to a job owned by you. If you need shell access to one or more nodes, you can request the scheduler assign some to you by launching an interactive batch job. 

Interactive jobs can be used for developing, testing, modifying, or debugging code--allowing for interactive access with a program as it runs. Requesting an interactive job will allocate resources and log you into a shell on a compute node. Interactive jobs are submitted with the ``salloc`` command. 

.. code-block:: shell

    $ salloc [options] [<command> [command args]]


When you run the salloc command, you won't get a prompt back until the batch system scheduler is able to run the job. Once that happens, the scheduler will drop you into a login session on the head node allocated to your interactive job. At this point, you will have a prompt and may run commands in this shell as needed. 


Batch Script Example
--------------------

.. code-block:: shell

    #!/bin/bash
    #
    # -- Request 16 cores
    #SBATCH --ntasks=16
    #
    # -- Specify a maximum wallclock of 4 hours 
    #SBATCH --time=4:00:00
    # 
    # -- Specify under which account a job should run
    #SBATCH --account=gfdl_x
    #
    # -- Set the name of the job, or Slurm will default to the name of the script
    #SBATCH --job-name=xyz
    #
    # -- Tell the batch system to set the working directory
    #SBATCH --chdir=/some/path/

    nt=$SLURM_NTASKS
    module load intel <version>

    srun -n $nt ./{executable} 

To submit the script above, called jobscript.sh, you would type:

.. code-block:: shell

    $ sbatch jobscript.sh
    


Job Submission Options
----------------------

Command-line options vs directives 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to specify sbatch options. The first is on the command line when using the sbatch command. 


.. code-block:: shell

    $ sbatch --clusters=c5 --account=abc123 myrunScript.sh
    

The second method is to insert directives at the top of the batch script using #SBATCH syntax. For example, 

.. code-block:: shell

    #SBATCH --clusters=c5
    #SBATCH --account=abc123


The two methods can be mixed together. However, options specified on the command line always override options specified in the script. 


The table below summarizes options for submitted jobs. Check the Slurm Man Pages for a more complete list. 

+------------------------+----------------------------+------------------------------+
|    Option              | Example Usage              | Description                  |
+========================+============================+==============================+
| ``-A`` ``--account``   | $SBATCH --account=abc123   | Specifies the project to     |
|                        |                            | which the job should be      |                          
+------------------------+----------------------------+------------------------------+
| ``-t`` ``--time``      | #SBATCH -t 4:00:00         | Specify a maximum wallclock. |
+------------------------+----------------------------+------------------------------+
| ``-J`` ``--job-name``  | #SBATCH -J jobname         | Set the name of the job.     |
+------------------------+----------------------------+------------------------------+
| ``-N`` ``--nodes``     | #SBATCH -N 1024            | Request that a minimum       |
|                        |                            | of X be allocated to a job   |
+------------------------+----------------------------+------------------------------+
| ``-n`` ``--ntasks``    | #SBATCH -n 8               | Requests for X tasks         | 
+------------------------+----------------------------+------------------------------+
| ``--mem``              | #SBATCH --mem=4g           | Specify the real memory      |
|                        |                            | required per node.           | 
+------------------------+----------------------------+------------------------------+
| ``-q`` ``--qos``       | #SBATCH --qos=normal       | Request a quality of service |
|                        |                            | for the job.                 |
+------------------------+----------------------------+------------------------------+
| ``-o`` ``--output``    | #SBATCH jobout.%j          | File where job STDOUT will   |
|                        |                            | be directed. (%j will be     |
|                        |                            | replaced with job ID)        |                        
+------------------------+----------------------------+------------------------------+
| ``-e`` ``--error``     | #SBATCH joberr.%j          | File where job STDERR will   |
|                        |                            | be directed. (%j will be     |
|                        |                            | replaced with the job ID)    |                    
+------------------------+----------------------------+------------------------------+
| ``--mail-user``        | #SBATCH --mail-            | Email address to be used for |
|                        |  user=user@somewhere.com   | notifications                |
|                        |                            |                              | 
+------------------------+----------------------------+------------------------------+
| ``-M`` ``--clusters``  | #SBATCH -M clustername     | clusters to issue commands to|
+------------------------+----------------------------+------------------------------+


Slurm Environment Variables
---------------------------

+--------------------------+----------------------------------------------------------------------------------+
| Variable                 | Description                                                                      |
+==========================+==================================================================================+
| $SLURM_SUBMIT_DIR        | The directory from which the batch job was submitted. By default, a new job      |
|                          | starts in your home directory. You can get back to the directory of job          |
|                          | submission with ``cd $SLURM_SUBMIT_DIR``. Note that this is not necessarily the  | 
|                          | same directory in which the batch script resides.                                |
|                          |                                                                                  |
+--------------------------+----------------------------------------------------------------------------------+
| $SLURM_JOBID             | The job's full identifier. A common use for $SLURM_JOBID is to append the job's  |
|                          | ID to the standard output and error files.                                       |
+--------------------------+----------------------------------------------------------------------------------+
| $SLURM_JOB_NUM_NODES     | The number of nodes requested.                                                   |
+--------------------------+----------------------------------------------------------------------------------+
| $SLURM_JOB_NAME          | The job name supplied by the user.                                               |
+--------------------------+----------------------------------------------------------------------------------+
| $SLURM_NODELIST          | The list of nodes assigned to the job.                                           |
+--------------------------+----------------------------------------------------------------------------------+


State Codes 
-----------
+--------------------------+----------------------------------------------------------------------------------+
| State Code               | Description                                                                      |
+==========================+==================================================================================+
| CA | Cancelled           | The job was explicitly cancelled by the user or system administrator             |
+--------------------------+----------------------------------------------------------------------------------+
| CD | Completed           | Job has terminated all processes on all nodes. Exit code of zero.                | 
+--------------------------+----------------------------------------------------------------------------------+
| F | Failed               | Job terminated with non-zero exit code or other failure condition.               |
+--------------------------+----------------------------------------------------------------------------------+
| R | Running              | Job currently has an allocation.                                                 |
+--------------------------+----------------------------------------------------------------------------------+
| TO | Timeout             | Job terminated upon reaching its time limit.                                     |
+--------------------------+----------------------------------------------------------------------------------+
| PD | Pending             | Job is awaiting resource allocation.                                             |
+--------------------------+----------------------------------------------------------------------------------+
| OOM | Out Of Memory      | Job experienced out of memory error.                                             |
+--------------------------+----------------------------------------------------------------------------------+
| NF | Node Fail           | The list of nodes assigned to the job.                                           |
+--------------------------+----------------------------------------------------------------------------------+

Job Reason Codes
----------------

+--------------------------+----------------------------------------------------------------------------------+
| Reason                   | Meaning                                                                          |
+==========================+==================================================================================+
| InvalidQOS               | The job's QOS is invalid.                                                        |
+--------------------------+----------------------------------------------------------------------------------+
| InvalidAccount           | The job's account is invalid                                                     |
+--------------------------+----------------------------------------------------------------------------------+
| NonZeroExitCode          | The job terminated with a non-zero exit code.                                    |
+--------------------------+----------------------------------------------------------------------------------+
| NodeDown                 | A node required by the job is down.                                              |
+--------------------------+----------------------------------------------------------------------------------+
| TimeLimit                | The job exhausted its time limit                                                 |
+--------------------------+----------------------------------------------------------------------------------+
| SystemFailure            | Failure of the Slurm system, a file system, the network, etc.                    |
+--------------------------+----------------------------------------------------------------------------------+
| JobLaunchFailure         | The job cannot be launched. This may be due to a file system problem, invalid    |
|                          | program name, etc.                                                               |
+--------------------------+----------------------------------------------------------------------------------+
| WaitingForScheduling     | The list of nodes assigned to the job.                                           |
+--------------------------+----------------------------------------------------------------------------------+


Job Dependencies
----------------
SLURM supports the ability to submit a job with constraints that will keep it running until these dependencies are met. A simple example is where job X cannot execute until job Y completes. Dependencies are specified with the ``-d`` option to Slurm. 

+----------------------------------+----------------------------------------------------------------------------------+
| Flag                             | Meaning                                                                          |
+==================================+==================================================================================+
|``SBATCH -d after:jobid[+time]``  | The job can start after the specified jobs start or are cancelled. The           |
|                                  | optional +time argument is a number of minutes. If specified, the job            |
|                                  | cannot start until that many minutes have passed since the listed jobs           |
|                                  | start/are cancelled. If not specified, there is no delay.                        |                
+----------------------------------+----------------------------------------------------------------------------------+
| ``SBATCH -d afterany:jobid``     | The job can start after the specified jobs have ended (regardless of exit state) |
+----------------------------------+----------------------------------------------------------------------------------+
| ``SBATCH -d afternotok:jobid``   | The job can start after the specified jobs terminate in a failed (non-zero) state|               
+----------------------------------+----------------------------------------------------------------------------------+
| ``SBATCH -d afterok:jobid``      | The job can start after the specified jobs complete successfully                 |
+----------------------------------+----------------------------------------------------------------------------------+
| ``SBATCH -d singleton``          | Job can begin after any previously-launched job with the same name and from the  |
|                                  | same user have completed. In other words, serialize the running jobs based on    |
|                                  | username+jobname pairs.                                                          |
+----------------------------------+----------------------------------------------------------------------------------+

Srun
----
Your C4/C5 job scripts will usually call ``srun`` to run an executable (or ``srun-multi`` if you have a multi-executable model).

.. code-block:: shell

    srun [OPTIONS... [executable [args...]]]

``srun`` accepts the following options:

+------------------------------------------------+----------------------------------------------------------------------------------+
| Option                                         | Description                                                                      |
+================================================+==================================================================================+
| ``-N``                                         | Number of nodes                                                                  |
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``-n``                                         | Total number of MPI tasks (default is 1)                                         | 
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``-c, --cpus-per-task=``                       | Logical cores per MPI task (default is 1)                                        |
|                                                | When used with ``--threads-per-core=1``:``c`` is equivalent to *physical* cores  |
|                                                | per task.                                                                        |
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``--threads-per-core=``                        | In task layout, use the specified maximum number of hardware threads per core.   |
|                                                | Must also be set in ``salloc`` or ``sbatch`` if using ``--threads--per-core=2``. |
+------------------------------------------------+----------------------------------------------------------------------------------+
|   ``--ntasks-per-node=``                       | If used without ``-n``: requests that a specific number of tasks be invoked on   |
|                                                | each node.                                                                       |
|                                                | If used with ``-n``: treated as a maximum count of tasks per node.               |
|                                                |                                                                                  |
+------------------------------------------------+----------------------------------------------------------------------------------+




Debugging
=========

Arm DDT
-------

Arm DDT is a powerful, easy-to-use graphical debugger. With Arm DDT it is possible to debug: 

- Single process and multithreaded software
- Parallel (MPI) Software 
- OpenMP
- Hybrid codes mixing paradigms such as MPI + OpenMP, or MPI + CUDA

Arm DDT supports:

- C, C++, and all derivatives of Fotran, including Fortran 90,
- Limited support for Python (CPython 2.7)
- Parallel languages/models including MPI, UPCm and fortran 2008 Co-arrays. 
- GPU languages such as HMPP, OpenMP Accelerators, CUDA and CUDA Fortran. 

Arm DDT helps you to find and fix problems on a single thread or across hundreds of thousands of threads. It includes static analysis to highlight potential code problems, integrated memory debugging to identify reads and writes that are outside of array bounds, and integration with MPI message queues. 

In addition to traditional debugging features, DDT also supports attaching to already-running processes and offline (non-interactive) debugging for long running jobs. 


Optimizing and Profiling
========================

Known Issues
============

Known Module Incompatibility on C5
----------------------------------

There is a known incompatibility with the cray-libsci module and the following intel modules: 

- intel-classic/2022.0.2
- intel-oneapi/2022.0.2

A recommended workaround to this issue is to either module unload cray-libsci or use another intel compiler. 

Executables from C3/C4 not working on C5
----------------------------------------

The C3/C4 and C5 nodes have different interconnects. The C3/C4 and C5 clusters are not binary compatible. Binaries compiled for C3/C4 will not execute on C5. Likewise, executables compiled for C5 will not run on C3/C4. Attempting to run an incompatible binary on C3, C4, or C5 will produce an error. 

Examples of the error are:

.. code-block:: shell

  Please verify that both the operating system and the processor support Intel(R) X87, CMOV, MMX, FXSAVE, SSE, SSE2, SSE3, SSSE3, SSE4_1, SSE4_2, MOVBE, POPCNT, AVX, F16C, FMA, BMI, LZCNT and AVX2 instructions.

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
