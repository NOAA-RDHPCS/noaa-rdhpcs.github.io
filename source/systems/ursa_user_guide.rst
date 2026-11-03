.. meta::
   :description: User guide for Ursa, a NOAA RDHPCS system at NESCC in
    Fairmont, West Virginia, featuring AMD Genoa CPUs and GPU nodes for
    weather prediction workloads.
   :keywords: Ursa, RDHPCS, NESCC, AMD Genoa, GPU, Slurm, weather prediction,
    Fairmont, West Virginia

.. _ursa-user-guide:

***************
Ursa User Guide
***************

.. image:: /images/Ursa.png
   :scale: 45%

.. _ursa-system-overview:

System Overview
===============

Ursa is located at the NOAA Environmental Security Computing Center (NESCC), in
Fairmont, West Virginia.
Ursa is a high performance computing system designed to support NOAA's
weather prediction workloads. It features AMD Genoa CPUs and GPU nodes,
which are connected to the same high performance file systems as
the Hera system at NESCC.

See `:ref:Getting Started <ursa-intro>` for a slide presentation and
recorded overview of the system.

System Configuration
====================

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * -
     - Compute System
     - GPU System
   * - CPU Type
     - AMD Genoa 9654: 96 cores/12 channels to memory
     - AMD Genoa 9654: 96 cores/12 channels to memory
   * - CPU Speed (GHz)
     - 2.4 GHz
     - 2.4 GHz
   * - Compute Nodes
     - 576
     - 58
   * - Cores/Node
     - 192
     - 192
   * - Total Cores
     - 110,592
     - 11,136
   * - Memory/Core (GB)
     - 2
     - 2
   * - OS
     - Rocky 9
     - Rocky 9
   * - CPU Peak Performance
     - 4.25 PFlops
     - 0.43 PFlops
   * - Interconnect
     - NDR-200 IB
     - NDR-200 IB
   * - Total Disk Capacity
     - >100 PB, (shared with Hera)
     - >100 PB, (shared with Hera)
   * - Total Ave Disk Performance
     - >1000 GB/s
     - >1000 GB/s
   * - GPU Type
     - N/A
     - NVIDIA H100-NVL
   * - GPU's/node
     - N/A
     - 2
   * - Memory/GPU (GB)
     - N/A
     - 94
   * - Total GPU FLOPS (TFLOPS)
     - N/A
     - 3.48 PFlops

Partitions
----------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Partition
     - QOS Allowed
     - Billing TRES Factor
     - Description
   * - u1-compute
     - batch,windfall, debug, urgent, long
     - 100
     - General compute resource. **Default** if no partition is specified.
   * - u1-h100
     - gpu, gpuwf
     - 100
     - For jobs that require nodes with the Nvidia H-100 GPUs.
   * - u1-gh
     - gpuwf
     - 100
     - For jobs that require nodes with the Nvidia Grace-Hopper processors.
   * - u1-mi300x
     - gpuwf
     - 100
     - For jobs that require nodes with the AMD MI300X GPUs.
   * - u1-service
     - batch, windfall
     - 100
     - Serial jobs (max 64 cores and/or 250 GB of memory per user),
       with a 24 hr wall time limit. Jobs will be run on
       service nodes that have external network connectivity. Useful
       for data transfers or access to external resources like databases.
       If your workflow requires pushing or pulling data to/from
       the HSMS(HPSS), it should be run there. This partition
       is also a good choice for doing your compilations and
       builds of your applications and libraries rather than
       doing it on the login nodes.

See the :ref:`Quality of Service (QOS) table <QOS-table>` for more information.

Node Sharing
------------

As of 6/18/26, node sharing has been enabled for all job sizes, unless you use
the ``--exclusive`` option when you submit your job.

For more information on this ``sbatch`` option, refer to the
`Slurm documentation <https://slurm.schedmd.com/sbatch.html>`_.

Front Ends and Service Partition
--------------------------------

Ursa has 15 outward-facing nodes.

* 4 nodes will be (front-end) login/cron nodes interactive use:
    * ``ufe01-ufe04``, total of 768 cores for interactive use.
      See :ref:`Login Node Usage <login_node_usage>` for important information
      about using Login nodes.
* 10 nodes will comprise the service partition:
    * 3,840 cores total.
    * Available via Slurm.
    * Target for compilation and data transfer jobs.
    * Target for scrontab jobs (Scrontab is preferred for recurring jobs).
* 1 node is available for ecflow
    * ``uecflow01``

