.. _ppan-user-guide:

###############
PPAN User Guide
###############

.. image:: /images/PPAN.png
   :scale: 75%


Post Processing and Analysis (PPAN) is a small cluster comprised of
over 130 Dell servers located at GFDL in Princeton, NJ. These systems
have multiple petabytes of disk storage and access to nearly 200
petabytes of archive storage. Combined with various generations of
Intel processors, from Sandy Bridge to Ice Lake, each has
specifications that range from 48-512GB of memory and are designed to
provide a system that can meet most user demands.

PPAN supports GFDL's science community by providing a place to further analyze
and interpret models generated on other HPC systems. This gives users a local
system to experiment and evaluate with various degrees of control and
validation of complex processes and tasks. PPAN is also a host to various
software packages including MATLAB and other complex combinations of Python & R
libraries.

The GFDL Post-processing and Analysis Cluster is called Pan. For interactive
use, it contains approximately 20 analysis hosts with names like an001, an101,
and an200.
The analysis hosts feature a high-performance (CXFS) interface to the big-data
filesystems ``/archive`` and ``/work``. A variety of data analysis software
packages is available via the environment modules system.

For batch use, Pan contains about 100 post-processing hosts with names like
pp006 and pp317. The Slurm batch scheduler permits models running on Gaea to
submit post-processing jobs to the GFDL cluster.

This diagram represents the PPAN Data Network.

.. image:: /images/PPANdiag.png
   :scale: 60%

Login to Analysis
=================

:ref:`Log into analysis using ssh <ssh_access>`, authenticate with either a
CAC or an RSA fob.

ssh setup for GFDL Workstations
-------------------------------

From the GFDL workstations, to setup ``ssh`` to allow additional analysis
logins without further authentication, existing users should run the
commands below to update the configuration files.  New users should not need
to run these commands.

.. code-block:: shell

   gfdl> setup-RSA
   gfdl> setup-CAC

To login with an RSA fob, type

.. code-block:: shell

   gfdl> ssh analysis

and enter your RSA PIN plus the 6 digits showing on the fob.

To login with a CAC, type

.. code-block:: shell

   gfdl> sshg3 analysis

and enter the PIN for your CAC.

The bastion host displays a menu of analysis hosts, showing the CPU cores,
memory, and /vftmp fast-scratch filesystem size on each host. To login to a
specific host, hit control-C and enter the host name.

C-shell Setup
-------------

In your ~/.cshrc and ~/.login, use the C-shell "if" statements below to
separate settings for analysis logins from settings for your workstation:

.. code-block:: shell

   if ( `gfdl_platform` == hpcs-csc ) then
      # settings for analysis logins
   endif
   if ( `gfdl_platform` == desktop ) then
      # settings for workstations
   endif


C-shell keybinds for analysis
-----------------------------

If you use a C-shell (csh or tcsh) you may find that your key bindings on
analysis are broken. e.g., the delete key produces a '~' instead of deleting a
character. To fix this, create a ~/.bindings file with the following
contents (mirroring the contents present in /etc/inputrc on the analysis nodes,
but converting them for csh.) Add a line to your `~/.cshrc` file under the
hpss-csc section from the C-shell Setup guidance above telling it to source
~/.bindings

.. code-block:: shell

   ## for linux console and RH/Debian xterm
   bindkey '^[[1~' beginning-of-line
   bindkey '^[[4~' end-of-line
   bindkey '^[[5~' history-search-backward
   bindkey '^[[6~' history-search-forward
   bindkey '^[[3~' delete-char
   bindkey '^[[2~' quoted-insert
   bindkey '^[[5C' forward-word
   bindkey '^[[5D' backward-word
   bindkey '^[[1;5C' forward-word
   bindkey '^[[1;5D' backward-word
   # for rxvt
   bindkey '^[[8~' end-of-line
   bindkey '^[Oc' forward-word
   bindkey '^[Od' backward-word
   # for non RH/Debian xterm, can't hurt for RH/DEbian xterm
   bindkey '^[OH' beginning-of-line
   bindkey '^[OF' end-of-line
   # for freebsd console
   bindkey '^[[H' beginning-of-line
   bindkey '^[[F' end-of-line


