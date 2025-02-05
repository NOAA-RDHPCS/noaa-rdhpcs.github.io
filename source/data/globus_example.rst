.. _globus_example:

**************
Globus Example
**************

Globus is the preferred and most efficient and robust way to transfer
data between Globus Collections and Endpoints (also known as DTNs) and
external storage systems. To use this service, you must have an RDHPCS
NOAA account and an RSA SecureID token. You can invoke Globus
functions either through a web interface or from a command line
interface (CLI).  Click the link to access `Globus Documentation
<https://docs.globus.org/guides/>`__.

The following is an example for the purpose of illustration, provided
for people  who need to get data moving from source to destination
without delay.

What you need to have on hand
-----------------------------

* Your NOAA username (First.Last), and your RDHPCS MFA token.
* The name and source of the destination endpoints, e.g.,
  *noaardhpcs#ppan_untrusted*, *noaardhpcs#hera*.
* The file systems exposed to the endpoints (e.g.,
  ``/collab1/data_untrusted``, ``/scratch1/``).

What you need to do
-------------------

1. Navigate to the `Globus Web App <https://app.globus.org>`_
2. Login with an existing organizational login, e.g., *NOAA RDHPCS*.
3. In the Globus File Manager's *Collection* dialog, search for the
   destination endpoint (e.g., *noaardhpcs#ppan_untrusted*).
4. In the *Path* dialog, select the endpoint's file system path (e.g.,
   ``/collab1/data_untrusted/First.Last``).
5. Repeat steps 3 and 4 for the second endpoint.
6. Select the files/directory to transfer.
7. Click the *Start* button.

Using Globus Online Data Transfer
=================================

An endpoint is a file transfer location (computer/server) accessible
to Globus. A collection is a server with a related access method to
files. Untrusted collections can transfer data to and from anywhere.
Trusted collections can transfer data to and from other trusted
collections. When you log into Globus and click Collections, you can
see what collections are shared with you, and also those that you
share with others. Globus lets you navigate through collections to
find source and target endpoints for your transfer, then select
directories or files to be transferred. The transfer itself is a
background process.

To copy a file, several files, or an entire directory between two
systems, navigate to Globus. Locate the source and target endpoints by
their given names and follow these steps:

#. Authenticate yourself to both endpoints.
#. Select the Directory Listing panel for each Endpoint.
#. Pick a directory in each panel for your source and destination.
#. Click START to initiate the transfer.


Globus Connect Service is available on the following RDHPCS and
partner clusters:

**RDHPCS clusters with GCS**

.. list-table::
   :header-rows: 1
   :align: left

   * - Cluster
     - Endpoint Name
     - File System(s)
     - RDHPCS Site
     - Host Access
   * - Ursa
     - noaardhpcs#ursa
     - /scratch3

       /scratch4
     - NESCC
     - Trusted hosts
   * - Hera
     - noaardhpcs#hera
     - /scratch1

       /scratch2
     - NESCC
     - Trusted hosts
   * - Niagara
     - noaardhpcs#niagara
     - /collab1/data
     - NESCC
     - Trusted hosts
   * - Niagara
     - noaardhpcs#niagara_untrusted
     - /collab1/data_untrusted
     - NESCC
     - Anywhere
   * - Jet
     - noaardhpcs#jet
     - /mnt/lfs5

       /mnt/lfs5
     - GSL
     - Trusted hosts
   * - Jet
     - noaardhpcs#jet_untrusted
     - /mnt/lfs5/data_untrusted
     - GSL
     - Anywhere
   * - PPAN
     - noaardhpcs#ppan_rdtn
     - /archive

       /home

       /nbhome

       /work

       /ptmp
     - GFDL
     - Trusted hosts
   * - PPAN
     - noaardhpcs#ppan_untrusted
     - /collab1/data_untrusted
     - GFDL
     - Anywhere
   * - Gaea
     - noaardhpcs#gaea
     - /gpfs/f5

       /gpfs/f6
     - NCRC
     - Anywhere
   * - Orion
     - msuhpc2#Orion-dtn
     - /work

       /work2
     - MSU HPC\ :superscript:`2`
     - Anywhere
   * - Orion
     - msuhpc2#Hercules
     - /work

       /work2
     - MSU HPC\ :superscript:`2`
     - Anywhere
   * - GFDL Data Portal
     - noaagfdl#data portal
     - /data
     - GFDL
     - Anywhere

