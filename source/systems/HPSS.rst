.. _HPSS:

****************
HPSS
****************

The centralized, long-term data archive system at National
Environmental Security Computing Center (NESCC) is based on
IBM's High Performance Storage System (HPSS). The NESCC HPSS
environment includes 22 petabytes of front-end disk cache,
five Oracle SL8500 enterprise tape libraries, three Spectra
Logic TFinity tape libraries, and 148 tape drives. Total
available capacity is 430 PB. HPSS is accessible from
WCOSS2, Hera, Niagara, Jet, and Gaea.

Users should keep the following things in mind when using
the HPSS system:

-  The HPSS system is well suited for storing large volumes
   of data.
-  Users should avoid transferring many small files (in the
   megabyte range or smaller) to HPSS since the process of
   moving numerous individual small files to and from tape
   is inefficient. Please tar up small files into one large
   tar file before storing data into HPSS, or use HTAR.
-  All data stored in HPSS is single copy. Deleted data
   cannot be recovered.
-  HPSS is not accessible from compute nodes. Access is
   available via Hera/Niagara/Jet front-end nodes (FEs),
   Gaea Data Transfer Nodes (DTN’s), and WCOSS2 transfer
   nodes.
-  Batch jobs that require access to HPSS should be
   submitted to the respective systems service or transfer
   queues.

For questions regarding the HPSS system, email
rdhpcs.hpss.help@noaa.gov.

=======================
Gaining Access to use HPSS
=========================

.. rubric:: New HPSS User Requests

A HPSS user must be a current user of a NOAA HPC compute
resource (RDHPC or WCOSS) to have access to HPSS. Access to
an HPSS project must be requested. When you are a member of
a project on a compute resource you are not automatically
added to the companion HPSS project (if there is one). Being
added to a HPSS project that you are already a member of on
a NOAA compute resource is done without PI or Portfolio
Manager approval, but both are notified that you are being
added. If you are not a member of the project on a NOAA
compute resource then PI or Portfolio manager approval is
required before you will be added. To **expedite** the
process please send an email to: rdhpcs.hpss.help@noaa.gov.
with the following subject line, replacing **USERNAME** and
**PORTFOLIO/PROJECT** with your username and project
request. If PI or Portfolio Manager approval is required,
the email should come from them.

**<$USERNAME>** requests access to HPSS -
**<PORTFOLIO/PROJECT(S)>**

ex: Jane.Doe requests access to HPSS - /BMC/chimera

All requests must have the following information:

-  User Name
-  Requested Project(s) - See `NESCC HPSS Data
   Structure <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Using_the_HSMS_HPSS#NESCC_HPSS_Data_Structure>`__
   for available HPSS projects
-  System HPSS Access is Needed From
   (Hera/Jet/Niagara/Gaea/WCOSS)

.. rubric:: Adding New Projects to HPSS

Projects on a NOAA compute resource are not given access to
the HPSS until requested by the Portfolio Manager (PfM). The
PfM also approves the maximum time retention directory
(pool) that a project is allowed to use on HPSS. All lesser
time pools will also be available. To add a project to the
HPSS the Portfolio Manager should submit a help request with
the following information:

-  Project name
-  associated users
-  maximum time retention pool

To remove a project from the HPSS the PfM should submit a
help request with the project name and data disposition
directions. Requests are reviewed and approved by the HPSS
Resource Manager and sent to the HPSS system administrator
for implementation.

**Requests to add users and projects to HPSS iare NOT
supported in AIM. Instead, the
request/review/implementation/notification process is
handled by the HPSS help ticket system.**  Email: rdhpcs.hpss.help@noaa.gov.

.. rubric:: NESCC HPSS Data Structure

HPSS data at NESCC is organized by portfolio, project and
retention period. Each retention period (1-5 Year &
Permanent) is set up as a separate file family. This means
that all data for a retention period is stored on the same
tapes. Projects live under the appropriate portfolio and
have been assigned access to specific retention directories.
Project users have access to write data to any of their
projects' retention directories. Data within the same
retention directory (/1-5 Year & /Permanent) can be moved to
other projects within the same retention directory. If data
needs to be moved to another retention period (ex: /1year ->
/2year) it must be copied.

