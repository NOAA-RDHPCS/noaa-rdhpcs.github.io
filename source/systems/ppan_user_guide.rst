.. _ppan-user-guide:

###############
PPAN User Guide
###############

.. image:: /images/PPAN.png
   :scale: 75%


Post Processing and Analysis (PPAN) is a small cluster comprised of
over 130 Dell servers located at the Geophysical Fluid Dynamics Laboratory
(GFDL) in Princeton, NJ. These systems
offer multiple petabytes of disk storage and access to nearly 200
petabytes of archive storage. Various generations of
Intel processors from Sandy Bridge to Ice Lake, and available
ranges from 48-512 GB of memory, are sufficient for most user
post-processing demands. See :ref:`analysis-hosts` and
:ref:`postprocess-hosts` for specifics.

PPAN supports GFDL's science community by providing a place to analyze
and interpret models generated on other HPC systems. This gives users a local
system to experiment and evaluate with various degrees of control and
validation of complex processes and tasks. PPAN is also a host to various
software packages, including MATLAB and other complex combinations of
Python and R libraries.

The GFDL Post-processing and Analysis Cluster is called Pan, or PPAN. It
contains approximately 20 analysis hosts for interactive use. The analysis
hosts feature a high-performance (CXFS) interface to the big-data filesystems
``/archive`` and ``/work``. A variety of data analysis software packages is
available via the environment modules system.

For batch use, Pan contains about 100 post-processing hosts with names like
pp006 and pp317. The Slurm batch scheduler permits models running on Gaea to
submit post-processing jobs to the GFDL cluster.

This diagram represents the PPAN Data Network.

.. image:: /images/PPANdiag.png
   :scale: 60%

Login to Analysis
=================

:ref:`Log into analysis using ssh <ssh_access>`, and authenticate with either a
CAC or a YubiKey.

ssh setup for GFDL Workstations
-------------------------------

From the GFDL workstations, you can set up ``ssh`` to allow additional
analysis logins without further authentication. Existing users
configuring CAC access should run the
command below to update the configuration files. New users, and those
authenticating with YubiKey, should not need to do so.

.. code-block:: shell

      gfdl> setup-CAC

To login with a YubiKey, type

.. code-block:: shell

   gfdl> ssh analysis

and enter your YubiKey PIN, then press and hold the YubiKey.

.. Note::

   If you intend to authenticate to PPAN with a YubiKey, you must register
   your YubiKey for RDHPCS use. This is separate from YubiKey GFDL access. See
   :ref:configure_yubikey for details.

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
analysis are broken. For instance, the delete key produces a '~' instead
of deleting a character. To fix this, create a ~/.bindings file with the
following contents (mirroring the contents present in /etc/inputrc on
the analysis nodes, but converting them for csh.) Add a line to your
`~/.cshrc` file under the hpss-csc section from the C-shell Setup guidance
above telling it to source ~/.bindings

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
nodes and run diagnostics or check on system resources.
Provided that your ssh keys
are configured correctly, you can ssh in from any of the analysis nodes as
follows:


.. code-block:: shell

  >ssh ${pp_nodename}

where ${pp_nodename} is one of the pp nodes (for example, pp212, pp301). The
same method will work from analysis to log into an analysis node; simply swap
out ${pp_nodename} for ${analysis_nodename}

.. note::

   This method will not work from a workstation.

File Systems
============

In each GFDL filesystem, you have your own directory to work in.
To determine your userdir, use the gfdluser $USER command.

For example, user First.A.Last may access the home directory as either:

.. code-block:: shell

   /home/First.Last
   /home/fal

The short *userdir* name is a convenient shorthand for the longer username
(First.Last).

/home and /nbhome
-----------------

The GFDL workstations and the analysis cluster use a unified home directory.
/home is backed up daily. New users are given a /home disk space quota of 10
GB.

There is also a supplemental home directory called */nbhome* (no-backup /home).
/nbhome is backed up weekly, not daily. New users are given an /nbhome disk
space quota of 10 GB.

