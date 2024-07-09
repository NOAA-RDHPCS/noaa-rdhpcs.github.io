###########################
Policies and Best Practices
###########################


System Usage
============

Login Node Usage
----------------

The login (front end) nodes are a part of the service nodes–providing
access to the rest of the cluster. Login nodes are not intended for
computation, instead they should be used for code and batch job
management tasks. Running heavy processes directly on the login nodes
may negatively impact other users who interact with the cluster.

Login nodes should be used for tasks similar to the following:

- Editing and compiling code
- Organizing data on project and home directories
- Submit jobs (batch, dtn, etc, ...)
- Monitor jobs

Use compute nodes for processes that require more cores, longer run
times, or more memory.

Cron Usage
==========

To schedule recurring jobs, cron is provided for users. On most
systems, cron jobs will be started on service/login nodes; therefore
the login node usage policy applies to cron jobs.

However, on systems such as Gaea, cron is no longer permitted. Instead,
**scrontab** is used.

**Scrontab** is a Slurm-managed crontab that runs on a designated
partition rather than the login nodes.

**Best Practices:**

- Please **DO** review your crontab/scrontab entries once a month and
  remove unneeded entries to assure efficient RDHPCS resource
  utilization! It is easy to forget to remove your crontab entries at
  the conclusion of your experiment!
- **DO NOT** redirect the output of your cron jobs to /dev/null. This
  will make it impossible for you to be notified of problems with your
  cron job.
- **DO NOT** rely on cron jobs running on specific hosts. Your crontab
  will be visible from all frontends, and jobs may be launched from
  any available frontend. (See Chron for more details).
- **DO NOT** run "scp", "rsync", and "tar" processes which last more
  than 2 minutes directly on the cron servers. They are most likely
  suited for the "service" or one of the "serial" parallel
  environments:
- **DO** Remove all "busy waits" (tight loops without sleeps) from
  workflow management scripts.
- **DO** add a line like: "MAILTO=First.Last@noaa.gov" to the top of
  your crontab or add scron directive “--mail-user=<email>” to your
  scrontab, so you get emails for cron job output (errors).

For Rocoto, it is always advisable to use the "default" version rather
than a specific version as shown below:

.. code-block:: shell

   $ /apps/rocoto/default/bin/rocotorun -w /path/to/myxml/wrf.xml -d /path/to/mydb/wrf.db

Any process launched from cron **MUST** be one of the following:

- call to "workflowmgr" for controlling recurring tasks, or
- other scripts that submits or manages jobs in the batch system, or
- short running (less than 1 minute) data manipulation task.
- **DO NOT** run compute tasks or large data management tasks from
  cron, as they will have a negative impact on all users and may cause
  system instability problems. Such processes may be killed without
  warning.

Cron Job Frequency
------------------

**DO NOT** create crontabs that execute every minute. There is no
reason to do so and it creates an unnecessary load on the system. This
rule also applies to all instances of the Workflow Manager.

Please use the following rules as to how often (at most) to call a
repeating processes:

- Does not run in an approved real-time reservation:

  - No more than every 10 minutes.

- Runs in an approved real-time reservation:

  - No more than every 3 minutes.

File System Usage Practices and Policies
========================================

High Performance File System (HPFS - Scratch)
---------------------------------------------

Hera's /scratch(1,2), Jet's
/lfs(1,4), and Niagara's /collab1 are scratch file systems for your
input and output project data for running current jobs, **NOT** for
long term data storage.

.. warning::

  Data on scratch is **NOT** backed up.

1. Keep source code and critical configuration files on /home, and
   back up critical data to HPSS.
2. Data unused over 30 days is considered old and should be removed or
   moved to a different storage vehicle.
3. Tar up old small files (or delete them) to free up space on the SSD
   pool and stay under your file count quota.