.. note::
**Note:** Please be sure to store the data you write to HPSS
in the appropriate retention directory, and in the correct
project if you belong to multiple projects. This will avoid
movement of data once it is stored on tape.

``/$PORTFOLIO/$PROJECT/$RETENTION``

``(ex: /BMC/wrf-chem/2year or /NCEPDEV/emc-meso/5year)``

Portfolios with projects currently storing data in HPSS are
NCEPPROD, NCEPDEV, BMC, HFIP, CPO, NAGAPE, NOS and SYSADMIN

.. table:: /NCEPDEV

   +---------+---------+---------+---------+---------+---------+---------+
   | emc-    | emc     | e       | m       | nesdis- | s       | swpc    |
   | climate | -marine | mc-ohdc | dl-stat | h-sandy | wpc-ipe | -wamgip |
   +---------+---------+---------+---------+---------+---------+---------+
   | emc-da  | e       | e       | md      | nesdi   | sw      | swpc    |
   |         | mc-meso | mc-swpc | l-surge | s-jcsda | pc-para | -wamipe |
   +---------+---------+---------+---------+---------+---------+---------+
   | emc-e   | em      | mdl-dmo | re4cast | sw      | sw      | m       |
   | nsemble | c-naqfc |         |         | pc-sair | pc-wdas | arineda |
   +---------+---------+---------+---------+---------+---------+---------+
   | cpc-om  | emc     | e       | GEFSRR  | mdl-ens | swp     | cpc-op  |
   |         | -global | mc-nems |         |         | c-solar |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | e       | emc-nhc | mdl-obs | nes     | swpc-g  | s       | wpc-    |
   | mc-hwrf |         |         | dis-drt | eospace | wpc-wam | archive |
   +---------+---------+---------+---------+---------+---------+---------+
   | e       | em      | md      |         |         |         |         |
   | mc-land | c-ocean | l-blend |         |         |         |         |
   +---------+---------+---------+---------+---------+---------+---------+

| 

.. table:: /BMC

   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | acb   | cfs   | forms | hmtb  | mef   | ome   | re    | sepp  | ufs   |       |
   |       | strat |       |       |       |       | gclim |       | -phys |       |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | aomip | che   | det   | frd   | hmtr  | nao   | o     | rem   | shout | t     |
   |       | m-var |       |       |       | s-ruc | plapb |       |       | exaqs |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ap-fc | ch    | dlaps | fut   | home  | neaqs | ppef  | ro    | sos   | uas   |
   |       | imera |       | extrm |       |       |       | -osse |       | -osse |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | arop  | c     | dtc   | gacs  | iset  | nesc  | pro   | roc   | stela | winds |
   |       | iaqex |       |       |       | cmgmt | fosse | osmic |       |       |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | arso  | cl    | etlcm | gap   | is    | nevs  | qnh   | rtrr  | st    | wrf   |
   |       | imatt |       | p2005 | idora |       |       |       | ratus | -chem |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | cal   | cmod  | fab   | gmtb  | isp-1 | news2 | qosap | rtvs  | str   | wr    |
   | nexfc |       |       |       |       |       |       |       | mtrck | f-dte |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | cases | co2   | fd    | gom   | je    | nim   | rcc21 | r     | taq   | w     |
   |       |       |       | trans | tmgmt |       |       | ucdev |       | rfhyb |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ccasm | c     | fdr   | gsd   | lpdm  | nre   | rcm1  | ruc   | taq_r | w     |
   |       | omgsi |       | -hpcs |       | lwind |       | lidar | eruns | rfruc |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ccp-m | cs    | fim   | gs    | madis | o     | rcm2  | ru    | tcmi  | w     |
   | ozart | d-wca |       | ienkf |       | dvars |       | csref |       | smcsr |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | cc    | cs    | fi    | gt-md | mcwi  | ol    | reanl |       |       |       |
   | p-wrf | dchem | re-wx |       |       | d-pro |       |       |       |       |
   |       |       |       |       |       | jects |       |       |       |       |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+

| 

