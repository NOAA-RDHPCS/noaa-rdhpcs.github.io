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

- Hera - A 760 Tflop Cray Compute Cluster high performance computing system
- HPSS - A 50 Petabyte IBM/Oracle hierarchical storage management system.

.. _hera-system-overview:

System Overview
===============

- Capacity of 3,270 trillion floating point operations per second – or 3.27
  petaflops
- The Fine Grain Graphical Processing Units have a total capacity of 2,000
  trillion floating point operations per second, or 2.0 petaflops
- 45 million hours per month with 63,840 cores and a total scratch disk capacity
  of 18.5 Petabytes.

NESCC is also home to Niagara, a cloud-based computing resource. In addition,
Test and Development systems are available through NESCC for system and
application testing.

System Configuration
--------------------

+---------------------+---------------+------------------+---------------+------------------+
|                     | Hera TCA      | Hera FGA         | Juno TCA      | Juno FGA         |
+=====================+===============+==================+===============+==================+
| CPU Type            | Intel SkyLake | Intel Haswell    | Intel SkyLake | Intel Haswell    |
+---------------------+---------------+------------------+---------------+------------------+
| CPU Speed           | 2.40 GHz      | 2.460 GHz        | 2.40 GHz      | 2.460 GHz        |
+---------------------+---------------+------------------+---------------+------------------+
| Reg Compute Nodes   | 1328          | 100              | 14            | 2                |
+---------------------+---------------+------------------+---------------+------------------+
| Cores/node          | 40            | 20               | 40            | 20               |
+---------------------+---------------+------------------+---------------+------------------+
| Total Cores         | 53,120        | 2000             | 560           | 40               |
+---------------------+---------------+------------------+---------------+------------------+
| Memory/Core         | 96 GB         | 256 GB           | 90 GB         | 256 GB           |
+---------------------+---------------+------------------+---------------+------------------+
| Peak Flops/node     | 12            | NA               | 12            | NA               |
+---------------------+---------------+------------------+---------------+------------------+
| Service Code Memory | 187 GB        | NA               | 187 GB        | NA               |
+---------------------+---------------+------------------+---------------+------------------+
| Total BigMem Nodes  | 268           | NA               | 268           | NA               |
+---------------------+---------------+------------------+---------------+------------------+
| BibMem Node Memory  | 384 GB        | NA               | 384 GB        | NA               |
+---------------------+---------------+------------------+---------------+------------------+
| CPU Flops           | 2672 TF       | 83.1 TF          | 28 TF         | 1.6 TF           |
+---------------------+---------------+------------------+---------------+------------------+
| GPUs/Node           | NA            | 8 P100           | NA            | 8 P100           |
+---------------------+---------------+------------------+---------------+------------------+
| Total GPUs          | NA            | 800              | NA            | 16               |
+---------------------+---------------+------------------+---------------+------------------+
| GPU Flops/GPU       | NA            | 4.7              | NA            | 4.7              |
+---------------------+---------------+------------------+---------------+------------------+
| Interconnect        | HDR-100 IB    | FDR-10 (40 Gbps) | HDR-100 IB    | FDR-10 (40 Gbps) |
+---------------------+---------------+------------------+---------------+------------------+
| Total GPU Flops     | NA            | 3760 TF          | NA            | 75 TF            |
+---------------------+---------------+------------------+---------------+------------------+

.. note::

    - The Skylake 6148 CPU has two AVX-512 units and hence a theoretical peak of 32
      double precision floating point operations per cycle with a base clock rate
      for floating point operations of 1.6 GHz.
    - Total flops is a measure of peak, and doesn’t necessarily represent actual
      performance.
    - Juno is the Test and Development System. Users must be granted specific access
      to the system for use.
    - The FGA part (the nodes with GPUs) are the same as what was on Theia; But the
      network has been upgraded to EDR.


Lustre File System Usage
==========


