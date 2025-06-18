.. _hera-user-guide:

***************
Hera User Guide
***************

.. image:: /images/Hera.jpg

Action Required
===============

.. attention::

   Migrate your data on Hera from ``/scratch[1,2]`` to ``/scratch[3,4]`` file systems, no later than **July 31, 2025!**

``/scratch[3,4]`` is now mounted on Hera, in addition to ``/scratch[1,2]``.
``/scratch[1,2]`` will be decommissioned in August, so you must migrate your
active data from ``/scratch[1,2]`` to ``/scratch[3,4]``. Important dates for
your data migration:

* ``/scratch[1,2]`` will be set to read only on **7/15/25**, plan to complete
  migrating your data to ``/scratch[3,4]`` by **7/31/25**.

* ``/scratch[1,2]`` is planned to be
  decommissioned (unmounted) at the **~8/5/25** NESCC maintenance downtime.


Here is the link to a `brief presentation
<https://docs.google.com/presentation/d/1bXH6hKE-vgn7k-CSp2aFWWlH4s5jhL5oKJ58QepFTxI/edit?slide=id.g30820fabc4a_16_0#slide=id.g30820fabc4a_16_0>`_
that should help you with your migration.

System Overview
===============

- Capacity of 3,270 trillion floating point operations per second – or
  3.27 petaFLOPS
- The Fine Grain Graphical Processing Units have a total capacity of
  2,000 trillion floating point operations per second, or 2.0
  petaFLOPS
- 45 million hours per month with 63,840 cores and a total scratch
  disk capacity of 18.5 Petabytes.

NESCC is also home to Niagara, a cloud-based computing resource. In
addition, Test and Development systems are available through NESCC for
system and application testing.

System Configuration
--------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * -
     - Hera
   * - CPU Type
     - Intel SkyLake
   * - CPU Speed (GHz)
     - 2.40
   * - Reg Compute Nodes
     - 1,328
   * - Cores/Node
     - 40
   * - Total Cores
     - 53,120
   * - Memory/Core (GB)
     - 96
   * - Peak FLOPS/Node
     - 12
   * - Service Code Memory (GB)
     - 187
   * - Total BigMem Nodes
     - 268
   * - BigMem Node Memory (GB)
     - 384
   * - CPU FLOPS (TFLOPS)
     - 2,672
   * - GPUs/Node
     - N/A
   * - Total GPUs
     - N/A
   * - GPU FLOPS/GPU
     - N/A
   * - Interconnect
     - HDR-100 IB
   * - Total GPU FLOPS (TFLOPS)
     - N/A



.. note::

   - The Skylake 6148 CPU has two AVX-512 units and hence a
     theoretical peak of 32 double precision floating point operations
     per cycle with a base clock rate for floating point operations of
     1.6 GHz.
   - Total FLOPS is a measure of peak, and doesn’t necessarily
     represent actual performance.
   - Juno is the Test and Development System. Users must be granted
     specific access to the system for use.


Hera Partitions
===============

To specify a partition, use the command `partition -p`. For example:

.. code-block:: shell

   sbatch -p batch ...

The following partitions are defined for Hera:

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Partition
     - QOS Allowed
     - Billable TRes per Core Performance Factor
     - Description
   * - hera
     - batch,windfall, debug, urgent, long
     - 165
     - General compute resource. **Default** if no partition is specified
   * - bigmem
     - batch,windfall, debug, urgent, long
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
   hera*
   service
   bigmem
   novel

An asterisk (*) indicates that default partition, where your job will be
submitted to if you do not specify a partition name at job submission.

**General compute jobs:** To assure the systems are used most efficiently,
specify the use of all general compute resource partitions. This allows the
batch scheduler to put your jobs on the first available resource.

Lustre File System Usage
========================

Lustre is a parallel, distributed file system often used to support
the requirements for high-performance I/O in large scale clusters by
supporting a parallel I/O framework that scales to thousands of nodes
and petabytes of storage. Lustre features include high-availability
and POSIX compliance.

On the RDHPCS Hera cluster there are two Lustre file systems available
for use: ``/scratch3`` and ``/scratch4``

The serial transfer rate of a single stream is generally greater than
1 GB/s but can easily increase to 6.5 GB/s from a single client, and
more than 10 GB/s if performed in a properly configured parallel
operation.

Lustre Volume and File Count
----------------------------

For efficient resource usage, Hera's ``/scratch3`` and ``/scratch4``
Lustre file systems have project based volume and file count quotas.
Each project has an assigned quota which is shared by all users on the
project. File count quotas are implemented to preserve the increased
performance of the 2-tier storage architecture, where the first 128 KB
of each file is stored on SSD and the remainder if any on HDD.
Historical data from Jet show that the average file count per GB is
~100. By default, projects on Hera are given a file count quota of 200
files per GB of volume quota or 100,000 files, whichever is higher.
Users will receive warning emails when their quota is exceeded. When
either the volume or file count quota is exceed by more than 1.2x,
writes will not be allowed.

