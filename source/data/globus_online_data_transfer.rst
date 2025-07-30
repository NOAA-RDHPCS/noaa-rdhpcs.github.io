.. _globus_online_data_transfer:

***************************
Globus Online Data Transfer
***************************

Globus is the preferred and most efficient way to transfer data
between DTNs and external storage systems. To use this service, you
must have a NOAA login name and a working RSA SecureID token. You can
invoke Globus functions either through a web interface or from a
command line interface (CLI).

Click here to access `Globus Documentation <https://docs.globus.org/guides/>`_.
Click here to review the `Globus Tutorial <https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view>`_

Overview
========

An endpoint is a file transfer location (computer/server) accessible
to Globus. A collection is a server with a related access method to
files. Untrusted collections can transfer data to and from anywhere.
Trusted collections can transfer data to and from other vetted
collections. When you log into Globus and click Collections, you can
see what collections are shared with you, and also those that you
share with others. Globus lets you navigate through collections to
find source and target endpoints for your transfer, then select
directories or files to be transferred. The transfer itself is a
background process.

To copy a file, several files, or an entire directory between two systems, navigate to `Globus <https://app.globus.org/>`_.
 Locate the source and target endpoints by their given names and
 follow these steps:


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
    “noaardhpcs#mercury_untrusted”. If necessary, authenticate with
    username and RSA password.
 #. In the File Manager, select Path:
    /collab1/data_untrusted/anonymous/from Orion
 #. Repeat for the other endpoint: msuhpc2#Orion-dtn
 #. Select files and directories, and click Start.

.. _globus_collection_summary:

RDHPCS Globus Collection Summary
================================

Globus Connect Service is available on the following RDHPCS and
partner clusters.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Cluster
     - Display Name
     - File Systems
     - Site
     - Access
   * - PPAN
     - noaardhpcs#ppan
       noaardhpcs#ppan_untrusted
     - /archive, /home, /nbhome, /work, /xtmp
       /collab1/data_untrusted
     - GFDL
     - Trusted hosts
       Anywhere
   * - Ursa
     - noaardhpcs#ursa
       noaardhpcs#ursa_untrusted
     - /scratch3, /scratch4
       /scratch3/data_untrusted, /scratch4/data_untrusted
     - NESCC
     - Trusted hosts
       Anywhere
   * - Gaea
     - | noaardhpcs#gaea
       | noaardhpcs#gaea_f6
     - | /gpfs/f5, $HOME
       | /gpfs/f6, $HOME
     - NCRC
     - Anywhere
   * - Hera
     - noaardhpcs#hera
       noaardhpcs#hera_untrusted
     - /scratch1, /scratch2
       /scratch1/data_untrusted, /scratch2/data_untrusted
     - NESCC
     - Trusted Hosts
       Anywhere
   * - Jet
     - | noaardhpcs#jet
       | noaardhpcs#jet_untrusted
     - | /mnt/lfs[5,6]
       | /mnt/lfs[5,6]/data_untrusted
     - GSL
     - Trusted hosts
       Anywhere
   * - Mercury
     - noaardhpcs#mercury
       noaardhpcs#mercury_untrusted
     - | /collab2/data
       | /collab2/data_untrusted
     - NESCC
     - Trusted hosts
       Anywhere
   * - Orion
     - msuhpc2#orion-dtn
     - /work, /work2
     - Orion DTN at MSU
     - Anywhere
   * - Hercules
     - msuhpc2#hercules
     - /work, /work2
     - Hercules DTN at MSU
     - Anywhere

NOAA RDHPCS Globus Endpoint Types
=================================

.. Note::

  It is preferable to use Trusted Endpoints for data transfer.

NOAA RDHPCS Globus Endpoints are either ''trusted'' or ''untrusted''.

* All RDHPCS systems provide DTN's
* DTNs have full access to the back-end file systems.
* DTNs only accept connections from pre-authorized sites. If your site
  can't access the DTNs and you need that capability, submit a help
  desk ticket. If the security team approves, your site will be
  pre-authorized.

NOAA RDHPCS UDTN's (Globus Untrusted Endpoint)
----------------------------------------------

UDTNs can accept connections and transfer data to and from any
location.  UDTNs have access to a specific directory of the back-end
file system, where files can be staged solely for the purpose of
transferring data.

Since your project space is not accessible from the UTDN, transferring
data to and from RDHPCS systems using the UDTN's is a two-step
process.

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
public site available via AWS resources.

#. Navigate to globus.org.
#. Select “existing organizational login" NOAA RDHPCS. The File
   Manager page displays.
#. Select Collection, and search for NOAARDHPCS# collections.
#. Once you can see the file lists, you can use the "File Manager" to
   move the files between the desired endpoints.

Globus Command Line Interface (CLI)
===================================

Globus CLI is available on Jet, Ursa, Hera, and Mercury.
Please load the "globus-cli" module by running the command:

.. code-block:: shell

    $ module load globus-cli

The above module also defines environment variables for the UUIDs
of some of the Globus endpoints that are commonly used by RDHPCS users.
Please run  the command:

.. code-block:: shell

    $ module show globus-cli

to see the environment variables that are defined when
you load the above module.

If you would like to use Globus-cli, either on your personal machine
or on a system where globus-cli is not installed, you can install it
easily . Instructions to install and use the Globus CLI are available
in the Globus documentation `CLI section <https://docs.globus.org/cli>`_.

Transferring Data to and from Your Computer
===========================================

To transfer data from your laptop/workstation to a NOAA RDHPCS system, you can

* Use Globus Connect Personal to transfer data between a NOAA RDHPCS
  UDTN and your local laptop/workstation.
* Use ``scp`` to a NOAA RDHPCS UDTN, using configured ssh port tunnels.
* Use ``scp`` to a NOAA RDHPCS UDTN where permitted (Jet, Hera)

.. note::

  NOAA RDHPCS considers your laptop/workstation a Globus Untrusted Endpoint.

Benefits of using Globus Connect Personal with UDTNs:

* Data can be transferred directly between your computer and an
  Untrusted Endpoint.
* Much faster transfer rates compared to ``scp`` and ``sftp``.
* Data transfers automatically suspend and resume as your computer
  goes to sleep, wakes up, or reboots.
* The mechanism for transferring data between your laptop/workstation
  (Untrusted Endpoint) and a NOAA RDHPCS UDTN is exactly the same.

Please see `Globus Connect Personal
<https://www.globus.org/globus-connect-personal>`_ for information
about setting up your laptop/workstation as a Globus Personal
Endpoint.

.. warning::

    Please note the following warnings when using the Globus Online transfers.

    * Globus transfers do not preserve file permissions. Arriving files will
      have (rw-r-r-) permissions, meaning arriving files will have user read
      and write permissions and group and world read permissions. Note that the
      arriving files will not have any execute permissions, so you will need to
      use chmod to reset execute permissions before running a
      Globus-transferred executable.
    * Globus will overwrite files at the destination with identically named
      source files. This is done without warning.
    * Globus has restriction of 8 active transfers across all the users. Each
      user has a limit of 3 active transfers, so it is required to transfer a
      lot of data on each transfer than less data across many transfers.
    * If a folder is constituted with mixed files including thousands of small
      files (less than 1MB each one), it would be better to tar the small files.
      Otherwise, if the files are larger, Globus will handle them.

Data Sharing with External Collaborators
========================================

.. Note::

  For a more complete discussion, see :ref:`transferring-data`.

RDHPCS users can share data with external collaborators who do not have
accounts on the RDHPCS system. You can share data files with external
collaborators, both inbound and outbound, using the Untrusted DTNs (UDTNs). The
process is described in this section.

**For data that is short-lived**, and not broadly shared with external users
use RDHPCS end-points.

**For data that is expected to be available for three 3 months
or more**, use the :ref:`institutional_data_portal` end-point.

**For data that is expected to be permanent** (e.g., >3 months), use the GFDL
institutional data portal end-point (noaagfdl#data_portal). This is for
outbound sharing of data only. The data group will provide a Globus url to
the data hosted upon completion of the data hosting.

Data hosted on the GFDL Data portal servers is accessible through Globus, and
available on request through the `data hosting request form
<https://docs.google.com/forms/d/e/1FAIpQLScH-2mMLHesN6DJlxLEVU6Kg8wXEKvEr-JgB_5nXchjCDrYww/viewform>`__
for papers, collaborations, and other projects. The requester will be notified
of the Globus URL when the request is completed. GFDL Data Transfer features
can be reviewed in `this table.
<https://docs.google.com/spreadsheets/d/1fVC60ztNzYxFui1zyF_S_AMfoc3O15oa1-oOKhGrqQI/edit?gid=0#gid=0>`_

For assistance, contact the GFDL team at oar.gfdl.dpteam@noaa.gov.

.. note::

  Refer to the `GFDL FAIR use and GFDL Data DOI policy
  <https://www.gfdl.noaa.gov/fair-use-policy/>`_ for external data sharing.

.. Note::

  * This data sharing feature is only available only on *untrusted*
    Globus endpoints (UDTNs).
  * You **must** share the collection with your collaborators.
    **THERE IS CURRENTLY NO PUBLIC SHARING AVAILABLE.**   You can share to an
    email address or a GlobusID.
  * You can only share directories under your ``/*/data_untrusted/$USER`` directory.
  * Before any sharing can be done, the user that is sharing the data
    must login to the system (Mercury, Ursa (WIP), Hera, Jet, ...) at least once,
    to make sure that the account is properly set up the with the necessary
    home and project directories.
  * It may be necessary to create (``mkdir``) your ``/*/data_untrusted/$USER``
    directory, depending on the system.

Refer to the :ref:`Globus Collection Summary <globus_collection_summary>` to
find the names of relevant Globus
Collections, and the exposed directory names.

How to Share Data
-----------------

The Globus web site provides complete instructions for sharing
your data. Click here for `file sharing instructions. <https://docs.globus.org/how-to/share-files/>`_

When you log into the Globus web site and click **Collections**, you can see
what collections are shared with you, and also those that you share with
others.
