.. _niagara-user-guide:

******************
Niagara User Guide
******************

.. _niagara-system-overview:

System Overview
===============
As NOAA's R&D severe weather and climate projects expand  to geographically dispersed private and public HPC clouds, it is imperative that the the NOAA RDHPCS program provide a service for data dissemination and analysis outside of the traditional HPC environment. The Niagara system is intended to be a collaborative location where data can be securely copied to and from any location, by any authorized user. It can also be used to disseminate R&D data to NOAA's collaborators around the globe.

The Niagara system includes:

- Back-end storage
- Data Transfer Nodes
- Interactive Nodes
- Software
- Account Management.

Users can connect to the Data Transfer Nodes (DTN) from any remote system to push or pull data. Beyond the Back-end storage and DTNs, the cluster allows for data analysis, visualization, verification, validation and data analytics. It is provided through a combination of hardware and software, which mirrors the user environment and a subset of the tools available on the legacy RDHPCS systems (Hera & Jet) and legacy Analysis systems (PPAN), but can also include software which is unique to this system and not traditionally found on traditional HPC systems.

Niagara System Features:

- 20 cores/socket, 2.5 GHz, 2 sockets/nodes
- 12 Login Nodes
- 25 Compute Nodes
- 2 DTNs available from trusted (pre-approved) NOAA and non-NOAA sites
- 2 Untrusted Data Transfer Nodes (UDTNs) available from anywhere on the internet
- 2 Web servers

Connecting
==========

Data Transfer
================

In order to use Niagara for file transfers, your must create user account directories. These directories are automatically created with your first login to a Niagara front end. The Niagara front ends may be accessed using either CAC or RSA credentials. Host names for CAC access can be found on this CAC login page. Host names for RSA access can be found on this RSA login page.

The following directories will automatically be created with your first login:

- /home/First.Last (your home directory)
- /collab1/data/First.Last (for your trusted data)
- /collab1/data_untrusted/First.Last(for your untrusted data)

.. note::

    When using the DTNs for data transfers:

- /home tree is not accessible from the DTNs
- /collab1/data/ tree is only accessible from the "Trusted DTN".
- /clooab1/data_untrusted tree is only accessible from the "Untrusted DTN"

    Per User Data Management on Niagara:

As Niagara is a hybrid system, a cross between a traditional HPC system and a data transfer/collaboration system, available to all RDHPCS users, the file system management needs to be handled differently then our more traditional HPC systems (Hera and Jet). The following are data management policies:

- All files under the "/collab1/data_untrusted/$USER" directory tree which have not been accessed in the last 5 days will be automatically purged.
- All files under the "/collab1/data/$USER" directory tree which have not been accessed in the last 60 days will be automatically purged.

Access time is defined as the last time the file was opened for reading or writing.

.. note::

If the file system's usage starts getting close to the total capacity then we will be forced implement a more aggressive purge policy (i.e., 30 day or 15 day purge) . So please actively manage your data.

- A default 10GB Lustre quota on each user's home directory "/collab1/home/$USER" .

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
