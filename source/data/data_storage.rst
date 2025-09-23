.. _data-storage:

************
Data Storage
************

Each RDHPCS system has multiple options for data storage.  Each user has
multiple user-affiliated storage spaces, and each project has multiple
project-affiliated storage spaces where data can be shared for collaboration.
Below we give an overview and explain where each storage area is mounted.

.. _summary-of-storage-areas:


Summary of Storage Areas
========================

The storage area to use in any given situation depends upon the activity you
wish to carry out. Storage areas are either user-centric or project-centric,
and are further divided by the underlying storage type (e.g., Network File
System (NFS), High Performance Storage System (HPSS), Lustre, IBM Spectrum
Scale). Each storage type has a different intended use as described below.

On each system, each user has a User Home area, and may have a User Archive
area. Each project has a Project Home area, Work areas, and Archive areas. The
different storage areas are summarized in the list and table below.

- **User Home:** Long-term data for routine access that is unrelated to a
  project.  It is mounted on compute nodes as read/write.  We strongly
  recommend that users launch and run jobs from one of the Work file systems
  due to its larger storage capacity and superior performance.
- **Project Home:** Long-term project data for routine access that's shared
  with other project members.  It is mounted on compute as read/write.  We
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

  .. tab-item:: Ursa
    :sync: ursa

    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                           | Type   | Permissions | Quota         | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+================================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                             | NFS    | User set    | 10 GB         | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/scratch[34]/<portfolio>/<projid>/<userid>`` | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                     | NFS    | 0755        | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Hera
    :sync: hera

    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                           | Type   | Permissions | Quota         | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+================================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                             | NFS    | User set    | 10 GB         | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/scratch[34]/<portfolio>/<projid>/<userid>`` | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                     | NFS    | 0755        | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+------------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Jet
    :sync: jet

    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                        | Type   | Permissions |  Quota        | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+=============================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                          | NFS    | User set    | 10 GB         | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/lfs[5,6]/<userid>``                      | Lustre | Project set | Project Based | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                  | NFS    | 0755        | N/A           | No      | No      | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+

  .. tab-item:: Mercury
    :sync: mercury

    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Area                     | Path                                        | Type   | Permissions |  Quota        | Backups | Purged  | Retention  | On Compute Nodes |
    +==========================+=============================================+========+=============+===============+=========+=========+============+==================+
    | User Home                | ``/home/<userid>``                          | NFS    | User set    | 5 GB          | Yes     | No      | 90 days    | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/collab2/data/<userid>``                  | Lustre | Project set | 60 TB         | No      | 60 days | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | Member Work              | ``/collab2/data_untrusted/<userid>``        | Lustre | Project set | 20 TB         | No      | 14 days | N/A        | Read/Write       |
    +--------------------------+---------------------------------------------+--------+-------------+---------------+---------+---------+------------+------------------+
    | User-Shared Applications | ``/contrib/<application>``                  | N/A    | N/A         | N/A           | N/A     | N/A     | N/A        | N/A              |
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


Notes on User-Centric Data Storage
----------------------------------

.. _data-user-home-directories-nfs:

User Home Directories (NFS)
===========================

The environment variable ``$HOME`` will always point to your current home
directory. It is recommended, where possible, that you use this variable to
reference your home directory. In cases in which using ``$HOME`` is not
feasible, it is recommended that you use ``/home/$USER`` (for ursa, hera, jet,
mercury, and pan) and ``ncrc/home/$USER`` for gaea.

Users should note that since this is an NFS-mounted filesystem, its performance
will not be as high as other file systems.

User Home Quotas
----------------

Quotas are enforced on user home directories. To request an increased quota,
contact the Help Desk. To view your current quota and usage, use the command
``quota`` on Gaea, Ursa, Hera, Jet, and Niagara; and ``homeuse`` on Pan:


.. tab-set::

  .. tab-item:: Gaea
    :sync: gaea

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      ncrc-svm1.ncrc.gov:/ncrc/home2
                        9228M  51200M  51200M            101k   4295m   4295m

  .. tab-item:: Ursa
    :sync: ursa

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      10.181.1.1:/home
                        4147M      0K   5120M            2112       0       0

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

  .. tab-item:: Mercury
    :sync: mercury

    .. code::

      $ quota -Qs
      Disk quotas for user userid (uid 12345):
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
      10.181.1.2:/home_mercury
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
directory's usage on gaea, run ``df -h /ncrc/proj/[projid]`` (where
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
the area's intended collaborative use. Under this setup, the process of sharing
data with other researchers amounts to simply ensuring that the data resides in
the proper work directory.

-  Member Work Directory: ``700``
-  Project Work Directory: ``770``
-  World Work Directory: ``775``

For example, if you have data that must be restricted only to yourself, keep
them in your Member Work directory for that project (and leave the default
permissions unchanged). If you have data that you intend to share with
researchers within your project, keep them in the project's Project Work
directory. If you have data that you intend to share with researchers outside
of a project, keep them in the project's World Work directory.

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
to the area's intended collaborative use. Under this setup, the process of
sharing data with other researchers amounts to simply ensuring that the data
resides in the proper archive directory.

-  Member Archive Directory: ``700``
-  Project Archive Directory: ``770``
-  World Archive Directory: ``775``

For example, if you have data that must be restricted only to yourself, keep
them in your Member Archive directory for that project (and leave the default
permissions unchanged). If you have data that you intend to share with
researchers within your project, keep them in the project's Project Archive
directory. If you have data that you intend to share with researchers outside
of a project, keep them in the project's World Archive directory.

Project Archive Access
----------------------

Project Archive directories stored on HPSS may only be accessed via utilities
called HSI and HTAR. For more information on using HSI or HTAR, see the
:ref:`nescc_hpss` page.

Project Archive directories stored on GFDL archive can be accessed from Pan,
the GFDL workstations, and using Globus.

.. _nescc_hpss:


NESCC HPSS
==========

The centralized, long-term data archive system at National Environmental
Security Computing Center (NESCC) is based on IBM's High Performance Storage
System (HPSS). The NESCC HPSS environment includes 22 petabytes of front-end
disk cache, five Oracle SL8500 enterprise tape libraries, three Spectra Logic
TFinity tape libraries, and 148 tape drives. Total available capacity is 430
PB. HPSS is accessible from WCOSS2, Hera, Mercury, Jet, and Gaea.

Users should keep the following things in mind when using the HPSS system:

-  The HPSS system is well suited for storing large volumes of data.
-  Users should avoid transferring many small files (in the megabyte range or
   smaller) to HPSS since the process of moving numerous individual small files
   to and from tape is inefficient. Please tar up small files into one large
   tar file before storing data into HPSS, or use HTAR.
-  All data stored in HPSS is single copy. Deleted data cannot be recovered.
-  HPSS **is not accessible from compute nodes.** Access is available via
   Hera/Mercury/Jet front-end nodes (FEs), Gaea Data Transfer Nodes (DTNs),
   and WCOSS2 transfer nodes.
-  Batch jobs that require access to HPSS must be submitted to the
   correct systems service or transfer queues.  Look for queue or partition
   names that contain "dtn".

For questions regarding the HPSS system, email rdhpcs.hpss.help@noaa.gov.

.. _gaining_access_to_use_hpss:


Gaining Access to use HPSS
==========================

.. _new_hpss_user_requests:

New HPSS User Requests
======================

Access to an HPSS project must be requested.  A HPSS user must be a current
user of a NOAA HPC compute resource (RDHPC or WCOSS) to have access to HPSS.
When you are a member of a project on a compute resource you are not
automatically added to the companion HPSS project (if there is one). Being
added to a HPSS project that you are already a member of on a NOAA compute
resource is done without PI or Portfolio Manager approval, but both are
notified that you are being added. If you are not a member of the project on a
NOAA compute resource then PI or Portfolio manager approval is required before
you will be added. To start the process please send an email to
rdhpcs.hpss.help@noaa.gov with the following subject line ``USERNAME requests
access to HPSS - PORTFOLIO/PROJECT``, replacing ``USERNAME`` and
``PORTFOLIO/PROJECT`` with your username and project request. If PI or
Portfolio Manager approval is required, the email should come from them.

All requests must have the following information:

-  User Name
-  Requested project(s) - See :ref:`NESCC HPSS Data Structure
   <nescc_hpss_data_structure>` for available HPSS projects
-  System HPSS access is needed from (Hera/Jet/Mercury/Gaea/WCOSS)

.. _adding_new_projects_to_hpss:

Adding New Projects to HPSS
---------------------------

Projects on a NOAA compute resource are not given access to the HPSS until
requested by the Portfolio Manager (PfM). The PfM also approves the maximum
time retention directory (pool) that a project is allowed to use on HPSS. All
lesser time pools will also be available. To add a project to the HPSS the
Portfolio Manager should submit a help request with the following information:

- Project name
- Associated users
- Maximum time retention pool

To remove a project from the HPSS the PfM should submit a help request with the
project name and data disposition directions. Requests are reviewed and
approved by the HPSS Resource Manager and sent to the HPSS system administrator
for implementation.

.. note::

   Requests for adding users and projects to HPSS is NOT supported in AIM, but
   instead the request/review/implementation/notification process is handled by
   the HPSS help ticket system.

   Email: rdhpcs.hpss.help@noaa.gov.

.. _nescc_hpss_data_structure:

NESCC HPSS Data Structure
=========================

HPSS data at NESCC is organized by portfolio, project and retention period,
with a directory structure of ``PORTFOLIO/PROJECT/RETENTION``.  Each retention
period (1-5 year & permanent) is set up as a separate file family, e.g.,
``1year``, ``2year``, ``3year``, ``4year``, ``5year``, and ``permanent``.  This
means that all data for a retention period is stored on the same tapes.
Projects live under the appropriate portfolio and have been assigned access to
specific retention directories.  Project users have access to write data to any
of their projects' retention directories.  Data within the same retention
directory can be moved to other projects within the same retention directory.
If data needs to be moved to another retention period (ex: ``/1year`` ->
``/2year``) it must be copied.

The structure has the following syntax:

.. code::

   /PORTFOLIO/PROJECT/RETENTION

Examples are:

.. code::

   /BMC/wrf-chem/2year

   /NCEPDEV/emc-meso/5year

.. note::

   Please be sure to store the data you write to HPSS in the appropriate
   retention directory, and in the correct project if you belong to multiple
   projects. This will avoid movement of data once it is stored on tape.

Portfolios Using HPSS
---------------------

Portfolios with projects currently storing data in HPSS are NCEPPROD,
NCEPDEV, BMC, HFIP, CPO, NAGAPE, NOS and SYSADMIN

