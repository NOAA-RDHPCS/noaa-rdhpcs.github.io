.. meta::
   :description: Guide to data transfer methods on RDHPCS systems, including
    Globus, Data Transfer Nodes, Untrusted DTNs, and SSH port tunneling.
   :keywords: data transfers, Globus, DTN, UDTN, port tunneling, rsync, scp,
    trusted hosts, firewall

.. _Data_Transfers:

##############
Data Transfers
##############

.. _data-transfer-overview:

========
Overview
========


RDHPCS provides several methods to transfer data to and from RDHPCS
systems. Each method has  advantages and
disadvantages or limitations. Users should pick the approach that best
suits their needs based on the information provided here.

For security reasons, access to most external
hosts or sites (including your laptop/desktop) is blocked, and access is
opened up on an as-needed basis.  Sites that have been allowed access
are referred to as *trusted hosts* and all other sites/hosts will be
considered *"untrusted" sites/hosts.*

See :ref:`requests_for_firewall_exceptions` for details if you need
access to or from a machine that is currently considered as an “untrusted”
host/site.

.. _data_transfer_methods:

Data Transfer Methods
=====================

* Globus Connect Service is a utility system, Web or CLI-based, for
  efficient data transfer between DTNs and external storage systems.
  Where Globus endpoints are available, it is the recommended method
  for high-speed transfer. Note that some sites outside the RDHPCS
  program do not support Globus.
* Data Transfer Nodes (DTNs) are dedicated systems
  deployed and configured specifically for data transfers, providing
  fast methods for data transfer.  DTNs
  can only be used within RDHPCS, and transfers are limited to
  High-Performance File Systems (HPFS).
* Untrusted Data Transfer Nodes (UDTNs). Nodes available from anywhere
  on the Internet, to support transfers in and out of the RDHPCS
  program to external sites. Globus, or typical data transfer
  commands, can be used for transfer to and from UDTNs.
* Port Tunnelling. SSH tunnels can be created from a point of login to
  any remote host. Once a tunnel has been created, you can use the
  tunnels for data transfers, even from “untrusted hosts". This
  method is available when other choices are not available or optimal.


.. _globus:

==============================
Using Globus for Data Transfer
==============================

.. _globus_online_data_transfer:


Globus is the preferred method for most data transfers to, from, and
between RDHPCS systems. It is a robust service designed for
high-performance, secure, and reliable research data management.
You can use Globus through a web interface or a command-line tool.

What is Globus and Why Use It?
==============================

Globus simplifies file transfer by providing a single interface to
your data across different systems (HPCs, laptops, cloud storage).
Key benefits include:

* **Reliability:** Globus automatically verifies file integrity and
  resumes transfers if they are interrupted by network issues.
* **Performance:** It uses multiple parallel streams to achieve
  significantly higher transfer speeds than traditional tools
  ``scp`` or ``sftp``.
* **Ease of Use:** A "fire-and-forget" model lets you start a large
  transfer and close your browser. Globus manages the process in the
  background and emails you upon completion.
* **Security:** You authenticate with your existing organizational
  credentials, and data is transferred over secure channels.

.. _globus_quickstart:

Quick Start Guide
-----------------

For users who want to get started immediately, here is the most common
workflow:

1.  Navigate to the `Globus Web App`_ and log in using your "NOAA RDHPCS"
    organizational login.
2.  You will see a two-panel interface. In one panel, find your source
    "Collection" (typically your personal laptop, which you can set up with
    ``Globus Connect Personal``).
3.  In the other panel, find your destination "Collection"
    for instance,``noaardhpcs#hera_untrusted`` to transfer to Hera).
4.  Select the files or directories you wish to move.
5.  Click the "Start" button. Globus manages the transfer and notifies
    you by email when it's done.

.. warning::

    **Important Considerations Before Your First Transfer**

    * **Files Can Be Overwritten:** If a file with the same name exists
      in the destination directory, Globus will overwrite it **without warning**.
    * **File Permissions Are Not Preserved:** Transferred files arrive with default
      read/write permissions (``rw-r--r--``). You will need to use the ``chmod``
      command to add execute permissions back to any scripts or applications.
    * **Transfer Limits:** Each user is limited to 3 active transfers at a time.
      For best performance, transfer a large directory in a single task rather
      than many small files in separate tasks.
    * **Archiving Small Files:** For directories containing thousands of very small
      files (under 1MB), it is much more efficient to archive them into a single
      ``.tar`` or ``.zip`` file before transferring.