4. Large files are still optimal for HPC batch job performance.
5. Do not open with O_APPEND unless you really need it.
6. High performance file systems such as Lustre Filesystems are
   designed for high performance and high resiliency. While they are
   good at what they do, they're not very good for very high Meta data
   intensive operations such as du, find, etc. Please avoid running
   such commands to monitor your file space space usage, especially
   from the top of your project level directory.

For more information about projects, see :doc:`Slurm </slurm/index>`


General Parallel File System (GPFS)
-----------------------------------

Gaea’s /gpfs/f5 is a general parallel
file system which provides project directories for short term project
data. F5 is not backed up. Users must ensure important files are
replicated to another off-site location

/data_untrusted
---------------

Every RDHPCS user is provided a user directory in the /data-untrusted
directory on each HPFS (scratch) file system on RDHPCS systems (Hera,
Jet, Niagara, etc.) they have access to.

Your "$SCRATCH/data_untrusted/$USER" directory is provided so that you
can move data on and off of the system from any external site, and is
for transient data only. Data should be removed from this directory as
soon as it’s transferred to its final destination.

Your inaction to remove old data from this directory could negatively
impact other users on the system, therefore; failure to comply with
this policy will force us to remove your data and disable your access
to this directory.

HFS
---

The /home file system (HFS) is for small amounts of critical
labor-intensive data, like source code, that need timely access. The
HFS is backed up nightly and weekly. Nightly backups are kept for a
week, and weekly backups are kept for at least 6 months.

HFS data can be retrieved from our snapshots - please see
:ref:`home_snapshot` for more information.

Each RDHPCS user is given a home directory (/home/First.Last) and a
**50GB** quota on each system (Hera, Jet, etc.) they have an account
on. All files owned by you in /home are counted not just files in your
/home/First.Last directory.

Usage and quota can be checked using the ``sacccount_params`` or the
``quota`` commands.  See :doc:`/slurm/index` for details.

If more quota is required, start a system help ticket with a request
and justification.

.. caution::

   Please **DO NOT** run jobs against files in your Home File System
   (HFS). This includes keeping input/output files or executable files
   for a parallel run in your home directory or even using symlinks in
   your home directories that point to your files in your project
   space in the scratch filesystem. It puts a tremendous burden on
   the HFS and has an adverse impact on all the users on the system.


Filesystem Backup and Data Retention
====================================

* /home

  * For code and important source files
  * Is backed up nightly.  Look at the snapshot directory
    (/home/.snapshot) to see what options are available

* /scratch

  * For data to drive models and model results
  * Scratch file systems are not backed up
  * Scratch file systems are not purged, it is up to the individual
    projects to determine the purge policy
  * Only copy new data to the HSMS, it is a scarce resource and is not
    infinite.

All of the file systems with the exception of /home and the HSMS are
considered scratch file systems. We want users to be aware of the
risks with those file systems. The scratch file systems are not backed
up in any way. While we do our best to ensure the reliability of those
file systems, they are not perfect and there is a small risk that data
could be lost without any possibility of recovery.

.. _home_snapshot:

Recover Recently Deleted Files from /home
-----------------------------------------

**Differences between the HPCS**

The home filesystem is backed up regularly. However, the filesystem
also supports snapshots, which will allow you to retrieve your own
files if they have been deleted over the last few days. The number of
days is different for Hera and Jet clusters.

Look at the snapshot directory (/home/$USER/.snapshot) to see what options
are available. Each directory listed there represent a day.

Consider an example:

.. code-block:: shell

    $ ls $HOME/.snapshot
    2021-09-09_0015-0600.daily  2021-09-14_0015-0600.daily  2021-09-19_0015-0600.daily
    2021-09-10_0015-0600.daily  2021-09-15_0015-0600.daily  2021-09-20_0015-0600.daily
    2021-09-11_0015-0600.daily  2021-09-16_0015-0600.daily  2021-09-21_0015-0600.daily
    2021-09-12_0015-0600.daily	2021-09-17_0015-0600.daily  2021-09-22_0015-0600.daily
    2021-09-13_0015-0600.daily	2021-09-18_0015-0600.daily  2021-09-23_0015-0600.daily

