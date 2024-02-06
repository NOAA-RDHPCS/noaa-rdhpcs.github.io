.. _globus_online_data_transfer:

***************************
Globus Online Data Transfer
***************************

Globus is the preferred and most efficient way to transfer data between DTNs, as well as external storage systems, such
as NCAR. Globus's functions can be invoked through a web interface using a browser, and also from a command line
interface (CLI). To use this service, you must have a NOAA login name and a working RSA SecureID token (hardware fob,
or soft token on smart phone).


.. _globus_quickstart:

==================
Globus Quick Start
==================

This section is for people in a hurry who need to get things
(data) moving from their source to destination without
delay.

There are a few basic, and very important things you need to
know. A common unexpected consequence of an otherwise
successully executed transfer request may be several
"missing files" after completion. Please note that Globus
skips symbolic links almost all the time. For more
information, please see Globus's FAQ section on this topic
at
https://docs.globus.org/faq/transfer-sharing/#how_does_globus_handle_symlinks

The following is only an example for illustration purposes.

+-----------------------------------+-----------------------------------+
| The name of the source and        | noaardhpcs#niagara_untrusted      |
| destination endpoints             | noaardhpcs#hera                   |
+-----------------------------------+-----------------------------------+
| Your NOAA username                | John.Smith                        |
+-----------------------------------+-----------------------------------+
| The names of filesystems exposed  | /collab1/data_untrusted/          |
| by the endpoints, respectively    | /scratch1/                        |
+-----------------------------------+-----------------------------------+

Steps to initiate a transfer request:

+-----------------------------------+-----------------------------------+
| Navigate your browser to this     | globus.org                        |
| address                           |                                   |
+-----------------------------------+-----------------------------------+
| Login with "existing              | NOAA RDHPCS                       |
| organizational login"             |                                   |
+-----------------------------------+-----------------------------------+
| In the File Manager, select       | noaardhpcs#niagara_untrusted      |
| Collection                        |                                   |
+-----------------------------------+-----------------------------------+
| If needed, authenticate yourself  | Username and RSA passcode         |
| to the endpoint                   |                                   |
+-----------------------------------+-----------------------------------+
| In the File Manager, select Path  | /coll                             |
|                                   | ab1/data_untrusted/John.Smith/... |
+-----------------------------------+-----------------------------------+
| Repeat for other endpoint         | noaardhpcs#hera                   |
|                                   | /scratch1/NCEPDEV/...             |
+-----------------------------------+-----------------------------------+
| Select the files/directories and  | Hit the Start button              |
| initiate transfer                 |                                   |
+-----------------------------------+-----------------------------------+

.. _rdhpcs_globus_collection:

========================
RDHPCS Globus Collection
========================

Globus Connect Service is available on the following RDHPCS
and partner clusters.

.. csv-table:: RDHPCS clusters with GCS
    :file: /files/globus_collections.csv
    :header-rows: 1

.. table:: External Endpoints trusted by RDHPCS

   =================== ============================================
   Endpoint/Collection Description
   =================== ============================================
   NCAR GLADE          Globus endpoint serving the Cheyenne cluster
   =================== ============================================

.. table:: RDHPCS Object Stores in the Cloud

   ====================================== ============================
   Endpoint/Collection                    Description
   ====================================== ============================
   noaardhpcs#cloud_aws_rdhpcs_projects   AWS Cloud RDHPCS endpoint
   noaardhpcs#cloud_azure_rdhpcs_projects Azure Cloud RDHPCS endpoint
   noaardhpcs#cloud_gcp_rdhpcs_projects   Google Cloud RDHPCS endpoint
   ====================================== ============================

|

.. table:: External S3 bucket connectors

   ============================== ===================================
   Endpoint/Collection            Description
   ============================== ===================================
   noaardhpcs#cloud_aws_s3_public Public AWS S3 connector
   noaardhpcs#cloud_aws_s3        Non-public managed AWS S3 connector
   ============================== ===================================

An *endpoint* is a file transfer location (computer/server)
accessible to Globus. If you want to copy a file, several
files, or an entire directory between two systems, you would
use your browser to connect to the Globus app,
https://app.globus.org/ locate the two endpoints by their
given names and follow the below steps:

-  Authenticate yourself to both endpoints using the proper
   method (userid, password, RSA token, etc.).
-  Select the Directory Listing panel for each of the two
   Endpoints.
-  Pick a directory in each panel for your *source* and
   *destination*, respectively.
