#####
Slurm
#####

Slurm is an open-source cluster management and job scheduler, originally
developed at the Lawrence Livermore National Laboratory.  Commercial support is
now provided by `SchedMD <https://schedmd.com>`__.  The information provided in
this document is a basic guide for some of the most useful commands, along with
specific information for the RDHPCS systems.  The SchedMD site maintains `full
documentation <https://slurm.schedmd.com/>`__ and basic `tutorials
<https://slurm.schedmd.com/tutorials.html>`__.

Some common Slurm commands are summarized in the table below.

.. _slurm-common-commands:

+--------------+------------------------------------------------+
| Command      | Action/Task                                    |
+==============+================================================+
| ``squeue``   | Show the current queue                         |
+--------------+------------------------------------------------+
| ``sbatch``   | Submit a batch script                          |
+--------------+------------------------------------------------+
| ``salloc``   | Submit an interactive job                      |
+--------------+------------------------------------------------+
| ``srun``     | Launch a parallel job                          |
+--------------+------------------------------------------------+
| ``sinfo``    | Show node/partition info                       |
+--------------+------------------------------------------------+
| ``sacct``    | View accounting information for jobs/job steps |
+--------------+------------------------------------------------+
| ``sacctmgr`` | View account information                       |
+--------------+------------------------------------------------+
| ``scancel``  | Cancel a job or job step                       |
+--------------+------------------------------------------------+
| ``scontrol`` | View or modify job configuration.              |
+--------------+------------------------------------------------+

All Slurm commands have on-line manual pages viewable via the ``man`` command
(e.g., ``man sbatch``) and extensive usage information using the ``--help``
option (e.g., ``sinfo --help``).  See :ref:`slurm-references` for links to the
SchedMD documentation.

Running a Job
=============

Computational work on the RDHPCS is performed by *jobs*. Jobs typically consist
of several components:

-  A batch submission script
-  A binary executable
-  A set of input files for the executable
-  A set of output files created by the executable

In general, the process for running a job is to:

#. Prepare executables and input files.
#. Write a batch script.
#. Submit the batch script to the batch scheduler.
#. Optionally monitor the job before and during execution.

In addition, users can perform interactive work on the compute nodes using the
``salloc`` command.

Batch Scripts
-------------

The most common way to interact with the batch system is via batch scripts. A
batch script is simply a shell script with added directives to request various
resources from or provide certain information to the scheduling system.  Aside
from these directives, the batch script is simply the series of commands needed
to set up and run your job.

To submit a batch script, use the command ``sbatch myjob.sl``.

Consider the following batch script:

.. code-block:: bash
   :linenos:

    #!/bin/bash
    #SBATCH -A ABC123
    #SBATCH -J RunSim123
    #SBATCH -o %x-%j.out
    #SBATCH -t 1:00:00
    #SBATCH -p hera
    #SBATCH -N 1024

    cd $MEMBERWORK/abc123/Run.456
    cp $PROJWORK/abc123/RunData/Input.456 ./Input.456
    srun ...
    cp my_output_file $PROJWORK/abc123/RunData/Output.456

In the script, Slurm directives are preceded by ``#SBATCH``, making them appear
as comments to the shell. Slurm looks for these directives through the first
non-comment, non-whitespace line. Options after that will be ignored by Slurm
(and the shell).

+------+--------------------------------------------------------------------+
| Line | Description                                                        |
+======+====================================================================+
|    1 | Shell interpreter line                                             |
+------+--------------------------------------------------------------------+
|    2 | Project to charge                                                  |
+------+--------------------------------------------------------------------+
|    3 | Job name                                                           |
+------+--------------------------------------------------------------------+
|    4 | Job standard output file (``%x`` will be replaced with the job     |
|      | name and ``%j`` with the Job ID)                                   |
+------+--------------------------------------------------------------------+
|    5 | Walltime requested (in ``HH:MM:SS`` format). See ``man sbatch``    |
|      | for other formats.                                                 |
+------+--------------------------------------------------------------------+
|    6 | Partition (queue) to use                                           |
+------+--------------------------------------------------------------------+
|    7 | Number of compute nodes requested                                  |
+------+--------------------------------------------------------------------+
|    8 | Blank line                                                         |
+------+--------------------------------------------------------------------+
|    9 | Change into the run directory                                      |
+------+--------------------------------------------------------------------+
|   10 | Copy the input file into place                                     |
+------+--------------------------------------------------------------------+
|   11 | Run the job ( add layout details )                                 |
+------+--------------------------------------------------------------------+
|   12 | Copy the output file to an appropriate location.                   |
+------+--------------------------------------------------------------------+

