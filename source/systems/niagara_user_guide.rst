.. _niagara-user-guide:

******************
Niagara User Guide
******************

.. _niagara-system-overview:

System Overview
===============
As NOAA's R&D severe weather and climate projects expand  to geographically dispersed private and public HPC clouds, it is imperative that the the NOAA RDHPCS program provide a service for data dissemination and analysis outside of the traditional HPC environment. The Niagara system is intended to be a collaborative location where data can be securely copied to and from any location, by any authorized user. It can also be used to disseminate R&D data to NOAA's collaborators around the globe.

The Niagara system includes:

- Back-end storage
- Data Transfer Nodes
- Interactive Nodes
- Software
- Account Management.

Users can connect to the Data Transfer Nodes (DTN) from any remote system to push or pull data. Beyond the Back-end storage and DTNs, the cluster allows for data analysis, visualization, verification, validation and data analytics. It is provided through a combination of hardware and software, which mirrors the user environment and a subset of the tools available on the legacy RDHPCS systems (Hera & Jet) and legacy Analysis systems (PPAN), but can also include software which is unique to this system and not traditionally found on traditional HPC systems.

Niagara System Features:

- 20 cores/socket, 2.5 GHz, 2 sockets/nodes
- 12 Login Nodes
- 25 Compute Nodes
- 2 DTNs available from trusted (pre-approved) NOAA and non-NOAA sites
- 2 Untrusted Data Transfer Nodes (UDTNs) available from anywhere on the internet
- 2 Web servers

.. _niagara-data-transfer:

Data Transfer
=============

In order to use Niagara for file transfers, your must create user account directories. These directories are automatically created with your first login to a Niagara front end. The Niagara front ends may be accessed using either CAC or RSA credentials. Host names for CAC access can be found on `<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/CAC_Login#Tectia_Initial_Setup_Procedures this CAC login page.>`_ Host names for RSA access can be found on this `<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/RSA_Login#The_RSA_login_process RSA login page.>`_

The following directories will automatically be created with your first login:

- /home/First.Last (your home directory)
- /collab1/data/First.Last (for your trusted data)
- /collab1/data_untrusted/First.Last(for your untrusted data)

.. note::

    When you use the DTNs for data transfer, remember:
    - /home tree is not accessible from the DTNs
    - /collab1/data/ tree is only accessible from the "Trusted DTN".
    - /clooab1/data_untrusted tree is only accessible from the "Untrusted DTN"

    
Niagara Data Management
-----------------------

Niagara is a hybrid system, a cross between a traditional HPC system and a data transfer/collaboration system, and available to all RDHPCS users. Therefore, the file system management differs from more traditional HPC systems (Hera and Jet). The following are data management policies:

- There is a default 10GB Lustre quota on each user's home directory "/collab1/home/$USER"
- All files under the "/collab1/data_untrusted/$USER" directory tree which have not been accessed in the last 5 days will be automatically purged.
- All files under the "/collab1/data/$USER" directory tree which have not been accessed in the last 60 days will be automatically purged.
- All files under the "/collab1/data/$PROJECT" directory are treated the same as HPFS (scratch) data, and are not deleted.

Access time is defined as the last time the file was opened for reading or writing.

.. note::

    If the file system's usage approaches total capacity, we will be forced implement a more aggressive purge policy (i.e., 30 day or 15 day purge) . So please actively manage your data.


Niagara System Configuration
============================
======================= =============
\                       Niagara
Front End /             Login Nodes 4
Compute Nodes           25
CPU Type                Intel SkyLake
CPU Speed               2.50 GHz
Cores/node              40
Memory/Core             4.8 GB
Memory/Node             192 GB
Peak Flops/node         2048 GFlops
======================= =============

 .. note::

      -  The Skylake 6148 CPU has two AVX-512 units and hence a theoretical peak of 32 double precision floating point operations per cycle with a base clock rate for floating point operations of 1.6 GHz.
      -  Total flops is a measure of peak, and doesn’t necessarily represent actual performance.


File Systems
-------------

======= ====== ======= =========
name    type   size    Bandwidth
collab1 Lustre 1.7 PiB > 27 GB/s
======= ====== ======= =========


Lustre File System Usage
========================

