.. _hera-user-guide:

***************
Hera User Guide
***************

About NESCC
===========

The NOAA Environmental Security Computing Center (NESCC), located in Fairmont,
West Virginia, is the location of NOAA's newest High Performance Computing Data
Center. This site provides computing resources to support NOAA's research in
Weather and Climate modeling as well as its other environmental research areas.

There are currently two major systems at NESCC:

- Hera* A 760 Tflop Cray Compute Cluster high performance computing system
- HPSS* A 50 Petabyte IBM/Oracle hierarchical storage management system.

.. _hera-system-overview:

System Overview
===============

- Capacity of 3,270 trillion floating point operations per second – or 3.27
  petaFLOPS
- The Fine Grain Graphical Processing Units have a total capacity of 2,000
  trillion floating point operations per second, or 2.0 petaFLOPS
- 45 million hours per month with 63,840 cores and a total scratch
  disk capacity of 18.5 Petabytes.

NESCC is also home to Niagara, a cloud-based computing resource. In addition,
Test and Development systems are available through NESCC for system and
application testing.

System Configuration
--------------------

+-------------------------+---------------+------------------+---------------+------------------+
|                         | Hera TCA      | Hera FGA         | Juno TCA      | Juno FGA         |
+=========================+===============+==================+===============+==================+
| **CPU Type**            | Intel SkyLake | Intel Haswell    | Intel SkyLake | Intel Haswell    |
+-------------------------+---------------+------------------+---------------+------------------+
| **CPU Speed**           | 2.40 GHz      | 2.460 GHz        | 2.40 GHz      | 2.460 GHz        |
+-------------------------+---------------+------------------+---------------+------------------+
| **Reg Compute Nodes**   | 1328          | 100              | 14            | 2                |
+-------------------------+---------------+------------------+---------------+------------------+
| **Cores/node**          | 40            | 20               | 40            | 20               |
+-------------------------+---------------+------------------+---------------+------------------+
| **Total Cores**         | 53,120        | 2000             | 560           | 40               |
+-------------------------+---------------+------------------+---------------+------------------+
| **Memory/Core**         | 96 GB         | 256 GB           | 90 GB         | 256 GB           |
+-------------------------+---------------+------------------+---------------+------------------+
| **Peak FLOPS/node**     | 12            | NA               | 12            | NA               |
+-------------------------+---------------+------------------+---------------+------------------+
| **Service Code Memory** | 187 GB        | NA               | 187 GB        | NA               |
+-------------------------+---------------+------------------+---------------+------------------+
| **Total BigMem Nodes**  | 268           | NA               | 268           | NA               |
+-------------------------+---------------+------------------+---------------+------------------+
| **BigMem Node Memory**  | 384 GB        | NA               | 384 GB        | NA               |
+-------------------------+---------------+------------------+---------------+------------------+
| **CPU FLOPS**           | 2672 TF       | 83.1 TF          | 28 TF         | 1.6 TF           |
+-------------------------+---------------+------------------+---------------+------------------+
| **GPUs/Node**           | NA            | 8 P100           | NA            | 8 P100           |
+-------------------------+---------------+------------------+---------------+------------------+
| **Total GPUs**          | NA            | 800              | NA            | 16               |
+-------------------------+---------------+------------------+---------------+------------------+
| **GPU FLOPS/GPU**       | NA            | 4.7              | NA            | 4.7              |
+-------------------------+---------------+------------------+---------------+------------------+
| **Interconnect**        | HDR-100 IB    | FDR-10 (40 Gbps) | HDR-100 IB    | FDR-10 (40 Gbps) |
+-------------------------+---------------+------------------+---------------+------------------+
| **Total GPU FLOPS**     | NA            | 3760 TF          | NA            | 75 TF            |
+-------------------------+---------------+------------------+---------------+------------------+

.. note::

   - The Skylake 6148 CPU has two AVX-512 units and hence a
     theoretical peak of 32 double precision floating point operations
     per cycle with a base clock rate for floating point operations of
     1.6 GHz.
   - Total FLOPS is a measure of peak, and doesn’t necessarily
     represent actual performance.
   - Juno is the Test and Development System. Users must be granted
     specific access to the system for use.
   - The nodes with GPUs are the same as what was on Theia; But the
     network has been upgraded to EDR.


Lustre File System Usage
========================

Lustre is a parallel, distributed file system often used to support
the requirements for high-performance I/O in large scale clusters by
supporting a parallel I/O framework that scales to thousands of nodes
and petabytes of storage. Lustre features include high-availability
and POSIX compliance.

On the RDHPCS Hera cluster there are two Lustre file systems available
for use: ``/scratch1`` and ``/scratch2``

The serial transfer rate of a single stream is generally greater than
1 GB/s but can easily increase to 6.5 GB/s from a single client, and
more than 10 GB/s if performed in a properly configured parallel
operation.

Lustre Volume and File Count
----------------------------

For efficient resource usage, Hera's ``/scratch1`` and ``/scratch2``
Lustre file systems have project based volume and file countquotas.
Each project has an assigned quota which is sharedby all users on the
project. File count quotas are implemented to preserve the increased
performance of the2 tier storage architecture where the first 128 KB
of eachfile is stored on SSD and the remainder if any on HDD.
Historical data from Theia and Jet show that the average file count
per GB is ~100. By default projects on Hera are given a file count
quota of 200 files per GB of volume quotaor 100,000 files whichever is
higher. Users will receive warning emails when their quota is
exceeded. When either the volume or file count quota is exceed by more
than 1.2x, writes will not be allowed.

Summary and detailed information on finding your project's disk volume
and file count quota and usage is found at:  `Getting Information
About Your  Projects
<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_Information_About_Your_Projects_-_SLURM>`__

Volume Quota Increase
^^^^^^^^^^^^^^^^^^^^^

If you are approaching your quota, your first step should be to delete
old files and/or move files to HPSS tape systems as appropriate. If
more volume is still needed, request a volume quota increases by
submitting a Hera :ref:`help ticket <getting_help>` with a
justification, including:

* Project name.
* Requested quota. Is the increase request temporary or permanent? If
  temporary, for how long?
* Justification, including an analysis of your workload detailing the
  volume needed


File Count Quota Increase
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are approaching your quota or your file count quota or are
running over 200 files/GB, your first step should be to delete old
small files. If you want to keep them around but they are not accessed
frequently, you should tar up many small files into one big file. If
you have an exceptional situation and believe you need a quota
increase, start a Hera :ref:`help ticket <getting_help>` including the
following information:


* Project name.
* Justification, including an analysis of your workload detailing the
  files/GB needed.
* Requested quota. Is the increase request temporary or permanent? And
  if temporary, for how long?


It will save time if the request comes directly from the or Portfolio
Manager. Once requests are approved by the PI they will be reviewed by
the Hera resource manager.

Lustre
======

Lustre functionality is divided among four primary components:

* MDS* Metadata Server
* MDT* Metadata Target
* OSS* Object Storage Server
* OST* Object Storage Target

An MDS server assigns and tracks all of the storage locations
associated with each file in order to direct fileI/O requests to the
correct set of OSTs and corresponding OSSs.

An MDT stores the metadata, filenames, directories, permissions and
file layout.

An OSS manages a small set of OSTs by controlling I/O accessand
handling network requests to them.

An OST is a block storage device, often several disks in a RAID
configuration.

Hera Lustre Configuration
-------------------------

All nodes (login and compute) access the lustre file-systems mounted
at ``/scratch1`` and ``/scratch2``. Each user has access to one or
more directories based on theproject which they are a member of, such
as:

.. code-block:: shell

   /scratch[1,2]/${PORTFOLIO}/${PROJECT}/${TASK}

where ``${TASK}`` is often, but not necessarily, the individual user's
login ID, as defined by the project lead. 

The number of servers and targets on each of the two Herafile systems
is:

* 2 MDSs (active/active)
* 2 MDTs
* 16 OSSs (active/active, embedded in DDN SFA 18k storage controllers)
* 122 OSTs (106 are HDDs, 16 are SSDs)
* 9.1 PiB of usable disk space (*df*hP /scratch{1,2}*)

Since each file system has two metadata targets, each project
directory is configured to use one of MDTs, and they are spread
roughly evenly between the two MDTs. This means that approximately 25%
of all Hera projects share metadata resources.

File Operations
---------------

When a compute node needs to create or access a file, it requests the
associated storage locations from the MDS and the associated MDT. I/O
operations then occur directly with the OSSs and OSTs associated with
the file, bypassing the MDS. For read operations file data flows from
the OSTs to the compute node.

Types of file I/O
-----------------

With Lustre, an application accesses data in the following ways:

* Single stream
* Single stream through a master
* Parallel

File Striping
-------------

A file is split into segments and consecutive segments arestored on
different physical storage devices (OSTs).

Aligned vs Unaligned Stripes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aligned stripes is where each segment fits fully onto a single OST.
Processes accessing the file do so at corresponding stripe
boundaries. Unaligned stripes means some file segments are split
across OSTs.

.. _hera-progressive-file-layouts:

Progressive File Layouts
^^^^^^^^^^^^^^^^^^^^^^^^