Using GPU Resources on Ursa
===========================
Ursa has one production GPU partition (``u1-h100``) and two
exploratory GPU
partitions (``u1-gh`` and ``u1-mi300x``). See the table above for
details.

Partition ``u1-h100``:  There are 58 nodes, each with 192 AMD cpu
cores, 2 NVIDIA  H100 GPUs with 94GB of memory/GPU.  This partition is
accessible from the ``gpu`` and ``gpuwf`` QOS’s. For billing and accounting:
one H100 gpu-hour will count as 192/2=96 cpu core-hours.

In order to have priority access to the H100 GPU resources you will
need a GPU specific project allocation. Please contact your
PI or Portfolio Manager to get a GPU specific allocation.

All projects with a CPU project allocation on Ursa have windfall
access to the H100 GPU resources, and conversely all users with
GPU specific project allocations have windfall access to the
non-GPU resources.

Using H100 GPU Resources With a GPU allocation
----------------------------------------------

If you have a H100 GPU specific project allocation on Ursa, you can access
the H100 GPUs by submitting to the ``u1-h100`` partition and ``gpu`` QOS as
shown in the example below where 3 H100 GPUs are being requested:

.. code-block:: shell

   sbatch -A mygpu_project -p u1-h100 -q gpu --gpus=h100:3 my_ml.job

Using H100 GPU Resources Without a GPU allocation
-------------------------------------------------

Users that do not have H100 GPU specific project allocations on Ursa
can access the H100 GPU resources at windfall priority. This means
that users can submit jobs to the system, but they will only run
when the resources are not being used by projects that do have a H100
GPU specific project allocation. This is helpful for users who are
interested in exploring the GPU resources for their applications.
To use the system in this mode please submit the jobs to the ``u1-h100``
partition and ``gpuwf`` QOS as shown in the example below where 2 H100
GPUs are being requested:

.. code-block:: shell

   sbatch -A mycpu_project -p u1-h100 -q gpuwf --gpus=h100:2 my_ml.job


Using the Exploratory GPU Resources
===================================

In addition to the NVIDIA H100 GPU system (Partition: ``u1-h100``), two new
small GPU exploratory systems (partitions) with the newer GPU types are
available for experimentation. These systems are connected to the Ursa
IB network and have access to the Ursa file systems. There are no
allocations or fairshare priority for these partitions; therefore all
projects with access to Ursa have equal access (first come first served)
to these partitions via the ``gpuwf`` QOS.

To access these nodes, login to Ursa and submit an interactive
batch job requesting these GPU resources. Once you have an interactive
shell, you can compile and run your applications on those nodes.
Please keep in mind that the CPUs on the exploratory GPU resources
are different from the CPUs in the production system.
Vendor provided software is available by loading the appropriate
modules. Please run the ``module spider`` command to see the list
of modules available.

Description of the two exploratory systems:

* Partition:  ``u1-gh``: There are 8 Grace Hopper nodes, each with
  one NVIDIA GH200 Grace Hopper Superchip with NVIDIA software.
  The CPU part of this superchip is an ARM processor with 72 cpu
  cores and approximately 213 GB of RAM. Click
  the `NVIDIA GH200 <https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/>`_
  for more detailed information.
  For billing and accounting: one grace hopper gpu-hour will count
  as 72 cpu core-hours.

* Partition:  ``u1-mi300x``. There are 5 nodes, each with 96 Intel cpu
  cores, 8 AMD Mi300x APUs each with 192 GB of RAM AMD ROCm software.
  Click `AMD MI300X <https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html>`_
  for more detailed information.
  For billing and accounting: one mi300x gpu-hour will count as
  96/8=12 cpu core-hours.

Run one of the following commands to get interactive access to these nodes:

.. code-block:: shell

  salloc -A mygpu_project -t 480 -p u1-gh     -q gpuwf --gpus=gh200:1
  salloc -A mygpu_project -t 480 -p u1-mi300x -q gpuwf --gpus=mi300x:2

In the examples above, the first example requests one node
with one GH200 GPU and the second example requests one node with
two MI300X GPUs.

.. _HPFS-scratch:

HPFS File Systems
=================

Ursa has the following three High Performance File Systems (HPFS) available:
``/scratch[3,4,5]``.

.. caution::
   Please note that the HPFS scratch file systems are **NOT** backed up!

The ``/scratch[3,4]`` file systems are Lustre file systems with project
based disk space quotas for routine work.

The ``/scratch5`` file system is a new VAST file system, which offers
different technology from the ``/scratch[3,4]`` Lustre file systems.
This is an all-flash filesystem designed to perform well for a variety
of workloads and files of varying size.

