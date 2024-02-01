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
option (e.g., ``sinfo --help``). 

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

+------------------------------------------------+----------------------------------------------------------------------------------+
| Option                                         | Description                                                                      |
+================================================+==================================================================================+
| ``-N``                                         | Number of nodes                                                                  |
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``-n``                                         | Total number of MPI tasks (default is 1)                                         | 
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``-c, --cpus-per-task=``                       | Logical cores per MPI task (default is 1)                                        |
|                                                | When used with ``--threads-per-core=1``:``c`` is equivalent to *physical* cores  |
|                                                | per task.                                                                        |
+------------------------------------------------+----------------------------------------------------------------------------------+
| ``--threads-per-core=``                        | In task layout, use the specified maximum number of hardware threads per core.   |
|                                                | Must also be set in ``salloc`` or ``sbatch`` if using ``--threads--per-core=2``. |
+------------------------------------------------+----------------------------------------------------------------------------------+
|   ``--ntasks-per-node=``                       | If used without ``-n``: requests that a specific number of tasks be invoked on   |
|                                                | each node.                                                                       |
|                                                | If used with ``-n``: treated as a maximum count of tasks per node.               |
|                                                |                                                                                  |
+------------------------------------------------+----------------------------------------------------------------------------------+

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
===============

The commands ``squeue``, ``scontrol`` and ``scancel`` from the :ref:`common
slurm commands table <slurm-common-commands>` will allow users to view,
monitor, cancel, and discover information about their jobs on the system.

Show Pending and Running Jobs
-----------------------------

Use the ``squeue`` command to view a list of current jobs in the queue. See ``man squeue`` for more information.

.. code-block:: shell

   $ squeue -a

To list jobs that belong to you 

.. code-block:: shell

   $ squeue -u <user name>


Show Completed Jobs
^^^^^^^^^^^^^^^^^^^

Slurm does not keep completed jobs in ``squeue``.

.. code-block:: shell

   $ sacct -S 2019-03-01 -E now -a

If you don’t specify ``-S`` and ``-E`` options ``sacct`` gives you data from today.

Use the ``sacct`` command option to list jobs that have run within the last 24 hours and to see their statuses (State). A full list of sacct options and job states can be found on the sacct man page. 

.. code-block:: shell

   $ sacct --user $USER --starttime `date --date="yesterday" +%F` -X --format=JobID,JobName%30,Partition,Account,AllocCPUS,State,Elapsed,QOS


Getting Details About a Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slurm only keeps information about completed jobs available via scontrol for 5
minutes after completion. After that time, sacct is the currently available way
of getting information about completed jobs.

.. code-block:: shell

   $ scontrol show job <jobid>


Understanding Slurm Fairshare
-----------------------------
SLURM utilizes a “FairShare” prioritization system. It uses the project’s allocation (RawShares) set by the Portfolio Manager and the RDHPCS Allocation Committee. SLURM normalizes the allocation into a % of system priority (Normshares). See definitions below. 

SLURM uses various job request parameters (submit time, partition, QOS, cores requested, requested wall clock time, etc.) and a calculated project's FairShare Factor (f) to continually assign/adjust the requested jobs’ priority until the job runs. 

FairShare is calculated from current allocation information (NormShares) and recent project and system usage data (EffectvUsage) such that more recent usage compared to your allocation and total system usage lowers the project's FairShare value and less recent usage compared to your allocation and total system usage increases the project's FairShare.

Fairshare Priority Factor
^^^^^^^^^^^^^^^^^^^^^^^^^
FairShare (f) = 2^-(EffectvUsage / NormShares ) (see definitions below)

**0.0 < f < 0.5**: The project is recently over utilizing their allocation relative to total system usage. 

**f ~0.5**: Recently the project has consistently utilized an amount ~equal to its allocation.

**0.5 < f < 1.0**: The project is recently underutilizing their allocation. 

Fairshare Definitions
^^^^^^^^^^^^^^^^^^^^^


**NormShares** is the project’s RawShares (allocated core-hours) divided by the total number of RawShares allocated to all projects on the system, or the fraction of the system the project has been allocated, which represents the projects system level priority without regard to QOS and recent usage priority adjustments. 

**RawShares** is the Core-hours allocation that has been assigned to project1 by the Portfolio Manager as discussed above. Rawshares means little toward job priority until it is compared to the total allocation of the system, which is the next parameter NormShares. Each user of project1 has the RawShare of parent, this means that all the users pull from the total RawShares of project1 and do not have their own individual sub-Shares. Thus all users on project1 have equal access to the full allocation of project1.

**EffectvUsage** is the project's ProjUsage (RawUsage) divided by the total RawUsage for the system.

**RawUsage** is the amount of core-seconds the project has used. RawUsage decays over time scaled linearly by the 1/2 life priority factor that is set for the system, which is currently 5-days (ex. current usage 100%, 5 day old usage 50%, 10 day old usage 25%, etc).

