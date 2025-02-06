.. _ursa-user-guide:

***************
Ursa User Guide
***************

.. image:: /images/Hera.jpg

About NESCC
===========

The NOAA Environmental Security Computing Center (NESCC), located in
Fairmont, West Virginia, is the location of NOAA's newest High
Performance Computing Data Center. This site provides computing
resources to support NOAA's research in Weather and Climate modeling
as well as its other environmental research areas.

There are four major systems at NESCC:

- Ursa* based  on AMD 9654 with DDN Lustre
- Rhea* based on AMD Turin with DDN Lustre & VAST File Systems.
- Hera* A 760 Tflop Cray Compute Cluster high performance computing
  system.
- HPSS* A 50 Petabyte IBM/Oracle hierarchical storage management
  system.

This guide discusses the Ursa System and Rhea file system.

System Overview
===============

The Ursa system is composed of 634 nodes, with 2x AMD 9654 (Genoa) chips per
node.

* 634 Nodes (384GB/node)
* 192 cores/node totaling 121,728 cores
* A subset of 58 nodes with 2x H100 GPUs
* AMD Genoa 9654: 96 cores/12 channels to memory
* AKA Zen 4
* Two sockets/node
* Infiniband NDR200
* DDN/Lustre ~40PB, >330GB/s
* Two file systems (/scratch3 & /scratch4)


The Ursa system has a a peak CPU performance of
4.77 petaflops, with a total memory of 243 terabytes (384 gigabytes/node). In
addition to the CPUs,  58 nodes will have 2x NVIDIA H100 GPUs per node with
94GB memory per GPU. This is a total number of 116 GPUs, which will provide
an additional 3.5 (=0.030*116) petaflops of performance.

The disk space will be
over 40 petabytes, with a maximum performance of over 330 gigabytes/second (DDN
Lustre).

The Rhea system will be composed of 1,380 nodes (2x AMD Turin chips per node,
192 cores/node totaling 264,960 cores) with a peak CPU performance of 22
petaflops with a total memory of 1,060 terabytes (768 gigabytes/node). In
addition to the CPUs, 138 nodes will have 2x NVIDIA H100 GPUs per node with
94GB memory per GPU). This is a total number of GPUs of 276, providing
an additional 8.3 (=276*0.030) petaflops of performance.

The disk space will be over 100 petabytes, with a maximum performance of over
600 gigabytes/second (DDN Lustre + a small VAST appliance).

The OS for both systems will be Rocky 9.

Old Hera System Overview
========================

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

System Configuration for Hera
-----------------------------

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
     - 100
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
   - The nodes with GPUs are the same as what was on Theia; But the
     network has been upgraded to EDR.

Partitions
----------

Lustre File Systems
-------------------

