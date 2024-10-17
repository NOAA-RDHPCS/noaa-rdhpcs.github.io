.. _summary-of-storage-areas:

************************
Summary of Storage Areas
************************

The storage area to use in any given situation depends upon the activity you
wish to carry out. Storage areas are either user-centric or project-centric,
and are further divided by the underlying storage type (e.g., Network File
System (NFS), High Performance Storage System (HPSS), Lustre, IBM Spectrum
Scale). Each storage type has a different intended use as described below.

On each system, each user has a User Home area, and may have a User Archive
area. Each project has a Project Home area, Work areas, and Archive areas. The
different storage areas are summarized in the list and table below.

- **User Home:** Long-term data for routine access that is unrelated to a
  project. It is mounted on compute nodes as read/write.  We strongly recommend
  that users launch and run jobs from one of the Work file systems due to its
  larger storage capacity and superior performance.
- **Project Home:** Long-term project data for routine access that's shared
  with other project members. It is mounted on compute as read/write.  We
  strongly recommend that users launch and run jobs from one of the Work file
  systems due to its larger storage capacity and superior performance.
- **Member Work:** Short-term user data for fast, batch-job access that is not
  shared with other project members.
- **Project Work:** Short-term project data for fast, batch-job access that's
  shared with other project members.
- **World Work:** Short-term project data for fast, batch-job access that's
  shared with users outside your project.
- **Member Archive:** Long-term project data for archival access that is not
  shared with other project members.
- **Project Archive:** Long-term project data for archival access that's shared
  with other project members.
- **World Archive:** Long-term project data for archival access that's shared
  with users outside your project.
- **User-Shared Applications:** User-managed applications shared with all users
  on the system.

.. _data-filesystem-summary:

.. tab-set::

  .. tab-item:: Gaea
    :sync: gaea

    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                      | Type | Permissions | Quota         | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+===========================================+======+=============+===============+=========+=========+============+==================+
    | User Home                | ``/ncrc/home[12]/<userid>``               | NFS  | User set    | 50 GB         | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | Project Home             | ``/ncrc/proj/<projid>``                   | NFS  | 2770        | Project Based | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/gpfs/f[56]/<projid>/scratch/<userid>`` | GPFS | User set    | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | Project Work             | ``/gpfs/f[56]/<projid>/proj-shared``      | GPFS | 2770        | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | Project World Work       | ``/gpfs/f[56]/<projid>/world-shared``     | GPFS | 2775        | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/usw/<application>``                    | NFS  | 0755        | N/A           | No      | No      | N/A        | Read/Write       |
    +--------------------------+-------------------------------------------+------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Hera
    :sync: hera

    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                           | Type   | Permissions | Quota         | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+================================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                             | NFS    | User set    | 5 GB          | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/scratch[12]/<portfolio>/<projid>/<userid>`` | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                     | NFS    | 0755        | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Jet
    :sync: jet

    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                        | Type   | Permissions |  Quota        | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+=============================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                          | NFS    | User set    | 5 GB          | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/lfs[5]/<userid>``                        | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                  | NFS    | 0755        | N/A           | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Niagara
    :sync: niagara

    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                        | Type   | Permissions |  Quota        | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+=============================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                          | NFS    | User set    | 5 GB          | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/collab1/data/<userid>``                  | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/collab1/data_untrusted/<userid>``        | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                  | NFS    | 0755        | N/A           | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Pan
    :sync: pan

    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Area                     | Path                                        | Type   | Permissions |  Quota        | Backups | Purged  | Retention  | AN/PP Nodes |
    +==========================+=============================================+========+=============+===============+=========+=========+============+=============+
    | User Home                | ``/home/<userid>``                          | NFS    | User set    | 10 GB         | Yes     | No      | 90 days    | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | User Work                | ``/nbhome/<userid>``                        | NFS    | User set    | 10 GB         | Yes     | No      | 90 days    | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Work              | ``/work/<userid>``                          | CXFS   | User set    | Project Based | No      | Yes     | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Work              | ``/xtmp/<userid>``                          | NFS    | User set    | Project Based | No      | No      | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Work              | ``/ptmp/<userid>``                          | NFS    | User set    | Project Based | No      | Yes     | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Work              | ``/vftmp/<userid>``                         | Local  | User set    | Project Based | No      | No      | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Work              | ``/collab1/data_untrusted/<userid>``        | NFS    | User set    | Project Based | No      | No      | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+
    | Member Archive           | ``/archive/<userid>``                       | NFS    | User set    | Project Based | No      | No      | N/A        | Read/Write  |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+-------------+

