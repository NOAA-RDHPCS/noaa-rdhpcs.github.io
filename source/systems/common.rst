*******************
General Information
*******************

Welcome to RDHPCS CommonDocs -- Information and procedures that
pertain across all RDHPCS systems.

The RDHPCS Maintenance Downtime Calendar has events for NESCC (Hera,
HPSS, Niagara), Jet, Boulder and Princeton Bastions, and other RDHPCS
system downtimes. `View the Calendar
<https://calendar.google.com/calendar/u/1/r?id=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

.. raw:: html

   <div>
   <iframe src="https://calendar.google.com/calendar/embed?src=noaa.gov_f1ggu43tm9lfeeg45t59a063cs%40group.calendar.google.com&ctz=America%2FNew_York"
           style="border: 0"
           width="800"
           height="600"
           frameborder="0"
           scrolling="no"></iframe>
   <p>You must be logged in to your NOAA Gmail account to see the calendar.</p>
   </div>

RDHPCS Platforms
================

.. tab-set::

   .. tab-item:: Gaea

      Climate Modeling and Research System (CMRS) at Oak Ridge
      National Laboratory `More Information
      <https://www.noaa.gov/organization/information-technology/gaea>`__

   .. tab-item:: Hera

      Predicting high-impact weather events `More Information
      <https://www.noaa.gov/organization/information-technology/hera>`__

   .. tab-item:: Jet

      Hurricane Forecast Improvement Program (HFIP) `More Information
      <https://www.noaa.gov/organization/information-technology/jet>`__

   .. tab-item:: Niagara

      Collaborative resource for data transfer `More Information
      <https://www.noaa.gov/organization/information-technology/niagara>`__

   .. tab-item:: MSU-HPC

      High-performance Computing collaboration with Mississippi State
      University (MSU) `More Information
      <https://www.noaa.gov/organization/information-technology/orion>`__


   .. tab-item:: Cloud

      Platform to create and use HPC computatational clusters on an
      as-needed basis. `More Information
      <https://www.noaa.gov/information-technology/hpcc>`__


.. note::

   mpirun" is preferable for non-uniform placement or MPMD jobs.

Batch Scripts
-------------

Batch jobs require a batch script that runs the commands and applications you
want to execute. Batch scripts are shell scripts (sh, bash, ksh, csh). If you
do not already have a script to run the commands you want to execute, you must
create one. Here is an example batch script called jobscript.sh that runs the
xhpl MPI program.

.. code-block:: shell

   #!/bin/ksh -l

   module load intel <version>
   module load impi <version>

   srun -n 12 ./xhpl


To submit the jobscript.sh script, you would execute:

.. code-block:: shell

   $ sbatch &lt;options&gt; jobscript.sh

Loading Modules
^^^^^^^^^^^^^^^

If you loaded modules when building your code, they must be loaded when the
job runs as well. This means that you must put the same module commands in your
batch scripts that you ran before building your code.

Modules with sh, bash, and ksh scripts
""""""""""""""""""""""""""""""""""""""

