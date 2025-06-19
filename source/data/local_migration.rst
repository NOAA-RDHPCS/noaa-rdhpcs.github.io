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
  transfered. If you have lots of small files, this will slow down the
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