.. tab-set::

   .. tab-item:: NCEPDEV

      .. hlist::
         :columns: 6

         * emc-climate
         * emc-da
         * emc-ensemble
         * cpc-om
         * emc-hwrf
         * emc-land
         * emc-marine
         * emc-meso
         * emc-naqfc
         * emc-global
         * emc-nhc
         * emc-ocean
         * emc-ohdc
         * emc-swpc
         * mdl-dmo
         * emc-nems
         * mdl-obs
         * mdl-blend
         * mdl-stat
         * mdl-surge
         * re4cast
         * GEFSRR
         * nesdis-drt
         * nesdis-h-sandy
         * nesdis-jcsda
         * swpc-sair
         * mdl-ens
         * swpc-geospace
         * swpc-ipe
         * swpc-para
         * swpc-wdas
         * swpc-solar
         * swpc-wam
         * swpc-wamgip
         * swpc-wamipe
         * marineda
         * cpc-op
         * wpc-archive

   .. tab-item:: BMC

      .. hlist::
         :columns: 6

         * acb
         * aomip
         * ap-fc
         * arop
         * arso
         * calnexfc
         * cases
         * ccasm
         * ccp-mozart
         * ccwrf
         * cfsstrat
         * chem-var
         * chimera
         * ciaqex
         * climatt
         * cmod
         * co2
         * comgsi
         * csd-wca
         * csdchem
         * forms
         * det
         * dlaps
         * dtc
         * etlcm
         * fab
         * fd
         * fdr
         * fim
         * fire-wx
         * hmtb
         * frd
         * futextrm
         * gacs
         * gapp2005
         * gmtb
         * gomtrans
         * gsd-hpcs
         * guienne
         * gt-md
         * mef
         * hmtr
         * home
         * iset
         * isidora
         * isp-1
         * jetmgmt
         * lpdm
         * madis
         * mcwi
         * ome
         * naos-ruc
         * neaqs
         * nesccmgmt
         * nevs
         * news2
         * nim
         * nrelwind
         * odvars
         * old-projects
         * regclim
         * oplapb
         * ppef
         * profosse
         * qnh
         * qosap
         * rcc21
         * rcm1
         * rcm2
         * reanl
         * sepp
         * rem
         * ro-osse
         * rocosmic
         * rtrr
         * rtvs
         * rucdev
         * ruclidar
         * rucsref
         * ufs-phys
         * shout
         * sos
         * stela
         * stratus
         * strmtrck
         * taq
         * taq_reruns
         * tcmi

   .. tab-item:: HFIP

      .. hlist::
         :columns: 6

         * cloudda
         * emcda
         * gfsenkf
         * globpsd
         * dtc-hurr
         * gpshwrf
         * gsihyb
         * hfip-ahw
         * gnmip
         * hfip-gfdl
         * hfip-hda
         * hfip-fiu
         * hfip-psu
         * hfip-um
         * hfip-mef
         * hfip-wisc
         * hfip-wisc2
         * hfip-utah
         * hur-aoml
         * hur-laps
         * hfipprd
         * hur-uri
         * hwrf-vd
         * hur-osse
         * hybda
         * modelpsd
         * hwrfv3
         * renkf
         * sso
         * Old-Projects
         * umarwi
         * wrfsatda

   .. tab-item:: NAGAPE

      .. hlist::
         :columns: 6

         * aoml-osse
         * arl
         * ciaqex
         * cmaq-so4
         * enso
         * glrcm
         * hpc-wof1
         * mmap-emd
         * nep
         * ocean-osse
         * reef5
         * seaglider
         * stc

   .. tab-item:: CPO

      .. hlist::
         :columns: 6

         * cpo_ngrr_e

   .. tab-item:: NOS

      .. hlist::
         :columns: 6

         * coast
         * crs
         * nosofs

   .. tab-item:: SYSADMIN

      .. hlist::
         :columns: 6

         * cmod
         * jetmgmt
         * nesccmgmt

.. _nescc_hpss_data_retention:

Data Retention
==============

Retention based storage is the HPSS archive policy in Fairmont, to better
manage data growth. Six retention storage pools (1-5year and permanent) were
created. Each retention period is setup as a separate file family. This means
all data for a retention period is stored on the same tapes. All HPSS projects
were then configured to write to one or more of these pools. Data in these
pools expires based upon the retention pool it was written in and would be
deleted upon expiration. All files in the HPSS archive have been assigned an
expiration date based on the file create time and the retention period it was
written to. Upon expiration files will be deleted from the HPSS archive.

.. _expired_data_deletion_process:

Expired Data Deletion Process
-----------------------------

.. _user_notification:

User Notification
~~~~~~~~~~~~~~~~~

Users will be notified of expired data via posted lists and email. These
notifications will take place on or before the first day of the month following
the data's expiration. For example, data that has an expiration date between
October 1 and October 31 2016 will have its notification posted on or before
November 1, 2016. The expired file list is located on HPSS in
``/Expired_Data_Lists/expired.YYYY-MM.txt``. All HPSS users have read access to
this file and can retrieve it for review. The file is easily searchable by HPSS
username. For each file included in the expired list the file owner, file
group, filename/path, and expire date are shown. For example:

.. code::

   root system /1year/SYSADMIN/nesccmgmt/test_file-1G-11 Jul-6-2016.

Email notification will also be sent to all users who have data listed in this
file. It is the user's responsibility to regularly check the posted list for
expired files they own. Once deleted these files cannot be recovered.

.. _expired_data_deletions:

Expired Data - Deletions
~~~~~~~~~~~~~~~~~~~~~~~~

The following table maps out when future deletions will take place.

