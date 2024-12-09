########
Overview
########

Slurm is an open-source cluster management and job scheduler, originally
developed at the Lawrence Livermore National Laboratory.  Commercial support is
now provided by `SchedMD <https://www.schedmd.com>`__.  The information provided in
this document is a basic guide for some of the most useful commands, along with
specific information for the RDHPCS systems.  The SchedMD site maintains `full
documentation <https://slurm.schedmd.com/>`__ and basic `tutorials
<https://www.schedmd.com/publications/>`__.

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

.. _slurm-running-a-job:

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

Loading Modules in a batch script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you loaded modules when building your code, they must be loaded when the
job runs as well. This means that you must put the same module commands in your
batch scripts that you ran before building your code.

Loading modules in a batch script requires one additional line to make the
module commands available in the script:

.. code-block:: bash
   :linenos:

    #!/bin/bash
    #SBATCH ( put directives here )

    source $MODULESHOME/init/bash
    module load THING1 THING2

+------+--------------------------------------------------------------------+
| Line | Description                                                        |
+======+====================================================================+
|    1 | Shell interpreter line                                             |
+------+--------------------------------------------------------------------+
|    2 | A placeholder for needed SBATCH directives                         |
+------+--------------------------------------------------------------------+
|    4 | The command that will make the module commands available           |
+------+--------------------------------------------------------------------+
|    5 | An example line for `module load`                                  |
+------+--------------------------------------------------------------------+


Module Loading Best Practices
""""""""""""""""""""""""""""""

.. note::

   Do Not Load Modules at Shell Initialization.

Upon user interactive login, running batch jobs, running cron scripts, and
running command line scripts, a shell is invoked.

Loading modules in shell initialization scripts can lead to unintended
consequences, as the shell's environment may be different than the one
expected. The wrong libraries can be loaded, the wrong tools can be used, the
wrong version of tools can be used, and even tools provided with the operating
system may no longer work properly or provide strange error messages. For these
reasons, we **highly** recommend that you do not add module loads to your
shell's initialization scripts.

Instead, we recommend that you remove module loads from shell initialization
scripts and do one or more of the following:

#. Add the module loads directly to your batch script or cron scripts
#. Create a separate script responsible for loading the desired modules and
   environment. This script can then be invoked/sourced any time you want to
   set up this specific environment. A command "alias" can also be added to
   your shell's initialization scripts. You can then run the alias command to
   invoke the desired shell environment.
#. Create a script as described above and have all members of your project
   invoke/source the exact same script. This will ensure that the exact same
   modules are used by all users. You can even add "module purge" to the
   beginning of the script to ensure that only the desired modules are being
   loaded.


If you need help implementing these methods, open an RDHPCS help ticket. See
:ref:`Getting_Help` for details.

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
     - Specify a maximum wall clock limit.
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

Specifying Partitions and QOS
-----------------------------

RDHPCS systems generally have a default partition and QOS. If you do not
specify these parameters, your job will be submitted to the default partition
and QOS.

If you wish choose a different partition or QOS you will need to specify them
as per the table above. Different partitions and QOS are available, depending
the resources you need. For example, jobs that require external network
connectivity or HPSS access will generally need to be submited to the
**service** partition.

QOS is used to specify a **priority** for the job.

There are limits, such as number of nodes and tasks,
and wall time limits for each partitions and QOS.
To see what those limits are, run the command ``sbatch-limits``.

The output of this command also shows which combinations of
partition/QOS are permitted, as not all partitions/QOS combinations are
allowed.

Run the command ``sbatch-limits -h`` to see the other available options.

.. _memory-usage:

Determine and specify a memory limit for your jobs
==================================================

You can use the "report-mem" command in your job to get memory usage
information from your batch job. But this
works only if you are able to successfully run your job to conclusion without
failing.

But if you don't know how much memory your application needs, you can "over
estimate" or use an entire node to get a successful run and include the
"report-mem" command in the job. To request all the available memory on the
node for a serial job you can use the ``--mem=0`` option on the ``sbatch``
command.

If your jobs are failing with memory errors, it is possible that your
application needs more memory than what you were giving for the job.

In the case of serial jobs (which means you may have other jobs running on the
same code and that your job is running), by default you get a certain amount of
memory. If your application needs more memory than the default, you need to
specify the memory needed by your job using the ``--mem=`` option. In general,
for parallel jobs you do not need to specify a memory limit. You can specify
the memory limit on the command line with using --mem option (for example
``--mem=2g`` to specify 2 GB of memory) or as an #SBATCH directive within the
job file.

For parallel jobs it is not necessary to specify the
memory requirement, but if each of your tasks requires more than its share of
memory on the node, the only way to get more memory is to spread the same
number of tasks on more nodes. The Memory High Water mark information
will help you determine how many nodes you would have to use to satisfy the
memory requirements of your job. There are a couple of different ways of
getting the memory usage information about your job.

Using report-mem utility in batch jobs
--------------------------------------

To get the maximum amount of memory (also called "Memory High Water mark") used
up to a specific point in your job, you can add the following command to your
job file:

   ``report-mem``

Typically, the best place to put this command is the end of your job
file or altered exit points if your jobs are written such that they may exit
before the end.

