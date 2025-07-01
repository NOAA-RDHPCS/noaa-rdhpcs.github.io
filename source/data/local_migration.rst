.. _migrating_local:

*****************************************
Migrating Data Between Local File Systems
*****************************************

.. note::

    Large scale data migration can be challenging and time consuming. Please
    review the following guidelines and tools to minimize the time it takes to
    move your data and ensure successful and complete migration

General Guidelines
==================

#. **Size the dataset and prune unneeded data.**
   Use tools such as ``du``, ``tree`` on the directories to understand the
   data volumes.  Ensure there are no duplicate data sets, temporary
   working files, or other unneeded content.  **The most efficient way
   to move data is to reduce the data to move.** Use ``tar`` or ``zip``
   archiving tools to collapse directories into a single file.  As
   appropriate, archive directories to the site-specific HSMS and
   delete from scratch file systems.
#. **Start early and leave plenty of time for migration.**
   Be aware that everyone on the filesystems will be moving data.
   Even with data sizes in hand, with limited insight into the data
   structure of individual directories, it is hard to predict exactly
   how long a transfer might take.  **Be sure to plan far ahead and
   leave yourself plenty of time to complete a migration!** Note that
   transferring many small files is often worse than a few large files
   because performance is more strongly related to the time it takes
   to access a file, not transfer it.
#. **Make sure that the user performing the copy has permissions to
   read all data in the directory to be transferred.** If a directory
   has files or sub-directories which are restricted, you will need to
   split it up into multiple transfers as multiple users, or change
   ownership on the source data first.
#. **Disable all batch and cron jobs that may be modifying the
   directories to be transferred!** Any create/modify/delete changes
   can result in errors for any data transfer tool. For transfer of a
   large directory it may be OK to perform an initial copy
   **interactively**, but definitely quiesce access before performing
   a final sync.
#. **Use a synchronization tool (NOT just** ``cp`` or ``mv`` **) and
   don’t rely on a one-time transfer completing perfectly.** This is
   important because you will most likely have to run the process more
   than once, and tools such as rsync will skip already copied
   files. Then go back and delete the source data once you have
   confirmed the copy is complete.
#. **For small data volumes, use an interactive session** on an HPCS head
   node.  In the unlikely event the volume of data to move is less
   than a terabyte (TB) / 1,000 gigabytes (GB) it is appropriate to
   use a head node to do an 'ad-hoc' data transfer using a tool such
   as rsync.
#. **For larger data volumes, submit a batch job** to a 'dtn' or similar
   queue

Suggested Tools
===============

du
--

An original part of Unix, the ``du`` disk usage tool will be found on
every HPCS.  It can provide a simple overview of the usage of a file
or directory.  Output can be easily sorted by piping the output
through ``sort``.  One example command is:

.. code-block:: shell

   du -sk DIRECTORY/* | sort -n

- ``-s`` will summarize sub directory usage
- ``-k`` will output in 1024-byte (1 kiB) blocks
- ``| sort -n`` pipes the output through the sort, sorted numerically

tree
----

A highly useful but optional part of Linux systems that `should` be
installed on all NOAA RDHPCS, the ``tree`` tool provides
tree-structured output about a directory with the option to summarize
and calculate usage.  One example command is:

.. code-block:: shell

        tree --du -h -d -L 2 --sort=size DIRECTORY

- ``--du`` will calculate disk usage on directories
- ``-h`` will display human-readable (K,M,G,T) volumes
- ``-d`` will summarize directories
- ``-L 2`` will only show two levels of directories
- ``--sort=size`` will sort output by size

.. code-block:: shell

    % tree --du -h -d --sort=size -L 2 .
    [8.8K]  .
    ├── [6.3K]  source
    │   ├── [2.6K]  images
    │   ├── [ 416]  data
    │   ├── [ 416]  systems
    │   ├── [ 288]  software
    │   ├── [ 224]  slurm
    │   ├── [ 192]  _templates
    │   ├── [ 192]  accounts
    │   ├── [ 160]  _downloads
    │   ├── [ 160]  files
    │   ├── [ 128]  _search
    │   ├── [ 128]  _static
    │   ├── [ 128]  contributing
    │   ├── [ 128]  help
    │   ├── [ 128]  logging_in
    │   ├── [  96]  FAQ
    │   ├── [  96]  compilers
    │   ├── [  96]  connecting
    │   └── [  96]  queue_policy
    ├── [1.7K]  build
    │   ├── [ 992]  html
    │   └── [ 608]  doctrees
    └── [  96]  utils

      15K used in 24 directories

.. attention::

   Do *not* use the ``du`` or ``tree`` command on the lustre file systems listed below:


+--------------+----------------+---------------------------------------------+
| Cluster      | File System    | Path to Report                              |
+==============+================+=============================================+
| Jet          |  LFS5          |  /lfs5/SYSADMIN/project-info/disk-usage     |
|              |                |                                             |
|              |  LFS6          |  /lfs6/SYSADMIN/project-info/disk-usage     |
+--------------+----------------+---------------------------------------------+
| Hera, Ursa   |  scratch1      |  /scratch1/SYSADMIN/project-info/disk-usage |
|              |                |                                             |
|              |  scratch2      |  /scratch2/SYSADMIN/project-info/disk-usage |
+              |                |                                             |
|              |  scratch3      |  /scratch3/SYSADMIN/project-info/disk-usage |
|              |                |                                             |
|              |  scratch4      |  /scratch4/SYSADMIN/project-info/disk-usage |
+--------------+----------------+---------------------------------------------+


rsync
-----

For basic migration, it is recommended to use the ``rsync`` tool to
transfer the files and directories. One example command is:

.. code-block:: shell

    rsync --archive --verbose --one-file-system /full/path/to/source/directory/ /full/path/to/destination/directory

.. warning::

    It is very important that you have a trailing slash after the
    source directory: ``/full/path/to/source/directory/`` **/**. If you do not,
    a second invocation of the same command will attempt to retransfer all of
    the data into a subdirectory, for example:

    ``/full/path/to/source/directory/directory``.