================ ================= ===========
Expire Date      Notification Date Delete Date
================ ================= ===========
Dec 1 - Dec 31   January 1         February 1
Jan 1 - Jan 31   February 1        March 1
Feb 1 - Feb 28   March 1           April 1
Mar 1 - Mar 31   April 1           May 1
Apr 1 - Apr 30   May 1             June 1
May 1 - May 31   June 1            July 1
Jun 1 - June 30  July 1            August 1
Jul 1 - Jul 31   August 1          September 1
Aug 1 - Aug 30   September 1       October 1
Sept 1 - Sept 30 October 1         November 1
Oct 1 - Oct 31   November 1        December 1
Nov 1 - Nov 30   December 1        January 1
================ ================= ===========

.. _file_size_guidelines:

File Size Guidelines
====================

Archiving files to HPSS is a much different process than writing files to disk
storage. Please be aware that the size of the files you write to HPSS can
impact the performance and efficiency of the system.

.. rubric:: Preferred file size range

File sizes in the gigabyte range are preferred for storing in HPSS. A few files
of hundreds of gigabytes each make the most efficient use of the system.

.. rubric:: Considerations for very large files

**Files larger than 3 TB WILL FAIL TO STORE IN HPSS.**
Transferring files that are 1 TB or larger increases the risk of poor system
performance as well as the risk (although small) of losing a file that contains
a large amount of data. We recommend storing files that are 1 TB or smaller.

.. rubric:: Avoid small files

Avoid transferring many small files — those in the megabyte range or smaller.
The process of moving numerous individual files to and from tape is
inefficient. It can become very time consuming and result in slowing the system
for all users.

When you need to store many small files, use one of these two approaches:

-  Use :ref:`htar <using-htar>` to transfer them together as a single archive
   file.
-  Use an archiving utility, e.g. ``tar``, on the source system to bundle the
   member files and then transfer the resulting archive file with ``hsi put``
   or or ``hsi cput``.

Please contact the HPSS helpdesk if you need help determining appropriate file
sizes for your specific workload.

.. _data_recovery_policy:

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

.. _nescc_hpss_getting_started:

Getting Started
===============

HPSS is only accessible from WCOSS, Theia, Jet and Gaea Data Transfer
Nodes (DTNs). Batch jobs should be used to access HPSS and need be
submitted to the respective systems service or transfer queues.  Look
for queue names that contain "dtn".

Modules have been created on each system to provide the proper
user environment and tools to access HPSS from these systems. These modules are
not loaded by default and will need to be loaded before you can use any of the
HPSS commands. To add the HPSS tools to your environment, use the following
module command:

.. tab-set::

   .. tab-item:: Hera, Jet, Mercury, and WCOSS

      .. code::

         module load hpss

   .. tab-item:: On Gaea RDTN's

      .. code::

         module use /usw/hpss/modulefiles
         module load hsi

.. _using-htar:

HTAR
----

HTAR allows the creation of archive files directly in HPSS without the need to
do an intermediate step of first creating the archive (tar) file on local disk
storage before copying the archive file to HPSS.  In addition, HTAR creates a
separate index file, which contains the names and locations of all of the
member files in the archive file. The index file allows individual files and
directories in the archive to be randomly retrieved without the need to read
through the archive file.

.. note:: Limitations

   HTAR has the following limitations:

      * File size: An individual file within the tar file may not be larger
        than 68 GB.
      * Directory paths: The directory path of any file may not exceed 154
        characters in length.
      * File names: File names may not exceed 99 characters in length.

.. _htar_cookbook:

HTAR Cookbook
~~~~~~~~~~~~~

.. _creating_an_htar_archive_file_example:

.. rubric:: Creating an HTAR Archive File Examples

To create a new archive file ``files.tar``  that contains ``file1`` and
``file2`` in the HPSS at ``/SYSADMIN/nesccmgmt/1year/testuser/work``:

.. code::

   htar -cvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar file1 file2

To create a new archive file ``time.tar`` that contains all files that match
the glob pattern ``time*`` in the HPSS directory
``/SYSADMIN/nesccmgmt/1year/testuser/work``:

.. code::

   $ htar -cvf /SYSADMIN/nesccmgmt/1year/testuser/work/time.tar time*

.. _retrieving_an_htar_archive_file_example:

.. rubric:: Retrieving an HTAR Archive File Examples