-  Click a button to initiate the transfer.

Once the above steps are completed, the movement of data
will be managed and supervised in the background. You may
close the browser or leave the browser open. The current
status of your request is displayed if you need it. When the
transfer is complete, you will be notified by email.

.. _noaa_rdhpcs_globus_endpoint_types:

=================================
NOAA RDHPCS Globus Endpoint Types
=================================

Similarly to DTNs, NOAA RDHPCS Globus Endpoints are either
*trusted* or *untrusted*

.. _noaa_rdhpcs_dtn_globus_trusted_endpoint:

NOAA RDHPCS DTN's (Globus Trusted Endpoint)
===========================================

-  DTN's will only accept connections from pre-authorized
   sites. If your site can access the DTN's, this is the
   preferred method of transferring the data.
-  DTN's have full access to the back-end file systems
   (please note: /home is not accessible, only the scratch
   file systems are).
-  If your site is not able to access the DTNs and you need
   the capability to regularly transfer data using the DTNs,
   please submit a help desk ticket so that it can added to
   the list of pre-authorized sites if approved by the
   security team.
-  All the RDHPCS systems provide DTN's.

.. _noaa_rdhpcs_dtn_globus_untrusted_endpoint:

NOAA RDHPCS DTN's (Globus Untrusted Endpoint)
=============================================

-  Unlike DTN's which are accessible only from
   pre-authorized sites, UDTN's can accept connections and
   transfer data to and from any location.
-  The UDTN's have access to only a specific directory of
   the back-end file system, where files can be staged only
   for the purpose of transferring data.
-  Since your project space is not accessible from the UTDN,
   generally transferring data to and from RDHPCS systems
   using the UDTN's is a 2-step process.
-  Not cleaning up your files on the uDTN's is considered a
   policy violation and appropriate action may be taken.

   -  To transfer the data out of the RDHPCS system you have
      to copy the data from your project space to the
      staging area and then pull data out of the UDTN from
      the remote machine.
   -  To transfer the data on to the RDHPCS system, you have
      to push the data to the UDTN, and then copy the
      file(s) from the staging area to your project space.

-  Currently only the Niagara system provides UDTN Globus
   Endpoint.

.. _noaa_rdhpcs_object_stores_in_the_cloud:

NOAA RDHPCS Object Stores in the Cloud
======================================

There are three types of cloud storage maintained by RDHPCS:
Microsoft Azure, Amazon S3, Google Cloud. From Globus's
perspective, connecting to these types of resources is
identical to *normal* endpoints serving DTNs.

.. _accessing-cloud-endpoints-in-our-environment:

============================================
Accessing cloud endpoints in our environment
============================================

The RDHPCS Globus plan offers connectors so you can access
data to from a public site that makes it available via AWS
resources. To use this service you must login to Globus with
your NOAA RDHPCS credentials.

.. _publicly-accessible-buckets-no-keys-required:

Publicly accessible buckets, no keys required
=============================================

As an example, let us consider the case where user needs to
get files from the NOAA RRFS expermient from the AWS Cloud
and has the following URL:

https://noaa-rrfs-pds.s3.amazonaws.com/index.html#rrfs_a/rrfs_a.20230725/00/control/

|
| Go to: https://registry.opendata.aws/

In the "Serach datasets" field enter the data set of
interest, in this case: **noaa-rrfs** (the first part of the
URL of interest)

Click on the results listed in the right pane of the window:
This will lead to: https://registry.opendata.aws/noaa-rrfs/

(Note: Alternatively you can simply "guess" the URL based on
the above pattern)

From that web page copy the **last part** of the ARN (in
this example **noaa-rrfs-pds**): arn:aws:s3:::noaa-rrfs-pds

|

Now you have the info you need.

-  Login to https://www.globus.org/ with your NOAA identity.
-  In the File Manager window

#. Enter into the "Collection" field:
   **noaardhpcs#cloud_aws_s3_public**