The ``/scratch1`` and ``/scratch2`` file systems are enabled with a
feature called Progressive File Layouts (PFL) that does file layout in
a way which is efficient for the vast majority of use cases. It uses a
single stripe count for small files (reducing overhead) and increases
the striping as the file gets bigger (increasing bandwidth and
balancing capacity), all without any user involvement. These file
systems are also augmented by a set of SSD OSTs (described above) and
with the PFL capability is further optimized for small file
performance. By default, smaller files are stored completely in SSD,
which further decreases random operation latency and allows the HDDs
to run more efficiently for streaming reads and writes. The default
configuration will automatically stripe and place files in a generally
optimal fashion to improve I/O performance for varying file sizes,
including the use of SSDs for better small-file performance. The
defaults also attempt to makethe best use of the SSD targets (which
are faster, but have much less capacity than HDDs). More details on
PFL are available in the `Lustre documentation
<https://doc.lustre.org/lustre_manual.xhtml>`_.

.. Note::

   The PFL feature makes much of the information documented below
   regarding customized striping unnecessary.

Users should not need to adjust stripe count and size on ``/scratch1``
and ``/scratch2``.  With PFL enabled, setting your own stripe layout
may reduce I/O performance for your files and the overall I/O
performance of the file system. If you have already used ``lfs
setstripe`` commands documented below, you should probably remove the
striping that may have already been set.

Here are the steps you should follow if you have any directories that
had explicitly set non-default striping:

#. Remove all ``lfs setstripe`` commands from your scripts.
#. Run the following command which changes the stiping back to default
   for each of the directories on which you may have set striping:

   .. code-block:: shell

      $ lfs setstripe -d <dir>

#. Open a help ticket with the subject like
   */scratchX/<portfolio>/<project> striped directories*. We will
   examine the files and assist with migrating files to an optimal
   layout if necessary.

Userspace Commands
------------------

Lustre provides the ``lfs`` utility to query and set access to the
file system. For a complete list of available options run ``lfs
help``.  To get more information on a specific ``lfs`` option, run
``lfs help <option>``.

Checking Diskspace
^^^^^^^^^^^^^^^^^^

Hera file system allocations are project based. Lustre quotas are
tracked and limited by Project ID (usually the same as group ID and
directory name). The Project ID is assigned to top-level project
directories and will be inherited for all new subdirs. Tracking and
enforcement includes maximum file count, not just capacity. To check
your usage details...

#. Look up your project ID number (not the name)  id
#. Query your usage and limits using that number, for a given file
   system.

.. code-block:: shell

   $ lfs quota -p <project ID number> /scratchX

User and Group usage (capacity and file count) is tracked but not
limited. You can also find your usage and your Unix group's usage:

.. code-block:: shell

   $ lfs quota -u <User.Name> /scratchX
   $ lfs quota -g <groupname> /scratchX

.. note::

  This is the group that owns the data, regardless of where it is
  stored in the file system directory hierarchy.

For example, to get a summary of the disk usage for project *rtnim*:

.. code-block:: shell

   $ id   
   uid=5088(rtfim) gid=10052(rtfim) groups=10052(rtfim)...
   $ lfs quota -p 10052 /scratch1
   Disk quotas for prj 10052 (pid 10052):
   Filesystem  kbytes   quota   limit   grace   files   quota   limit   grace
   /scratch1       4  1048576 1258291      *      1  100000  120000      *
   ("kbytes" = usage, "quota" = soft quota, "limit" = hard quota)

Finding Files
^^^^^^^^^^^^^

The ``lfs find`` command is more efficient than the standard ``find``,
it may be faster too. For example, finding fortran source files
accessed within the last day:

.. code-block:: shell

   $ lfs find . -atime -1 -name '*.f90'

Striping Information
^^^^^^^^^^^^^^^^^^^^

You can view the file striping (layout on disk) of a file with:

.. code-block:: shell

   $ lfs getstripe <filename>

The Hera default configuration uses Progressive File Layout (PFL).

  * The first part of each file is stored on SSD
  * Up to 256 KB, single stripe
  * As the file grows bigger, it overflows to disks and it stripes it
    across more disks and more disks
  * Up to 32 MB on HDD, single stripe
  * Up to 1 GB on HDD, 4-way stripe
  * Up to 32 GB on HDD, 8-way stripe
  * > 32 GB on HDD, 32-way stripe, larger object size

So small files reside on SSDs, big files get striped progressively
wider.  The ``lfs getstripe`` command above shows the full layout.
Typically not all components are instantiated. Only the extents which
have *l_ost_idx* (object storage target index) and *l_fid* (file
identifier) listed actually have created objects on the OSTs.

.. warning::

   Do not attempt to set striping!! If you think the default is not
   working for you, submit a :ref:`help ticket <getting_help>` to let
   us know and assist.

Other lfs Commands
^^^^^^^^^^^^^^^^^^

* ``lfs cp`` – to copy files.
* ``lfs ls`` – to list directories and files.

These commands are often quicker as they reduce the number of stat and
remote procedure calls needed.

Read Only Access
^^^^^^^^^^^^^^^^

If a file is only going to be read, open it as *O_RDONLY*. If you
don’t care about the access time, open it as *O_RDONLY* or
*O_NOATIME*. If you need access time information and you are doing
parallel IO, let the master open it as *O_RDONLY* and all other ranks
as *O_RDONLY* or *O_NOATIME*.

Avoid Wild Cards
^^^^^^^^^^^^^^^^

