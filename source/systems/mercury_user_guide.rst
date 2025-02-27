.. _mercury-user-guide:

##################
Mercury User Guide
##################


.. image:: /images/niagara.jpg
   :scale: 25%

.. _mercury-system-overview:

System Overview
===============

As NOAA's R&D severe long range weather projects expand to
geographically dispersed private and public HPC clouds, it is
imperative that the the NOAA RDHPCS program provide a service for data
dissemination and analysis outside of the traditional HPC environment.
Mercury is intended to be a collaborative location where
data can be securely copied to and from any location, by any
authorized user. It can also be used to disseminate R&D data to NOAA's
collaborators around the globe.

The Mercury system includes:

- Back-end storage
- Interactive Nodes
- Software
- Account Management.

Users can connect to the Data Transfer Nodes (DTN) from any remote
system to push or pull data. Beyond the Back-end storage and DTNs, the
cluster allows for data analysis, visualization, verification,
validation and data analytics. These are provided through a combination of
hardware and software, which mirrors the user environment and a subset
of the tools available on the legacy RDHPCS systems and
legacy Analysis systems (PPAN). It can also include software which is
unique to this system and not traditionally found on traditional HPC
systems.

Mercury System Features:

- 20 cores/socket, 2.5 GHz, 2 sockets/nodes
- 12 Login Nodes
- 2 DTNs available from trusted (pre-approved) NOAA and non-NOAA sites
- 2 Untrusted Data Transfer Nodes (UDTNs) available from anywhere on
  the internet.
- 2 Web servers


Data Transfer
================

In order to use Mercury for file transfers, you must create user
account directories. These directories are automatically created with
your first login to a Mercury front end. The Mercury front ends may be
accessed using either CAC or RSA credentials. This table contains
:ref:`bastion hostnames <bastion_hostnames>` for CAC and RSA access.

The following directories will automatically be created with your
first login:

- /home/First.Last (your home directory)
- /collab2/data/First.Last (for your trusted data)
- /collab2/data_untrusted/First.Last(for your untrusted data)

.. note::

   When using the DTNs for data transfers:

   - /home tree is not accessible from the DTNs
   - /collab2/data/ tree is only accessible from the "Trusted DTN".
   - /collab2/data_untrusted tree is only accessible from the
     "Untrusted DTN"


Per User Data Management on Mercury
-----------------------------------

Mercury is a hybrid system, a cross between a traditional HPC
system and a data transfer/collaboration system, available to all
RDHPCS users. Mercury file system management has special requirements. The
following are data management policies:

- All files under the "/collab2/data_untrusted/$USER" directory tree
  which have not been accessed in the last 5 days will be
  automatically purged.
- All files under the "/collab2/data/$USER" directory tree which have
  not been accessed in the last 60 days will be automatically purged.
- All files under the "/collab2/data/$PROJECT" directory are treated
  the same as HPFS (scratch) data and are not deleted.
- A default 10GB Lustre quota on each user's home directory
  "/collab2/home/$USER" .

Access time is defined as the last time the file was opened for
reading or writing.

.. warning::

   If the file system's usage approaches the total
   capacity, we will be forced implement a more aggressive purge
   policy (i.e., 30 day or 15 day purge) . So please actively manage
   your data.

Lustre File System Usage
========================

Lustre is a parallel, distributed file system often used to support
the requirements for high-performance I/O in large scale clusters by
supporting a parallel I/O framework that scales to thousands of nodes
and petabytes of storage. Lustre features include high-availability
and POSIX compliance.

On the RDHPCS Mercury system there is one Lustre file system, /collab2,
available for use.

The serial transfer rate of a single stream is generally greater than
1 GB/s but can easily increase to 6.5 GB/s from a single client, and
more than 10 GB/s if performed in a properly configured parallel
operation.

Components
----------

Lustre functionality is divided among four primary components:

-  MDS - Metadata Server
-  MDT - Metadata Target
-  OSS - Object Storage Server
-  OST - Object Storage Target

An MDS is a server that assigns and tracks all of the storage locations
associated with each file, in order to direct file I/O requests to the
correct set of OSTs and corresponding OSSs.

An MDT stores the metadata, filenames, directories, permissions and
file layout, handling network requests to them.

An OSS manages a small set of OSTs by controlling I/O access and

An OST is a block storage device, often several disks in a RAID
configuration.

Configuration
-------------

All nodes access the lustre file-systems mounted at /collab2.

The number of servers and targets on *each* of the two Mercury file
systems is:

-  2 MDSs (active/active)
-  2 MDTs
-  4 OSSs (active/active, embedded in DDN SFA14kx storage
   controllers)
-  24 OSTs (all are HDDs)
-  1.9 PiB of usable disk space (*df -hP /collab1*)

File Operations
---------------

-  When a compute node needs to create or access a file, it requests
   the associated storage locations from the MDS and the associated
   MDT associated with the file, bypassing the MDS.
-  I/O operations then occur directly with the OSSs and OSTs
-  For read operations, ile data flows from the OSTs to the compute
   node.

With Lustre, there are three basic ways which an application accesses
data:

-  Single stream
-  Single stream through a master
-  Parallel.

**File Striping**

A file is split into segments and consecutive segments are stored on
different physical storage devices (OSTs).

-  Aligned stripes is where each segment fits fully onto a single OST.
   Processes accessing the file do so at corresponding stripe
   boundaries.
-  Unaligned stripes means some file segments are split across OSTs.

**Userspace Commands**

Lustre provides a utility to query and set access to the file system.

For a complete list of available options:

.. code-block:: shell

   lfs help

To get more information on a specific option:

.. code-block:: shell

   lfs help <option>

