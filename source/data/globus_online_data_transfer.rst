.. _globus_online_data_transfer:

***************************
Globus Online Data Transfer
***************************

Globus is the preferred and most efficient way to transfer data
between DTNs and external storage systems. To use this service, you
must have a NOAA login name and a working RSA SecureID token. You can
invoke Globus functions either through a web interface or from a
command line interface (CLI).

* Click here to access `Globus Documentation
  <https://docs.globus.org/guides/>`_.
* Click here to review the `Globus Tutorial
  <https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view>`_

Overview
========

An endpoint is a file transfer location (computer/server) accessible
to Globus. A collection is a server with a related access method to
files. Untrusted collections can transfer data to and from
anywhere.Trusted collections can transfer data to and from other
vetted collections. When you log into Globus and click Collections,
you can see what collections are shared with you, and also those that
you share with others. Globus lets you navigate through collections to
find source and target endpoints for your transfer, then select
directories or files to be transferred. The transfer itself is a
background process.

To copy a file, several files, or an entire directory between two
systems, navigate to `Globus <https://app.globus.org/>`_. Locate the
source and target endpoints by their given names and follow these
steps:

#. Authenticate yourself to both endpoints.
#. Select the Directory Listing panel for each Endpoint.
#. Pick a directory in each panel for your source and destination.
#. Click START to initiate the transfer.

Example
-------

 #. Navigate to globus.org.
 #. Select “existing organizational login" NOAA RDHPCS. The File
    Manager page displays.
 #. Select Collection, and choose the file system
    “noaardhpcs#niagara_untrusted”. If necessary, authenticate with
    username and RSA password.
 #. In the File Manager, select Path:
    /collab1/data_untrusted/anonymous/from Orion
 #. Repeat for the other endpoint: msuhpc2#Orion-dtn
 #. Select files and directories, and click Start.


RDHPCS Globus Collection Summary
--------------------------------

Globus Connect Service is available on the following RDHPCS and
partner clusters.

.. tab-set::

  .. tab-item:: Hera
    :sync: hera

    +-----------+----------------------------+--------------------------+---------+---------------+
    | Cluster   | Display Name               | File Systems             | Site    | Access        |
    +===========+============================+==========================+=========+===============+
    | Hera      | noaardhpcs#hera            | /scratch1, /scratch2     | NESCC   | Trusted hosts |
    +-----------+----------------------------+--------------------------+---------+---------------+
    | Hera      | noaardhpcs#hera_untrusted  | /scratch1/data_untrusted | NESCC   | anywhere      |
    |           |                            | /scratch2/data_untrusted |         |               |
    +-----------+----------------------------+--------------------------+---------+---------------+

  .. tab-item:: Jet
   :sync: jet

   +-----------+----------------------------+--------------------------+---------+---------------+
   | Cluster   | Display Name               | File Systems             | Site    | Access        |
   +===========+============================+==========================+=========+===============+
   | Jet       | noaardhpcs#jet             | /mnt/lfs1, /mnt/lfs4     | NESCC   | Trusted hosts |
   +-----------+----------------------------+--------------------------+---------+---------------+
   | Jet       | noaardhpcs#jet_untrusted   | /mnt/lfs1/data_untrusted | NESCC   | anywhere      |
   |           |                            | /mnt/lfs4/data_untrusted |         |               |
   +-----------+----------------------------+--------------------------+---------+---------------+

  .. tab-item:: Niagara
   :sync: niagara

   +-----------+------------------------------+--------------------------+---------+---------------+
   | Cluster   | Display Name                 | File Systems             | Site    | Access        |
   +===========+==============================+==========================+=========+===============+
   | Niagara   | noaardhpcs#niagara           | /collab1/data            | NESCC   | Trusted hosts |
   +-----------+------------------------------+--------------------------+---------+---------------+
   | Niagara   | noaardhpcs#niagara_untrusted | /mnt/lfs1/data_untrusted | NESCC   | anywhere      |
   +-----------+------------------------------+--------------------------+---------+---------------+


  .. tab-item:: Gaea
   :sync: gaea

   +-----------+-------------------+--------------------+---------+---------------+
   | Cluster   | Display Name      | File Systems       | Site    | Access        |
   +===========+===================+====================+=========+===============+
   | PPAN      | ncrc#dtn          | /gpfs/f5           | NCRC    | Trusted hosts |
   +-----------+-------------------+--------------------+---------+---------------+