#. Enter into the "Path" field:
   **/noaa-rrfs-pds/rrfs_a/rrfs_a.20230725/00/control/**

Once you are able to see the listing of files you can use
the "File Manager" to move the files between the desired
endpoints. If you are new to Globus, please see the
following for general information on how to transfer files
using Globus:

https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer#Using_Globus_Connect

That should do it!

For Globus CLI use, the endpoint UUID is given by (**please
note:** Module **globus-cli** needs to be loaded before any
globus commands are used)

::

   $ globus endpoint search noaardhpcs#cloud_aws_s3_public

You may save the UUID in an environment variable you create,
e.g.: ``RDHPCS_AWS_PUBLIC``. From here on, normal Globus CLI
methods will work. For example, to get a directory listing,
type

::

   $ globus ls -l $RDHPCS_AWS_PUBIC\:/noaa-rrfs-pds/

.. _non-public-keysecret-required:

Non-public, key/secret required
===============================

These are non-public sites, curated by the owners, who must
provide you with two things:

-  AWS IAM Access Key ID
-  AWS IAM Secret Key

To gain access, you must use a specific endpoint name
available through the RDHPCS subscription.

#. In the File Manager search for and select
   ``noaardhpcs#cloud_aws_s3``
#. Click on the three vertical dots to the right of the
   Collection field
#. Select the *Credentials* tab

| If the STATUS column has *invalid*, click on the spanner
  (wrench) icon near the right edge of the window
| Enter the **Access Key ID** and **Secret key** and hit the
  **Continue** button, and you have access to the contents
  of the S3 bucket.

**CAVEAT:** Because the access/secret key combination is
specific to only one collection, you can only be connected
to at most one bucket at a time.

**CHANGE BUCKETS** If you need to access a different bucket
with this mechanism, you must delete your AWS Access
Credentials first, so you create a different one linked to
the new bucket. As above, when you select the *Credentials*
tab, you will see the STATUS as *active*. To remove these
credentials, so you can create a new association with the
new access key/secret, click on the dust bin (trash can)
icon.

.. _transferring-data-to-and-from-external-sites:

============================================
Transferring Data to and from External Sites
============================================

Globus Connect can only be used to transfer data to and from
sites who also have Globus Connect subscriptions. The
easiest way to determine if an external site supports Globus
Connect is to search for that organization's Endpoints.
Reference the section below on "How to Find, Select, and
Browse Globus Endpoints".

.. _transferring-data-to-and-from-your-computer:

===========================================
Transferring Data to and from Your Computer
===========================================

To transfer data from your laptop/workstation to a NOAA
RDHPCS system, you can either use scp to a NOAA RDHPCS DTN
(using pre-configured ssh port tunnels), use scp to a NOAA
RDHPCS UDTN (Niagara only), or you can use Globus Connect
Personal to transfer data between a NOAA RDHPCS UDTN and
your local laptop/workstation. NOTE: NOAA RDHPCS considers
your laptop/workstation a Globus Untrusted Endpoint. Some of
the benefits of using Globus Connect Personal with UDTNs:

-  Data can be transferred directly between your computer
   and an Untrusted Endpoint.
-  Faster transfer rates as compared to scp and sftp.
-  Data transfers automatically suspends and resumes as your
   computer goes to sleep, wakes up, or reboots.
-  The mechanism for transferring data between your
   laptop/workstation (Untrusted Endpoint) and a NOAA RDHPCS
   UDTN is exactly the same as what is described in the rest
   of this document.

Please see `Globus Connect
Personal <https://www.globus.org/globus-connect-personal>`__
for information about setting up your laptop/workstation as
a Globus Personal Endpoint.

.. _data-sharing-with-external-collaborators:

========================================
Data Sharing With External Collaborators
========================================

This section addresses the problem of how to get users from
the outside whom you trust to either send or receive data
from selected directories.

It is possible to share data files with your collaborators,
both inbound and outbound, using the "Untrusted DTNs" or
"UDTNs" even if they do not have login privileges on RDHPCS
computers. This will allow RDHPCS users to share data with
their external collaborators that do not have accounts on
the RDHPCS systems.

Please note the following:

-  This data sharing feature is currently available only on
   so-called *untrusted* Globus endpoints.
-  Sharing happens at directory level and not at the level
   of individual files.
-  You can only share directories under the root of the
   "``/*/data_untrusted/$USER``" directory. All uDTNs have
   that directory.
-  The person with whom you share should have a GlobusID; do
   not share based only on an email address.
-  Before any sharing can be done, it is necessary for the
   user that is sharing the data to login to the system
   (Niagara, Hera, Jet, ...) at least once so that the
   account is properly set up the with the necessary home
   and project directories.
-  **Please refer to the following link for more details on
   untrusted Globus collections, purge policy details:
   [**\ `Untrusted Transfer
   Nodes <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Transferring_Data#Untrusted_Data_Transfer_Nodes_.28.22udtn.22s.29>`__\ **]**
   Here you will find the names of relevant Globus
   Collections, and the exposed directory names.