Lustre is a parallel, distributed file system often used to support the requirements for high-performance I/O in large
scale clusters by supporting a parallel I/O framework that scales to thousands of nodes and petabytes of storage. Lustre features include high-availability and POSIX compliance.

On the RDHPCS Hera cluster there are two Lustre file systems available for use, /scratch1 and /scratch2

The serial transfer rate of a single stream is generally greater than 1 GB/s but can easily increase to 6.5 GB/s from a single client, and more than 10 GB/s if performed in a properly configured parallel operation.

  .. rubric:: Lustre Volume and File Count

For efficient resource usage, Hera's /scratch1 and /scratch2Lustre file systems have project based volume and file countquotas. Each project has an assigned quota which is sharedby all users on the project. File count quotas are new andare implemented to preserve the increased performance of the2 tier storage architecture where the first 128 KB of eachfile is stored on SSD and the remainder if any on HDD.Historical data from Theia and Jet show that the averagefile count per GB is ~100. By default projects on Hera aregiven a file count quota of 200 files per GB of volume quotaor 100,000 files whichever is higher.
Users will receive warning emails when their quota isexceeded. When either the volume or file count quota isexceed by more than 1.2x, writes will not be allowed.
| 
Summary and detailed information on finding your project's disk volume and file count quota and usage is found at:  `Getting Information About Your  Projects <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_Information_About_Your_Projects_-_SLURM>`__

.. rubric:: Volume Quota Increase

If you are approaching your quota, the first step should beto delete old files and/or move files to HPSS tape systemsas appropriate. If more volume is still needed, as withprevious systems, volume quota increases are requested bysubmitting a Hera help ticket with a justification,including:

1. Project name.
2. Requested quota. Is the increase request temporary or permanent? If temporary, for how long?
3. Justification, including an analysis of your workload detailing the volume needed


.. rubric:: File Count Quota Increase

If you are approaching your quota or your file count quotaor are running over 200 files/GB, the first step should beto delete old small files. If you want to keep them aroundbut they are not accessed frequently, you should tar up manysmall files into one big files. If you have an exceptionalsituation and believe you need a quota increase, pleasestart a Hera help ticket including the followinginformation:

::

1. Project name.   
2. Justification, including an analysis of your workload detailing the files/GB needed.   
3. Requested quota. Is the increase request temporary or permanent? If temporary, for how long?


The request has to be approved by the project's PI (orPortfolio Manager), so it will save time if the requestcomes from the PI (or Portfolio Manager). Once requests areapproved by the PI (or Portfolio Manager) they will bereviewed by the Hera resource manager.

.. rubric:: Lustre

Lustre functionality is divided among four primarycomponents:

           * MDS - Metadata Server
           * MDT - Metadata Target
           * OSS - Object Storage Server
           * OST - Object Storage Target

An MDS is server that assigns and tracks all of the storagelocations associated with each file in order to direct fileI/O requests to the correct set of OSTs and correspondingOSSs.
An MDT stores the metadata, filenames, directories,permissions and file layout.
An OSS manages a small set of OSTs by controlling I/O accessand handling network requests to them.
An OST is a block storage device, often several disks in a RAID configuration.  

.. rubric:: Hera Lustre configuration

All nodes (login and compute) access the lustre file-systemsmounted at /scratch1 and /scratch2.
Each user has access to one or more directories based on theproject which they are a member of, such as:

.. code-block:: shell
    
    /scratch[1,2]/${PORTFOLIO}/${PROJECT}/${TASK}

...where ${TASK} is \**often but not necessarily*\* the individual user's login ID, as defined by the project lead. The number of servers and targets on *each* of the two Herafile systems is:

           * 2 MDSs (active/active)
           * 2 MDTs
           * 16 OSSs (active/active, embedded in DDN SFA18k storage   controllers)
           * 122 OSTs (106 are HDDs, 16 are SSDs)
           * 9.1 PiB of usable disk space (*df -hP /scratch{1,2}*)