To conform to the POSIX standard for bash, sh, and ksh you **MUST** add the
``-l`` option (that is a lowercase L) to the shebang (e.g. ``#!/bin/bash``)
line at the top of your script for all sh, bash, or ksh batch scripts.

For example:

.. code-block:: shell

   #!/bin/ksh -l

   module load intel <version>
   module load impi <version>

   srun -n 12 ./xhpl

If you omit the -l, the module commands will fail and your job will not run
properly, and even may crash.

More information for using modules can be found in :ref:`Modules <Modules>`.

Module Loading Best Practices
""""""""""""""""""""""""""""""

.. note::

   Do Not Load Modules at Shell Initialization.

Upon user interactive login, running batch jobs, running cron scripts, and
running command line scripts, a linux shell is invoked. The way the shell is
invoked determines which shell initialization scripts (~/.cshrc, ~/.tcshrc
~/.bashrc,~/.bash_profile, Etc.) are invoked at start up, and how the shell's
environment will be set up. Although it can be estremely useful and beneficial
to customize these shell scripts, we have seen a large number of issues related
to loading modules within these shell scripts.

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

Job Submission Options
----------------------

sbatch options
^^^^^^^^^^^^^^

You are allowed to specify options from teh set used for the
SLURM batch system. For a list of options, you may look at the man page:

``$ man sbatch``

or the command usage statement:

``$ sbatch --help``

Additional sbatch information can be found at the `vendor's website <https://slurm.schedmd.com/sbatch.html>`_.

Command-line options vs directive options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two way to specify sbatch options. The first is on the command line
when issuing the sbatch command. For example,

``$ sbatch -A fim --ntasks=256 jobscript.sh``

The second method is to insert directives at the top of the batch script using
#SBATCH syntax. For example:


.. code-block:: shell

   #!/bin/bash -l

   #SBATCH -A fim
   #SBATCH --ntasks=256

The two methods may be mixed together, if desired. Options specified on the
command line always override options specified in the script.

A Quick Start Batch Script Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This script is a very basic template that provides examples for some common
sbatch options. It also includes the required options. This can be
used as a general guide when constructing a new batch script.

.. code-block:: shell

   #!/bin/bash -l
   #
   # -- Request that this job run on sJet
   #SBATCH --partition=sjet
   #
   # -- Request 16 cores
   #SBATCH --ntasks=16
   #
   # -- Specify a maximum wallclock of 4 hours
   #SBATCH --time=4:00:00
   #
   # -- Specify under which account a job should run
   #SBATCH --account=hpl
   #
   # -- Set the name of the job, or Slurm will default to the name of the script
   #SBATCH --job-name=HPL
   #
   # -- Tell the batch system to set the working directory to the current working directory
   #SBATCH --chdir=.

   nt=$SLURM_NTASKS

   module load intel <version>
   module load impi <version>

   srun -n $nt ./xhpl


.. note::

   The variable $SLURM_NTASKS is used in the example above so that the rest
   of the script can stay portable. If you want to change the number of cores
   used, you only change the submission, not how that value is used in the rest of
   the script.

To submit the above script, called jobscript.sh, you would type:

``$ sbatch jobscript.sh``

Specifying the project account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use -A (--account) to specify the project that will be charged when your job is
run. **You are required to specify an account when a job is launched.**

``$ sbatch -A fim``

To find out which projects you are authorized to use, see
:ref:`slurm-getting-information-about-your-projects`.

Specifying a Partition
^^^^^^^^^^^^^^^^^^^^^^

**Fair Job Billing** SLURM adjusts the Effective Usage (EffectvUsage) and
FairShare Factor of a completed job based the
Billing Trackable RESources (TRes).
For each partition we have set a Billable TRes for per core performance based
on standard performance tests (see the partition tables below for each system).
Jobs run on partitions with slower per core performance will have a lower
EffectvUsage, and therefore maintain a higher FairShare Factor, which means a
higher priority for future jobs. The result is that your project's priority
decay based on recent usage (FairShare Factor) will be handled fairly,
independent of partition. A project's actual core-hour usage is not effected by
Billable TRes factors, so monthly usage reports like shpcrpt used to report
system utilization will report actual core-hours used independent of relative
core performance.

Use the sinfo command for partition, node, state, and availability information.

.. code-block:: shell

   $ sinfo

Use the sacctmgr command to get information about what combination of
Accounts/QOS you have access to (and their limits):

.. code-block:: shell

      $ sacctmgr show associations where user=$USER format=Cluster,Account%20,User%20,QOS%60,partition,maxjobs,maxsubmitjobs


Jet Partitions
--------------

To see current overall Jet compute status/usage by partition, and Jet scratch
file system status/usage, see the :ref:`jet-user-guide`.


Visit the Jet System Information page for more information on each partition:

The following Jet partitions and Jet Billable TRes Factors are defined:

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Partition
     - QOS Allowed
     - Billable TRes per Core Performance Factor
     - Description
   * - sjet
     - batch,windfall, debug, urgent, novel
     - 145
     - General compute resource - Intel Sandybridge
   * - vjet
     - batch,windfall, debug, urgent, novel
     - 165
     - General compute resource - Intel IvyBridge
   * - xjet
     - batch,windfall, debug, urgent, novel
     - 150
     - General compute resource - Intel Haswell
   * - kjet
     - batch,windfall, debug, urgent, novel
     - 165
     - General compute resource - Intel Skylake
   * - bigmem
     - batch,windfall, debug, urgent
     - 150
     - Large memory jobs; 4 nodes, each with 24 cores and 256 GB of memory - Intel Haswell
   * - novel
     - novel
     - 165
     - Partition for running novel or experimental jobs where nearly the full
       system is required. If you need to use the novel QOS, please sumbit a
       ticket to the help system and tell us what you want to do. We will
       normally have to arrange for some time for the job to go through, and we
       would like to plan the process with you. Please note that if you use
       **novel partition** you also need to specify **novel QoS.**
   * - service
     - batch,windfall, debug, urgent
     - 0
     - Serial jobs (max 1 core), with a 24 hr limit. Jobs will be run on front
       end (login) nodes that have external network connectivity. Useful for
       data transfers or access to external resources like databases. If you
       have a workflow that requires pushing or pulling data to/from the
       HSMS(HPSS), this is where they should be run. See the Login (Front End)
       Node Usage Policy for important information about using Login nodes.

To see a list of the available partitions use the command:

.. code-block:: shell

   $ sinfo -O partition
   sjet
   vjet
   xjet
   kJet

   bigmem
   service

Selecting General compute resources on Jet: Unless you have a real-time
reservation (see below), and to assure the all partitions are used most
efficiently, we recommend that you specify the use of the default, **all**
general compute resource partitions. This option gives the batch scheduler the
flexibility to put your job on the first available resource. To do this, you
must choose compilation options that create executables that can be used on any
partition, which is covered in the Recommended Intel Compiler Options for
Optimization section in the :ref:`jet-user-guide`.

On Jet the processor architecture, cores per node and memory per core varies
for each partition so your execution time may vary slightly; therefore it is
important to understand the architectural differences, so you understand how
your code will run and perform on various partitions.

To specify all Jet General Compute Resource Partitions (the default), so your
job will run on the first available partition, **do not specify a
partition.**

Hera Partitions
---------------

For more information on each partition, see the :ref:`hera-user-guide`.

To specify a partition, use the command `partition -p`. For example:

.. code-block:: shell

   sbatch -p batch ...

The following partitions are defined:

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

Requesting a Single Partition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To specify a single non-default partition for your job, use:  `-p
(--partition)`

.. code-block:: shell

   #SBATCH --partition=service

to request service

Requesting Multiple Partitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a system has multiple general compute resource partitions (ex: Jet), we
recommend that you request all general compute resource partitions on that
system, unless you have well understood reason not to do so. This approach can
significantly reduce wait time for your jobs to start (qwait) and will improve
overall system utilization. With SLURM there is no new job priority penalty for
using slower cores (see Billable TRes above). Jobs will always run within a
single partition, never spanning multiple partitions.

To request multiple partitions, list the partitions separated by a comma. For
example, on Jet to use only the xJet and kJet general compute resource
partitions, specify:

.. code-block:: shell

   #SBATCH --partition=xjet,kjet

Specifying the number of cores for your job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use `--ntasks`` to set the total number of cores required for your job.

.. code-block:: shell

   #SBATCH --ntasks=12

This is the correct way to set the number of procs (cores) needed to run a job.
If you need to change the processor layout, refer to the next section for
instructions. For the maximum core count allowed per QOS, see the table below.

Specifying a processor layout for your job (uniform layout example)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simple method of laying out tasks where all the cores on a node are used
with one MPI task per core works reasonably well for most applications.  These
are however cases where the default amount of memory available per core is
insufficient and need more memory than is available.

In those instances, it will be necessary to spread out tasks on more nodes so
that there are fewer MPI tasks on a node than there are cores.  The other cores
may be left idle or could be used for speeding up the code by using threads.

For example on a machine that has 12 cores per node, the default layout
mentioned above would use all the 12 cores per node.  If each task needs twice
the amount of memory, then you would have to place only 6 MPI tasks on each
node.

In the example below, even though there are 12 cores available on the node,
only 6 MPI tasks are placed on a node so that each task gets double the amount
of memory than using all the 12 cores.

.. code-block:: shell

   #SBATCH --nodes=4
   #SBATCH --ntasks-per-node=6

The --cpus-per-task option can be used to specify layout for a threaded job
(e.g. OpenMP). For example, a hybrid MPI/OpenMP job where each MPI process uses
2 threads:

.. code-block:: shell

   #SBATCH --nodes=4
   #SBATCH --ntasks-per-node=3
   #SBATCH --cpus-per-task=2


   export OMP_NUM_THREADS=2          # Note that this is needed too!
   srun ./myexe

Other examples:

.. code-block:: shell

   #SBATCH --nodes=12
   #SBATCH --ntasks-per-node=1

The above example will start the job on 12 nodes, with one task/thread per
node.

.. note::

   **--nodes=20** is not the same as **-nodes=20 --ntasks-per-node=12**. By
   default, 1 task per node is used. It is best to always explicitly list the
   --ntasks-per-node (or --ntasks) expression that you need.


**It is required that the user specify the number of tasks they want, either
with -n (--ntasks) or -N (--nodes) or both.** Failing to specify the number of
tasks will result in a job submission error.

Example for WRF
"""""""""""""""

WRF is a good example where non-uniform placement is required, as the first
task usually requires a lot more memory than the remaining tasks.

In this example, we will look at a case where WRF needs 12 MPI tasks. Assume
that the first task needs a lot of memory, and that we would like to place the
first task on a node by itself.

If we have a machine that has 40 cores per node and we cannot fit all the 12
MPI tasks on one node, we would like to run the job on 2 nodes and 12 MPI
tasks, placing **(1+11)** MPI tasks on those two nodes.

For this example the job file would look like this:

.. code-block:: shell

    #SBATCH --nodes=2
    #SBATCH --ntasks=12

    module use -a /contrib/sutils/modulefiles
    srun -m arbitrary -w `arbitrary.pl 1,11` ./wrf.exe


Setting the --cpus-per-task parameter
"""""""""""""""""""""""""""""""""""""

.. note::

   We are still investigating this issue and will update it as we learn more.


With the update of Slurm from 20.11.7 to 21.08.5 , the behavior of
enforcing memory limit for the job-step by Slurm has changed from the previous
version resulting in some users seeing **"Out of Memory"** or **OOM**
errors. Please note that this is not a bug but a fix for an issue that was
more lax in its previous implementation.  Jobs that took advantage of the lax
implementation in the previous version may see the "out-of-memory" errors with
this new implementation. <p> Please keep in mind that when you specify
**"--cpus-per-task"** option on the sbatch command, **each job-step only
gets its proportional share of memory!**  If you leave that option out on the
sbatch command, or if you specify **"--mem=0"** then each of the job-steps,
launched by srun within a job, will be able to use all the available memory
allocated for that job.  Please note that how much memory is allcated to the
job depends on whether the job is a "shared" job or an "exclusive" job.  On
Hera and Jet, currently all the non-serial jobs get exclusive access to the
node whereas on the MSU systems the default is "non-exclusive".  It is worth
noting that as core counts increase on the newer processors "exclusive" will be
the preferred option, so non-MSU systems also may move towards "non-exclusive"
or "shared" mode in the future.


There may be situations your job where you do need this option on sbatch for
your parallel job-step but there are serial job-steps in the same job that need
more memory than what is available based on the above, in which case it can
over ridden on the `srun` command.

Here is a concrete example:

.. code-block:: shell

   #!/bin/bash -l
   #SBATCH ...
   #SBATCH --cpus-per-task=2           # Each job-step by default only gets 2 CPUs worth of memory
   #SBATCH

   srun $wrf_exe                    # 2 CPUs worth of memory is sufficient for this task

   #  The next task requires 4 times each CPU's share of memory, so we can override it thus
   # even the post processor is a serial task

   srun --cpus-per-task=4 $post        # Without that it will only 2 CPUs worth of memory


As mentioned above, an alternative solution is specify **"--mem=0"** as one of
the SBATCH directives in the job or as a command line option instead of
modifying the srun line.

Specifying a processor layout for your job (non-uniform or arbitrary example)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Some applications require tasks to be laid out non-uniformly. For example a
number of applications have task0 requiring more memory than the remaining
tasks. This requires the capability of doing non-uniform task layout.

The script named ``arbitrary.pl`` is available when module
``sutils``from ``contrib`` is loaded as follows:

.. code-block:: shell

   module use -a /contrib/sutils/modulefiles
   module load sutils


This script can be used to generate a host list that can be used for arbitrary
layout in a couple of different ways.

.. note::

   The script ``arbitrary.pl`` can only be used within a batch job file!

It is best illustrated with a simple example. Suppose we want to run on 3
nodes, with 4 tasks on the first node, 2 on the second and 6 on the third node.
So the task layout would be ( 4 + 2 + 6 ) for a total of 12 MPI tasks on 3
nodes:

.. code-block:: shell

   sbatch --nodes=3 --ntasks=12 ...

And inside the batch job you have:

.. code-block:: shell

   module use -a /contrib/sutils/modulefiles
   module load sutils
   srun -m arbitrary -w `arbitrary.pl 4,2,6` ./a.out

This results in the desired task placement.

 When running on a larger number of nodes it is difficult provide a long list
 of tasks, so the following form is also supported.

Suppose the desired lay out is 1 task on first node and 10 tasks on 4 nodes,
for a total of 41 MPI tasks on 5 nodes; so the desired layout is (1 + 10 + 10 +
10 + 10).

In this case, instead of using the long form:

.. code-block:: shell

   arbitrary.pl 1,10,10,10,10


we can use the multiplier as a short cut as shown below:

.. code-block:: shell

   arbitrary.pl 1,10x4


An alternative approach to above is to use SLURM_HOSTFILE as shown below (bash
example):

 .. code-block:: shell

  module use -a /contrib/sutils/modulefiles
  module load sutils
  arbitrary.pl 1,12x10,3x2 &gt; arb2-$SLURM_JOB_ID
  export SLURM_HOSTFILE=arb2-$SLURM_JOB_ID

  srun -n 127 a.out


Please note that the scripts ``arbitrary.pl`` and ``layout.pl``
are simple perl scripts that are located at:

.. code-block:: shell

   /contrib/sutils/bin/arbitrary.pl
   /contrib/sutils/bin/layout.pl


Please feel free to copy these scripts and modify them to suit your needs.

MPMD example
""""""""""""

Another script called ``layout.pl`` is available when sutils module is
loaded that can be used for MPMD jobs.

The script ``layout.pl`` has a syntax similar to &quot;mpirun&quot; and it
creates a configuration file that is used with --multi-prog option of the srun
command.

It is best illustrated with a simple example:

Suppose we want to run on 12 nodes, using 10 tasks per node, and would like to
launch:

* 20 tasks of a.out
* 60 tasks of b.out
* 40 tasks of c.out

.. code-block:: shell

   sbatch --nodes=12 --ntasks-per-node=10 … slurmjob

   module use -a /contrib/sutils/modulefiles
   module load sutils
   layout.pl -n 20 a.out : -n 60 b.out : -n 40 c.out &gt; lay2-$SLURM_JOB_ID
   srun --multi-prog lay2-$SLURM_JOB_ID

Specifying Wall Clock Time
^^^^^^^^^^^^^^^^^^^^^^^^^^

You should specify a wall clock time for your job. If you do not set a wall
clock time it will **default to 5 minutes**. **We recommend that you do NOT set
a wall clock time less than 5 minutes**. If your jobs will take longer than 5
minutes, request a wall clock time reasonably close to but not less than (see
note below) the actual wall clock time that the job will take to run.
Specifying an excessively large wall clock time will result in increased wait
time for your job to start (qwait), and more importantly reduced scheduler
efficiency and overall system utilization. When requesting Multiple Partitions
(see below), as is recommended, take into account the longest run time
partition. Due to several other factors that effect run time your job run time
on a &quot;slower&quot; partition may be better as compared to the Billable
TRes per Core Performance Factor listed in the Partition tables above.
Therefore:

**Frequently** review the wall clock time of the jobs you run in order to
better estimate your requested wall clock time. Increased accuracy of specified
wall clock time with your job submissions will shorten queue wait times, and
increase scheduler efficiency and overall system utilization.

.. note::

   Any job that runs longer than its requested wall clock time or the partition's
   time limit will be terminated by the scheduler. When specifying your wall clock
   time, add some extra time to your recent observed run time history to be sure
   it will finish: **>10-20%</span>** for short run times, **>5-10%</span>** for
   long run times, to allow for random fluctuations in run times caused by system
   load.

For example, to set a one-hour time limit:

.. code-block:: shell

   #SBATCH --time=1:00:00

For the maximum wall clock allowed see the Queue(QOS) tables below.

Specifying a Quality of Service (QOS) - Jet and Hera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To specify a quality-of-service (QOS), use ``--qos (-q)``. For example, to
specify the batch QOS:

.. code-block:: shell

   #SBATCH -q batch

Several different QOS's are available.

.. note::

   If you have an allocation of "windfall only" (Allocation = 1) you can only
   submit to the windfall or gpuwf QOS.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - QOS
     - Min Cores
     - Max cores
     - Max Wall clock
     - Billing TRES Factor
     - Description - Limits
   * - All QOS's
     -
     -
     -
     -
     - **Across all QOS's**: Max of 400 jobs pending/running per project-account,
       additional jobs will be rejected. Max of 20 jobs per project-account will gain
       age priority. Exceptions are stated below.
   * - batch
     - 1
     - 8400*
     - 8 hours (Partition exceptions: Service: 24 hrs)
     - 1.0
     - **Default**: quality of service for non-reservation jobs with an
       allocation more than "Windfall Only"(RawShares =1).
   * - urgent
     - 1
     - 8400*
     - 8 hours
     - 2.0
     - QOS for a job that requires more urgency than batch. Your project's
       FairShare will be lowered at 2.0x the rate as compared to Batch. Only one
       job per project-account can be pending/running at any time. When a
       project's FairShare is below 0.45, jobs submitted to Urgent are
       automatically changed to Batch and users notified via stderr.
   * - debug
     - 1
     - 8400*
     - 30 minutes
     - 1.25
     - Highest priority QOS, useful for debugging sessions. Your project's
       FairShare will be lowered at 1.25x the rate as compared to Batch. Only 2
       jobs per user can be pending/running at any time. This QOS should NOT be
       used for fast-turnaround of general work. **NOTE:** If you need to debug
       your code through an iterative process, we recommend that you submit a
       long running interactive job to the default QOS. This lets you restart
       your application as needed, without having to start a new batch job.
   * - gpu
     - 20 (1 node)
     - 800 (40 nodes)
     - 168 hours (7 days)
     - 1.0
     - This QOS can only be used on Hera in combination with the **fge** partition.
       Max total “GrpTRESRunMins” of 720,000 core-minutes (600 node-hours) of
       running jobs at any time, per project-account. “GrpTRESRunMins” is
       defined as cores_allocated * wallclock_requested of running jobs. A
       project can have up to the max number of jobs pending/running as defined
       above, but the queued jobs will NOT be considered for scheduling if the
       project’s running jobs exceed this limit. Use this `gsheet as a
       reference
       <https://docs.google.com/spreadsheets/d/16rwriSZA4hQNRndGb_tsxYXg8Ct3oGvETEgD-zeQkBE/edit?gid=1801089973#gid=1801089973>`_
       For example, the following combinations of the max running jobs per
       project-account are permitted:

       * A project can have three 1-node jobs at 168 hours of wallclock
         and one 1-node job at 96 hours of wallclock.
       * A project can have one 8-node job at 75 hours of wallclock.

   * - gpuwf
     - 20 (1 node)
     - 800
     - 168 hours (7 days)
     - 0.0
     - This QOS can only be used on Hera in combination with the **fge**
       partition. Max total “GrpTRESRunMins” of 201,600 core-minutes (168
       node-hours) of running jobs at any time, per project-account.
       “GrpTRESRunMins” is defined as cores_allocated * wallclock_requested of
       running jobs. A project can have up to the max number of jobs
       pending/running as defined above, but the queued jobs will NOT be
       considered for scheduling if the project’s running jobs exceed this
       limit. Use this `gsheet as a reference
       <https://docs.google.com/spreadsheets/d/16rwriSZA4hQNRndGb_tsxYXg8Ct3oGvETEgD-zeQkBE/edit?gid=1801089973#gid=1801089973>`_
       For example, the following combinations of the max running jobs per
       project-account are permitted:

       * A project can have two 2-node jobs at 24 hours of wallclock and
         one 1-node job at 72 hours of wallclock.
       * A project can have one 1-node job at 168 hours of wallclock.

       Lowest priority QOS for use with GPU nodes. If you have an allocation of
       "windfall only" (Monthly allocation = 1) you can only submit to this
       QOS. Submitting to this QOS will NOT affect your future job priority
       FairShare Factor (f). EffectvUsage = 0. See How FairShare Works. This
       QOS is useful for low priority jobs that will only run when the system
       (partition(s)) has enough unused space available, while not lowering the
       project's FairShare priority
   * - windfall
     - 1
     - 8400*
     - 8 hours (Partition exceptions: Service: 24 hours)
     - 0.0
     - Lowest priority QOS If you have an allocation of "windfall only"
       (Monthly allocation = 1) you can only submit to this QOS. Submitting to
       this QOS will NOT affect your future job priority FairShare Factor (f).
       EffectvUsage = 0. See How FairShare Works.
       Windfall QOS is useful for low priorty jobs that will only run when the system
       (partition(s)) has enough unused space available, while not lowering the
       projects FairShare priority.
   * - novel
     - 8401
     - LArgest partition size
     - 8 hours
     - 1.0
     - QOS for running novel or experimental jobs where nearly the full system
       is required. If you need to use the novel QOS, please submit a ticket to
       the Help system and tell us what you want to do. We will normally have
       to arrange for some time for the job to go through, and we would like to
       plan the process with you.
       **NOTE:** The novel QOS can only be used with the novel partition.

.. note::

   Some partitions are smaller than the "Max Cores" QOS limit. Jobs submitted
   only to partitions with an insufficient number of cores will get stuck in
   pending, will **not** run, and will have to be manually deleted by the user.
   The max nodes allowed per partition is the min of the max cores allowed
   divided by the cores per node of the partition (Hera and kJet: 8400/40=210
   nodes) or the max number of nodes in the partition (vJet: 288 nodes).

Changing QOS's
--------------

You can change the QOS of jobs at submission and post submission. While you can
use this feature in many different ways, one practical situation where this may
be useful is to maintain your fairshare priority by starting jobs in the
“windfall” QOS, then changing to the “batch” QOS if it is still pending.

.. note::

   BE CAREFUL:If your job does not meet the criteria of the QOS that you change
   it to, it will remain pending indefinitely.

You can immediately change the QOS of your pending job(s). The following is an
example of immediately changing 2 pending jobs (26866 and 26867) to the “batch”
QOS.

.. code-block:: shell

   scontrol update job 26866,26867 qos=batch

When submitting a job to a certain QOS, you can tell Slurm to change it to a
different QOS at a certain time if it is still pending.  In the following
example, you submit the job to the “windfall” QOS, then tell Slurm to change
the job to the  “batch” QOS if it’s still pending after 5 minutes. <span
style="font-size: 16px">** NOTE:** Do not use a time less than 2 min (120
seconds). <span style="font-size: 16px">** NOTE:** On Orion and Hercules the
“at” functionality is only available on login1.


.. code-block::shell


   jfe01.% sbatch -q windfall jobfile
   Submitted batch job 26990
   jfe01.%


   jfe01.% echo scontrol update job 26990 qos=batch | at -M now +5min
   warning: commands will be executed using /bin/sh
   job 6 at Sun Dec 17 16:07:00 2023
   jfe01.%


You can change the QOS of all your pending job(s) in a QOS to another QOS after
it has been pending for a certain time.  The following example script will
change all your pending “windfall” jobs to “batch” if they have been pending
for at least 600 seconds (10 min), whenever you run it. <span style="font-size:
16px">** NOTE:** Do not use a time less than 120 seconds (2 min).

.. code-block::shell

   Script: windfall2batch.sh
   —-------------
   #!/bin/bash
   # Purpose: Look at my jobs in windfall QOS that are still pending.
   #          If any job has been pending
   #          for more than "time-in-seconds" move those jobs to "batch"
   #
   # Usage: windfall2batch.sh [time-in-seconds]
   # Default time is 600 seconds (10 minutes)

   time=${1:-600}
   squeue -u $USER -t pending -q windfall -O JobID,PendingTime,Reason --noheader | \
      awk -v time=$time '$2 > time && ($3 == "Priority" || $3 == "Resources")      \
            {system("scontrol update job " $1 " qos=batch")}'


You can run the script manually when necessary. If you want to do so routinely,
you may put this in cron at the desired intervals.

Specifying a job Name
^^^^^^^^^^^^^^^^^^^^^

Giving your jobs meaningful names can help you locate them when monitoring
their progress. Use the -J (--job-name) option. For example,

.. code-block:: shell

   #SBATCH -J
   WRF_ARW_00Z

The default name for a job is the name of the job script
that is being submitted.

Setting the names of output files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not specify the names of the output files that contain the stdout and
stderr from your job script, a file will be written to the directory in which
you issued the sbatch command. A file containing both the stdout and stderr
from your job script will be called: slurm-&lt;jobid&gt;.out where
&lt;jobid&gt; is the SLURM job id of the job.

Use the -o (--output) option to specify the name of the stdout file <pre>
#SBATCH -o /full/path/of/stdout/file </pre> Use the -e (--error) option to
specify the name of the stderr file <pre> #SBATCH -e /full/path/of/stderr/file
</pre> If you want stdout and stderr to go to the same file, do not specify the
-e option.

Passing environment variables to the job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default the environment variables set in the current shell is passed to the
job that is submitted. However if any variable is explicitly passed into the
script with a value, only that value is passed to the script!

If you wish to pass local environment to the script and in addition set a
specific variable that is currently not in the current environment
(&quot;ndays=20&quot; in the example below), you can do it in the following
way:

.. code-block:: shell

   sbatch --export=ALL,ndays=20 … sbatch.job

It is important to note that ``ALL`` is required if you want the
local environment variables are to be exported to the script in addition to the
value explicitly set. If ``ALL`` is left out, only the value of
ndays=20 is passed in.

If you do not want to export your local environment, please use the following
syntax:

.. code-block:: shell

   sbatch --export=NONE … sbatch.job

.. caution::

   Not exporting the current environment can be a little tricky
   and likely to cause some errors unless the necessary environment is created in
   the job. It may also require setting ``--export=ALL`` on the
   ``srun`` command within the job.

Requesting email notification about jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the --mail-user and --mail-type options to request notifications by
email when a job enters one or more states. Both options are required. Use the
--mail-user option to specify a comma delimited list of email addresses where
email notifications are to be sent. Use the --mail-type option to specify which
job states you want email notifications for. The most useful notifications
flags passed to --mail-type are NONE, BEGIN, END, and FAIL and can be combined.
A full list of parameters can be found on the sbatch man page.

* FAIL: mail is sent when the job fails with non-zero exit code.
* BEGIN: mail is sent when the job begins execution.
* END: mail is sent when the job terminates.
* NONE: no email is sent.

Example. To send email notification to Joe and Jane when your job starts and
when it terminates, do:

.. code-block::shell

   $ sbatch --mail-user=[mailto:Joe.User@noaa.gov Joe.User@noaa.gov],[mailto:Jane.User@noaa.gov Jane.User@noaa.gov]--mail-type=&lt;the other options go here&gt; myscript.sh

Specifying the working directory as the current directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is good practice to keep your batch scripts portable, and when they get
moved around the working directory is relative to where the script is. To do
this, specify the working directory with the -D (--chdir) option as the current
directory. Ex:

.. code-block:: shell

   #SBATCH -D .

The other way to do this is with the $SLURM_SUBMIT_DIR variable. This variable
stores the path from where your script was submitted. So at the top of your
batch script, add:

.. code-block:: shell

   cd $SLURM_SUBMIT_DIR

Starting a job after a specific date/time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a job is waiting for data to arrive based on time of day (e.g. 12:30Z), the
--begin option allows for a job to hold in the queue until at least the time
(or date/time) specified with the option. For example:

.. code-block:: shell

   #SBATCH --begin=19:25

The above option will cause the job to hold until 19:25 GMT. If resources are
available shortly after 19:25, the job will run. If not, the job will wait
until resources are available (this is not a reservation). Note that if the
sbatch was submitted at 19:26 GMT, the job will hold until 19:25 GMT the next
day!

Date/time can be specified as:

.. code-block:: shell

   YYYY-MM-DD[Thh:mm[:ss]]

YYYY is year, MM is month, DD is day, hh is
hour, mm is minute and ss is second. The letter T is required as a delimiter if
specifying both date and time. All times are considered to be in the future, so

.. code-block:: shell

   2110-12-21T06:30

would be December 21, 2110 at 06:30 GMT.

The ``--begin`` option also accepts an arbitrary amount of time to wait. For
example:

.. code-block::shell

   #SBATCH --begin=now+1hour


will start the job 1 hour from when the
job is launched, if resources are available.

Submitting a serial job
-----------------------

A serial job can be run on a single node. These jobs are scheduled separately
so that the scheduler can pack multiple jobs onto a single node, improving the
overall usefulness of the system. You do not have to specify a specific queue
name. Requesting a single processor will automatically allow sharing of the
compute node.

By default, a serial job gets only its share of the memory available on a node,
about 2 GB/core or so depending on the type of node.  If your serial job needs
more memory than the default, specify that using the "--mem=<mem>" option.

For more information, **How to Get Memory Usage Information** later in this
document.

Running serial tasks as one parallel job
----------------------------------------

 * (method 1 - Slrum Job Arrays)

If you have number of "similar" tasks to be done, the Slurm Job Array feature
may be useful for you.

Running tasks as one parallel job
---------------------------------

* (method 2 - backgrounded processes) ==

Sometimes you have scripts that do similar serial tasks  on
different data files. Instead of submitting a bunch of serial jobs to
accomplish the task, create a parallel job do all of those tasks in one job.

.. code-block:: shell

    sbatch -A nesccmgmt -N 1 --wrap 'myexe file1 file2**&**   myexe2 inp1 out2**&**  **wait** '

Alternatively, one can have the following script named myjob.sh:

.. code-block:: shell

    #!/bin/bash
    set -x
    myexe  file1 file2 **&**
    myexe2 inp1 out2 **&**
    **wait**

which can be submitted with the command:

.. code-block:: shell

    sbatch -A nesccmgmt -N 1 myjob.sh

In the command above, 1 node is requested to run serial tasks (in this case 2
tasks) in the background.  Since the processes have been backgrounded, a "wait"
is required at the end of the job.

Please note that this method only works for single node jobs.  If you are
planning to use more than one node, use the second approach below.

Running serial tasks as one parallel job
----------------------------------------

* (method 3 - using srun "multi-prog" option)

Sometimes you have scripts that do &quot;similar&quot; serial tasks that need
to be done on different data files. Instead of submitting a bunch of serial
jobs to accomplish the task, submit a parallel job to do all of those tasks in
one job.

In the example below we use &quot;echo&quot; as the command but it can be any
script. We have four tasks, so we request four tasks on the submit line, and
indicate in the config file which rank does which task, as shown below:

.. code-block:: shell

   tfe07.% cat serial-tasks.config
   #
   # The format of this file is:
   # Rank  Command [command args]
   #
   0 echo  is processing 00
   1 echo  is processing 01
   2 echo  is processing 02
   3 echo  is processing 03
   tfe07.%

Submit the job using the following (or create an equivalent batch job file):

.. code-block:: shell

   <pre>tfe07.% sbatch -A nesccmgmt -n 4 --wrap &quot;srun -l --multi-prog serial-tasks.config&quot;
   Submitted batch job 520894
   tfe07.%

Once the job has completed:

.. code-block:: shell

   tfe07.% cat slurm-520894.out
   Start prolog.task v19.04.17 on node t0378 for job 520894 :: Fri May 17 17:07:08 UTC 2019
   _______________________________________________________________
   End prolog.task v19.04.17 Fri May 17 17:07:08 UTC 2019
   2: is processing 02
   1: is processing 01
   0: is processing 00
   3: is processing 03
   _______________________________________________________________
   Start Epilog v19.04.17 on node t0378 for job 520894 :: Fri May 17 17:07:10 UTC 2019
   Job 520894 (not serial) finished for user Raghu.Reddy in partition theia with exit code 0:0
   _______________________________________________________________
   End Epilogue v19.04.17 Fri May 17 17:07:10 UTC 2019
   tfe07.%


Submitting an Interactive Job
-----------------------------

An interactive job is useful for tasks, such as debugging, that require
interactive access with a program as it runs. With SLURM there are two ways to
run jobs interactively, srun or salloc. We recommend that you use salloc.

For example, to request two nodes for 30 min (with X11 forwarding so that you
can use X-windows based tools) you can do the following:

.. code-block:: shell

   salloc --x11=first -q debug -t 0:30:00 --nodes=2 -A marine-cpu

When you run the salloc command, you won't get a prompt back until the batch
system scheduler is able to run the job. Once that happens, the scheduler will
drop you into a login session on the head node allocated to your interactive
job. At this point, you will have a prompt and may run commands, such as your
codes or debuggers as desired. In the example above, an srun command is
executed. salloc is similar to sbatch in that it creates an allocation for you
to run in, however only interactive jobs can be run inside the salloc
allocation.

If you need to display X windows back to your desktop screen from within an
interactive job, you must use **ssh -X** when logging in to Jet.**

If you are using x2go and need to use X windows-based tools, then also do an
**ssh -X localhost** before doing the salloc command.

Submitting a job to run a command on a compute node
---------------------------------------------------

Users sometimes need to run simple commands, and there is a tendency to run
them on the login node in an interactive shell.  For compute intensive jobs
doing this puts a heavy load on the login nodes and affects all interactive
users. The command wgrib is one such example.

A better approach is to request an interactive access to a compute node as
described above, or simply submit a job to a compute node without the need for
a script, as shown below.

Instead of running the command on a login node interactively as shown below:

.. code-block:: shell

    wgrib2 grib_file -bin out.bin

one can simply do:

.. code-block:: shell

    sbatch -A <acct> -n 1 -t 30 -q debug --wrap **"wgrib2 grib_file -bin out.bin"**

Please note that if command above needs more memory than the default, you may
need to add something like **"--mem=4g"** (or whatever memory is appropriate).

If you need to run a command that interacts with the user or generates
graphical output, **srun** can be used to run a command on the compute node;
for example, to run a python script on a compute node that generate an image
you can use the following method:

.. code-block:: shell

    srun --pty --x11 -A nesccmgmt -N 1 -t 30 python myplot.py

Please also pay attention the comments in the previous section regarding X11
forwarding.

Submitting a job with arguments
-------------------------------

If you want to submit a script that accepts arguments you need to add the
arguments after the job file name on the sbatch command. It is similar to the
Unix method of passing arguments to a script as shown in the example below:

.. code-block:: shell

   sbatch batch.job arg1 arg2

The command above passes arg1 as $1 and arg2 as
$2 etc. similar to the Unix convention of argument passing.

Submitting jobs with job dependencies
-------------------------------------

SLURM supports the ability to submit a job with dependencies with other jobs. A
simple example is where job Y cannot execute until job X completes. The use of
the -d options (``--dependency=<options>`` is the way to
specify the job dependency.

Review the sbatch manpage for a list of dependency conditions (look for
--dependency in the sbatch options list) that can be used. Usage
format is illustrated in the example script below that includes
&quot;afterok&quot; as a dependency condition.

Here is a simple example of how to run a chain of jobs with dependencies,
assuming that you have a parallel helloworld.f example program in your current
directory. Note the --parsable option that returns just the Job ID from sbatch.

create/edit the file **depend** with the contents:

.. code-block:: shell

   #!/bin/bash
   jid1=$(sbatch --parsable -n1 -A nesccmgmt -J sim --wrap=&quot;srun sleep 10&quot;)
   jid2=$(sbatch --parsable -n1 -A nesccmgmt -J post --dependency=afterok:$jid1 --wrap=&quot;srun hostname&quot;)

then make it executable:

.. code-block:: shell

   chmod 0755 depend

Initiate the sequence of dependent jobs by

executing **depend** from the command line:

.. code-block:: shell

   ./depend

Notification about dependent jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default you do not get any email notifications of your jobs. For jobs with
dependency, it may be desirable to know if a job has been removed because the
dependency can never be satisfied. In those cases it may be useful to submit
dependent jobs with following notification options:

.. code-block::s hell

   --mail-type=END
   --mail-user=$[mailto:USER@noaa.gov USER@noaa.gov]

With these options you
will get a notification when the job ends, and if the job is removed you will
get an email with the following subject:


.. code-block:: shell

   Slurm Job_id=423748 Name=gfs-post Ended, Run time 00:00:00, CANCELLED, ExitCode 0



How to Get Memory Usage Information
-----------------------------------

You can use the ``report-mem`` command
in your job to get memory usage information from your batch job as mentioned in
the section below.  But this works only if you are able to successfully run
your job to conclusion without failing.

But if you don't know how much memory your application needs, you can "over
estimate" or use an entire node to get a successful run and include the
"report-mem" command in the job as mentioned in the next section. To request
all the available memory on the node for a serial job you can use the
**--mem=0** option on the sbatch command.

If your jobs are failing with memory errors, it is possible that your
application needs more memory than what you were giving for the job. In the
case of serial jobs (which means you may have other jobs running on the same
code and that your job is running), by default to get a certain amount of
memory.  If your application happens to need to more memory than the default,
you need to specify the memory needed by your job using the "--mem=" option.

In general, for parallel jobs you do not need to specify a memory limit.

You can specify the memory limit on the command line with using **--mem**
option (for example "--mem=2g" to specify 2 GB of memory) or as an #SBATCH
directive within the job file.

Note that for parallel jobs it is not necessary to specify the memory
requirement, but if each of your tasks requires more than its share of memory
on the node, the only way to get more memory is to spread the same number of
tasks on more nodes.  Getting the Memory High Water mark information will help
you determine how many nodes you would have to use to satisfy the memory
requirements of your job.

There are a couple of different ways of getting the memory usage information
about your job.

Using report-mem utility in your batch jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get the maximum amount of memory (also called "Memory High Water mark") used
up to a specific point in your job, you can add the following command to your
job file:

.. code-block:: shell

    report-mem

Typically, the best place to put this command would be at the end of your job
file or altered exit points if your jobs are written such that they may exit
before the end.

There may be instances where the above solution is not feasible because you
don't have direct access to the job file.  For example, you might be using
other scripts to generate job files on the fly, where users have the option to
specify launch option in a "config" file.  In those instances, you can get a
memory report for your parallel jobs using "--epilog" option of the srun
command as shown below:

.. code-block:: shell

    srun --epilog=/apps/local/bin/report-mem   wrf.exe

Using report-mem utility on a job that is currently running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your job is currently running on the system and you would like to find out
the Memory High Water Mark up to that point, use the "report-mem" command from
a login node on that job, as shown in the example below:

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The techniques above give you the amount of memory used on each node as opposed
to giving you the amount of memory used by each task.

To find the amount of memory used by each task, use this method:

# Submit the job, but use a full node (using "sbatch -N 1  ..." for example)

If your execute line is:

.. code-block:: shell

    ./myexe

replace it with

.. code-block:: shell

    **/usr/bin/time** ./myexe

If you search for the string "elapsed" you will find a line resembling the
following:

.. code-block:: shell

    1.34user 15.57system 0:22.76elapsed 74%CPU (0avgtext+0avgdata **7822876
    maxresident**)k


which shows that this process used approximately **7.8 GB** of memory

When you are ready to run the job in production you can request one task and
the appropriate amount of memory by doing something like the following:

.. code-block:: shell

     sbatch --ntasks=1 **--mem=8000M** ... jobfile

While the prefixes M and G both work, the number specified must be an integer.

If you would prefer that the single-core job allocates the entire node, use one
of the following options:

.. code-block:: shell

   #SBATCH --exclusive

or

.. code-block:: shell

   #SBATCH --nodes=1


The same technique is used for parallel jobs.  The main difference will be that
you need to replace the launch line in the following way:

If your mpi launch command is:

.. code-block:: shell

   srun ./wrf


you should change that to:

.. code-block:: shell

   srun -l /usr/bin/time ./wrf


The report you get will be the amount of memory used by each task. You can
calculate the memory used on each node by determining how many tasks were
placed on each node.

Shown below is a sample report using the grep command to filter and show only
output of interest, sorted by rank order:

.. code-block:: shell

    hfe03.% grep maxresident osu-osu_mbw_mr-0002-04.o4885268 | sort
    0: 15.98user 3.06system 0:19.67elapsed 96%CPU (0avgtext+0avgdata **23928maxresident**)k
    1: 16.23user 2.68system 0:19.67elapsed 96%CPU (0avgtext+0avgdata **23984maxresident**)k
    2: 16.42user 2.62system 0:19.67elapsed 96%CPU (0avgtext+0avgdata **23984maxresident**)k
    3: 16.35user 2.55system 0:19.67elapsed 96%CPU (0avgtext+0avgdata **23868maxresident**)k
    4: 15.99user 3.13system 0:19.64elapsed 97%CPU (0avgtext+0avgdata **21976maxresident**)k
    5: 16.24user 2.67system 0:19.64elapsed 96%CPU (0avgtext+0avgdata **23996maxresident**)k
    6: 16.45user 2.67system 0:19.64elapsed 97%CPU (0avgtext+0avgdata **21952maxresident**)k
    7: 16.40user 2.57system 0:19.64elapsed 96%CPU (0avgtext+0avgdata **24020maxresident**)k
    hfe03.%

In the example above each task used approximately **23900 KB** (or **23 MB**)
of memory.

== Big/dedicated runs - Using the "novel" QoS == The **novel** QoS is set up to
handle special situations, particularly for large jobs requiring a large number
of nodes (typically for "limited" time):

A couple of examples are given below:

* Users may have an occasional need to run very big jobs that would normally
  not fit within the limits of the "batch" QoS.
* Users may have a need to do some scalability studies that may require running
  up to a very large node count.

It would be very disruptive to schedule such big jobs during normal production
time.  So jobs in the novel QOS would typically be run at the end of
maintenance downtimes.

If you have such needs **please submit a helpdesk ticket** with the subject
line "**Request for running jobs in novel QoS**" and provide the following
information:

* How many jobs will you be submitting?
* What is the number of nodes your biggest job would need?
* What is the maximum length of estimated time your jobs would need to be
  completed?
* If there are multiple jobs can they all be run at the same time?
* Can other jobs be run at the same time as your jobs or do you need
  "exclusive" access?
* Do you need to be able to monitor your runs when your jobs are running? As
  mentioned above, jobs in the novel QoS will normally be run during downtimes
  and users typically don't have access to the machine to do the monitoring.

Best effort will be made to schedule those runs at the end of maintenance
downtimes that typically happen once a month.

Real-time Reservations
----------------------

If you have a real-time reservation it will be assigned a time slot on a set of
nodes on a single partition. You will be giving separate specific directions
how to specify the nodes that are allocated to you.


Monitoring Jobs
===============

List jobs
---------

Use the squeue command to get a listing of the current jobs in the queue.

.. code-block:: shell

   $ squeue
               JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               30049      kjet     test Kyle.Ste  R       0:02      1 t758

List jobs that belong only to you
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the -u option to list only the jobs that belong to you. Provide your
username as an argument to -u. This is preferable to using 'squeue | grep' to
extract the jobs that belong to you for two reasons. First, this method allows
you to see which of the jobs are active, eligible, and blocked. Second,
usernames are truncated in the squeue output, making it hard to grep.

.. code-block:: shell

   $ squeue -u &lt;user name&gt;


List jobs that have completed within the last 24 hours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the sacct command option to list jobs that have run within the last 24
hours and to see their statuses (State). A full list of sacct options and job
states can be found on the sacct man page.

.. code-block:: shell

   tfe03.% sacct --user $USER --starttime `date --date=&quot;yesterday&quot; +%F` -X --format=JobID,JobName%30,Partition,Account,AllocCPUS,State,Elapsed,QOS
         JobID                        JobName  Partition    Account  AllocCPUS      State    Elapsed        QOS
   ------------ ------------------------------ ---------- ---------- ---------- ---------- ---------- ----------
   492264                      hello-slurm.job      theia  nesccmgmt         48     FAILED   00:00:05   windfall
   492295                      hello-slurm.job      theia  nesccmgmt         48 CANCELLED+   00:00:01   windfall
   492299                      hello-slurm.job     bigmem  nesccmgmt         48     FAILED   00:00:07   windfall
   492314                      hello-slurm.job     bigmem  nesccmgmt         48     FAILED   00:00:04   windfall
   504402        NPB-128-mvp2-mg-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:00:27      batch
   504403        NPB-128-mvp2-cg-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:00      batch
   504404        NPB-128-mvp2-lu-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:22      batch
   504405        NPB-128-mvp2-ft-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:29      batch
   504411       HELLO-2-12-hello_mpi_c-intel-+      theia  nesccmgmt         48  COMPLETED   00:00:06      batch
   505240        NPB-128-mvp2-mg-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:00:23      batch
   505241        NPB-128-mvp2-cg-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:01      batch
   505242        NPB-128-mvp2-lu-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:22      batch
   505243        NPB-128-mvp2-ft-intel-mvp2-D-      theia  nesccmgmt        144  COMPLETED   00:02:24      batch
   tfe03.%



Query detailed job status information for a specific job
--------------------------------------------------------

Use the ``scontrol show job`` command to query detailed information
about queued or running jobs or jobs that have finished in the last 15 minutes.
This could be useful when trying to determine why a job is not running and has
remained queued for a long time. Note that this information is only available
from the time the job is launched until 5 minutes after it has completed on
theia and 3 hours on jet.

.. code-block:: shell

   $ scontrol show job 251091
   JobId=251091 JobName=test
      UserId=Kyle.Stern(20411) GroupId=nobody(502) MCS_label=N/A
      Priority=304406866 Nice=0 Account=nesccmgmt QOS=debug
      JobState=COMPLETED Reason=None Dependency=(null)
      Requeue=1 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
      RunTime=00:00:03 TimeLimit=00:20:00 TimeMin=N/A
      SubmitTime=2019-03-29T17:51:37 EligibleTime=2019-03-29T17:51:37
      AccrueTime=2019-03-29T17:51:37
      StartTime=2019-03-29T17:51:37 EndTime=2019-03-29T17:51:40 Deadline=N/A
      PreemptTime=None SuspendTime=None SecsPreSuspend=0
      LastSchedEval=2019-03-29T17:51:37
      Partition=theia AllocNode:Sid=tfe09:99898
      ReqNodeList=(null) ExcNodeList=(null)
      NodeList=t[1145-1161]
      BatchHost=t1145
      NumNodes=17 NumCPUs=408 NumTasks=400 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
      TRES=cpu=408,mem=1020000M,node=17,billing=408
      Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
      MinCPUsNode=1 MinMemoryCPU=2500M MinTmpDiskNode=0
      Features=(null) DelayBoot=00:00:00
      OverSubscribe=NO Contiguous=0 Licenses=(null) Network=(null)
      Command=/home/Kyle.Stern/ticket_146
      WorkDir=/home/Kyle.Stern/.
      StdErr=/home/Kyle.Stern/./slurm-251091.out
      StdIn=/dev/null
      StdOut=/home/Kyle.Stern/./slurm-251091.out
      Power=


Query a job's estimated start time
----------------------------------

Use the &quot;squeue --start&quot; command to get a point-in-time estimate of
when your job may start. Reservation based start time estimation incorporates
information regarding current administrative, user, and job reservations to
determine the earliest time the specified job could allocate the needed
resources and start running. In essence, this estimate will indicate the
earliest time the job would start assuming this job was the highest priority
job in the queue.

.. code-block:: shell

    squeue --start
             JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
            251092     theia     test Kyle.Ste PD 2019-03-29T18:55:58     17 (null)               (BeginTime)


Please note: The start time estimate can change drastically, depending
on the number of partitions specified, new jobs being submitted to the queue,
and how accurately idle jobs and running jobs have specified their wall clock
time.

Deleting jobs
-------------

To cancel a job use the scancel command

.. code-block:: shell

   $ scancel $JOBID

Job Preemption
--------------

During Hurricane season (usually from July 1 thru Oct 31) job preemption may be
in effect for some reservations. All users will be notified when preemption is
in effect and on what partition(s) it exists. Preemption means that non
realtime jobs are eligible to be preempted (killed) to allow the project with
preemption rights on a certain set of nodes to run at a set time. Preemption
only occurs when the scheduler is unable to run a realtime job due to lack of
space. Jobs with less wall clock time remaining are less likely to be
preempted. Users should, therefore, avoid requesting more wall clock time than
is necessary in order to minimize their chances of being preempted. Realtime
jobs running under a standing reservation or in a realtime queue are not
eligible for preemption as they already have their and nodes and time slot
reserved. When jobs are preempted, they are killed and automatically requeued
at the same priority they had when they previously started to run. If you do
not wish your job to be requeued when it is preempted, you must submit it using
the &quot;--no-requeue&quot; option.

Useful variables in the batch environment
-----------------------------------------

The variables listed below are created in your job's environment by the batch
system. Developers have found these useful as ways to make batch scripts more
intelligent and limit hard-coding information about your job in the
environment.

.. code-block:: shell

   $SLURM_JOB_ID - The jobid of the currently running job
   $SLURM_SUBMIT_DIR - The directory from which the batch script was submitted
   $SLURM_JOB_QOS - The assigned quality of service (qos) for this job
   $SLURM_NTASKS - The number of tasks assigned to this job

Charging Algorithm for Your Jobs
================================

Most jobs are charged only based on the amount of wall clock time **used** by
the jobs, not based on the amount of time **requested** for the jobs. Exception
to this is a rule are jobs run in a reservation, which are charged based on the
length of the reservation.

The units allocated and the numbers reported by the command
<code>saccount_params</code> are in **core-hours**.

Charging is done differently for serial and parallel jobs and serial jobs.

In the notes below, we will use **CPN** as "Cores Per Node"; this number
depends on the machine and the partition you are running on, and here are some
examples based on the current hardware:

* Hera - 40 cores per node
* xJet - 24 cores per node
* sJet - 16 cores per node, etc

**Charging for parallel jobs** (any job requesting two or more cores):

**Core-hours = (actual wall clock time used by the job) * (number of nodes
requested) * CPN**

.. note::

   For parallel jobs you are charged for the entire node even if use only a
   subset of the cores on the node. For example, on xJet if you request 48
   cores with --ntasks=48, you get 2 nodes.

   **Charging for serial jobs**:
   **Core-hours = (wall time used by the job)**