|

.. _how-to-share-data:

How To Share Data
=================

            The Globus web site as excellent documentation on the steps
            involved in sharing your data. Instead of replicating those
            instructions we are including the link to their instructions
            here:

            https://docs.globus.org/how-to/share-files/

            By logging into the Globus web site and clicking on
            "Collections" you should be able to see what collections are
            shared with you, and also those that you share with others.
            The next Section has more detail about using Globus.

.. _using-globus-connect:

====================
Using Globus Connect
====================

The RDHPCS program deployed Globus Connect Services (GCS)
across several sites. This service allows users to use a web
based interface, or a command-line utility for transferring
data between sites supported by GCS.

.. _globus-tutorials-and-training:

Tutorials and Training Materials
================================

`Intro to GCS <https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view>`__

`Instructional videos by Globus <https://docs.globus.org/how-to/instructional-videos>`__
offers some very useful tutorials.

This `"how-to" link <https://docs.globus.org/how-to/>`__
provides high quality online tutorials from Globus for end
users and administrators.

.. _login-and-navigate-the-globus-site:

Login and Navigate the Globus Site
==================================

You should identify yourself to Globus using your NOAA
userid described below.

.. _login-with-your-noaa-credentials:

Login with your NOAA credentials
--------------------------------

-  Navigate to: https://www.globus.org
-  Select **Login** in the upper right corner.
-  Look for the "Use your existing organizational login"
   section. In the field directly below (may have the string
   "Look-up your organization" at first) select
   ``NOAA RDHPCS``
-  Click the Continue button.
-  Complete you login with your camelcase (First.Last)
   Username and RSA pass code

**Legacy Globus ID** WARNING! Using your globusID, if you
have one, may work, but is strongly discouraged, as it will
not allow you to access certain cloud-based reources, such
as the AWS S3 Globus connectors, for example.

**After a successful login**

Following a successful login, you are now in the File
Manager. The left sidebar has buttons for several
activities, of which the two of most interest are:

-  `Collections <https://app.globus.org/collections>`__
-  `File Manager <https://app.globus.org/file-manager>`__

.. _find-select-and-browse-globus-endpoints:

Find, Select, and Browse Globus Endpoints
-----------------------------------------

| Select COLLECTIONS from the left sidebar. This will bring
  your browser to a page with a banner that looks like this:

.. image:: /images/globus_collections.png

| When you search for a Collection, you may enter the first
  few (or many) characters of the collection's name.

| For example, searching for ``noaardhpcs#jet`` will turn up
  this result:

.. image:: /images/globus_collections_2.png

| You can browse the exposed directories by clicking on the
  link, or this symbol:

.. image:: /images/GT.png

.. _setup-globus-connect-personal-on-laptopworkstation:

Setup Globus Connect Personal on Laptop/Workstation
---------------------------------------------------

Permissions are needed to add software to your
laptop/workstation. If you are not allowed to install
software, please see your local IT laptop/workstation
support representative.

-  **IMPORTANT!** Before you start, please ensure that the
   firewall rules affecting your personal workstation are
   configured according to `these
   instructions <https://docs.globus.org/how-to/configure-firewall-gcp/>`__
-  Navigate to `Globus Connect
   Personal <https://www.globus.org/globus-connect-personal>`__.
-  Select the proper platform from the "Install Globus
   Connect Personal" box, and follow instructions.

| You may also reference the `how-to
  video <https://docs.globus.org/how-to/instructional-videos/>`__.
| CAVEATS

-  If you get a new computer, and are transferring all
   digital assets from an old host to this new one, it is
   best to delete the personal collection application from
   the older host first. When your new host becomes fully
   operational, simply install the Globus Connect Personal.
   It only takes a minute or two.
-  If your localhost is on a VPN, Globus connect personal
   operation may be hindered, because the dynamics of
   firewall rules may be different from what they are
   without the VPN. If you have difficulties, and using a
   computer where you have no administrative privileges,
   please share `this
   information <https://docs.globus.org/how-to/configure-firewall-gcp/>`__
   with your local IT helpdesk.


.. _initiate-and-manage-data-transfers:

==================================
Initiate and Manage Data Transfers
==================================

.. _via-the-globus-connect-web-interface:

Via the Globus Connect Web Interface
====================================