Summary and detailed information on finding your project's disk volume
and file count quota and usage is found :ref: `here
<Getting_Information_about_your_Projects>`.

Volume Quota Increase
^^^^^^^^^^^^^^^^^^^^^

If you are approaching your quota, you should first delete old files
and/or move files to HPSS tape systems as appropriate. If more volume
is still needed, open a Help ticket to request a volume quota
increase. Send email to rdhpcs.hera.help@noaa.gov, with the subject
line Quota Increase, and a justification, including:

* Project name.
* Requested quota. Is the increase request temporary or permanent? If
  temporary, for how long?
* Justification, including an analysis of your workload detailing the
  volume needed


File Count Quota Increase
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are approaching your quota or your file count quota or are
running over 200 files/GB, you should first delete old small files. If
you want to keep them around but they are not accessed frequently, you
should tar up many small files into one big file. If you have an
exceptional situation and believe you need a quota increase, open a
Help ticket. Send email to rdhpcs.hera.help@noaa.gov that includes the
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

An OSS manages a small set of OSTs by controlling I/O access and
handling network requests to them.

An OST is a block storage device, often several disks in a RAID
configuration.

Hera Lustre Configuration
-------------------------

All nodes (login and compute) access the lustre file-systems mounted
at ``/scratch3`` and ``/scratch4``. Each user has access to one or
more directories based on the project which they are a member of, such
as:

.. code-block:: shell

   /scratch[3,4]/${PORTFOLIO}/${PROJECT}/${TASK}

where ``${TASK}`` is often, but not necessarily, the individual user's
login ID, as defined by the project lead.

The number of servers and targets on each of the two Hera file systems
is:

* 2 MDSs (active/active)
* 2 MDTs
* 16 OSSs (active/active, embedded in DDN SFA 18k storage controllers)
* 122 OSTs (106 are HDDs, 16 are SSDs)
* 9.1 PiB of usable disk space (*df*hP /scratch{3,4}*)

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

A file is split into segments and consecutive segments are stored on
different physical storage devices (OSTs).

Aligned vs Unaligned Stripes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aligned stripes is where each segment fits fully onto a single OST.
Processes accessing the file do so at corresponding stripe boundaries.
Unaligned stripes means that some file segments are split across OSTs.

.. _hera-progressive-file-layouts:

Progressive File Layouts
^^^^^^^^^^^^^^^^^^^^^^^^

The ``/scratch3`` and ``/scratch4`` file systems are enabled with a
feature called Progressive File Layouts (PFL), which is efficient for
the vast majority of use cases. It uses a single stripe count for
small files (reducing overhead) and increases the striping as the file
gets bigger (increasing bandwidth and balancing capacity), all without
any user involvement. These file systems are also augmented by a set
of SSD OSTs (described above) and with the PFL capability is further
optimized for small file performance. By default, smaller files are
stored completely in SSD, which further decreases random operation
latency and allows the HDDs to run more efficiently for streaming
reads and writes. The default configuration will automatically stripe
and place files in a generally optimal fashion to improve I/O
performance for varying file sizes, including the use of SSDs for
better small-file performance. The defaults also attempt to make the
best use of the SSD targets (which are faster, but have much less
capacity than HDDs). More details on PFL are available in the `Lustre
documentation <https://www.lustre.org/documentation/>`_.

.. Note::

   The PFL feature makes much of the information documented below
   regarding customized striping unnecessary.

Users should not need to adjust stripe count and size on ``/scratch3``
and ``/scratch4``.  With PFL enabled, setting your own stripe layout
may reduce I/O performance for your files and the overall I/O
performance of the file system. If you have already used ``lfs
setstripe`` commands documented below, you should probably remove the
striping that may have already been set.

Here are the steps you should follow if you have any directories that
had explicitly set non-default striping:

#. Remove all ``lfs setstripe`` commands from your scripts.
#. Run the following command which changes the striping back to default
   for each of the directories on which you may have set striping:

   .. code-block:: shell

      $ lfs setstripe -d <dir>

#. Open a help ticket with the subject line
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
directories and will be inherited for all new subdirectories. Tracking
and enforcement includes maximum file count, not just capacity. To
check your usage details:

#. Look up your project ID number (not the name)
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
   $ lfs quota -p 10052 /scratch3
   Disk quotas for prj 10052 (pid 10052):
   Filesystem  kbytes   quota   limit   grace   files   quota   limit   grace
   /scratch3       4  1048576 1258291      *      1  100000  120000      *
   ("kbytes" = usage, "quota" = soft quota, "limit" = hard quota)

Finding Files
^^^^^^^^^^^^^