RDHPCS Object Stores in the Cloud
---------------------------------

+-------------------------------------------+---------------------------------+
| Endpoint/Collection                       | Description                     |
+===========================================+=================================+
| noaardhpcs#cloud_aws_rdhpcs_projects      | AWS Cloud RDHPCS endpoint       |
+-------------------------------------------+---------------------------------+
| noaardhpcs#cloud_azure_rdhpcs_projects    | Azure Cloud RDHPCS endpoint     |
+-------------------------------------------+---------------------------------+
| noaardhpcs#cloud_gcp_rdhpcs_projects      | Google Cloud RDHPCS endpoint    |
+-------------------------------------------+---------------------------------+

External S3 Bucket Connectors
-----------------------------

+---------------------------------------+-------------------------------------+
| Endpoint/Collection                   | Description                         |
+=======================================+=====================================+
| noaardhpcs#cloud_aws_s3_public        | Public AWS S3 connector             |
+---------------------------------------+-------------------------------------+
| noaardhpcs#cloud_aws_s3_authenticated | Non-public managed AWS S3 connector |
+---------------------------------------+-------------------------------------+
| noaardhpcs#cloud_aws_s3_authenticated2| Non-public managed AWS S3 connector |
+---------------------------------------+-------------------------------------+


NOAA RDHPCS Globus Endpoint Types
=================================

NOAA RDHPCS Globus Endpoints are either ‘’trusted’’ or ‘’untrusted’’.

* All RDHPCS systems provide DTN’s
* DTNs have full access to the back-end file systems.
* DTNs only accept connections from pre-authorized sites. If your site
  can’t access the DTNs and you need that capability, submit a help
  desk ticket. If the security team approves, your site will be
  pre-authorized.

.. note::

    It is preferable to use trusted endpoints for data transfer
    whenever possible.

NOAA RDHPCS UDTN’s (Globus Untrusted Endpoint)
==============================================

UDTNs can accept connections and transfer data to and from any
location. UDTNs have access to a specific directory of the back-end
file system, where files can be staged solely for the purpose of
transferring data. Since your project space is not accessible from the
UTDN, transferring data to and from RDHPCS systems using the UDTN’s is
a two-step process.

#. Copy the data out of your project space to the staging area and
   then pull data out of the UDTN from the remote machine.
#. To transfer data back to the RDHPCS system, push the data to the
   UDTN, then copy the file(s) from the staging area to your project
   space.

NOAA RDHPCS Object Stores in the Cloud
======================================

RDHPCS maintains Cloud Stores in Microsoft Azure, Amazon S3, and
Google Cloud.  From the Globus perspective, connecting to these types
of resources is identical to any other endpoints serving DTNs. The
RDHPCS Globus plan offers connectors to access data to and from a
public site available via AWS resources.

Accessing Cloud Endpoints in our environment
============================================

The RDHPCS Globus plan offers connectors so you can access data to from a
public site that makes it available via AWS resources. To use this service you
must login to Globus with your NOAA RDHPCS credentials.


Publicly accessible buckets, no keys required
---------------------------------------------

As an example, let us consider the case where user needs to get files from the
NOAA RRFS expermient from the `AWS Cloud
<https://noaa-rrfs-pds.s3.amazonaws.com/index.html#rrfs_a/rrfs_a.20230725/00/control/>`_.


Go to `<https://registry.opendata.aws/>`_.

In the "Search datasets" field enter the data set of interest, in this case: noaa-rrfs (the first part of the URL of interest)
Click on the results listed in the right pane of the window: This will lead to: `<https://registry.opendata.aws/noaa-rrfs/>`_.

From that web page, copy the last part of the ARN (in this example
noaa-rrfs-pds): arn:aws:s3:::noaa-rrfs-pds Now you have the info you need.


    1. Login to <https://www.globus.org/> with your
       NOAA identity.
    2. In the File Manager window

  - Enter into the "Collection" field: noaardhpcs#cloud_aws_s3_public
  - Enter into the "Path" field:
    /noaa-rrfs-pds/rrfs_a/rrfs_a.20230725/00/control/

Once you are able to see the listing of files you can use the "File Manager" to
move the files between the desired endpoints.