The VAST file system is significantly more expensive per PB than
the Lustre file systems, and we currently do not know what
the performance implications of this file system are as opposed
to the Lustre file system on your applications.
Therefore, currently only two
projects, ``rstprod`` and ``public``, have project based quotas
on the VAST file system.  However, all other Ursa projects and
users may explore the suitability of this new file system
for your applications via the purged directory,
``/scratch5/purged``.

.. warning::

   **This directory will be purged of all files that have not
   been accessed in the past 90 days**. Depending on usage we
   will adjust the purge schedule as needed, preceded by a user
   notification. Users under the ``/purged`` directory have a quota
   of **250 TB**.

If you want to use ``/scratch5``,  create and use a single
sub-directory under the ``/purged`` directory
(``/scratch5/purged/$USER``), with the directory name the
same as the First.Last of your NOAA email.

Since ``/scratch5`` is a new and different technology from our
previous Lustre file systems, the RDHPCS program would appreciate
insight into your experiences with it. In particular, we would
like to know how performance has been affected (both positively
or negatively) and how stable and consistent the file system
is for your applications. Please send this information via
an RDHPCS Ursa help ticket with the subject of ``/scratch5``
performance results.

If the performance of your application suite is significantly
improved using the VAST File system vs the Lustre file systems
and you would like your project to have non-purged quota project
space on ``/scratch5``, please have your Portfolio Manager
submit a request via a RDHPCS Ursa Help ticket. Include the amount
of disk space you require and a detailed justification, including
a performance comparison for your application suite between
``/scratch[3,4]`` and ``/scratch5``.

Usage/Quota information for ``/scratch[3,4]`` file systems
----------------------------------------------------------

The new file systems ``/scratch[3,4]`` on
Ursa and Hera have a performance improving feature called
“Hot Pools”.  With Hot Pools, the first 1 GB of each file is written
to the fast SSD (hot) tier, by default. After some time, usually
10 to 15 minutes, the file is mirrored to the slower HDD (cold) tier
and will be double counted as usage toward your quota. As long as the
file is actively used, it will stay on both tiers (hot and cold). Unused
files are removed from the hot tier and reside only on the cold tier.

**As a result the reported usage for the first 1 GB of
active files may be doubled.**

Cron and Scrontab Services
==========================

On Ursa both ``cron`` and ``scrontab`` services are available.
We strongly recommend using ``scrontab`` instead of ``cron``
whenever possible.  For information on how to use ``scrontab``
please see :ref:`scrontab <rdhpcs_scrontab>`.

.. _Ursa-Software-Stacks:

Software Stack
==============

* Ursa OS is Rocky 9.4, similar to MSU systems (Rocky 9.1)
* Module layout is akin to what you see on MSU
  systems; installed using spack.

  * Please run the ``module spider`` command to see all
    the available modules!

* Compilers: Intel's oneapi, Nvidia's nvhpc, and
  AMD's AOCC compilers are available.
* MPIs: Intel MPI from Intel, HPC-X MPI from Nvidia, and openMPI
  implementations are available.

  * We have seen much better performance and stability with
    HPC-X in our testing of communication intensive benchmarks
    as it is optimized to take advantage of the NDR-200 IB
    network more effectively.

* An Intel stack is in place. Other stacks will be
  considered if requested.


.. meta::
   :description: Overview of available compilers and MPI stacks on RDHPCS
    systems, including Intel and NVIDIA compilers with Intel MPI,
    and how to load and use them.
   :keywords: compilers, Intel, MPI, Intel MPI, NVIDIA, Fortran,
    C, C++, parallel, HPC, HPC-X

.. _compilers:

Compilers and MPI Stacks
========================

The following compilers and MPI stacks are available on RDHPCS systems:

* Compilers: Intel oneapi compilers, NVIDIA compilers from NVIDIA HPC SDK
  (nvhpc), GNU compilers
* MPI stacks: Intel oneapi MPI, HPCX-MPI (LTS), HPCX-MPI from NVIDIA
  HPC SDK (nvhpc)

Using the Intel oneapi compilers with Intel oneapi MPI
------------------------------------------------------

To see the available modules, run the  command
``module spider intel-oneapi-mpi intel-oneapi-mpi``,
which will print a list of available Intel compiler and Intel MPI modules.

Load the desired version of the module files as follows:

.. code-block:: shell

    module load intel-oneapi-compilers/<version> intel-oneapi-mpi/<version>

Then use the following commands/wrappers to compile your applications.

For non-MPI applications, use the following commands:

.. code-block:: shell

    ifx: for non-MPI Fortran applications
    icx: for non-MPI C/C++ applications


