.. _mercury-user-guide:

##################
Mercury User Guide
##################


.. image:: /images/niagara.jpg
   :scale: 25%

.. _mercury-system-overview:

System Overview
===============

Mercury is primarily a data transfer/collaboration system that is available to
all RDHPCS. It is intended to be a collaborative system where data can be
securely copied to and from any location, by any authorized user, to
disseminate Research and Development (R&D) data to NOAA’s collaborators around
the globe.

The Mercury system includes:

- Interactive Login Nodes / Front Ends
- File System
- Data Transfer Nodes
- Back-end storage (HPSS)

Mercury System Features:

- Dual-socket AMD EPYC Genoa 9654, 2.40Ghz, 96 Cores
- 4 Login Nodes
- Trusted Data Transfer Nodes (DTNs) available from trusted (pre-approved)
  NOAA and non-NOAA sites
- Untrusted Data Transfer Nodes (UDTNs) available from anywhere on the internet

.. note::

   No compute nodes are available on Mercury.

Interactive Logins
==================

The Mercury front ends may be accessed using either CAC or
RSA credentials. Host names for CAC and RSA access can be found in the
:ref:`bastion_hostnames` table.

Data Transfer
=============

Data transfer instructions can be found on the
`Transferring Data page <https://docs.rdhpcs.noaa.gov/data/transferring_data.html#transferring-data>`_.

In order to use Mercury for file transfers, user account directories must be in
place. These directories are automatically created with your first login to a
Mercury front end.  The following directories will automatically be created
with your first login:

  - ``/home/First.Last`` (your home directory)
  - ``/collab2/data/First.Last`` (for your trusted data)
  - ``/collab2/data_untrusted/First.Last`` (for your untrusted data)

When you use the DTNs for data transfers:

  - ``/home`` tree is not accessible from the DTNs.
  - ``/collab2/data/`` tree is accessible from the DTNs and uDTNs.
  - ``/collab2/data_untrusted`` tree is only accessible from the uDTNs,
    but will be visible on the uDTNs as ``/collab2/$USER``.

Per User Data Management on Mercury
===================================

Below are the data management policies for Mercury:

- All files under the ``/collab2/data_untrusted/$USER`` directory tree which
  have not been accessed in the last 14 days will be automatically purged.
- All files under the ``/collab2/data/$USER`` directory tree which have not
  been accessed in the last 60 days will be automatically purged.

A default 10GB quota on each user’s home directory ``/home/$USER``.

.. note::

   Access time is defined as the last time the file was opened for reading or
   writing. If the file system’s usage starts getting close to the total
   capacity then we will be forced to implement a more aggressive purge policy
   (i.e., 30 day or 15 day purge). Please actively manage your data.


Software Stack
==============

Mercury has a minimal software stack for compiling and running
programs, as this system is primarily intended for data transfers and data
sharing. Please open a help ticket for additional information on the software
stack.

CRON Services
=============

CRON services are available on Mercury. See `the CRON page
<https://docs.rdhpcs.noaa.gov/software/workflows/cron/index.html#cron>`_
for additional information on how to use CRON.

HPSS Access
===========

HPSS is accessible. See the
`NESCC HPSS page <https://docs.rdhpcs.noaa.gov/data/nescc_hpss.html>`_
for additional information.

Getting Help
============

Please see the `Help page <https://docs.rdhpcs.noaa.gov/help/index.html>`_
for more information on how to get help for Mercury.

