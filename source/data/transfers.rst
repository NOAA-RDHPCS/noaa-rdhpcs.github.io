.. meta::
   :description: Guide to data transfer methods on RDHPCS systems, including
    Globus, Data Transfer Nodes, Untrusted DTNs, and SSH port tunneling.
   :keywords: data transfers, Globus, DTN, UDTN, port tunneling, rsync, scp,
    trusted hosts, firewall

.. _Data_Transfers:

##############
Data Transfers
##############

RDHPCS provides several ways to move data to and from its systems. Globus is
the preferred method wherever it is available. This page lists the hostnames
and collection names you need, helps you pick a method, and then walks through
each one.

.. _quick_reference:

===============
Quick Reference
===============

If you already know which method you want, take the hostname or collection
name you need from the tables below.

.. _dtn_hostnames:

Trusted Data Transfer Node Hostnames
====================================

Use these hostnames with :manpage:`scp(1)`, :manpage:`sftp(1)`, and
:manpage:`rsync(1)`. Trusted Data Transfer Nodes (DTNs) accept connections
only from pre-authorized hosts. See :ref:`firewall-modifications` if your
host is not authorized.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - System
     - Fully qualified host name
     - Site
   * - Mercury
     - dtn-mercury.fairmont.rdhpcs.noaa.gov
     - NESCC
   * - Ursa
     - dtn-ursa.fairmont.rdhpcs.noaa.gov
     - NESCC
   * - Orion
     - orion-dtn.hpc.msstate.edu
     - MSU
   * - Hercules
     - hercules-dtn.hpc.msstate.edu
     - MSU

.. TODO: Confirm whether Gaea and PPAN have scp-reachable trusted DTN
   hostnames. The previous version of this page listed "N/A" for both in the
   untrusted DTN table, and named no trusted DTN for either system.

.. TODO: Confirm whether Hera still has a DTN. The previous version of this
   page named dtn-hera.fairmont.rdhpcs.noaa.gov in the firewall request
   section only, and Hera still appears in the bastion hostname table in
   source/connecting/index.rst.

.. note::

    Your user name is case sensitive. Use the ``First.Last`` form, not
    ``first.last``.

.. _udtn_hostnames:

Untrusted Data Transfer Node Hostnames
======================================

Untrusted Data Transfer Nodes (uDTNs) accept connections from anywhere on the
internet, including your own laptop. They expose only a staging directory, not
your project space, so transfers through a uDTN take two steps. See
:ref:`udtn_two_step`.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - System
     - Globus collection
     - Host name for scp, sftp, rsync
     - Directory on the system
     - Same directory seen on the uDTN
   * - Mercury
     - noaardhpcs#mercury_untrusted
     - udtn-mercury.fairmont.rdhpcs.noaa.gov
     - :file:`/collab2/data_untrusted/$USER`
     - :file:`/collab2/$USER`
   * - Ursa
     - noaardhpcs#ursa_untrusted
     - udtn-ursa.fairmont.rdhpcs.noaa.gov
     - :file:`/scratch[34]/data_untrusted/$USER`
     - :file:`/scratch[34]/$USER`
   * - PPAN
     - noaardhpcs#ppan_untrusted
     - Not available -- use Globus
     - :file:`/collab1/data_untrusted/$USER`
     -
   * - Gaea C5/F5
     - noaardhpcs#gaea
     - Not available -- use Globus
     - :file:`/gpfs/f5`, :file:`/ncrc/home[12]/$USER`
     -
   * - Gaea C6/F6
     - noaardhpcs#gaea_f6
     - Not available -- use Globus
     - :file:`/gpfs/f6`, :file:`/ncrc/home[12]/$USER`
     -
   * - Orion
     - msuhpc2#orion-dtn
     - orion-dtn.hpc.msstate.edu
     - :file:`/work`, :file:`/work2`
     -
   * - Hercules
     - msuhpc2#hercules
     - hercules-dtn.hpc.msstate.edu
     - :file:`/work`, :file:`/work2`
     -

.. hint::

    On Mercury and Ursa the directory path on the system differs from the path
    you see on the uDTN. The final column shows the uDTN path where it differs.

.. important::

    Files in your uDTN staging directory that have not been accessed in the
    last 5 days are purged automatically. Move your data to project space as
    soon as the transfer finishes.

.. _globus_collection_summary:

Globus Collections
==================

Globus Connect Service is available on the following RDHPCS and partner
clusters. Use these collection names in the `Globus App`_ or with the
:ref:`Globus CLI <globus_cli>`.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Cluster
     - Collection name
     - File systems
     - Site
     - Host access
   * - Ursa
     - | noaardhpcs#ursa
       | noaardhpcs#ursa_untrusted
     - | /scratch3, /scratch4
       | /scratch3/data_untrusted, /scratch4/data_untrusted
     - NESCC
     - | Trusted hosts
       | Anywhere
   * - Mercury
     - | noaardhpcs#mercury
       | noaardhpcs#mercury_untrusted
     - | /collab2/data
       | /collab2/data_untrusted
     - NESCC
     - | Trusted hosts
       | Anywhere
   * - PPAN
     - | noaardhpcs#ppan
       | noaardhpcs#ppan_untrusted
     - | /archive, /home, /nbhome, /work, /xtmp
       | /collab1/data_untrusted
     - GFDL
     - | Trusted hosts
       | Anywhere
   * - Gaea
     - | noaardhpcs#gaea
       | noaardhpcs#gaea_f6
     - | /gpfs/f5, $HOME
       | /gpfs/f6, $HOME
     - NCRC
     - Anywhere
   * - Orion
     - msuhpc2#orion-dtn
     - /work, /work2
     - MSU
     - Anywhere
   * - Hercules
     - msuhpc2#hercules
     - /work, /work2
     - MSU
     - Anywhere
   * - GFDL Data Portal
     - noaagfdl#data_portal
     - /data
     - GFDL
     - Anywhere

.. TODO: The two collection tables that previously appeared on this page
   disagreed on three values. Confirm each of the following:
   (1) Mercury -- /collab2/data or /collab1/data?
   (2) PPAN -- noaardhpcs#ppan or noaardhpcs#ppan_rdtn?
   (3) GFDL Data Portal -- noaagfdl#data_portal or "noaagfdl#data portal"?

.. _cloud_collections:

Cloud Object Store Collections
==============================