- ``--archive`` (``-a``) will ensure all ownership and dates are
  preserved in the transfer.
- ``--verbose`` (``-v``) will display details of every file being
  transferred. If you have lots of small files, this will slow down the
  transfer processes.
- ``--one-file-system`` (``-x``) restricts the transfer to the source
  filesystem. This is important when symlinks are used to point to
  data that exists on other filesystems.

To keep the two directories exactly the same, use ``--delete`` -- if
the file **did not** exist in source, you want it removed on
destination if does exist:

- ``--delete`` means to remove files from the destination that are not
  in the source directory. If after a completed rsync a file was then
  removed from the source, then the next rsync with the –delete option
  would then remove the file from the destination/ It may be
  preferable to clean up the source only after confirming that all the
  files have been transferred.

.. warning::

    Do not use the ``–-delete`` option if you do not want data in the
    destination directory to be removed.

xsync
-----

On Jet and Hera, an additional data synchronization tool,
``xsync`` is available in ``/apps/local/bin``. It is an unsupported
wrapper around ``rsync``,
``find``, and ``xargs`` that performs multi-threaded transfers.

Usage of ``xsync`` is almost identical to ``rsync`` as described above.

.. note::

    ``xsync`` does not support the ``--include`` and ``--exclude``
    rsync options.  To view additional parameters to tune threading
    and depth for better performance, run ``xsync –-help``. In most
    cases they should not be needed.


A sample batch script to transfer data
======================================

Here is a sample batch script that can be used as a template, then
submitted to the batch system to perform the data movement:

.. code-block:: shell

    #!/bin/bash

    #SBATCH --job-name=data-transfer
    #SBATCH --partition=PARTITION_GOES_HERE
    #SBATCH --time=08:00:00
    #SBATCH --nodes=1
    #SBATCH --output=$HOME/data-transfer-job-%j

    set -x

    SRC=/path/to/source/directory/                 # Note trailing slash
    DEST=/path/to/destination/directory

    echo "$(date) : Starting sync from $SRC to $DEST"

    rsync -ax $SRC $DEST

    echo "$(date) : Ending sync from $SRC to $DEST"


Before using this template, replace the ``PARTITION_GOES_HERE`` with
the appropriate partition for the HPCS being used.  Refer to the
system-specific pages for that information.

After updating the template and saving it locally as a batch job,
submit it to the batch system. Watch for the exit status -- if it does
not finish in 8 hours, resubmit it. Once it finishes successfully, add
``-v`` to the rsync line and submit it one more time. Examine the
output file carefully to make sure there are no errors.

If after several tries, the transfer still hasn’t completed, and the
errors are not obvious upon reading the batch job output, refer to the
:ref:`getting help <getting_help>` pages and ask for assistance.  Be
sure and include the file paths of the output files of your transfer
jobs for best assistance.

Known Issues
============

My job runs to completion but the files are not transferred
-----------------------------------------------------------

Look at the job output for obvious errors.  It will be in your home
directory in a file starting with ``data-transfer-job-``.  If your job
completes and the files appear to not to have transferred, read that
file for clues.

If you are not a regular user of the batch system, it is likely that
your initialization files are printing messages (typically with
``echo`` command in the initialization files) that are causing the
jobs to fail.

If this happens you could rename your initialization files (.cshrc, .tcshrc,
.bashrc, .login, .profile, .bash_profile, etc) temporarily and try again.
A better solution is to address the problems caused by these initialization
files.

Were all my files transferred?
------------------------------

Look at the job output.  It will be in your home directory in a file
starting with ``data-transfer-job-``.  When the job completes read
that file for clues and any errors.  You can ignore WARNings, and
other messages, but any message with the string "FATAL" suggests an
incomplete transfer.  It can happen because you ran out of time, or
there may be other problems.  If your job exited because it ran out of
time you should be able to resubmit the job but be sure to add the
**--resume** option.