You can then access the old files in your copy of your home directory
under the appropriate snapshot.

So, if you want to recover files in your $HOME from January 22nd, 2024:

.. code-block:: shell

    $ cd $HOME/.snapshot/2021-09-22_0015+0000.homeSnap

Copy the files you want from the here, the snapshot,  to anywhere in
your real home.


HPSS (Data Retention)
---------------------

Retention based storage is the HPSS archive policy in Fairmont, to
better manage data growth.

Six retention storage pools (1-5year and Permanent) were created. Each
retention period is set up as a separate file family. This means all
data for a given retention period is stored on the same tapes.

All HPSS projects were then configured to write to one or more of
these pools. Data in these pools expires based upon the retention pool
it was written in and would be deleted upon expiration.

All files in the HPSS archive have been assigned an expiration date
based on the file create time and the retention period it was written
to. Upon expiration files will be deleted from the HPSS archive.

Expired Data Deletion Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**User Notification**

Users will be notified of expired data via posted lists and email.
These notifications will take place on or before the first day of the
month following the data’s expiration.

For example, data that has an expiration date between October 1 and
October 31 2023 will have its notification posted on or before
November 1, 2023. The expired file list is located on HPSS in
/Expired_Data_Lists/expired.YYYY-MM.txt. All HPSS users have read
access to this file and can retrieve it for review. The file is easily
searchable by HPSS username.

For each file included in the expired list the file owner, file group,
filename/path, and expire date are shown, for example:

``root system /1year/SYSADMIN/nesccmgmt/test_file-1G-11 Jul-6-2023``.

Email notification will also be sent to all users who have data listed
in this file. It is the user’s responsibility to regularly check the
posted list for expired files they own. Once deleted these files
cannot be recovered.

**Expired Data - Deletions**

The following table maps out when future deletions will take place.

+------------------+-------------------+-------------+
| Expire Date      | Notification Date | Delete Date |
+==================+===================+=============+
| Dec 1 – Dec 31   | January 1         | February 1  |
+------------------+-------------------+-------------+
| Feb 1 – Feb 28   | March 1           | April 1     |
+------------------+-------------------+-------------+
| Mar 1 – Mar 31   | April 1           | May 1       |
+------------------+-------------------+-------------+
| Apr 1 – Apr 30   | May 1             | June 1      |
+------------------+-------------------+-------------+
| May 1 – May 31   | June 1            | July 1      |
+------------------+-------------------+-------------+
| Jun 1 – June 30  | July 1            | August 1    |
+------------------+-------------------+-------------+
| Jul 1 – Jul 31   | August 1          | September 1 |
+------------------+-------------------+-------------+
| Aug 1 – Aug 30   | September 1       | October 1   |
+------------------+-------------------+-------------+
| Sept 1 – Sept 30 | October 1         | November 1  |
+------------------+-------------------+-------------+
| Oct 1 – Oct 31   | November 1        | December 1  |
+------------------+-------------------+-------------+
| Nov 1 – Nov 30   | December 1        | January 1   |
+------------------+-------------------+-------------+



Data Recovery Policy
^^^^^^^^^^^^^^^^^^^^

Occasionally an archive tape is damaged or otherwise becomes partially
unreadable. When that happens, the local RDHPCS staff works with the
manufacturer to troubleshoot the problem and take additional steps to
attempt to recover the missing data.

Very rarely, even with these additional efforts, we are unable to
recover missing files. The user will be told which files
we cannot recover.

In that case, the user has one further option. There are a number of
outside recovery services which will make further attempts at recovery
for a fee. Some charge a flat fee, some charge more if they are able
to recover than if they are unable to recover.

If the user wishes to sign up for such a service and pay the fee,
RDHPCS will handle the logistics of shipping and other coordination
with the recovery service.


Data Disposition
================

RDHPCS users’ data is the responsibility of the user, the PI, and the
Portfolio Manager. The PI or Portfolio Manager, as appropriate, can
initiate a help request to manage data. As a policy matter, RDHPCS
System Management does not initiate the deletion of data belonging to
active users or active projects, except as detailed below.