.. important::

  Files within "Work" directories (i.e., Member Work, Project Work, World Work)
  are *not* backed up and are *purged* on a regular basis according to the
  time frames listed above.

.. _data-user-centric-areas:

==================================
Notes on User-Centric Data Storage
==================================

.. _data-user-home-directories-nfs:

User Home Directories (NFS)
===========================

The environment variable ``$HOME`` will always point to your current home
directory. It is recommended, where possible, that you use this variable to
reference your home directory. In cases in which using ``$HOME`` is not
feasible, it is recommended that you use ``/home/$USER`` (for hera, jet,
niagara, and pan) and ``ncrc/home/$USER`` for gaea.

Users should note that since this is an NFS-mounted filesystem, its performance
will not be as high as other file systems.

User Home Quotas
----------------

Quotas are enforced on user home directories. To request an increased quota,
contact the Help Desk. To view your current quota and usage, use the command
``quota`` on Gaea, Hera, Jet, and Niagara; and ``homeuse`` on Pan:


.. tab-set::

  .. tab-item:: Gaea
    :sync: gaea

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      ncrc-svm1.ncrc.gov:/ncrc/home2
                        9228M  51200M  51200M            101k   4295m   4295m

  .. tab-item:: Hera
    :sync: hera

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      10.181.1.1:/home
                        4147M      0K   5120M            2112       0       0

  .. tab-item:: Jet
    :sync: jet

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      10.181.1.1:/home
                        4147M      0K   5120M            2112       0       0

  .. tab-item:: Niagara
    :sync: niagara

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      10.181.1.2:/home_niagara
                         544K      0K   5120M              23       0       0

  .. tab-item:: Pan
    :sync: pan

    .. code::

      $ homeuse
      /home & /nbhome usage - 2024.01.16 10:01

      GROUP USERNAME                   FILESYS        FILES         GB   QUOTA  USE%
      grp   userid                  -  /home        447,121      29.80      40   74%
      grp   userid                  -  /nbhome      113,115       5.34      10   53%

User Home Permissions
---------------------

The default permissions for user home directories is shown in the
:ref:`Filesystem Summary Table <data-filesystem-summary>`. Users have the
ability to change permissions on their home directories, although it is
recommended that permissions be set to as restrictive as possible (without
interfering with your work).

User Home Backups
-----------------

If you accidentally delete files from your home directory, you may be able to
retrieve them. Online backups are performed at regular intervals. Hourly
backups for the past 24 hours, daily backups for the last 7 days, and
once-weekly backups are available. It is possible that the deleted files are
available in one of those backups. The backup directories are named
``hourly.*``, ``daily.*``, and ``weekly.*`` where ``*`` is the date/time stamp
of backup creation. For example, ``hourly.2020-01-01-0905`` is an hourly backup
made on January 1st, 2020 at 9:05 AM.

The backups are accessed via the ``.snapshot`` subdirectory. Note that ``ls``
alone (or even ``ls -a``) will not show the ``.snapshot`` subdirectory exists,
though ``ls .snapshot`` will show its contents. The ``.snapshot`` feature is
available in any subdirectory of your home directory and will show the online
backups available for that subdirectory.

To retrieve a backup, simply copy it into your desired destination with the
``cp`` command.

User Archive Directories (PAN Only)
===================================

The :ref:`gfdl_archive` provides long-term storage for the large amounts of
data created on the NOAA compute systems. The mass storage facility consists of
tape and disk storage components, servers, and the Data Migration Facility
(DMF) software. After data is uploaded, it persists on disk for some period of
time. The length of its life on disk is determined by how full the disk caches
become.

User archive areas on HPSS are intended for storage of data not immediately
needed in either User Home directories (NFS) or User Work directories (GPFS or
Lustre). Where available, User Archive directories should not be used to store
project-related data. Rather, Project Archive directories should be used for
project data.

User Archive Access
-------------------

Only GFDL users are given a personal :ref:`archive space <gfdl_archive>`. Users
are granted HPSS access if they are members of projects with Project Archive
areas.  GFDL users can transfer data to HPSS from any RDHPCS system using the
Princeton DTN, or the Princeton Globus end point.


User Archive Accounting
-----------------------

The GFDL director allocates tape storage to each GFDL group. A group leader may
also set allocations for individuals in the group. These allocations, and the
percent used, are shown by the local ``archrpt`` command.

For information on usage and best practices for HPSS, please see the :ref:`GFDL
archive <gfdl_archive>` page.

.. _data-project-centric-areas:

=====================================
Notes on Project-Centric Data Storage
=====================================

Project directories provide members of a project with a common place to store
code, data, and other files related to their project.

.. _data-project-home-directories-nfs:

Project Home Directories (NFS)
==============================

