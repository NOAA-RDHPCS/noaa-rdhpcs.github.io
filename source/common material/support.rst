.. _login_front_end_node_usage_policy:

Login (Front End) Node Usage Policy
===================================
The login (front end) nodes are a part of the service nodes that provide
access to the rest of the cluster. They are intended for code and batch
job management tasks, not for computation.

Running jobs or processes directly on the login nodes causes load that
can negatively affect other users and overall system efficiency and
utilization.

Login nodes should ONLY be used for tasks similar to the following:

-  Editing and compiling code
-  Organizing data on project and home directories
-  Copying data on and of off the system
-  Accessing external databases or performing other operations that
   require external access
-  Running very short (less than 1 minute) 1 core, low memory (<2GB),
   low compute intensity "glue" jobs

Tasks that do not fit into the above criteria (including
compute-intensive or MPI jobs) should be run via the batch system.
Processes that require more cores, longer run times, or more memory,
particularly if they execute regularly, should be run on compute or big
memory nodes, not a front end. There are two ways do this:

-  Create a batch script and submit it as a normal job, see: `Running
   and Monitoring
   Jobs <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Running_and_Monitoring_Jobs_on_Jet_and_Theia_-_SLURM>`__.
-  See `Submitting an Interactive
   Job <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Running_and_Monitoring_Jobs_on_Jet_and_Hera(Theia)_-_SLURM#Submitting_an_Interactive_Job>`__
   on how to create an interactive job session.
-  **IMPORTANT NOTE**: Running a job in the "service" partition is the
   same as running on Login nodes. So please use a partition other than
   the "service" partition for your jobs, especially if your jobs don't
   need access to external resources (such as HPSS). If your jobs
   require access to an external resource you need to separate your jobs
   into two separate jobs, one to fetch/put the files that will be
   submitted to the "service" partition and another to do the
   computations which should be submitted to a partition other than the
   service partition; using the dependency feature of Slurm may be
   helpful in coordinating these two types of jobs.

.. _automated_process_monitoring_deletion_and_notification:

Automated Process Monitoring, Deletion, and Notification
--------------------------------------------------------

In order to avoid significant adverse user impact due to processes
violating the policies we have implemented a process monitoring tool
that constantly monitors the Login Nodes for policy violations, and
takes the following actions:

-  Terminates any process that is prohibited from running on the login
   node
-  Terminates any process that is consuming more than 300% CPU (>3
   threads) for longer than 10 minutes of CPU time.
-  Terminates any process that is consuming more than 30% of total
   system memory for longer than 1 minute of CPU time.
-  Sends an email notification to the responsible user

When you receive such an email notification please take the necessary
remedial action. Usually the remedy is to run such process on a compute
node as documented in the previous section. If you have any questions
please feel free to contact the appropriate helpdesk. `Help
Requests <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__

.. _cron_usage_policy_and_best_practices:

Cron Usage Policy and Best Practices
====================================

The `Cron <http://en.wikipedia.org/wiki/Cron>`__ service is provided for
users to launch time-sensitive jobs. All cron jobs will be started on
the service/login nodes; therefore the `Login (Front End) Node Usage
Policy <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Login_(Front_End)_Node_Usage_Policy>`__
applies to all Cron jobs

Best Practices:

-  **Please DO** review your crontab entries **once a month** and remove
   unneeded entries to assure efficient RDHPCS resource utilization! It
   is easy to forget to remove your crontab entries at the conclusion of
   your experiment!

-  **DO NOT** redirect the output of your cron jobs to */dev/null*. This
   will make it impossible for you to be notified of problems with your
   cron job.

-  **DO NOT** rely on cron jobs running on specific hosts. Your crontab
   will be visible from all frontends, and jobs may be launched from any
   available frontend. (See Chron for more details).

-  **DO NOT** run "scp", "rsync", and "tar" processes which last more
   than 2 minutes directly on the cron servers. They are most likely
   suited for the "service" or one of the "serial" parallel
   environments:

-  **Remove** all "busy waits" (tight loops without sleeps) from
   workflow management scripts.