RDHPCS maintains cloud stores in Amazon S3, Microsoft Azure, and Google Cloud.
From the Globus perspective, these work exactly like any other collection.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Collection
     - Description
   * - noaardhpcs#cloud_aws_rdhpcs_projects
     - AWS cloud RDHPCS collection
   * - noaardhpcs#cloud_azure_rdhpcs_projects
     - Azure cloud RDHPCS collection
   * - noaardhpcs#cloud_gcp_rdhpcs_projects
     - Google Cloud RDHPCS collection
   * - noaardhpcs#cloud_aws_s3_public
     - Public AWS S3 connector
   * - noaardhpcs#cloud_aws_s3_authenticated
     - Non-public managed AWS S3 connector
   * - noaardhpcs#cloud_aws_s3_authenticated2
     - Non-public managed AWS S3 connector

.. TODO: Confirm the name of the first authenticated S3 connector. The
   previous version of this page called it both
   noaardhpcs#cloud_aws_s3_authenticated and
   noaardhpcs#cloud_aws_s3_authenticated1.

.. _data-transfer-overview:

========================
Choose a Transfer Method
========================

Each method has advantages and limitations. Pick the one that best suits your
needs.

.. list-table::
   :header-rows: 1
   :align: left

   * - Method
     - Use it when
     - Limitations
   * - :ref:`Globus <globus>`
     - Almost always. It is the fastest and most reliable option, and the only
       one that restarts itself after a failure.
     - Some sites outside the RDHPCS program do not support Globus.
   * - :ref:`Trusted DTNs <transferring-data-trusted-dtn>`
     - You are transferring between RDHPCS systems, or from another trusted
       host, and you want to use scp, sftp, or rsync.
     - Only reachable from pre-authorized hosts. Usually cannot reach your
       :file:`/home` directory.
   * - :ref:`Untrusted DTNs <udtn_transfers>`
     - The other end is outside the RDHPCS program -- a university, a cloud
       provider, or your own laptop.
     - Exposes a staging directory only, so transfers take two steps. Purged
       after 5 days. No unattended transfers.
   * - :ref:`SSH port tunnel <established-tunnel>`
     - None of the above work for your case, and you are moving a modest
       number of files.
     - Slower. Requires a bastion session to stay open.

.. _trusted_and_untrusted:

Trusted and Untrusted Hosts
===========================

For security reasons, access to most external hosts and sites is blocked,
including your laptop or desktop. Access is opened on an as-needed basis.
Sites that have been allowed access are called *trusted hosts*. Every other
site is an *untrusted host*.

This distinction drives everything else on this page:

* Trusted DTNs and trusted Globus collections talk only to other trusted
  hosts, and they can see your project file systems.
* Untrusted DTNs and untrusted Globus collections talk to anywhere, but they
  can see only a staging directory.

If you need access to or from a host that is currently untrusted, see
:ref:`requests_for_firewall_exceptions`.

.. note::

    Before you can use a DTN or uDTN on any system, you **must log in to that
    system at least once.** Your directories are created on first login, and
    the DTNs cannot create them for you.

.. note::

    Unattended data transfers are allowed on the trusted DTNs only. See
    :ref:`unattended_transfers`.

.. _globus:
.. _globus_online_data_transfer:

=========================
Transfer Data with Globus
=========================

Globus is the preferred and most efficient way to transfer data between
Globus collections and external storage systems. To use it you need a NOAA
login name and a working MFA token. You can drive Globus from a web browser
or from the command line.

An **endpoint** is a file transfer location -- a computer or server --
accessible to Globus. A **collection** is a server together with an access
method for its files. Globus lets you browse collections, pick a source and a
destination, and start a transfer. The transfer itself runs in the background:
you can close your browser, and Globus emails you when it finishes.

Untrusted collections transfer data to and from anywhere. Trusted collections
transfer data only to and from other vetted collections. When you log in to
Globus and click **Collections**, you can see which collections are shared
with you and which you share with others.

.. seealso::

    * `Globus documentation <https://docs.globus.org/guides/>`_
    * `How to log in and transfer files with Globus
      <https://docs.globus.org/guides/tutorials/manage-files/transfer-files/>`_
    * `Globus transfer and sharing FAQ
      <https://docs.globus.org/faq/transfer-sharing/>`_

.. _globus_example:

Make Your First Transfer in the Web App
=======================================

Before you start, have these on hand:

* Your NOAA user name (``First.Last``) and your RDHPCS MFA token.
* The names of the source and destination collections, for example
  *noaardhpcs#ppan_untrusted* or *noaardhpcs#ursa*. See
  :ref:`globus_collection_summary`.
* The file system paths exposed by those collections, for example
  :file:`/collab1/data_untrusted` or :file:`/scratch4`.

Then:

#. Navigate to the `Globus App`_.
#. Select **existing organizational login**, then **NOAA RDHPCS**. The File
   Manager page displays.
#. In the File Manager *Collection* field, search for your first collection,
   for example *noaardhpcs#ppan_untrusted*. Authenticate if prompted.
#. In the *Path* field, enter the path you want, for example
   :file:`/collab1/data_untrusted/First.Last`.
#. Repeat steps 3 and 4 in the second panel for the other collection.
#. Select the files or directories to transfer.
#. Click **Start**.

Globus manages the transfer in the background and emails you when it
completes.

.. _globus_personal:

Set Up Your Own Computer with Globus Connect Personal
=====================================================

Your laptop or workstation is not a Globus collection on its own. Globus
Connect Personal is a small application that turns it into one, called a
*personal collection*. Once it is running, your computer appears in the
Globus File Manager just like any RDHPCS collection, and you transfer files
between the two panels exactly as you would between two RDHPCS systems.

This is the recommended way to move data between your own computer and
RDHPCS.

.. important::

    NOAA RDHPCS treats your laptop or workstation as an **untrusted**
    endpoint. Pair your personal collection with a **uDTN** collection from
    :ref:`udtn_hostnames`, not with a trusted collection. Because your project
    space is not visible from a uDTN, the transfer takes two steps. See
    :ref:`udtn_two_step`.

Why use Globus Connect Personal instead of ``scp``:

* Transfer rates are much faster than ``scp`` or ``sftp``.
* Transfers suspend and resume automatically as your computer sleeps, wakes,
  or reboots. A large transfer survives closing your laptop lid.
* Globus retries failed files on its own and emails you when the transfer
  finishes.
* Globus verifies each file after transfer, so you know the copy is intact.
* You do not need an SSH port tunnel, and you do not need to keep a terminal
  window open.

