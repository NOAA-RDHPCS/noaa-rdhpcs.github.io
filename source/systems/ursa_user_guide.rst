.. _ursa-user-guide:

***************
Ursa User Guide
***************

.. image:: /images/Ursa.png
   :scale: 45%

.. _ursa-system-overview:

Ursa System Overview
====================
Ursa is located at the NOAA Environmental Security Computing Center (NESCC), in
Fairmont, West Virginia.

Getting Started with Ursa
-------------------------
Log into your NOAA Google account, and you can view a
`slide presentation introducing Ursa
<https://docs.google.com/presentation/d/1Miz_d5-atesgbfQhVk7LAWFNiveWwyDQFz3XZ4dfXLg/edit?pli=1&slide=id.p#slide=id.p>`_.
Log into your NOAA Google account, and you can also review
a `recorded version of the presentation
<https://drive.google.com/file/d/15-C4Zs_oMxUQ2_QqPm-9CkxPkeK46q56/view>`_.

Ursa System Configuration
=========================

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

Ursa Partitions
---------------

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
     - Serial jobs (max 4 cores), with a 24 hr limit. Jobs will be run on
       service nodes that have external network connectivity. Useful
       for data transfers or access to external resources like databases.
       If your workflow requires pushing or pulling data to/from
       the HSMS(HPSS), it should be run there. This partition
       is also a good choice for doing your compilations and
       builds of your applications and libraries rather than
       doing it on the login nodes.

See the :ref:`Quality of Service (QOS) table <QOS-table>` for more information.

Ursa Node Sharing
-----------------

Jobs requesting less than 192 cores or the equivalent amount
of memory will share the node with other jobs.

With the Ursa ``u1-compute`` partition:

* If you request 1-191 cores for your job
  you will be allocated and charged for the greater of
  the number of cores requested or the amount of memory
  requested in GB divided by 2.
* If you request 192 or greater cores you will be given and charged for whole
  nodes, in multiples of 192 cores. (ex. Request - 193, charged for 384 cores)

Ursa Front Ends and Service Partition
---------------------------------------
Ursa has 15 outward-facing nodes.

* 4 nodes will be (front-end) login/cron nodes interactive use:
    * ``ufe01-ufe04``, total of 768 cores for interactive use.
      See the `Login (Front End) Node Usage Policy <https://docs.rdhpcs.noaa.gov/queue_policy/policies.html#login-node-usage>`_ for important information about using Login nodes.
* 10 nodes will comprise the service partition:
    * 3,840 cores total.
    * Available via Slurm.
    * Target for compilation and data transfer jobs.
    * Target for scrontab jobs (Scrontab is preferred for recurring jobs).
* 1 node is available for ecflow
    * ``uecflow01``

Using GPU Resources on Ursa
===========================
Ursa has 2 H100 GPUs each with 94GB of memory in the ``u1-h100``
partition as indicated in the table above.  This partition
is only accessible from the ``gpu`` and ``gpuwf`` QOSes.

In order to have priority access to the GPU resources you will need to
have a GPU specific project allocation. Please contact your PI
or Portfolio Manager for getting a GPU specific allocation.

All projects with a CPU project allocation on Ursa have
windfall access to the GPU resources, and conversely all users with
GPU specific project allocations have windfall access
to the non-GPU resources.

Using GPU Resources With a GPU allocation
-----------------------------------------

If you have a GPU specific project allocation on Ursa you
can access the GPUs by
submitting to the ``u1-h100`` partition and ``gpu`` QOS as shown in
the example below where 2 H100 GPUs on 1 node are being requested:

.. code-block:: shell

   sbatch -A mygpu_project -p u1-h100 -q gpu -N 1 --gres=gpu:h100:2 my_ml.job

Using GPU Resources Without a GPU allocation
--------------------------------------------