.. note::

   The environment variables used in the above script example are used to
   indicate locations as specified in :ref:`summary-of-storage-areas`, and are
   not available on any RDHPCS system.

Interactive Jobs
----------------

Most users will find batch jobs an easy way to use the system, as they allow
you to "hand off" a job to the scheduler, allowing them to focus on other tasks
while their job waits in the queue and eventually runs. Occasionally, it is
necessary to run interactively, especially when developing, testing, modifying
or debugging a code.

Since all compute resources are managed and scheduled by Slurm, it is not
possible to simply log into the system and immediately begin running parallel
codes interactively. Rather, you must request the appropriate resources from
Slurm and, if necessary, wait for them to become available. This is done
through an "interactive batch" job. Interactive batch jobs are submitted with
the ``salloc`` command. Resources are requested via the same options that are
passed via ``#SBATCH`` in a regular batch script (but without the ``#SBATCH``
prefix). For example, to request an interactive batch job with the same
resources that the batch script above requests, you would use ``salloc -A
ABC123 -J RunSim123 -t 1:00:00 -p batch -N 1024``. Note there is no option for
an output file...you are running interactively, so standard output and standard
error will be displayed to the terminal.

.. note::

   At times it will be useful to use a graphical interface (GUI) while running
   an interactive job, for example a graphical debugger.  To allow the
   interactive job to allow displaying the graphical interface, you must supply
   the ``--x11`` option to ``salloc``.

Common ``sbatch`` Options
-------------------------

There are two ways to specify sbatch options. The first is on the command line
when using the sbatch command.

.. code-block:: shell

   $ sbatch --clusters=<cluster> --account=abc123 myrunScript.sh

The second method is to insert directives at the top of the batch script using
#SBATCH syntax. For example,

.. code-block:: shell

   #SBATCH --clusters=<cluster>
   #SBATCH --account=abc123

The two methods can be mixed together. However, options specified on the
command line always override options specified in the script.

The table below summarizes options for submitted jobs. Check the Slurm Man
Pages for a more complete list.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Option
     - Example Usage
     - Description
   * - ``-A``, ``--account``\
     - ``$SBATCH --account=abc123``
     - Specifies the project to which the job should be charged.
   * - ``-t``, ``--time``
     - ``#SBATCH -t 4:00:00``
     - Specify a maximum wallclock.
   * - ``-J``, ``-job-name``
     - ``#SBATCH -J jobname``
     - Set the name of the job.
   * - ``-N``, ``--nodes``
     - ``#SBATCH -N 1024``
     - Request the number of nodes be allocated to a job.
   * - ``-n``, ``--ntasks``
     - ``#SBATCH -n 8``
     - Request for a number of total tasks.
   * - ``--mem``
     - ``#SBATCH --mem=4g``
     - Specify the real memory required per node
   * - ``-q``, ``--qos``
     - ``#SBATCH --qos=normal``
     - Request a quality of service for the job.
   * - ``-o``, ``--output``
     - ``#SBATCH --output=jobout.%j``
     - File where the job's STDOUT will be directed.  (``%j`` will be replaced
       with the job ID.)
   * - ``-e``, ``--error``
     - ``#SBATCH --error=joberr.%j``
     - File where the job's STDERR will be directed.  (``%j`` will be replaced
       with the job ID.)  The ``-o`` and ``-e`` options may reference the same
       file to have both the STDOUT and STDERR go to the same file.
   * - ``--mail-user``
     - ``#SBATCH --mail-user=user@example.com``
     - Email address to be used for notifications.
   * - ``-M``, ``--clusters``
     - ``#SBATCH --clusters=cluster_name``
     - Clusters to submit the job to.

.. note::

   Gaea uses a federation of clusters which include the login and dtn cluster
   (es), the compute clusters (e.g., c5, c6), and the GFDL post processing and
   analysis cluster (gfdl).  On gaea, the ``--clusters`` option must be
   specified, and should be specified for many of the Slurm commands.