Install Globus Connect Personal
-------------------------------

Install the version for your operating system, then start it and log in with
the same NOAA RDHPCS identity you use for the `Globus App`_. During setup you
give your collection a name, which is how it appears in the File Manager.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Operating system
     - Installation instructions
   * - Linux
     - `Install on Linux
       <https://docs.globus.org/globus-connect-personal/install/linux/>`_
   * - macOS
     - `Install on macOS
       <https://docs.globus.org/globus-connect-personal/install/mac/>`_
   * - Windows
     - `Install on Windows
       <https://docs.globus.org/globus-connect-personal/install/windows/>`_

Choose Which Directories to Expose
----------------------------------

By default, Globus Connect Personal shares your home directory in read and
write mode, and nothing else. You can change which paths are accessible, and
whether each one is readable or writable.

Restricting paths is worth doing. It limits what a mistaken transfer can
overwrite on your own machine, and it keeps the File Manager listing short.
See `Configuration and file permissions
<https://docs.globus.org/globus-connect-personal/>`_ for the settings on each
operating system.

.. note::

    On Linux, Globus Connect Personal must be running for your collection to
    appear in the File Manager. If your collection shows as offline, start it
    with :command:`globusconnectpersonal -start`.

.. seealso::

    * `Globus Connect Personal overview
      <https://docs.globus.org/globus-connect-personal/>`_
    * `Installation instructions for all platforms
      <https://docs.globus.org/globus-connect-personal/install/>`_

.. _globus_cli:

Use the Globus Command Line
===========================

Use the command line when you want to script a transfer, or when you are
already logged in to an RDHPCS system and do not want to switch to a browser.
The web app and the CLI drive the same service, so a transfer you start from
one is visible in the other.

The Globus command line interface (CLI) is available on Ursa and Mercury. To
load it, run:

.. code-block:: shell

    $ module load globus-cli

The module also defines environment variables holding the UUIDs of Globus
collections commonly used by RDHPCS users. To see them, run:

.. code-block:: shell

    $ module show globus-cli

Log In
------

Before your first transfer, authenticate. This opens a URL that you paste
into a browser, then paste the resulting code back into the terminal:

.. code-block:: shell

    $ globus login
    $ globus whoami

Your login persists, so you do not need to repeat this for every transfer.

Find a Collection
-----------------

Commands take a collection UUID, not a display name. Look one up with
``globus endpoint search``:

.. code-block:: shell

    $ globus endpoint search noaardhpcs#ursa_untrusted

List a Directory
----------------

.. code-block:: shell

    $ globus ls -l <collection-uuid>:/scratch4/data_untrusted/First.Last/

.. TODO: The previous version of this page contained a table of collection
   UUIDs and their environment variable names (UUID_HERA_DTN, UUID_JET_DTN,
   UUID_NIAGARA_DTN, and so on) in source/files/globus_endpoints.csv. Every
   entry named a decommissioned system. Confirm the current UUIDs and
   variable names, then add them here.

Transfer Files
--------------

``globus transfer`` takes a source and a destination, each written as
``<collection-uuid>:<path>``. This example transfers a single file from a
personal collection to the PPAN untrusted collection. Replace ``First.Last``
with your own user name, and replace each UUID with one you looked up:

.. code-block:: console

    [First.Last@an001 ~]$ globus transfer my-personal-external-endpoint-id:myDataFileName_here.txt \
    6ba73d87-08f2-463e-bf8f-83cc3e7a871f:First.Last/myDataFileName_there.txt

To transfer a whole directory, add ``--recursive``. To check on a transfer
after you submit it:

.. code-block:: shell

    $ globus task list
    $ globus task wait <task-id>

To move many separate paths in one task, use ``--batch``, which reads
source and destination pairs from standard input. See the `globus transfer
reference <https://docs.globus.org/cli/reference/transfer/>`_.

Install the CLI Elsewhere
-------------------------

If you want the Globus CLI on your personal machine, or on a system where it
is not installed, you can install it yourself. Globus recommends ``pipx``, so
that the CLI keeps working across changes to your system Python.

.. seealso::

    * `Globus CLI documentation <https://docs.globus.org/cli/>`_
    * `CLI quickstart <https://docs.globus.org/cli/quickstart/>`_
    * `Using the CLI <https://docs.globus.org/cli/using-the-cli/>`_
    * `CLI examples <https://docs.globus.org/cli/examples/>`_

.. _globus_scheduled:

Schedule and Repeat Transfers
=============================

You do not have to start every transfer by hand. Globus Timers runs a
transfer on a schedule, and repeats it at an interval you choose. This is
useful when you are pulling a data set that is updated daily, or when you
want a long transfer to start overnight.

To schedule a transfer in the web app, set up the transfer as usual in the
File Manager, then open the **Transfer & Timer Options** menu before you
click **Start**. Set a **Schedule Start** date and time, and a **Repeat**
interval if you want the transfer to run more than once.

Because a repeated transfer skips files that are already present and
unchanged at the destination, a timer is also a practical way to keep two
directories in sync.

.. note::

    Timers do not remove the uDTN two-step problem on their own. A scheduled
    transfer can move data into your :file:`data_untrusted` staging directory,
    but you still need to move it to project space before the 5-day purge. See
    :ref:`udtn_two_step`.

.. seealso::

    * `How to schedule a transfer
      <https://docs.globus.org/api/timers/getting-started/schedule-a-transfer/>`_
    * `Automate transfers with a service account
      <https://docs.globus.org/guides/recipes/automate-with-service-account/>`_

.. _globus_sharing:

Share Data with Collaborators
=============================

RDHPCS users can share data with external collaborators who do not have
accounts on the RDHPCS systems. You can share files both inbound and
outbound using the untrusted DTNs.

**For data that is short-lived**, and not broadly shared with external users,
use RDHPCS endpoints.

**For data that is expected to be available for three months or more**, use
the :ref:`institutional_data_portal` endpoint.

.. note::

  * Data sharing is available on *untrusted* Globus collections (uDTNs) only.
  * You **must** share the collection with your collaborators. **There is
    currently no public sharing available.** You can share to an email
    address or to a GlobusID.
  * You can share only directories under your
    :file:`/*/data_untrusted/$USER` directory.
  * Before you share anything, you must log in to the system at least once,
    so that your home and project directories are created.
  * You may need to create your :file:`/*/data_untrusted/$USER` directory
    with ``mkdir``, depending on the system.