.. _globus_concepts:

Understanding Globus Concepts
=============================

To use Globus effectively, it helps to understand two core concepts:
**Collections**, and the difference between **Trusted** and **Untrusted**.

*   **Endpoint and Collection:** An **Endpoint** is a physical server or
    system where your files reside (like the Hera HPC cluster, your laptop).
    A **Collection** is a specific directory or set of files on that Endpoint
    that has been made accessible to Globus. You interact with Collections, not
    Endpoints directly.

*   **Trusted vs. Untrusted Collections:** RDHPCS provides two types of
    collections, each for a different purpose.

    .. list-table::
       :header-rows: 1
       :stub-columns: 1
       :widths: 20 25 30 50

       * - Collection Type
         - Access From
         - File System Access
         - Common Use Case
       * - **Trusted**
         - Pre-approved/whitelisted IP addresses (primarily other NOAA HPCs).
         - Full access to project and scratch filesystems (e.g., ``/scratch3``, ``/lfs5``).
         - High-speed data migration between two RDHPCS systems (e.g., moving data from Gaea to Jet).
       * - **Untrusted**
         - Anywhere on the internet.
         - Limited to a temporary staging directory (e.g., ``/data_untrusted/$USER``).
         - Transferring files between your laptop and an HPC, or sharing data with an external collaborator.


Workflows and Detailed Guides
-----------------------------

.. _globus-untrusted-workflow:

Workflow: Moving Data to Project Directories via Untrusted Collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common task is moving data from an external source (like your laptop)
into a specific project directory on an HPC system. Since Untrusted
Collections only provide access to a temporary staging area, this is a
two-step process:

**Step 1: Transfer Data to the Staging Area**
   Use the Globus Web App to transfer data from your source
   (typically your Globus Connect Personal endpoint) to the appropriate
   Untrusted Collection (for instance, ``noaardhpcs#ursa_untrusted``).
   Your data will arrive in a temporary directory, such as
   ``/scratch3/data_untrusted/$USER``.

**Step 2: Move Data to its Final Destination**
   Log in to the target HPC system (e.g., Ursa) via ``ssh``.
   Use the command line to move your data from the staging area to your project directory.

   .. code-block:: console

      # Example of moving data on Ursa
      mv /scratch3/data_untrusted/$USER/my_research_data /path/to/my/project/

A simplified visual of the workflow:

``[Your Laptop] ---(Globus)---> [HPC Staging Area] --->
(mv/cp on HPC)---> [HPC Project Directory]``


Using the Globus Web App
~~~~~~~~~~~~~~~~~~~~~~~~

The `Globus Web App`_ provides a graphical interface for all transfer and
sharing tasks.

To transfer data, you will need to know:

*   The name of the source and destination Collections.
*   The file paths for your source and destination directories.

The process is as follows:

1.  Navigate to the `Globus Web App <https://app.globus.org>`_.
2.  Login with an existing organizational login, selecting *NOAA RDHPCS*.
3.  In the Globus File Manager, search for your source Collection
    in one panel.
4.  In the second panel, search for your destination Collection
5.  Once connected, you can navigate the file systems in each panel.
6.  Select the files or directories you wish to transfer.
7.  Click the **Start** button to begin the transfer.

.. _globus-cli:

Using the Globus Command Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For users who prefer the command line or need to script transfers,
the Globus CLI is available on most RDHPCS systems.

To use it, you must first load the environment module:

.. code-block:: console

   $ module load globus-cli

This module also defines environment variables for the UUIDs of commonly
used Globus collections. You can run ``module show globus-cli``
review these variables.


For complete installation and usage instructions, please refer to the
official `Globus CLI Documentation <https://docs.globus.org/cli>`_.

Sharing Data with Globus
~~~~~~~~~~~~~~~~~~~~~~~~

You can use Globus to share data with external collaborators who do not have
RDHPCS accounts. Data can be shared from an Untrusted Collection with
any person who has a Globus account.

.. note::

    *   This feature is only available from **Untrusted Collections**.
    *   You can only share directories that are located within your user-specific
        untrusted directory (``/*/data_untrusted/$USER``, for example).
    *   Before sharing, you must log into the corresponding HPC system
        at least once to ensure your account directories are properly set up.

How to Share Data
'''''''''''''''''
The Globus web site provides complete instructions for sharing your data.
See the official `How to Share Files Guide <https://docs.globus.org/how-to/share-files/>`_.

When you log into the Globus web site and click **Collections**, you can
manage the collections you have shared and those that have been shared
with you.

.. _DTNs:

Data Transfer Nodes (DTNs)
--------------------------

We highly recommend using this method to transfer data when available,
as it provides a fast method for transferring TO and FROM HPC Systems
- Jet, Ursa, Mercury, Gaea, and Orion.  Please see the
Transferring Data page for complete details.

Note the following:

* DTNs can only be used **between NOAA RDHPCS systems.** For transfers
  involving systems outside the NOAA RDHPCS, see the UDTN section below.
* DTNs can typically only access the High-Performance Filesystems
  (HPFS-scratch file systems), not the **/home** filesystems.  This is a
  HPC site-specific configuration.
* Unattended data transfers can only be done using the DTNs.

If you are unable to use the DTNs, please review the other available options.

.. _UDTNs:

Untrusted Data Transfer Nodes (UDTNs)
-------------------------------------

Untrusted DTNs (UDTNs) are accessible from anywhere on the internet.
They are designed to allow data to be transferred in and out of the
RDHPCS program from external (non-NOAA HPC) sites -- Cloud
providers, Universities, for example. UDTNs only access the following
directories on the host system:

``/*/data_untrusted/$USER``

For occasional transfers to/from untrusted hosts, you can use two stage
copying to copy data from an remote host to an RDHPCS host.

* Untrusted DTNs can only be used for inbound connections.
  The connection cannot be started
  on the DTNs, but data can flow in either direction. Typically, users
  should be able to log in to the remote system and initiate a transfer
  from the remote machine.

.. note::

    Before you use the UDTN for data transfers, you MUST have logged
    into the appropriate host for the necessary directories to appear -
    including your /home.

    See :ref:`transferring-data`
    for complete details.

.. _Port_Tunnelling:

Port Tunnelling
---------------

In the SSH port tunnel method, an SSH tunnel is created between your
point of login (typically your desktop) to the remote host (typically
Ursa, Jet or other remote hosts). The port tunnel method works
from any system on the network (that is, your local machine does not
necessarily have to be in the noaa.gov domain). We recommend using
this method when the options above are not available or
are not optimal for your use case.  Please see the
Transferring Data page for complete details.

.. _requests_for_firewall_exceptions:

Requests for Firewall Exceptions
================================

For security reasons, access to/from all external sites is controlled
by a Firewall and most external sites are blocked and allowed to
connect only through an exception to the Firewall rules. Please see
the Transferring Data page for complete details.

.. _firewall_exception_terms:

Firewall Exception Terms
========================

* Data Transfer Method: scp, sftp, rsync, globus, wget, curl, "globus"
* Local Machine: Where you will be logged in when initiating the transfer
* Remote Machine: The other machine that will be involved in the transfer.

.. note::

    If you need to access an external site on a routine basis
    for your work, you will need to request a Firewall Exception. Submit a
    helpdesk ticket with the subject line: Firewall Exception request and
    provide the information requested below.

* Justification: Some information about why this is needed
* Data Transfer Method: The utility that will be used for doing data transfer
* Local Machine: DNS name, IP address (or endpoint for Globus)
* Remote Machine: DNS name, IP address (or endpoint for Globus)
* Sample command: A typical transfer command

.. note::
    If you have a globus endpoint, please provide it, as that would be the
    preferred method for data transfers.

.. note::
    Using Globus, you can have a third party transfer where both the ends of a
    transfer are remote.


.. _transferring-data:

=================
Transferring Data
=================

This section provides details and examples for data transfer methods other
than Globus, as well as a consolidated reference of all RDHPCS Globus
Collections.

.. _globus_collection_summary:

RDHPCS Globus Collections Reference
===================================

The following RDHPCS and partner clusters provide Globus collections.
For transfers involving your local machine or external collaborators,
always use the **Untrusted** collection.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 15 35 20 20 20

   * - Cluster
     - Collection Display Name
     - File Systems
     - Site
     - Access
   * - **PPAN**
     - | noaardhpcs#ppan
       | noaardhpcs#ppan_untrusted
     - | /archive, /home, /work
       | /collab1/data_untrusted
     - GFDL
     - | Trusted Hosts
       | Anywhere
   * - **Ursa**
     - | noaardhpcs#ursa
       | noaardhpcs#ursa_untrusted
     - | /scratch3, /scratch4
       | /scratch3/data_untrusted, /scratch4/data_untrusted
     - NESCC
     - | Trusted Hosts
       | Anywhere
   * - **Gaea**
     - | noaardhpcs#gaea
       | noaardhpcs#gaea_f6
     - | /gpfs/f5, $HOME
       | /gpfs/f6, $HOME
     - NCRC
     - | Anywhere
       | Anywhere
   * - **Jet**
     - | noaardhpcs#jet
       | noaardhpcs#jet_untrusted
     - | /mnt/lfs[5,6]
       | /mnt/lfs[5,6]/data_untrusted
     - GSL
     - | Trusted Hosts
       | Anywhere
   * - **Mercury**
     - | noaardhpcs#mercury
       | noaardhpcs#mercury_untrusted
     - | /collab2/data
       | /collab2/data_untrusted
     - NESCC
     - | Trusted Hosts
       | Anywhere
   * - **Orion**
     - msuhpc2#orion-dtn
     - /work, /work2
     - MSU
     - Anywhere
   * - **Hercules**
     - msuhpc2#hercules
     - /work, /work2
     - MSU
     - Anywhere


.. _migrating_local:
.. note::

    Large scale data migration can be challenging and time consuming. Please
    review the following guidelines and tools to minimize the time it takes to
    move your data and ensure successful and complete migration

General Guidelines
------------------

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
   don't rely on a one-time transfer completing perfectly.** This is
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
---------------

du
---

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
    │   ├── [2.6K]  images
    │   ├── [ 416]  data
    │   ├── [ 416]  systems
    │   ├── [ 288]  software
    │   ├── [ 224]  slurm
    │   ├── [ 192]  _templates
    │   ├── [ 192]  accounts
    │   ├── [ 160]  _downloads
    │   ├── [ 160]  files
    │   ├── [ 128]  _search
    │   ├── [ 128]  _static
    │   ├── [ 128]  contributing
    │   ├── [ 128]  help
    │   ├── [ 128]  logging_in
    │   ├── [  96]  FAQ
    │   ├── [  96]  compilers
    │   ├── [  96]  connecting
    │   └── [  96]  queue_policy
    ├── [1.7K]  build
    │   ├── [ 992]  html
    │   └── [ 608]  doctrees
    └── [  96]  utils

      15K used in 24 directories

Local Data Migration note and table

.. attention::

   Do *not* use the ``du`` or ``tree`` command on the lustre filesystems listed below:


+-------------+-------------+
| Cluster     | File System |
+=============+=============+
|| Jet        || /lfs5      |
||            || /lfs6      |
+-------------+-------------+
|| Ursa       || /scratch3  |
||            || /scratch4  |
+-------------+-------------+


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

- ``--delete`` means to remove files from the destination that are not in the
  source directory. If after a completed rsync a file was then removed from the
  source, then the next rsync with the ``--delete`` option would then remove
  the file from the destination/ It may be preferable to clean up the source
  only after confirming that all the files have been transferred.

.. warning::

    Do not use the ``--delete`` option if you do not want data in the
    destination directory to be removed.

xsync
-----

On Jet and Ursa, an additional data synchronization tool,
``xsync`` is available in ``/apps/local/bin``. It is an unsupported
wrapper around ``rsync``,
``find``, and ``xargs`` that performs multi-threaded transfers.

Usage of ``xsync`` is almost identical to ``rsync`` as described above.

.. note::

    ``xsync`` does not support the ``--include`` and ``--exclude``
    rsync options.  To view additional parameters to tune threading
    and depth for better performance, run ``xsync --help``. In most
    cases they should not be needed.


A sample batch script to transfer data
--------------------------------------

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

If after several tries, the transfer still hasn't completed, and the
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
