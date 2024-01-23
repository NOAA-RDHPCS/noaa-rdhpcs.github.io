.. _MSU-HPC-user-guide:

******************
MSU-HPC User Guide
******************

.. _orion-system-overview:

General Information
===================

Logging In
----------

To login to Orion or Hercules via SSH, you will use your MSU account username,
MSU password, and Duo two-factor authentication.

.. rubric:: Password Maintenance

If you know your MSU password (or temporary password), use the MSU Training and
Password System (TAPS) site to Manage your Multi#Factor Authentication settings
with Duo and/or change your password. `TAPS <https://taps.hpc.msstate.edu/>`__
is also where you go to do MSU training required before you can login, and for
yearly password resets and training to keep your account active.

.. rubric:: Password Resets

If you forgot your password, a password reset can only be done via phone during
normal business days (M-F) from 08:00-12:00 and 13:00-17:00 Central Time. Please
call: *(662) 325-9146*. If you do not get an answer keep calling every 30
minutes. If busy call again every 15 minutes. The MSU HPC2 admin will verify
your ID, unlock your account, and issue a temporary password that is only valid
to access the `TAPS portal <https://taps.hpc.msstate.edu/>`__.

.. note::

   The user is then required to access TAPS and change their password **within 3
   days** and complete any out-of-date training requirements.

.. rubric:: DUO Multi-Factor Authentication

Please see additional information about setting up and using DUO at
`Multi-Factor Authentication
<https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Getting_an_Account#Dual#factor_authentication_and_Password_Change_.28user_responsibility.29>`__

.. rubric:: Setting Up DUO on a New Device

This section assumes:

- You have already successfully configured DUO on an old device. If you do not,
  please see the link above.
- You have access to the old device.

#.  Go to `TAPS <https://taps.hpc.msstate.edu/>`__ and choose Manage DUO and
    :menuselection:`Password --> Add new Device`.
#.  Select "Send Me a Push".
#.  Open DUO on the old device -- you should be prompted to accept a request for
    authentication.
#.  Approve that request and then on your PC, you should be prompted to enter a
    device type. Keep following the prompts to add a token to your new device.

.. rubric:: Login nodes: Available externally via SSH

To SSH to Orion or hercules, you'll need your MSU username, password and DUO
authentication:

.. code::

   $ ssh <MSU username>@orion-login.hpc.msstate.edu



.. code::

   $ ssh <MSU username>@hercules#login.hpc.msstate.edu

.. note::

   Orion and Hercules have multiple front-end (i.e. login) nodes.  The host names for these are:


   * ``orion-login-1.hpc.msstate.edu``
   * ``orion-login-2.hpc.msstate.edu``
   * ``orion-login-3.hpc.msstate.edu``
   * ``orion-login-4.hpc.msstate.edu``
   * ``hercules-login-1.hpc.msstate.edu``
   * ``hercules-login-2.hpc.msstate.edu``
   * ``hercules-login-3.hpc.msstate.edu``
   * ``hercules-login-4.hpc.msstate.edu``

   The host names ``orion-login.hpc.msstate.edu`` and
   ``hercules-login.hpc.msstate.edu`` are DNS round-robin names for
   ``orion-login-{1..4}`` and ``hercules-login-{1..4}`` respectively.

Orion Example:

.. code::

   ssh jdoe@orion#login.hpc.msstate.edu

   ********** N O T I C E **********

   This system is under the control of and/or the property of Mississippi State
   University (MSU).  It is for authorized use only.  By using this system, all
   users acknowledge notice of and agree to comply with all MSU and High
   Performance Computing Collaboratory (HPC2) policies governing use of
   information systems.

   Any use of this system and all files on this system may be intercepted,
   monitored, recorded, copied, audited, inspected, and disclosed to authorized
   university and law enforcement personnel, as well as authorized individuals of
   other organizations.  By using this system, the user consents to such
   interception, monitoring, recording, copying, auditing, inspection and
   disclosure at the discretion of authorized university personnel.

   Unauthorized, improper or negligent use of this system may result in
   administrative disciplinary action, up to and including termination, civil
   charges, criminal penalties, and/or other sanctions as determined by applicable
   law, MSU policies, HPC2 policies, law enforcement or other authorized State
   and Federal agencies.

   ********** N O T I C E **********

   Using keyboard-interactive authentication.
   Password:
   Using keyboard-interactive authentication.
   Duo two-factor login for jdoe

   Enter a passcode or select one of the following options:

    1. Duo Push to 123-456-7890

   Passcode or option (1-1):
   Success. Logging you in...
   Last login: Mon Apr 13 15:37:46 2020 from 73.83.153.210


   NOTICE:

   Orion is a cluster system running CentOS 7.6 configured as follows.

   1800 nodes, 3600 processors, 72,000 processor cores


   jdoe@Orion-login-4 ~ $

.. rubric:: Web Portal: Available via your web browser

A browser based web interface, know as Open OnDemand (OOD), is available for
accessing the Orion system. Through the web interface you can manage files,
submit & monitor jobs, launch graphical applications, and run remote desktop
session.

- The Orion Web Portal can be reached through this `URL
  <https://orion-ood.hpc.msstate.edu/>`__
- The Hercules Web Portal is not yet available.

.. Note::

   You'll need your MSU username, password, and DUO authentication.

Please refer to MSU's `OOD Documentation
<https://intranet.hpc.msstate.edu/helpdesk/resource#docs/ood_guide.php>`__ for
more information.


.. rubric:: Data Transfer nodes: Available via SCP and SFTP

MSU has several data transfer nodes for orion and hercules.  Data can be
transferred to and from orion and hercules using SCP or SFTP.  The host names
for the DTNs are for orion:

   * ``orion-dtn-1.hpc.msstate.edu``
   * ``orion-dtn-2.hpc.msstate.edu``
   * ``orion-dtn-3.hpc.msstate.edu``
   * ``orion-dtn-4.hpc.msstate.edu``
   * ``orion-dtn.hpc.msstate.edu`` the DNS round-robin for ``orion-dtn-{1..4}``,

and for hercules:

   * ``hercules#dtn#1.hpc.msstate.edu``
   * ``hercules#dtn#2.hpc.msstate.edu``
   * ``hercules#dtn#3.hpc.msstate.edu``
   * ``hercules#dtn#4.hpc.msstate.edu``
   * ``hercules#dtn.hpc.msstate.edu`` the DNS round-robin for ``hercules#dtn#{1..4}``.

.. rubric:: Globus EndPoints: Available via the Globus File Manager

The Globus EndPoints ``msuhpc2-Orion-dtn`` and ``msuhpc2-Hercules`` can be used
to transfer data to and from Orion and Hercules respectively.  This can be
accomplished using the `Globus File Manager App
<https://app.globus.org/file#manager>`__, or the `Globus CLI
<https://docs.globus.org/cli/>`__.

.. rubric:: Development nodes: Available via SSH (internal access only)

While compiles may be done on any of the nodes, the development nodes serve the
purpose for software development and compiles in which additional system
libraries may be requested to be installed that are normally not required for
runtime. Also, the development nodes provide the only gateway for writing into
the ``/apps/contrib/`` directories.

The development nodes for orion are:

   * ``orion-devel-1.hpc.msstate.edu``
   * ``orion-devel-2.hpc.msstate.edu``

and for Hercules:

   * ``hercules-devel-1.hpc.msstate.edu``
   * ``hercules-devel-2.hpc.msstate.edu``

.. rubric:: Additional Information

- Project Storage Space: ``/work/noaa/``
- Applications: ``/apps/``
- Contrib: ``/apps/contrib`` (submit a help desk ticket for directory creation)
- Environment loading: Lmod
- Workload management: Slurm
- `MSU Resource Documentation <https://intranet.hpc.msstate.edu/helpdesk/resource#docs>`__

.. _msu_hpc_running_jobs_on_msu_hpc_systems:

Running Jobs on MSU-HPC Systems
===============================

.. rubric:: Running and Monitoring Jobs on Orion and Hercules

All compute and memory-intensive tasks must be submitted to the batch system for
execution on system compute resources. This section describes the requirements
and common patterns for job submission and monitoring.

**To improve your job turnaround** and efficiently use the system resources
please read and follow instructions carefully.

.. rubric:: Submitting a Job

There are two types of jobs: batch jobs and interactive jobs.

**Batch Jobs**

Most jobs are batch jobs. These are jobs that do not require any interaction and
consist of a shell script that contains the commands you want to run. The
``sbatch`` command is used to submit batch jobs.

.. code::

   $ sbatch <options> <script>

Typically some of the options you would specify are:

   - The account to charge the run to (**this is mandatory**)
   - The number of nodes/tasks needed for the job
   - The time limit for the job
   - The location of stdout/stderr
   - A name for the job

Slurm provides command line options in both long form and short form and either
form can be used. For example, to specify a time limit of 30 min, all of these
following forms are valid:

.. code::

   $ sbatch -t 30          jobfile
   $ sbatch --time=30      jobfile
   $ sbatch --time=0:30:00 jobfile

In addition to the commands that you want to run, job files typically have Slurm
directives at the top job files. The directives are of the form:

.. code::

   #SBATCH <options>
   #SBATCH <options>

For example, to specify the time limit as a directive, you should have the
following line before any of the executable commands in your job file:

.. code::

   #SBATCH --time=0:30:00

These directives can be used instead of specifying options on the command line.
If an option is specified both as a directive and on the command line, the
command line option takes precedence.

It is also possible to specify some of the options by setting an environment
variable. Please see the sbatch man page for details. If the same option is
specified in multiple forms, the order of precedence is command-line,
environment variable setting, and finally the directive in the job file.

.. note::

   Refer to ``man sbatch`` or the `Slurm documentation
   <https://slurm.schedmd.com/sbatch.html>`__ for more information and all
   available options.

.. rubric:: Submitting a Batch Script

The following script is a very basic template that provides examples for some
common sbatch options. It also includes required options. This can be used as a
general guide when constructing a new batch script.

.. code::

   #!/bin/bash -l
   #
   # -- Request that this job run on orion
   #SBATCH --partition=orion
   #
   # -- Request 40 cores
   #SBATCH --ntasks=40
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

   The variable ``$SLURM_NTASKS`` is used in the example above so that the rest
   of the script can stay portable.  If you want to change the number of cores
   used, you only change the submission, not how that value is used in the rest
   of the script.

To submit the above script, called ``jobscript.sh``, you would type:

.. code::

   $ sbatch jobscript.sh

.. rubric:: Submitting a serial job

A serial job can be run on a single node. These jobs are scheduled separately so
that the scheduler can pack multiple jobs onto a single node, improving the
overall usefulness of the system. You do not have to specify a specific queue
name. Requesting a single processor will automatically allow sharing of the
compute node.