Since each file system has two metadata targets, each project directory is configured to use one of MDTs, and they are spread roughly evenly between the two MDTs. This means that approximately 25% of all Hera projects share metadata resources.

.. rubric:: File Operations

* When a compute node needs to create or access a file, it   requests the associated storage locations from the MDS   and the associated MDT.
* I/O operations then occur directly with the OSSs and OSTs   associated with the file, bypassing the MDS.
* For read operations file data flows from the OSTs to the   compute node.

.. rubric:: Types of file I/O

With Lustre, there are three basic ways which an applicationaccesses data:

           * Single stream
           * Single stream through a master
           * Parallel

.. rubric:: File Striping

A file is split into segments and consecutive segments arestored on different physical storage devices (OSTs).

.. rubric:: Aligned vs Unaligned Stripes

* Aligned stripes is where each segment fits fully onto a   single OST. Processes accessing the file do so at   corresponding stripe boundaries.
* Unaligned stripes means some file segments are split   across OSTs.

.. rubric:: Progressive File Layouts

The /scratch1 and /scratch2 file systems are enabled with afeature called "Progressive File Layouts" (PFL) that does file layout in a way which is efficient for the vast majority of use cases. It uses a single stripe count for small files (reducing overhead) and increases the striping as the file gets bigger (increasing bandwidth and balancingcapacity), all without any user involvement.
These file systems are also augmented by a set of SSD OSTs (described above) and with the PFL capability is further optimized for small file performance. By default, smaller files are stored completely in SSD, which further decreases random operation latency and allows the HDDs to run more efficiently for streaming reads and writes. The default configuration will automatically stripe and place files in a generally optimal fashion to improve I/O performance for varying file sizes, including the use of SSDs for better small-file performance. The defaults also attempt to makethe best use of the SSD targets (which are faster, but have much less capacity than HDDs).
More details on PFL are available `<here: http://wiki.lustre.org/Progressive_File_Layoutshttp://doc.lustre.org/lustre_manual.xhtml#pfl>`_

**Important Note:** The PFL feature makes much of the information documented below regarding customizing striping unnecessary.

           * Users should not need to adjust stripe count and size on   /scratch1 and /scratch2.*
           * With PFL enabled, setting your own stripe layout may   reduce I/O performance for your files and the overall I/O   performance of the file system.
           * If you have already used "lfs setstripe" commands   documented below, you should probably remove the striping   that may have already been set. 
           
Here are the steps you should follow if you have any directories that had explicitly set non-default striping:

1. Remove all "lfs setstripe" commands from your scripts.
2. Run the following command which changes the stiping back to default for each of the directories on which you may have set striping: 

.. code-block:: shell 

   *lfs setstripe -d <dir>*

3. Open a `<help ticket https://rdhpcs-common-docs.rdhpcs.noaa.gov/wikis/rdhpcs-common-docs/doku.php?id=submitting_help_request>`_  with the subject like "/scratchX/<portfolio>/<project>   striped directories". We will examine the files and   assist with migrating files to an optimal layout if necessary.

.. rubric:: Userspace Commands

Lustre provides a utility to query and set access to the file system.
For a complete list of available options:

.. code-block:: shell

  lfs help

To get more information on a specific option:

.. code-block:: shell

  lfs help <option>

.. rubric:: Checking Diskspace

Hera file system allocations are “project” based. Lustre quotas are tracked and limited by “Project ID” (usually the same as group ID and directory name). The Project ID is assigned to top-level project directories and will be inherited for all new subdirs.
Tracking and enforcement includes maximum file count, not just capacity.
To check your usage details...


1. Look up your project ID number (not the name)  id  
2. Query your usage and limits using that number, for a given file system.  

.. code-block:: shell 

   lfs quota -p <project ID number> /scratchX

User and Group usage (capacity and file count) is tracked but not limited. You can also find your usage and your unixgroup's usage:

.. code-block:: shell
    
    lfs quota -u <User.Name> /scratch1    lfs quota -g <groupname> /scratch1

.. note::
  This is the *group* that owns the data,*regardless of where it is stored in the file system directory hierarchy*.

For example, to get a summary of the disk usage for project "rtnim":

.. code-block:: shell

   $ id   uid=5088(rtfim) gid=10052(rtfim) groups=10052(rtfim)...
   $ lfs quota -p 10052 /scratch1   Disk quotas for prj 10052 (pid 10052):        Filesystem  kbytes   quota   limit   grace   files   quota   limit   grace         /scratch1       4  1048576 1258291      *      1  100000  120000       -
   ("kbytes" = usage, "quota" = soft quota, "limit" = hard quota)

.. rubric:: Finding Files

The *lfs find* command is more *efficient* than the GNUfind, it may be faster too.
For example, finding fortran source files accessed within the last day:

.. code-block:: shell

    lfs find . -atime -1 -name '*.f90

.. rubric:: Striping Information
  
You can view the file striping (layout on disk) of a file with:

.. code-block:: shell

    lfs getstripe <filename>

The Hera default configuration uses “Progressive FileLayout” or PFL.

  * The first part of each file is stored on SSD
  * Up to 256 KB, single stripe (This is similar to how Panasas /scratch3,4 operated)
  * As the file grows bigger, it overflows to disks and it   stripes it across more disks and more disks
  * Up to 32 MB - on HDD, single stripe  
  * Up to 1 GB - on HDD, 4-way stripe  
  * Up to 32 GB - on HDD, 8-way stripe  
  * > 32 GB - on HDD, 32-way stripe, larger object size

So small files reside on SSDs, big files get striped“progressively” wider!
The "getstripe" command above shows the full layout.Typically not all components are instantiated. Only theextents which have "l_ost_idx" (object storage target index)and "l_fid" (file identifier) listed actually have createdobjects on the OSTs.
*Do not attempt to set striping!! If you think the default is not working for you, please let us know by submitting a help ticket.*

.. rubric:: Other lfs Commands

.. code-block:: shell

  * lfs cp – 

to copy files.

.. code-block:: shell

  * lfs ls – 

to list directories and files.

These commands are often quicker as they reduce the numberof stat and remote procedure calls needed.

.. rubric:: Read Only Access

           * If a file is only going to be read, open it as O_RDONLY.
           * If you don’t care about the access time, open it as   O_RDONLY|O_NOATIME.
           * If you need access time information and you are doing   parallel IO, let the master open it as O_RDONLY and all   other ranks as O_RDONLY|O_NOATIME.

.. rubric:: Avoid Wild Cards