The ``tar`` and ``rm`` commands are inefficient when operating on a
large set of files on Lustre. The reason lies in the time it takes to
expand the wildcard. Performing ``rm -rf *`` on millions of files
could take days,and impact all other users. (And you shouldn't do just
``*`` anyway, it is dangerous. Instead, generate a list of files to be
removed ortar-ed, and to act them one at a time, or in small sets.

.. code-block:: shell

   $ lfs find /path/to/old/dir/ -t f -print0 | xargs -0 -P 8 rm -f

Broadcast Stat Between MPI or OpenMP Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If many processes need the information from ``stat()``, do it once, as
follows:

#. Have the master process perform the ``stat()`` call.
#. Then broadcast it to all processes.

Tuning Stripe Count (not typically needed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   The following steps are not typically needed on the Hera Lustre
   file systems. See the :ref:`Progressive File Layouts
   <hera-progressive-file-layouts>` description above. Please open a
   :ref:`help ticket <getting_help>` prior to changing stripe
   parameters on your ``/scratch1`` or ``/scratch2`` files.

General Guidelines
""""""""""""""""""
It is *beneficial* to stripe a file when...

* Your program reads a single large input file and performs the input
  operation from many nodes at the same time.
* Your program reads or writes different parts of the same file at the
  same time.

   * You should stripe these files to prevent all the nodes from
     reading from the same OST at the same time. This will avoid
     creating a bottleneck in which your processes try to read from a
     single set of disks.
   * Your program waits while a large output file is written.

* You should stripe this large file so that it can perform the
  operation in parallel. The write will complete sooner and the amount
  of time the processors are idle will be reduced.
* You have a large file that will not be accessed very frequently. You
  should stripe this file widely (with a larger stripe count), to
  balance the capacity across more OSTs. * This (in current Lustre
  version) requires rewriting the file.

It is not always necessary to stripe files.

If your program periodically writes several small files from each
processor, you don't need to stripe the files  because they will be
randomly distributed across the   OSTs.

Striping Best Practices
"""""""""""""""""""""""

* Newly created files and directories inherit the stripe settings of
  their parent directories.
* You can take advantage of this feature by organizing your large and
  small files into separate directories, then setting a stripe count
  on the large-file directory so that all new files created in the
  directory will be automatically striped.
* For example, to create a directory called ``dir1`` with a stripe size
  of 1 MB and a stripe count of 8, run:

.. code-block:: shell

   $ mkdir dir1    
   $ lfs setstripe -c 8 dir1

You can pre-create a file as a zero-length striped file by running
``lfs setstripe`` as part of your job script or as part of the I/O
routine in your program. You can then write to that file later. For
example, to pre-create the file ``bigdir.tar`` with a stripe count of
20, and then add data from the large directory ``bigdir``, run:

.. code-block:: shell

   $ lfs setstripe*c 20 bigdir.tar
   $ tar cf bigdir.tar bigdir

Globally efficient I/O, from a system viewpoint, on a Lustre file
system is similar to computational load balancing in a leader-worker
programming model, from a user application viewpoint. The Lustre file
system can be called upon to service many requests across a striped
file system asynchronously, and this works best if best practices,
outlined above, are followed. A very large file that is only striped
across one or two OSTs can degrade the performanceof the entire Lustre
system by filling up OST sunnecessarily. By striping a large file over
many OSTs, you increase bandwidth for accessing the file and can
benefit from having many processes operating on a single file
concurrently. If all large files accessed by all users are striped
then I/O performance levels can be enhanced for all users. Small files
should never be striped with large stripe counts if they are striped
at all. A good practice is to make sure small files are written to a
directory with a stripe countof 1... effectively no striping.

Increase Stripe Count for Large Files
"""""""""""""""""""""""""""""""""""""

Set the stripe count of the directory to a large value.  This spreads
the reads/writes across more OSTs, balancing the load and data.

.. code-block:: shell

   $ lfs setstripe -c 30 /scratchN/your_project_dir/path/large_files/

Use a Small Stripe Count for Small Files
""""""""""""""""""""""""""""""""""""""""

Place small files on a single OST. This causes the small files not to
be spread out, fragmented, across OSTs.

.. code-block:: shell

   $ lfs setstripe -c 1 /scratchN/your_project_dir/path/small_files/

Parallel IO Stripe Count
""""""""""""""""""""""""

Single shared files should have a stripe count equal to, or a factor
of the number of processes which access the file. If the number of
processes in your application is greater than 106 (the number of HDD
OSTs), use '-c 1' to use all of the OSTs.  The stripe size should be
set to allow as much stripe alignment as possible. Try to keep each
process accessing as few OSTs as possible.

.. code-block:: shell

   $ lfs setstripe -s 32m -c 24 /scratchN/your_project_dir/path/parallel/

You can specify the stripe count and size programmatically, by
creating an MPI info object.

Single Stream IO
""""""""""""""""

* Set the stripe count to 1 on a directory.
* Write all files in this directory.
* Compute
* Otherwise set the stripe count to 1 for the file.

.. code-block:: shell

   $ lfs setstripe -s 1m -c 1 /scratchN/your_project_dir/path/serial/


Applications and Libraries
==========================

A number of applications are available on Hera. They should
be run on a compute node. They are serial tasks, not
parallel, and thus, a single core may be sufficient. If your
memory demands are large, it may be appropriate to use an
entire node even though you are using only a single core.

Using Anaconda Python on Hera
-----------------------------

Please see :ref:`Installing Miniconda <installing-miniconda>` for
installation instructions.

.. warning::

   RDHPCS support staff does not have the available resources to
   support or maintain these packages. You will be responsible for the
   installation and troubleshooting of the packages you choose to
   install. Due to architectural and software differences some of the
   functionality in these packages may not work.

MATLAB
------

Information is available `here:
<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php?title=Applications_and_Libraries#MATLAB>`_.

Using IDL on Hera
-----------------

The IDL task can require considerable resources. It should not be run
on a frontend node. It is recommended that you run IDL on a compute
node either in a job or via interactive job. Take a whole node and
there is no need to use the ``--mem=<memory>`` parameter. If you
request a single task you would get a shared node and in those
instances you should consider using ``--mem=<memory>`` option (since
IDL is memory intensive).

To run IDL on an interactive queue:

.. code-block:: shell

   $ salloc -x11=first -ntasks=40 -t 60 -A <account>
   $ cd <your working directory>
   $ module load idl
   $ idl      # or idled

IDL can be run from a normal batch job as well.

Multi-Threading in IDL
^^^^^^^^^^^^^^^^^^^^^^

IDL is a multi-threaded program. By default, the number of
threads is set to the number of CPUs present in the
underlying hardware. The default number of threads for Hera
compute node is 48 (the number of virtual CPUs). It should
not be run as a serial job with the default thread number as
the threaded program will affect other jobs on the same
node.

The number of threads needs to be set as 1 if a job is going to be
submitted as a serial job, which can be achieved by setting the
environment variable ``IDL_CPU_TPOOL_NTHREADS`` to 1, or setting it
with the CPU procedure in IDL: ``CPU, TPOOL_NTHREADS = 1``. If a job
requires larger than 10 GB memory, it is recommended to run the job on
either the bigmem node or a whole node.

Using ImageMagick on Hera
-------------------------

The ImageMagick module can be loaded on Hera with the
following command:

.. code-block:: shell

  $ module load imagemagick

The modules set an environment variable and paths in your
environment to access the files.

:$MAGICK_HOME: is set to the base directory
:$MAGICK_HOME/bin: is added to your search path
:$MAGICK_HOME/man: is added to your MANPATH
:$MAGICK_HOME/lib: is added to your LD_LIBRARY_PATH

ImageMagick, and the utilities that are part of this package
including ``convert``, should be run on a compute node for
gang processing of many files, either via a normal batch job
or via an interactive job.

Using R on Hera
---------------

R is a software environment for statistical computing and
graphics. It is available on Hera as a module within the
Intel module families. The R module can be loaded on Hera
with the following commands:

.. code-block:: shell

   $ module load intel
   $ module load R

R has many contributed packages that can be added to standard R. `CRAN
<https://cran.r-project.org/web/packages/>`_, the global repository of
open-source packages that extend the capabiltiies of R, has a complete
list of R packages as well as the packages for download.

Due to the access restrictions from Hera to the CRAN repository, you
may need to download an R package first to your local workstation and
then copy it to your space on Hera to install the package as detailed
below.

To install a package from the command line:

.. code-block:: shell

  $ R CMD INSTALL <path_to_file>

To install a package from within R

.. code-block:: r

  > install.packages("path_to_file", repos = NULL, type="source")

where *path_to_file* would represent the full path and file
name.

When you try to install a package for the first time, you
may get a message similar to:

.. code-block:: shell

  'lib = "/apps/R/3.2.0-intel-mkl/lib64/R/library"' is not writable
  Would you like to use a personal library instead?  (y/n)

Reply with *y* and it will prompt you for a location.

Libraries
---------

A number of libraries are available on Hera. The following
command can be used to list all the available libraries and
utilities:

.. code-block:: shell

   module spider


Using Modules
=============

Hera uses the LMOD hierarchical modules system. LMOD is a Lua based
module system that makes it easy to place modules in a hierarchical
arrangement. So you may not see all the available modules when you
type the ``module avail`` command.

For example, when you load the Intel module, only libraries compiled
with the Intel compiler will be listed when you list with the ``module
avail`` command.

Currently the following hierarchies are defined:

:compiler: Currently: intel, pgi
:mpi: Currently: impi, mvapich2

Use the ``module spider`` command to find all possible modules.

For example, assuming you have not loaded any of the compiler or mpi
modules, if you're interested in finding out which versions of HDF5
are available, if you type the command ``module avail hdf5`` you will
not see any of the modules listed:

.. code-block:: shell

   $ module avail hdf5

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

This is because you have not loaded any of the compiler modules, and
HDF5 modules installed on the system require one of the compiler
modules. But if you're still interested in finding out which versions
are available, and when you want to find more details about which
compilers will have to be loaded in order to use that module, you have
to use the "module spider" command as shown below:

.. code:: shell

   $ module spider hdf5

   *-----------------------------------------------------------------------------------------------------------
      hdf5:
   *-----------------------------------------------------------------------------------------------------------
         Versions:
            hdf5/1.8.14

         Other possible modules matches:
            hdf5parallel, netcdf-hdf5parallel

   *-----------------------------------------------------------------------------------------------------------
      To find other possible module matches do:
          module*r spider '.*hdf5.*'

   *-----------------------------------------------------------------------------------------------------------
      To find detailed information about hdf5 please enter the full name.
      For example:

         $ module spider hdf5/1.8.14
   *-----------------------------------------------------------------------------------------------------------

   $ module spider hdf5/1.8.14

   *-----------------------------------------------------------------------------------------------------------
      hdf5: hdf5/1.8.14
   *-----------------------------------------------------------------------------------------------------------

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

   *-----------------------------------------------------------------------------------------------------------
      To find other possible module matches do:
          module*r spider '.*hdf5/1.8.14.*'

The current configuration has no default modules loaded. Run:

 .. code:: shell

   $ module avail

to see the list of modules available for you load now.
At a minimum you will want to do:

.. code-block:: shell

   $ module load intel impi
   $ module list

   Currently Loaded Modules:
      1) intel/18.0.5.274   2) impi/2018.0.4

Modules on Hera
---------------

The way to find the latest modules on Hera is to run
``module avail`` to see the list of available modules for
the compiler and the MPI modules currently loaded:

.. code-block:: shell

   $ module avail

   *-------------------------------- /apps/lmod/lmod/modulefiles/Core*--------------------------------
       lmod/7.7.18    settarg/7.7.18

   *----------------------------------- /apps/modules/modulefiles*------------------------------------
       advisor/2019         g2clib/1.4.0           intel/19.0.4.243            rocoto/1.3.1
       antlr/2.7.7          gempak/7.4.2           intelpython/3.6.8           szip/2.1
       antlr/4.2     (D)    grads/2.0.2            matlab/R2017b               udunits/2.1.24
       cairo/1.14.2         hpss/hpss              nag-fortran/6.2             vtune/2019
       cnvgrib/1.4.0        idl/8.7                nccmp/1.8.2                 wgrib/1.8.1.0b
       contrib              imagemagick/7.0.8-53   ncview/2.1.3                xxdiff/3.2.Z1
       ferret/6.93          inspector/2019         performance-reports/19.1.1
       forge/19.1intel/18.0.5.274     (D)          pgi/19.4

      Where:
       D:  Default Module

Please note that, because LMOD is a hierarchical module system, you
only see the list of modules that you can load at this point in time
(based on what other modules you may have loaded). To see the complete
list of modules available on the system, use the ``module spider``
command:

.. code-block:: shell

   $ module spider

   *-----------------------------------------------------------------------------------------------
    The following is a list of the modules currently available:
   *-----------------------------------------------------------------------------------------------
      advisor: advisor/2019

      anaconda: anaconda/anaconda2, anaconda/anaconda2-4.4.0, anaconda/anaconda3-4.4.0, ...

      antlr: antlr/2.7.7, antlr/4.2

      bitrep: bitrep/1.0
   ...

In this example, each module name represents a different package. In
cases where there are multiple versions of a package, one will be set
as a default. For example, for the intel compiler there are multiple
choices:

.. code-block:: shell

   $ module avail intel

   *----------------------------------- /apps/modules/modulefiles*------------------------------------
       intel/18.0.5.274 (D)    intel/19.0.4.243    intelpython/3.6.8

      Where:
       D:  Default Module

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

So if you run:

.. code-block:: shell

   $ module load intel

the default version will be loaded, in this case intel/18.0.5.274.

If you want to load a specific version, you can. We highly recommend
you use the system defaults unless something is not working or you
need a different feature. To load a specific version, specify the
version number.

.. code-block:: shell

   $ module load intel/19.0.4.243

In some cases other required modules may be loaded for you. The Intel
module manages all the sub modules, you do not have to worry about it.

.. note::

   - When unloading modules, only unload those that you have loaded.
     The others are done automatically from master modules.
   - Modules is a work in progress, and we will be improving their
     uses and making which modules you load more clear.

Loading Modules in batch jobs
-----------------------------

Any modules that you loaded when building your codes needs to be
loaded when your job runs as well. This means that you must put the
same module commands in your batch scripts that you ran before
building your code.

Modules with sh, bash, and ksh scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to the way the POSIX standard is defined for bash, sh, and ksh you
**MUST** add the ``-l`` option (that is a lowercase L) to the shebang
(e.g. ``#!/bin/sh``) line at the top of your script for all sh, bash,
or ksh batch scripts. For example:

.. code-block:: shell

   #!/bin/ksh -l

   module load intel
   module load impi

   srun -n 12 /xhpl

Failure to use ``-l`` will cause the module commands to fail and your
job will not run properly and may crash in hard to diagnose ways.

Additional Documentation on Lua modules
---------------------------------------

Refer to the `LMOD documentation
<https://lmod.readthedocs.io/en/latest/>`_ for more detailed
information on Lua module utility.

Using MPI
=========

Loading the MPI module
----------------------

There are two MPI implementations available on Hera: Intel MPI and
MVAPICH2. We recommend one of the following two combinations:

-  IntelMPI with the Intel compiler
-  MVAPICH2 with the PGI compiler.

At least one of the MPI modules must be loaded before compiling and
running MPI applications. These modules must be loaded before
compiliing applications as well in your batch jobs before executing a
parallel job.

Working with Intel Compilers and IntelMPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At least one of the MPI modules must be loaded before compiling
and running MPI applications. This is done as follows:

.. code-block:: shell

   $ module load intel impi

Compiling and Linking MPI applications with IntelMPI
""""""""""""""""""""""""""""""""""""""""""""""""""""

For the primary MPI library, IntelMPI, the easiest way to compile
applications is to use the appropriate wrappers: mpiifort, mpiicc, and
mpiicpc.

.. code-block:: shell

   $ mpiifort -o hellof hellof.f90
   $ mpiicc -o helloc helloc.c
   $ mpiicp -o hellocpp hellocpp.cpp

.. note::

   Please note the extra "i" in ``mpiifort``. ``mpiicc``, and
   ``mpiicp`` commands.

Launching MPI applications with IntelMPI
""""""""""""""""""""""""""""""""""""""""

For instructions on how to run MPI applications please refer to
:ref:`Running <slurm-running-a-job>` and :ref:`Monitoring Jobs
<slurm-monitoring-jobs>`.

Launching an MPMD application with intel-mpi-library-documentation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For instructions on how to run MPI applications please refer to
:ref:`Running <slurm-running-a-job>` and :ref:`Monitoring Jobs
<slurm-monitoring-jobs>`.

Launching OpenMP/MPI hybrid jobs with IntelMPI
""""""""""""""""""""""""""""""""""""""""""""""

For instructions on how to run MPI applications please refer to
:ref:`Running <slurm-running-a-job>` and :ref:`Monitoring Jobs
<slurm-monitoring-jobs>`.

Note about MPI-IO and Intel MPI
"""""""""""""""""""""""""""""""

Intel MPI doesn't detect the underlying file system by default when
using MPI-IO. You have to pass the following variables on to your
application:

.. code-block:: shell

   export I_MPI_EXTRA_FILESYSTEM=on
   export I_MPI_EXTRA_FILESYSTEM_LIST=lustre

Additional documentation on Intel MPI
"""""""""""""""""""""""""""""""""""""

The `Intel documentation library
<https://www.intel.com/content/www/us/en/developer/tools/documentation.html>`_
has extensive documentation, the following are a list of specific
documents that may be useful.

* `Intel MPI 5: <https://www.intel.com/content/www/us/en/developer/tools/documentation.html?f:@stm_10184_en=%5BIntel%C2%AE%20MPI%20Library%5D>`_
* `Intel PSM documentation
  <https://www.intel.com/content/dam/support/us/en/documents/network-and-i-o/fabric-products/OFED_Host_Software_UserGuide_G91902_06.pdf>`_.
  is very helpful for troubleshooting and turning purposes. This is
  because Intel MPI is based on the PSM layer.

Using PGI and mvapich2
----------------------

At least one of the MPI modules must be loaded before compiling
and running MPI applications. This is done with as follows:

.. code-block:: shell

   module load pgi mvapich2

Compiling and Linking MPI applications with PGI and MVAPICH2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When compiling with the PGI compilers, please use the wrappers:
``mpif90``, ``mpif77``, ``mpicc``, and ``mpicpp``.

.. code-block:: shell

   $ mpif90 -o hellof hellof.f90
   $ mpicc -o helloc helloc.c
   $ mpicpp -o hellocpp hellocpp.cpp

Launching MPI applications with MVAPICH2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For instructions on how to run MPI applications please refer to
:ref:`Running <slurm-running-a-job>` and :ref:`Monitoring Jobs
<slurm-monitoring-jobs>`.

Launching OpenMP/MPI hybrid jobs with MVAPICH2 (TBD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For instructions on how to run MPI applications please refer to
:ref:`Running <slurm-running-a-job>` and :ref:`Monitoring Jobs
<slurm-monitoring-jobs>`.

Additional documentation on using MVAPICH2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the `MVAPICH User Guide
<https://mvapich.cse.ohio-state.edu/userguide/>`_.

Tuning MPI (TBD)
----------------

Several options can be used to improve the performance of MPI jobs.

Profiling my MPI application with Intel MPI
-------------------------------------------

Add the following variables to get profiling information from your runs:

.. tab-set::

   .. tab-item:: bash
      :sync: bash

      .. code-block:: shell

         export I_MPI_STATS=<num>      # Can choose a value up to 10
         export I_MPI_STATS_SCOPE=col  # Statistics for collectives only

   .. tab-item:: csh
      :sync: csh

      .. code-block:: shell

         setenv I_MPI_STATS <num>      # Can choose a value up to 10
         setenv I_MPI_STATS_SCOPE col  # Statistics for collectives only

The Intel runtime library has the ability to bind OpenMP threads to
physical processing units. The interface is controlled using the
KMP_AFFINITY environment variable. Thread affinity can have a dramatic
effect on the application speed. It is recommended to set
``KMP_AFFINITY=scatter`` to achieve optimal performance for most
OpenMP applications. Review the information is on the `Intel
documentation library`_.

Intel Trace Analyzer
^^^^^^^^^^^^^^^^^^^^

Intel Trace Analyzer (formerly known as Vampir Trace) can be used for
analyzing and troubleshooting MPI programs. Please refer to the
`documentation
<https://www.intel.com/content/www/us/en/docs/trace-analyzer-collector/get-started-guide/2021-4/overview.html>`_.
Even though we have modules created for "itac" for this utility, it
may better to follow the instructions from the link above as the
instructions for more recent versions may be different than when we
created the module.

Debugging Codes
===============

Debugging Intel MPI Applications
--------------------------------

When troubleshooting MPI applications using Intel MPI, it may be
helpful if the debug versions of the Intel MPI library are used. To do
this,  use one of the following:

.. code-block:: shell

   $ mpiifort -O0 -g -traceback -check all -fpe0 -link_mpi=dbg ...             # if you are running non-multithreaded application
   $ mpiifort -O0 -g -traceback -check all -fpe0 -link_mpi=dbg_mt -openmp ...  # if you are running multi-threaded application

Using the ``-link_mpi=dbg`` makes the wrappers use the debug versions
of the MPI library, which may be helpful in getting additional
traceback information.

In addition to compiling with the options mentioned above, you may be
able to get some additional trace back information and core files if
you change the core file size to be unlimited (the default value for
core file is zero; hence call filed generation is disabled). In order
to enable it you need to have the following in your shell
initialization files in your home directory (the file name and the
syntax depends on your login shell):

.. tab-set::

   .. tab-item:: bash
      :sync: bash

      .. code-block:: shell

         ulimit -c unlimited

   .. tab-item:: csh
      :sync: csh

      .. code-block:: shell

         limit coredumpsize unlimited

Application Debuggers
---------------------

A GUI based debugger named DDT by Linary is available on Hera. Linaro
has `detailed documentation
<https://docs.linaroforge.com/23.1.2/html/forge/index.html>`_.

.. note::

   Since DDT is GUI debugger, interactions over a wide area network
   can be extremely slow. You may want to consider using a Remote
   Desktop which in our environment is X2GO as `documented
   <https://heradocs.rdhpcs.noaa.gov/wiki/index.php/Setting_up_and_using_x2go.>`__

Invoking DDT on Hera with Intel IMPI
------------------------------------

Getting access to the compute resources for interactive use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For debugging you will need interactive access to the desired set of
compute nodes using salloc with the desired set of resources:

.. code-block:: shell

   $ salloc --x11=first -N 2 --ntasks=4 -A <project> -t 300 -q batch

At this point you are on a compute node.

Load the desired modules
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   $ module load intel impi forge


The following is a temporary workaround that is currently needed until
it is fixed by the vendor.

.. tab-set::

   .. tab-item:: bash
      :sync: bash

      .. code-block:: shell

         $ export ALLINEA_DEBUG_SRUN_ARGS "%jobid% --gres=none --mem-per-cpu=0 -I -W0 --cpu-bind=none"

   .. tab-item:: csh
      :sync: csh

      .. code-block:: shell

         $ setenv ALLINEA_DEBUG_SRUN_ARGS "%jobid% --gres=none --mem-per-cpu=0 -I -W0 --cpu-bind=none"

Launch the application with the debugger
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   % ddt srun -n 4 ./hello_mpi_c-intel-impi-debug

This will open GUI in which you can do your debugging.
Please note that by default it seems to save your current
state (breakpoints, etc. are saved for your next debugging
session).

Using DDT
^^^^^^^^^

Some things should be intuitive, but we
recommend you look through the vendor documentation links
shown above if you have questions.

Profiling Codes
===============

Linaro Forge
------------

Linaro Forge allows easy profiling of applications. Very brief
instructions are included below.

- Compile with the debug flag (usually ``-g``
- Do not move your source files; the path is hardwired
  and will not found if relocated
- Load the *forge* module with ``module load forge``
- Run by prefixing with ``map --profile`` before the launch
  command

.. code-block:: shell

   #SBATCH ...
   #SBATCH ...

   module load intel impi forge

   map --profile mpirun -np 8 ./myexe

Then submit the job as you normally do. Once the job has completed,
you should file ``*.map`` files in your directory.

You have to view those files using the allinea ``map``
utility:

.. code-block:: shell

   module load forge         # If not already loaded
   map <map_file>.map

The above command will bring up a graphical viewer to view
your profile

Perf-report is another tool that provides the profiling
capability.

.. code-block:: shell

   perf-report srun ./a.out

TAU
---

The TAU Performance System® is a portable profiling and
tracing toolkit for performance analysis of parallel
programs written in Fortran, C, C++, Java, Python. Supports
application use of MPI and/or OpenMP. Also supports GPU.
Portions of the TAU toolkit are used to instrument code at
compile time. Environment variables control a number of
things at runtime. A number of controls exist, permitting
users to:

-  specify which routines to instrument or to exclude
-  specify loop level instrumentation
-  instrument MPI and/or OpenMP usage
-  throttle controls to limit overhead impact of small, high
   frequency called routines
-  generate event traces
-  perform memory usage monitoring

The toolkit includes the Paraprof visualizer (a Java app)
permitting use on most desk and laptop systems (Linux,
MacOS, Windows) for viewing instumentation data. The 3D
display can be very useful. Paraprof supports the creation
of user defined metrics based on the metrics directly
collected (ex: FLOPS/CYCLE).

The event traces can be displayed with the Vampir, Paraver,
or JumpShot tools.

Quick-start Guide for TAU
^^^^^^^^^^^^^^^^^^^^^^^^^

The Quick-start Guide for TAU only addresses basic usage. Please
keep in mind that this is an evolving document!

Find the Quick Start `here <https://heradocs.rdhpcs.noaa.gov/wiki/index.php?title=Quick-start_guide>`__

Tutorial slides for TAU
^^^^^^^^^^^^^^^^^^^^^^^

A set of slides presenting a recipe approach to beginning
with Tau is available `here <https://drive.google.com/a/noaa.gov/file/d/0B6Oipp_vs9tlMzcybEhXeUs2UjQ/view?usp=sharing>`__

MPI and OpenMP support
^^^^^^^^^^^^^^^^^^^^^^

TAU build supports profiling of both MPI and OpenMP applications.

The Quick-start Guide mentions using
``Makefile.tau-icpc-papi-mpi-pdt``. This supports profiling of MPI
applications. You must use
``Makefile.tau-icpc-papi-mpi-pdt-openmp-opari`` for OpenMP profiling.
``Makefile.tau-icpc-papi-mpi-pdt-openmp-opari`` can be used for either
MPI or OpenMP or both.

Managing Contrib Projects
=========================

Overview of Contrib Package
---------------------------

The system staff do not have the resources to maintain every piece of
software requested. There are also cases where developers of the
software are the system users, and putting a layer in between them and
the rest of the system users is inefficient. To support these needs,
we have developed a ``/contrib`` package process. A ``/contrib``
package is one that is maintained by a user on the system. The system
staff are not responsible for the use or maintenance of these
packages.

Responsibilities of a Contrib Package Maintainer
------------------------------------------------

Maintainers are expected to:

-  Follow the naming conventions and guidelines outlined in
   this document
-  Apply security updates as quickly as possible after they
   become availble
-  Update software for bug fixes and functionality as users
   request
-  Respond to user email requests for help using the
   software

Guidelines for Contrib Packages
-------------------------------

- The package should be a single program or toolset.
- We want to prevent having a single directory being a repository for
  many different packages. If you support multiple functions, please
  request multiple packages
- The package may have build dependencies on other packages, but it
  must otherwise be self-contained
- The package may not contain links to files in user or project
  directories.
- We expect each package to be less than 100MB. If you need more,
  please tell us when you request your package. We can support larger
  packages but we need to monitor the space used.
- We expect each package to have less than 100 files. If you need
  more, please tell us when you request your package.

Requesting to be a Contrib Package Maintainer
---------------------------------------------

If you wish to maintain a package in contrib, please open a :ref:`help
request <getting_help>` with:

-  a list of the packages you wish to maintain
-  justification why each is needed
-  the user who will be maintaining the package.

In certain cases, multiple users can manage a package,and
unix group write permissions may be granted for the
directory. In that case, specify the unix group that will be
maintaining the package.

Managing a Contrib Package
--------------------------

After your request has been approved to use space in the
``/contrib`` directory, two directories will be created for you:

* ``/contrib/$MYDIR``
* ``/contrib/modulefiles/$MYDIR``

This is where you will install your software for this package and
optionally install a module to allow users to load the environmental
settings necessary to use this package. The variable ``$MYDIR`` is the
name of the ``/contrib`` package you requested.

The directory convention of ``/contrib`` is designed to match
that of ``/apps``. This means that one piece of software goes
into a subdirectory under the ``/contrib`` level. If you want to
manage multiple package, please request multiple ``/contrib``
package. You can do this all at one time when submitting
your request to the Help System.

Contrib Package Directory Naming Conventions
--------------------------------------------

When installing software into your ``/contrib`` directory, first
determine if this is software that should be versioned (multiple
versions may exist at one time) or unversioned (there will only ever
be one version installed, and upgrade will overwrite the existing
software). For verisoned software, please install it into a
subdirectory of your package that is named after the version number.
For supporting multiple versions of software the install path should
be ``/contrib/$MYDIR/$VER``, where ``$MYDIR`` is the directory
assigned to you and $VER is the version number. 

So if your package is named ferret, and you are installing the version
3.2.6, the software should be installed in ``/contrib/ferret/3.2.6``

For supporting un-versioned software, just install the software
directly into your package directory ``/contrib/$MYDIR/``.

Providing Modules to Access Contrib Installed Software
------------------------------------------------------

For each contrib package, a corresponding directory will be
created for modules. The base directory name is
``/contrib/modulefiles``. Each package will have a
subdirectory created named after the package. For example,
for the ferret package, there will also be a directory
created named ``/contrib/modulefiles/ferret``

The ``/contrib/modulefiles`` directory will already be on
the modules path by default, so all users will be able to
see the modules when they run module list. Modules should
follow the same naming convention as the directories that
contain the software. Use some name that represents what it
is (ex: tools or dat). For versioned software, the name of
the module file should be the version number ($VER). See
below for information on how to create modules.

Creating Modules for Contrib Packages
-------------------------------------

There are example modules found in
``/contrib/modulefiles.example/ferret``

Please use those as a template. Contrib package maintainers
must follow these conventions:

-  Modules must display the notice when loaded providing
   contact information on how to get help.
-  Module naming convention should be based on the version
   number of the software.
-  Please ask questions through the Help System regarding
   how to construction modules.

Specifying a Default Module
---------------------------

If you have multiple versions of a package installed, it is
good practice to set which one is the default for the user.
This way, the user does not have to explicitly specify which
version they want to load. This is done by using a file
called .version that is placed in the module directory that has the format:

.. code-block:: tcl

   #%Module
   ##
   ## version file for default module version
   #
   set ModulesVersion      "<version>"

Where ``<version>`` is the desired default version.

Fine Grain Architecture (FGA) System
====================================

The Fine Grain Architecture (FGA) system has been installed
as an addition to Hera to facilitate experimentation with
emerging architectures. In addition to the traditional
processors, each compute node on the FGA system has multiple
GPUs on each node.

The part of the system that doesn't include the GPUs has
been generally referred to as the Traditional Computing
Architecture (TCA) and these two abbreviation TCA and FGA
will be used in this document to refer to these two systems.

System Information
------------------

-  The FGA system consists of a total of 100 nodes (named
   tg001 through tg100)
-  Each node has two 10 core Haswell processors (20 cores
   per node, referred to as Socket0 and Socket1)
-  Each node has 256 GB of memory
-  Each node has 8 Tesla P100 (Pascal) GPUs.

* GPUs 0-3 are connected to Socket0, and
* GPUs 4-7 are connected to Socket1
* The interconnect fabric is a fat tree network, made up of 1 Mellanox Connect-X 3 IB card connected to Socket1
* The FGA system has access to all the same file systems that TCA has

Please note that the network fabric on the FGA system has
the Mellanox IB cards which are different from the regular
Hera (or TCA) which has Intel TrueScale IB cards; this
distinction becomes important because the kernel running on
these FGA nodes is different from the TCA.

Just as an example about how this may impact users,
depending on the application it may be necessary to compile
your application on a FGA compute node by getting access to
an interactive compute node in the "fge" queue.

Getting an allocation for FGA resources
---------------------------------------

All projects with an allocation on Hera have windfall access to FGA
resources. All FGA projects (RDARCH portfolio) have windfall access to
Hera TCA resources. We are soliciting project requests for compute
allocations on the FGA system.

Users interested in an allocation on the fine-grain
augmentation may request an FGA allocation by sending a
couple of paragraphs (through their PIs if they are not a
PI) to the :ref:`help system <getting_help>`.

The paragraphs should contain the following information:

-  The number of node-hours requested.
-  Disk space (in terabytes) requested.
-  A brief description of the project in terms of science
   objectives and computer science objectives.
-  Planned way to exploit (or learning to exploit) the GPUs.

Note that there are approximately 64,000 node-hours
(1,270,000 core-hours) available. Since the intent is to use
an entire node (including the GPUs) only full node will be
available for allocation (although the bookkeeping will be
done in core-hours).

Using FGA resources without an allocation
-----------------------------------------

Users that do not have allocations on the FGA system will
have access to the FGA system at windfall priority.  Which
means users will be able to submit jobs to the system, but
they will only run when the resources are not being used by
projects that do have an FGA allocation. This is helpful for
users who are in interested in exploring the GPU resources
for their applications. To use the system in this mode
please submit the jobs to the fgewf partition and windfall
QoS by including the following:

.. code-block:: shell

      sbatch -p fgewf -q windfall ...

User Environment
----------------

Since the FGA is part of Hera, there are no separate login
nodes for using the FGA. When you log in to Hera you will be
connected to one of the front end nodes on Hera.

There are however some additional software packages and
their associated modules that are useful only on the FGA. A
couple of examples of this are cuda and mvapich2-gdr
libraries.

Compiling and Running Codes on the FGA
--------------------------------------

Please keep in mind that the software stacks on the FGA
machines are slightly different from regular Hera TCA nodes
(including the FE nodes) as mentioned above. This is because
the TCA and FGA nodes have different network cards which
necessitates that we have different images for these two
systems.

.. note::

   We recommend that compilation be done for FGA applications
   only on a compute node after obtaining a shell on one of the
   FGA compute nodes by submitting an interactive batch job to
   the *fge* or the *fgews* QoS.

Compiling and Running Codes Using CUDA
--------------------------------------

Compilation for non-MPI applications may be done either on
the front-ends or on compute nodes. But generally we
recommend compiling on an FGA compute node.

The following module will have to be loaded before compiling
and executing cuda programs:

.. code-block:: shell

   $ module load cuda

Generally you should use the latest cuda available

.. note:: We have limited experience with cuda.

The following flags were seen in sample codes
for compiling codes for the Pascal GPUs

.. code-block:: shell

   $ nvcc -gencode arch=compute_60,code=sm_60 mycode.cu

Compiling and Running Codes Using Intel MPI
-------------------------------------------

If you're using Intel MPI (with or without cuda; see the
note above if you're using cuda), compilation may be done on
the front-ends or on the computes nodes in an
interactive-batch job. But we would still recommend
compiling on an FGA compute node by submitting an
interactive batch job to the "fge" queue.

Please load the following modules before compilation and
also load these modules in the batch job before execution:

.. code-block:: shell

   $ module load intel impi
   $ mpiicc -o mycexe mycode.c
   $ mpiifort -o myfxex mycode.f90

.. note::

   Specific versions are listed only as examples; you
   can load any of the available versions

In addition, the following environment variables will have
to be set in the job file before execution (using the syntax
appropriate for the shell you are using):

.. tab-set::

   .. tab-item:: bash
      :sync: bash

      .. code-block:: shell

         $ module load intel impi
         $ export I_MPI_FABRICS shm:ofa
         $ srun ./myexe

   .. tab-item:: csh
      :sync: csh

      .. code-block:: shell

         $ module load intel impi
         $ setenv I_MPI_FABRICS shm:ofa
         $ srun ./myexe

This is necessary because the FGA nodes have Mellanox IB
cards as opposed to the Intel IB cards as in the regular
Hera nodes. Because of this difference in hardware the
software is also different on the FGA nodes. The FGA nodes
do not support the TMI fabric setting which is the default
on the regular Hera nodes.

Compiling and Building Codes Using mvapich2-gdr Library
-------------------------------------------------------

The MVAPICH2-GDR (GDR stands for GPUDirect RDMA) from Ohio
State University is available for experimentation and
testing on the FGA nodes.

.. note:: 

   We recommend that compilation be done for FGA applications
   only on a compute node after obtaining a shell on one of the
   FGA compute nodes by submitting an interactive batch job to
   the *fge* or the *fgedebug* queue.

Since the wait times for the fge queue are fairly short it
should be fine to use just the regular "fge" queue.
You need to load the following modules:

.. code-block:: shell

   $ module load intel cuda mvapich2-gdr    # Please consider using the latest versions of these
   $ mpif90 -o myfort.exe myfortcode.f90 -L$CUDALIBDIR -lcuda -lcudart
   $ mpicc -o myc.exe    myccode.c

In addition to loading the modules mentioned above, at
execution time you need to set the following environment
variables in your job file:

.. code-block:: shell

   $ module load intel cuda mvapich2-gdr
   $ env LD_PRELOAD=$MPIROOT/lib64/libmpi.so
   $ mpirun -np $PBS_NP ./myexe

.. note::

   By default the MVAPICH2-GDR lib will use GDRCOPY If for some reason
   you don't want to use it, set the the environment variable
   ``MV2_USE_GPUDIRECT_GDRCOPY=0``.

Compiling and Building Codes Using OpenMPI
------------------------------------------

The OpenMPI implimentation of MPI is available for
experimentation and testing on the FGA nodes. The current
installed version is the one that came with the PGI
compiler, so PGI examples are shown below.

You need to load the following modules:

.. code-block:: shell

   $ module load pgi cuda openmpi     # Please consider loading the latest versions of these
   $ mpif90 -o myfort.exe myfortcode.f90 -L$CUDALIBDIR -lcuda -lcudart
   $ mpicc  -o myc.exe myccode.c

In addition to loading the modules mentioned above, at
execution time you need to set the following environment
variables in your job file:

.. code-block:: shell

   $ module load pgi cuda openmpi # Please consider loading the latest versions of these
   $ mpirun -np $PBS_NP -hostfile $PBS_NODEFILE ./myexe

The following link has additional information on using OpenMPI,
particularly for `CUDA enabled applications
<https://www.open-mpi.org/faq/?category=runcuda>`__

Compiling codes with OpenACC directives on Hera
-----------------------------------------------

OpenACC directive based programming is available with the
PGI compilers. It is best to load the most recent PGI
compiler available for this. The example below shows how to
compile a serial program that has OpenACC directives:

.. code:: shell

   $ module load pgi cuda        # Please consider loading the latest versions of these
   $ pgf90 -acc -ta=nvidia,cc60,nofma -Minfo=accel -Msafeptr myprog.f90

Compiling MPI codes with OpenACC directives on Hera
---------------------------------------------------

We have limited experience of using these new technologies, so the
best we can do with this point is point you to the `web resources
<https://developer.nvidia.com/legacy-pgi-support>`__ The following link
has a presentation on some advanced topics on using `multiple GPUs
<https://on-demand.gputechconf.com/gtc/2016/webinar/openacc-course/Advanced-OpenACC-Course-Lecture2--Multi-GPU-20160602.pdf>`__

Submitting Batch Jobs to the FGA System
---------------------------------------

Users that have FGE specific allocation they can submit jobs
to the *fge* partition. Users that don't have an FGE
specific allocation can submit to the GPU nodes by
submitting to the *fgewf* partition and will run with
windfall priority.

One thing to keep in mind is that unlike the TCA, the
FGA nodes have a maximum of 20 cores per node (Hera TCA has
24 cores per node).

Hints on Rank Placement/Performance Tuning
------------------------------------------

.. NOTE::

   This section is included below just as a
   suggestion and is being updated as we learn more. Please
   note that the following section seems to be applicable only
   to Intel MPI.

Please keep in mind that there are
4 GPUs connected to the first socket and 4 GPUs connected to
the second socket.
For best performance it will be necessary to pin the MPI
processes such that they're not moving from core to core on
the node during the run.

First a simple script for pinning in a straightforward way
is shown below, followed by a couple of examples that were
modified from actual examples used in the benchmarking run:

.. code-block:: shell

   #!/bin/bash
   #set*x
   #
   # Assumptions for this script:
   #    1) The arguments are: exe and args to the executable
   #    2) Local rank 0 is using GPU0, etc.
   #    3) If "offset" environment variable is set, that is added to
   #   to lrank.  Generally avoid core 0;
   #      * Use an offset of  1 to place on first  socket
   #      * Use an offset of 11 to place on second socket
   #   Note:
   #First 4 GPUs connected to the first socket (cores 0-9)
   #Last  4 GPUs connected to the second socket (cores 10-19)

   let lrank=$PMI_RANK%$PBS_NUM_PPN
   let offset=${offset:-0} # set offset to 10 to place on second socket

   let pos=( $lrank + $offset)

   numactl*a*l*-physcpubind=$pos $*

The job can be launched by using:

.. code-block:: shell

   mpirun -np ${nranks} ./place.sh $exe

Based on the experience from the Cray benchmarking team, a
couple of examples of achieving the desired pinning are
shown below. In the first example, there are 4 MPI ranks on each
node, the goal is to pin the 4 ranks to the first socket and
specific cores; Also in this example each rank used 2
threads, and hence 2 cores are specified for each rank:

.. code-block:: shell

   #!/bin/bash
   #location of HPL
   HPL_DIR=`pwd`
   # set*x
   # Number of CPU cores
   CPU_CORES_PER_RANK=1

   export I_MPI_FABRICS=shm:OFA
   export I_MPI_PIN=disable
   export OMP_NUM_THREADS=$CPU_CORES_PER_RANK
   export MKL_NUM_THREADS=$CPU_CORES_PER_RANK

   #export CUDA_DEVICE_MAX_CONNECTIONS=12
   export CUDA_DEVICE_MAX_CONNECTIONS=12
   export CUDA_COPY_SPLIT_THRESHOLD_MB=1

   #APP=./xhpl.intel
   APP=$exe

   #lrank=$OMPI_COMM_WORLD_LOCAL_RANK
   let lrank=$PMI_RANK%4

   case ${lrank} in
   [0])
     export DEV_ID=0
     numactl*a*l*-physcpubind=2,6 $APP $*
     ;;
   [1])
     export DEV_ID=1
     numactl*a*l*-physcpubind=3,7 $APP $*
     ;;
   [2])
     export DEV_ID=2
     numactl*a*l*-physcpubind=4,8 $APP $*
     ;;
   [3])
     export DEV_ID=3
     numactl*a*l*-physcpubind=5,9 $APP $*
     ;;
   esac