For MPI applications, use the following commands/wrappers:

.. code-block:: shell

    mpiicx: for C/C++ MPI applications
    mpiifx: for Fortran MPI applications
    mpif90 -fc=ifx:  for Fortran MPI applications


Use the man pages, or the ``--help`` option on these commands, to get more
detailed information about the options available with those commands.

Recommended Intel Compiler Options for Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following options are a starting point to optimize code. Users
should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell

   -O3 -xHOST -ip   -align array64byte
   -O3 -qopt-zmm-usage=high -axCORE-AVX512  -align array64byte -ip      # For Skylake processors (Hera)

.. note::

   Using the AVX-512 instructions may or may not improve performance. We
   recommended that you experiment with and without these options and use the
   one that performs the best.


Compiling for reproducible results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some applications may need to use the ``-fp-model`` option to obtain consistent
arithmetic results across core counts. This option better controls the order of
execution and may affect performance. See ``man ifx``; for additional
information.

.. code-block:: shell

   -fp-model strict
   -fp-model precise


Recommended Intel compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code. The
``-gen-interfaces`` can also be useful for finding errors.

.. code-block:: shell

   -O0 -g -traceback -check all -fpe0

Thread-safe compilation
^^^^^^^^^^^^^^^^^^^^^^^

If thread-safe compilation is desired, be sure to use one of the following
options (this is an issue with only Intel Fortran compiler):

.. code-block:: shell

   -qopenmp (if the source file has OpenMP directives that need to be honored)
   -recursive    # or -auto (these two are equivalent)


Other potentially useful Intel compiler options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your code has very large arrays you may see an error of the type:

.. code-block:: shell

   : relocation truncated to fit: R_X86_64_PC32 out_fem


This usually indicates very large arrays (>2GB of data section). In these
situations you will have to compile the application with the flag:

``-mcmodel=medium -static-intel``

If you use this option, keep in mind that al l dependent libraries must also be
compiled, either with this option or with ``-fpic`` option.

Run the command: ``ifx --help`` to see all the available options.

Using the NVIDIA compilers
--------------------------

The NVIDIA compilers are available on Ursa only.
To see the available versions of the NVIDIA HPC compilers, use the
command ``module spider nvhpc``.

You need to load a module for a specific version of the compiler before you
can use that compiler: ``module load nvhpc/<version>``. Loading this module
also loads the necessary libraries and environment variables for the NVIDIA
compilers and HPCX-MPI that is provided by NVIDIA.

Then use the following commands/wrappers for compiling your applications.

For non-MPI applications:

.. code-block:: shell

   nvfortran - for Fortran sources
   nvc       - for C sources
   nvcc      - for Cuda C sources
   nvc++     - for C++ sources

For MPI applications:

.. code-block:: shell

   mpif90  - for Fortran 90 MPI sources
   mpic    - for C MPI sources
   mpicc   - for Cuda C MPI sources
   mpic++  - for C++ MPI sources

Documentation on NVIDIA compiler options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The man pages are the best resource for documentation on compiler options.
After you've loaded the modules as instructed above, run

.. code-block:: shell

   man nvfortran
   man nvcc


NVIDIA compiler options for optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for optimizing code.
Users should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell


   -O3 -fastsse -tp=sandybridge,ivybridge,haswell,skylake


NVIDIA compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code.

.. code-block:: shell

   -O0 -g -traceback -Mbounds -Mchkfpstk -Mchkptr -Mchkstk

Using the HPCX-MPI MPI implementation
-------------------------------------

The HPCX-MPI implementation is available on Ursa for use with
GNU and Intel compilers. To see the available versions of the
HPCX-MPI implementation, use the command
``module spider hpcx-mpi``.

Once the module is loaded, use the following commands/wrappers for
compiling your applications.

.. code-block:: shell

   mpif90  - for Fortran 90 MPI sources
   mpic++  - for C and C++ MPI sources


.. _ursa-intro:

Getting Started with Ursa
=========================

The Ursa system was introduced to the NOAA community in a
presentation on June 20, 2024. You can review the `
`slide presentation that introduced Ursa,
<https://docs.google.com/presentation/d/1Miz_d5-atesgbfQhVk7LAWFNiveWwyDQFz3XZ4dfXLg/edit?pli=1&slide=id.p#slide=id.p>`_,
or watch a `recorded version of the presentation
<https://drive.google.com/file/d/15-C4Zs_oMxUQ2_QqPm-9CkxPkeK46q56/view>`_

Getting Help
=============

Open a :ref:`help request <getting_help>` for any Ursa issue.