Slurm Environment Variables
---------------------------

Slurm reads a number of environment variables, many of which can provide the
same information as the job options noted above. We recommend using the job
options rather than environment variables to specify job options, as it allows
you to have everything self-contained within the job submission script (rather
than having to remember what options you set for a given job).

Slurm also provides a number of environment variables within your running job.
The following table summarizes those that may be particularly useful within
your job (e.g. for naming output log files):

+--------------------------+--------------------------------------------------+
| Variable                 | Description                                      |
+==========================+==================================================+
| ``$SLURM_SUBMIT_DIR``    | The directory from which the batch job was       |
|                          | submitted.  By default, a new job starts in your |
|                          | home directory. You can get back to the          |
|                          | directory of job submission with                 |
|                          | ``cd $SLURM_SUBMIT_DIR``. Note that this is not  |
|                          | necessarily the same directory in which the      |
|                          | batch script resides.                            |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOBID``         | The job's full identifier. A common use for      |
|                          | ``$SLURM_JOBID`` is to append the job's ID to    |
|                          | the standard output and error files.             |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOB_NUM_NODES`` | The number of nodes requested.                   |
+--------------------------+--------------------------------------------------+
| ``$SLURM_JOB_NAME``      | The job name supplied by the user.               |
+--------------------------+--------------------------------------------------+
| ``$SLURM_NODELIST``      | The list of nodes assigned to the job.           |
+--------------------------+--------------------------------------------------+

.. _slurm-state-codes:

State Codes
-----------

A job will transition through several states during its lifetime. Common ones
include:

+-----+---------------+-------------------------------------------------------+
| State Code          | Description                                           |
+=====+===============+=======================================================+
| CA  | Cancelled     | The job was explicitly cancelled by the user or       |
|     |               | system administrator                                  |
+-----+---------------+-------------------------------------------------------+
| CD  | Completed     | Job has terminated all processes on all nodes. Exit   |
|     |               | code of zero.                                         |
+-----+---------------+-------------------------------------------------------+
| F   | Failed        | Job terminated with non-zero exit code or other       |
|     |               | failure condition.                                    |
+-----+---------------+-------------------------------------------------------+
| R   | Running       | Job currently has an allocation.                      |
+-----+---------------+-------------------------------------------------------+
| TO  | Timeout       | Job terminated upon reaching its time limit.          |
+-----+---------------+-------------------------------------------------------+
| PD  | Pending       | Job is awaiting resource allocation.                  |
+-----+---------------+-------------------------------------------------------+
| OOM | Out Of Memory | Job experienced out of memory error.                  |
+-----+---------------+-------------------------------------------------------+
| NF  | Node Fail     | The list of nodes assigned to the job.                |
+-----+---------------+-------------------------------------------------------+

Job Reason Codes
----------------

+----------------------+------------------------------------------------------+
| Reason               | Meaning                                              |
+======================+======================================================+
| InvalidQOS           | The job's QOS is invalid.                            |
+----------------------+------------------------------------------------------+
| InvalidAccount       | The job's account is invalid                         |
+----------------------+------------------------------------------------------+
| NonZeroExitCode      | The job terminated with a non-zero exit code.        |
+----------------------+------------------------------------------------------+
| NodeDown             | A node required by the job is down.                  |
+----------------------+------------------------------------------------------+
| TimeLimit            | The job exhausted its time limit                     |
+----------------------+------------------------------------------------------+
| SystemFailure        | Failure of the Slurm system, a file system, the      |
|                      | network, etc.                                        |
+----------------------+------------------------------------------------------+
| JobLaunchFailure     | The job cannot be launched. This may be due to a     |
|                      | file system problem, invalid program name, etc.      |
+----------------------+------------------------------------------------------+
| WaitingForScheduling | The list of nodes assigned to the job.               |
+----------------------+------------------------------------------------------+

Job Dependencies
----------------

SLURM supports the ability to submit a job with constraints that will keep it
running until these dependencies are met. A simple example is where job X
cannot execute until job Y completes. Dependencies are specified with the
``-d`` option to Slurm.