-  Add a line like: **"MAILTO=First.Last@noaa.gov"** to the top of your
   crontab, so you get emails for cron job output (errors).

-  For Rocoto, it is always advisable to use the "default" version
   rather than a specific version as shown below:

``   /apps/rocoto/``\ **``default``**\ ``/bin/rocotorun -w /path/to/myxml/wrf.xml -d /path/to/mydb/wrf.db``

Any process launched from cron **MUST** be one of the following:

-  call to "workflowmgr" for controlling recurring tasks, or
-  other scripts that submits or manages jobs in the batch system, or
-  short running (less than 1 minute) data manipulation task.
-  **DO NOT** run compute tasks or large data management tasks from
   cron, as they will have a negative impact on all users and may cause
   system instability problems. Such processes may be killed without
   warning.

.. _cron_job_frequency:

Cron Job Frequency
------------------

**DO NOT** create crontabs that execute every minute. There is no reason
to do so and it creates an unnecessary load on the system. This rule
also applies to all instances of the Workflow Manager.

Please use the following rules as to how often (at most) to call a
repeating processes:

-  Does not run in an approved real-time reservation:

   -  No more than every 10 minutes.

-  Runs in an approved real-time reservation:

   -  No more than every 3 minutes.

.. _using_cron:

Using Cron
----------

Login to a frontend node on Hera, Jet or Niagara. Display or Edit your
crontab with the following commands:

::

   crontab -l 
   crontab -e

The format of the crontab entries is as follows (run "**man 5 crontab**"
for more details):

::

   Field1 Field2 Field3 Field4 Field5 Command

Where the fields are defined as (run "**man 5 crontab**" for more
details):

::

   Field1 - minute (0-59) 
   Field2 - hour (0-23) 
   Field3 - day of month (1-31) 
   Field4 - month (1-12) 
   Field5 - day of week (0-7, both 0 and 7 are Sunday)

Command is any standard command one would run from the command line. You
should use the full path to the program and not assume anything about
the current directory. By default, the command should follow bash shell
syntax, unless you know what you are doing and change the SHELL
variable.

**Run "man 5 crontab" for more details.**

There are a few important variables that can be set in your crontab. To
set the variables, just put the settings at the top of your crontab. Ex:

::

   MAILTO=[mailto:Joe.Z.Smith@noaa.gov Joe.Z.Smith@noaa.gov]

If you want to change the shell so that tcsh is used, which will affect
the formatting of the crontab entry:

::

   SHELL=/bin/tcsh

Example crontab:

::

   MAILTO=[mailto:Joe.Z.Smith@noaa.gov Joe.Z.Smith@noaa.gov]

       0,15,30,45 * * * * /home/joe.z.smith/bin/runmycommand 2&gt;&amp;1

.. _setting_the_environment_for_cron_processes:

Setting the Environment for Cron Processes
------------------------------------------

Cron will start processes with a *minimal* environment. This may be
inadequate for processes that interact with tools that are not located
in /usr/bin or /bin. For such cases, modify your shell script to
completely source the environment, like it is an interactive shell.

-  **For bash**, the first line in your script should look like:

::

   #!/bin/bash --login

-  **For ksh**:

::

   #!/bin/ksh --login

-  **For {t}csh**:

::

   #!/bin/tcsh

-  For executables or scripts in another language (perl, python, ruby):

Binaries and interpreted languages may not include the concept of
setting up the environment as an interactive shell does (tcsh, bash,
ksh). For such cases, use a wrapper script to set up your environment as
described above, and then execute a given binary. That way you can
simply prepend the wrapper script to your crontab entry. For example:

::

   15 */2 * * * /home/Joe.User/bin/run_cron_job.sh /home/Joe.User/bin/clean_up_files.rb -p foo 2&gt;&amp;1

.. _chron___distributed_high_availability_cron_services:

"chron" - distributed, high-availability, cron services
-------------------------------------------------------

Since RDHPCS machines have multiple front-end nodes, we have implemented
a system that unifies crontabs across all of the front ends. The
benefits of this are:

-  Users only have to maintain one crontab.
-  The crontab can be edited from any frontend.
-  Cron jobs will be distributed across all frontends.
-  If a front end is unavailable or the load is too high, cron jobs will
   be directed to another node.

A given job (single line in the crontab file) will run on the same host
for successive iterations, *as long as that host is up and the text of
the line does not change*. This deterministic behavior can be useful for
debugging workflows. However, *do not rely on cron jobs running on
specific hosts*, and you may need to check all frontend nodes to see if
a given cron job is still running.

Chron (short for "chronograph", but longer than "cron") is a set of
wrappers around the standard Linux cron daemon and tools. Chron takes
advantage of the $SHELL environment variable feature in cron to
intercept each job before it runs and ensure it is distributed across
the available nodes. A wrapper around the standard "crontab" utility
manages the setting of the $SHELL variable. **It is very important that
you do not attempt to bypass the wrapper script.** The wrapper script
will be in your path by default. If you encounter problems, please open
a help ticket.

.. _file_system_usage_practices:

File System Usage Practices
===========================

**HPFS (Scratch)**

The High Performance File Systems (HPFS): Hera's /scratch(1,2), Jet's
/lfs(1,4), and Niagara's /collab1 are scratch file systems for your
project data. They are **NOT** backed up and have various of degrees of
resiliency during facility incidents (power and cooling issues, etc.)
and operational incidents. Our scratch file systems are designed for
cost effective high performance and capacity, for the temporary storage
of your input, in process, and output data for running jobs. They are
**NOT** designed for high resiliency such that it is inevitable that we
will eventually have unplanned outages and data loss. You should **NOT**
store the only copy of data that you need to retain on these scratch
file systems as it is **NOT** recoverable if deleted or lost due to file
system resiliency.

#. Keep source code and critical configuration files on /home, and back
   up critical data to HPSS.
#. Tar up old small files (or delete them) to free up space on the SSD
   pool and stay under your file count quota.
#. Large files are still optimal for HPC batch job performance.
#. Do not open with O_APPEND unless you really need it.

.. _home_file_system_hfs:

Home File System (HFS)
----------------------