.. table:: /HFIP

   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | cl    | dtc   | gnmip | hfi   | hfi   | hfip  | hf    | hur   | h     | Ol    |
   | oudda | -hurr |       | p-fiu | p-mef | -utah | ipprd | -osse | wrfv3 | d-Pro |
   |       |       |       |       |       |       |       |       |       | jects |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | emcda | gp    | hfip  | hfi   | hfip  | hur   | hu    | hybda | renkf | u     |
   |       | shwrf | -gfdl | p-psu | -wisc | -aoml | r-uri |       |       | marwi |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | gf    | g     | hfi   | hf    | hfip- | hur   | hw    | mod   | sso   | wrf   |
   | senkf | sihyb | p-hda | ip-um | wisc2 | -laps | rf-vd | elpsd |       | satda |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | gl    | hfi   |       |       |       |       |       |       |       |       |
   | obpsd | p-ahw |       |       |       |       |       |       |       |       |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+

.. table:: /NAGAPE

   +-------+-------+-------+-------+-------+-------+-------+------+-------+-------+-------+------+
   | aoml- | ci    | cmaq  | enso/ | g     | hpc-  | mmap  | nep/ | o     | r     | seagl | stc/ |
   | osse/ | aqex/ | -so4/ |       | lrcm/ | wof1/ | -emd/ |      | cean- | eef5/ | ider/ |      |
   |       |       |       |       |       |       |       |      | osse/ |       |       |      |
   +-------+-------+-------+-------+-------+-------+-------+------+-------+-------+-------+------+
   | arl/  |       |       |       |       |       |       |      |       |       |       |      |
   +-------+-------+-------+-------+-------+-------+-------+------+-------+-------+-------+------+

| 

.. table:: /CPO

   +-------------+
   | cpo_ngrr_e/ |
   +-------------+

| 

.. table:: /NOS

   ====== ==== =======
   coast/ crs/ nosofs/
   ====== ==== =======

| 

.. table:: /SYSADMIN

   ===== ======== ==========
   cmod/ jetmgmt/ nesccmgmt/
   ===== ======== ==========

.. rubric:: Data Retention

Retention based storage is the HPSS archive policy in
Fairmont, to better manage data growth. Six retention
storage pools (1-5year and Permanent) were created. Each
retention period is setup as a separate file family. This
means all data for a retention period is stored on the same
tapes. All HPSS projects were then configured to write to
one or more of these pools. Data in these pools expires
based upon the retention pool it was written in and would be
deleted upon expiration. All files in the HPSS archive have
been assigned an expiration date based on the file create
time and the retention period it was written to. Upon
expiration files will be deleted from the HPSS archive.

.. rubric:: Expired Data Deletion Process -  User Notification

Users will be notified of expired data via posted lists and
email. These notifications will take place on or before the
first day of the month following the data’s expiration. For
example, data that has an expiration date between October 1
and October 31 2016 will have its notification posted on or
before November 1, 2016. The expired file list is located on
HPSS in /Expired_Data_Lists/expired.YYYY-MM.txt. All HPSS
users have read access to this file and can retrieve it for
review. The file is easily searchable by HPSS username. For
each file included in the expired list the file owner, file
group, filename/path, and expire date are shown. ex: root
system /1year/SYSADMIN/nesccmgmt/test_file-1G-11 Jul-6-2016.
Email notification will also be sent to all users who have
data listed in this file. It is the user’s responsibility to
regularly check the posted list for expired files they own.
Once deleted these files cannot be recovered.

.. rubric:: Expired Data - Deletions

The following table maps out when future deletions will take
place.

================ ================= ===========
Expire Date      Notification Date Delete Date
Dec 1 – Dec 31   January 1         February 1
Jan 1 – Jan 31   February 1        March 1
Feb 1 – Feb 28   March 1           April 1
Mar 1 – Mar 31   April 1           May 1
Apr 1 – Apr 30   May 1 June 1
May 1 – May 31   June 1July 1
Jun 1 – June 30  July 1August 1
Jul 1 – Jul 31   August 1          September 1
Aug 1 – Aug 30   September 1       October 1
Sept 1 – Sept 30 October 1         November 1
Oct 1 – Oct 31   November 1        December 1
Nov 1 – Nov 30   December 1        January 1
================ ================= ===========