There may be instances where this is not feasible because you
don't have direct access to the job file. For example, you might be using other
scripts to generate job files on the fly, where users have the option to
specify launch option in a "config" file. In those instances, you can get a
memory report for your parallel jobs using ``--epilog`` option of the srun
command as shown below:

.. code-block:: shell

   srun --epilog=/apps/local/bin/report-mem   wrf.exe

Using report-mem utility on a job that is currently running
-----------------------------------------------------------

If your job is currently running on the system and you would like to find the
Memory High Water Mark up to that point, use
the ``report-mem`` command from a
login node on that job, as in the example below:

.. code-block:: shell

    hfe03.% report-mem -j 4665051
    Peak memory usage summary:
    min = 11139788 KB
    ave = 11181442 KB
    max = 11261556 KB
    All nodes sorted by peak memory as percentage of limit: (in KB)
    % of user user user total total
    Node limit max limit current current phys
    h16c50 12.0 11261556 94208000 11259356 14455952 97609020
    h25c22 11.9 11208488 94208000 11207184 14486172 97609020
    h25c17 11.9 11178112 94208000 11177692 14508136 97609024
    h25c40 11.8 11152296 94208000 11151424 14451696 97609024
    h25c48 11.8 11148416 94208000 11147668 14445588 97609024
    h25c20 11.8 11139788 94208000 11139672 14465660 97609024
    hfe03.%

Determining the amount of memory used by a process
--------------------------------------------------

The techniques above give you the amount of memory used on each node,
rather than the amount of memory used by each task.

To find the amount of memory used by each task, use this method:

    Submit the job, but use a full node (using ``sbatch -N 1 ...`` for example)

If your execute line is:

   ``./myexe``

replace it with

   ``/usr/bin/time ./myexe``

If you search for the string "elapsed", you will find a line resembling the
following:

.. code-block:: shell

   1.34user 15.57system 0:22.76elapsed 74%CPU (0avgtext+0avgdata 7822876 maxresident)k


which shows that this process used approximately 7.8 GB of memory.

When you are ready to run the job in production you can request one task and
the appropriate amount of memory by doing something like the following:

.. code-block:: shell

    sbatch --ntasks=1 --mem=8000M ... jobfile

While the prefixes M and G both work, the number specified must be an integer.
If you would prefer that the single-core job allocates the entire node, use one
of the following options:

    ``#SBATCH --exclusive``

or

    ``#SBATCH --nodes=1``

The same technique is used for parallel jobs. The main difference will be that
you need to replace the launch line as follows.

If your mpi launch command is:

   ``srun ./wrf``

you should change that to:

   ``srun -l /usr/bin/time ./wrf``

The report wil list the amount of memory used by each task. You can
calculate the memory used on each node by determining how many tasks were
placed on each node.

Shown below is a sample report using the grep command to filter and show only
output of interest, sorted by rank order:

.. code-block:: shell

   hfe03.% grep maxresident osu-osu_mbw_mr-0002-04.o4885268 | sort
   0: 15.98user 3.06system 0:19.67elapsed 96%CPU (0avgtext+0avgdata 23928maxresident)k
   1: 16.23user 2.68system 0:19.67elapsed 96%CPU (0avgtext+0avgdata 23984maxresident)k
   2: 16.42user 2.62system 0:19.67elapsed 96%CPU (0avgtext+0avgdata 23984maxresident)k
   3: 16.35user 2.55system 0:19.67elapsed 96%CPU (0avgtext+0avgdata 23868maxresident)k
   4: 15.99user 3.13system 0:19.64elapsed 97%CPU (0avgtext+0avgdata 21976maxresident)k
   5: 16.24user 2.67system 0:19.64elapsed 96%CPU (0avgtext+0avgdata 23996maxresident)k
   6: 16.45user 2.67system 0:19.64elapsed 97%CPU (0avgtext+0avgdata 21952maxresident)k
   7: 16.40user 2.57system 0:19.64elapsed 96%CPU (0avgtext+0avgdata 24020maxresident)k
   hfe03.%

In this example, each task used approximately 23900 KB (or 23 MB) of memory.

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

.. _slurm-monitoring-jobs:

Monitoring Jobs
===============

The commands ``squeue``, ``scontrol`` and ``scancel`` from the :ref:`common
slurm commands table <slurm-common-commands>` will allow users to view,
monitor, cancel, and discover information about their jobs on the system.

Show Pending and Running Jobs
-----------------------------

Use the ``squeue`` command to view a list of current jobs in the queue.  See
``man squeue`` for more `information <squeue_>`_.

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
:math:`>0.5` indicates the project is underutilized.

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
    the system, which is currently 1-days (ex. current usage 100%, 1 day old
    usage 50%, 2 day old usage 25%, etc).

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
sfairshare use the ``sfairshare -h`` command.

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

.. _slurm-generating-reports:

Generating Reports
==================

Several of the Slurm utilities can be used to generate usage reports.  Slurm
supplies :ref:`slurm-sreport`.  The RDHPCS team supplies :ref:`slurm-shpcrpt`.
Both tools can generate similar reports.

See the following for more information:

.. toctree::

   sreport
   shpcrpt

.. _slurm-references:

References
==========

Further information about Slurm, and the Slurm commands are available using
``man <command>`` on all RDHPCS systems, or on the SchedMD documentation site.

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