HPFS (Scratch) Data
-------------------

Inactive users’ and closed projects’ data shall be dispositioned by
the PI or Portfolio Manager to maintain efficient usage of RDHPCS
resources. If the PI or Portfolio Manager cannot personally implement
the disposition of the data, the PI or PM can issue a help ticket, and
request that RDHPCS System Management do so.

The RDHPCS program policy is to NOT delete active project HPFS data.
If the PI or Portfolio Manager so directs in a help request, we will
change ownership of active HPFS project data to another project
member.

Niagara Per User Data
---------------------

As Niagara is a hybrid system (a cross between a traditional HPC
system and a data transfer/collaboration system, available to all
RDHPCS users), the file system management needs to be handled
differently then on more traditional HPC systems (Hera and Jet). As a
result, the following data management policies are implemented on
Niagara:

* All files under the ``collab1/data_untrusted/$USER`` directory tree
  which have not been accessed in the last 5 days will be
  automatically purged.
* All files under the ``/collab1/data/$USER`` directory tree which
  have not been accessed in the last 60 days will be automatically
  purged.
* All files under the ``/collab1/data/$PROJECT`` directory are treated
  the same as HPFS (scracth) data and are not deleted.

The definition of access time is the last time the file was opened for
reading or writing.

.. note::

   If the file system's usage starts getting close to the total
   capacity, we will be forced implement a more aggressive purge
   policy (i.e. 30 day or 15 day purge) . So please actively manage
   your data.

Home File System (HFS) Data
----------------------------

The RDHPCS program policy is to **NOT** delete active users Home File
System (HFS or /home) data, or to change ownership of HFS data. The
Portfolio Manager may issue a help ticket to request special
dispositioning of HFS data.

Deactivated users' HFS data may be removed and saved to the tape
archive system in a retention pool of at least 5 years.


Managing Packages in ``/contrib``
=================================

Overview of ``contrib`` Packages
--------------------------------

The system staff do not have the resources to maintain every piece of
software requested. There are also cases where developers of the
software are the system users, and putting a layer in between them and
the rest of the system users is inefficient. To support these needs,
we have developed a ``/contrib`` package process. A ``/contrib`` package
is one that is maintained by a user on the system. The system staff
are not responsible for the use or maintenance of these packages.

.. _contrib:

Responsibilities of a ``contrib`` Package Maintainer
----------------------------------------------------

Maintainers are expected to:

* Follow the naming conventions and guidelines outlined in this
  document
* Apply security updates as quickly as possible after they become
  availble
* Update software for bug fixes and functionality as users request
* Respond to user email requests for help using the software

``contrib`` Packages Guidelines
-------------------------------

* The package should be a single program or toolset.  We want to
  prevent having a single directory being a repository for many
  different packages.
* If you support multiple functions, please request multiple packages.
* The package may have build dependencies on other packages, but it
  must otherwise be self-contained.
* The package may not contain links to files in user or project
  directories.
* We expect each package to be less than 100MB.
* If you need more, please tell us when you request your package.
* We can support larger packages but we need to monitor the space
  used.
* We expect each package to have less than 100 files.

``contrib`` Package Maintainer Requests
---------------------------------------

If you wish to maintain a package in ``contrib``, please send a request to
the Help System with:

* List of the packages you wish to maintain.
* Justification why each is needed.
* The user who will be maintaining the package.

.. note::

   In certain cases, multiple users can manage a package, and unix
   group write permissions may be granted for the directory. In that
   case, specify the unix group that will be maintaining the package.

Managing a ``contrib`` Package
------------------------------

After your request has been approved to use space in the ``/contrib``
directory, two directories will be created for you:

* ``/contrib/<package>``, and
* ``/contrib/<package>/modulefiles``