+----------------------------------+------------------------------------------+
| Flag                             | Meaning                                  |
+==================================+==========================================+
|``SBATCH -d after:jobid[+time]``  | The job can start after the specified    |
|                                  | jobs start or are cancelled. The         |
|                                  | optional +time argument is a number of   |
|                                  | minutes. If specified, the job cannot    |
|                                  | start until that many minutes have       |
|                                  | passed since the listed jobs start/are   |
|                                  | cancelled. If not specified, there is no |
|                                  | delay.                                   |
+----------------------------------+------------------------------------------+
| ``SBATCH -d afterany:jobid``     | The job can start after the specified    |
|                                  | jobs have ended, regardless of exit      |
|                                  | state.                                   |
+----------------------------------+------------------------------------------+
| ``SBATCH -d afternotok:jobid``   | The job can start after the specified    |
|                                  | jobs terminate in a failed (non-zero)    |
|                                  | state.                                   |
+----------------------------------+------------------------------------------+
| ``SBATCH -d afterok:jobid``      | The job can start after the specified    |
|                                  | jobs complete successfully               |
+----------------------------------+------------------------------------------+
| ``SBATCH -d singleton``          | Job can begin after any                  |
|                                  | previously-launched job with the same    |
|                                  | name and from the same user have         |
|                                  | completed. In other words, serialize     |
|                                  | the running jobs based on                |
|                                  | username+jobname pairs.                  |
+----------------------------------+------------------------------------------+

Srun
----

Your job scripts will usually call ``srun`` to run an executable on multiple
nodes.

.. code-block:: shell

   $ srun [OPTIONS... [executable [args...]]]

``srun`` accepts the following options:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Option
     - Description
   * - ``-N``,  ``--nodes``
     - Number of nodes to use.
   * - ``-n``, ``--ntasks``
     - Total number of MPI tasks (default is 1).
   * - ``-c``, ``--cpus-per-task``
     - Logical cores per MPI task (default is 1).  When used with
       ``--threads-per-core=1``, ``-c`` is equivalent to *physical* cores per
       task.
   * - ``--threads-per-core``
     - In task layout, use the specified maximum number of hardware threads per
       core.  Must also be set in ``salloc`` or ``sbatch`` if using
       ``--threads--per-core=2``.
   * - ``--ntasks-per-node``
     - If used without ``-n``, requests that a specific number of tasks be
       invoked on each node.  If used with ``-n``, treated as a maximum count
       of tasks per node.

Heterogeneous Jobs
^^^^^^^^^^^^^^^^^^
A heterogeneous job is a job in which each component has virtually all job
options available including partition, account and QOS (Quality Of Service).
For example, part of a job might require four cores and 4 GB for each of 128
tasks while another part of the job would require 16 GB of memory and one CPU.

To run a heterogeneous job use ``srun`` and separate the different components
with the colon (``:``) character.  This is similar to ``mpirun``.

.. code-block:: shell

   srun --ntasks=1 --cpus-per-task=32 ./executable : --ntasks=128 --cpus-per-task=1 ./executable

Monitoring Jobs
===============

The commands ``squeue``, ``scontrol`` and ``scancel`` from the :ref:`common
slurm commands table <slurm-common-commands>` will allow users to view,
monitor, cancel, and discover information about their jobs on the system.

Show Pending and Running Jobs
-----------------------------

Use the ``squeue`` command to view a list of current jobs in the queue.  See
``man squeue`` for more `information <squeue>`_.

.. code-block:: shell

   $ squeue -a

To list jobs that belong to a specific user

.. code-block:: shell

   $ squeue -u <userid>


Show Completed Jobs
-------------------

Slurm does not keep completed jobs in ``squeue``.

.. code-block:: shell

   $ sacct -S 2019-03-01 -E now -a

If you don’t specify ``-S`` and ``-E`` options ``sacct`` gives you data from
the current day.

Use the ``sacct`` command option to list jobs that have run within the last 24
hours and to see their statuses (State). A full list of ``sacct`` options and
:ref:`job states <slurm-state-codes>` can be found on the ``sacct`` man page.

.. code-block:: shell

   $ sacct --user $USER --starttime `date --date="yesterday" +%F` -X --format=JobID,JobName%30,Partition,Account,AllocCPUS,State,Elapsed,QOS