Refer to :ref:`globus_collection_summary` for collection names and the
directories they expose.

The Globus web site provides complete instructions for sharing your data. See
the `file sharing instructions <https://docs.globus.org/how-to/share-files/>`_.

.. _institutional_data_portal:

GFDL Institutional Data Portal
------------------------------

**For data that is expected to be permanent**, use the GFDL institutional data
portal endpoint, ``noaagfdl#data_portal``. This is for outbound sharing only.

Data hosted on the GFDL data portal servers is accessible through Globus, and
available on request through the `data hosting request form
<https://docs.google.com/forms/d/e/1FAIpQLScH-2mMLHesN6DJlxLEVU6Kg8wXEKvEr-JgB_5nXchjCDrYww/viewform>`__
for papers, collaborations, and other projects. The requester is notified of
the Globus URL when the request is completed. GFDL data transfer features can
be reviewed in `this table.
<https://docs.google.com/spreadsheets/d/1fVC60ztNzYxFui1zyF_S_AMfoc3O15oa1-oOKhGrqQI/edit?gid=0#gid=0>`_

For assistance, contact the GFDL team at oar.gfdl.dpteam@noaa.gov.

.. note::

  Information shared through the GFDL portal is shared permanently. Refer to
  the `GFDL FAIR use and GFDL Data DOI policy
  <https://www.gfdl.noaa.gov/fair-use-policy/>`_ for external data sharing.

.. _cloud_endpoints:

Transfer To and From Cloud Object Stores
========================================

The RDHPCS Globus plan offers connectors so you can reach data held in AWS S3
buckets. To use this service, log in to Globus with your NOAA RDHPCS
credentials. See :ref:`cloud_collections` for the collection names.

.. note::

  Load the ``globus-cli`` module before you use any Globus command line
  commands.

Publicly Accessible Buckets
---------------------------

No keys are required. As an example, consider getting files from the NOAA
RRFS experiment on the `AWS Cloud
<https://noaa-rrfs-pds.s3.amazonaws.com/index.html#rrfs_a/rrfs_a.20230725/00/control/>`_.

#. Go to `<https://registry.opendata.aws/>`_.
#. In the **Search datasets** field, enter the data set of interest, in this
   case ``noaa-rrfs``, which is the first part of the URL of interest.
#. Click the result in the right pane. This leads to
   `<https://registry.opendata.aws/noaa-rrfs/>`_.
#. From that page, copy the last part of the ARN. In this example, the ARN is
   ``arn:aws:s3:::noaa-rrfs-pds``, so the part you need is ``noaa-rrfs-pds``.
#. Log in to the `Globus App`_ with your NOAA identity.
#. In the File Manager *Collection* field, enter
   ``noaardhpcs#cloud_aws_s3_public``.
#. In the *Path* field, enter
   :file:`/noaa-rrfs-pds/rrfs_a/rrfs_a.20230725/00/control/`.

Once you can see the file listing, use the File Manager to move files between
the collections you want.

Non-Public Buckets That Require Keys
------------------------------------

Some sites are curated by their owners and are not public. To reach one, the
owner must give you two things:

- An AWS IAM access key ID
- An AWS IAM secret key

Then:

#. In the File Manager, search for and select
   ``noaardhpcs#cloud_aws_s3_authenticated`` or
   ``noaardhpcs#cloud_aws_s3_authenticated2``.
#. Click the three vertical dots to the right of the *Collection* field.
#. Select the *Credentials* tab.
#. If the STATUS column shows *invalid*, click the wrench icon.
#. Enter the **Access Key ID** and **Secret key**, then click **Continue**.

You now have access to the contents of the S3 bucket.

.. note::

  There are collections provided to let you transfer from one cloud bucket to
  another, if you need that.

.. warning::

  An access key and secret key pair is specific to one collection, so you can
  be connected to at most one bucket at a time.

To change buckets, first delete your working AWS access credentials, so you
can create a different pair linked to the new bucket. Select the *Credentials*
tab, where the STATUS shows *active*, then click the trash can icon.

.. _globus_limits:

Globus Limits and Behavior
==========================

.. warning::

    Note the following when you use Globus transfers.

    * Globus transfers do not preserve file permissions. Arriving files have
      ``rw-r--r--`` permissions. They have no execute permission, so you must
      use ``chmod`` to reset execute permission before you run a
      Globus-transferred executable.
    * Globus overwrites files at the destination with identically named
      source files. It does this without warning.
    * Globus allows 8 active transfers across all users, and each user is
      limited to 3 active transfers. Prefer fewer, larger transfers over many
      small ones.
    * If a folder holds thousands of small files, each less than 1 MB, tar
      them first. Globus handles larger files well on its own.

.. _transferring-data:

=======================================
Transfer Data with scp, sftp, and rsync
=======================================

Globus is the preferred method. Use the commands in this section when the
other end of your transfer does not support Globus, or when you are moving a
small number of files.

Many users are accustomed to using scp and sftp through the login nodes.
The DTNs are much faster, so we recommend them over login nodes wherever they
are available.

Only the high-performance file systems -- the scratch file systems -- are
available through the DTNs, not your :file:`/home` file system. When you are
asked for a password, authenticate using YubiKey MFA.

.. note::
    If you use WinSCP on Windows, choose SFTP as the protocol rather than SCP.

.. _transferring-data-trusted-dtn:

From a Trusted Host to a DTN
============================

By default, trusted DTNs are accessible only from some hosts within noaa.gov
(and Orion). If you need access to or from a host that is not accessible, we
must modify the system firewalls. See :ref:`firewall-modifications`.

DTNs support ssh-based transfer methods: :manpage:`scp(1)`,
:manpage:`rsync(1)`, and :manpage:`sftp(1)`. Authentication uses your NOAA
name and password with YubiKey multi-factor authentication.

Take the host name from :ref:`dtn_hostnames`, then:

.. code-block::

    scp /path/to/local/file First.Last@dtn-<name>.<site>.rdhpcs.noaa.gov:/path/on/HPC/System
    First.Last@dtn-<name>.<site>.rdhpcs.noaa.gov's password:

At the password prompt, enter your YubiKey token response.

.. Note::
    Your user name is case sensitive in the ``scp`` command. Use the form
    ``First.Last``, not ``first.last``.

.. _udtn_transfers:

From Anywhere to an Untrusted DTN
=================================