The ``lfs find`` command is more efficient than the standard ``find``,
and may be faster too. For example, to find fortran source files
accessed within the last day:

.. code-block:: shell

   $ lfs find . -atime -1 -name '*.f90'

Striping Information
^^^^^^^^^^^^^^^^^^^^

You can view the file striping layout with the command:

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
   working for you, submit a  help ticket to let us know and assist.

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
   parameters on your ``/scratch3`` or ``/scratch4`` files.

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
across one or two OSTs can degrade the performance of the entire Lustre
system by filling up OSTs unnecessarily. By striping a large file over
many OSTs, you increase bandwidth to access the file and can
benefit from having many processes operating on a single file
concurrently. If all large files accessed by all users are striped,
I/O performance levels can be enhanced for all users. Small files
should never be striped with large stripe counts, if they are striped
at all. A good practice is to make sure small files are written to a
directory with a stripe count of 1, effectively no striping.

Increase Stripe Count for Large Files
"""""""""""""""""""""""""""""""""""""

Set the stripe count of the directory to a large value.  This spreads
the reads/writes across more OSTs, balancing the load and data.

.. code-block:: shell

   $ lfs setstripe -c 30 /scratchN/your_project_dir/path/large_files/

Use a Small Stripe Count for Small Files
""""""""""""""""""""""""""""""""""""""""

Place small files on a single OST. Small files will then not be spread
out across OSTs.

.. code-block:: shell

   $ lfs setstripe -c 1 /scratchN/your_project_dir/path/small_files/

Parallel IO Stripe Count
""""""""""""""""""""""""

Single shared files should have a stripe count equal to, or a factor
of, the number of processes which access the file. If the number of
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

See :ref:`Installing Miniconda <installing-miniconda>` for
installation instructions.

.. warning::

   RDHPCS support staff does not have the available resources to
   support or maintain these packages. You will be responsible for the
   installation and troubleshooting of the packages you choose to
   install. Due to architectural and software differences some of the
   functionality in these packages may not work.

MATLAB
------

Information is available *TBD*

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
compute nodes is 48 (the number of virtual CPUs). It should
not be run as a serial job with the default thread number, as
the threaded program will affect other jobs on the same
node.

The number of threads needs to be set to 1 if a job is going to be
submitted as a serial job, which can be achieved by setting the
environment variable ``IDL_CPU_TPOOL_NTHREADS`` to 1, or setting it
with the CPU procedure in IDL: ``CPU, TPOOL_NTHREADS = 1``. If a job
requires larger than 10 GB memory, you should run the job on
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
open-source packages that extend the capabilities of R, has a complete
list of R packages as well as the packages for download.

Due to access restrictions from Hera to the CRAN repository, you
may need to download an R package to your local workstation first,
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

See :ref:`Modules <modules>`


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
compiling applications as well in your batch jobs before executing a
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

* `Intel MPI 5: <https://www.intel.com/content/www/us/en/docs/mpi-library/developer-guide-linux/2021-13/overview.html>`_
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

Profiling an MPI application with Intel MPI
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
OpenMP applications. For details, review the information in the `Intel
documentation library`_.

Intel Trace Analyzer
^^^^^^^^^^^^^^^^^^^^

Intel Trace Analyzer (formerly known as Vampir Trace) can be used for
analyzing and troubleshooting MPI programs. Please refer to the
`documentation <https://www.intel.com/content/www/us/en/developer/tools/documentation.html>`__.
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

A GUI based debugger named DDT by Linaro is available on Hera. Linaro
has `detailed documentation
<https://docs.linaroforge.com/23.1.2/html/forge/index.html>`_.

.. note::

   Since DDT is GUI debugger, interactions over a wide area network
   can be extremely slow. You may want to consider using a Remote
   Desktop which in our environment is :ref:`X2GO <x2go-remote-desktop>`.

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

- Compile with the debug flag
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
programs written in Fortran, C, C++, Java, and Python. It supports
application use of MPI and/or OpenMP, and also supports GPU.
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
MacOS, Windows) to view instrumentation data. The 3D
display can be very useful. Paraprof supports the creation
of user defined metrics based on the metrics directly
collected (ex: FLOPS/CYCLE).

The event traces can be displayed with the Vampir, Paraver,
or JumpShot tools.

Quick-start Guide for TAU
^^^^^^^^^^^^^^^^^^^^^^^^^

The Quick-start Guide for TAU only addresses basic usage. Please
keep in mind that this is an evolving document!

Find the Quick Start *TBD*

Tutorial slides for TAU
^^^^^^^^^^^^^^^^^^^^^^^

A set of slides presenting a recipe approach to beginning
with Tau is available *TBD*

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

A /contrib package is one that is maintained by a user on the system.
The system staff are not responsible for the use or maintenance of
these packages. See :ref:`Contrib <contrib>` for details.