The script above is used in the mpirun command; please note
that in the example above the name of the executable is
passed in the environment variable "exe". Just as a second example a similar script for pinning to the
specific cores on the second socket is shown below:

.. code-block:: shell

   #!/bin/bash
   #location of HPL
   HPL_DIR=`pwd`
   # set*x
   # Number of CPU cores
   CPU_CORES_PER_RANK=1

   export I_MPI_FABRICS=shm:OFA
   export I_MPI_PIN=disable
   export OMP_NUM_THREADS=$CPU_CORES_PER_RANK
   export MKL_NUM_THREADS=$CPU_CORES_PER_RANK

   #export CUDA_DEVICE_MAX_CONNECTIONS=12
   export CUDA_DEVICE_MAX_CONNECTIONS=12
   export CUDA_COPY_SPLIT_THRESHOLD_MB=1

   #APP=./xhpl.intel
   APP=$exe

   #lrank=$OMPI_COMM_WORLD_LOCAL_RANK
   let lrank=$PMI_RANK%4

   case ${lrank} in
   [0])
     export DEV_ID=4
     numactl*a*l*-physcpubind=12,16 $APP $*
     ;;
   [1])
     export DEV_ID=5
     numactl*a*l*-physcpubind=13,17 $APP $*
     ;;
   [2])
     export DEV_ID=6
     numactl*a*l*-physcpubind=14,18 $APP $*
     ;;
   [3])
     export DEV_ID=7
     numactl*a*l*-physcpubind=15,19 $APP $*
     ;;
   esac