.. tab-item:: Orion
   :sync: orion

   +-----------+---------------------+--------------------+-------------------+---------------+
   | Cluster   | Display Name        | File Systems       | Site              | Access        |
   +===========+=====================+====================+===================+===============+
   | orion     | msuhpc2#Orion-dtn   | /work, /work2      | Orion DTN at MSU  | Anywhere      |
   +-----------+---------------------+--------------------+-------------------+---------------+

  .. tab-item:: Hercules
   :sync: hercules

   +-----------+---------------------+--------------------+---------------------+---------------+
   | Cluster   | Display Name        | File Systems       | Site                | Access        |
   +===========+=====================+====================+=====================+===============+
   | Hercules  | msuhpc2#Hercules    | /work, /work2      | Hercules DTN at MSU | Anywhere      |
   +-----------+---------------------+--------------------+---------------------+---------------+


NOAA RDHPCS Globus Endpoint Types
=================================

NOAA RDHPCS Globus Endpoints are either **trusted** or **untrusted**.

.. note::

  It is preferable to use Trusted Endpoints for data transfer.

NOAA RDHPCS DTNs (Globus Trusted Endpoint)
-------------------------------------------

* All RDHPCS systems provide DTNs
* DTNs have full access to the back-end file systems.
* DTNs only accept connections from pre-authorized sites. If your site
  can’t access the DTNs and you need that capability, submit a help
  desk ticket. If the security team approves, your site will be
  pre-authorized.

NOAA RDHPCS UDTNs (Globus Untrusted Endpoint)
---------------------------------------------

UDTNs can accept connections and transfer data to and from any
location.  UDTNs have access to only a specific directory of the
back-end file system, where files can be staged solely for the purpose
of transferring data.

Since your project space is not accessible from the UTDN, transferring
data to and from RDHPCS systems using the UDTN's is a  two-step
process:

#. Copy the data out of your project space to the staging area and
   then pull data out of the UDTN from the remote machine.
#. To transfer data back to the RDHPCS system, push the data to the
   UDTN, then copy the file(s) from the staging area to your project
   space.

NOAA RDHPCS Object Stores in the Cloud
--------------------------------------

RDHPCS maintains Cloud Stores in Microsoft Azure, Amazon S3, and
Google Cloud. From the Globus perspective, connecting to these types
of resources is identical to any other endpoints serving DTNs.

The RDHPCS Globus plan offers connectors to access data to and from a
public site available via AWS resources:

#. Navigate to globus.org.
#. Select “existing organizational login" NOAA RDHPCS. The File
   Manager page displays.
#. Select Collection, and search for NOAARDHPCS# collections.
#. Once you can see the file lists, you can use the "File Manager" to
   move the files between the desired endpoints.

Globus Command Line Interface (CLI)
===================================

The CLI is available on Jet, Hera, and Niagara.

If you would like to use Globus-cli either on your personal machine,
or on a system that doesn't have globus-cli installed, you can install
it easily . Instructions to install and use the Globus CLI are
available `<here https://docs.globus.org/cli/ Globus CLI>`_.

Transferring Data to and from Your Computer
===========================================

To transfer data from your laptop/workstation to a NOAA RDHPCS system,
you have the following options:

* use scp to a NOAA RDHPCS DTN (using pre-configured ssh port tunnels)
* use scp to a NOAA RDHPCS UDTN
* use Globus Connect Personal to transfer data between a NOAA RDHPCS
  UDTN and your local laptop/workstation.

.. note::

  NOAA RDHPCS considers your laptop/workstation a Globus Untrusted
  Endpoint.

Some of the benefits of using Globus Connect Personal with UDTNs:

* Data can be transferred directly between your computer and an
  Untrusted Endpoint.
* Transfer rates are faster, as compared to scp and sftp.
* Data transfers automatically suspends and resumes as your computer
  goes to sleep, wakes up, or reboots.
* The mechanism for transferring data between your laptop/workstation
  (Untrusted Endpoint) and a NOAA RDHPCS UDTN is exactly the same as
  what is described in the rest of this document.

Please see `<Globus Connect Personal
https://www.globus.org/globus-connect-personal>`_ for information
about setting up your laptop/workstation as a Globus Personal
Endpoint.