This is where you will install your software for this package and
optionally install a module to allow users to load the environmental
settings necessary to use this package. The variable <package> is the
name of the ``/contrib`` package you requested. The directory convention
of ``/contrib`` is designed to match that of /apps. Thus, one piece of
software goes into a subdirectory under the ``/contrib`` level. If you
want to manage multiple packages, please request multiple ``/contrib``
package. You can do this all at one time when submitting your request
to the Help System.

Maintaining "Metadata" for ``contrib`` Packages
-----------------------------------------------

Since ``contrib`` packages are intended to be used by other users on the
system it will be helpful to have a ``/contrib/<package>/README`` file
that contains at least the following information:

* Package Name:
* Purpose:
* Maintainer:
* Contact info for questions/help:
* Any other info that will be useful for general users to know


``contrib`` Package Directory Naming Conventions
------------------------------------------------

When installing software into your ``/contrib`` directory, first determine
if this is software that should be versioned (multiple versions may
exist at one time) or unversioned (there will only ever be one version
installed, and upgrade will overwrite the existing software). For
verisoned software, please install it into a subdirectory of your
package that is named after the version number. For supporting
multiple versions of software the install path should be:

``/contrib/<package>/<version>``

Where <package> is the directory assigned to you and $VER is the
version number. Thus if your package is named ferret and you are
installing the version 3.2.6, the software should be installed in:

``/contrib/ferret/3.2.6``

For supporting un-versioned software, only install the software
directly into your package directory:

``/contrib/<package>/``


Queue Policy
============

Overview
--------

* The queuing system should allow groups/projects to spend their
  allocation each month.
* The tension between keeping persistent jobs in the system and
  running very large jobs suggests that there should be a limit on the
  number of cores a job may use, but with a capability to make
  exceptions for “novel” jobs that may require up to the entire
  system.

  This will promote consideration of whether a job requires a large
  number of cores due to, for example, memory or schedule constraints,
  or whether it is simply desired.
* There should be queues with different priority levels usable by the
  scheduling algorithm. At the very least, run-time variability would
  need to be assessed before we could even think of implementing this.

Specifying a Quality of Service (QOS)
-------------------------------------

To specify a quality-of-service (QOS), use --qos (-q).

For example, to specify the batch QOS:

.. code-block:: shell

    $  #SBATCH -q batch

Several different QOS's are usually available.

Changing QOS's
--------------

You can change the QOS of jobs at submission and post submission.
While you can use this feature in many different ways, one practical
situation where this may be useful is to maintain your fairshare
priority by starting jobs in the “windfall” QOS, then changing to the
“batch” QOS if it is still pending. See `Slurm_` for more information
on Fairshare

.. note::

   If your job does not meet the criteria of the QOS that you change
   it to, it will remain pending indefinitely.

You can immediately change the QOS of your pending job(s).

The following is an example of immediately changing 2 pending jobs
(26866 and 26867) to the “batch” QOS:

.. code-block:: shell

   $ scontrol update job 26866,26867 qos=batch

When submitting a job to a certain QOS, you can tell Slurm to change
it to a different QOS at a certain time if it is still pending. In the
following example, you submit the job to the “windfall” QOS, then tell
Slurm to change the job to the “batch” QOS if it’s still pending after
5 minutes. NOTE: Do not use a time less than 2 min (120 seconds).

.. note::

   On Orion and Hercules the “at” functionality is only available on login1.


.. code-block:: shell

   $ sbatch -q windfall jobfile
   Submitted batch job 26990

.. code-block:: shell

   $ echo scontrol update job 26990 qos=batch | at -M now +5min
   warning: commands will be executed using /bin/sh
   job 6 at Sun Dec 17 16:07:00 2023

You can change the QOS of all your pending job(s) in a QOS to another
QOS after it has been pending for a certain time. The following
example script will change all your pending “windfall” jobs to “batch”
if they have been pending for at least 600 seconds (10 min), whenever
you run it.

.. note::

   Do not use a time less than 120 seconds (2 min).

Jet and Hera
------------