Users that do not have GPU specific project allocations
on Ursa can access
the GPU resources at windfall priority. Which means users will be able
to submit jobs to the system, but they will only run when the
resources are not being used by projects that do have a GPU
specific project allocation.
This is helpful for users who are in interested in
exploring the GPU resources for their applications. To use the system
in this mode please submit the jobs to the ``u1-h100`` partition and
``gpuwf``
QOS as shown in the example below where 2 H100 GPUs on 1 node are
being requested:

.. code-block:: shell

   sbatch -A mycpu_project -p u1-h100 -q gpuwf -N 1 --gres=gpu:h100:2 my_ml.job


Using the Exploratory GPU Resources
===================================

In addition to the NVIDIA H100 GPU system (Partition: ``u1-h100``),
two new small GPU exploratory systems with the newer GPU types
are available for experimentation.  These systems are connected
to the Ursa IB network and have access to the Ursa file systems.
All projects with access to Ursa have equal access to the
new Exploratory Systems via the ``gpuwf`` QOS.

To access these nodes, login to Ursa and submit an interactive
batch job requesting these GPU resources. Once you have an interactive
shell, you can compile and run your applications on those nodes.
Vendor provided software is available by loading the appropriate
modules. Please run the ``module spider`` command to see the list
of modules available.

Description of the two exploratory systems:

* Partition:  ``u1-gh``. Eight Grace Hopper nodes with one
  NVIDIA GH200 Grace Hopper Superchip with NVIDIA software.
  These nodes have a single NDR200 connection to Ursa
  IB fabric.  More detailed information about
  the `NVIDIA GH200 <https://resources.nvidia.com/en-us-data-center-overview-mc/en-us-data-center-overview/grace-hopper-superchip-datasheet-partner>`_
  is available from NVIDIA.

* Partition:  ``u1-mi300x``. Three dual-Intel CPU sockets
  with 8 AMD Mi300x APUs nodes with AMD ROCm software.
  These nodes have a single NDR200 connection to the
  Ursa IB fabric. Click `AMD MI300X <https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html>`_
  for more detailed information.

Run one of the following commands to get interactive access to these nodes:

.. code-block:: shell

  salloc -A mygpu_project -t 480 -p u1-gh     -q gpuwf -N 1 --gres=gpu:gh200:1
  salloc -A mygpu_project -t 480 -p u1-mi300x -q gpuwf -N 1 --gres=gpu:mi300x:2

In the examples above, the first example requests one node
with one GH200 GPU and the second example requests one node with
two MI300X GPUs.

Ursa Software Stack
===================

* Ursa OS is Rocky 9.4, similar to MSU systems (Rocky 9.1)
  whereas Hera/Jet are Rocky 8.
* Module layout is more akin to what you see on MSU
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

Ursa HPFS File Systems
======================

Ursa has the following three High Performance File Systems (HPFS) available:
``/scratch[3,4,5]``.

.. note::
    ``/scratch5`` is only available on Ursa.

.. caution::
   Please note that the HPFS scratch file systems are **NOT** backed up!

The ``/scratch[3,4]`` file systems are Lustre file systems with project
based disk space quotas for routine work.

The ``/scratch5`` file system is a new VAST file system, which offers
different technology from the ``/scratch[3,4]`` Lustre file systems.
Below are some technical insights regarding the new Vast file system.

* This is an all-flash filesystem designed to perform well for a variety
  of workloads and files of varying size.
* VAST offers unique data cataloging abilities that can be used
  with HDF and NetCDF file formats. This should help to create
  new streamlined and efficient analysis pipelines.

The VAST file system is significantly more expensive per PB than
the Lustre file systems, and we currently do not know what
the performance implications of this file system are as opposed
to the Lustre file system on your applications.
Therefore, currently only two
projects, ``rstprod`` and ``public``, have project based quotas
on the VAST file system.  However, all other Ursa projects and
users may utilize ``/scratch5``, via the purged directory,
``/scratch5/purged``.

.. warning::

   **This directory will be purged of all files that have not
   been accessed in the past 30 days**. Depending on usage we
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

Getting Help
=============

For any Ursa or Rhea issue, open a :ref:`help request <getting_help>`.
