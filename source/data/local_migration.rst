.. _migrating_local:

************************************
Migrating Data Between Local Systems
************************************

.. note::

    Large scale data migration can be challenging and time consuming. Please
    review the following guidelines and tools to minimize the time it takes to
    move your data and ensure successful and complete migration

General Guidelines
==================

    1. **Remove unneeded data!**
    The most efficient way to move a directory is to minimize the data you
    move. Delete temporary data you have been meaning to get around to purging.
    Tar and zip small files that you probably won’t need for a while. Archive
    old files and subdirectories to the HSMS and delete them from scratch file
    systems.

    2. With limited insight into the data structure of individual
    directories, it is hard to predict exactly how long a transfer might take.
    **Be sure to plan far ahead and leave yourself plenty of time to complete a
    migration!** Note that transferring many small files is often worse than a
    few large files because performance is more strongly related to the time it
    takes to access a file, not transfer it.

    3. Perform transfers from a
    compute node in a batch job as explained below. **Do not use the
    front-ends.** The I/O on front-end nodes is slower than on a compute nodes
    because they are shared with other users. (Yes, there is a run-time
    limitation for a compute job, but that can be addressed by splitting the
    transfer into smaller chunks and the approaches below).

    4. Use a
    synchronization tool (NOT just “cp” or “mv”) and **don’t rely on a one-time
    transfer completing perfectly.** This is important because you will most
    likely have to run the process more than once, and tools such as rsync will
    skip already copied files. Then go back and delete the source data once you
    have confirmed the copy is complete.

    5. Disable all batch and cron jobs
    that may be modifying the directories to be transferred. Any
    create/modify/delete changes can result in errors for any data transfer
    tool. For transfer of a large directory it may be OK to perform an initial
    copy **live**, but definitely quiesce access before performing a final
    sync.

    6. Make sure that the user performing the copy has permissions to
    read all data in the directory to be transferred. If a directory has files
    which are restricted, you will need to split it up into multiple transfers
    as multiple users, or change ownership on the source data first


Suggested Tools
===============

.. note::

    To move a large number of files, please submit a batch job
    to do the transfers ``as explained in a later section in this page``

rsync
-----

For basic migration, we recommend that you use rsync to transfer your
directories . Assuming your directory to move is named
``/mnt/lfs3/SYSADMIN/jetmgmt/jsmith/dir1``, a good way to transfer the data is:

.. code-block:: shell

    rsync -axv /mnt/lfs3/SYSADMIN/jetmgmt/jsmith/dir1
    /mnt/lfs4/SYSADMIN/jetmgmt/jsmith/    # Can use --delete if you want SRC and DEST to look the same

The -a option means archive, and will make sure
all ownership and dates are preserved in the transfer.

The -v option means verbose, and each file transfer will be displayed. This
allows you to see what is happening. If you have lots of small files, this
could slow down the transfer processes.

The –delete option means to remove files from the destination that are not in
the source directory. If after a completed rsync a file was then removed from
the source, then the next rsync with the –delete option would then remove the
file from the destination/ It may be preferable to clean up the source only
after confirming that all the files have been transferred.

The "-delete" option is useful when you want to keep the two directories
looking exactly the same.  Which means, if the file **did not** exist in
source, you want it removed on destination if did exist.

.. warning::

    Do not use the –delete option if you do not want data in the destination
    directory to be removed.

The -x option means to not cross filesystem boundaries. This is important when
links are used in your directories to point to other data that exist in on
other filesystems.

.. note::

    It is very important that you have a trailing slash after the
    source directory ``(/mnt/lfs3/SYSADMIN/jetmgmt/flast'''/''')``. If you do not,
    a second invocation of the same command will attempt to retransfer all of
    the data into a subdirectory, for example:

    ``/mnt/lfs4/SYSADMIN/jetmgmt/flast/flast``.

xsync
-----

An additional data synchronization tool, **xsync** is also available. It
is also a wrapper around rsync (and "find" and "xargs")
that performs multi-threaded transfers.

Usage of xsync is almost identical to rsync as described above.

.. note::

    The "include" and "exclude" rsync options are **not fully supported**. To view
    additional parameters to tune threading and depth for better performance, run
    ``xsync –-help``. In most cases they should not be needed.

Here is a sample job file that does a final check and also transfers any
remaining files that may have been created after intial transfer has been
completed:

.. code-block::

    #!/bin/bash -l
    #SBATCH -A myacct
    #SBATCH --time=8:00:00
    #SBATCH -N 1          # This can use only 1 node
    #SBATCH -o %x.o%j
    #SBATCH -J xfer-chk
    #SBATCH -p xjet

    set -x
    date

    SRC=/mnt/lfs3/SYSADMIN/nesccmgmt/$USER/regress           # Note - no "/" at the end
    DEST=/mnt/lfs4/SYSADMIN/nesccmgmt/$USER/                 # Note - ends with a "/"

    xsync -axv $SRC $DEST

    date

Creating a batch job to transfer your data
==========================================

The following is a sample batch job that can be submitted to perform the data
transfer work on a compute node.

.. code-block:: shell

    #!/bin/bash --login

    #SBATCH --job-name=storm
    #SBATCH --partition=xjet
    #SBATCH --time=08:00:00
    #SBATCH --nodes=1

    set -x

    SRC=/mnt/lfs3/BMC/storm/$USER/dir
    DEST=/mnt/lfs4/BMC/storm/$USER/         # NOTE: The dest is one level higher, and a trailing "/"!!!

    OUT=/home/jsmith/storm_jsmith_rsync.log
    echo “$(date) : Starting sync from $SRC to $DEST”&gt;&gt; $OUT

    rsync -ax $SRC $DEST&gt;&gt; $OUT 2&gt;&amp;1                  # --delete should not be needed

    echo “$(date) : Ending sync from $SRC to $DEST”&gt;&gt; $OUT


In this example, the project name should be changed to your own project.
The script asks for 1 node. The reason for this is that we want a dedicated
node for the data transfer to maximize performance.

After creating your batch job, submit it to the batch system. If it does not
finish in 8 hours, resubmit it. Once it finishes, add “-v” to the rsync line
and submit it one more time. Examine the output file carefully to make sure
there are no errors.

If after several tries, the transfer still hasn’t completed, email
rdhpcs.hera.help@noaa.gov,  and let us know. Include the paths of the output
files of your transfer jobs so we can see what is happening.

Known Issues
============

My job runs to completion but the files are not transferred
-----------------------------------------------------------

If your job completes and the files appear to not to have transferred, check
the job output files and the log files.  It is likely that your initialization
files are printing messages (typically with ``echo`` command in the
initialization files) that are causing the jobs to fail.

If this happens you could rename your initialization files (.cshrc, .tcshrc,
.bashrc, .login, .profile, .bash_profile, etc) temporarily and try again

A better solution is to address the problems caused by these initialization
files.

Were all my files transferred?
------------------------------

After your job has completed successfully, check if there are any errors. You
can ignore WARNings, and other messages, but  any message with the
string "FATAL" suggests an incomplete transfer.  It can happen because you
ran out of time, or there may be other problems.  If your job exited because it
ran out of time you should be able to resubmit the job but be sure to add the
**--resume** option.

You can also use "xsync" as mentioned above to make sure everything has been
completed as mentioned in the section above.

You can check how much data you had in your old file system and in the new file
system using the commands:

.. code-block:: shell

  lfs quota -u $USER /mnt/lfs3        to see how much was in /lfs3
  lfs quota -u $USER /mnt/lfs4        to see how much has been transferred to the new /lfs4

This will give you approximately how much data has been transferred.