Rank placement when using mvapich2
----------------------------------

For MVAPICH2 the following seems to work to place all the ranks on the
second socket. In this example, I'm using two nodes, and trying to run
eight tasks, and place them only| on the second socket on each node:

.. code-block:: shell

   $ setenv MV2_USE_GPUDIRECT_GDRCOPY 1
   $ setenv MV2_ENABLE_AFFINITY 1
   $ mpirun -np 8 -env MV2_CPU_MAPPING=16:17:18:19 ./$exe | sort -k 4
   Hello from rank 00 out of 8; procname = tg001, cpuid = 16
   Hello from rank 01 out of 8; procname = tg001, cpuid = 17
   Hello from rank 02 out of 8; procname = tg001, cpuid = 18
   Hello from rank 03 out of 8; procname = tg001, cpuid = 19
   Hello from rank 04 out of 8; procname = tg002, cpuid = 16
   Hello from rank 05 out of 8; procname = tg002, cpuid = 17
   Hello from rank 06 out of 8; procname = tg002, cpuid = 18
   Hello from rank 07 out of 8; procname = tg002, cpuid = 19

Please note that the two environment variables shown above
need to be set as currently they're not set by default. But
this one is subject to change and the module may be modified
in the future to set it by default.

For more details, see the `MVAPICH2 user guide
<https://mvapich.cse.ohio-state.edu/userguide/>`__.