The /home file system (HFS) is for small amounts of critical
labor-intensive data, like source code, that needs timely access. The
HFS is backed up nightly and weekly. Nightly backups are kept for a
week, and weekly backups are kept for at least 6 months. HFS data can be
retrieved from our snapshots - please see
`here <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/FAQs_-_Frequently_Asked_Questions#How_can_I_recover_recently_deleted_files_from_.2Fhome.3F>`__.
Each RDHPCS user is given a home directory (/home/First.Last) and a 5GB
quota on each system (Hera, Jet, etc.) they have an account on. All
files owned by you in /home are counted not just files in your
/home/First.Last directory. Usage and quota can be checked using the
"quota" command or the "sacccount_params" command (`Getting Information
About Your
Account <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_Information_About_Your_Account_-_SLURM>`__).
If more quota is required, start a system help ticket with a request and
justification.
`HELP <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__

**CAUTION:** Please **DO NOT** run jobs against files in your Home File
System (HFS). This includes keeping input/output files or executable
files for a parallel run in your home directory or even using symlinks
in your home directories that point to your files in your project space
in the scratch filesystem. This puts a tremendous burden on the HFS and
has an adverse impact on all the users on the system.

::

   [John.Smith@hfe07 ~]$ quota
   Disk quotas for user John.Smith (uid 11111): 
        Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
   10.181.1.2:/testhome
                         0       0 57671680               1       0       0        
   10.181.1.1:/home
                    326144       0 5242880            1055       0       0        

.. _hpss_tape_system_hpss:

HPSS Tape System (HPSS)
-----------------------

The HPSS tape system is for data that you need to keep that can be
retrieved more slowly. The HPSS tape system is highly reliable but data
stored is single copied and is **NOT** backed up. Make prudent use of
the proper retention pool to control the size and cost of the tape
system. More information on the HPSS is found here:
`HPSS <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Using_the_HSMS_HPSS>`__

.. _world_writeable_permissions_on_data:

World Writeable Permissions on Data
-----------------------------------

It is highly recommended that you do **NOT** allow world-writable
permissions (drwxrwsr\ **w**\ x) for your directories/files.

Directories/files have the following permission structure (below is a
breakdown of **drwxrwsrwx**):

===== ===== ===== ============
d/f/l owner group other(world)
d     rwx   rws   rwx
===== ===== ===== ============

::

   # find /project-directory{3,4}/ -maxdepth 3 -type d -perm -o=w | xargs ls -ld
   drwxrwsrwx  5 First.Last      project1    4096 Aug 16 13:23 /project-directory3/project1
   drwxrwsrwx  8 First.Last      project2   12288 Aug 16 13:26 /project-directory3/project2
   drwxrwsrwx 24 First.Last      project3    8192 Aug 16 12:55 /project-directory4/project3
   drwxrwxrwx  4 First.Last      project4    4096 Aug 15 09:28 /project-directory4/project4
   drwxrwsrwx  10 First.Last     project5    4096 Jan 14  2019 /project-directory4/project5

Allowing the **write** (w) permission for **other(world)**
(drwxrwsr\ **w**\ x) puts the directory/files at risk for any user on
the system (or in your project) mistakenly doing an "rm -rf" and
deleting all of your data.

| If you have directories and files with world-write permissions, we
  recommend changing the permissions by running "chmod o-rwx" or at the
  very least "chmod o-w".
| Please be careful with find and rm commands that work recursively. If
  in a find command please do a dry run first to see what actually
  happens. If a recursive rm command either use the "-i" option or
  double check your syntax (especially with wild cards). Prefixing the
  path with a . also can help but even that is not fool proof.

**PLEASE NOTE:** data stored under project spaces (see above) is **NOT**
backed up and **cannot** be recovered!

::

   [First.Last@fe1 ~]$ ls -l
   total 68540
   drwxrwxrwx  2 First.Last group      4096 Aug 21 21:16 test-directory
   -rwxr-xr-x  1 First.Last group  69873964 Apr  1 14:31 script.sh
   drwxrwxr-x  3 First.Last group      4096 Oct 11  2018 directory

   [First.Last@fe1 ~]$ chmod o-rwx test-directory
   [First.Last@fe1 ~]$ ls -l
   total 68540
   drwxrwx---  2 First.Last group      4096 Aug 21 21:16 test-directory
   -rwxr-xr-x  1 First.Last group  69873964 Apr  1 14:31 script.sh
   drwxrwxr-x  3 First.Last group      4096 Oct 11  2018 directory

.. _root_level_data_changes:

Root Level Data Changes
-----------------------

Any root level data changes to projects (deletion of files, permissions,
ownership, etc.) must be approved by the project PI. Please open a help
ticket to the corresponding RDHPCS system with the following
information:

#. The full path of the directory/files that need to be deleted
#. A brief explanation of why the user is unable to delete the
   directories/files in question
#. Approval from the project PI that it is OK to delete the said
   directories/files

\ **Please note that deleting data from projects (scratch(HPFS) and
tape) is permanent - once deleted can never be restored.**\ 

.. _protecting_restricted_data:

Protecting Restricted Data
==========================

This describes how to protect the RSTPROD restricted data on Hera. Hera
uses regular Linux group based protection for restricted data.

It is up to the user to make sure that files containing restricted data
are set to have the group as "rstprod" and also to make sure that
permissions for the world are removed.

::

   # chgrp -R rstprod $DIR
   # chmod -R rwx-go $DIR

Where $DIR is the directory with the files you want to protect.

When these files are copied to a different location, please be sure to
use the "-p" option on the "cp" command to preserve the group and the
protection for those files:

::

   # cp -rp $DIR $TARGET_DIR

.. _managing_packages_in_contrib:

Managing Packages in /contrib
=============================

.. _overview_of_contrib_packages:

Overview of Contrib Packages
----------------------------

The system staff do not have the resources to maintain every piece of
software requested. There are also cases where developers of the
software are the system users, and putting a layer in between them and
the rest of the system users is inefficient. To support these needs, we
have developed a /contrib package process. A /contrib package is one
that is maintained by a user on the system. The system staff are not
responsible for the use or maintenance of these packages.

.. _responsibilities_of_a_contrib_package_maintainer:

Responsibilities of a Contrib Package Maintainer
------------------------------------------------

Maintainers are expected to:

-  Follow the naming conventions and guidelines outlined in this
   document
-  Apply security updates as quickly as possible after they become
   availble
-  Update software for bug fixes and functionality as users request
-  Respond to user email requests for help using the software

.. _contrib_packages_guidelines:

Contrib Packages Guidelines
---------------------------

-  The package should be a single program or toolset.

   -  We want to prevent having a single directory being a repository
      for many different packages.

-  If you support multiple functions, please request multiple packages.
-  The package may have build dependencies on other packages, but it
   must otherwise be self-contained.
-  The package may not contain links to files in user or project
   directories.
-  We expect each package to be less than 100MB.
-  If you need more, please tell us when you request your package.
-  We can support larger packages but we need to monitor the space used.
-  We expect each package to have less than 100 files.

.. _contrib_package_maintainer_requests:

Contrib Package Maintainer Requests
-----------------------------------

If you wish to maintain a package in contrib, please send a request to
the Help System with:

-  List of the packages you wish to maintain.
-  Justification why each is needed.
-  The user who will be maintaining the package.

   -  In certain cases, multiple users can manage a package, and unix
      group write permissions may be granted for the directory. In that
      case, specify the unix group that will be maintaining the package.

.. _managing_a_contrib_package:

Managing a Contrib Package
--------------------------

After your request has been approved to use space in the /contrib
directory, two directories will be created for you:

::

   /contrib/$MYDIR
   /contrib/$MYDIR/modulefiles

This is where you will install your software for this package and
optionally install a module to allow users to load the environmental
settings necessary to use this package. The variable $MYDIR is the name
of the /contrib package you requested. The directory convention of
/contrib is designed to match that of /apps. Thus, one piece of software
goes into a subdirectory under the /contrib level. If you want to manage
multiple package, please request multiple /contrib package. You can do
this all at one time when submitting your request to the `Help
System <help_system>`__.

.. _contrib_package_directory_naming_conventions:

Contrib Package Directory Naming Conventions
--------------------------------------------

When installing software into your /contrib directory, first determine
if this is software that should be versioned (multiple versions may
exist at one time) or unversioned (there will only ever be one version
installed, and upgrade will overwrite the existing software). For
verisoned software, please install it into a subdirectory of your
package that is named after the version number. For supporting multiple
versions of software the install path should be:

::

    /contrib/$MYDIR/$VER

Where $MYDIR is the directory assigned to you and $VER is the version
number. Thus if your package is named ferret and you are installing the
version 3.2.6, the software should be installed in:

::

    /contrib/ferret/3.2.6

For supporting un-versioned software, only install the software directly
into your package directory:

::

    /contrib/$MYDIR/

.. _providing_modules_to_access_contrib_installed_software:

Providing Modules to Access Contrib Installed Software
------------------------------------------------------

For each contrib package, a corresponding directory will be created for
modules. The base directory name is "/contrib/modulefiles.” Each package
will have a subdirectory created named after the package. For example,
for the ferret package, there will also be a directory created named:

::

   /contrib/ferret/modulefiles

In order for users to know what contrib software is available and who
the "Point of Contact" is, users should do a listing of the /contrib
directory:

``   ls -l /contrib``

Once they which software in cotrib they need to use, then can add that
package to their module path and then load the module. For example,
"sutil" is a contrib package, and in order to use it, users would do the
following:

| ``    module use -a /contrib/sutils/modulefiles``
| ``    module load sutils``

.. _creating_modules_for_contrib_packages:

Creating Modules for Contrib Packages
-------------------------------------

There are example modules found here:

::

   /contrib/modulefiles.example/ferret

Please use those as a template. Contrib package maintainers must follow
these conventions:

-  Modules must display the notice when loaded providing contact
   information on how to get help.
-  Module naming convention should be based on the version number of the
   software.
-  Please ask questions through the Help Desk regarding how to
   construction modules.
