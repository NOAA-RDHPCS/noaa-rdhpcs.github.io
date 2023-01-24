.. _gaea-user-guide:

***************
Gaea User Guide
***************

.. _gaea-system-overview:

.. image:: /images/Gaea_web.jpg

System Overview
===============

`Gaea <https://www.noaa.gov/organization/information-technology/gaea>`_
is an `NOAA Research and Development High-Performance Computing System
(RDHPCS) <https://www.noaa.gov/information-technology/hpcc>`_ operated
by the `National Climate-Computing Research Center (NCRC)
<https://www.ncrc.gov/>`_.  The NCRC is located within the
`National Center for Computational Sciences (NCCS)
<https://www.ornl.gov/division/nccs>`_ at the `Oak Ridge National
Laboratory (ORNL) <https://www.ornl.gov/>`_.   The NCRC is a
collaborative effort between the `Department of Energy
<https://www.energy.gov/>`_ and the `National Atmospheric and Oceanic
Administration <https://www.noaa.gov/>`_.

The Gaea System consists of two HPE Cray XC40 systems, with an
aggregate of more than 200 terabytes of memory and a peak
calculating capacity greater than 5.25 petaflops.

Gaea uses a high-capacity Lustre file system with over 32 petabytes
of storage.  The file system is connected to the Gaea system using
FDR InfiniBand.

.. csv-table:: Gaea Cluster Stats
    :file: /files/gaea_stats.csv
    :header-rows: 1

.. list-table:: Gaea Cluster Stats (list)
    :header-rows: 1

    * - C3
      - C4
      - C5
      - F2 File System
    * - Cray XC40-LC Haswell
      - Cray XC40-LC Broadwell
      - HPE EX Rome
      - DDN Lustre
    * - 1,504 compute nodes
        (2 x Intel Haswell 16-cores per node)
      - 2,656 compute nodes (2 x Intel Broadwell 18-cores per node)
      - 1,792 compute nodes (2 x AMD Rome 64-cores per node)
      - 32 PB total usable; ZFS compression
    * - 64GB DDR4 per node; 96TB total
      - 64GB DDR4 per node; 145TB total
      - 251 GB DDR5 per node; 449TB total
      - 36 OSS; 72 OST; 4 MDS
    * - 1.77 PF peak
      - 3.52 PF peak
      - 27.1 PF peak
      -

.. panels::
    :container: container-lg pb-4
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    C3
    ^^^
    Cray XC40-LC Haswell

    1,504 compute nodes
    (2 x Intel Haswell 16-cores per node)

    64GB DDR4 per node; 96TB total

    1.77 PF peak

    ---

    C4
    ^^^
    Cray XC40-LC Broadwell

    2,656 compute nodes (2 x Intel Broadwell 18-cores per node)

    64GB DDR4 per node; 145TB total

    3.52 PF peak

    ---

    C5
    ^^^
    HPE EX Rome

    1,792 compute nodes (2 x AMD Rome 64-cores per node)

    251 GB DDR5 per node; 449TB total

    27.1 PF peak

    ---

    F2 File System
    ^^^
    DDN Lustre

    32 PB total usable; ZFS compression

    36 OSS; 72 OST; 4 MDS

Connecting
==========

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
**CAC bastions refusing login attempts without asking for PIN**

We have had reports of users being unable to connect to the CAC bastions via TECTIA client. As documented, CAC bastions are the servers you connect to with the sshg3 gaea.rdhpcs.noaa.gov.  They maintain your Globus certificate and put your connection through to the Gaea login nodes. On Linux clients one workaround is to kill the ssh-broker-g3 process and try your login again.

 ---
ps -ef | grep ssh-broker-g3
4060     15451 15184  0 14:05 pts/4    00:00:00 grep ssh-broker-g3
4060     29775 29765  0 Dec22 ?        00:00:42 /opt/tectia/bin/ssh-broker-g3 --run-on-demand
kill -9 29775
sshg3 gaea
 ---

**C3 & C4 shells hang on login &amp; X2Go connections hang at "connecting"**

Users have often reported issues where their sessions freeze or hang on C3 login nodes (gaea9-gaea12) unless Ctrl+c is pressed.

Furthermore, X2Go connections hang (for more than the usual 10 seconds or so) at &quot;connecting&quot;.

This issue can also result in your jobs timing out either at the start of the job or the end.

A fix for this is [https://bugzilla.redhat.com/show_bug.cgi?id=885901 known] to the Linux community but has yet to be released for the Linux distro on Gaea.

The workaround is to delete or move the ~/.history file.

**Potential workaround for current Gaea slowness**

Many jobs on Gaea are currently experiencing longer than normal run times.

One user has gotten his jobs to complete successfully again by increasing io_layout* (thereby decreasing the load on the I/O server/node).

This isn't a guaranteed workaround, but we wanted to share with everyone in case it helps others.