Getting Details About a Job
---------------------------

Slurm only keeps information about completed jobs available via ``scontrol``
for 5 minutes after a job completes.  After that time, ``sacct`` is the way of
getting information about completed jobs.

.. code-block:: shell

   $ scontrol show job <jobid>

.. _slurm-priority-and-fairshare:

Priority and Fairshare
======================

Slurm uses a priority-based scheduling system to allocate resources to jobs.
The priority of a job is calculated based on several factors, including the
job's requested resources, the time at which the job was submitted, and any
user-defined priority adjustments.

Slurm's fairshare system is a way of allocating resources based on the
historical usage of different users and groups. Fairshare is designed to ensure
that resources are distributed fairly over time, so that no one user or group
dominates the system.

.. _slurm-fairshare:

Understanding Slurm Fairshare
-----------------------------

SLURM utilizes a “FairShare” prioritization system. It uses the project’s
allocation (RawShares) set by the Portfolio Manager and the RDHPCS Allocation
Committee. Slurm normalizes the allocation into a percentage of system priority
(Normshares). See definitions below.

Slurm uses various job request parameters (submit time, partition, QOS, job
size, requested wall clock time, etc.) and a calculated project's FairShare
Factor (f) to continually assign/adjust the requested jobs’ priority until the
job runs.

FairShare is calculated from current allocation information (NormShares) and
recent project and system usage data (EffectvUsage) such that more recent usage
compared to your allocation and total system usage lowers the project's
FairShare value and less recent usage compared to your allocation and total
system usage increases the project's FairShare.

Fairshare Priority Factor
-------------------------

The fairshare factor serves to prioritize queued jobs such that those jobs
charging accounts that are under-serviced are scheduled first, while jobs
charging accounts that are over-serviced are scheduled when the machine would
otherwise go idle.

Slurm's fair-share factor is a floating point number between 0.0 and 1.0 that
reflects the shares of a computing resource that a user has been allocated and
the amount of computing resources the user's jobs have consumed. The higher the
value, the higher is the placement in the queue of jobs waiting to be
scheduled.

Slurm on the RDHPCS systems use the `Classic Fairshare Algorithm
<https://slurm.schedmd.com/classic_fair_share.html>`__ that is calculated by
the equation

.. math::

   fairshare\_factor = 2^{-(EffectvUsage / NormShares)}

A fairshare factor value :math:`<0.5` indicates that a project is over
utilizing their allocation relative to total system usage, whereas a factor
:math:`>0.5` indicates the project is underutilizing.

Fairshare Definitions
---------------------

:EffectvUsage:: the project's ProjUsage (RawUsage) divided by the total
    RawUsage for the system.
:NormShares: the project’s RawShares (allocated core-hours) divided by the
   total number of RawShares allocated to all projects on the system, or the
   fraction of the system the project has been allocated, which represents the
   projects system level priority without regard to QOS and recent usage
   priority adjustments.
:RawShares: the Core-hours allocation that has been assigned to project1 by the
   Portfolio Manager as discussed above. Rawshares means little toward job
   priority until it is compared to the total allocation of the system, which
   is the next parameter NormShares. Each user of project1 has the RawShare of
   parent, this means that all the users pull from the total RawShares of
   project1 and do not have their own individual sub-Shares. Thus all users on
   project1 have equal access to the full allocation of project1.
:RawUsage: the amount of core-seconds the project has used. RawUsage decays
    over time scaled linearly by the 1/2 life priority factor that is set for
    the system, which is currently 5-days (ex. current usage 100%, 5 day old
    usage 50%, 10 day old usage 25%, etc).

Projects with a windfall allocation always have a FairShare, Normshares, and
EffectvUsage of 0 and therefore always have the lowest priority.

.. note::

   Jobs run in the windfall QOS will NOT count toward RawUsage (and
   EffectvUsage) and hence will not lower FairShare.

Fairshare Reporting
-------------------

Summary of all accounts

.. code-block:: shell

   $ sshare

Summary of one account

.. code-block:: shell

   $ sshare -A <account>

Details by user of one account

.. code-block:: shell

   $ sshare -a -A <account>

Details by user of all accounts

.. code-block:: shell

   $ sshare -a

Priority Reporting
------------------