.. note::

  If you have an allocation of "windfall only" (Allocation = 1) you
  can only submit to the windfall or gpuwf QOS.

.. list-table::
   :header-rows: 1
   :align: left

   * - QOS
     - Minimum Nodes
     - Maximum Nodes
     - Maximum Wall Clock
     - Billing TRES Factor
     - Description and Limits
   * - All QOS's
     -
     -
     -
     -
     - Max of 400 pending/running jobs per project/account, additional
       jobs will be rejected. Max of 20 jobs per project/account will
       gain age priority. Exceptions are stated below.
   * - batch
     - 1
     - 8,400\ [1]_
     - 8 hours
     - 1.0
     -  Default QOS for non-reservation jobs with an allocation more
        then *Windfall-Only* (``RawShare=1``).
   * - urgent
     - 1
     - 8,400\ [1]_
     - 8 hours
     - 2.0
     -  QOS for a job that requires more urgency than *batch*. Your
        project's :ref:`FairShare <slurm-fairshare>` will be lowered
        at 2.0x the rate as compared to *batch*.  Only one job per
        project/account can be pending/runnin at any time. When a
        project's FairShare is below 0.45, jobs submmit to *urgent*
        are automatically changed to *batch* and users notified via
        stderr.
   * - debug
     - 1
     - 8,400\ [1]_
     - 30 minutes
     - 1.25
     - Highest priority QOS, useful for debugging sessions.  Your
       project :ref:`FairShare <slurm-fairshare>` will be lowered at
       1.25x the rate as compared to *batch*.  Only two jobs per user
       can be pending/running at any time.  This QOS should NOT be
       used for fast-turnaround of general work. While the *debug* QOS
       is available, we recommend that if you need to work through an
       iterative process to debug a code, that you submit a longer
       running interactive job to the default QOS so that you can
       restart your application over and over again without having to
       start a new batch job.
   * - gpu
     - 20 (1 node)
     - 800 (40 nodes)\ [1]_
     - 168 hours (7 days)
     - 1.0
     - This QOS can only be used on Hera in combination with the fge
       partition. Max total “GrpTRESRunMins” of 720,000 core-minutes
       (600 node-hours) of running jobs at any time, per
       project-account. “GrpTRESRunMins” is defined as cores_allocated
       * wallclock_requested of running jobs. A project can have up to
       the max number of jobs pending/running as defined above, but
       the queued jobs will NOT be considered for scheduling if the
       project’s running jobs exceed this limit. Use this gsheet as a
       reference: Grp TRES Run Minutes For example, the following
       combinations of the max running jobs per project-account are
       permitted: 1. A project can have three 1-node jobs at 168 hours
       of wallclock and one 1-node job at 96 hours of wallclock. 2. A
       project can have one 8-node job at 75 hours of wallclock.
   * - gpuwf
     - 20 (1 node)
     - 800 (40 nodes)\ [1]_
     - 168 hours (7 days)
     - 1.0
     - This QOS can only be used on Hera in combination with the fge
       partition. Max total “GrpTRESRunMins” of 201,600 core-minutes
       (168 node-hours) of running jobs at any time, per
       project-account. “GrpTRESRunMins” is defined as cores_allocated
       * wallclock_requested of running jobs. A project can have up to
       the max number of jobs pending/running as defined above, but
       the queued jobs will NOT be considered for scheduling if the
       project’s running jobs exceed this limit. Use this gsheet as a
       reference: Grp TRES Run Minutes For example the following are
       combinations of the max running jobs per project-account that
       are permitted: 1. A project can have two 2-node jobs at 24
       hours of wallclock and one 1-node job at 72 hours of wallclock.
       1. A project can have one 1-node job at 168 hours of wallclock.
       Lowest priority QOS for use with GPU nodes. If you have an
       allocation of “windfall only” (Monthly allocation = 1) you can
       only submit to this QOS. Submitting to this QOS will NOT affect
       your future job priority FairShare Factor (f). EffectvUsage = 0.
       See How FairShare Works. This QOS is useful for low priority
       jobs that will only run when the system (partition(s)) has
       enough unused space available, while not lowering the project’s
       FairShare priority.
   * - windfall
     - 1
     - 8,400\ [1]_
     - 8 hours (Partition exception: *service*)
     - 0.0
     - Lowest priority QOS.  If you have an allocation of
       windfall-only (monthly allocation is 1) you can only submit to
       this QOS.  Submitting to this QOS will NOT affect your future
       job priority :ref:`FairShare <slurm-fairshare>` factor (f) for
       your non-windfall jobs. Useful for low priority jobs that will
       only run when the system/partition has enough unused space
       available while not effecting the project's FairShare priority.
   * - novel
     - 501 (Orion), 251 (Hercules)
     - Largest partition size
     - 8 hours
     - 1.0
     - QOS for running novel or experimental where nearly the full
       system is required.  If you need to use the *novel* QOS, please
       submit a ticket to the :ref:`help system <getting_help>` and
       tell us what you want to do.  We will normally have to arrange
       for some time for the job to go through, and we would like to
       plan the process with you.