To extract ``file1`` and ``file2`` from the archive ``files.tar`` located in
the HPSS directory ``/SYSADMIN/nesccmgmt/1year/testuser/work``:

.. code::

   $ htar -xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar ./file1 ./file2

To extract all files from the archive ``files.tar`` located in the HPSS
directory ``/SYSADMIN/nesccmgmt/1year/testuser/work``:

.. code::

   $ htar -xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

.. _list_files_in_archive_file:

.. rubric:: List Files in an HTAR Archive File Example

To list the names of files in the archive ``files.tar`` located in the HPSS
directory ``/SYSADMIN/nesccmgmt/1year/testuser/work``:

.. code::

   $ htar -tvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

.. _recrating_an_htar_index_file_example:

.. rubric:: Recreating a HTAR Index File Example

This operation is used either to reconstruct an index for tar files whose index
file is unavailable (e.g., accidentally deleted), or for tar files that were
not originally created by HTAR.

.. code::

   $ htar -Xvf /SYSADMIN/nesccmgmt/1year/testuser/work/files.tar

.. _using-hsi:

HSI
---

HSI is an FTP-like interface to the HPSS.  HSI is most useful for file and
directory manipulation.  HSI supports wild cards for local and HPSS pathname
pattern matching, and provides recursion for many commands, including the
ability to store, retrieve, and list entire directory tress, or change
permissions on entire trees.  Some HSI operations, such as ``cp`` and ``mkdir``
resemble their Linux and UNIX counterparts.

For example:

-  ``hsi ls`` lists the contents of a directory
-  ``hsi cp`` copies files within the HPSS
-  ``hsi rm`` permanently removes a file
-  ``hsi mkdir`` creates a directory
-  ``hsi rmdir`` deletes a directory
-  ``hsi mv`` moves files within the HPSS directory structure

.. _hsi_basic_usage:

HSI Basic Usage
~~~~~~~~~~~~~~~

HSI can accept input several different way.

.. rubric:: Interactive Command

When using the interactive command form, enter the HSI operations.

.. code::

   $ hsi
   [connecting to hpsscore1.fairmont.rdhpcs.noaa.gov/1217]
   ******************************************************************
   *   Welcome to the NESCC High Performance Storage System         *
   *                                                                *
   *   Current HPSS version: 7.4.3 Patch 2                          *
   *                                                                *
   *                                                                *
   *           Please Submit Helpdesk Request to                    *
   *              rdhpcs.hpss.help@noaa.gov                         *
   *                                                                *
   *  Announcements:                                                *
   ******************************************************************
   Username: User.ID  UID: 1234  Acct: 1234(1234) Copies: 1 Firewall: off [hsi.5.0.2.p5 Mon Sep 12 15:22:37 UTC 2016]
   [hpsscore1]/PORTFOLIO-> mkdir foo
   [hpsscore1]/PORTFOLIO-> cd foo
   [hpsscore1]/PORTFOLIO/foo-> put hpss_file

.. rubric:: Single line execution

Enclose the HSI operations in quotes, separated with the semicolon (;)
character.

.. code::

   hsi "mkdir foo; cd foo; put hpss_file"

.. rubric:: Using commands from a File

Use the HSI ``in`` operation to read HSI operations from a file

.. code::

   $ cat command_file
   mkdir foo
   cd foo
   put hpss_file
   $ hsi in command_file

.. rubric:: Using a Heredoc

Similar to using operations contained in a file, the shell's heredoc feature
can be used to pass to HSI the operations.  This method is useful in a batch
job script.

In this example, we get a file from HPSS, ``hpss_file``, and place it in a new
directory foo on the local system.

.. code::

   $ hsi <<EOF
      lmkdir foo
      lcd foo
      get local_file : hpss_file
   EOF

.. note::

   The HSI ``get`` and ``put`` operations use a different syntax than FTP to
   identify the local file name. The HSI syntax uses a ``:`` (colon character)
   to separate the local pathname from the HPSS pathname.

.. caution::

   The ``mv``, ``put``, and ``get`` HSI operations can overwrite data at their
   targets without warning.  This is a problem if you mistakenly remove or
   overwrite data, because it cannot be recovered. To help prevent inadvertently
   overwriting your HPSS files with these commands, establish directory
   permissions carefully.