As mentioned earlier, Slurm uses `multiple factors
<https://slurm.schedmd.com/priority_multifactor.html>`__ to determine a job's
priority.  The ``sprio`` command reports the job's priority.

.. code-block:: shell

   $ sprio -j 12345
      JOBID PARTITION   PRIORITY   SITE       AGE   ASSOC  FAIRSHARE        QOS     TRES
      12345 hera        18302014      0   5000000       0    3301977   10000000   cpu=38

.. _slurm-getting-information-about-your-projects:

Getting Information About Your Projects
=======================================

The RDHPCS system administrators have supplied additional tools to help the
users gather information concerning their jobs, job's fairshare, and allocation
usage.  The tools listed in this section may not be available on all RDHPCS
systems.

sfairshare
----------

The ``sfairshare`` command will show the current FairShare priority status of
all projects. Of particular interest will likely be the , the ``-u`` option to
list just your projects, ``-w`` option (these projects always have the lowest
priority) to exclude listing windfall projects, and the ``-T <threshold>``
option, which will give you a list of all projects and their FairShare value
with a higher value than the threshold value you enter. For more options on
sfairshare use the sfairshare ``-h`` command.

.. code-block:: shell

   $ sfairshare -w
   Project         FairShare       Rank    NormShares      EffUsage
   -----------     ----------      ------  ----------      ----------
   amb-verif            0.974      23/90      0.00105         0.00004
   aoml-hafs1           0.476      70/90      0.13904         0.15884
   aoml-osse            0.415      74/90      0.06094         0.08237
   aoml-phod            0.503      66/90      0.04483         0.04732
   ap-fc                0.963      24/90      0.00435         0.00024
   arl                  0.317      85/90      0.00003         0.00006
   .
   .
   .
   $ sfairshare -w -T 0.5
   Project         FairShare       Rank    NormShares      EffUsage
   -----------     ----------      ------  ----------      ----------
   amb-verif            0.974      23/90      0.00105         0.00004
   aoml-phod            0.503      66/90      0.04483         0.04731
   ap-fc                0.963      24/90      0.00435         0.00024
   bpe                  1.000      1/90       0.00002         0.00000
   ccasm                0.719      44/90      0.00005         0.00003
   ccp-mozart           0.552      59/90      0.00042         0.00036
   .
   .
   .

The Slurm ``sshare`` command to get project FairShare priority information
sorted by Portfolio and sub-Portfolio. Note that Slurm only uses a project's
Fairshare value in priority calculations, not the Portfolio's or
sub-Portfolio's FairShare.

.. note::

   ``sfairshare`` is only available on Hera and Jet.

.. _slurm-saccount-params:

saccount_params
---------------

The ``saccount_params`` will show your current:

- Home File System usage/quota (MB)
- For each of your projects

    - Compute: FairShare priority value, (FairShare rank vs all other
      projects), partition access and available QOS's for all your projects.
      Include -l (for long) if you want to see current 30-day allocation, last
      30-day usage, and FairShare to 6 digits(``saccount_params -l``).
    - Scratch disk usage/quota (GB), files on disk and file count quota.

.. note::

   Projects with a windfall allocation of 1 will show an allocation of 0, but you
   will see the correct Available QOS: windfall. Projects with an allocation of 2
   will show an allocation of 1, but you will see the correct Available QOS:
   Batch, debug, etc.

.. note::

   ``saccount_params`` is only available on Hera, Jet, Orion.

.. code-block:: shell

   $ saccount_params

   Account Params -- Information regarding project associations for userid
      Home Quota (/home/userid) Used: 4149 MB Quota: 5120 MB

      Project: projid
         FairShare=1.000 (91/91)
         Partition Access: ALL
         Available QOSes: gpuwf,windfall
         Directory: /scratch[12]/[portfolio]/projid DiskInUse=206372 GB, Quota=255000 GB, Files=5721717, FileQUota=51000000

.. _slurm-shpcrpt:

shpcrpt
-------

The ``shpcrpt`` tool will report a project's FairShare factor and rank,
allocation, and the current month to date (MTD) compute usage information on
all your project(s), detailed project information by user, and summary
information for all projects on the system.

On some RDHPCS system, ``shpcrpt`` is available after loading the ``shpcrpt``
module.

