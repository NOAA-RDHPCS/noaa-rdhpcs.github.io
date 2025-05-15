.. _ursa-user-guide:

***************
Ursa User Guide
***************
.. _ursa-system-overview:

Ursa System Overview
====================
Ursa is located at the :ref:`NOAA Environmental Security Computing
Center (NESCC) <locations-of-rdhpcs>`, located in Fairmont, West
Virginia.

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
     - batch,windfall, debug, urgent
     - 100
     - General compute resource. **Default** if no partition is specified.
   * - u1-h100
     - gpu, gpuwf
     - 100
     - For jobs that require nodes with GPUs.
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
--------------------------
With the Ursa u1 partition:

* If you request 1-192 cores for your job
  you will be allocated and charged for the greater of
  the number of cores requested or the amount of memory
  requested divided by 2.
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

   sbatch -A mygpu_project -p u1-h100 -q gpu -N 1 –gres=gpu:h100:2 my_ml.job

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

   sbatch -A mycpu_project -p u1-h100 -q gpuwf -N 1 –gres=gpu:h100:2 my_ml.job


Ursa Software Stack
-------------------
* Ursa uses Slurm as the batch system.
* Spack is used to install software in /apps.
* Modules are used similarly to the MSU systems.
* An Intel stack is in place, and NVHPC stacks will be added.
  AMD compiler AOCC is also available.
* The following MPI implementations are available: HPC-X
  from Nvidia and Intel-oneapi-MPI from Intel.
  We have seen much better performance using the
  HPC-X MPI and would recommend as the first choice
  for this system.
* Ursa uses the most current versions of the compilers/libraries.

Ursa File Systems
-----------------
Ursa and Hera will share 2 new file systems, /scratch3 and /scratch4,
that will replace Hera’s /scratch1 and /scratch2.

/scratch3 and /scratch4
------------------------
* DDN Lustre, each file system: >50 PB, > 500 GB/s
* Mounted on Ursa and Hera

Cron and Scrontab Services
--------------------------
On Ursa both ``cron`` and ``scrontab`` services are available.
We strongly recommend using ``scrontab`` instead of ``cron``
whenever possible.  For information on how to use ``scrontab``
please see :ref:`scrontab <rdhpcs_scrontab>`.

Getting Help
------------

For any Ursa or Rhea issue, open a :ref:`help request <getting_help>`.
