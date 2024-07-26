.. _gfdl_archive:

************
GFDL Archive
************

The GFDL archive is a long-term archive system based on HPE's Data Management
Framework (DMF).  The GFDL archive includes 13.1 petabytes of front-end disk
cache, 5 tape libraries, and 160+ tape drives. Total available capacity is 360
PB. The GFDL archive is accessible from Pan and other GFDL systems.

Users should keep the following things in mind when using the GFDL archive
system:

-  The GFDL archive is well suited for storing large volumes of data.
-  Users should avoid storing small files (in the megabyte range or smaller) to
   the archive since the process of moving numerous individual small files to
   and from tape is inefficient.  Please tar up small files into one large tar
   file before storing data into the archive.
-  All data stored in the archive is single copy. Deleted data cannot be
   recovered.
-  The archive file system should not be used for direct file access.  Users
   should copy files to one of the other Pan file systems prior to working with
   the file.

For questions regarding the HPSS system, email oar.gfdl.help@noaa.gov.

.. _gaining_access_to_use_gfdl_archive:

Gaining Access to use the GFDL Archive
======================================

All users with a GFDL account will have a personal archive directory.

.. _gfdl_archive_data_structure:

GFDL Archive Data Structure
===========================

The users archive area is located at ``/archive/$USER``.  The
``/archive/$USER`` is a symbolic link to ``/arch[0-8bcfgh]/$USER``.  These
``arch[0-8bcfgh]`` directories are used to better distribute the load on the
front-end cache drives.

All files are ultimately stored on tapes housed in the tape libraries, access
to those files is using the Linux file system structure on the front-end cache.
When a file is accessed, DMF will automatically recall the file from tape and
place it on the front-end cache disk.

.. _gfdl_archive_data_retention:

Data Retention
==============

At this time files stored in the GFDL archive do not have a set retention
policy.  GFDL divisions and users can decide how long to keep files in the
archive.  However to ensure adequate space is available for all, uses should
remove data that is no longer needed.

.. _gfdl_archive_data_recovery_policy:

Data Recovery Policy
====================

Occasionally an archive tape is damaged or otherwise becomes partially
unreadable. When that happens, the local RDHPCS staff works with the
manufacturer to troubleshoot the problem and take steps to attempt to recover
the missing data. Very rarely, even with these efforts, we are unable to
recover the missing files. The user will then be informed of the files we
cannot recover.

In that case, the user has one further option. There are a number of outside
recovery services which will make further attempts at recovery for a fee. Some
charge a flat fee, some charge more if they are able to recover than if they
are unable to recover. If the user wishes to sign up for such a service and pay
the fee, RDHPCS will handle the logistics of shipping and other coordination
with the recovery service.

.. _gfdl_archive_getting_started:

Getting Started
===============

The GFDL archive is accessible from all Pan nodes, including all DTNs, and via
a Globus endpoint.  The GFDL archive is also available as read-only from the
GFDL workstations.

DMF has a few utilities to help manage files stored on in the tape library and
their residency on the front-end disk cache.  The list, with a brief
description is in the table below.  See ``man <command>`` for more information.

+---------------------+-----------------------------------------------+
| Commands            | Description                                   |
+=====================+===============================================+
| ``dmget <files>``   | Recall files from tape to the front-end cache |
+---------------------+-----------------------------------------------+
| ``dmput <files>``   | Write files to tape                           |
+---------------------+-----------------------------------------------+
| ``dmwho``           | Show pending dmgets with wait times           |
+---------------------+-----------------------------------------------+
| ``dmls -l <files>`` | Show file state (disk/tape residence)         |
+---------------------+-----------------------------------------------+

.. warning::

    Files should be copied from ``/archive`` to the one of the other Pan file
    systems, e.g., ``/vftmp`` fast-scratch filesystem, before use.

Allocation and Quota
--------------------

The GFDL director allocates tape storage to each GFDL group. A group leader may
also set allocations for individuals in the group. These allocations, and the
percent used, are shown by the local ``archrpt`` command:

 archrpt -s
 archrpt -r <group>

These allocations are enforced administratively. For details, see ``archrpt
-h``.

Finding Files
-------------

To facility the ability for users to search for files in the GFDL archive, a
database of file in the archive is updated daily.  To search for files in the
archive, supply a pattern to  the ``dmlocate`` command:

.. code::

 $ dmlocate <pattern>

Refer to ``man dmlocate`` for more information.

.. _nescc_hpss_help:

GFDL Archive Help
=================

For additional questions, please email: oar.gfdl.help@noaa.gov.