Using Nvidia Multi-Process Service
----------------------------------

What is MPS
^^^^^^^^^^^

Multi-Process Service (MPS) is a service that allows
multiple tasks on a node to share a GPU.

On Hera for example, we have 20 cores on a node and only 8
GPU. Under normal circumstances, one could use just 8 MPI
tasks on each node, and have each of those tasks to
exclusively use 1 GPU.

Sometimes there may not be enough work from one task to keep
the GPU busy, in which case it may be beneficial to share
the GPU and have more MPI tasks on each node.

The performance benefits of taking this approach are very
much application dependent.

How do I use MPS
^^^^^^^^^^^^^^^^

In the example below, we describe the simplest use case and
we will update the documentation as we gather more
experience. For the simplest case, we will consider running an MPI
application on just one node after getting access to a FGA
compute node by submitting an interactive batch job to the
fge queue.

Assuming you have obtained an interactive compute node as
mentioned above:

- Load the necessary modules. The MPS services available
  after the cuda module is loaded:

   .. code-block:: shell

      $ module load intel/16.1.150 cuda/8.0 mvapich2-gdr/2.2-3-cuda-8.0-intel

- Start the MPS daemon:

   .. code-block:: shell

      $ setenv CUDA_MPS_LOG_DIRECTORY /tmp/nvidia-log
      $ setenv CUDA_MPS_PIPE_DIRECTORY /tmp/nvidia-pipe
      $ nvidia-cuda-mps-control* -d