.. _hsi_cookbook:

HSI Cookbook
~~~~~~~~~~~~

.. rubric:: Moving Files/Directories in HPSS

To move a directory or file to a new location in HPSS:

.. code::

   $ hsi mv /1year/PORTFOLIO/old/location /1year/PORTFOLIO/new/location

Please note that the ``mv`` operation will only work for files/directories
stored in the same retention directory. If you need to move data between
retention directories you must use cp. Please contact the HPSS helpdesk for
steps on doing this efficiently.

.. rubric:: Writing Files to HPSS

To put the file ``local_file`` into the HPSS directory
``/BMC/testproj/myid/work``

.. code::

   $ hsi put /full_local/path/local_file : /BMC/testproj/myid/work/local_file

.. rubric:: Retrieve a File from HPSS

In this example, we will To get the HPSS file ``hpss_file`` located in the HPSS
directory ``/BMC/testproj/myid/work``.

To place ``hpss_file`` in your current directory:

.. code::

   $ hsi get /BMC/testproj/myid/work/hpss_file

To place ``hpss_file`` in the local directory ``/full_local/path`` with the
name ``new_name``:

.. code::

   $ hsi get /full_local/path/new_name : /BMC/testproj/myid/work/hpss_file

.. rubric:: Retrieve a File from HPSS and Preserve the Modification Time

.. code::

   $ hsi get -p /BMC/testproj/myid/work/hpss_file

.. rubric:: Listing the Contents of an HPSS Directory

To list the contents of the directory /BMC/testproj

.. code::

   $ hsi ls /BMC/testproj

The ``ls`` operation has other useful options.  Using the ``-N`` option will
list fill file information, along with the full path to the file.

.. code::

   [core]/-> ls -N /BMC/testproj
   -rw-------    1 User.ID  grp      54727283200 Mar 20  2016 /BMC/testproj/hpss_file1.tar
   -rw-------    1 User.ID  grp             5408 Mar 20  2016 /BMC/testproj/hpss_file1.tar.idx
   -rw-------    1 User.ID  grp      54727283200 Mar 20  2016 /BMC/testproj/hpss_file2.tar
   -rw-------    1 User.ID  grp             5408 Mar 20  2016 /BMC/testproj/hpss_file2.tar.idx

The ``-V`` option will list the tape volume information for a file (PV List is
the tape volume):

::

   [core]/-> ls -V /BMC/testproj/hpss_file1.tar
   /BMC/testproj:
   -rw-------    1 User.ID  grp           5         1234 TAPE   54727283200 Mar 20  2016 hpss_file1.tar
   Storage   VV   Stripe
    Level   Count  Width  Bytes at Level
   ----------------------------------------------------------------------------
    1 (tape)   1       1  54727283200
     VV[ 0]:   Object ID: 8c0772a0-8552-11e4-af76-0002559ae41b
               ServerDep: 7d72478a-bb87-11d6-9419-0002559ae41b
     Pos:    121+0   PV List: N0998300

.. _file_expiration_commands:

File Expiration Commands
------------------------

The HSI operations ``expls`` and ``expfind`` are used to show and find the
expiration date of data stored in HPSS.  Each operation has the ``-h`` option
to display the usage information.

.. rubric:: Operation expls Help

.. code::

   $ hsi "expls -h"
   Usage expls [-?] [-A] [-R] [-v] [path ...]
     -?  : display this usage
     -A  : display absolute pathnames
     -R  : [standard option]recursively list hash entries for files in the specified path(s)
     -v  : verbose listing mode

.. rubric:: Operation expfind Help

.. code::

   $ hsi "expfind -h"
   Usage: expfind[ete] [-?] [-A] [-b beginTime] [-d days] [-e endTime] [-R]  [path ...]
     -?  : display this usage
     -A  : display absolute pathname for files
     -b  : specify beginning time in range
     -d  : find file that will be expiring in specified number of days from today
     -e  : specify ending time in range
     -R  : [standard option]recursively delete expiration time for the specified path(s)
     Note: If -b is not specified, then files whose expiration time is <= endTime are listed
           If -e is not specified, then files whose expiration time is>= beginTime are listed
           If neither -b nor -e is specified, all expired files in the path(s) are listed
              based on the time at which the command is started
    Times are of the form YYYY-MM-DD[-hh:mm:ss]
    hours/mins/seconds are optional and default to 00:00:00 if not specified