Untrusted DTNs are open systems reachable from anywhere, including your
personal machine. Take the host name from :ref:`udtn_hostnames`, then use the
same commands as above.

Note the following important points:

* Before you can use the uDTNs on any cluster, **you must log in to that
  cluster at least once** to create the necessary directories.
* File space on the uDTNs is very limited. Move your data to project space as
  soon as possible and clean up temporary files. If you do not, we must remove
  your data and disable your access to the directory.
* **All files under your allocated directories that have not been accessed in
  the last 5 days are purged automatically.**
* Unattended transfers are allowed on the trusted DTNs only, never on a uDTN.
* You can use Globus to transfer data to and from the uDTNs.

.. _udtn_two_step:

Two-Step Transfers Through a uDTN
---------------------------------

Your project directories are not directly accessible from the uDTNs, so
moving data to or from project space takes two steps.

To bring data **in** to your project space:

#. Transfer to the :file:`data_untrusted` tree using the uDTN.
#. Move or copy the data to your allocated project space.

To send data **out**, do the same steps in reverse order.

.. _established-tunnel:

Through an SSH Port Tunnel
==========================

With the SSH port tunnel method, an SSH tunnel is created between your point
of login -- typically your desktop -- and the remote host. The port tunnel
method works from any system on the network, so your local machine does not
have to be in the noaa.gov domain. Use this method when the DTNs are not
accessible.

.. _ssh-tunnel:

SSH Port Tunnel from Linux-like Systems
---------------------------------------

This method requires two sessions on your local machine: one to establish the
SSH port tunnel, and the other to perform the copy. To establish the port
tunnel, get the appropriate bastion hostname for the host you need from the
:ref:`bastion_hostnames` table.

Before You Begin
^^^^^^^^^^^^^^^^

Only the first session to a bastion can establish an ssh tunnel. You already
have an existing session when you see messages like:

  .. code-block:: shell

    -------------------
    bind [127.0.0.1]:57037: Address already in use
    channel_setup_fwd_listener_tcpip: cannot listen to port: 57037
    Could not request local forwarding.
    -------------------

To establish a new tunnel, do one of the following:

  * Close any existing sessions.
  * Open a new session using a bastion where you have no existing sessions.

In the steps below, replace ``First.Last`` with your own HPC username, and
``XXXXX`` with the unique local port number assigned to you when you log in to
your HPC system. Use the word ``localhost`` where indicated. It is not a
variable; do not substitute anything else. You run these commands on your
local machine, not within the HPC system terminal.

As long as the ssh window remains open, you can use the forwarded port for
data transfers. After the first session has been opened with port forwarding,
any further connections -- login via ssh, copy via scp -- work as expected.

**1. Find your local port number**

To find your unique local port number, log in to your HPC system. Make a note
of the number, then close all sessions. The number is different on each
system.

.. image:: /images/linux_xfer1.png
   :scale: 75%
   :alt: Terminal login banner showing the assigned local port number

.. note::
    Open two terminal windows for this process.

**Local Client Window #1**

Enter the appropriate command for your environment. Replace ``XXXXX`` with the
local port number from step 1.

For Windows PowerShell, enter:

.. code-block:: shell

     ssh -m hmac-sha2-512-etm@openssh.com -LXXXXX:localhost:XXXXX First.Last@ursa-mfa.fairmont.rdhpcs.noaa.gov

For Mac or Linux, enter:

.. code-block:: shell

     ssh -LXXXXX:localhost:XXXXX First.Last@ursa-mfa.fairmont.rdhpcs.noaa.gov

If you run X11 applications with x2go or normal terminals, add the ``-X``
parameter:

.. code-block:: shell

    ssh -X -LXXXXX:localhost:XXXXX First.Last@ursa-mfa.fairmont.rdhpcs.noaa.gov

.. image:: /images/linux_xfer2.png
   :scale: 75%
   :alt: Terminal showing an ssh command with local port forwarding options

Verify that the tunnel works by running this in another local window on your
local machine:

.. code-block:: shell

   ssh -p <port> First.Last@localhost

``<port>`` is the local port number you used above, ``First.Last`` is your
user ID on the RDHPCS systems, and ``localhost`` is typed as-is.

You are prompted for your password. Enter your MFA response and you should be
able to log in. Once you can log in, log out again -- that session was only
to test the tunnel.

**2. Use scp or rsync to complete the transfer**

**Local Client Window #2**

Keep the window from step 1 open. The tunnel exists only as long as that
session stays alive.

To transfer a file **to** an HPC system, for Windows PowerShell, enter:

.. code-block:: shell

  scp -P XXXXX /local/path/to/file First.Last@localhost:/path/to/file/on/HPCSystems

For Mac or Linux, enter:

.. code-block:: shell

  rsync <put rsync options here> -e 'ssh -l First.Last -p XXXXX' /local/path/to/files First.Last@localhost:/path/to/files/on/HPCSystems

To transfer a file **from** an HPC system, for Windows PowerShell, enter:

.. code-block:: shell

    scp -P XXXXX First.Last@localhost:/path/to/file/on/HPCSystems /local/path/to/file

For Mac or Linux, enter:

.. code-block:: shell

    rsync <put rsync options here> -e 'ssh -l First.Last -p XXXXX' First.Last@localhost:/path/to/files/on/HPCSystems /local/path/to/files

In either case you are asked for a password. Touch your YubiKey to
authenticate.

.. note::

   Your username is case sensitive in the ``scp`` command. Use the form
   ``First.Last``.

SSH Port Tunnel for PuTTY-CAC on Windows
----------------------------------------

PuTTY-CAC is an SSH client used to configure and initiate a connection. As
needed, install `PuTTY-CAC
<https://github.com/NoMoreFood/putty-cac/releases/>`_. If you cannot install
software on your machine, contact your local systems administrator.

**Configuration**

Enter host information to configure an SSH terminal session.

.. image:: /images/putty1.png
   :scale: 75%
   :alt: PuTTY-CAC session configuration window with the bastion host name

In the left pane under Connection, select **Data** and enter your NOAA user
name as it appears in your NOAA email address -- for example, ``Robin.Lee`` if
your NOAA email is Robin.Lee@noaa.gov. The user name is case sensitive. If you
do not save a user name, you must enter it each time you open a session.

.. image:: /images/putty2.png
   :scale: 75%
   :alt: PuTTY-CAC Data pane with the user name field filled in

Complete the configuration:

* Select **Session** from the top of the left pane.
* Select **Save**, between Load and Delete.

**Open a first system session**

Open the session to make sure it works, and to record the local port number
you need to complete the port tunneling setup.

* Select the configured session from the **Saved Sessions** list, select
  **Load**, then **Open**.
* Enter your MFA passcode.
* Find and record your local port number.
* Click **Exit**, or close the PuTTY-CAC window to end the session.

**Port tunnel setup**

* Open PuTTY-CAC.
* Select the session from the Saved Sessions list, then **Load**.
* In the left pane, under Connection > SSH, select **Tunnels**.
* Check **Local ports accept connections from other hosts**.
* In the **Source Port** field, enter your local port number.
* In the **Destination Port** field, enter ``localhost:<local port number>``,
  where the local port number matches the source port.
* Select the **Local** and **Auto** radio buttons.
* Click **Add**.

.. image:: /images/putty3.png
   :alt: PuTTY-CAC Tunnels pane configured with a local port forward

To save the configuration change, select **Session** in the left pane, then
**Save**. Select **Open** to log in and verify that the updated session works.

Create a new port tunnel for each SSH system you intend to use. Each one has a
unique local port number.

To add extra saved sessions for the same system -- for example, for another
bastion -- when you already have the local port number:

* Load your current saved session.
* Enter the new host name for the other bastion.
* Give the new session a new name.
* Select **Save**. The new session appears in the list of saved sessions.
* Select **Open** to log in and verify the new session works.

WinSCP
------

.. note::
  You must have a port tunnel established before you can use WinSCP. The
  port-forwarded session must remain active to maintain the WinSCP
  connection. Use the word ``localhost`` where indicated. It is not a
  variable; do not substitute anything else.

Once port forwarding is configured, open and configure WinSCP. Be sure to
select SFTP as the file protocol.

.. code-block:: shell

  Hostname: localhost
  Port: your-assigned-port-used-in-Step-1-above
  File protocol: SFTP

.. image:: /images/winSCP1.png
  :scale: 50%
  :alt: WinSCP login dialog configured for localhost with the SFTP protocol

When prompted for a password, enter your MFA passcode:

.. image:: /images/winSCP2.png
  :scale: 75%
  :alt: WinSCP password prompt

.. _unattended_transfers:

===========================
Set Up Unattended Transfers
===========================

For real-time experiments that require data to be transferred automatically,
we support unattended data transfers from @noaa.gov hosts and other trusted
hosts. The data can flow in either direction, but the connection must be
initiated from the remote host.

.. note::

    Unattended data transfers are allowed on the :ref:`trusted DTNs
    <transferring-data-trusted-dtn>` only.

.. tip::

    Before you set up SSH keys, consider whether Globus solves your problem
    instead. A scheduled or repeating timer covers most recurring transfers
    without any key management, and it works with untrusted collections. See
    :ref:`globus_scheduled`.

.. important::

    Unattended data transfers to Gaea can only be completed using the `Globus
    App`_, or another method that can authenticate using an X509 certificate,
    such as :command:`gsiscp` or :command:`globus-url-copy`.

This capability is intended mainly for projects that can demonstrate a need
for it. If you need it, answer the following questions and follow the steps
below:

* What command will you use to do the transfers?
* What is the name of the machine where you will run the transfer command?
  Below we call this the **Remote Host**.
* What is the name of the NOAA RDHPCS machine you are trying to access? We
  call this the **RDHPCS-HOST**.

1. Copy :file:`~/.ssh/id_rsa.pub` from the remote host and place it on the
   RDHPCS-HOST in the directory :file:`~/scp-pubkeys/`.

2. On the RDHPCS-HOST, rename the file so that it is clear where it came
   from. For example, if the **Remote Host** was "tide":

   .. code-block:: console

       $ mv ~/scp-pubkeys/id_rsa.pub ~/scp-pubkeys/id_rsa.pub-tide

3. Send a help request with the subject line **Request for unattended data
   transfer capability**. Include the following information:

    * Your username on the RDHPCS-HOST.
    * The full path of the file containing the key from the Remote Host.
    * The IP address of the Remote Host.

.. note::

    Do not put keys in your home :file:`.ssh` directory. Put them in the
    :file:`$HOME/scp-pubkeys` directory on the RDHPCS-HOST.

.. admonition:: WCOSS2 Users Only
   :class: important

   The public key directory on WCOSS2 is :file:`/u/sshKeys/$USER`. You do not
   have to provide the IP addresses when you fill out the information
   requested.

If you do not have an RSA key on the remote system -- that is, if you have no
:file:`id_rsa.pub` file in your :file:`$HOME/.ssh` directory -- you can
generate one on Linux with:

.. code-block:: shell

    # ssh-keygen -t rsa

.. warning::

    When you are prompted for a passphrase, press <Enter>. Otherwise you are
    prompted for the passphrase even when you are set up for unattended data
    transfers, which defeats the purpose.

If you have difficulties, contact the support staff for help.

.. _requests_for_firewall_exceptions:
.. _firewall_exception_terms:
.. _firewall-modifications:

============================
Request a Firewall Exception
============================

For security reasons, a firewall controls access to and from all external
sites. Most external sites are blocked and can connect only through an
exception to the firewall rules.

By default, only hosts in the noaa.gov domain can reach the DTNs. If you need
to transfer data using the DTNs from hosts outside noaa.gov, submit a request
to open the firewall.

.. note::

    If you need to access an external site on a routine basis for your work,
    submit a help desk ticket with the subject line **Firewall Exception
    request** and provide the information below.

.. important::

    Plan ahead. Review by the security team can take up to two weeks, not
    including troubleshooting implementation issues.

.. note::
    If you have a Globus collection, provide it. Globus is the preferred
    method for data transfers, and using it may avoid the need for an
    exception entirely. With Globus you can also run a third-party transfer,
    where both ends of the transfer are remote.

Terms Used in a Request
=======================

* **Data Transfer Method:** the utility you will use -- scp, sftp, rsync,
  globus, wget, or curl.
* **Local Machine:** where you will be logged in when you initiate the
  transfer.
* **Remote Machine:** the other machine involved in the transfer.

What to Include in Your Request
===============================

* **Summary/Justification for transfer:** Why do you need this, and for how
  long? State whether it is permanent or temporary, and give a timeframe if
  it is temporary.
