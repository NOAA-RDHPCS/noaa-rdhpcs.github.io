.. _globus_online_data_transfer:

***************************
Globus Online Data Transfer
***************************

REVISING GLOBUS DATA TRANSFER 

Globus is the preferred and most efficient way to transfer data between
DTNs and external storage systems. To use this service, you must have a NOAA login name and a working RSA SecureID token. You can invoke Globus functions either through a web interface or from a command line interface (CLI).

Click here to access `Globus Documentation <https://docs.globus.org/guides/>`_.
Click here to review the `Globus Tutorial <https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view>`_

Overview
========

An endpoint is a file transfer location (computer/server) accessible to Globus. A collection is a server with a related access method to files. Untrusted collections can transfer data to and from
anywhere.Trusted collections can transfer data to and from other vetted collections. When you log into Globus and click Collections, you can see what collections are shared with you, and also those that you share with others. Globus lets you navigate through collections to find source and target endpoints for your transfer, then select directories or files to be transferred. The transfer itself is a background process. 

To copy a file, several files, or an entire directory between two systems, navigate to `Globus <https://app.globus.org/>`_.
 Locate the source and target endpoints by their given names and follow these steps:


 #. Authenticate yourself to both endpoints.
 #. Select the Directory Listing panel for each Endpoint.
 #. Pick a directory in each panel for your source and destination.
 #. Click START to initiate the transfer.

Example
-------

 #. Navigate to globus.org.
 #. Select “existing organizational login" NOAA RDHPCS. The File Manager page displays.
 #. Select Collection, and choose the file system “noaardhpcs#niagara_untrusted”. If necessary, authenticate with username and RSA password.
 #. In the File Manager, select Path: /collab1/data_untrusted/anonymous/from Orion
 #. Repeat for the other endpoint: msuhpc2#Orion-dtn
 #. Select files and directories, and click Start.


RDHPCS Globus Collection Summary
================================

Globus Connect Service is available on the following RDHPCS and partner clusters.

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
   | PPAN      | ncrc#dtn          | /lustre/f2/scratch | NCRC    | Trusted hosts |
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

   +-----------+---------------------+--------------------+----------------------+---------------+
   | Cluster   | Display Name        | File Systems       | Site                 | Access        | 
   +===========+=====================+====================+======================+===============+
   | Hercules  | msuhpc2#Hercules    | /work, /work2      | Hercules DTN at MSU  | Anywhere      |
   +-----------+---------------------+--------------------+----------------------+---------------+