Basic Lustre Information
------------------------

Lustre is a parallel, distributed file system often used to
support the requirements for high-performance I/O in large
scale clusters by supporting a parallel I/O framework that
scales to thousands of nodes and petabytes of storage.
Lustre features include high-availability and POSIX
compliance.

On the RDHPCS Niagara system there is one Lustre file
systems available for use, /collab1

The serial transfer rate of a single stream is generally
greater than 1 GB/s but can easily increase to 6.5 GB/s from
a single client, and more than 10 GB/s if performed in a
properly configured parallel operation.

Lustre Components
-----------------

Lustre functionality is divided among four primary
components:

-  MDS - Metadata Server
-  MDT - Metadata Target
-  OSS - Object Storage Server
-  OST - Object Storage Target

An MDS is server that assigns and tracks all of the storage
locations associated with each file in order to direct file
I/O requests to the correct set of OSTs and corresponding
OSSs.

An MDT stores the metadata, filenames, directories,
permissions and file layout.

An OSS manages a small set of OSTs by controlling I/O access
and handling network requests to them.

An OST is a block storage device, often several disks in a
RAID configuration.

Niagara Lustre Configuration
----------------------------

All nodes access the lustre file-systems mounted at /collab1.

The number of servers and targets on *each* of the two
Niagara file systems is:

-  2 MDSs (active/active)
-  2 MDTs
-  4 OSSs (active/active, embedded in DDN SFA14kx storage
   controllers)
-  24 OSTs (all are HDDs)
-  1.9 PiB of usable disk space (*df -hP /collab1*)

File Operations
---------------

-  When a compute node needs to create or access a file, it
   requests the associated storage locations from the MDS
   and the associated MDT.
-  I/O operations then occur directly with the OSSs and OSTs
   associated with the file, bypassing the MDS.
-  For read operations file data flows from the OSTs to the
   compute node.

Types of file I/O
-----------------

With Lustre, there are three basic ways which an application
accesses data:

-  Single stream
-  Single stream through a master
-  Parallel

File Striping
-------------

A file is split into segments and consecutive segments are
stored on different physical storage devices (OSTs).

-  Aligned stripes is where each segment fits fully onto a
   single OST. Processes accessing the file do so at
   corresponding stripe boundaries.

-  Unaligned stripes means that some file segments are split
   across OSTs.

Userspace Commands
------------------

Lustre provides a utility to query and set access to the file system.

For a complete list of available options:

.. code-block:: shell

    lfs help

To get more information on a specific option:

.. code-block:: shell

    lfs help <option>

Finding Files
-------------

The *lfs find* command is more *efficient* than the GNU
find, it may be faster too.

An example: to find fortran source files accessed within the
last day.