* **Source Systems (DNS name)**
* **Source IPs**
* **Destination Systems (DNS name)**
* **Destination IPs:** use the ``host`` command to find IPs.
* **Destination Port name(s):** service name, such as dns, http, nfs, or
  bluearc-admin.
* **Destination Port number(s) or range**
* **Destination Port protocol (tcp/udp)**
* **Direction:** which way is the connection initiated? To NOAA RDHPCS
  systems (inbound), or out from NOAA RDHPCS systems (outbound)?
* **An example command:** a typical command showing how you will do the
  transfers.

Source addresses for the DTNs:

.. code-block:: shell

    dtn-ursa.fairmont.rdhpcs.noaa.gov = 140.208.202.[4-5]
    dtn-mercury.fairmont.rdhpcs.noaa.gov = 140.208.202.[76-77]

To find the IP address of a destination, use the ``host`` command:

.. code-block:: shell

    First.Last@ufe04$ host ruc.noaa.gov
    ruc.noaa.gov has address 140.172.12.92

Example: Inbound Through a DTN
------------------------------

* **Summary/Justification for transfer:** Requesting (permanent) wget access
  to pull data from ruc.noaa.gov via the Ursa DTNs to transfer weather data
  to NOAA R&D systems.
* **Source Systems (DNS name):** dtn-ursa.fairmont.rdhpcs.noaa.gov,
  dtn-mercury.fairmont.rdhpcs.noaa.gov
* **Source IPs:** 140.208.202.[4-5], 140.208.202.[76-77]
* **Destination Systems:** ruc.noaa.gov
* **Destination IPs:** 140.172.12.92
* **Destination Port name(s):** HTTP/HTTPS, SSH
* **Destination Port number(s) or range:** 80, 22, 443
* **Destination Port protocol (tcp/udp):** tcp
* **Direction:** Outbound
* **An example command:**
  ``wget -r -A "a-deck-ecmwf-wmo*" https://ruc.noaa.gov/hfip/fiorino/tc/ecmwf/2019/wmo/``

.. _internally_initiated:

Transfers Initiated From an RDHPCS System
=========================================

This applies to NESCC systems -- Ursa and Mercury.

HPC systems have no specific hosts for internally initiated transfers.
Transfers initiated from HPC systems use the front end nodes, or nodes in the
service partition.

The firewall rules block all outgoing traffic by default. We permit
internally initiated transfers by request, after review and approval by the
security team. If you need this capability, send a request to the help system
with the subject line ``<$SYSTEM> FEs to <$HOSTNAME>``, using the appropriate
system and hostname.

.. code-block:: shell

  Ursa:
  Source Systems:  ufe[1-16].fairmont.rdhpcs.noaa.gov
  Source IPs:  140.208.193.[131-146]
  Mercury:
  Source Systems:  mfe[01-04].fairmont.rdhpcs.noaa.gov
  Source IPs: 140.208.193.[101-104]

.. TODO: The previous version of this page also listed Hera front ends
   (hfe[1-12].fairmont.rdhpcs.noaa.gov, 140.208.193.[1-12]). Confirm whether
   Hera should still be listed here.

Include the same information listed in `What to Include in Your Request`_.

Example: Outbound From the Front Ends
-------------------------------------

* **Subject:** Ursa FEs to podaac-tools.jpl.nasa.gov
* **Justification:** Requesting (permanent) wget access to pull data from
  podaac-tools.jpl.nasa.gov via the Ursa front ends to transfer weather data
  to NOAA.
* **Source Systems:** ufe[1-16].fairmont.rdhpcs.noaa.gov,
  mfe[01-04].fairmont.rdhpcs.noaa.gov
* **Source IPs:** 140.208.193.[131-146], 140.208.193.[101-104]
* **Destination Systems:** podaac-tools.jpl.nasa.gov
* **Destination IPs:** 128.149.132.160
* **Destination Port name(s):** HTTP/HTTPS, SSH
* **Destination Port number(s) or range:** 80, 22, 443
* **Destination Port protocol (tcp/udp):** tcp
* **Direction:** Outbound
* **An example command:**
  ``wget -r -A.nc https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal``

.. _migrating_local:

=========================================
Move Large Data Between Local Filesystems
=========================================

.. note::

    Large scale data migration can be challenging and time consuming. Review
    the following guidelines and tools to minimize the time it takes to move
    your data, and to make sure the migration completes successfully.

General Guidelines
==================

#. **Size the dataset and prune unneeded data.**
   Use tools such as ``du`` and ``tree`` on the directories to understand the
   data volumes. Make sure there are no duplicate data sets, temporary
   working files, or other unneeded content. **The most efficient way to move
   data is to reduce the data to move.** Use ``tar`` or ``zip`` to collapse
   directories into a single file. As appropriate, archive directories to the
   site-specific HSMS and delete them from the scratch file systems.
#. **Start early and leave plenty of time for migration.**
   Everyone on the filesystems will be moving data. Even with data sizes in
   hand, it is hard to predict how long a transfer takes. **Plan far ahead
   and leave yourself plenty of time.** Transferring many small files is
   often worse than a few large files, because performance depends more on
   the time to access a file than the time to transfer it.
#. **Make sure the user performing the copy can read all the data.** If a
   directory has restricted files or sub-directories, you must split it into
   multiple transfers as multiple users, or change ownership on the source
   data first.
#. **Disable all batch and cron jobs that may modify the directories you are
   transferring.** Any create, modify, or delete change can cause errors for
   any data transfer tool. For a large directory it may be fine to perform an
   initial copy **interactively**, but quiesce access before you perform a
   final sync.
#. **Use a synchronization tool, not just** ``cp`` **or** ``mv``, **and do
   not rely on a one-time transfer completing perfectly.** You will most
   likely have to run the process more than once, and tools such as rsync
   skip already-copied files. Delete the source data only once you have
   confirmed the copy is complete.
#. **For small data volumes, use an interactive session** on an HPCS head
   node. If the volume to move is less than a terabyte, it is appropriate to
   use a head node for an ad-hoc transfer with a tool such as rsync.
#. **For larger data volumes, submit a batch job** to a ``dtn`` or similar
   queue.

Suggested Tools
===============

du
--

An original part of Unix, the :manpage:`du(1)` disk usage tool is on every
HPCS. It gives a simple overview of the usage of a file or directory. Sort
the output by piping it through ``sort``:

.. code-block:: shell

   du -sk DIRECTORY/* | sort -n

- ``-s`` summarizes sub-directory usage.
- ``-k`` outputs in 1024-byte (1 kiB) blocks.
- ``| sort -n`` pipes the output through sort, sorted numerically.

tree
----

A highly useful but optional part of Linux systems that *should* be installed
on all NOAA RDHPCS, the ``tree`` tool gives tree-structured output about a
directory, with the option to summarize and calculate usage:

.. code-block:: shell

        tree --du -h -d -L 2 --sort=size DIRECTORY

- ``--du`` calculates disk usage on directories.
- ``-h`` displays human-readable (K, M, G, T) volumes.
- ``-d`` summarizes directories.
- ``-L 2`` shows only two levels of directories.
- ``--sort=size`` sorts output by size.

.. code-block:: shell

    % tree --du -h -d --sort=size -L 2 .
    [8.8K]  .
    ├── [6.3K]  source
    │   ├── [2.6K]  images
    │   ├── [ 416]  data
    │   ├── [ 416]  systems
    │   ├── [ 288]  software
    │   ├── [ 224]  slurm
    │   ├── [ 192]  _templates
    │   ├── [ 192]  accounts
    │   ├── [ 160]  _downloads
    │   ├── [ 160]  files
    │   ├── [ 128]  _search
    │   ├── [ 128]  _static
    │   ├── [ 128]  contributing
    │   ├── [ 128]  help
    │   ├── [ 128]  logging_in
    │   ├── [  96]  FAQ
    │   ├── [  96]  compilers
    │   ├── [  96]  connecting
    │   └── [  96]  queue_policy
    ├── [1.7K]  build
    │   ├── [ 992]  html
    │   └── [ 608]  doctrees
    └── [  96]  utils

      15K used in 24 directories

.. attention::

   Do *not* use the ``du`` or ``tree`` command on the lustre filesystems
   listed below:

+-------------+-------------+
| Cluster     | File System |
+=============+=============+
|| Ursa       || /scratch3  |
||            || /scratch4  |
+-------------+-------------+

rsync
-----

For basic migration, use the :manpage:`rsync(1)` tool to transfer files and
directories:

.. code-block:: shell

    rsync --archive --verbose --one-file-system /full/path/to/source/directory/ /full/path/to/destination/directory

.. warning::

    You must have a trailing slash after the source directory:
    ``/full/path/to/source/directory/`` **/**. Without it, a second
    invocation of the same command retransfers all of the data into a
    subdirectory, for example
    ``/full/path/to/source/directory/directory``.

- ``--archive`` (``-a``) preserves all ownership and dates in the transfer.
- ``--verbose`` (``-v``) displays details of every file transferred. If you
  have lots of small files, this slows down the transfer.
- ``--one-file-system`` (``-x``) restricts the transfer to the source
  filesystem. This matters when symlinks point to data on other filesystems.

To keep the two directories exactly the same, use ``--delete``:

- ``--delete`` removes files from the destination that are not in the source
  directory. It may be preferable to clean up the source only after
  confirming that all files transferred.

.. warning::

    Do not use the ``--delete`` option if you do not want data in the
    destination directory to be removed.

A Sample Batch Script
=====================

Here is a sample batch script you can use as a template, then submit to the
batch system to perform the data movement:

.. code-block:: shell

    #!/bin/bash

    #SBATCH --job-name=data-transfer
    #SBATCH --partition=PARTITION_GOES_HERE
    #SBATCH --time=08:00:00
    #SBATCH --nodes=1
    #SBATCH --output=$HOME/data-transfer-job-%j

    set -x

    SRC=/path/to/source/directory/                 # Note trailing slash
    DEST=/path/to/destination/directory

    echo "$(date) : Starting sync from $SRC to $DEST"

    rsync -ax $SRC $DEST

    echo "$(date) : Ending sync from $SRC to $DEST"

Before you use this template, replace ``PARTITION_GOES_HERE`` with the
appropriate partition for the HPCS you are using. Refer to the
system-specific pages for that information.

After you update the template and save it locally as a batch job, submit it to
the batch system. Watch for the exit status. If it does not finish in 8 hours,
resubmit it. Once it finishes successfully, add ``-v`` to the rsync line and
submit it one more time. Examine the output file carefully to make sure there
are no errors.

If after several tries the transfer still has not completed, and the errors
are not obvious from the batch job output, refer to the :ref:`getting help
<getting_help>` pages and ask for assistance. Include the file paths of the
output files of your transfer jobs.

.. _tuning_and_troubleshooting:

=================================
Tune Your Host and Troubleshoot
=================================

Tuning Hosts to Improve Data Transfer Rates
===========================================

The standard tuning parameters for network settings are not optimal for
high-latency transfers, which means any transfer to or from Ursa unless you
are in West Virginia. The right settings depend on where you are and the
latency between your system and Ursa. A good place to start is to change the
settings on your local host to match:

.. code-block:: shell

    net.core.rmem_max=16777216
    net.core.wmem_max=16777216
    net.ipv4.tcp_rmem=4096 87380 16777216
    net.ipv4.tcp_wmem=4096 65536 16777216

For a good reference on how to tune your host, see the ESnet `host tuning
guide <https://fasterdata.es.net/host-tuning/>`_.

Additional tuning depends on where your system is located, the type of
network interface your host has, and many other options. Work with your local
network administrators to tune your local hosts and maximize network
performance.

My Job Runs to Completion but the Files Are Not Transferred
===========================================================

Look at the job output for obvious errors. It is in your home directory in a
file starting with ``data-transfer-job-``. If your job completes and the files
appear not to have transferred, read that file for clues.

If you are not a regular user of the batch system, it is likely that your
initialization files are printing messages -- typically with an ``echo``
command -- that are causing the jobs to fail.

If this happens, you could rename your initialization files (:file:`.cshrc`,
:file:`.tcshrc`, :file:`.bashrc`, :file:`.login`, :file:`.profile`,
:file:`.bash_profile`) temporarily and try again. A better solution is to
address the problems caused by these initialization files.

Were All My Files Transferred?
==============================

Look at the job output. It is in your home directory in a file starting with
``data-transfer-job-``. When the job completes, read that file for clues and
errors. You can ignore WARNings and other messages, but any message with the
string "FATAL" suggests an incomplete transfer. That can happen because you
ran out of time, or because of other problems. If your job exited because it
ran out of time, you should be able to resubmit the job, but be sure to add
the ``--resume`` option.

.. _Globus App: https://app.globus.org/