-  Login and navigate to FILE MANAGER, and pick two
   Collections.
-  Navigate to the desired directories in both panels.
-  Select the files you want transferred, and hit the Start
   button. In the example below, we pick two files from
   Orion (the right panel).

.. image:: /images/globus-SelectForXfer.png

After you click the Start button and no issues are
identified, a confirmation will pop up near the top-right
part of your screen:

.. image:: /images/globus-Requestok.png

You can check on the status of the transfer on the
ACTIVITY panel

.. image:: /images/globus-activity.png

More details about the transfer is on the page displayed
when you click on this symbol:

.. image:: /images/GT.png

.. _via-the-globus-command-line-interface:

Via the Globus Command Line Interface
=====================================

The CLI is available on Jet, Hera, and Niagara.

| If you would like to use Globus-cli either on your
  personal machine or on a system that doesn't have
  **globus-cli** installed you can easily install it on your
  own by following the instructions at this link:

https://docs.globus.org/cli/

Basic usage is documented here, but please see the following
link for more details about this feature at: `Globus
CLI <https://docs.globus.org/cli/>`__.

.. _getting-started-with-globus-cli:

Getting Started With Globus CLI
-------------------------------

On Hera, Jet, Niagara, load the "globus-cli" module:

::

   $ module load globus-cli

On MSU Systems, Orion, Hercules, load the "python/3.7.5"
module to enable the globus command:

::

   $ module load python/3.7.5

Login to Globus via the CLI (local web browser required for
login)

1) Run the command:

::

   $ globus login
   Please authenticate with Globus here:
   ------------------------------------
   https://auth.globus.org/v2/oauth2/authorize?client_id=...access_type=offline&prompt=login
   ------------------------------------

| 2) Open a browser, cut-n-paste the link, and authenticate
  with your NOAA RDHPCS credentials (RSA Passcode).
| 3) Agree to things requested in a Consent form.
| 4) Cut and paste the Native App Code into the terminal
  prompt to complete your login.
| 5)

::

   Enter the resulting Authorization Code here: HjrDuhAu2XhIzxggwhe54z9kd2zYuPsdfdsQ

   You have successfully logged in to the Globus CLI!

   You can check your primary identity with
     globus whoami

   For information on which of your identities are in session use
     globus session show

   Logout of the Globus CLI with
     globus logout

.. _search-for-globus-endpoints:

Search for Globus Endpoints
---------------------------

One endpoint on Orion, and another one serving Niagara is
identified by an ID (32 digit hex number). The ID is needed
to conduct further operations. Below are a few examples
returned by the endpoint search, your listing will be longer

::

   $ globus endpoint search msuhpc2

   ID                                   | Owner                           | Display Name
   ------------------------------------ | ------------------------------- | -------------------
   84bad22e-cb80-11ea-9a44-0255d23c44ef | msuhpc2@globusid.org            | msuhpc2#Orion-dtn
   ...

   $ globus endpoint search noaardhpcs#niagara
   ID                                   | Owner                   | Display Name
   ------------------------------------ | ----------------------- | ----------------------------
   b6e851c3-2c25-44d4-82a7-ac4005e81a37 | b6e851c3-2c25-44d4...   | noaardhpcs#endpoint_niagara
   8fd89064-b16e-11ea-9a3b-0255d23c44ef | 3758d26a-bf6...         | noaardhpcs#niagara_untrusted
   21467dd0-afd6-11ea-8f12-0a21f750d19b | noaardhpcs@globusid.org | noaardhpcs#niagara
   ...

For transfer purposes, do not pick an ID associated with a
display name that has ``#endpoint_``

.. _define-endpoint-ids-in-shell-variables:

Define Endpoint ID's in Shell Variables
---------------------------------------

For easy reference, define each Endpoint's ID in shell
variables

sh/bash example:

::

   $ export ORION=84bad22e-cb80-11ea-9a44-0255d23c44ef
   $ export NIAGARA=21467dd0-afd6-11ea-8f12-0a21f750d19b

csh/tcsh example:

::

   $ setenv ORION 84bad22e-cb80-11ea-9a44-0255d23c44ef
   $ setenv NIAGARA 21467dd0-afd6-11ea-8f12-0a21f750d19b

.. _check-your-access:

Check Your Access
-----------------

1) Check to see if you can list a directory. If you can not,
globus will provide instructions on what to do:

::

   $ globus ls $NIAGARA
   MissingLoginError: Missing login for b6e851c3-2c25-44d4-82a7-ac4005e81a37, please run

     globus session update

2) In this case, run the **globus session update** command
with your "Globus Identity" as directed above: (Note: You
can use the command **globus whoami** to get your globus
identity)

::

   $ globus session update first.last@rdhpcs.noaa.gov --no-local-server

   Please authenticate with Globus here:
   ------------------------------------
   https://auth.globus.org/v2/oauth2/authorize?client_id=d8c55291-867b-4e0d-8f4b-c235ef16deeb&redirect_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview_identity_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall+urn%3Aglobus%3Aauth%3Ascope%3Agroups.api.globus.org%3Aall+urn%3Aglobus%3Aauth%3Ascope%3Asearch.api.globus.org%3Aall+urn%3Aglobus%3Aauth%3Ascope%3Ab6e851c3-2c25-44d4-82a7-ac4005e81a37%3Amanage_collections&state=_default&response_type=code&access_type=offline&prompt=login
   ------------------------------------

   Enter the resulting Authorization Code here:

Copy the big auth.globus.org URL into your browser, and
complete the process. Enter the authorization code at the
prompt.

::

   You have successfully logged in to the Globus CLI!
   ...

            .. rubric:: Determine Source and Destination Directories on
               each
               Endpoint[\ `edit </index.php?title=Globus_Online_Data_Transfer&action=edit&section=28>`__\ ]
               :name: determine-source-and-destination-directories-on-each-endpointedit

            ::

               $ globus ls $ORION\:/work/noaa/<project>/John.Smith/
               $ globus ls $NIAGARA\:/collab1/data/<John.Smith>/

.. _initiate-globus-transfer:

Initiate Globus Transfer
------------------------

Copy a file called ``testfile`` from Orion to Niagara.

**Note:** Unlike scp, the following command needs a file
name if a single file is being transferred.

::

   $ globus transfer $ORION\:/work/noaa/<project name>/jsmith/testfile $NIAGARA\:/collab1/data/John.Smith/testfile
   Message: The transfer has been accepted and a task has been created and queued for execution
   Task ID: af8c7e14-a67b-11ea-bee4-0e716405a293

.. _check-globus-transfer:

Check Globus Transfer
---------------------

::

   $ globus task list
   Task ID                              | Status    | Type     | Source .. | Dest .. | Label
   ------------------------------------ | --------- | -------- | ------------------- | ------
   af8c7e14-a67b-11ea-bee4-0e716405a293 | SUCCEEDED | TRANSFER | ...       | ...     | NULL

.. _add-globus-support-to-google-contacts:

Add Globus Support to Google Contacts
-------------------------------------

Sometimes, Globus sends you email notifications. In order to
avoid NOAA Email quarantine (where MOC filters emails
indicated by AI to be spam), the email address
``support@globus.org`` must be entered into a user’s NOAA
Google Contacts to whitelist the address.

#. Log into the user’s NOAA Google email account, using a
   web browser **(use of local system email and contacts
   applications will not suffice!)**
#. Select the Google Contacts application from the 3x3 grid
   applications icon at top right of the email web page
#. Click the “Create contact” button at the top left of the
   Contacts web page
#. Enter “Globus” in the Company field, without the quotes
#. Enter ``support@globus.org`` in the email field
#. Click “Save"

.. image:: /images/globus-google-contact.png

.. _frequently-used-collectionendpoint-uuids:

=========================================
Frequently Used Collection/Endpoint UUIDs
=========================================

(last updated 2023, November 13)

On RDHPCS systems the use of the globus-cli requires loading
of the **globus-cli** module:

::

    module load globus-cli

On MSU HPC systems the use of globus-cli requires loading of
the **python** module:

::

    module load python/3.7.5
    which globus

On RDHPCS systems loading the **globus-cli** module defines
the environment variables to contain the UUID of some of the
endpoints of interest to the RDHPCS users.

This information is provided as-is, and is subject to
change. It is best to use methods described in the training
materials above to verify the actual UUID.

.. csv-table:: Common Endpoint UUID's
    :file: /files/globus_endpoints.csv
    :header-rows: 1


.. _additional-information-on-using-globus-connect:

===============
Additional Info
===============

This documentation has been simplified because Globus
provides high quality online documentation and instructional
videos. You will find the following
`link <https://docs.globus.org/how-to/>`__ very helpful for
training and reference, to be used in conjunction with this
documentation.