xterm and  gnome-terminal
-------------------------

After login to the analysis cluster, you may invoke:

.. code-block:: shell

   xterm &
   gnome-terminal &

These child sessions inherit the parent's scratch directory ($TMPDIR). By
default, gnome-terminal does not read your .login file.

Logging into the PP nodes
-------------------------

Sometimes, for debugging or other purposes, it can be useful to log into the pp
nodes and run diagnostics / check on system resources. To do so, ssh in from
any of the analysis nodes (workstations don't work):

.. code-block:: shell

  >ssh ${pp_nodename}

where ${pp_nodename} is one of the pp nodes (i.e. pp212, pp301). The same
method will work from analysis (not from the workstations) to log into an
analysis node; simply swap out ${pp_nodename} for ${analysis_nodename}

File Systems
============

In each GFDL filesystem, you have your own directory to work in. Two names
point to this directory: your username (First.Last) and your "userdir"
(initials).

For example, user First.Last may access his home directory as either:

.. code-block:: shell

   /home/First.Last
   /home/fal

The short "userdir" name is a convenient shorthand for the longer username
(First.Last).

/home and /nbhome
-----------------

The GFDL workstations and the analysis cluster use a unified home directory.
/home is backed up daily. New users are given a /home disk space quota of 10
GB.

There is also a supplemental home directory called "/nbhome" (no-backup /home).
/nbhome is backed up weekly (not daily). New users are given an /nbhome disk
space quota of 10 GB.

To see your /home and /nbhome quota and usage, run the local `homeuse`` command
instead of the usual `quota -vs`. You can run the command on a GFDL workstation
or the analysis cluster. The disk usage amounts it shows are updated hourly:

.. code-block:: shell

   linux> homeuse
   /home & /nbhome usage - Jul 22 14:01

   GROUP USERNAME                     FILESYS     FILES        GB  QUOTA  USE%
   s     Joe.Scientist               -  /home       80270      6.27     10   63%
   s     Joe.Scientist               -  /nbhome    110080      4.91     10   49%


The `homerpt` command shows group reports of /home or /nbhome usage.
You can run the command on a GFDL workstation or the analysis cluster. Run it with no
options to see the usage message:

.. code-block:: shell

   homerpt

/archive
--------

/archive is the GFDL tape archive filesystem. It behaves like any other
filesystem, except that file data is on tape storage until recalled to disk.
/archive is mounted read/write on the analysis cluster, but read-only on GFDL
workstations.

Files will be recalled from tape automatically when they are opened. But if
many files are needed, it is best to use the commands below to recall files
from tape. These commands are available on the analysis cluster and GFDL
workstations. "dm" stands for "Data Migration".

.. code-block:: shell

   dmget   <files>   # recall files from tape
   dmwho             # show pending dmgets with wait times
   dmls -l <files>   # show file state (disk/tape residence)

See the dmgt man page for more details.

Files should be copied from /archive to the /vftmp fast-scratch filesystem
before use. The GFDL director allocates tape storage to each GFDL group. A
group leader may also set allocations for individuals in the group. These
allocations, and the percent used, are shown by the local `archrpt` command:

.. code-block:: shell

   archrpt -s
   archrpt -r <group>

These allocations are enforced administratively. For details, see
:ref:`about_archrpt`.


/archive is intended for large files only. To save small files, combine related
files into a single tar or cpio file, and store this larger file in /archive.

A "locate" database for /archive, updated daily, is now available. To search
all of your /archive pathnames for a pattern, run

.. code-block:: shell

 dmlocate pattern

on the analysis cluster or a GFDL workstation. See `man dmlocate`
for more details.

/vftmp & $TMPDIR
----------------

/vftmp is a fast-scratch filesystem local to every analysis and post-processing
host.

On analysis hosts, /vftmp varies in size from 8 TB to 37 TB, as shown on the
login menu. On most post-processing hosts, /vftmp is 8 TB. There are a few
"bigvftmp" hosts with 27 TB or 44 TB of /vftmp.

The environment variable $TMPDIR points to a fast-scratch directory unique to
each batch job or interactive session. $TMPDIR is removed when the job or
session ends. Currently $TMPDIR is:

.. code-block:: shell

   /vftmp/<First.Last>/pbs<pbs_jobid>  ...in batch jobs
   /vftmp/<First.Last>/pid<shell_pid>  ...in interactive sessions.

On analysis hosts, you may use /vftmp/<First.Last> for long-term scratch files.
These files are not backed up. They are not automatically wiped, but may be
removed by an administrator if /vftmp fills. To return to the same analysis
host at a later login, hit control-C at the login menu, then enter the host
name.

As much as possible, interactive work should be done in $TMPDIR or
/vftmp/<First.Last>.

/work
-----

/work is a large long-term scratch filesystem available with read/write access
on the analysis cluster. /work is not backed up, and is mounted read-only by
the GFDL workstations.

To see your current usage of /work, run the local command:

.. code-block:: shell

   quotause


/ptmp
-----

The /ptmp filesystems are used to stage data for FRE post-processing. /ptmp is
not backed up and is mounted read-only by the GFDL workstations.

/net, /net2, /net3
------------------

/net, /net2, and /net3 are GFDL workstation filesystems of 100 GB or more. /net
is backed up, but /net2 and /net3 are not. /net, /net2, and /net3 are mounted
read/write on the workstations, and read-only on the analysis hosts.

In an analysis login session, use gcp to transfer files to/from the /net,
/net2, or /net3 filesystems. For example:

.. code-block:: shell

   module load gcp
   gcp /archive/USER/testfile gfdl:/net2/USER/testfile
   gcp gfdl:/net2/USER/testfile /archive/USER/testfile

/net, /net2, and /net3 are not mounted on the post-processing nodes, but they
can be accessed via gcp.

Batch Software
==============

The NOAA/RDHPCS systems in Princeton, Boulder, and Fairmont, and the DOE Gaea
system, use the Slurm batch system.

Slurm is an open-source batch system developed by DOE since 2003. It is now in
wide use at DOE and other supercomputer sites. Slurm now includes backfill
scheduling and accounting. Commercial support is available from SchedMD LLC.
Slurm replaces the Moab batch system used since 2010. Tables below show
corresponding Slurm and Moab commands and options.

Access
------

Slurm can be used from any PP/AN analysis host. Logins to analysis
automatically do "module load slurm".


Local Commands
--------------

Easy-to-use local job display scripts are available on PP/AN. The '-h' or
'--help option will display the usage messages below:

.. sourcecode::

   qa|qi|qr|qc [options..]
      -u           show my jobs
      -u user      show user's jobs
      -j n         jobname length  (default=14)
      -n n         username length (default=14)
      -s           sort by node (qr) or time (qc)

      qa          show all jobs
      qi          show input queue
      qr          show running jobs
      qc          show completed & failed jobs

   qj jobid       show job details
   qn an|pp       show Slurm batch nodes

Using these scripts, it's easy to show long jobnames. For example:

.. code-block:: shell

   an200> qr -j40

shows all running jobs, with 40 characters of each jobname.

Gotchas
-------

#. If -o is a directory, the job submission succeeds, the job is scheduled, and
immediately fails with reason NonZeroExitCode.

3. If -D dir is not specified, the job's working directory is the submission
directory. If this directory does not exist on the execution host, Slurm does
"cd /tmp" and runs the job.

#. Slurm redirects standard output and standard error to the logfile pointed to
   in the header only after a line is finished executing. If you need a
   heartbeat to monitor script progress, consider using another meachanism.

#. If slurm scripts do not end with a POSIX-standard new line character, the
   last line of the script will not execute. Please note that this is not an
   issue if you are editing your script; this is a possible issue if you
   auto-generate code  for batch submission outside of FRE. (`Reference
   <https://thoughtbot.com/blog/no-newline-at-end-of-file>`_


Analysis Software
=================

To access most analysis software, you must use the "module" command, described
below. Only matlab, idl, and mathematica are accessible without loading a
module.

Most GFDL software on PP/AN (and workstations) is managed by Spack, which
facilitates easier, automated, and more frequent software updates. The `GFDL
Spack-managed software environment wiki
<https://wiki.gfdl.noaa.gov/index.php/Spack-managed_software_environment>`_
provides more information.

To request installation of a new analysis software package, open a help desk
ticket. Send email to oar.gfdl.help@noaa.gov, with Software Installation in the
subject line.

Using Modules
-------------

The "module" command allows you to select a version of a software package to
use. After doing "module load <package>", the executables and man pages for
<package> will be available.

To see the available software packages, run:

.. code-block:: shell

 module avail

To load the default release of a software package, pyferret for example, run:

.. code-block:: shell

 module load pyferret

To load a specific release of a software package, pyferret 7.4 for example,
run:

.. code-block:: shell

 module load pyferret/7.4

To show the currently loaded modules, run:

.. code-block:: shell

 module list

To remove all currently loaded modules, run:

.. code-block:: shell

 module purge

For more information on modules, run "module help" or "man module".

netcdf Library
--------------

We are now using netcdf-c:

.. code-block:: shell

   module load netcdf-c
   IDL Multi-threading

IDL is available without using modules.

By default, IDL runs multi-threaded using a number of threads equal to the
number of cores on the host. Especially for batch jobs, it is better to set a
smaller number of threads, which won't vary between hosts. To set IDL to use 4
threads:

.. code-block:: shell


   setenv IDL_CPU_TPOOL_NTHREADS 4
   NAG Library

The mark 22 release of the NAG SMP Library is installed on the GFDL analysis
cluster hosts an001 and an002. For details, see the Nag page of the GFDL wiki.

MATLAB Licenses
---------------

To see the current usage of MATLAB licenses, run "lmgfdl" in an analysis
cluster or workstation window:


.. _about_archrpt:

*************
About Archrpt
*************

| Archprt displays detailed information about archive data usage for
  user and group.

::

   Usage:
           archrpt -r|-s [view] [sort] [date]

           -r show full report
                [view]    group|user
                [sort]    bytes|files
                [date]    YYMMDD
           -s show group summary
                [sort]    bytes|files
                [date]    YYMMDD

   Options:
       -r, --report
               Show full report.

               view|sort|date optins can be used.

       -s, --summary
               Show group summary.

               sort|date options can be used.

       -h, --help
               Display usage.

       -m, --man
               Display man page.

.. _report_option__r:

Report Option [-r]
------------------

The report option will output both user and group quota info.

Options:

::

   [view]    group|user
   [sort]    bytes|files
   [date]    YYMMDD

.. _show_archive_report_by_specified_group_view:

Show Archive Report By Specified Group [view]
---------------------------------------------

Command:

::

   archrpt -r o

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   x1e          Joeseph.User        o      212,756        3.32T     4.00T/  83.1
   z3j          Joe.Scientist       o      192,901       44.62T    45.00T/  99.2
   ......

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_user_view:

Show Archive Report By Specified User [view]
--------------------------------------------

Command:

::

   archrpt -r r7j

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   r7j          Rob.Scientist      j       145,105      134.11T   140.00T/  95.8

.. _show_archive_report_by_specified_group_and_sort_by_files_view_sort:

Show Archive Report By Specified Group and Sort By Files [view] [sort]
----------------------------------------------------------------------

Command:

::

   archrpt -r o files

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   x1e          Joeseph.User        o      212,756        3.32T     4.00T/  83.1
   z3j          Joe.Scientist       o      192,901       44.62T    45.00T/  99.2
   ...

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_group_and_sort_by_bytes_view_sort:

Show Archive Report By Specified Group and Sort By Bytes [view] [sort]
----------------------------------------------------------------------

Command:

::

   archrpt -r o bytes

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   x1e          Joeseph.User        o      212,756        3.32T     4.00T/  83.1
   z3j          Joe.Scientist       o      192,901       44.62T    45.00T/  99.2
   ...

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_date_date:

Show Archive Report By Specified Date [date]
--------------------------------------------

Date format: YYMMDD

Command:

::

   archrpt -r 120119

The commands above can also be used with the date option.

| Show Archive Report By Specified Group:
| Command:

::

   archrpt -r j 120119

|
| Show Archive Report By Specified User:
| Command:

::

   archrpt -r r7j 120119

|
| Show Archive Report By Specified Group and Sort By Files:
| Command:

::

   archrpt -r j files 120119

|
| Show Archive Report By Specified Group and Sort By Bytes:
| Command:

::

   archrpt -r j bytes 120119

.. _summary_option__s:

Summary Option [-s]
===================

The summary option will output group quota info.

Options:

::

   [sort]    bytes|files
   [date]    YYMMDD

.. _show_archive_summary:

Show Archive Summary
--------------------

Command:

::

   archrpt -s

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                          230,642            112.04T          500.00T/  22.4
   ...
   Totals                 130,026,459          28616.42T

.. _show_archive_summary_and_sort_by_files_sort:

Show Archive Summary and Sort By Files [sort]
---------------------------------------------

Command:

::

   archrpt -s files

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                       41,228,072           8181.26T        10712.40T/  87.8
   ....

   Totals                 130,026,459          28616.42T

.. _show_archive_summary_and_sort_by_bytes_sort:

Show Archive Summary and Sort By Bytes [sort]
---------------------------------------------

Command:

::

   archrpt -s bytes

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                       41,228,072           8181.26T        10712.40T/  87.8
   ...

   Totals                 130,026,459          28616.42T

.. _show_archive_summary_by_date_date:

Show Archive Summary By Date [date]
-----------------------------------

Date format: YYMMDD

Command:

::

   archrpt -s 120119

Output:

::

   Report for date: 120119
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   j                          230,640            112.03T          500.00T/  22.4
   ...
   Totals            130,895,617        28627.62T

The commands above can also be used with the date option.

| Show Archive Summary and Sort By Files:
| Command:

::

   archrpt -s files 120119

| Show Archive Summary and Sort By Bytes:
| Command:

::

   archrpt -s bytes 120119

.. _group_quotas:

Group Quotas
============

Group quotas are provided by the front office.

.. _user_quotas:

User Quotas
===========

Info
----

User quotas have been added to archrpt. These quotas are defined by
the group head and are either a percentage of the group quota or an
absolute size.

Example:

::

   Report for date: 120126
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   x1e          Joeseph.User        o      212,756        3.32T     4.00T/  83.1
   z3j          Joe.Scientist       o      192,901       44.62T    45.00T/  99.2
   ...

Configuration
-------------

User quotas are authorized by the group head and defined in a text
file. Group heads may choose any path name for the file, but once
selected please inform Garrett Power and/or Ed Weiss so that it can be
linked into archrpt. This file is owned by the group head or his
designee, and only the owner should have write access to the file.
Once linked to the archrpt configuration directory, the quota file
owner can adjust users' quotas by editing this file. The format of the
user quota file is as follows:

filename: **x.quota**

::

   js  John.Smith  500G
   jd  Jane Doe    2%

In the file, each line is a defined user with the **first column being
the user's initials**, **second column user's First.Last name**, and
**third column the user's quota size**. Each column should be
separated with **tab spacing**. If a user in the group is omitted,
that user has no individual quota limit, but is still restricted by
the group quota.

::

   js       = user's user initials.
   John.Smith  = user's First.Last name.
   10%     = quota size the user should be allocated of the group quota.
             The quota can be either a percentage or a size of the quota.
             The size can be in the form of Percentage, Gigabytes, Terabytes, or Petabytes.
             10% = 10 percent of the group quota
             500G = 500 Gigabytes
             1T = 1 Terabyte
             1P = 1 Petabyte

Again, this file can be created at any path name in the owner's home
directory. It should be **write only** by the owner and **readable by
everyone** (e.g. **chmod 644**). Then to activate the file and make it
available to archrpt, please provide its path name to Garrett Power
and/or Ed Weiss so it can be linked to the archrpt configuration
directory.

.. _enforcing_quotas:

Enforcing Quotas
================

Group and User quotas are enforced by another script that will check
to see if users are over their quotas. If a group is over its quota,
each user in that group will receive an email stating the group is
over its quota limit. If an individual user is over quota, a warning
email is sent to just that user.