- Confirm that MPS daemon is running

  .. code-block:: shell

      $ ps -elf | grep nvidia-cuda-mps-control | grep -v grep
      1 S User.Id  47724      1  0  80   0*  2666 poll_s 16:56 ?        00:00:00 nvidia-cuda-mps-control -d

- You can run some of the MPS commands.

  Please keep in mind that MPS does not have a command prompt,
  so typically you run the MPS commands as shown below:

  .. code-block:: shell

   $ echo get_server_list | nvidia-cuda-mps-control
   Server 0 not found

  Then you run your application like you normally would.
  At the end of your session, terminate the deamon by running the command:

  .. code-block:: shell

      $ echo quit | nvidia-cuda-mps-control

Documentation for MPS
^^^^^^^^^^^^^^^^^^^^^

For additional details see the `Overview
<https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf>`__

Compiling and Building Codes With The Cray Programming Environment
------------------------------------------------------------------

A custom built version of mvapich2 must be used when compiling and running with
the Cray Programming Environment (CrayPE). To run an MPI
program using the Cray
Programming Environment (CrayPE), you must first set up
the proper environment.
This has been rolled into a single ``module load`` command
that brings in all required
modules:

.. note::

   Currently because of a compatibility issue between
   regular Modules and Lmod (which Hera uses), the CrayPE
   modules don't work with tcsh. Hence all of these examples
   are shown with bash.