.. rubric:: File Size Guidelines

Archiving files to HPSS is a much different process than
writing files to disk storage. Please be aware that the size
of the files you write to HPSS can impact the performance
and efficiency of the system.

**Preferred file size range** File sizes in the gigabyte
range are preferred for storing in HPSS. A few files of
hundreds of gigabytes each make the most efficient use of
the system.

**Considerations for very large files** Transferring files
that are 1 TB or larger increases the risk of poor system
performance as well as the risk (although small) of losing a
file that contains a large amount of data. We recommend
storing files that are 1 TB or smaller.

**Avoid small files** Avoid transferring many small files —
those in the megabyte range or smaller. The process of
moving numerous individual files to and from tape is
inefficient. It can become very time consuming and result in
slowing the system for all users.

When you need to store many small files, use one of these
two approaches:

-  Use
   `[HTAR <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Using_the_HSMS_HPSS#HTAR>`__]
   to transfer them together as a single archive file.
-  Use a tar command on the source system to bundle the
   member files and then transfer the resulting tar file
   with the HSI put or cput command.

Please contact the HPSS helpdesk if you need help
determining appropriate file sizes for your specific
workload.

.. rubric:: Data Recovery Policy

Occasionally an archive tape is damaged or otherwise becomes
partially unreadable. When that happens, the local RDHPCS
staff works with the manufacturer to troubleshoot the
problem and take additional steps to attempt to recover the
missing data. Very rarely, even with these additional
efforts, we are unable to recover the missing files. The
user will then be informed of the files we cannot recover.

In that case, the user has one further option. There are a
number of outside recovery services which will make further
attempts at recovery for a fee. Some charge a flat fee, some
charge more if they are able to recover than if they are
unable to recover. If the user wishes to sign up for such a
service and pay the fee, RDHPCS will handle the logistics of
shipping and other coordination with the recovery service.

.. rubric:: Getting Started on HPSS

HPSS is only accessible from WCOSS, Theia, Jet and Gaea
Remote Data Transfer Nodes (RDTN). Modules have been created
on each system to provide the proper user environment and
tools to access HPSS from these systems. These modules are
not loaded by default and will need to be loaded before you
can use any of the HPSS commands. To add the HPSS tools to
your environment, use the following module command:

**On Hera, Jet, Niagara, and WCOSS**

::

   module load hpss

**On Gaea RDTN's**

::

   module use /sw/rdtn/modulefiles; module load hsi

.. rubric:: HTAR

HTAR has been optimized for creation of archive files
directly in HPSS, without having to go through the
intermediate step of first creating the archive (tar) file
on local disk storage, and then copying the archive file to
HPSS via some processes. In addition, HTAR creates a
separate index file, which contains the names and locations
of all of the member files in the archive (tar) file. The
index file allows individual files and directories in the
archive to be randomly retrieved without having to read
through the archive file.

.. rubric:: Limitations

Please be aware of the following limitations for HTAR:

#. File size: An individual file within the tar file may not
   be larger than 68 GB.
#. Directory paths: The directory path of any file may not
   exceed 154 characters in length.
#. File names: File names may not exceed 99 characters in
   length.

.. rubric:: Usage

The HTAR command line has the general form:

.. code-block::

   htar action{create|extract|list} archive_file_name [options] [filelist]

