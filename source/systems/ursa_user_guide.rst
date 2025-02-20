.. _ursa-user-guide:

***************
Ursa User Guide
***************

.. image:: /images/Hera.jpg

The Ursa and Rhea systems are based at the NOAA Environmental Security
Computing Center (NESCC). Located in Fairmont, West Virginia, NESCC houses
NOAA's newest High Performance Computing Data Center. This site provides
computing resources to support NOAA's research in weather and atmospheric trend
modeling, as well as its other environmental research areas.

There are four major systems at NESCC:

- Ursa, based on AMD 9654 with DDN Lustre
- Rhea, based on AMD Turin with DDN Lustre & VAST File Systems.
- Hera, a 760 Tflop Cray Compute Cluster high performance computing
  system.
- HPSS, a 50 Petabyte IBM/Oracle hierarchical storage management
  system.


.. _ursa-system-overview:

Ursa System Overview
====================

- Capacity of 3,270 trillion floating point operations per second – or
  3.27 petaFLOPS
- The Fine Grain Graphical Processing Units have a total capacity of
  2,000 trillion floating point operations per second, or 2.0
  petaFLOPS
- 45 million hours per month with 63,840 cores and a total scratch
  disk capacity of 18.5 Petabytes.

System Configuration
--------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * -
     - Ursa
     - Rhea
   * - CPU Type
     - AMD Genoa 9654: 96 cores/12 channels to memory
     - AMD Turin 9655: 96 cores/12 channels to memory
   * - CPU Speed (GHz)
     - TBD
     - TBD
   * - Reg Compute Nodes
     - 634
     - 1380
   * - Cores/Node
     - 192
     - 192
   * - Total Cores
     - 121,728
     - 264,960
   * - Memory/Core (GB)
     - 96
     - 256
   * - Peak Performance
     - 4.77 petaFlops
     - 22 petaFlops
   * - Service Code Memory (GB)
     - 187
     - N/A
   * - CPU FLOPS (TFLOPS)
     - 2,672
     - 83.1
   * - Disk Space
     - >40 Petabytes
     - >100 Petabytes
   * - Maximum Performance
     - >330 gigabytes/second
     - >600 gigabytes/second
   * - GPU FLOPS/GPU
     - N/A
     - 4.7
   * - Interconnect
     - HDR-100 IB
     - FDR-10 (40 Gbps)
   * - Total GPU FLOPS (TFLOPS)
     - N/A
     - 3,760

The OS for both systems will be Rocky 9.

Ursa/Rhea Front Ends and Service Partition
------------------------------------------

Each system comes with 16 outward facing nodes.

4 nodes will be (front-end) login nodes:

* 768 cores total, for interactive use.
* ufe01-ufe04.
* Will handle cron as well.

12 nodes will comprise the service partition:

* 2,304 cores total.
* Available via Slurm.
* Target for all data transfer jobs.
* Target for scrontab jobs (Scrontab is the preferred method for
  recurring jobs).

One spare node, Uecflow01,  will be available for ecflow.  A similar
configuration will be used for the 16 outward facing nodes for Rhea.

Ursa Software stack
-------------------

* Ursa uses Slurm as the batch system.
* Spack is used to install software in /apps.
* Modules are used similarly to the MSU systems.
* An Intel stack is in place, and AMD and NVHPC stacks will be added.
* Ursa uses the most current versions of the compilers/libraries.

Rhea File Systems
-----------------

Rhea and Ursa will share file systems.  A new file system will be installed,
targeted at handling small files and small block I/O. It will be accessible to
Ursa and Rhea.

/scratch3 and /scratch4
^^^^^^^^^^^^^^^^^^^^^^^

* DDN Lustre.
* Upgraded with Rhea to ~60PB each.
* Initially mounted on Ursa, followed by Rhea.

/scratch5
^^^^^^^^^

* VAST (all flash file system).
* Delivered in support of Rhea at ~22PB.
* Targeted toward small files, small block I/O and ML/AI.


This file system will make use of `Darshan
<https://www.mcs.anl.gov/research/projects/darshan/>`_ a scalable HPC I/O
characterization tool. Darshan is designed to capture an accurate picture of
application I/O behavior, including properties such as patterns of access
within files, with minimum overhead.


Getting Help
------------

For any Ursa or Rhea issue, open a :ref:`help request <getting_help>`.