tar and rm are *inefficient* when operating on a large setof files on lustre.
The reason lies in the time it takes to expand the wildcard. "*rm -rf \**" on millions of files could take days,and impact all other users. (And you shouldn't do just "\*"anyway, it is dangerous.
Instead, DO generate a list of files to be removed ortar-ed, and to act them one at a time, or in small sets.

.. code-block:: shell

   lfs find /path/to/old/dir/ -t f -print0 | xargs -0 -P 8 rm -f

.. rubric:: Broadcast Stat Between MPI or OpenMP Tasks

If many processes need the information from stat(), do it**once**, as follows:

* Have the master process perform the stat() call.
* Then broadcast it to all processes.

.. rubric:: Tuning Stripe Count (not typically needed)

  .. note::

**IMPORTANT:** *The following steps are not typicallyneeded on the Hera Lustre file systems. See the "ProgressiveFile Layouts" description above. Please open a supportticket prior to changing stripe parameters on your /scratch1or /scratch2 files.*

.. rubric:: General Guidelines

It is *beneficial* to stripe a file when...

           * Your program reads a single large input file and performs the input operation from many nodes at the same time.
           * Your program reads or writes different parts of the same file at the same time.
  * You should stripe these files to prevent all the nodes from reading from the same OST at the same time.
     * This will avoid creating a bottleneck in which your processes try to read from a single set of disks.

           * Your program waits while a large output file is written.
  * You should stripe this large file so that it can perform the operation in parallel.
     * The write will complete sooner and the amount of time the processors are idle will be reduced.
  * You have a large file that will not be accessed very frequently.
     * You should stripe this file widely (with a larger stripe count), to balance the capacity across more OSTs. * This (in current Lustre version) requires rewriting the file.

It is not always necessary to stripe files...

 * If your program periodically writes several small files from each processor, you don't need to stripe the files   because they will be randomly distributed across the   OSTs.

.. rubric:: Striping Best Practices

           * Newly created files and directories inherit the stripe settings of their parent directories.
           * You can take advantage of this feature by organizing your large and small files into separate directories, then setting a stripe count on the large-file directory so that all new files created in the directory will be automatically striped.
           * For example, to create a directory called "dir1" with a stripe size of 1 MB and a stripe count of 8, run:

.. code-block:: shell

    mkdir dir1    lfs setstripe -c 8 dir1

You can "pre-create" a file as a zero-length striped file byrunning lfs setstripe as part of your job script or as partof the I/O routine in your program. You can then write tothat file later. For example, to pre-create the file"bigdir.tar" with a stripe count of 20, and then add datafrom the large directory "bigdir," run:

.. code-block:: shell

    lfs setstripe -c 20 bigdir.tar    tar cf bigdir.tar bigdir

Globally efficient I/O, from a system viewpoint, on a lustrefile system is similar to computational load balancing in aleader-worker programming model, from a user applicationviewpoint. The lustre file system can be called upon toservice many requests across a striped file systemasynchronously and this works best if best practices, asoutlined above, are followed. A very large file that is onlystriped across one or two OSTs can degrade the performanceof the entire Lustre system by filling up OSTsunnecessarily.
By striping a large file over many OSTs, you increasebandwidth for accessing the file and can benefit from havingmany processes operating on a single file concurrently. Ifall large files accessed by all users are striped then I/Operformance levels can be enhanced for all users.
Small files should never be striped with large stripe countsif they are striped at all. A good practice is to make suresmall files are written to a directory with a stripe countof 1... effectively no striping.

.. rubric:: Increase Stripe Count for Large Files

           * Set the stripe count of the directory to a large value.
           * This spreads the reads/writes across more OSTs, therefore   \**balancing*\* the load and data.

.. code-block:: shell

    lfs setstripe -c 30 /scratch1/your_project_dir/path/large_files/

.. rubric:: Use a Small Stripe Count for Small Files

           * Place \**small files*\* on a single OST.
           * This causes the small files not to be spread   out/\**fragmented*\* across OSTs.

.. code-block:: shell

    lfs setstripe -c 1 /scratch1/your_project_dir/path/small_files/

.. rubric:: Parallel IO Stripe Count

           * Single shared files should have a stripe count \**equal   to*\* (or a factor of) the number of processes which   access the file.
           * If the number of processes in your application is greater   than 106 (the number of HDD OSTs), use '-c -1' to use all   of the OSTs
           * The stripe size should be set to allow as much stripe   alignment as possible.
           * Try to keep each process accessing as few OSTs as  possible.

.. code-block:: shell

    lfs setstripe -s 32m -c 24 /scratch1/your_project_dir/path/parallel/

You can specify the stripe count and size programmatically,by creating an MPI info object.

.. rubric:: Single Stream IO

           * Set the stripe count to 1 on a directory.
           * Write all files in this directory.
           * Compute
           * Otherwise set the stripe count to 1 for the file. 

.. code-block:: shell

    lfs setstripe -s 1m -c 1 /scratch1/your_project_dir/path/serial/

        
Data and Storage
================

Software
========

Shell & Programming Environments
================================

Compiling
=========

Running Jobs
============

Debugging
=========

Optimizing and Profiling
========================

Known Issues
============