That should do it!

.. note::

  Module globus-cli needs to be loaded before any globus commands are used.

For Globus CLI use, the endpoint UUID is given by:

.. code-block:: shell

  $ globus endpoint search noaardhpcs#cloud_aws_s3_public

You may save the UUID in an environment variable you create, e.g.:
RDHPCS_AWS_PUBLIC. From here on, normal Globus CLI methods will work.

For example, to get a directory listing, type

.. code-block:: shell

  $ globus ls -l $RDHPCS_AWS_PUBIC\:/noaa-rrfs-pds/

#. Navigate to globus.org.
#. Select the “existing organizational login” NOAA RDHPCS. The File
   Manager page displays.
#. Select Collection, and search for NOAARDHPCS# collections.
#. Once you can see the file lists, you can use the “File Manager” to
   move the files between the desired endpoints.

Non-public, secret keys required
--------------------------------
There are non-public sites, curated by the owners. To access the sites,
owners must provide you with two things:

- AWS IAM Access Key ID
- AWS IAM Secret Key

To gain access, you must use a specific endpoint name available through the
RDHPCS subscription.

1. In the File Manager search for and select
   noaardhpcs#cloud_aws_s3_authenticated1 or
   noaardhpcs#cloud_aws_s3_authenticated2

.. note::

  There are endpoints provided to facilitate transfers from one cloud bucket to another in case it is needed.

2. Click on the three vertical dots to the right of the Collection field
3. Select the *Credentials* tab.

If the STATUS column shows *invalid*, click the wrench icon.
Enter the **Access Key ID** and **Secret key**, and hit **Continue**,
and you have access to the contents of the S3 bucket.

.. warning::

  Because the access/secret key combination is specific to only one collection,
  you can only be connected to at most one bucket at a time.

**Change buckets**

If you need to access a different bucket with this mechanism, you must delete
your working AWS Access Credentials first, so you create a different one linked
to the new bucket. As above, when you select the Credentials tab, you will see
the STATUS as active. To remove these credentials, so you can create a new
association with the new access key/secret, click on the trash can
icon.

Globus Command Line Interface (CLI)
===================================

The CLI is available on Jet, Ursa (WIP), Hera, and Niagara. If you would like to
use Globus-cli, either on your personal machine or on a system where
globus-cli is not installed, you can install it easily. Refer to the
instructions to install and use the `Globus CLI
<https://docs.globus.org/cli/>`_.

Transferring Data to and from Your Computer
===========================================

To transfer data from your laptop/workstation to a NOAA RDHPCS system, you can

* use *scp* to a NOAA RDHPCS DTN (using pre-configured SSH port
  tunnels.
* use *scp* to a NOAA RDHPCS UDTN
* use `Globus Connect Personal
  <https://www.globus.org/globus-connect-personal>`_ to transfer data
  between a NOAA RDHPCS UDTN and your local laptop/workstation.

NOAA RDHPCS considers your laptop/workstation as a Globus Untrusted Endpoint.

Some benefits of using Globus Connect Personal with UDTNs:

* Data can be transferred directly between your computer and an
  Untrusted Endpoint.
* Faster transfer rates as compared to scp and sftp.
* Data transfers automatically suspends and resumes as your computer
  goes to sleep, wakes up, or reboots.

The mechanism for transferring data between your laptop/workstation
(Untrusted Endpoint) and a NOAA RDHPCS UDTN is exactly the same. See
`Globus Connect Personal`_ for information about setting up your
laptop/workstation as a Globus Personal Endpoint.

GFDL Institutional Data Portal
==============================

Data hosted on the GFDL Data portal servers is accessible through Globus, and
available on request through the `data hosting request form
<https://docs.google.com/forms/d/e/1FAIpQLScH-2mMLHesN6DJlxLEVU6Kg8wXEKvEr-JgB_5nXchjCDrYww/viewform>`__ for papers,
collaborations, and other projects. The requester will be notified of the
Globus URL when the request is completed. GFDL Data Transfer features can be
reviewed in `this table.
<https://docs.google.com/spreadsheets/d/1fVC60ztNzYxFui1zyF_S_AMfoc3O15oa1-oOKhGrqQI/edit?gid=0#gid=0>`_

.. note::

  Information shared through the GFDL portal is shared permanently.