.. tab-set::

  .. tab-item:: Gaea
    :sync: gaea

    .. code-block:: shell

      $ module use /usw/shpcrpt/modulefiles
      $ module load shpcrpt

Use ``shpcrpt --help`` for more details.

.. code-block:: shell

   $ shpcrpt -c <cluster>
   =================================================================================================================
   Report                           Summary Report
   Report Run:                      Fri 02 Feb 2024 09:48:57 PM  UTC
   Report Period Beginning:         Thu 01 Feb 2024 12:00:00 AM  UTC
   Report Period Ending:            Fri 01 Mar 2024 12:00:00 AM  UTC
   Percentage of Period Elapsed:    6.6%
   Percentage of Period Remaining:  93.4%
   =================================================================================================================
   Project               NormShares   FairShare        Rank  Allocation   Cr-HrUsed    Windfall   TotalUsed       %Used        Jobs
   -------------------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- -----------
   proj01                  0.010531    0.501784       64/90     476,712      65,412           0      65,412      13.72%       1,600
   proj02                  0.000000    1.000000       90/90           1           0           0           0       0.00%           0
   proj03                  0.001050    0.920788       35/90      47,520         456           0         456       0.96%      23,469
   proj04                  0.154815    0.619112       46/90   7,008,123     505,651           0     505,651       7.22%      27,067
   .
   .
   .

To see a specific group’s hpc report, specify the group:

.. code-block:: shell

   $ shpcrpt -p <project> -c <cluster>
   =================================================================================================================
   Report                           Project Report for:projid
   Report Run:                      Fri 02 Feb 2024 09:50:20 PM  UTC
   Report Period Beginning:         Thu 01 Feb 2024 12:00:00 AM  UTC
   Report Period Ending:            Fri 01 Mar 2024 12:00:00 AM  UTC
   Percentage of Period Elapsed:    6.6%
   Percentage of Period Remaining:  93.4%
   =================================================================================================================
   Machines:                               clusterid
   Initial Allocation in Hours:              493,151
   Net Allocation Adjustments:               -16,439
                                    ----------------
   Adjusted Allocation:                      476,712

   Core Hours Used:                           65,444
   Windfall Core Hours Used:                       0
                                    ----------------
   Total Core Hours Used:                     65,444

   Project Normalized Shares:               0.010531
   Project Fair Share:                      0.501784
   Project Rank:                               64/90

   Percentage of Period Elapsed:                6.6%
   Percentage of Period Remaining:             93.4%
   Percentage of Allocation Used:              13.7%

   User                             Cr-HrUsed    Windfall   TotalUsed       %Used      Jobs
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   Johana.Romero-Alvarez               40,085           0      40,085       8.41%     1,547
   Sudheer.R.Bhimireddy                25,359           0      25,359       5.32%        53
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   Total                               65,444           0      65,444      13.73%     1,600

   Total Report Runtime: 2.49 seconds (ver. 23.07.06-FNJT)

.. note::

   The ``shpcrpt`` command requires the ``-c <clusterid>`` option.

.. note::

   The ``shpcrpt`` command can take a while to return results.  This is due to
   ``shpcrpt`` pulling data directly from Slurm to generate the reports.

.. _slurm-references:

References
==========

* `Slurm Documentation`_
* sacct_
* salloc_
* sacctmgr_
* sbatch_
* scancel_
* scontrol_
* sinfo_
* squeue_
* srun_
* `Slurm Fairshare`_

.. _`Slurm Documentation`: https://slurm.schedmd.com/
.. _`squeue`: https://slurm.schedmd.com/squeue.html
.. _`sbatch`: https://slurm.schedmd.com/sbatch.html
.. _`salloc`: https://slurm.schedmd.com/salloc.html
.. _`srun`: https://slurm.schedmd.com/srun.html
.. _`sinfo`: https://slurm.schedmd.com/sinfo.html
.. _`sacct`: https://slurm.schedmd.com/sacct.html
.. _`sacctmgr`: https://slurm.schedmd.com/sacctmgr.html
.. _`scancel`: https://slurm.schedmd.com/scancel.html
.. _`scontrol`: https://slurm.schedmd.com/scontrol.html
.. _`Slurm Fairshare`: https://slurm.schedmd.com/classic_fair_share.html
