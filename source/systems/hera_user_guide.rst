.. _hera-user-guide:

***************
Hera User Guide
***************

.. image:: /images/Hera.jpg

About NESCC
===========

The NOAA Environmental Security Computing Center (NESCC), located in
Fairmont, West Virginia, is the location of NOAA's newest High
Performance Computing Data Center. This site provides computing
resources to support NOAA's research in long-range weather modeling
as well as its other environmental research areas.

There are currently two major systems at NESCC:

- Hera* A 760 Tflop Cray Compute Cluster high performance computing
  system.
- HPSS* A 50 Petabyte IBM/Oracle hierarchical storage management
  system.

In mid-year 2025 the Ursa system based on AMD 9654 with 2 DDN Lustre
file systems and a VAST file system is expected to be available.
In the first half of 2026 the Rhea system, based on AMD Turin is
expected to be available.

These `slides
<https://docs.google.com/presentation/d/1uFii6V18uaYMcA7WNKF3eAtn26LU4pcxp8uEqEdDPz0/edit#slide=id.g30820fabc4a_16_0>`_
present the schedule and configuration of Ursa and Rhea.


.. _hera-system-overview:

System Overview
===============

- Capacity of 3,270 trillion floating point operations per second – or
  3.27 petaFLOPS
- The Fine Grain Graphical Processing Units have a total capacity of
  2,000 trillion floating point operations per second, or 2.0
  petaFLOPS
- 45 million hours per month with 63,840 cores and a total scratch
  disk capacity of 18.5 Petabytes.

NESCC is also home to Niagara, a cloud-based computing resource. In
addition, Test and Development systems are available through NESCC for
system and application testing.

System Configuration
--------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * -
     - Hera TCA
     - Hera FGA
     - Juno TCA
     - Juno FGA
   * - CPU Type
     - Intel SkyLake
     - Intel Haswell
     - Intel SkyLake
     - Intel Haswell
   * - CPU Speed (GHz)
     - 2.40
     - 2.46
     - 2.40
     - 2.46
   * - Reg Compute Nodes
     - 1,328
     - 68
     - 14
     - 2
   * - Cores/Node
     - 40
     - 20
     - 40
     - 20
   * - Total Cores
     - 53,120
     - 2,000
     - 560
     - 40
   * - Memory/Core (GB)
     - 96
     - 256
     - 90
     - 256
   * - Peak FLOPS/Node
     - 12
     - N/A
     - 12
     - N/A
   * - Service Code Memory (GB)
     - 187
     - N/A
     - 187
     - N/A
   * - Total BigMem Nodes
     - 268
     - N/A
     - 268
     - N/A
   * - BigMem Node Memory (GB)
     - 384
     - N/A
     - 384
     - N/A
   * - CPU FLOPS (TFLOPS)
     - 2,672
     - 83.1
     - 28
     - 1.6
   * - GPUs/Node
     - N/A
     - 8 x P100
     - N/A
     - 8 x P100
   * - Total GPUs
     - N/A
     - 800
     - N/A
     - 16
   * - GPU FLOPS/GPU
     - N/A
     - 4.7
     - N/A
     - 4.7
   * - Interconnect
     - HDR-100 IB
     - FDR-10 (40 Gbps)
     - HDR-100
     - FDR-10 (40 Gbps)
   * - Total GPU FLOPS (TFLOPS)
     - N/A
     - 3,760
     - N/A
     - 75

.. note::

   - The Skylake 6148 CPU has two AVX-512 units and hence a
     theoretical peak of 32 double precision floating point operations
     per cycle with a base clock rate for floating point operations of
     1.6 GHz.
   - Total FLOPS is a measure of peak, and doesn’t necessarily
     represent actual performance.
   - Juno is the Test and Development System. Users must be granted
     specific access to the system for use.


Hera Partitions
===============

To specify a partition, use the command `partition -p`. For example:

.. code-block:: shell

   sbatch -p batch ...

The following partitions are defined for Hera:

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Partition
     - QOS Allowed
     - Billable TRes per Core Performance Factor
     - Description
   * - fge
     - gpu, gpuwf
     - 158
     - For jobs that require nodes with GPUs. See the Specifying QOS
       table below for more details. There are 100 Haswell nodes, each
       containing 8 P100 GPUs. Each P100 has 16GB of memory.
   * - hera
     - batch,windfall, debug, urgent
     - 165
     - General compute resource. **Default** if no partition is specified
   * - bigmem
     - batch,windfall, debug, urgent
     - 165
     - For large memory jobs; 268 nodes, each with 40 cores and 384 GB of memory
   * - novel
     - novel
     - 165
     - Partition to run novel or experimental jobs where nearly the full
       system is required.
       If you need to run a novel job, please submit a help ticket and tell us what
       you want to do. We will normally have to arrange for some time for the job to
       go through, and we would like to plan the process with you.
       Also, please note that if you use **novel partition** you also need to
       specify **novel QoS**.
   * - service
     - batch,windfall, debug, urgent
     - 0
     - Serial jobs (max 1 core), with a 24 hr limit. Jobs will be run on front
       end nodes that have external network connectivity. Useful for data
       transfers or access to external resources like databases. If your
       workflow requires pushing or pulling data to/from the HSMS(HPSS), it
       should be run there. See the Login (Front End) Node Usage Policy for
       important information about using Login nodes.

To see a list of available partitions use the command

.. code-block:: shell

   $ sinfo -O partition
   fge
   hera*
   service
   bigmem
   novel

An asterisk (*) indicates that default partition, where your job will be
submitted to if you do not specify a partition name at job submission.

**General compute jobs:** To assure the systems are used most efficiently,
specify the use of all general compute resource partitions. This allows the
batch scheduler to put your jobs on the first available resource.

Getting Help
------------

As with any Hera issue, open a :ref:`help request <getting_help>`.
