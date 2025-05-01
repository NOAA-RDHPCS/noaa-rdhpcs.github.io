.. _ursa-user-guide:

***************
Ursa User Guide
***************
.. _ursa-system-overview:

Ursa System Overview
====================
Ursa is located at the `NOAA Environmental Security Computing Center (NESCC) <https://docs.rdhpcs.noaa.gov/systems/common.html#locations-and-systems-of-the-rdhpcs>`_, located in Fairmont, West Virginia.

Ursa System Configuration
-------------------------

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
--------------------
See the :ref:`QOS partition table <QOS-table>` for more information.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Partition
     - QOS Allowed
     - Billing TRES Factor
     - Description
   * - u1
     - batch,windfall, debug, urgent
     - 100
     - General compute resource. **Default** if no partition is specified.
   * - u1-h100
     - gpu, gpuwf
     - 100
     - For jobs that require nodes with GPUs. See the `QOS table <https://docs.rdhpcs.noaa.gov/queue_policy/policies.html#queue-policy>`_ for more details.
   * - u1-service
     - batch, windfall
     - 100
     - Serial jobs (max 4 cores), with a 24 hr limit. Jobs will be run on service nodes that have external network connectivity. Useful for data transfers or access to external resources like databases.
       If your workflow requires pushing or pulling data to/from the HSMS(HPSS), it should be run there.

Ursa Node Sharing
--------------------------
With the Ursa u1 partition:

* If you request 1-192 cores you will be given and charged for the number of
  cores you request.
* If you request 193 or greater cores you will be given and charged for whole
  nodes, in multiples of 192 cores. (ex. Request - 193, charged for 384 cores)


Ursa Front Ends and Service Partition
---------------------------------------
Ursa has 15 outward-facing nodes.

* 4 nodes will be (front-end) login/cron nodes interactive use:
    * ufe01-ufe04, total of 768 cores for interactive use.
      See the `Login (Front End) Node Usage Policy <https://docs.rdhpcs.noaa.gov/queue_policy/policies.html#login-node-usage>`_ for important information about using Login nodes.
* 10 nodes will comprise the service partition:
    * 3,840 cores total.
    * Available via Slurm.
    * Target for compilation and data transfer jobs.
    * Target for scrontab jobs (Scrontab is preferred for recurring jobs).
* 1 node is available for ecflow
    * uecflow01

Ursa Software Stack
-------------------------
* Ursa uses Slurm as the batch system.
* Spack is used to install software in /apps.
* Modules are used similarly to the MSU systems.
* An Intel stack is in place, and AMD and NVHPC stacks will be added.
* Ursa uses the most current versions of the compilers/libraries.

Ursa File Systems
------------------------
Ursa and Hera will share 2 new file systems, /scratch3 and /scratch4,
that will replace Hera’s /scratch1 and /scratch2.

/scratch3 and /scratch4
------------------------
* DDN Lustre, each file system: >50 PB, > 500 GB/s
* Mounted on Ursa and Hera

Getting Help
------------

For any Ursa or Rhea issue, open a :ref:`help request <getting_help>`.
