.. _HSMS_user-guide:

********************
HSMS HPSS User Guide
********************

NESCC HPSS
==========
The centralized, long-term data archive system at National
Environmental Security Computing Center (NESCC) is based on IBM's High
Performance Storage System (HPSS). The NESCC HPSS environment includes
22 petabytes of front-end disk cache, five Oracle SL8500 enterprise
tape libraries, three Spectra Logic TFinity tape libraries, and 148
tape drives. Total available capacity is 430 PB. HPSS is accessible
from WCOSS2, Hera, Niagara, Jet, and Gaea.

Users should keep the following things in mind when using the HPSS
system:

- The HPSS system is well suited for storing large volumes of data.
- Users should avoid transferring many small files (in the megabyte
  range or smaller) to HPSS since the process of moving numerous
  individual small files to and from tape is inefficient. Please tar
  up small files into one large tar file before storing data into
  HPSS, or use HTAR.
- All data stored in HPSS is single copy. Deleted data cannot be
  recovered.
- HPSS is not accessible from compute nodes. Access is available via
  Hera/Niagara/Jet front-end nodes (FEs), Gaea Data Transfer Nodes
  (DTN’s), and WCOSS2 transfer nodes.
- Batch jobs that require access to HPSS should be submitted to the
  respective systems service or transfer queues.

For questions regarding the HPSS system, email
rdhpcs.hpss.help@noaa.gov.

Gaining Access to use HPSS
==========================

New HPSS User Requests
----------------------

A HPSS user must be a current user of a NOAA HPC compute resource
(RDHPC or WCOSS) to have access to HPSS. Access to an HPSS project
must be requested. When you are a member of a project on a compute
resource you are not automatically added to the companion HPSS project
(if there is one). Being added to a HPSS project that you are already
a member of on a NOAA compute resource is done without PI or Portfolio
Manager approval, but both are notified that you are being added. If
you are not a member of the project on a NOAA compute resource then PI
or Portfolio manager approval is required before you will be added. To
expedite the process please send an email to:
rdhpcs.hpss.help@noaa.gov. with the following subject line, replacing
USERNAME and PORTFOLIO/PROJECT with your username and project request.

**<$USERNAME> requests access to HPSS - <PORTFOLIO/PROJECT(S)**

Example:

Jane.Doe requests access to HPSS - /BMC/chimera

.. note::

    If PI or Portfolio Manager approval is required, the email should
    come from them.



All requests must have the following information:

- User Name
- Requested Project(s) - See NESCC HPSS Data Structure for available
  HPSS projects
- System HPSS Access is Needed From (Hera/Jet/Niagara/Gaea/WCOSS)


Adding New Projects to HPSS
---------------------------

Projects on a NOAA compute resource are not given access to the HPSS
until requested by the Portfolio Manager (PfM). The PfM also approves
the maximum time retention directory (pool) that a project is allowed
to use on HPSS. All lesser time pools will also be available. To add a
project to the HPSS the Portfolio Manager should submit a help request
with the following information:

- Project name, associated users, maximum time retention pool

To remove a project from the HPSS, the PfM should submit a help
request with the project name and data disposition directions.
Requests are reviewed and approved by the HPSS Resource Manager and
sent to the HPSS system administrator for implementation.

.. note::

    Requests for adding users and projects to HPSS are NOT supported
    in AIM. Instead, the request/review/implementation/notification
    process is handled by the HPSS help ticket system. Email:
    rdhpcs.hpss.help@noaa.gov.

NESCC HPSS Data Structure
-------------------------

HPSS data at NESCC is organized by portfolio, project and retention
period. Each retention period (1-5 Year & Permanent) is set up as a
separate file family. This means that all data for a retention period
is stored on the same tapes. Projects live under the appropriate
portfolio and have been assigned access to specific retention
directories. Project users have access to write data to any of their
projects' retention directories. Data within the same retention
directory (/1-5 Year & /Permanent) can be moved to other projects
within the same retention directory. If data needs to be moved to
another retention period (ex: /1year -> /2year) it must be copied.

.. note::

    Please be sure to store the data you write to HPSS in the
    appropriate retention directory, and in the correct project if you
    belong to multiple projects. This will avoid movement of data once
    it is stored on tape.


**/$PORTFOLIO/$PROJECT/$RETENTION**

(ex: /BMC/wrf-chem/2year or /NCEPDEV/emc-meso/5year)

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
         * gsienkf
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

Data Retention
==============

Retention based storage is the HPSS archive policy in Fairmont, to
better manage data growth. Six retention storage pools (1-5year and
Permanent) were created. Each retention period is setup as a separate
file family. This means all data for a retention period is stored on
the same tapes. All HPSS projects were then configured to write to one
or more of these pools. Data in these pools expires based upon the
retention pool it was written in and would be deleted upon expiration.
All files in the HPSS archive have been assigned an expiration date
based on the file create time and the retention period it was written
to. Upon expiration files will be deleted from the HPSS archive.

Expired Data Deletion Process
-----------------------------

**User Notification**

Users will be notified of expired data via posted lists and email.
These notifications will take place on or before the first day of the
month following the data’s expiration. For example, data that has an
expiration date between October 1 and October 31 2016 will have its
notification posted on or before November 1, 2016. The expired file
list is located on HPSS in /Expired_Data_Lists/expired.YYYY-MM.txt.
All HPSS users have read access to this file and can retrieve it for
review. The file is easily searchable by HPSS username. For each file
included in the expired list the file owner, file group,
filename/path, and expire date are shown. ex: root system
/1year/SYSADMIN/nesccmgmt/test_file-1G-11 Jul-6-2023. Email
notification will also be sent to all users who have data listed in
this file. It is the user’s responsibility to regularly check the
posted list for expired files they own. Once deleted these files
cannot be recovered.

**Expired Data - Deletions**

The following table lays out the timing for deletions.