Projects with a windfall allocation always have a FairShare, Normshares, and EffectvUsage of 0 and therefore always have the lowest priority.

**Note**: Jobs run in the windfall QOS will NOT count toward RawUsage (and EffectvUsage) and hence will not lower FairShare.

For a new job to run sooner, regardless of your current FairShare value, it is important that you do the following:

- Select the appropriate QOS. 
- Submit your job ASAP as a job’s priority increases with time in the queue regardless of other priority factors.
- Enter an appropriate wall clock time. Excessive wall clock times will delay that start of your job, and contributes to overall inefficient scheduling and system utilization.



Fairshare Reporting
^^^^^^^^^^^^^^^^^^^

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


Priority Analysis of Your Job
-----------------------------

sprio
^^^^^

.. code-block:: shell

   sprio -j 12345

.. _slurm_tips_fairshare:


Getting Information About Your Projects
---------------------------------------

Use the sfairshare command to show the current FairShare priority status of all projects. Of particular interest will likely be the , the -u option to list just your projects, -w option (these projects always have the lowest priority) to exclude listing windfall projects, and the -T <threshold> option, which will give you a list of all projects and their FairShare value with a higher value than the threshold value you enter. For more options on sfairshare use the sfairshare -h command. 

Here are examples from Hera:

.. code-block:: shell

   [First.Last@hfe12 ~]$ sfairshare -w
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
   [First.Last@hfe12 ~]$ sfairshare -w -T 0.5
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


Use the SLURM sshare command to get project FairShare priority information sorted by Portfolio and sub-Portfolio. Note: SLURM only uses a project's Fairshare value in priority calculations, not the Portfolio's or sub-Portfolio's FairShare.

saccount_params
^^^^^^^^^^^^^^^

Available on Hera, Jet, Orion

Use the saccount_params or account_params command to get your current:

- Home File System usage/quota (MB)

- For each of your projects
    - Compute: FairShare priority value, (FairShare rank vs all other projects), partition access and available QOS's for all your projects. Include -l (for long) if you want to see current 30-day allocation, last 30-day usage, and FairShare to 6 digits(``saccount_params -l``).
    - Scratch disk usage/quota (GB), files on disk and file count quota.

``NOTE``: Projects with a windfall allocation of 1 will show an allocation of 0, but you will see the correct Available QOS: windfall. Projects with an allocation of 2 will show an allocation of 1, but you will see the correct Available QOS: Batch, debug, etc.

.. code-block:: shell

   [First.Last @hfe07 ~]$ saccount_params


shpcrpt
^^^^^^^

Use the shpcrpt tool to get current project's FairShare factor and rank, allocation, and ~current month to date (MTD) Compute usage information on all your project(s), detailed project information by user, and summary information for all projects on the system. 

To execute shpcrpt, load the module (if not already in present in env) and then call the script with the necessary parameters

If you call shpcprt without any arguments, you will receive an error message. You must use `-c` or ``--cluster`` to identify the cluster. 

Use ``shpcrpt --help`` for more details. 


Example:

.. code-block:: shell

   $ shpcrpt -c <cluster>

To see a specific group’s hpc report, specify the group:

.. code-block:: shell

   $ shpcrpt -p <project> -c <cluster>

Getting Portfolio or Sub-portfolio Information 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The shpcprt tool includes three options to display Portfolio or Sub-portfolio project information. Typically, this can help provide a faster report since less data needs to be gathered and processed from the database. 

These options are:

- H - Displays the Portfolio and SubPortfolio columns containing that information for each project
- P - Follow 'P' with portfolio name to display projects associated with that portfolio, only.
- S - Follow 'S' with sub-portfolio name to display projects associated with that sub-portfolio, only

The options only apply to the summary report (not user (-u) or project (-p) reports). Here are examples on how to use these options: 

.. code-block:: shell

   $ shpcrpt -c hera -H

Portfolio-specific summary report using -H and -P options 

.. code-block:: shell

   $ shpcrpt -c hera -H -P bmc

Sub-portfolio-specific summary report using -H and -S options

.. code-block:: shell

   $ shpcrpt -c hera -H -S csd


Useful Slurm Commands 
---------------------

To see available clusters

.. code-block:: shell

   $ sacctmgr show clusters 

To find the accounts to which you belong

.. code-block:: shell

   $ sacctmgr show assoc where user=$USER formatcluster,partition,account,user%20,qos%60

To submit a job to a specific cluster

.. code-block:: shell
    
   $ sbatch --clusters=<cluster> --nodes=1 --account=<account_name> --qos=normal --export=NONE /path/to/job/script

To submit an interactive job 

.. code-block:: shell

   $ salloc --qos=<qos_name> --nodes=1 --x11 -t1:00:00


