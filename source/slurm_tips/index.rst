.. _slurm:

##########
SLURM Tips
##########

Please be aware that Gaea is not like a usual Slurm cluster.  Slurm expects that
all nodes are homogeneous and capable of being used for any purpose.  Gaea is a
heterogeneous set of clusters (hence the need to specify a cluster as shown
below.)  This also means that partitions (queues) for resources with different
purposes will need to set up your job's environment to provide access to the
software for that purpose.(data transfer nodes being chief among these.)  Under
Slurm your job will only have the system shell init scripts run if you specify
``--export=NONE``.  The result is that ``--export=NONE`` is a required argument
to get your job to see software specific to a given node type, e.g. HSI/HTAR for
HPSS on the data transfer nodes.

For general information about SLURM, see `Introduction to SLURM
<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Introduction_to_SLURM>`_
and subsequent topics in the Commondocs pages.

Useful Commands
---------------

To find the accounts to which you belong

.. code-block:: shell

   sacctmgr show assoc where user=$USER formatcluster,partition,account,user%20,qos%60

Submit a job to the C3 cluster

.. code-block:: shell

   sbatch --clusters=c3 --nodes=1 --account=gfdl_z --qos=normal --export=NONE /path/to/job/script

Submit an urgent job to the C3 cluster

.. code-block:: shell

   sbatch --clusters=c3 --nodes=1 --accoun=tgfdl_z --qo=surgent --export=NONE /path/to/job/script

Submit a job to the C4 cluster

.. code-block:: shell

   sbatch --clusters=c4 --nodes=1 --account=gfdl_z --qos=normal --export=NONE /path/to/job/script

Submit a job to the LDTN

.. code-block:: shell

   sbatch --clusters=es --partition=ldtn --nodes=1 --ntasks-per-node=1 --account=gfdl_z --qos=normal --export=NONE /path/to/job/script

Submit a job to the RDTNs

.. code-block:: shell

   sbatch --clusters=es --partition=rdtn --nodes=1 --ntasks-per-node=1 --account=gfdl_z --qos=normal --export=NONE /path/to/job/script

To submit interactive work to c3

.. code-block:: shell

   salloc --clusters=c3 --qos=interactive --nodes=1 --x11

If you’re using x2go the X forwarding won’t work without the following
workaround: gsissh -XY to another gaea login node and then run salloc.

Running your models
-------------------

Run a simple executable on all allocated processes

.. code-block:: shell

   srun ./executable

To run a heterogeneous job

.. code-block:: shell

   srun --ntasks=1 --cpus-per-task=32 ./executable : --ntasks=128 --cpus-per-task=1 ./executable

.. note::

   We are working an issue where modulecmd is not initialized in all shells. If you
   find that modulecmd is missing, add the following to your job script:

.. code-block:: shell

   source /opt/modules/default/init/&lt;your_job_script_shell_type&gt;

Monitoring Jobs
---------------

Shell Setup
^^^^^^^^^^^

Do not set these in jobs/shells you intend to submit work from as they will
override your job submission script #SBATCH directives, causing warnings and
errors. Use them in shells you intend to monitor jobs from.

.. tab-set::

   .. tab-item:: [t]csh

      .. code-block:: tcsh

         setenv SLURM_CLUSTERS t4,c3,c4,gfdl,es

   .. tab-item:: bash

      .. code-block:: bash

         export SLURM_CLUSTERS=t4,c3,c4,gfdl,es

Show Pending and Running Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   squeue -a

Show Completed Jobs
^^^^^^^^^^^^^^^^^^^

Slurm does not keep completed jobs in ``squeue``.

.. code-block:: shell

   sacct -S 2019-03-01 -E now -a

If you don’t specify ``-S`` and ``-E`` options ``sacct`` gives you data from today.

Getting details about a job
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slurm only keeps information about completed jobs available via scontrol for 5
minutes after completion. After that time, sacct is the currently available way
of getting information about completed jobs.

.. code-block::

   scontrol show job --clusterses 5978

Fair Share Reporting
--------------------

Summary of all accounts
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   sshare

Summary of one account
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   sshare -A aoml

Details by user of one account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   sshare -a -A gefs

Details by user of all accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   sshare -a

Priority Analysis of Your Job
-----------------------------

sprio
^^^^^

.. code-block:: shell

   sprio -j 12345

.. _slurm_tips_fairshare:

Understanding Slurm FairShare
=============================

.. _slurm_tips_running_monitoring:

Running and Monitoring Jobs
===========================

.. _slurm_tips_getting_project_information:

Getting Information About Your Projects
=======================================

.. _slurm_tips_saccount_params:

The ``saccout_params`` Command
------------------------------

.. _slurm_tips_shpcrpt:

The ``shpcrpt`` Command
-----------------------