.. [1] Some partitions are small than the **Max Cores** QOS limit.
   Jobs submitted only to partitions with an insufficient number of
   cores will get stuck in pending, will not run, and will have to be
   manually deleted by the user. The max nodes allowed per partition
   is the min of the max cores allowed divided by the cores per node
   of the partition (Hera and kJet: 8400/40=210 nodes) or the max
   number of nodes in the partition (vJet: 288 nodes).

Gaea
----

This section documents the queue structure on Gaea.
The original queue policy was approved through NOAA's HPC Integrated
Management Team. Changes and fine-tuning to the queue structure can be
done on a weekly basis through the Configuration Management process.

The following guidelines were put in place:


General Recommendations
-----------------------

* Use a fair-share algorithm that can throttle scheduling priority by
  comparing how much of a particular allocation has been used at a
  given time with how much should have been used, assuming constant
  proportional usage. This will promote steady usage throughout the
  month.
* Use two separate allocations, renewed monthly, with multiple queues
  drawing down each of them:

  * 50% of the available time for high-priority and urgent work. That
    should minimize queue wait time. Queues are:

    * Urgent, for schedule-driven work that must be completed ASAP.
    * Novel, for jobs that have unusual resource requirements,
      typically needing more than 25% of the system’s cores. These can
      be run during an 8-hour period immediately after Preventative
      Maintenance is complete, since no other jobs will be running at
      that time.

  * 50% for all other **normal-priority** allocated work. Queues would be:

    * Batch, for regular allocated jobs
    * Debugging/Interactive work
    * Windfall, a quality of service (QOS) tag, for work that will not
      be charged against an allocation. Windfall can be specified with
      '-l qos=' directive, as:

.. code-block:: shell

    $ sbatch –-qos=windfall

or in your job script:

.. code-block:: shell

    #SBATCH -–qos=windfall

Priorities Between QOS
-------------------------

* Normally, the Urgent QOS will have the highest priority but remain
  subject to the fair-share algorithm. This will discourage groups
  from hoarding high-priority time for the end of the month.
* Within a group/project, jobs in the Urgent queue are higher priority
  than jobs in the Normal queue, with each group expected to manage
  the intra-group mix per their allocation.
* At any given time, the suite of jobs drawn from the Urgent queue and
  running on the system should use about 50% of the available cores
  (per the fair-share algorithm), but that suite is permitted to use
  more than 50% as needed (with the implication that less than 50%
  will be used at other times of the month).
* Limit the largest job to 25% of the available cores except in the
  Novel queue.
* Limit time requested for individual job segments to 12 hours.
* Interactive/debugging jobs have a tiered limit.


Debug & Batch QOS
-----------------

Interactive / Debug The interactive queue may have different time
limits based on the size of the submitted job. To see the current
queue wallclock limits, run

.. code-block:: shell

  $ sacctmgr show qos format=Name,MaxWall
