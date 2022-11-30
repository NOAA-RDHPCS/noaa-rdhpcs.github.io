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