.. meta::
   :description: User guide for Hera, a NOAA RDHPCS system at NESCC with
    63,840 cores, supporting weather prediction and research workloads.
   :keywords: Hera, RDHPCS, NESCC, scratch, Slurm, weather prediction,
    Intel

.. _hera-user-guide:

***************
Hera User Guide
***************

.. image:: /images/Hera.jpg


System Overview
===============

- Capacity of 3,270 trillion floating point operations per second – or
  3.27 petaFLOPS
- 45 million hours per month with 63,840 cores and a total scratch
  disk capacity of 9.1 Petabytes.

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
     - Hera
   * - CPU Type
     - Intel SkyLake
   * - CPU Speed (GHz)
     - 2.40
   * - Reg Compute Nodes
     - 1,328
   * - Cores/Node
     - 40
   * - Total Cores
     - 63,840
   * - Memory/Core (GB)/Node
     - 96
   * - Peak FLOPS/Node
     - 12
   * - Service Code Memory (GB)
     - 187
   * - Total BigMem Nodes
     - 268
   * - BigMem Node Memory (GB)
     - 384
   * - CPU FLOPS (TFLOPS)
     - 2,672
   * - Interconnect
     - HDR-100 IB


.. note::

   - The Skylake 6148 CPU has two AVX-512 units and hence a
     theoretical peak of 32 double precision floating point operations
     per cycle with a base clock rate for floating point operations of
     1.6 GHz.
   - Total FLOPS is a measure of peak, and doesn't necessarily
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
   * - hera
     - batch,windfall, debug, urgent, long
     - 165
     - General compute resource. **Default** if no partition is specified
   * - bigmem
     - batch,windfall, debug, urgent, long
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
     - batch,windfall
     - 165
     - For jobs that require external network connectivity (including
       access to the HPSS archival system). Default of 1 core with
       a maximum of 4 cores and a maximum time limit of 24 hrs.
       Jobs will be run on front
       end nodes as those have external network connectivity. Useful for data
       transfers or access to external resources like databases. If your
       workflow requires pushing or pulling data to/from the HSMS(HPSS), it
       should be run there. See the Login (Front End) Node Usage Policy for
       important information about using Login nodes.

See the :ref:`Quality of Service (QOS) table <QOS-table>` for more information.

To see a list of available partitions use the command

.. code-block:: shell

   $ sinfo -O partition
   hera*
   service
   bigmem
   novel

An asterisk (*) indicates that default partition, where your job will be
submitted to if you do not specify a partition name at job submission.

**General compute jobs:** To assure the systems are used most efficiently,
specify the use of all general compute resource partitions. This allows the
batch scheduler to put your jobs on the first available resource.

File System Usage
=================

Hera file systems are shared with Ursa.
For information on the shared file systems available for Hera, see the
:ref:`High Performance File System <HPFS-scratch>` section
of the Ursa User Guide.

Software Stacks
===============

Software available on Hera is a subset of the software available on Ursa.
For information on the software stacks available for Hera,
see :ref:`Software Stacks <Ursa-Software-Stacks>` section of the
Ursa User Guide.