.. rubric:: List the Expiration Date of a File

.. code::

   $ hsi "expls /1year/BMC/testproj/file.20160712"
   Wed Jul 12 15:57:35 2017  /1year/BMC/testproj/file.20160712

.. rubric:: Find Files that Expired On or Before a Certain Date

.. code::

   $ hsi "expfind -e 2016-08-30"
   Expiring: /bench1/gyre.tar (Wed Jan 20 22:16:58 2016) Owner: User.Id [1234] Group: grp [1234]
   Expiring: /bench1/HSUBSYS1.0.hpssdb.NODE0000.CATN0000.20150605013019.001 (Sat Jun 18 13:32:36 2016) Owner: root [0] Group: system [0]
   Expiring: /bench1/HSUBSYS1.0.hpssdb.NODE0000.CATN0000.20150606013020.001 (Sat Jun 18 15:41:39 2016) Owner: root [0] Group: system [0]
   Expiring: /bench1/htar_thiea_baseline.tar (Thu Jan 28 20:58:11 2016) Owner: User.Id [1234] Group: grp [1234]
   Expiring: /bench1/htar_thiea_baseline.tar.idx (Thu Jan 28 20:58:11 2016) Owner: User.Id [1234] Group: grp [1234]

.. _sample_hpss_batch_job:

Sample HPSS Batch Job
---------------------

The following is a sample script that shows how to transfer data to HPSS via a
batch job:

.. code::

   #!/bin/bash
   #SBATCH --ntasks=1
   #SBATCH --time=0:30:00
   #SBATCH --account=<ENTER A VALID PROJECT HERE>
   # Use the proper partition name.
   #    Jet, Hera, Mercury use the 'service' partition
   #    Gaea is 'dtn_f5_f6', with optional --constraint=f5 or --constraint=f6
   #      to route to a node which has that file system mounted
   #SBATCH --partition=<USE THE CORRECT PARTITION, SEE ABOVE>
   #SBATCH --qos windfall
   #SBATCH --job-name=hpss-test

   # Initialize the module environment, load the appropriate module for a given HPCS

   source $MODULESHOME/init/bash
   domainname=$(perl -T -e "use Net::Domain(hostdomain); print hostdomain")
   if [[ $domainname =~ boulder|fairmont ]]; then
        module load hpss
   elif [[ $domainname =~ ncrc ]]; then
        module use /usw/hpss/modulefiles
        module load hsi
   fi

   set -x

   hpssdir=${hpssdir:-/1year/PORTFOLIO/project/User.Id}    # XXXX: Location of your file in HPSS
   tarfile=${tarfile:-hpss_file.tar}                       # XXXX: Name of the tar file in HPSS
   dirsave=${dirsave:-/path/to/save/directory}             # XXXX: Location of data you want to write to HPSS

   cd $SLURM_SUBMIT_DIR

   #   Check if the tarfile index exists.  If it does, assume that
   #   the data for the corresponding directory has already been
   #   tarred and saved.
   hsi "ls -l ${hpssdir}/${tarfile}.idx"
   tar_file_exists=$?
   if [ $tar_file_exists -eq 0 ]
   then
      echo "File $tarfile already saved."
      exit
   fi

   #   htar is used to create the archive, -P creates
   #   the directory path if it does not already exist,
   #   and an index file is also made.
   htar -P -cvf ${hpssdir}/$tarfile $dirsave
   err=$?
   if [ $err -ne 0 ]
   then
      echo "File $tarfile was not successfully created."
      exit 3
   fi

.. note::

   The HSMS is not an infinite resource. Quotas will be enabled over time to
   prevent uncontrolled use. Only save what you need to save. Consider the cost
   of time and compute resources to regenerate data from the original input
   files. That is often cheaper than storing the data long term.

.. _hpss_help:

HPSS Help
=========

For additional questions, please email: rdhpcs.hpss.help@noaa.gov.

.. _gfdl_archive:


GFDL Archive
============

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