.. code-block:: shell

    lfs
    lfs find . -atime -1 -name `*.f90

Other lfs Commands

-  lfs cp to copy files.
-  lfs ls to list directories and files.

These commands are often quicker as they reduce the number
of stat and remote procedure calls needed.

Read Only Access
----------------

-  If a file is only going to be read, open it as O_RDONLY.
-  If you don’t care about the access time, open it as
   O_RDONLY|O_NOATIME.
-  If you need access time information and you are doing
   parallel IO, let the master open it as O_RDONLY and all
   other ranks as O_RDONLY|O_NOATIME.

Avoid Wild Cards

tar and rm are *inefficient* when operating on a large set
of files on lustre.

The reason lies in the time it takes to expand the wild
card. "*rm -rf \**" on millions of files could take days,
and impact all other users. (And you shouldn't do just "\*"
anyway, it is dangerous.)

Instead, DO generate a list of files to be removed or
tar-ed, and to act them one at a time, or in small sets.

.. code-block:: shell

   lfs find /path/to/old/dir/ -t f -print0 | xargs -0 -P 8 rm -f

Broadcast Stat Between MPI or OpenMP Tasks
------------------------------------------

If many processes need the information from stat(), do it
**once**, as follows:

-  Have the master process perform the stat() call.
-  Then broadcast it to all processes.

Tuning Stripe Count
-------------------

.. note::

    The following steps are not typicallyneeded on the Niagara Lustre file systems. See the "Progressive File Layouts" description above. Please open a support ticket prior to changing stripe parameters on your /collab1 files.*

General Guidelines
------------------

It is *beneficial* to stripe a file when:

-  Your program reads a single large input file and performs the input operation from many nodes at the same time.
-  Your program reads or writes different parts of the same file at the same time. You should stripe these files to prevent all the nodes from reading from the same OST at the same time. This will avoid creating a bottleneck in which your processes try to read from a single set of disks.
-  Your program waits while a large output file is written. You should stripe this large file so that it can perform the operation in parallel. The write will complete sooner and the amount of time the processors are idle will be reduced.
-  You have a large file that will not be accessed very frequently. You should stripe this file widely (with a larger stripe count), to balance the capacity across more OSTs. This (in current Lustre version) requires rewriting the file.


It is not always necessary to stripe files...

-  If your program periodically writes several small files from each processor, you don't need to stripe the files because they will be randomly distributed across the OSTs.

Striping Best Practices
-----------------------

-  Newly created files and directories inherit the stripe
   settings of their parent directories.
-  You can take advantage of this feature by organizing your
   large and small files into separate directories, then
   setting a stripe count on the large-file directory so
   that all new files created in the directory will be
   automatically striped.
-  For example, to create a directory called "dir1" with a
   stripe size of 1 MB and a stripe count of 8, run:

.. code-block:: shell

    mkdir dir1
    lfs setstripe -c 8 dir1

You can "pre-create" a file as a zero-length striped file by
running lfs setstripe as part of your job script or as part
of the I/O routine in your program. You can then write to
that file later. For example, to pre-create the file
"bigdir.tar" with a stripe count of 20, and then add data
from the large directory "bigdir," run:

.. code-block:: shell

    lfs setstripe -c 20 bigdir.tar
    tar cf bigdir.tar bigdir

Globally efficient I/O, from a system viewpoint, on a lustre
file system is similar to computational load balancing in a
leader-worker programming model, from a user application
viewpoint. The lustre file system can be called upon to
service many requests across a striped file system
asynchronously and this works best if best practices, as
outlined above, are followed. A very large file that is only
striped across one or two OSTs can degrade the performance
of the entire Lustre system by filling up OSTs
unnecessarily.

By striping a large file over many OSTs, you increase
bandwidth for accessing the file and can benefit from having
many processes operating on a single file concurrently. If
all large files accessed by all users are striped then I/O
performance levels can be enhanced for all users.

Small files should never be striped with large stripe counts
if they are striped at all. A good practice is to make sure
small files are written to a directory with a stripe count
of 1... effectively no striping.

Increase Stripe Count for Large Files
-------------------------------------

-  Set the stripe count of the directory to a large value.
-  This spreads the reads/writes across more OSTs, therefore
   \**balancing*\* the load and data.

.. code-block:: shell

    lfs setstripe -c 30 /collab1/data/path/large_files/

Use a Small Stripe Count for Small Files
----------------------------------------

-  Place \**small files*\* on a single OST.
-  This causes the small files not to be spread
   out/\**fragmented*\* across OSTs.

.. code-block:: shell

    lfs setstripe -c 1 /collab1/data/path/small_files/

Parallel IO Stripe Count
------------------------

-  Single shared files should have a stripe count \**equal
   to*\* (or a factor of) the number of processes which
   access the file.
-  If the number of processes in your application is greater
   than 106 (the number of HDD OSTs), use '-c -1' to use all
   of the OSTs
-  The stripe size should be set to allow as much stripe
   alignment as possible.
-  Try to keep each process accessing as few OSTs as
   possible.

.. code-block:: shell

    lfs setstripe -s 32m -c 24 /collab1/data/path/parallel/

You can specify the stripe count and size programmatically,
by creating an MPI info object.

Single Stream IO
----------------

-  Set the stripe count to 1 on a directory.
-  Write all files in this directory.
-  Compute
-  Otherwise set the stripe count to 1 for the file.

.. code-block:: shell

    lfs setstripe -s 1m -c 1 /collab1/data/path/serial/


Using Modules
=============

Niagara users the LMOD hierarchical modules system, which
is slightly different from the traditional "Modules" but is
compatible with it.

LMOD is a Lua based module system that makes it easy to
place modules in a hierarchical arrangement. So you may not
see all the available modules when you type the "module
avail" command.

For example, when you load the Intel module, only libraries
compiled with the Intel compiler will be listed when you
list with the "module avail" command.

Currently the following hierarchies are defined:

::

   compiler    - Currently: intel, pgi
   mpi         - Currently: impi, mvapich2

Use "module spider" command to find all possible modules.

For example, assuming you have not loaded any of the
compiler or mpi modules, if you're interested in finding out
which versions of HDF5 are available, if you type the
command "module avail hdf5" you will not see any of the
modules listed:

.. code-block:: shell

   $ module av hdf5

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

   $

This is because you have not loaded any of the compiler
modules, and HDF5 modules installed on the system require
one of the compiler modules. But if you're still interested
in finding out which versions are available, and when you
want to find more details about which compilers will have to
be loaded in order to use that module, you have to use the
"module spider" command has shown below:

.. code-block:: shell

   $ module spider hdf5

   ------------------------------------------------------------------------------------------------------------
     hdf5:
   ------------------------------------------------------------------------------------------------------------
        Versions:
           hdf5/1.8.14

        Other possible modules matches:
           hdf5parallel, netcdf-hdf5parallel

   ------------------------------------------------------------------------------------------------------------
     To find other possible module matches do:
         module -r spider '.*hdf5.*'

   ------------------------------------------------------------------------------------------------------------
     To find detailed information about hdf5 please enter the full name.
     For example:

        $ module spider hdf5/1.8.14
   ------------------------------------------------------------------------------------------------------------

   $
   $
   $ module spider hdf5/1.8.14

   ------------------------------------------------------------------------------------------------------------
     hdf5: hdf5/1.8.14
   ------------------------------------------------------------------------------------------------------------

        Other possible modules matches:
           hdf5parallel, netcdf-hdf5parallel

       This module can only be loaded through the following modules:

         intel/13.1.3
         intel/14.0.2
         intel/15.0.0
         intel/15.1.133
         pgi/12.5
         pgi/14.10
         pgi/15.1

   ------------------------------------------------------------------------------------------------------------
     To find other possible module matches do:
         module -r spider '.*hdf5/1.8.14.*'

   $

The current configuration has no default modules loaded.
Run:

.. code-block:: shell

   $ module avail

to see the list of modules available for you load now.

At a minimum you will want to do:

.. code-block:: shell

   $ module load intel impi
   $ module list

   Currently Loaded Modules:
     1) intel/18.0.5.274   2) impi/2018.0.4


   $

Modules on Niagara
------------------

To find the latest modules on Niagara, run **module avail** to see the list of available modules for
the compiler and the MPI modules currently loaded:

.. code-block:: shell

   $ module avail

   --------------------------------- /apps/lmod/lmod/modulefiles/Core ---------------------------------
      lmod/7.7.18    settarg/7.7.18

   ------------------------------------ /apps/modules/modulefiles -------------------------------------
      advisor/2019         g2clib/1.4.0    intel/19.0.4.243  rocoto/1.3.1
      antlr/2.7.7          gempak/7.4.2    intelpython/3.6.8 szip/2.1
      antlr/4.2     (D)    grads/2.0.2     matlab/R2017b     udunits/2.1.24
      cairo/1.14.2         hpss/hpss       nag-fortran/6.2   vtune/2019
      cnvgrib/1.4.0        idl/8.7         nccmp/1.8.2       wgrib/1.8.1.0b
      contrib  imagemagick/7.0.8-53        ncview/2.1.3      xxdiff/3.2.Z1
      ferret/6.93          inspector/2019  performance-reports/19.1.1
      forge/19.1           intel/18.0.5.274     (D)    pgi/19.4

     Where:
      D:  Default Module

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".


   $

Please note that because LMOD is a hierarchical module
system you only see the list of modules that you can load at
this point in time (based on what other modules you may have
loaded).

To see the complete list of modules available on the system,
use the "module spider" command:

.. code-block:: shell

   $ module spider

   ------------------------------------------------------------------------------------------------
   The following is a list of the modules currently available:
   ------------------------------------------------------------------------------------------------
     advisor: advisor/2019

     anaconda: anaconda/anaconda2, anaconda/anaconda2-4.4.0, anaconda/anaconda3-4.4.0, ...

     antlr: antlr/2.7.7, antlr/4.2

     bitrep: bitrep/1.0
   …

   $

In the above, each module name represents a different
package. In cases where there are multiple versions of a
package, one will be set as a default. For example, for the
intel compiler there are multiple choices:

.. code-block:: shell

   $ module avail intel

   ------------------------------------ /apps/modules/modulefiles -------------------------------------
      intel/18.0.5.274 (D)    intel/19.0.4.243    intelpython/3.6.8

     Where:
      D:  Default Module

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

   $

So if you run:

.. code-block:: shell

   $ module load intel

The default version will be loaded, in this case
intel/18.0.5.274.

If you want to load a specific version, you can. We highly
recommend you use the system defaults unless something is
not working or you need a different feature. To load a
specific version, specify the version number.

.. code-block:: shell

   $ module purge
   $ module load intel/19.0.4.243
   $ module list

   Currently Loaded Modules:
     1) intel/19.0.4.243

   $

In some cases other required modules may be loaded for you.
The Intel module manages all the sub modules, you do not
have to worry about it.

.. note::

    -  When unloading modules, only unload those that you have loaded. The others are done automatically from master modules.
    -  Modules is a work in progress, and we will be improving their uses and making which modules you load more clear.

Loading Modules in batch jobs
-----------------------------

Any modules that you loaded when building your codes needs
to be loaded when your job runs as well. This means that you
must put the same module commands in your batch scripts that
you ran before building your code.

Modules with sh, bash, and ksh scripts
--------------------------------------

Due to the way the POSIX standard is defined for bash, sh,
and ksh you **MUST** add the -l option (that is a lowercase
L) to the shebang (e.g. #!/bin/sh) line at the top of your
script for all sh, bash, or ksh batch scripts. For example:

.. code-block:: shell

   #!/bin/ksh -l

   module load intel
   module load impi

   srun -n 12 ​./xhpl

Failure to use -l will cause the module commands to fail and
your job will not run properly and may crash in hard to
diagnose ways.

Additional Documentaion on Lua Modules
--------------------------------------

Detailed information on Lua module utility is available `<http://lmod.readthedocs.org/en/latest/ here.>`_