.. code-block:: shell

   $ bash -l
   $ module purge
   $ module load craype-hera
   $ module list

   Currently Loaded Modules:
     1) craype-haswell   7) cray-libsci/17.11.1
     2) craype-network-infiniband         8) PrgEnv-cray/1.0.2
     3) craype/2.5.13         9) cray-libsci_acc/17.03.1
     4) cce/8.6.410) craype-accel-nvidia60
     5) cudatoolkit/8.0.44   11) perftools-base/6.5.2
     6) mvapich2_cce/2.2rc1.0.3_noslurm  12) craype-hera/8.6.4

Then compile the program. The compiler drivers are

:cc: c code
:ftn: fortran
:CC: c++ code

.. note::

   Do not use the "mpi" drivers associated
   with the mvapich2 library.

.. note::

   The sample programs and scripts used in the examples below can be
   found in the directory on Hera:
   ``/apps/local/examples/craype/XTHI_SIMPLE``

.. code-block:: shell

   $ cc -homp -o xthi xthi.c  # (-homp is default, so not explicitly needed)

To run the executable, secure the appropriate compute
node(s) and set the environment:

.. code-block:: shell

   $ module load craype-hera
   $ export LD_LIBRARY_PATH=${CRAY_LD_LIBRARY_PATH}:${LD_LIBRARY_PATH}
   $ cc -homp -o xthi xthi.c
   $ mpirun -env OMP_NUM_THREADS 1 -n 4 -machinefile $PBS_NODEFILE ./xthi
   Warning: Process to core binding is enabled and OMP_NUM_THREADS is set to non-zero (1) value
   If your program has OpenMP sections, this can cause over-subscription of cores and consequently poor performance
   To avoid this, please re-run your application after setting MV2_ENABLE_AFFINITY=0
   Use MV2_USE_THREAD_WARNING=0 to suppress this message
   Hello from rank 0, thread 0, on sg001. (core affinity = 20)
   Hello from rank 1, thread 0, on sg001. (core affinity = 21)
   Hello from rank 2, thread 0, on sg002. (core affinity = 20)
   Hello from rank 3, thread 0, on sg002. (core affinity = 21)

All MPI ranks are running on unique cores in the fge
queue. Alternatively, if you want
to place ranks on specific cores, you can use the
``MV2_CPU_MAPPING`` environment variable:

.. code-block:: shell

   $ mpirun -env OMP_NUM_THREADS 1 -env MV2_CPU_MAPPING=0:10 -n 2 -machinefile $PBS_NODEFILE ./xthi
   Warning: Process to core binding is enabled and OMP_NUM_THREADS is set to non-zero (1) value
   If your program has OpenMP sections, this can cause over-subscription of cores and consequently poor performance
   To avoid this, please re-run your application after setting MV2_ENABLE_AFFINITY=0
   Use MV2_USE_THREAD_WARNING=0 to suppress this message
   Hello from rank 1, thread 0, on sg001. (core affinity = 10)
   Hello from rank 0, thread 0, on sg001. (core affinity = 0)

Here, each rank is running on its own socket. If this strategy is used
with OpenMP threaded codes, all threads will be placed on the same
core as the master thread, leading to contention and reduced
performance.

.. code-block:: shell

   $ mpirun -env OMP_NUM_THREADS 4 -n 1 -machinefile $PBS_NODEFILE ./xthi
   Warning: Process to core binding is enabled and OMP_NUM_THREADS is set to non-zero (4) value
   If your program has OpenMP sections, this can cause over-subscription of cores and consequently poor performance
   To avoid this, please re-run your application after setting MV2_ENABLE_AFFINITY=0
   Use MV2_USE_THREAD_WARNING=0 to suppress this message
   WARNING: Requested total thread count and/or thread affinity may result in
   oversubscription of available CPU resources!  Performance may be degraded.
   Set OMP_WAIT_POLICY=PASSIVE to reduce resource consumption of idle threads.
   Set CRAY_OMP_CHECK_AFFINITY=TRUE to print detailed thread-affinity messages.
   Hello from rank 0, thread 2, on sg001. (core affinity = 0)
   Hello from rank 0, thread 0, on sg001. (core affinity = 0)
   Hello from rank 0, thread 3, on sg001. (core affinity = 0)
   Hello from rank 0, thread 1, on sg001. (core affinity = 0)

Each thread is placed on core.0 with the master thread. To avoid this
contention, the application must be launched with numactl like this
using in a script (r4.sh in the example below):

.. code-block:: shell

   #!/bin/bash
   HPL_DIR=`pwd`
   CPU_CORES_PER_RANK=4
   export OMP_NUM_THREADS=$CPU_CORES_PER_RANK
   export MV2_ENABLE_AFFINITY=0
   export OMP_WAIT_POLICY=PASSIVE
   APP=./xthi #-craype-silene #./xthi_test
   let lrank=$PMI_RANK%8
   echo "PMI_RANK: $PMI_RANK"
   echo "lrank:    $lrank"
   export I_MPI_EAGER_THRESHOLD=524288
   export OMP_WAIT_POLICY=active
   export OMP_SCHEDULE=dynamic,1
   export RANKS_PER_SOCKET=1
   export CUDA_COPY_SPLIT_THRESHOLD_MB=1
   export ICHUNK_SIZE=768
   export CHUNK_SIZE=2688
   export TRSM_CUTOFF=9990000
   export TEST_SYSTEM_PARAMS=1
   case ${lrank} in
   [0])
   #  export CUDA_VISIBLE_DEVICES=0
   #  numactl*a*l*-physcpubind=2,6 $APP
     numactl*a*l*-physcpubind=0,1,2,3 $APP
     ;;
   [1])
   #  export CUDA_VISIBLE_DEVICES=1
   #  numactl*a*l*-physcpubind=3,7 $APP
     numactl*a*l*-physcpubind=10,11,12,13 $APP
     ;;
   [2])
   #  export CUDA_VISIBLE_DEVICES=2
   #  numactl*a*l*-physcpubind=4,8 $APP
     numactl*a*l*-physcpubind=2 $APP
     ;;
   [3])
   #  export CUDA_VISIBLE_DEVICES=3
   #  numactl*a*l*-physcpubind=5,9 $APP
     numactl*a*l*-physcpubind=3 $APP
     ;;
   [4])
   #  export CUDA_VISIBLE_DEVICES=4
   #  numactl*a*l*-physcpubind=12,16 $APP
     numactl*a*l*-physcpubind=4 $APP
     ;;
   [5])
   #  export CUDA_VISIBLE_DEVICES=5
   #  numactl*a*l*-physcpubind=13,17 $APP
     numactl*a*l*-physcpubind=5 $APP
     ;;
   [6])
   #  export CUDA_VISIBLE_DEVICES=6
   #  numactl*a*l*-physcpubind=14,18 $APP
     numactl*a*l*-physcpubind=6 $APP
     ;;
   [7])
   #  export CUDA_VISIBLE_DEVICES=7
   #  numactl*a*l*-physcpubind=15,19 $APP
     numactl*a*l*-physcpubind=7 $APP
     ;;
   esac

In this case, we have a single node with two MPI ranks running each
spawning 4 OpenMP threads. The threads are placed such that each set
is running on its own socket:

.. code-block:: shell

   $ mpirun -env OMP_NUM_THREADS 4 -n 2 -machinefile $PBS_NODEFILE ./r4.sh
   PMI_RANK: 1
   lrank:    1
   PMI_RANK: 0
   lrank:    0
   Hello from rank 0, thread 0, on sg001. (core affinity = 0-3)
   Hello from rank 0, thread 3, on sg001. (core affinity = 0-3)
   Hello from rank 0, thread 2, on sg001. (core affinity = 0-3)
   Hello from rank 0, thread 1, on sg001. (core affinity = 0-3)
   Hello from rank 1, thread 0, on sg001. (core affinity = 10-13)
   Hello from rank 1, thread 1, on sg001. (core affinity = 10-13)
   Hello from rank 1, thread 2, on sg001. (core affinity = 10-13)
   Hello from rank 1, thread 3, on sg001. (core affinity = 10-13)

Using this as a template, it is easy to place ranks and
threads in many different ways. This
example only uses the lrank=0,1 case branches but the user
is encouraged to exeriment with
other placement strategies.

Some helpful web resources
--------------------------

- https://www.openacc.org/
- https://www.openacc.org/resources
- https://developer.nvidia.com/legacy-pgi-support
- https://stackoverflow.com/questions/tagged/openacc

Getting Help
------------

As with any Hera issue, open a :ref:`help request <getting_help>`.

Policies and Best Practices
===========================

Below is a list of policies that govern the use of the NESCC RDHPCS
computing systems. In RDHPCS CommonDocs, see:

*  `Usage and Software Support Policies
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Usage_and_Software_Support_Policies>`__
*  `Login (Front_End) Node Usage Policy
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Login_(Front_End)_Node_Usage_Policy>`__
*  `Cron Usage Policy
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Cron_Usage_Policy>`__
*  `Module Loading Best Practices
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Module_Loading_Best_Practices>`__
*  `Managing Packages in /contrib
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Managing_Packages_in_/contrib>`__
*  `Software Install Request Policy
   </index.php/Software_install_request_policy>`
*  `Protecting Restricted Data
   <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Protecting_Restricted_Data>`__