On some RDHPCS systems, projects are provided with a Project Home storage area
in the NFS-mounted filesystem. This area is intended for storage of data, code,
and other files that are of interest to all members of a project. Since Project
Home is an NFS-mounted filesystem, its performance will not be as high as other
file systems.

.. note::

  Data files stored in the project home area on Gaea should only be small files
  (<100MB).  Larger files should be stored in the project work area.

Project Home Path, Quota, and Permissions
-----------------------------------------

The path, quota, and permissions for Project Home directories are summarized in
the :ref:`Filesystem Summary Table <data-filesystem-summary>`.

Quotas are enforced on Project Home directories. To check a Project Home
directory’s usage on gaea, run ``df -h /ncrc/proj/[projid]`` (where
``[projid]`` is the project ID). Note, however, that permission settings on
some subdirectories may prevent you from accessing them, and in that case you
will not be able to obtain the correct usage. If this is the case, contact
help@olcf.ornl.gov for the usage information.

Project Home directories are root-owned and are associated with the project's
Unix group. Default permissions are set such that only members of the project
can access the directory, and project members are not able to change
permissions of the top-level directory.

Project Home Backups
--------------------

If you accidentally delete files from your project home directory, you may be
able to retrieve them. Online backups are performed at regular intervals.
Hourly backups for the past 24 hours, daily backups for the last 7 days, and
once-weekly backups are available. It is possible that the deleted files are
available in one of those backups. The backup directories are named
``hourly.*``, ``daily.*``, and ``weekly.*`` where ``*`` is the date/time stamp
of backup creation. For example, ``hourly.2020-01-01-0905`` is an hourly backup
made on January 1st, 2020 at 9:05 AM.

The backups are accessed via the ``.snapshot`` subdirectory. Note that ``ls``
alone (or even ``ls -a``) will not show the ``.snapshot`` subdirectory exists,
though ``ls .snapshot`` will show its contents. The ``.snapshot`` feature is
available in any subdirectory of your project home directory and will show the
online backups available for that subdirectory.

To retrieve a backup, simply copy it into your desired destination with the
``cp`` command.

Project Work Areas
==================

Project Work Areas to Facilitate Collaboration (Gaea)
-----------------------------------------------------------

To facilitate collaboration among researchers, RDHPCS systems provide distinct
types of project-centric work storage areas.  Each directory should be used for
storing files generated and used by computationally-intensive HPC jobs related
to a project.

The difference between the three storage areas lies in the accessibility of the
data to project members and to researchers outside of the project. Member Work
directories are accessible only by an individual project member by default.
Project Work directories are accessible by all project members.  World Work
directories are potentially readable by any user on the system.

Permissions
-----------

UNIX Permissions on each project-centric work storage area differ according to
the area’s intended collaborative use. Under this setup, the process of sharing
data with other researchers amounts to simply ensuring that the data resides in
the proper work directory.

-  Member Work Directory: ``700``
-  Project Work Directory: ``770``
-  World Work Directory: ``775``

For example, if you have data that must be restricted only to yourself, keep
them in your Member Work directory for that project (and leave the default
permissions unchanged). If you have data that you intend to share with
researchers within your project, keep them in the project’s Project Work
directory. If you have data that you intend to share with researchers outside
of a project, keep them in the project’s World Work directory.

Backups
-------

Member Work, Project Work, and World Work directories **are not backed up**.
Project members are responsible for backing up these files, either to Project
Archive areas (HPSS) or to an off-site location.

Project Archive Directories
===========================

Projects may be allocated project-specific archival space on the High
Performance Storage System (HPSS) or on the GFDL archive. Each project is given
a quota.  If a higher quota is needed, contact the appropriate help desk.

Permissions
-----------

UNIX Permissions on each project-centric archive storage area differ according
to the area’s intended collaborative use. Under this setup, the process of
sharing data with other researchers amounts to simply ensuring that the data
resides in the proper archive directory.

-  Member Archive Directory: ``700``
-  Project Archive Directory: ``770``
-  World Archive Directory: ``775``

For example, if you have data that must be restricted only to yourself, keep
them in your Member Archive directory for that project (and leave the default
permissions unchanged). If you have data that you intend to share with
researchers within your project, keep them in the project’s Project Archive
directory. If you have data that you intend to share with researchers outside
of a project, keep them in the project’s World Archive directory.

Project Archive Access
----------------------

Project Archive directories stored on HPSS may only be accessed via utilities
called HSI and HTAR. For more information on using HSI or HTAR, see the
:ref:`nescc_hpss` page.

Project Archive directories stored on GFDL archive can be accessed from Pan,
the GFDL workstations, and using Globus.