Frequently Asked Questions
==========================

Why can't I reach external sites via git, wget,scp, or other tools?
-------------------------------------------------------------------
   
By default, outbound HTTP/HTTPS access is blocked by the
RDHPCS firewalls. A firewall change request must be
submitted and vetted by security before the site is allowed
to be accessed. Access is almost always granted for
government and university sites. I will submit a firewall
change request to allow access to NSIDC from any R&D HPC
system (Niagara, Hera, or Jet). It will take about 1-2
weeks. Are there any other sites that you need access to?

Why can't I access HPSS from anywhere but WCOSS and R&D HPC systems?
--------------------------------------------------------------------

Since the Orion and other external systems are non-NOAA HPC
systems and managed completely independently, there is no
way that we can allow direct HPSS access from these systems.
This has been a major issue for many of our users.

Niagara was deployed so that users could retrieve data from
HPSS and move it to an external NOAA or non-NOAA sites. Data
can of course be moved in the opposite direction as well.
The CRON service is available on all R&D HPC systems for
creating automated scripts and workflows for moving data. If
automated workflows are required and justified by the user,
then it is possible to set up Unattended Data
Transfers using scp and key-pair authentication.


Why am I seeing slow data rates when moving data to/from Niagara?
-----------------------------------------------------------------

We realized early on that scp transfer rates would not
suffice to move large amounts of data between Niagara and
external systems. To provide a solution we
have deployed a new service called Globus Online. Although
it is still very much a new service for us and we are still
flushing out the user documentation, users should be able to
move large amounts of data at somewhere around 100-200MB/s.
Since Niagara sites at the same site as HPSS, you should
also get decent data rates when moving data to and from
HPSS.

For more information please see A LINK TO NEW GLOBUS DOCS

I hate your confusing documentation.
------------------------------------

If you have specific issues or requests for missing or confusing
documentation, please open up a help ticket and let us know.
Since our support team is stretched pretty thin, it is
always helpful to get feedback from users on where we have
deficiencies.