To see your /home and /nbhome quota and usage, run the local `homeuse`` command
instead of the usual `quota -vs`. You can run the command on a GFDL workstation
or the analysis cluster. The disk usage amounts it shows are updated hourly:

.. code-block:: shell

   linux> homeuse
   /home & /nbhome usage - Jul 22 14:01

   GROUP USERNAME                     FILESYS     FILES        GB  QUOTA  USE%
   s     First.Last                  -  /home       80270      6.27     10   63%
   s     First.Last                  -  /nbhome    110080      4.91     10   49%


The ``homerpt`` command shows group reports of /home or /nbhome usage.
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

Files will be recalled from tape automatically when they are opened. If
many files are needed, it is best to use the commands below to recall files
from tape. These commands are available on the analysis cluster and GFDL
workstations. *dm* stands for *Data Migration*.

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

As far as possible, interactive work should be done in $TMPDIR or
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

/net, /net2, and /net3 are not mounted on the post-processing nodes, but
can be accessed via gcp.

Batch Software
==============

The DOE Gaea system, and NOAA/RDHPCS systems in Princeton, Boulder, and
Fairmont, use the Slurm batch system.

Slurm is an open-source batch system developed by DOE since 2003. It is now in
wide use at DOE and other supercomputer sites. Slurm now includes backfill
scheduling and accounting. Commercial support is available from SchedMD LLC.

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
      qc          show completed and failed jobs

   qj jobid       show job details
   qn an|pp       show Slurm batch nodes

Using these scripts, it's easy to show long jobnames. For example:

.. code-block:: shell

   an200> qr -j40

shows all running jobs, with 40 characters of each jobname.

Gotchas
-------

* If -o is a directory, the job submission succeeds, the job is scheduled, and
  immediately fails with reason NonZeroExitCode.

* If -D dir is not specified, the job's working directory is the submission
  directory. If this directory does not exist on the execution host, Slurm does
  ``cd /tmp`` and runs the job.


  * Slurm redirects standard output and standard error to the logfile
    pointed to in the header only after a line is finished executing.
    If you need a heartbeat to monitor script progress, consider using
    another mechanism.


  * If slurm scripts do not end with a POSIX-standard new line character, the
    last line of the script will not execute. Please note that this is not an
    issue if you are editing your script; this is a possible issue if you
    auto-generate code  for batch submission outside of FRE. (`Reference
    <https://thoughtbot.com/blog/no-newline-at-end-of-file>`_

Podman
======

Podman is an open-source utility that can be used on Gaea or PPAN to create and
manage containers. For more information, see the
`Podman documentation <https://podman.io/docs>`__.

.. note::

    Before you can use Podman on Gaea or PPAN, you will need to request
    Podman access through the :ref:`Help System <getting_help>`
    Send an email to oar.gfdl.help@noaa.gov, and specify Podman access
    in the subject line.


Analysis Software
=================

To access most analysis software, you must use the ``module`` command,
described below. (Note that matlab, idl, and mathematica are accessible
without loading a module.)

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

The ``module`` command allows you to select a version of a software package to
use. After doing ``module load <package>``, the executables and man pages for
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

By default, IDL runs multi-threaded, using a number of threads equal to the
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

To see the current usage of MATLAB licenses, run ``lmgfdl`` in an analysis
cluster or workstation window:

.. code-block:: shell

   an001> lmgfdl

.. _about_archrpt:


About Archrpt
=============

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

   Report for date: 120126
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   x1e          Joseph.User        o      212,756        3.32T     4.00T/  83.1
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

   Report for date: 120126
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   r7j          Mad.Scientist      j       145,105      134.11T   140.00T/  95.8

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
   x1e          Joseph.User        o      212,756        3.32T     4.00T/  83.1
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
   x1e          Joseph.User        o      212,756        3.32T     4.00T/  83.1
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
-------------------

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
   x1e          Joseph.User        o      212,756        3.32T     4.00T/  83.1
   z3j          Joe.Scientist       o      192,901       44.62T    45.00T/  99.2
   ...

Configuration
-------------

User quotas are authorized by the group head and defined in a text
file. Group heads may choose any path name for the file, but once
selected please inform the group head, so that the path can be
linked into archrpt. This file is owned by the group head or their
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
everyone** (**chmod 644**, for instance). Then to activate the file and make it
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


.. _analysis-hosts:


Analysis Hosts
==============