By default, a serial job gets only its share of the memory available on a node
(memory per core = ~total memory / total cores). If your serial job needs more
memory than the default, specify that using the ``--mem=<mem>`` option.

.. rubric:: Submitting an Interactive Job

An interactive job is useful for tasks, such as debugging, that require
interactive access with a program as it runs. With Slurm there are two ways to
run jobs interactively, ``srun`` or ``salloc``. We recommend that you use ``salloc``.

For example, to request two nodes for 30 min (with X11 forwarding so that you
can use X-windows based tools) you can do the following:

.. code::

   salloc --x11=first -q debug -t 0:30:00 --nodes=2 -A marine-cpu

When you run the ``salloc`` command, you won't get a prompt back until the batch
system scheduler is able to run the job. Once that happens, the scheduler will
drop you into a login session on the head node allocated to your interactive
job. At this point, you will have a prompt and may run commands, such as your
codes or debuggers as desired. In the example above, an ``srun`` command is
executed. ``salloc`` is similar to sbatch in that it creates an allocation for
you to run in, however only interactive jobs can be run inside the salloc
allocation.

If you need to display X windows back to your desktop screen from within an
interactive job, you must use ``ssh -X`` when logging in.

.. rubric:: Submitting a job with arguments

If you want to submit a script that accepts arguments you need to add the
arguments after the job file name on the sbatch command. It is similar to the
Unix method of passing arguments to a script as shown in the example below:

.. code::

   sbatch batch.job arg1 arg2

The command above passes ``arg1`` as ``$1`` and ``arg2`` as ``$2`` etc., similar
to the Unix convention of argument passing.

.. rubric:: Submitting jobs with job dependencies

Slurm supports the ability to submit a job with dependencies with other jobs. A
simple example is where job Y cannot execute until job X completes. The use of
the ``-d <options>`` (``--dependency=<options>``) is the way to specify the job
dependency.

Review the ``man sbatch`` for a list of dependency conditions (look for
``--dependency`` in the options list) that can be used. Usage format is
illustrated in the example script below that includes ``afterok`` as a dependency
condition.

Here is a simple example of how to run a chain of jobs with dependencies,
assuming that you have a parallel ``helloworld.f`` example program in your current
directory.  Create/edit the file "**depend**" with the contents:

.. code::

   #!/bin/bash
   jid1=$(sbatch --parsable -n1 -A noaatest -J sim --wrap="srun sleep 10")
   jid2=$(sbatch --parsable -n1 -A noaatest -J post --dependency=afterok:$jid1 --wrap="srun hostname")

.. note:: The ``--parsable`` option returns just the Job ID from sbatch.

Make it executable:

.. code::

   $
   chmod 0755 depend

Initiate the sequence of dependent jobs by executing ``depend`` from the command
line:

.. code::

   $ ./depend

.. rubric:: Big runs - Using the "novel" QoS

The *novel* QoS is set up to handle special situations, particularly for large
jobs requiring a large number of nodes (typically for limited time):

A couple of examples are given below:

-  Users may have an occasional need to run very big jobs that would normally
   not fit within the limits of the *batch* QoS.
-  Users may have a need to do some scalability studies that may require running
   up to a very large node count.

It would be very disruptive to schedule such big jobs during normal production
time. So jobs in the novel QOS would typically be run at the end of maintenance
downtimes.

If you have such needs please submit a help desk ticket with the subject line
"Request for running jobs in novel QoS" and provide the following information:

-  How many jobs will you be submitting?
-  What is the number of nodes your biggest job would need?
-  What is the maximum length of estimated time your jobs would need to be
   completed?
-  If there are multiple jobs can they all be run at the same time?
-  Can other jobs be run at the same time as your jobs or do you need
   exclusive user of the nodes?
-  Do you need to be able to monitor your runs when your jobs are running? As
   mentioned above, jobs in the novel QoS will normally be run during downtimes
   and users typically don't have access to the machine to do the monitoring.

Best effort will be made to schedule those runs at the end of maintenance
downtimes that typically happen once a month.

.. rubric:: Job Submission Options

The options you are allowed to specify are the set of options used for the Slurm
batch system.  For a list of options refer to ``man sbatch``, run ``sbatch
--help``, or refer to the `Slurm documentation
<https://slurm.schedmd.com/sbatch.html>`__.

.. rubric:: Command-line options vs directive options

There are two way to specify sbatch options. The first is on the command line
when issuing the sbatch command. For example,

.. code::

   $ sbatch -A fim --ntasks=256 jobscript.sh

The second method is to insert directives at the top of the batch script using
#SBATCH syntax. For example,

.. code::

   #!/bin/bash -l

   #SBATCH -A fim
   #SBATCH --ntasks=256

The two methods may be mixed together, if desired. Options specified on the
command line always override options specified in the script.

.. rubric:: Specifying the project account

Use the ``-A`` (``--account``) option to specify the project that will be
charged when your job is run.

.. note:: You are required to specify an account when a job is submitted.

.. code::

   $ sbatch -A fim

Specifying a Partition
----------------------

.. rubric:: Orion Partitions

The following Orion partitions and Orion Billable TRes Factors are defined:


+---------------+-------------------------+-------------------------+
| Partition     | QOS's allowed           | Description             |
+===============+=========================+=========================+
| orion         | batch,windfall, debug,  | General compute         |
|               | urgent, novel           | resource                |
+---------------+-------------------------+-------------------------+
| bigmem        | batch,windfall, debug,  | Large memory jobs       |
|               | urgent                  |                         |
+---------------+-------------------------+-------------------------+
| service       | batch, windfall, debug, | Serial jobs (max 1      |
|               | urgent                  | core), with a 24 hr     |
|               |                         | limit. Jobs will be run |
|               |                         | on front end (login)    |
|               |                         | nodes that have         |
|               |                         | external network        |
|               |                         | connectivity. Useful    |
|               |                         | for data transfers or   |
|               |                         | access to external      |
|               |                         | resources like          |
|               |                         | databases. If you have  |
|               |                         | a workflow that         |
|               |                         | requires pushing or     |
|               |                         | pulling data to/from    |
|               |                         | the HSMS(HPSS), this is |
|               |                         | where they should be    |
|               |                         | run. See the section    |
|               |                         | **Login (Front End)     |
|               |                         | Node Usage Policy**     |
|               |                         | below for important     |
|               |                         | information about using |
|               |                         | Login nodes.            |
+---------------+-------------------------+-------------------------+

.. rubric:: Hercules Partitions

The following partitions are defined:

+---------------+-------------------------+-------------------------+
| Partition     | QOS's allowed           | Description             |
+===============+=========================+=========================+
| hercules      | batch, windfall, debug, | General compute         |
|               | urgent, novel           | resources               |
+---------------+-------------------------+-------------------------+
| service       | batch, windfall, debug, | Serial jobs (max 1      |
|               | urgent                  | core), with a 24 hr     |
|               |                         | limit. Jobs will be run |
|               |                         | on front end nodes that |
|               |                         | have external network   |
|               |                         | connectivity. Useful    |
|               |                         | for data transfers or   |
|               |                         | access to external      |
|               |                         | resources like          |
|               |                         | databases. If you have  |
|               |                         | a workflow that         |
|               |                         | requires pushing or     |
|               |                         | pulling data to/from    |
|               |                         | the HSMS(HPSS), this is |
|               |                         | where they should be    |
|               |                         | run. See the section    |
|               |                         | **Login (Front End)     |
|               |                         | Node Usage Policy**     |
|               |                         | below for important     |
|               |                         | information about using |
|               |                         | Login nodes.            |
+---------------+-------------------------+-------------------------+

To specify a partition for your job, use the ``-p`` (``--partition``) option.  For example,

.. code::

   #SBATCH --partition=service

to request the *service* partition.

.. rubric:: Specifying Wall Clock Time

You should specify a wall clock time for your job.  The default wall-clock time
is 5 minutes if not defined.  If your jobs will take longer than 5 minutes,
request a wall clock time reasonably close to but not less than (see note below)
the actual wall clock time that the job will take to run.  Specifying an
excessively large wall clock time will result in increased wait time for your
job to start and, more importantly, reduced scheduler efficiency and overall
system utilization.  When requesting multiple partitions (see below), as is
recommended, take into account the longest run time partition.  Due to several
other factors that effect run time, your job run time on a slower partition may
be better as compared to the billable TRes per core performance factor listed in
the partition tables above. Therefore:

Frequently review the wall clock time of the jobs you run in order to better
estimate your requested wall clock time. Increased accuracy of specified wall
clock time with your job submissions will shorten queue wait times, and increase
scheduler efficiency and overall system utilization.

.. note::

   We recommend that you do NOT set a wall clock time less than 5 minutes.

.. note::

   Any job that runs longer than its requested wall clock time or the
   partition's time limit will be terminated by the scheduler. When specifying
   your wall clock time, add some extra time to your recent observed run time
   history to be sure it will finish to allow for random fluctuations in run
   times caused by system load.  For example, 10-20% for short run times, 5-10%
   for long run times.

For example, to set a one-hour time limit:

.. code::

   #SBATCH --time=1:00:00

For the maximum wall clock allowed, see the :ref:`Quality of Service (QOS)
tables <msu_hpc_qos_table>`.

.. rubric:: Specifying a Quality of Service (QOS)

To specify a quality-of-service (QOS), use the ``--qos`` (``-q``) option. For
example:

.. code::

   #SBATCH -q batch

There are several different QOS'es depending on your needs.

.. note::

   If you have an windfall only allocation (allocation = 1) you can only
   submit to the *windfall* QOS.

.. _msu_hpc_qos_table:

+-----------+------------+------------+------------+-----------+-----------------------------------------+
| QOS       | Min Nodes  | Max Nodes  | Max Wall   | Billing   | Description                             |
|           |            |            | Clock      | TRes      | Limits                                  |
|           |            |            |            | Factor    |                                         |
+===========+============+============+============+===========+=========================================+
| All QOS's |            |            |            |           | **Across all QOS**                      |
|           |            |            |            |           | Max of 400 pending/running jobs         |
|           |            |            |            |           | per project/account,                    |
|           |            |            |            |           | additional jobs will be rejected.       |
|           |            |            |            |           | Max of 20 jobs per project/account      |
|           |            |            |            |           | will gain age priority.                 |
|           |            |            |            |           | Exceptions are stated below.            |
+-----------+------------+------------+------------+-----------+-----------------------------------------+
| batch     | 1          | 500        | 8 hours    | 1.0       | Default QOS for non-reservation         |
|           |            | (Orion) &  | (Partition |           | jobs with an allocation more then       |
|           |            | 250        | exceptions |           | *Windfall-Only* (``RawShare=1``).       |
|           |            | (Hercules) | --         |           |                                         |
|           |            | Hercules)  | *service*  |           |                                         |
|           |            |            | 24 hrs)    |           |                                         |
+-----------+------------+------------+------------+-----------+-----------------------------------------+
| urgent    | 1          | 500        | 8 hours    | 2.0       | QOS for a job that requires more        |
|           |            | (Orion),   |            |           | urgency than *batch*.  Your project     |
|           |            | 250        |            |           | :ref:`FairShare <slurm_tips_fairshare>` |
|           |            | (Hercules) |            |           | will be lowered at 2.0x the rate as     |
|           |            |            |            |           | compared to *batch*.  Only one job per  |
|           |            |            |            |           | project/account can be pending/running  |
|           |            |            |            |           | at any time.  When a project's          |
|           |            |            |            |           | FairShare is below 0.45, jobs submmited |
|           |            |            |            |           | to *urgent* are automatically changed   |
|           |            |            |            |           | to *batch* and users notified via       |
|           |            |            |            |           | stderr.                                 |
+-----------+------------+------------+------------+-----------+-----------------------------------------+
| debug     | 1          | 500        | 30         | 1.25      | Highest priority QOS, useful for        |
|           |            | (Orion),   | minutes    |           | debugging sessions.  Your project       |
|           |            | 250        |            |           | :ref:`FairShare <slurm_tips_fairshare>` |
|           |            | (Hercules) |            |           | will be lowered at 1.25x the rate as    |
|           |            |            |            |           | compared to *batch*.  Only two jobs per |
|           |            |            |            |           | user can be pending/running at any      |
|           |            |            |            |           | time.  This QOS should NOT be used for  |
|           |            |            |            |           | fast-turnaround of general work.        |
|           |            |            |            |           | While the *debug* QOS is available, we  |
|           |            |            |            |           | recommend that if you need to work      |
|           |            |            |            |           | through an iterative process to debug   |
|           |            |            |            |           | a code, that you submit a longer        |
|           |            |            |            |           | running interactive job to the default  |
|           |            |            |            |           | QOS so that you can restart your        |
|           |            |            |            |           | application over and over again without |
|           |            |            |            |           | having to start a new batch job.        |
+-----------+------------+------------+------------+-----------+-----------------------------------------+
| windfall  | 1          | 500        | 8 hours    | 0.0       | Lowest priority QOS.  If you have an    |
|           |            | (Orion),   | (Partition |           | allocation of windfall-only (monthly    |
|           |            | 250        | exceptions |           | allocation is 1) you can only submit to |
|           |            | (Hercules) | *service*  |           | this QOS.  Submitting to this QOS will  |
|           |            |            |            |           | NOT affect your future job priority     |
|           |            |            |            |           | :ref:`FairShare <slurm_tips_fairshare>` |
|           |            |            |            |           | factor (f) for your non-windfall jobs.  |
|           |            |            |            |           | Useful for low priority jobs that will  |
|           |            |            |            |           | only run when the system/partition has  |
|           |            |            |            |           | enough unused space available while not |
|           |            |            |            |           | effecting the project's FairShare       |
|           |            |            |            |           | priority.                               |
+-----------+------------+------------+------------+-----------+-----------------------------------------+
| novel     | 501        | Largest    | 8 hours    | 1.0       | QOS for running novel or experimental   |
|           | (Orion),   | partition  |            |           | where nearly the full system is         |
|           | 251        | size       |            |           | required.  If you need to use the       |
|           | (Hercules) |            |            |           | *novel* QOS, please submit a ticket to  |
|           |            |            |            |           | the :ref:`help system <getting_help>`   |
|           |            |            |            |           | and tell us what you want to do.  We    |
|           |            |            |            |           | will normally have to arrange for some  |
|           |            |            |            |           | time for the job to go through, and we  |
|           |            |            |            |           | would like to plan the process with     |
|           |            |            |            |           | you.                                    |
+-----------+------------+------------+------------+-----------+-----------------------------------------+

.. rubric:: Specifying a job name

Giving your jobs meaningful names can help you locate them when monitoring their
progress. Use the ``-J`` (``--job-name``) option. For example,

.. code::

   #SBATCH -J WRF_ARW_00Z

The default name for a job is the name of the job script that is being
submitted.

.. rubric:: Setting the names of output files

If you do not specify the names of the output files that contain the stdout and
stderr from your job script, a file will be written to the directory in which
you issued the sbatch command. A file containing both the stdout and stderr from
your job script will be called: ``slurm-<jobid>.out`` where ``<jobid>`` is the
Slurm job ID.

Use the ``-o`` (``--output``) option to specify the name of the stdout file

.. code::

   #SBATCH -o /full/path/of/stdout/file

Use the ``-e`` (``--error``) option to specify the name of the stderr file

.. code::

   #SBATCH -e /full/path/of/stderr/file

If you want stdout and stderr to go to the same file, do not specify the ``-e``
option.

.. rubric:: Passing environment variables to the job

By default the environment variables set in the current shell is passed to the
job that is submitted.  However if any variable is explicitly passed into the
script with a value, only that value is passed to the script!

If you wish to pass local environment to the script and in addition set a
specific variable that is currently not in the current environment (``ndays=20``
in the example below), you can do it in the following way:

.. code::

   sbatch --export=ALL,ndays=20 … sbatch.job


It is important to note that ``ALL`` is required if you want the local
environment variables are to be exported to the script in addition to the value
explicitly set. If ``ALL`` is left out, only the value of ``ndays=20`` is passed in.

If you do not want to export your local environment, please use the following
syntax:

.. code::

   sbatch --export=NONE … sbatch.job

.. caution::

   Not exporting the current environment can be a little tricky and likely to
   cause some errors unless the necessary environment is created in the job. It
   may also require setting ``--export=ALL`` on the ``srun`` command within the
   job.

.. rubric:: Requesting email notification about jobs

You can use the ``--mail-user`` and ``--mail-type`` options to request
notifications by email when a job enters one or more states.  Both options are
required.  Use the ``--mail-user`` option to specify a comma delimited list of
email addresses where email notifications are to be sent.  Use the
``--mail-type`` option to specify which job states you want email notifications
for. The most useful notifications flags passed to ``--mail-type`` are *NONE*,
*BEGIN(, *END*, and *FAIL* and can be combined. A full list of parameters can be
found on the sbatch man page.

-  FAIL: mail is sent when the job fails with non-zero exit code.
-  BEGIN: mail is sent when the job begins execution.
-  END: mail is sent when the job terminates.
-  NONE: no email is sent.

To send email notification to Joe and Jane when your job starts and when it
terminates, do:

.. code::

   $ sbatch --mail-user=Joe.User@noaa.gov,Jane.User@noaa.gov \
      --mail-type=<the other options go here> myscript.sh

.. rubric:: Specifying the working directory as the current directory

It is good practice to keep your batch scripts portable, and when they get moved
around the working directory is relative to where the script is. To do this,
specify the working directory with the ``-D`` (``--chdir``) option as the current
directory. Ex:

.. code::

   #SBATCH -D .

The other way to do this is with the ``$SLURM_SUBMIT_DIR`` variable. This
variable stores the path from where your script was submitted. So at the top of
your batch script, add:

.. code::

   cd $SLURM_SUBMIT_DIR

.. rubric:: Starting a job after a specific date/time

If a job is waiting for data to arrive based on time of day (e.g., 12:30Z), the
``--begin`` option allows for a job to hold in the queue until at least the time
(or date/time) specified with the option. For example:

.. code::

   #SBATCH --begin=19:25

The above option will cause the job to hold until 19:25 GMT. If resources are
available shortly after 19:25, the job will run. If not, the job will wait until
resources are available (this is not a reservation). Note that if the sbatch was
submitted at 19:26 GMT, the job will hold until 19:25 GMT the next day!

Date/time can be specified as:

.. code::

   YYYY-MM-DD[Thh:mm[:ss]]

*YYYY* is year, *MM* is month, *DD* is day, *hh* is hour, *mm* is
minute and *ss* is second. The letter "T" is required as a
delimiter if specifying both date and time. All times are
considered to be in the future, so

.. code::

   2110-12-21T06:30

would be December 21, 2110 at 06:30 GMT.

The ``--begin`` option also accepts an arbitrary amount of time to wait. For
example:

.. code::

   #SBATCH --begin=now+1hour

will start the job 1 hour from when the job is launched, if resources are
available.

Monitoring Jobs
---------------

.. rubric:: List jobs

Use the ``squeue`` command to get a listing of the current jobs in the queue.

.. code::

   $ squeue
    JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    30049     orion     test Kyle.Ste  R       0:02      1 t758

.. rubric:: List jobs that belong only to you

Use the ``-u`` option to list only the jobs that belong to you. Provide your
username as an argument to ``-u``. This is preferable to using ``squeue \| grep`` to
extract the jobs that belong to you for two reasons. First, this method allows
you to see which of the jobs are active, eligible, and blocked. Second,
usernames are truncated in the ``squeue`` output, making it hard to grep.

.. code::

   $ squeue -u <user name>

.. rubric:: List jobs that have completed within the last 24 hours

Use the ``sacct`` command option to list jobs that have run within the last 24
hours and to see their statuses (State). A full list of ``sacct`` options and job
states can be found on the ``sacct`` man page.

::

   % sacct --user $USER \
           --starttime `date --date="yesterday" +%F` \
           -X \
           --format=JobID,JobName%30,Partition,Account,AllocCPUS,State,Elapsed,QOS

.. rubric:: Query detailed job status information for a specific job

Use the ``scontrol show job`` command to query detailed information about queued
or running jobs or jobs that have finished in the last 15 minutes. This could be
useful when trying to determine why a job is not running and has remained queued
for a long time.

.. code::

   $ scontrol show job 251091

Query a job's estimated start time
----------------------------------

Use the ``squeue --start`` command to get a point-in-time estimate of when your
job may start. Reservation based start time estimation incorporates information
regarding current administrative, user, and job reservations to determine the
earliest time the specified job could allocate the needed resources and start
running. In essence, this estimate will indicate the earliest time the job would
start assuming this job was the highest priority job in the queue.

.. code::

   $ squeue --start
    JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
   251092     orion     test Kyle.Ste PD 2019-03-29T18:55:58     17 (null)   (BeginTime)

.. note::

   The start time estimate can change drastically, depending on the number of
   partitions specified, new jobs being submitted to the queue, and how
   accurately idle jobs and running jobs have specified their wall clock time.

.. rubric:: Deleting jobs

To cancel a job use the scancel command

.. code::

   $ scancel $JOBID

Getting Information about your Projects
---------------------------------------

MSU-HPC uses SLURM as its batch scheduler as does NOAA's RDHPCS systems. SLURM
allocations result in a percentage of total system priority. For more
information on how SLURM prioritizes submitted jobs please refer to
:ref:`understaning Fairshare <slurm_tips_fairshare>` and :ref:`Running and
Monitoring Jobs <slurm_tips_running_monitoring>`.

.. rubric:: Load contrib and noaatools Module

The module tools work on all MSU-HPC systems. On the MSU-HPC
side, load the noaatools module.

.. code::

   $ module avail
   $ module load contrib noaatools
   $ module list

.. rubric:: saccount_params

Use ``saccount_params`` to get information on your projects and disk
usage, and quota.

.. code::

   $ saccount_params
   Account Params -- Information regarding project associations for userid
       Home Quota (/home/userid) Used: 1035 MB Quota: 8192 MB Grace: 10240

       Project: noaa-hpc
           ProjectFairshare=N/A    Core Hours Used=N/A

           Directory: /work/noaa/noaatest DiskInUse=0 GB, Quota=0 GB, Files=0, FileQUota=0

       Project: noaatest
           ProjectFairshare=0.040 (356/414)    Core Hours Used (30 days)=96.6, 30-day Allocation=2
           Partition Access: ALL
           Available QOSes: batch,debug,novel,ood,special,urgent,windfall

           Directory: /work/noaa/noaatest DiskInUse=83981 GB, Quota=95000 GB, Files=3633923, FileQUota=0

       Project: role-noaatest
           ProjectFairshare=N/A    Core Hours Used=N/A

.. note::

   For an explanation of the meaning of these values and general scheduling
   information click `here
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/SLURM_Fair-share>`__.

.. note::

   The parenthetical values after project fairshare indicate the rank of the
   project with respect to all other allocated projects. If the first number is
   lower, your project is likely to have higher priority than other projects. (Of
   course, other factors weigh in to scheduling.)

.. note::

   Your must use the ``saccount_params`` command.  There is no ``account_params`` command alias.

.. rubric:: shpcrpt

Use ``shpcrpt`` to get project usage information.

To get a summary of all project on orion:

.. code::

   $  shpcrpt -c orion -s
   =================================================================================================================
    Report   Summary Report
    Report Run:          Tue 24 Aug 2021 11:30:31 PM  UTC
    Report Period Beginning:         Sun 01 Aug 2021 12:00:00 AM  UTC
    Report Period Ending:Wed 01 Sep 2021 12:00:00 AM  UTC
    Percentage of Period Elapsed:    77.4%
    Percentage of Period Remaining:  22.6%
   =================================================================================================================
   Project   NormShares      ProjFS  Allocation   Cr-HrUsed    Windfall   TotalUsed       %Used        Jobs
   -------------------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- -----------
   aeolus      0.000000         0.0           0           0           0           0       0.00%           0
   amb-verif   0.000216         inf      10,405           0           0           0       0.00%           0
   ... more projects ...
   zrtrr       0.003801     1.35613     183,107      62,065           0      62,065      33.90%       1,040
    -------------------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- -----------
    Total       1.000000  48,168,012  32,643,860       1,068  32,644,928      67.77%     204,281

   Total Report Runtime: 43.58 seconds (ver. 21.08.05)

.. note::

   For Hercules use ``shpcrpt -c hercules -s``

To see information for a single project:

.. code::

   $ shpcrpt -c orion -p noaatest
   =================================================================================================================
    Report   Project Report for:noaatest
    Report Run:          Tue 24 Aug 2021 11:33:10 PM  UTC
    Report Period Beginning:         Sun 01 Aug 2021 12:00:00 AM  UTC
    Report Period Ending:Wed 01 Sep 2021 12:00:00 AM  UTC
    Percentage of Period Elapsed:    77.4%
    Percentage of Period Remaining:  22.6%
   =================================================================================================================
    Machines:           orion
    Initial Allocation in Hours:1,277,285
    Net Allocation Adjustments:         0
 ----------------
    Adjusted Allocation:        1,277,285

    Core Hours Used:1,972,001
    Windfall Core Hours Used:           0
 ----------------
    Total Core Hours Used:      1,972,001

    Project Normalized Shares:   0.026517
    Project Fair Share:          0.652081

    Percentage of Period Elapsed:   77.4%
    Percentage of Period Remaining: 22.6%
    Percentage of Allocation Used: 100.0%

   User     Cr-HrUsed    Windfall   TotalUsed       %Used      Jobs
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   jdoe     1,972,001           0   1,972,001     100.00%    20,465
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   Total    1,972,001           0   1,972,001     100.00%    20,465

   Total Report Runtime: 11.95 seconds (ver. 21.08.05)

.. note::

   For Hercules use ``shpcrpt -c hercules -p <your project``.

.. rubric:: reportFSUsage

Use ``reportFSUsage`` to see a summary of all project disk usage.

.. code::

   $ reportFSUsage
   ------------------------------------------------------------------------------------
   LUSTRE QUOTA AND USAGE REPORT
   ------------------------------------------------------------------------------------
   Date: 2021.08.24
   ------------------------------------------------------------------------------------
   Directory/Group Usage(GB)   Quota(GB)   Limit(GB)      Files  Percentage
   ------------------------------------------------------------------------------------
   amb-verif   0        9500       10000         15         0.0
   aoml-hafs1         864429     1045000     1100000    9255418        82.7
   ... more projects ...
   zrtrr   25007      153425      161500    1059162        16.3
   ------------------------------------------------------------------------------------
   TOTAL_USAGE(GB):  4570575     7327825     7713500  223683296        62.4
   ------------------------------------------------------------------------------------
   NOTE: ** indicates that this project is over quota.
   ------------------------------------------------------------------------------------
   END OF REPORT

.. rubric:: Other useful Links

- :ref:`Getting Information About Your Projects <slurm_tips_getting_project_information>`
- :ref:`The saccount_params Command <slurm_tips_saccount_params>`
- :ref:`The shpcrpt Command <slurm_tips_shpcrpt>`

MSU-HPC System Configuration
============================

Managing Packages in /contrib
-----------------------------

.. rubric:: Overview

The system staff do not have the resources to maintain every piece of software
requested. There are also cases where developers of the software are the system
users, and putting a layer in between them and the rest of the system users is
inefficient. To support these needs, we have developed a /apps/contrib package
process. A /apps/contrib package is one that is maintained by a user on the
system. The system staff are not responsible for the use or maintenance of these
packages.

.. rubric:: Responsibilities of a Contrib Package Maintainer

Maintainers are expected to:

- Follow the naming conventions and guidelines outlined in this document
- Apply security updates as quickly as possible after they become available
- Update software for bug fixes and functionality as users request
- Respond to user email requests for help using the software

.. rubric:: Contrib Packages Guidelines

- The package should be a single program or toolset. We want to prevent having a
  single directory being a repository for many different packages.
- If you support multiple functions, please request multiple packages.
- The package may have build dependencies on other packages, but it must
  otherwise be self-contained.
- The package may not contain links to files in user or project directories.
- We expect each package to be less than 100MB.
- If you need more, please tell us when you request your package.
- We can support larger packages but we need to monitor the space used.
- We expect each package to have less than 100 files.

.. rubric:: Contrib Package Maintainer Requests

If you wish to maintain a package in contrib, please send a request to the Help
System including:

- List of the packages you wish to maintain.
- Justification why each is needed.
- The user who will be maintaining the package.

In certain cases, multiple users can manage a package, and unix group write
permissions may be granted for the directory. In that case, specify the unix
group or Role account that will be maintaining the package.

.. rubric:: Managing a Contrib Package

After your request has been approved to use space in the /contrib directory, two
directories will be created for you:

.. code::

    /apps/contrib/<package>
    /apps/contrib/<package>/modulefiles

This is where you will install your software for this package and optionally
install a module to allow users to load the environmental settings necessary to
use this package. The variable ``<package>`` is the name of the
``/apps/contrib`` package you requested. Thus, one piece of software goes into a
subdirectory under the ``/apps/contrib`` level. If you want to manage multiple
packages, please request multiple /apps/contrib package. You can do this all at
one time when submitting your request to the Help System.

.. rubric:: Maintaining "Metadata" for the contrib Package

Since contrib packages are intended to be used by other users on the system it
will be helpful to have an ``/apps/contrib/<package>/README`` file that contains
at least the following information:

- Package Name:
- Purpose:
- Maintainer:
- Contact info for questions/help:
- Any other info that will be useful for general users to know

.. rubric:: Contrib Package Directory Naming Conventions

When installing software into your /apps/contrib directory, first determine if
this is software that should be versioned (multiple versions may exist at one
time) or un-versioned (there will only ever be one version installed, and
upgrade will overwrite the existing software). For versioned software, please
install it into a subdirectory of your package that is named after the version
number. For supporting multiple versions of software the install path should be:

.. code::

    /apps/contrib/<package>/<version>

Where ``<package>`` is the directory assigned to you and $VER is the version
number. Thus, if your package is named *ferret* and you are installing the
version *3.2.6*, the software should be installed in:

.. code::

    /apps/contrib/ferret/3.2.6

For supporting un-versioned software, only install the software directly into
your package directory:

.. code::

    /apps/contrib/<package>/

.. rubric:: Providing Modules to Access Contrib Installed Software

For each contrib package, a corresponding directory will be created for modules.
The base directory name is ``/apps/contrib/<package>/modulefiles``. Each package
will have a subdirectory created named after the package. For example, for the
ferret package, there will also be a directory created named:

.. code::

    /apps/contrib/ferret/modulefiles

In order for users to know what contrib software is available and who the "Point
of Contact" is, users should do a listing of the ``/apps/contrib directory``:

::

   ls -l /apps/contrib

Once they which software in cotrib they need to use, then can add that package
to their module path and then load the module. For example, *sutil* is a contrib
package, and in order to use it, users would do the following:

::

    module use -a /apps/contrib/sutils/modulefiles
    module load sutils

.. rubric:: Creating Modules for Contrib Packages

Example modules can be found here:

.. code::

   /apps/contrib/modulefiles.example/ferret

Please use those as a template. Contrib package maintainers must follow these
conventions:

- Modules must display the notice when loaded providing contact information on
  how to get help.
- Module naming convention should be based on the version number of the
  software.

Please ask questions through the Help Desk regarding how to construct modules.

Account Management
==================

.. note::

   If you need an account on MSU-HPC, contact your project's Account Manager to
   submit an account request for you.

Getting An Account
------------------

MSU-HPC users are not allowed to request their own account on the system. A new
account request must come from a project's Account Manager (like a RDHPCS
Principal Investigator - PI) or a project's Portfolio Manager (PfM) who holds an
MSU account.

.. rubric:: Submit a New User Account Request (Account Manager/PI/PfM Responsibility)

The following procedure is intended for the Account Manager or the Portfolio
Manager who has an active MSU account.

.. rubric:: Assemble User Information

Before you begin, collect the following details:

-  First Name
-  Last Name
-  Desired Login Name - Typcially first initial, last name
   (John Doe = jdoe)
-  Email address. Preferably the user's @noaa.gov address. Otherwise use a
   business email address that best aligns with the user's work or university.
-  Effective Date. Typically today
-  Expiration Date. 1 year or less from the Effective Date.
-  Project(s) As Account Manager, you can only assign a user to your projects.

.. Note::

   When you request a new account, you become the account supervisor. As
   supervisor, you are responsible to renew the user's account when it
   approaches the expiration date.

   See :ref:`Account Renewal <msu_account_renewal>`

.. rubric:: Login to the MSU account management system

-  Navigate to MSU's account management system: `MSU Account
   Management <https://intranet.hpc.msstate.edu/services/external_accounts/noaa>`__
-  Authenticate using your MSU username and password.

.. Note::

   If you do not remember your password, see `Logging In - Password
   <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in#Password>`__

.. rubric:: Check to see if the user already has an account. If not, request account.

-  `NOAA-HPC Project Management by User <https://intranet.hpc.msstate.edu/services/external_accounts/noaa/manageProjects.php>`__
-  If the user appears in the drop-down, their MSU account already exists.
   Select the user and assign them to your projects. If not, navigate to:
   `NOAA-HPC Computer Account Request
   <https://intranet.hpc.msstate.edu/services/external_accounts/noaa/requestAccount.php>`__
-  Complete the form.
-  Click save and Submit. This completes the initial account request. It's good
   practice to notify the prospective new user that the request has been made, so
   they can expect email from MSU.

Once the initial account request has been submitted, MSU will send the
prospective user email similar to the following, to request the additional
information needed for the background check and account finalization.

.. code::

   From: help@hpc.msstate.edu
   Date: Fri, Jan 31, 2020 at 12:21 PM
   Subject: NOAA-HPC Users Agreement confirmation
   To: <john.doe@noaa.gov>

   A computer account request has been submitted to the the Mississippi State
   University High Performance Computing Collaboratory (MSU HPC2) on your
   behalf.  In order to facilitate continued processing of this account request,
   you must complete the application via the below web address.

   `<https://www.hpc.msstate.edu/computing/external_accounts/noaa/confirmAccount.php>`__

   This request will be removed from the queue if no response is received by
   02/14/20.

   For problems related to your computer account request, please reply to this
   message and provide details of the problem.

   If you received this email in error, you can simply ignore the email.

   --

   Systems Administration Team
   High Performance Computing Collaboratory
   Mississippi State University
   help@hpc.msstate.edu

.. rubric:: Complete the HPC2-NOAA User Account Request Confirmation form (User)

-  Click on the link provided in the email, fill out the form, agree to the
   terms and conditions, and submit the form.

.. note::

   If you have an NOAA RDHPCS account, use the same Organization, Phone, and
   Address you use in AIM. Otherwise, use your business contact information.

If you find you are unable to submit the form, try another password. **Do not
use the # character** as it has periodically caused problems.  Certain other
characters in the password might block the form submission, please submit a help
ticket if you experience a problem `Orion Help
<https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.

.. note::

   The password that you enter will be your temporary password. So please
   remember your password.  This is critical to the next step of the on-boarding
   process.

.. rubric:: Set Password and Complete Training (User)

MSU vets the account request and creates the user account (1-2 weeks). MSU then
sends email, similar to the one below, will be to the new prospective user. To
find the email, search your emails with the following:

.. code::

   From: @hpc.msstate.edu
   Subject: new user account

   The following account has been created:

   ReqDate     EffDate     Supervisor  MSU_Status  Account_Type   Login   UserName
   -----------------------------------------------------------------------------------------------
   2020-01-31  2020-01-29  name        NonMSU      Orion          jdoe    John Doe


   Two-Factor authentication (2FA) registration and password changing is
   required within 3 days. Security training must then be completed before HPC2
   resources can be accessed.

   Visit https://taps.hpc.msstate.edu to complete these requirements.


.. rubric:: Login to MSU's Training and Password System

- Within 3 days of receiving the email, navigate to
  `<https://taps.hpc.msstate.edu>`__
- Authenticate using your username and your temporary password.

.. note::

   If your temporary 3-day password has expired, it will need to be reset. See:
   `Logging In - Reset Password
   <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in#Password>`__

-  Upon successful login, you will see the TAPS Home page.

.. rubric:: Take MSU Security Training

-  Click on the IT Security *Start training* button.
-  Upon successful completion of the training, you will get a confirmation.
-  Go back to the TAPS Home page.

.. rubric:: Take MSU Insider Threat Training

-  Click on the Insider Threat *Start training* button. Upon successful
   completion of the training, you will get a confirmation.
-  Go back to the TAPS Home page.

.. rubric:: Dual-factor authentication and Password Change (User)

-  Navigate to `TAPS <https://taps.hpc.msstate.edu>`__

.. rubric:: Setup Dual-factor authentication App

- Click on the *Manage Duo and Password* button.
- Specify Duo Mobile Phone Device
- Specify Duo Mobile Phone Number
- Specify Duo Phone Type*
- Install Duo App
- Activate Duo App
- Change Temporary Password
- Password Change Successful
- Logout and log back in again

Congratulations! Your account is now fully set up and you can login to MSU-HPC.

.. rubric:: Account Reactivation

If your account has expired, you will need to reactivate. To begin the process,
start a Help ticket: `MSU-HPC Help Request
<https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.


.. _msu_account_renewal:

Account Renewal
---------------

To keep your MSU account current and active:

-  Log on to the system every 90 days (successful login to MSU-HPC or
   authentication to one of the MSU Account Management web pages).
-  Complete yearly password changes and security training updates, which are
   required each January (regardless of your effective date). Users have
   until the end of January to comply, using the online MSU HPC2 Training and
   Password System `TAPS <https://taps.hpc.msstate.edu/>`__, otherwise the user
   account will be locked.
-  Make sure your supervisor renews your account before the account expiration
   date.

If an MSU account is not renewed by the expiration date, the account will be
locked. The expiration date is set by the account supervisor when the user
account is created or renewed, and cannot be more than one (1) year from the
effective date. The user account renewal request can only be completed by the
supervisor of record. If the supervisor is to be on an extend absence, then the
supervisor should start an :ref:`Orion help ticket <getting_help>` to assign an
new supervisor so the user may maintain their account during your absence.

.. note::

   A users Home File System directory (``/home/userID``) is deleted when a
   user's account is deleted.  User account deletion can occur any time after a
   user account is scheduled for deletion. User accounts are scheduled for
   deletion 2 weeks after a user accounts expiration date and the account is
   not renewed.  Once your HFS data is deleted it will NOT be recoverable.
   Project data (``/work``) is not deleted when a users account is deleted.

.. rubric:: Renewal Request Email from MSU (Supervisor)

When an active user's account approaches the expiration date, an email will
be sent to the supervisor from MSU so that the supervisor can request a renewal
or decide not to renew the account.

Here is an example of the email:

.. code::

   From: <null@hpc.msstate.edu>
   Date: Thu, Jan 21, 2021 at 8:11 AM
   Subject: HPC-NOAA Computer Account Expiration Notice
   To: <jdoe@hpc.msstate.edu>

   The external users agreement for J. Doe will expire on 02/05/21.  If
   you wish to renew this agreement, please go to:
   https://intranet.hpc.msstate.edu/services/external_accounts/noaa/requestAccount.php?id=1234&user=jdoe

   to request a renewal of the agreement.  If you do not wish to renew this
   agreement, please ignore this email.

   --
   Systems Administration Team
   High Performance Computing Collaboratory
   Mississippi State University
   help@hpc.msstate.edu

If the renewal time has passed, or the initial account renewal email was missed,
request an account renewal `here:
<https://intranet.hpc.msstate.edu/services/external_accounts/noaa/>`__

.. rubric::  Fill out the NOAA-HPC Computer Account Request Form

#.  Note the Expiration Date in the email.
#.  Follow the link to open a pre-populated webform. You may be required to
    provide your MSU login credentials. If you don't know your password start an
    `Orion help ticket
    <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.
#. Verify the email address. Change it if needed.
#. Set the Effective Date.  The effective date may pre-populate with the current
   date instead of the Expiration Date. Change the Effective Date to be the
   Expiration Date in the email.
#. Set the new Expiration Date.  This should be set to 1 year after the new
   Effective Date (if your Effective Date is 02/05/21, the Expiration Date
   should be 02/05/22), unless you want the user account to expire sooner than 1
   year. 1 year is the max allowed by MSU.
#.  Save Request when complete

This completes the renewal request. The supervisor should consider notifying the
user that the renewal request has been made so they will be vigilant for an
email from MSU. MSU will email the user to provide additional information and
confirm the request.

.. rubric:: HPC2-NOAA User Account Request Confirmation (User)

Once the account renewal request has been submitted by the supervisor, an email
similar to the one below will be sent from MSU directly to the user, asking for
additional information and request confirmation.

.. code::

   From: help@HPC.MsState.Edu <help@HPC.MsState.Edu>
   Sent: January 21, 2021 13:03
   To: forrest.hobbs@noaa.gov
   Subject: NOAA-HPC Users Agreement confirmation

   A computer account request has been submitted to the the Mississippi State
   University High Performance Computing Collaboratory (MSU HPC2) by Eric
   Schnepp on your behalf.  In order to facilitate continued processing of this
   account request, you must complete the application via the below web address.

   https://www.hpc.msstate.edu/computing/external_accounts/noaa/confirmAccount.php?confCode=XXXXXXXX

   This request will be removed from the queue if no response is received by
   02/04/21.

   For problems related to your computer account request, please reply to this
   message and provide details of the problem.

   If you received this email in error, you can simply ignore the email.
   --
   Systems Administration Team
   High Performance Computing Collaboratory
   Mississippi State University

   help@hpc.msstate.edu

.. rubric::  Fill out the HPC2-NOAA User Account Request Confirmation Form

#.  Click on the link provided in the email
#.  Fill out the form.

   -  Your password is your current MSU password. If you don't know your
      password start an `Orion help ticket
      <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.
   -  If you have an NOAA RDHPCS account use the same Organization, Phone, and
      Address you use in AIM. Otherwise, use your business contact information.

#.  Agree to the terms and conditions, and submit the form.

The form will then be submitted back to MSU for final approval.  If the renewal
is approved you will not be notified, and your access is maintained.  If the
renewal is denied the supervisor will be notified by email.

Managing Portfolios, Projects and Allocation
--------------------------------------------

.. rubric:: Portfolio Management on MSU-HPC Systems

On the MSU-HPC system, Portfolios, Projects, and Project Allocations are managed
by Portfolio Managers (PfM's) and Principle Investigators (PI's) the exact same
way as they are for NOAA's RDHPCS systems (Hera/Jet/Gaea/HPSS). The main
difference for Account Management between NOAA RDHPCS systems and the MSU-HPC
system is how Project members (users) are managed.

.. rubric:: Managing Projects within a Portfolio

Project changes (add or remove a project, changing the PI, changing compute
allocation and disk quota) on MSU-HPC systems are requested by the Portfolio
Manager, who emails the :ref:`Orion Help System <getting_help>`.

.. note::

   Projects with the same name between RDHPCS systems and MSU-HPC systems will
   have the same PI, and the MSU-HPC project must have the same user membership
   on Hercules and Orion.

.. note::

   The portfolio manager is responsible for the portfolio across all R&D HPC
   resources (MSU-HPC/Hera/Jet/HPSS/Gaea).

.. rubric:: Adding/Removing Project Members

See :ref:`Adding/Removing Project Members
<account_adding_and_removing_project_members>`.

.. rubric:: Managing Allocations

Allocations on this system are managed the exact same way as they are for NOAA's
RDHPCS systems (Hera, Jet etc.) For more information, please see: `RDHPCS
Allocations
<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Allocations>`__

Role Accounts
-------------

Role accounts are available on the MSU-HPC system. A Role account allows
multiple members of a project to manage a project's scientific work, including
but not limited to automated workflows.

Mississippi State University's MSU-HPC system has system-specific policies
concerning Role Accounts. These are required for MSU to remain compliant with
their security controls and security plan.

 .. rubric:: Role Account Policies

 -  A role account is a user account that is shared by one or more users.
 -  Role accounts follow the naming convention ``role-baseprojectname``.
 -  There can be only one role account per MSU-HPC project, and a role account
    can be only assigned to a single project.
 -  Role accounts are managed by the same Account Managers as the base project.
 -  A role account is managed like a project (ex. membership is managed by the
    Account Managers on the NOAA-HPC Project Management by Project" page). Any
    MSU-HPC user can be a member of the role account, but it is recommended that
    they also be a member of the base project.
 -  Role accounts are only created with approval of one of the base projects
    Account Managers (Portfolio Mgr or PI).
 -  No passwords or Duo will be assigned to Role accounts.
 -  Role accounts may be used for setting up unattended data transfers via SSH
    key pairs
 -  Role accounts may run jobs, utilize cron services, and be used to manage
    contrib directories.

 -  Access to the Role account shall be done via the ``sudo -su
    role-PROJECTNAME`` command.
 -  The sudo command can be run on Login, Development, and DTN nodes.

 .. rubric:: To Request and/or perform Management on a Role Account

 -  The PI or PfM should submit a request by emailing the Help Desk at
    rdhpcs.orion.help@noaa.gov.
 -  The request should include:

   -  Name:
   -  PI:
   -  Project:
   -  Users:

 -  The Role account will be created and the PI will be assigned as the Account
    Manager. As with projects, the PI may request that additional Account
    Managers be assigned as well.
 -  The PI/Account Managers must use the *Project Management* web form to add
    and remove users from their Role account.


Help, Policies, Best Practices, Issues
======================================

MSU-HPC Help Requests
---------------------

If you have any issues, questions, or comments, please email the Help System:
rdhpcs.orion.help@noaa.gov

.. note::

   Help tickets are normally addressed by the RDHPCS   User Support team and the
   MSU Orion Support team from 0900 -1700 Eastern Time, Monday - Friday, except
   Government holidays.

.. _msu_known_issues:

Known Issues
------------

*Last Updated: 11/29/23*

.. rubric:: General

-  No Major issues

.. rubric:: Hercules

-  IDL is not yet available on Hercules. MSU hopes to have this available by the
   end of June. Please continue to use Orion for IDL work.
-  There is not yet an Open OnDemand (OOD) service available. This service won't
   be available until a while after the system has been placed into production.

.. rubric:: Orion

-  No Major issues

Policies and Best Practices
---------------------------

* All MSU-HPC accounts are managed outside of NOAA and are therefore subject to
  MSU's Account Management and Security Policies.
* If you have an active NOAA email account, then this must be used when creating
  a MSU account.
* Only members of NOAA projects are allowed to access NOAA's data directories
  (``/work/noaa`` and ``/work2/noaa``).
* Only users with an active NOAA account will be able to reach R&D HPCS
  documentation.
* Access to the Niagara system requires an active RDHPCS account.

.. note::

   A users Home File System directory (/home/userID) is deleted when a user's
   account is deleted. User account deletion can occur any time after a user
   account is scheduled for deletion. User accounts are scheduled for deletion 2
   weeks after a user accounts expiration date and the account is not renewed.
   Once your HFS data is deleted it will NOT be recoverable. Project data
   (``/work`` and ``/work2``) is not deleted when a users account is deleted.

.. rubric:: Best Practices

-  Due to limited disk space on Orion, it is highly recommended that data be
   moved back to the R&D HPC Niagara system.
-  Due to limited network bandwidth, it is highly recommended that  `Globus
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Transferring_Data_Globus>`__
   be used for moving data between Orion and Niagara.

Protecting Restricted Data
--------------------------

Restricted data (*rstprod*) is allowed on the MSU-HPC system. Be sure to follow
all of NOAA's restricted data policies when using MSU-HPC. Request access to
*rstprod* via `AIM <https://aim.rdhpcs.noaa.gov>`__  Provide the following
information in your justification:

-  The machine(s) where you will need rstprod access on (i.e. Hercules, Orion).
-  The project(s) you will be using rstprod data for.

User Notifications
------------------

Below is a historical list of all significant user notifications.

-  `1 06/02/2023 <#06/02/2023>`__
-  `2 04/26/2023 <#04/26/2023>`__
-  `3 02/17/2022 <#02/17/2022>`__
-  `4 12/14/2021 <#12/14/2021>`__
-  `5 10/19/2021 <#10/19/2021>`__
-  `6 10/04/2021 <#10/04/2021>`__
-  `7 09/30/2021 <#09/30/2021>`__
-  `8 08/25/2021 <#08/25/2021>`__

.. rubric:: 06/02/2023

A new computing resource is now available for production use by NOAA’s R&D HPC
user community. The new system is named “Hercules” and as with Orion, is owned
and managed by Mississippi State University (MSU). This is a brand-new system,
with a brand-new software stack. So please be aware that you may encounter
issues when compiling, running jobs, and setting up automated workflows. Please
email any questions or issues to “rdhpcs.hercules.help@noaa.gov”.

Hercules System Overview:

:Manufacturer: Dell
:Model: PowerEdge C6520
:Total Compute Nodes: 512
:Total Cores: 40,960
:Total System Memory: 262,144 GB
:Processor: Xeon Platinum 8380 40 Core @ 2.3GHz
:Cores per Node: 80
:Memory per Node: 512GB
:Interconnect: Mellanox Infiniband NDR-200
:File Systems: 2 DDN Lustre File system /work & /work2 (shared with Orion)
:Home File System: NFS with 10GB user quota
:Allocations: Core-hour allocations (independent from Orion), Disk allocations (Shared between Orion and Hercules)
:Other Node Types: Login nodes (4), Development nodes (2), and Data Transfer nodes (4)

* `MSU’s Official Hercules Documentation <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/hercules_guide.php>`__
* `Hercules Per-Project Allocations (Core-Hour & Disk) <https://docs.google.com/spreadsheets/d/12hCDc_c9f1NYXszHB787gwhG-TK7Js7rVzftL3Qcv9Q/edit?usp=sharing>`__

**NOAA’s RDHPCS Supplemental Documentation**
* :ref:`How to run jobs <msu_hpc_running_jobs_on_msu_hpc_systems>`
* :ref:`Known Issues (supplemental) <msu_known_issues>`
* :ref:`Differences between Orion and Hercules <msu_faq_what_are_the_differences_between_orion_and_hercules>`

.. rubric:: 04/26/2023

A new computing resource is now available for the NOAA R&D HPC user community at
Mississippi State University (MSU). The new system has been named “Hercules” and
as with Orion, is owned and managed by MSU. As this is a brand new system, with
a brand new software stack, we would like your help in flushing out any issues
before we place the system into full production. So we are asking our current
Orion users to assist us with the pre-operational testing of this new system. We
would greatly appreciate it if you could try compiling your models, running your
models, testing your workflows, and then provide us with feedback by emailing
rdhpcs.orion.help@noaa.gov. Please also email any questions or issues to the
same email address. If everything goes well with the testing then we hope to
announce full production in early May. Thank you for all your help!

Hercules System Overview:

:Manufacturer: Dell EMC
:Model: PowerEdge C6520
:Interconnect: Mellanox Infiniband NDR-200
:Processor: Xeon Platinum 8380 40Core@2.3GHz
:Total System Memory: 262,144 GB
:Total Compute Nodes: 512
:Cores per Node: 80
:Total Cores: 40,960
:File Systems: 2 DDN Lustre File system /work & /work2 (shared with Orion)
:Allocations: Core-hour allocations (independent from Orion), Disk allocations (Shared between Orion and Hercules)
:Home File System: NFS with 10GB of space per user
:Other Node Types: Login nodes (4), Development nodes (2), and Data Transfer nodes (4)

* `MSU’s Official Hercules Documentation <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/hercules_guide.php>`__
* :ref:`How to run jobs <msu_hpc_running_jobs_on_msu_hpc_systems>`


Please note the following: During the pre-operational test phase we are only
allowing “windfall” QOS jobs to run. This will allow you to run test jobs
without negatively impacting your project’s Fairshare. Once the system is ready
for production then we will upload the core-hour allocations and make all QOSs
available for use.

* :ref:`Known Issues (supplemental) <msu_known_issues>`
* :ref:`Differences between Orion and Hercules <msu_faq_what_are_the_differences_between_orion_and_hercules>`

.. rubric:: 02/17/2022

Dear NOAA Orion Users,
Please see this month's update on Mississippi State
University's (MSU) Orion system.

**System Issues:**

-  There has been an ongoing issue with the "/work2" file system significantly
   underreporting disk usage. Although we believe this issue has now been
   resolved, the storage vendor is going to perform some additional verification
   work during next week's downtime.
-  The Orion Systems Activity is in the process of being relocated to a new web
   server. We hope to have it back up and running as soon as possible.

**New Features:**

-  Although there is nothing new to report, Orion hit its highest usage yet in
   January by NOAA's projects and users. Keep up the great work!

**Reminders:**

-  The deadline for taking your annual MSU security training and changing your
   MSU password was January, 31st 2022. Anyone who did not meet the deadline has
   had their account disabled. If you still require access to Orion then there
   is still time to take your training and change your password. Cleck `here
   <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Orion_Password_and_Security_Training_Information>`__
   for more details.
-  There is no direct access to the HPSS system from Orion. The Niagara system is available for all RDHPCS users to
   use as an intermediary storage location for moving data to and from HPSS.
-  CRON services are only available on Login node “orion-login-1”. Please use this Login node when creating
   and editing your crontab.
-  Role accounts (shared user) are now available for use on Orion.

For more information click `here <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__

-  If you have any comments, questions, or concerns then
   please email the RDHPCS Help Desk. The details are
   located below.

**General Information:**

-  Orion Help: Email "rdhpcs.orion.help@noaa.gov". Please
   use your "@noaa.gov" email if you have a NOAA account.
-  `MSU’s Orion Documentation (all users) <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/>`__
-  `NOAA's Orion Docs (supplemental for NOAA users) <https://oriondocs.rdhpcs.noaa.gov>`__
-  `NOAA's Niagara Docs (NOAA users) <https://niagaradocs.rdhpcs.noaa.gov>`__
-  `RDHPCS Maintenance/Events Calendar (NOAA users) <https://calendar.google.com/calendar/b/1?cid=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

.. rubric:: 12/14/2021

Dear NOAA Orion Users,
Please see this month's update on Mississippi State
University's (MSU) Orion system.

**System Issues:**

-  There is an ongoing issue with the "/work2" file system significantly underreporting disk usage. The root cause
   has yet to be determined by the file system vendor.
-  During the last downtime there was extensive testing performed on the Infiniband fabric. As a result of this
   testing, a handful of nodes have been identified as having network bandwidth issues. This may have caused
   intermittent job performance problems. The nodes have been pulled from production for repair and revalidation.
-  The Orion Systems Activity page needs to be relocated to a new web server. We hope to have this service back up and available in January.

**New Features:**

-  SLURM Batch System Changes

As with NOAA's R&D HPC systems, the limits for Orion's special QOSs are as
follow:

*debug*

- There is a maximum of 2 jobs per user, regardless of state (running or
  pending).
- There is a maximum of 30 minutes of wall clock time.
- To offset the increase in job priority there is a 1.25x charge rate for each
  job. This counts against your project's overall Fairshare value.

*urgent*

- There is a maximum of 1 job per project, regardless of state (running or
  pending).
- There is a maximum of 8 hours of wall clock time
- To offset the increase in job priority, there is a 2x charge rate for each
  job. This counts against your project's overall Fairshare value.

Please Note: As both the "debug" and "urgent" QOSs have a Fairshare penalty
associated with them, it is highly recommended that you use them sparingly.
Under normal circumstances you should be using either the "batch" QOS (standard
charge rate) or the "windfall" QOS (very lowest priority but no charge).

**Reminders:**

-  There is no direct access to the HPSS system from Orion. The Niagara system
   is available for all RDHPCS users to use as an intermediary storage location
   for moving data to and from HPSS.
-  CRON services are only available on Login node “orion-login-1”. Please use
   this Login node when creating and editing your crontab.
-  The “/work2” file system on Orion is now available to all NOAA projects and
   users.
-  Role accounts (shared user) are now available for use on Orion.

For more information `click here <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__

-  If you have any comments, questions, or concerns then please email the RDHPCS
   Help Desk. The details are located below.

.. rubric:: 10/19/2021

​Dear NOAA Orion Users,

Please see this month's update on Mississippi State University's (MSU) Orion
system.

**System Issues:**

-  There have been reports by a couple of users that jobs are intermittently
   timing out and failing to run to completion. Although I/O is suspected, it is
   still unclear if the issue is an application, file system, interconnect, or
   compute node issue. The Orion support staff is actively investigating this
   issue and planning to run extensive diagnostics during the upcoming downtime.

**New Features:**

-  SLURM Batch System Changes

Several changes have been made to Orion’s SLURM configuration this month. For
those of you using NOAA’s R&D HPC systems, these changes should be similar to
those recently made on NOAA’s Jet, Hera, and Niagara systems.

-  The parameter "FairShare" is now being used as a replacement for "LevelFS".
   The “hierarchical priority calculation” feature has also been disabled. These
   changes will ensure that the Batch system evaluates each project completely
   independently from other projects. The usage of one project will not impact
   the priority of other projects in the same Portfolio or Sub-Portfolio.
-  The “sfairshare”, “saccount_params”, and “shpcrpt” reports have been updated
   to reflect the move to “FairShare”. Here is a summary of those changes:

   -  All reports now report “FairShare” rather than “LevelFS” or “ProjectFS”
   -  Ranking is with respect to all NOAA projects on the system, not just
      within your Portfolio. There is a known issue with shpcrpt where it will
      give a slightly different ranking then the other reports. This will be
      resolved in the next release.
   -  If you are just looking for your project’s FairShare and your ranking then
      the “sfairshare -u” report may be useful.
   -  Both the “sfairshare” and “saccount_params” reports have a “-h” option
      that provides available options.

Note: As always, please load the proper environment by issuing the command
“module load contrib noaatools” before attempting to run any of theses reports.

-  When Slurm calculates each project’s FairShare priority it looks back in time
   at recent utilization. The algorithm applies a half-life decay value to all
   previous usage. If the half-life is set to 15 days (as it was previously)
   then the 15 day old usage is weighted at 50%, 30 day old usage at 25% and so
   on. We have reduced the half-life to 5 days to mitigate the negative effect
   of borrowing/loaning core-hours, as well as using extra core-hours during the
   rare lull times on the system.

-  The default memory allocation per core has been changed from using all
   available memory on a node to being based on the cores requested per node.
   Standard compute nodes with a total memory of 192GB will default to 4608 Mb
   per core. Big memory nodes with a total memory of 384GB will default to 9472
   Mb per core. Users can change these defaults by using the “--mem” or
   “--exclusive” SLURM options. Please run “man sbatch” for more details on
   these options.

**Reminders:**

-  There is no direct access to the HPSS system from Orion. The Niagara system
   is available for all RDHPCS users to use as an intermediary storage location
   for moving data to and from HPSS.
-  CRON services are only available on Login node “orion-login-1”. Please use
   this Login node when creating and editing your crontab.
-  The “/work2” file system on Orion is now available to all NOAA projects and
   users.
-  Role accounts (shared user) are now available for use on Orion.

`For more information <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__

-  If you have any comments, questions, or concerns then please email the RDHPCS
   Help Desk. The details are located below.

**Upcoming Downtimes:**

| -  MSU Orion Maintenance
| Orion maintenance is scheduled to start at 6AM Central on Wednesday, 10/20, and
| go through 5PM Central on Thursday, 10/21/21. There are a number of upgrades
| occurring on Wednesday (firmware, Lustre client, etc.) so the extra day is
| required to perform extensive system testing and validation.
| -  RDHPCS Niagara Maintenance
| Niagara maintenance is scheduled for Tuesday, 11/02/21 from 0800 to 1800 ET.

**General Information:**

-  Orion Help: Email "rdhpcs.orion.help@noaa.gov". Please use your "@noaa.gov" email if you have a NOAA account.
-  `MSU’s Orion Documentation (all users) <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/>`__
-  `NOAA's Orion Docs (supplemental for NOAA users) <https://oriondocs.rdhpcs.noaa.gov>`__
-  `NOAA's Niagara Docs (NOAA users) <https://niagaradocs.rdhpcs.noaa.gov>`__
-  `RDHPCS Maintenance/Events Calendar (NOAA users) <https://calendar.google.com/calendar/b/1?cid=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

Thank You, RDHPCS Management

.. rubric:: 10/04/2021

On Wednesday, October 6, beginning at 1:00pm CDT, changes to orion's slurm
configuration will be made. These changes will be completed live and a short
window of service interruption for job submissions may occur while the scheduler
is restarted.

These changes should help with job throughput.

Users should note a change to the default memory allocation. The default memory
allocation per core will be changed from using all available memory to being
based on cores requested per node. Standard compute nodes w/ 192GB will default
to 4608 Mb per core Big mem nodes w/ 384GB will default to 9472 Mb per core
Users can change these defaults by using the --mem or --exclusive options.

Running jobs should not be affected, and queued jobs may have their
priority/fairshare adjusted after the reconfiguration.

| For any associated problems, submit a help desk ticket.
| HPC2 users email: help@hpc.msstate.edu
| NOAA users email: rdhpcs.orion.help@noaa.gov

.. rubric:: 09/30/2021

Dear NOAA Orion Users,

As with NOAA's R&D HPC systems, we plan to start providing you with regular
monthly updates on Mississippi State University's Orion system. These updates
will be directed towards providing you with information on system issues, new
features, reminders, upcoming downtimes, and general information.

**System Issues:**

-  There have been some intermittent reports of the "/work"
   file system being unresponsive on the Login nodes. The
   Orion support staff if actively working with the file
   system vendor to investigate this issue.

**New Features:**

-  The new “/work2” file system on Orion is now available to all NOAA projects
   and users.

As part of this effort we reviewed each project’s current disk quota, reviewed
each project’s historical usage on “/work”, and then adjusted quota’s
accordingly. Some projects have had no or very low usage, as compared to their
quota, so quotas were reduced for these projects. However many projects were
left unchanged and a few had their quota increased slightly. Initial quota
limits on “/work2” have been set to be equal to the recently adjusted “/work”
quotas. So each project should now have roughly 2x the usable disk capacity
across both file systems. You should experience equal or slightly improved
performance when using “/work2”. Due to a new caching feature, you may also see
small file read performance improve with /work2.Instructions on how to see your
project allocation, quota, and usage information is detailed `here
<https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Getting_Info_about_your_Projects-Orion>`__

-  Role accounts (shared user) are now available for use on Orion.

For more information please click `here <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__

**Reminders:**

-  There is no direct access to the HPSS system from Orion. The Niagara system
   is available for all RDHPCS users to use as an intermediary storage location
   for moving data to and from HPSS.
-  CRON services are only available on Login node “orion-login-1”. Please use
   this Login node when creating and editing your crontab.
-  If you have any comments, questions, or concerns then please email the RDHPCS
   Help Desk. The details are located below.

**Upcoming Downtimes:**

| -  RDHPCS Niagara Maintenance
| Niagara maintenance is scheduled for Tuesday, 10/05/21 from 0800 to 1800 ET.
|
| -  MSU Orion Maintenance
| The exact day and time for Orion’s October maintenance is still TBD. However it
| is expected to be later in the month and could require a 2 day downtime, due to
| extensive firmware upgrades.

**General Information:**

-  Orion Help: Email "rdhpcs.orion.help@noaa.gov". Please use your "@noaa.gov"
   email if you have a NOAA account.
-  `MSU’s Orion Documentation (all users) <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/>`__
-  `NOAA's Orion Docs (supplemental for NOAA users) <https://oriondocs.rdhpcs.noaa.gov>`__
-  `NOAA's Niagara Docs (NOAA users) <https://niagaradocs.rdhpcs.noaa.gov>`__
-  `RDHPCS Maintenance/Events Calendar (NOAA users) <https://calendar.google.com/calendar/b/1?cid=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

.. rubric:: 08/25/2021

Dear NOAA Orion Users,

As with NOAA's R&D HPC systems, we plan to provide you with regular updates on
Mississippi State University's Orion system. These updates will be directed
towards providing you with information on general issues, new features,
reminders, upcoming downtimes, and general information.

**General Issues:**

- Earlier this month the "/work" file system became dangerously full and almost
  hit it's capacity limit. The issue was due to a Lustre quota configuration
  issue. The issue was identified, resolved quickly, and should not be an issue
  in the future. However some of you may have noticed a significant jump in your
  project's disk usage. This was a direct result of the quota fix being applied.

**New Features:**

-  Role accounts (shared user) are now available for use on Orion. For more
   information click `here
   <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__.

**Reminders:**

-  There is no direct access to the HPSS system from Orion. The Niagara system
   is available for all RDHPCS users to use as an intermediary storage location
   for moving data to and from HPSS.
-  If you have any comments, questions, or concerns then please email the RDHPCS
   Help Desk. The details are located below.

**Upcoming Downtimes:**

-  RDHPCS Niagara Maintenance

Niagara maintenance is scheduled for Wednesday, 09/01/21
from 0800 to 1800 ET.

-  MSU Orion Maintenance

Orion maintenance is scheduled for Tuesday, 09/28/21 from
0800 to 1700 CT.

**General Information:**

-  Orion Help: Email "rdhpcs.orion.help@noaa.gov". Please use your "@noaa.gov"
   email if you have a NOAA account.
-  `MSU’s Orion Documentation (all users) <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/>`__
-  `NOAA's Orion Docs (supplemental for NOAA users) <https://oriondocs.rdhpcs.noaa.gov>`__
-  `NOAA's Niagara Docs (NOAA users) <https://niagaradocs.rdhpcs.noaa.gov>`__
-  `RDHPCS Maintenance/Events Calendar (NOAA users) <https://calendar.google.com/calendar/b/1?cid=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

.. _msu_faq:

MSU FAQ
=======

.. _msu_faq_what_are_the_differences_between_orion_and_hercules:

.. rubric:: What are the differences between Orion and  Hercules?

Although the ``/work`` and ``/work2`` file systems are mounted on both Orion and
Hercules (via a shared InfiniBand interconnect), you should expect Hercules to
behave like a standalone HPC system.

Here are some of the key differences:

-  Orion runs CentOS 7.x for its Operating System. Hercules runs Rocky Linux 9.x
   for its Operating System. There may be subtle differences between the two.
-  Hercules has all of the same basic software packages as Orion, but with the
   latest version of each package installed. MSU will consider installing older
   software versions upon request. This should be done via a help ticket and
   should include a justification as to why the older version is needed and an
   estimate as to how long it will be needed.
-  With a few exceptions, Spack is being used to build and manage the
   Open-source software stack on Hercules. This includes the module file for
   each Open-source software package. The directory and module names are
   different then Orion.
-  The "/apps" directory structure is significantly different between the two
   system. Software built on Hercules, using Spack, will be installed in its own
   ``/apps/spack/<package-hash>`` subdirectory. Any software package built with
   Spack will have a Spack generated hash as part of it's directory name. Any
   time ``/apps/spack`` software package are rebuilt they will get a new hash.
   This may occur often. So it is imperative to not use hard coded paths and
   instead, us modules for loading the required build and run environment.
-  The name and order by which module files are loaded is different between the
   two systems.

Here are other items of interest:

-  Hercules has its own set of Login nodes, Development nodes, Compute nodes,
   Data Transfer nodes, etc.
-  Hercules has its own Home File System (HFS) and its own ``/apps/contrib``
   directory. As with Orion, only the HFS is the ONLY file system which is
   backed up.
-  Hercules has a completely separate CRON service. Workflows need to be managed
   independently on the two systems. Please use ``<system name>-login-1`` for
   editing your crontab file.
-  The Batch system is completely separate between the two systems. A project's
   Fairshare on one system will not impact the project's Fairshare on the other
   system. Users cannot check the status or submit jobs between the two systems.
   There is no Federated configuration in place.
-  Although core-hour (Fairshare) allocation will be managed independently, a
   project's disk allocation will be shared between the two systems. Users can
   follow the exact same directory path on each system to access their data.
-  Core-hour usage reporting will be reported separately for each system.
-  You do not have to do anything different in regards to MSU's Account
   Management systems. All users have accounts on both systems. This is the same
   for Role accounts.
-  Each NOAA project/group has the exact same user membership on both systems.
-  Users have to login (via ssh or putty) to Hercules and Orion separately.
-  The ``screen`` command has been replaced with ``tmux``.

.. _msu_faq_will_orions_software_stack_be_upgraded_to_match_hercules:

.. rubric:: Will Orion's software stack be upgraded to match Hercules?

Although this is an ongoing discussion between NOAA and MSU, a decision has not
yet been made. There are a lot of different variables which need to be
considered first. The most prudent approach at this time, is to flush out any
issues with the new software stack on Hercules, allow NOAA projects to port over
their workflows and models to Hercules, let these models and workflows run for a
while on Hercules, and then reevaluate the potential impact of running the new
software stack on Orion. It will also depend greatly on the projected longevity
of the Orion system. Orion runs the CentOS 7.x Operating System. Vendor support
for this OS ends on June 30th, 2024. The OS's end of vendor support date may
drive the need to upgrade Orion to the new software stack. If this were to
happen then multiple user notices would be sent out over a period of multiple
months.

.. _msu_faq_should_i_use_the_work_or_work2_file_system_for_my_project:

.. rubric:: Should I use the ``/work`` or ``/work2`` file system for my project?

Although all NOAA projects have been provided with a disk allocation on both
file systems, there are some architectural differences between the two file
systems. The ``/work2`` file system has over 2x the capacity of ``/work``. It
also has a Solid State Disk (SSD) storage, which may improve small file
performance and random I/O. We recommend that you try both file systems and then
choose which one works better for your project.

.. _msu_faq_where_do_i_find_more_information_on_how_to_login:

.. rubric:: Where do I find more information on how to login?

Refer to `Logging In <logging-in>`

.. _msu_faq_where_do_i_find_more_information_on_msus_annual_security_trainig_and_password_requirements:

.. rubric:: Where do I find more information on MSU's annual security training and password requirements?

`Orion Password and Security Training Information </index.php/Orion_Password_and_Security_Training_Information>`__

.. _msu_faq_how_do_i_use_jupyter_notebooks_on_orion:

.. rubric:: How do I use Jupyter Notebooks on Orion?

Typically, port forwarding is needed to launch and use jupyter from the command
line. Orion's current security posture does not allow port forwarding, so the
recommended method for using Jupyter on Orion is to use the interactive Jupyter
Notebooks application or the Virtual Desktop on our Open OnDemand HPC portal:
https://orion-ood.hpc.msstate.edu

Implementation of Open OnDemand includes a Jupyter Notebook interactive server
application under the :menuselection:`Interactive Apps`` dropdown menu. When you
select the jupyter notebook application, on the next page you can enter in slurm
job parameters then launch the server application on one of the Orion nodes as a
job.

MSU has documentation for the Open OnDemand interface `here
<https://intranet.hpc.msstate.edu/helpdesk/resource-docs/ood_guide.php>`__

The OOD jupyter notebook instance is currently launched with the python/3.7.5
module that is available on Orion. You should be able to launch custom kernels
by placing the kernel specs in ``$HOME/.local/share/jupyter/kernels`` before
launching jupyter notebook with OOD.

.. _msu_faq_why_am_i_getting_a_segmentation_fault_occured_error_when_i_run_my_program:

.. rubric:: Why am I getting a "segmentation fault occurred" error when I run my program?

-  Job crashed due to small stack size (on both Orion and Hercules)

Although this may be a bug in your code, it is more likely to be a stack size
issue. Stack space is a segment of program memory that is typically used by
temporary variables in the program's subroutines and functions. Attempting to
access a variable that resides beyond the stack space boundary will cause
segmentation faults. The usual remedy is to increase the stack size and re-run
your program. The soft limit (default) for the stack size on Orion and Hercules
is set to 16KB. You can set this limit higher by running ``ulimit -s
<stack_size>`` and then running ``ulimit -s`` to verify. We recommend that you
set this within your batch scripts and do not add this to your ``~/.bashrc`` file,
as it can cause unintended consequences.

-  Job crashed due to out of node memory (on both Orion and Hercules)

The job crashed for large size and worked for small size. One possibility is out
of node physical memory. The suggested solution is to use more nodes, or run
less MPI tasks per node. Make sure that the node is not shared with other jobs
(``#SBATCH --exclusive``). job crashed due to out of MPI buffer size for intel
compiler

-  Job crashed due to MPI buffer size on Hercules only

The job crashed for large size and worked for small size. The large size worked
for a single MPI task and crashed with multiple MPI tasks. In intel compiler,
the default ``I_MPI_SHM_HEAP_VSIZE`` is 8192 (unit is MB). Users can redefine this
value before ``srun`` command based on the maximum node memory (not exceeding the
maximum node memory). When too big, it will have the MPI initialization error
as: unable to allocate shared memory.

-  ``--ntasks-per-node`` option on Hercules only

For the large domain, when ``--ntasks-per-node`` has been used, the model
crashes. Since the hercules has much large memory on each node, user does not
need to use this option.


.. rubric:: Use modules on Hercules - For WRF model as an example

Loading modules will provide the defined environment variables. However the
variable name may not be what you used on other machines. Users should check and
make sure. Following is an example when compile WRF model on Hercules.

-  Netcdf

The netcdf-c and netcdf-fortran have been installed in different directories.
After loading the modules, it provides ``NETCDF_C_ROOT`` and
``NETCDF_FORTRAN_ROOT``. Users need to copy them to the same directory and provide
the definition of “NETCDF” in order to compile WRF. For example, I create a new
directory for ``$NETCDF``:

.. code::

   $ cp -r $NETCDF_C_ROOT/\* $NETCDF/.
   $ cp -r NETCDF_FORTRAN_ROOT/\* $NETCDF/.

-  Parallel netcdf

After loading the module, it provides ``PARALLEL_NETCDF_ROOT``. Users need to
define “PNETCDF”. For example: ``export PNETCDF=$PARALLEL_NETCDF_ROOT``.
Otherwise, the WRF model compiles successfully. But fails when you use parallel
IO (such as set ``io_form_input=11`` in ``namelist.input``).