.. code-block::

   htar  [-?]  -{c|D|K||t|U|x|X}  [-d debuglevel] -f Archive[-B] [-E] [exclude option(s)][-H opt[:opt...]] [-h]  [-J]  [-l login_name] [-L inputlist] [-M maxfiles]
        [-m] [-O] [-o] [-n time] [-N fifoname] [-P] [-p] [-q]  [-v] [-V [-w]
        [-I {IndexFile | .suffix}] [-Y auto | [Archive COS ID][:Index File COS ID]]
        [-S Bufsize] [-T Max Threads] [Filespec | Directory ...]

   -f Archive   Specifies Archive file name (required option)

   -c      Creates a new Archive file
   -D      Soft-deletes member files from the Archive file (flags files as <deleted> in the Index file)
   -K      Verify the contents of an existing Archive file
   -t      Lists contents of Archive file, using the Index file.
   -U      Undeletes soft-deleted member files in the Archive file
   -x      Extracts files from the Archive file to local file(s). 
   -X      builds a new Index file by reading an existing tar Archive file.

   Options 

   -?      Display help message

   -B      Display block numbers [-t option]

   -d debuglevel   Sets debug level (0 - 5). 0=no debug,5=highest debug level

   -E      Archive file and Index file are local files (not HPSS-resident)

   Exclude options (note: multiple exclude options can be given)
       --exclude pattern      - do not include objects that match pattern
       --exclude-from file    - same as exclude, but read patterns from file
       --exclude-ignore=file  - check for file in each new directory and read exclude patterns that apply just to that directory
       --exclude-ignore-recursive=file - same as exclude-ignore, but apply patterns recursively
       --exclude-backups      - exclude backup and lock file that match the shell globbing patterns '.#*', '*~', '#*#' 
       --exclude-caches       - if directory contains a valid cache file (CACHEDIR.TAG) include directory and cache file, but not contents
       --exclude-caches-under - same as exclude-caches, but only archive the directory, omit the CACHEDIR.TAG file
       --exclude-caches-all   - same as exclude-caches, but omit directory completely
       --exclude-tag=file     - if directory contains file, include only the directory and the file, not the other contents
       --exclude-tag-under    - same as exclude-tag, but omit the file
       --exclude-tag-all      - same as exclude-tag, but completely omit the directory and all its contents
       --exclude-vcs-ignores  - exclude patterns that are ignored by version control systems: .gitignore, cvsignore, .bzrignore,.hgignore
       --exclude-vcs          - exclude files and directories used by version control systems such as CVS, RCS, SCCS, .git, .gitignore,.svn, .bzr,.hg, ...

   -f Archive   Specifies Archive file name (required option)

   -H opt[:opt...] Specifies colon-separated list of options, as follows:
       acct=id|name - set the account ID or account name to use for this run.

       crc - enable CRC checksum generation when copying member files to the archive.
          Enabling this option can cause I/O performance to be degraded and CPU  
          utilization to be increased

       cix - for extract operations from HPSS archives, precopies the index file to
       a temporary local file before reading the archive file

       copies=x - sets number of copies to specify when using auto-COS selection
       during a <create> operation

       nocfchk - disables consistency file vs index file checking 

       exfile=path - specifies path to a file containing an "exceptions list"

        of files that were not successfully transferred

       family=id[,index_id] - specifies file family ID to use when creating HPSS-resident
        archive files and, optionally, the family ID to use when creating the index file

       msg_interval - specifies the delay time (in seconds) for writing status messages
        to the fifo specified by the -N option

       okfile=path - specifies path to a file to contain a list of successfully transferred files

       nocrc - [Default] disable CRC checksum generation when copying 

       noglob - do not expand wildcard characters in pathnames

       norecurse - do not recursively traverse local directories for create/verify/append

       nostage - try to avoid prestaging HPSS tape-resident Archive files for -x,-X,etc. actions

       port=x - specify port number for the "-Hserver" option

       relpaths - (Verify operations only) Force relative paths when verifying member file contents

       rmlocal - remove local member files after successfully writing them to the archive file

       server=host - specify the htar server hostname or IP address. 

       tss=stack_size - specify the thread stacksize to use. Value can include k,kb,m,or mb
          case-insensitive suffix to specify kilobytes or megabytes

       umask=x - specify the octal umask value to set for HPSS or local archive/index file creation

       verify=x[,x...] - perform post-transfer verification.  x can be one or more

          of the following options,which processed left-to-right:

          info - compares tar header info with the corresponding values in the
     index
          crc/nocrc - enable/disable verifying member file CRC value by reading the archive 
     file and comparing the regenerated CRC with that of the index file
          compare/nocompare - enable/disable byte-by-byte comparison of the local member
     files with the corresponding archive files.
          0 - enables "info" verification
          1 - enables level 0 + "crc" verification
          2 - enables level 1 + "compare" verification
          all -  enables all comparison options (currently, tar hdr checking,
     CRC checking, and local file comparisons).
          paranoid/noparanoid - enable/disable last-ditch efforts to avoid problems such
     as comparing whether local files were modified during creation before
     deleting (if -H rmlocal).

   -h      Follow symbolic links as if they were normal files or directories.

   -I index_name   Specifies the Index file name or suffix.  If the first
   character of the index_name is a period, then a suffix (e.g. .idx) 
   is assumed

   -J      Extract/List files based upon index ordinals instead of pathnames

   -l login_name   Specify the login name to use for authenticating

   -L InputList    Use the list of files and directories listed in the InputList
   variable for this operation.

   -M maxfiles  Specifies the maximum number of member files to allow in
    the archive during initial creation.

   -m      Uses the time of extraction as the modification time.

   -N pipename Specifies the pathname of a named pipe (fifo) to which htar will
           send periodic status messages.

   -n time   For creates, only include files that were modified within the time
           period. Time is of the form:  "days" ":hours", or "days:hours"

   -O      Extract files to stdout

   -o      Use UID/GID of user running program, even if running as root.

   -p      Restore perms to their original modes, ignoring the present umask.

   -P      Create intermediate subdirectories for Archive file on creates.

   -q      Run in "quiet" mode

   -S bufsize  Specifies the buffer size to use for HPSS I/O operations.
   Can be specified as kilobytes (e.g. 23k or 23kb) or megabytes (23m  or 23mb)

   -T threads  Specifies the maximum number of threads to use for copying.
   local files to the Archive file.

   -V      "Slightly Verbose" option - displays transfer statistics

   -v      Verbose mode - displays -V info plus list of files operated upon

   -w      Wait for interactive OK 

   -Y auto or Archive_cosID:Index_cosID  Specifies Archive File and/or Index File 
   Class of Service ID to be used when creating new Archive and/or Index File.
   "auto" will result in the COS being selected based upon the archive file size.

.. rubric:: Creating an HTAR Archive File Example

To write file1 and file2 to a new archive called "files.tar"
into the HPSS directory
/SYSADMIN/nesccmgmt/1year/testuser/work:

::

   htar -cvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar file1 file2

To write all of the files named time to a new archive called
time.tar into the HPSS
directory/SYSADMIN/nesccmgmt/1year/testuser/work

::

   htar -cvf /SYSADMIN/nesccmgmt/1year/testuser/work/time.tar time*

.. rubric:: Retrieving an HTAR Archive File Example

To extract file1 and file2 from the archive files.tar
located in the HPSS directory
/SYSADMIN/nesccmgmt/1year/testuser/work:

::

   htar -xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar ./file1 ./file2

To extract all files from the archive files.tar located in
the HPSS directory /SYSADMIN/nesccmgmt/1year/testuser/work:

::

   htar -xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

To list the names of files in the archive files.tar located
in the HPSS directory
/SYSADMIN/nesccmgmt/1year/testuser/work:

::

   htar -tvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

**Recreating a HTAR Index File Example**

This operation is used either to reconstruct an index for
tar files whose Index File is unavailable (e.g.,
accidentally deleted), or for tar files that were not
originally created by HTAR.

::

   htar -Xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

.. rubric:: HSI

HSI is a FTP-like interface to the HPSS. HSI is most useful
for file and directory manipulation. HSI supports wild cards
for local and HPSS pathname pattern matching, and provides
recursion for many commands, including the ability to store,
retrieve, and list entire directory tress, or change
permissions on entire trees. HSI commands include some
familiar ones, such as cp and mkdir, that resemble their
Linux and UNIX counterparts.

For example:

-  ls lists the contents of a directory
-  rm permanently removes a file
-  mkdir creates a directory
-  rmdir deletes a directory
-  mv moves files within the HPSS directory structure.

.. rubric:: Usage

HSI can accept input several different way. From a
interactive command line:

::

   [Skylar.Nelson@tfe01]$ hsi
   [connecting to hpsscore1.fairmont.rdhpcs.noaa.gov/1217]
   ******************************************************************
   *   Welcome to the NESCC High Performance Storage System         *
   *    *
   *   Current HPSS version: 7.4.3 Patch 2  *
   *    *
   *    *
   *           Please Submit Helpdesk Request to        *
   *  rdhpcs.hpss.help@noaa.gov *
   *    *
   *  Announcements:*
   ******************************************************************
   Username: Skylar.Nelson  UID: 2407  Acct: 2407(2407) Copies: 1 Firewall: off [hsi.5.0.2.p5 Mon Sep 12 15:22:37 UTC 2016]
   [hpsscore1]/NCEPDEV->

Single line execution:

::

   hsi "mkdir foo; cd foo; put hpss_file"

From a command file:

::

   hsi "in command_file"

From a batch script:

::

   hsi <<EOF
       pwd
       mkdir foo
       cd foo
       get local_file : hpss_file
   EOF

For 'get' and 'put' operations, HSI uses a different syntax
than FTP to identify the local file name. The syntax uses a
':' (colon character) to separate the local pathname from
the HPSS pathname. CAUTION - The mv, put, and get commands
can overwrite data at their targets without warning. This is
a problem if you mistakenly remove or overwrite data,
because it cannot be recovered. To help prevent
inadvertently overwriting your HPSS files with these
commands, establish directory permissions carefully.

.. rubric:: HSI Examples

.. rubric:: Moving Files/Directories in HPSS Using HSI Example

To mv a directory or file to a new location in HPSS:

``hsi mv /1year/SYSADMIN/old/location /1year/SYSADMIN/new/location``

Please note that mv will only work for files/directories
stored in the same retention directory. If you need to move
data between retention directories you must use cp. Please
contact the HPSS helpdesk for steps on doing this
efficiently.

.. rubric:: Writing Files to HPSS Using HSI Example

To put the file local_file into the HPSS directory
/BMC/testproj/myid/work

``hsi put /full_local/path/local_file : /BMC/testproj/myid/work/local_file``

.. rubric:: Reading a File from HPSS using HSI Example

To get the HPSS file local_file located in the HPSS
directory /BMC/testproj/myid/work

In your current directory (.)

::

   hsi get /BMC/testproj/myid/work/local_file

In the directory /full_local/path with name new_name:

::

   hsi get /full_local/path/new_name : /BMC/testproj/myid/work/local_file

Retrieve file with keeping modification time:

::

   hsi get -p /full_local/path/new_name : /BMC/testproj/myid/work/local_file

.. rubric:: Listing the Contents of an HPSS Directory using HSI

To list the contents of the directory /BMC/testproj

::

   hsi ls /BMC/testproj

List the full path of files in a directory

.. code-block::

   [core]/->ls -N /bench1
   -rw-------    1 Skylar.Nelson  g01      54727283200 Mar 20  2016 /bench1/htar_jet_baseline-aftrupgrd1.tar
   -rw-------    1 Skylar.Nelson  g01 5408 Mar 20  2016 /bench1/htar_jet_baseline-aftrupgrd1.tar.idx
   -rw-------    1 Skylar.Nelson  g01      54727283200 Mar 20  2016 /bench1/htar_jet_baseline-aftrupgrd10.tar
   -rw-------    1 Skylar.Nelson  g01 5408 Mar 20  2016 /bench1/htar_jet_baseline-aftrupgrd10.tar.idx

List tape volume information for a file (PV List is the tape
volume):

::

   [core]/->ls -V /bench1/htar_jet_baseline-aftrupgrd1.tar
   /bench1:
   -rw-------    1 Skylar.Nelson  g01           5         2407 TAPE   54727283200 Mar 20  2016 htar_jet_baseline-aftrupgrd1.tar
   Storage   VV   Stripe
    Level   Count  Width  Bytes at Level
   ----------------------------------------------------------------------------
    1 (tape)   1       1  54727283200
     VV[ 0]:   Object ID: 8c0772a0-8552-11e4-af76-0002559ae41b
   ServerDep: 7d72478a-bb87-11d6-9419-0002559ae41b
     Pos:    121+0   PV List: N0998300

.. rubric:: File Expiration Commands

Expls and Expfind are HSI commands used to show and find the
expiration date of data stored in HPSS.

**Expls help page**

::

   [core]/bench1->expls -h

   Usage expls [-?] [-A] [-R] [-v] [path ...]

     -?  : display this usage

     -A  : display absolute pathnames

     -R  : [standard option]recursively list hash entries for files in the specified path(s)

     -v  : verbose listing mode

**Expfind help page**

::

   [core]/bench1->expfind
   Usage: expfind[ete] [-?] [-A] [-b beginTime] [-d days] [-e endTime] [-R]  [path ...]
     -?  : display this usage
     -A  : display absolute pathname for files
     -b  : specify beginning time in range
     -d  : find file that will be expiring in specified number of days from today
     -e  : specify ending time in range
     -R  : [standard option]recursively delete expiration time for the specified path(s)
     Note: If -b is not specified, then files whose expiration time is <= endTime are listed
           If -e is not specified, then files whose expiration time is>= beginTime are listed
           If neither -b nor -e is specified, all expired files in the path(s) are listed
  based on the time at which the command is started
    Times are of the form YYYY-MM-DD[-hh:mm:ss]
    hours/mins/seconds are optional and default to 00:00:00 if not specified

**To list the expiration date of a file in HPSS**

::

   [core]/bench1->expls /bench1/testfile.20160712a
   Wed Jul 12 15:57:35 2017  /bench1/testfile.20160712a

**To find files that expired on or before a certain date**

::

   [core]/bench1->expfind -e 2016-08-30
   Expiring: /bench1/gyre.tar (Wed Jan 20 22:16:58 2016) Owner: Skylar.Nelson [2407] Group: g01 [201]
   Expiring: /bench1/HSUBSYS1.0.hpssdb.NODE0000.CATN0000.20150605013019.001 (Sat Jun 18 13:32:36 2016) Owner: root [0] Group: system [0]
   Expiring: /bench1/HSUBSYS1.0.hpssdb.NODE0000.CATN0000.20150606013020.001 (Sat Jun 18 15:41:39 2016) Owner: root [0] Group: system [0]
   Expiring: /bench1/htar_thiea_baseline.tar (Thu Jan 28 20:58:11 2016) Owner: Skylar.Nelson [2407] Group: g01 [201]
   Expiring: /bench1/htar_thiea_baseline.tar.idx (Thu Jan 28 20:58:11 2016) Owner: Skylar.Nelson [2407] Group: g01 [201]

.. rubric:: Sample HPSS Batch Job
   :name: sample-hpss-batch-job

The following sample script shows how to transfer data to
HPSS via a batch job on Theia:

::

   #!/bin/bash -l
   #SBATCH --ntasks=1
   #SBATCH --time=0:30:00
   #SBATCH -A nesccmgmt
   #SBATCH --partition=service
   #SBATCH -J hpss-test

   module load hpss

   set -x

   hpssdir=${hpssdir:-/1year/SYSADMIN/nesccmgmt/Skylar.Nelson}  # XXXX: Location of your file in HPSS
   tarfile=${tarfile:-theiatest.tar}    # XXXX: Name of the tar file in HPSS
   dirsave=${dirsave:-/scratch3/SYSADMIN/nesccmgmt/Skylar.Nelson/new_test/} # XXXX: Location of data you want to write to HPSS

   cd $SLURM_SUBMIT_DIR
   #
   #   Check if the tarfile index exists.  If it does, assume that
   #   the data for the corresponding directory has already been
   #   tarred and saved.
   #

    hsi "ls -l ${hpssdir}/${tarfile}.idx"
    tar_file_exists=$?
    if [ $tar_file_exists -eq 0 ]
     then
      echo "File $tarfile already saved."
     exit
    fi

   #   htar is used to create the archive, -P creates
   #   the directory path if it does not already exist,
   #   and an index file is also made.
   #
    htar -P -cvf ${hpssdir}/$tarfile $dirsave
    err=$?
    if [ $err -ne 0 ]
      then
        echo "File $tarfile was not successfully created."
      exit 3
    fi

.. warning::
The HSMS is not an infinite resource. NOAA does not have
   an infinite budget. Quotas will be enabled over time to
   prevent uncontrolled use. Only save what you need to
   save. Consider the cost of time and compute resources to
   regenerate data from the original input files. That is
   often cheaper than storing the data long term.

.. rubric:: HPSS Help


For additional questions, please email: rdhpcs.hpss.help@noaa.gov.

         