.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Node
     - CPUs
     - GB Total Mem [#f1]_
     - /vftmp (TB)
     - S:C:T (actual) [#f2]_
     - S:C:T (SLURM)
     - Annotations
     - AVX [#f3]_
     - Architecture [#f4]_
   * - an001
     - 12
     - 202
     - 16
     - 2:6:1
     - 4:1:1
     -
     -
     - nehalem
   * - an002
     - 12
     - 202
     - 16
     - 2:6:1
     - 4:1:1
     -
     -
     - nehalem
   * - an005
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an006
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an007
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     - 2x /vftmp speed, scron
     -
     - westmere
   * - an008
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     - 2x /vftmp speed, scron
     -
     - westmere
   * - an009
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an0010
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an011
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an012
     - 8
     - 101
     - 10
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an013
     - 8
     - 202
     - 16
     - 2:4:1
     - 4:1:1
     - Reserved/Engineering test
     -
     - westmere
   * - an014
     - 8
     - 101
     - 16
     - 2:4:1
     - 4:1:1
     -
     -
     - westmere
   * - an101
     - 16
     - 540
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX
     - sandybridge
   * - an102
     - 16
     - 540
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX
     - sandybridge
   * - an104
     - 16
     - 540
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX
     - sandybridge
   * - an105
     - 24
     - 270
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX
     - sandybridge
   * - an106
     - 24
     - 270
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX2
     - sandybridge
   * - an107
     - 16
     - 270
     - 40
     - 2:8:1
     - 4:1:1
     - jhan
     - AVX
     - sandybridge
   * - an108
     - 24
     - 270
     - 40
     - 2:8:1
     - 4:1:1
     -
     - AVX
     - sandybridge
   * - an200
     - 16
     - 540
     - 72
     - 2:8:1
     - 4:1:1
     -
     - AVX2
     - broadwell
   * - an201
     - 16
     - 540
     - 48
     - 2:8:1
     - 4:1:1
     - jhanbigmem
     - AVX512
     - skylake
   * - an202
     - 16
     - 540
     - 48
     - 2:8:1
     - 4:1:1
     -
     - AVX512
     - skylake
   * - an203
     - 16
     - 540
     - 48
     - 2:8:1
     - 4:1:1
     -
     - AVX512
     - skylake
   * - an204
     - 16
     - 540
     - 48
     - 2:8:1
     - 4:1:1
     -
     - AVX512
     - skylake
   * - an205
     - 16
     - 540
     - 48
     - 2:8:1
     - 4:1:1
     -
     - AVX512
     - skylake
   * - an206
     - 24
     - 1080
     - 48
     - 2:12:1
     - 4:1:1
     -
     - AVX512
     - icelake
   * - an207
     - 24
     - 1080
     - 48
     - 2:12:1
     - 4:1:1
     -
     - AVX512
     - icelake
   * - an208
     - 24
     - 4328
     - 48
     - 2:12:1
     - 4:1:1
     - NAG library
     - AVX512
     - icelake
   * - an209
     - 24
     - 4328
     - 48
     - 2:12:1
     - 4:1:1
     -
     - AVX512
     - icelake
   * - an210
     - 24
     - 4328
     - 44
     - 2:12:1
     - 4:1:1
     -
     - AVX512
     - icelake
   * - an211
     - 24
     - 4328
     - 44
     - 2:12:1
     - 4:1:1
     -
     - AVX512
     - icelake


.. _postprocess-hosts:

Post-Processing Hosts
=====================

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Nodes (Range)
     - CPUs/host
     - GB Memory [#f5]_
     - /vftmp (TB)
     - S:C:T (actual)
     - S:C:T (SLURM)
     - Partition
     - AVX Instructions
   * - pp[008-010]
     - 16
     - 203
     - 10
     - 2:8:1
     - 2:8:1
     - workflow
     - yes
   * - pp[013-014]
     - 8
     - 51
     - 10
     - 2:4:1
     - 2:4:1
     - hpetest
     - no
   * - pp[017-026]
     - 8
     - 51
     - 10
     - 2:4:1
     - 2:4:1
     - dask
     - no
   * - pp[027-066,068,072-074]
     - 8
     - 51
     - 10
     - 2:4:1
     - 8:1:1
     - batch/stage
     - no
   * - pp[101,104,105]
     - 8
     - 101
     - 20
     - 2:4:1
     - 8:1:1
     - batch/stage
     - no
   * - pp[200-202]
     - 8
     - 101
     - 48
     - 2:4:1
     - 8:1:1
     - batch/stage
     - no
   * - pp[203-212]
     - 8
     - 203
     - 48
     - 2:4:1
     - 8:1:1
     - batch/stage
     - no
   * - pp[300-309]
     - 16
     - 135
     - 20
     - 2:8:1
     - 8:1:1
     - batch/stage
     - yes
   * - pp310
     - 16
     - 270
     - 36
     - 2:8:1
     - 2:8:1
     - batch/stage
     - yes
   * - pp[311-333]
     - 16
     - 135
     - 20
     - 2:8:1
     - 8:1:1
     - batch/stage
     - yes
   * - pp[334-338]
     - 24
     - 270
     - 24
     - 2:12:1
     - 8:1:1
     - batch/stage
     - yes
   * - pp[339-343]
     - 24
     - 540
     - 24
     - 2:12:1
     - 8:1:1
     - batch/stage
     - yes
   * - pp[400-401]
     - 24
     - 540
     - 24
     - 2:12:1
     - 8:1:1
     - gpu
     - yes


.. Note::

   .. rubric:: Footnotes

   .. [#f1] Units expressed in base-10 multiple-byte as recommended by the
      International Standard IEC 80000-13 Quantities and Units – Part 13:
      Information Science and Technology, International Electrotechnical
      Commission (2008).

   .. [#f2] **S**: Number of CPU sockets per host, **C**: Number of physical
      cores per socket, **T**: Number of threads per core
      (`Hyper-threading <https://en.wikipedia.org/wiki/Hyper-threading>`_)

   .. [#f3] Advanced Vector eXtension support processor
      (`AVX <https://en.wikipedia.org/wiki/Advanced_Vector_Extensions>`_)

   .. [#f4] Processor architecture denomination.

   .. [#f5] Units expressed in base-10 multiple-byte as recommended by the
      International Standard IEC 80000-13 Quantities and Units – Part 13:
      Information Science and Technology, International Electrotechnical
      Commission (2008).


Using GCP
=========

GCP (general copy) is a convenient tool for copying data between NOAA RDHPCS
sites. It simplifies efficient data transfer between the various NOAA sites and
their filesystems with a syntax similar to the standard unix copy tool, cp or
scp.

Using GCP is simple -- just use a variant of the commands below to perform a
transfer:

.. code-block:: bash

   module load gcp
   gcp -v /path/to/some/source/file /path/to/some/destination/file

.. note::

   The ``-v`` option enables verbose output, including useful information
   for debugging. You can obtain a full list of available options with
   ``gcp --help``.

Smartsites
----------

GCP introduces the *smartsites*, similar to the scp use of hostname, to
indicate the remote site to transfer to or from. This concept enables the
transfer of files from one NOAA system to another. Each NOAA site has its own
smartsite. The currently supported smartsites in GCP are:


+---------+----------------------------------------------------------------+
| GFDL    | Pan and GFDL workstations in Princeton, NJ                     |
+---------+----------------------------------------------------------------+
| data1   | GFDL Data portal in Princeton, NJ                              |
+---------+----------------------------------------------------------------+
| Gaea    | ORNL hosted NCRC/CMRS system in Oak Ridge, TN                  |
+---------+----------------------------------------------------------------+
| Hera    | NESCC system in Fairmont, WV                                   |
+---------+----------------------------------------------------------------+

To transfer data from one site to another, simply prepend the smartsite and a
colon to your file location (for example, ``gaea:/path/to/file``).

This smartsite example pushes data from a source site (GFDL) to a remote site
(Gaea).

.. note::

   We are not required to use a smartsite for the local site where
   we currently operate (but it is not an error to include it).

The following commands are equivalent:

.. code-block:: bash

   gcp -v /path/to/some/file gaea:/path/to/remote/destination
   gcp -v gfdl:/path/to/some/file gaea:/path/to/remote/destination

.. note::

   It can be very inefficient to move a file from /archive. It's better to
   transfer to /ptmp first. You don't have to specify the smartsite in the
   destination file path, as gcp can pull data from a remote site as well as
   pushing it:

   ``gcp -v gaea:/path/to/a/file /path/to/a/local/destination``

Log Session ID
--------------

GCP includes a comprehensive logging system. Each transfer is recorded and is
easily searchable if debugging is needed. Each transfer has a
unique log session id, visible if the -v option is used. It is highly
recommended that this option always be enabled in your transfers. A sample of
the expected output is below:

.. code-block:: console

     gcp -v /path/to/source/file /path/to/destination
     gcp 2.0.246 on keo.gfdl.noaa.gov by First.Last at Mon May 13 12:24:07 2023
     Unique log session id is 2c2607db-608f-46a7-a06a-ac576b9494be at 2023-04-13Z16:24


If you experience any problems while using GCP, please re-run your
transfer using the -v option, and provide the session id with your
help desk ticket.

Supported Filesystems
---------------------

GCP can copy data from many filesystems at the HPCS sites, but not all. Below
is a list of supported filesystems for each site. Note that sometimes GCP is
able to support a filesystem from within the local site, but not from external
sites.

GFDL Workstations
^^^^^^^^^^^^^^^^^

.. note::

   You cannot transfer files from a GFDL
   workstation to any remote site. You must use GFDL's PAN cluster to push or pull
   files to a remote site.

.. note::

   You will need a valid Globus proxy certificate
   from PAN (analysis) in your home directory. This is created and/or updated
   for you when you log into PAN. Proxy certificates are valid for 30 days.


Filesystems that GCP supports locally from GFDL workstations:

   ``/net, /net2, /home, /nbhome, /work, /archive``

Filesystems that GCP supports remotely from GFDL workstations, only to data1:

   ``/net, /net2, /home, /nbhome, /work, /archive``

GFDL PAN
^^^^^^^^

Filesystems that GCP supports locally from GFDL's PAN cluster:

   ``/net, /net2, /home, /nbhome, /ptmp, /work, /archive``

Filesystems that GCP supports remotely from other sites:

   ``/home, /ptmp, /work, /archive``


GFDL Data1
^^^^^^^^^^

The GCP **data1:** destination is used to transfer data to the **data1** host
from GFDL WS or GFDL Pan.

Gaea
^^^^

The Gaea site contains multiple node types (eslogin, rdtn,
batch).

Filesystems that GCP supports locally from within Gaea:

   ``/lustre/f1, /ncrc/home``

Filesystems that GCP supports remotely from other sites:

   ``/lustre/f1, /ncrc/home``

Hera
^^^^

Filesystems that GCP supports locally from Hera:

   ``/home, /scratch3, /scratch4``

Filesystems that GCP supports remotely from other sites:

   ``/scratch3, /scratch4``

Helpful Hints
-------------

Creating directories
^^^^^^^^^^^^^^^^^^^^

GCP provides an option for automatically creating new directories:

   ``-cd.``

The final segment of the path is interpreted as a directory if a trailing slash
is included. Otherwise, it will be interpreted as a file. A few examples are
below.

Transferring into new directories:

   ``gcp -cd /path/to/a/file /path/to/a/nonexistent/directory/``

The above creates a file called 'file' in a directory called 'directory':

   ``/path/to/a/nonexistent/directory/file``

Transferring into a file:

   ``gcp -cd /path/to/a/file /path/to/a/nonexistent/directory``

The above creates a file called 'directory' in a directory called
'nonexistent':

   ``/path/to/a/nonexistent/directory``

Recursive transfers
^^^^^^^^^^^^^^^^^^^

GCP provides the ``-r`` option to recursively transfer the contents of
directories.

Synchronize
^^^^^^^^^^^

GCP provides the ``-sync`` option to transfer files to the destination only if
the source is newer. This works for both recursive and non recursive transfers.

Caveats
-------

   * Sources from remote sites cannot include wildcards.
   * GCP does not preserve timestamps or file permissions.

Using the --batch option on Gaea
--------------------------------

Use ``gcp --batch`` for non-blocking transfers.

   * Only available where dtn queues are configured.
   * This is a non-blocking transfer and so is only appropriate when you or the
     script does not need to know explicitly when the transfer started or
     completed.
   * The batch log file is stored in ``$HOME/.gcp_gaea``
   * Needed for transfers initiated on Gaea batch nodes.


.. note::

   Use of ``gcp -d/--debug`` is not recommended. The function of the
   debug option has been superseded by logging that is done for all
   transfers automatically. You can obtain the log session id by using
   the ``-v``/``--verbose`` option. The ``-d`` option produces voluminous
   output and is not recommended.


If you encounter any bugs, confusing documentation, or other issues with GCP,
please open a :ref:`Help ticket. <getting_help>`
