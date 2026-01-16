.. _connecting-to-rdhpcs:

##########
Connecting
##########

.. _Account Information Management:	https://aim.rdhpcs.noaa.gov

Connecting for the first time
=============================

All connections to the NOAA RDHPCS enclave are done via Secure Shell
(SSH) in a terminal session to a Bastion, or via a web browser to
`ParallelWorks <https://noaa.parallel.works>`__.  See our :ref:`ParallelWorks guide <cloud-user-guide>`.

.. note::

   For access to the MSU HPC systems Orion and Hercules, please review
   the :ref:`MSU-HPC <MSU-HPC-user-guide>` user guide.

Authentication is via a :ref:`CAC/PIV card<common-access>` or
YubiKey Multi-Factor Authentication.

Internal to the enclave, `X509 certificates
<https://en.wikipedia.org/wiki/X.509>`__ are used to authenticate
between resources.  At first login, and at yearly intervals, a master
certificate valid for one year is created (SSH Bastion login required)
with a user-defined pass-phrase.  At each successive log in, a
thirty-day proxy certificate is created and used for resource access
and data transfers.

.. attention::

   You must have access to an RDHPCS resource (system) in order to log
   into it!  Visit the `Account Information Management`_ website to
   view your RDHPCS profile and system access.


Access to most RDHPCS systems require a signed x.509 certificate.  The
first login attempt will generate a master certificate request.  You
will experience a short (less than 5 minute) delay while the request
is signed. Users cannot fully log on to a system until that
certificate is signed.

The prompt will ask you to create a passphrase. Create a passphrase
with a minimum of three words.

.. note::

    Do not worry if you forget your passphrase -- just continue to
    try.  On the 4th attempt the system will prompt you to recreate
    your master certificate.

.. _ssh_access:

Secure Shell (SSH) Access
=========================

Access to on premise RDHPCS compute resources is done using the Secure Shell
(SSH) protocol to one of the system's bastions, or via ParallelWorks.

MSU systems (Orion, Hercules) are accessed via SSH or OpenOnDemand.
See MSU-HPC :ref:`MSUHPC-logging-in` for instructions.

SSH clients are available for Windows-based systems, such as published
by VanDyke software.  For recent SecureCRT versions, the preferred
authentication setting is shown above.

For Windows systems, `PuTTY
<https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_,
`SecureCRT <https://www.vandyke.com/products/securecrt/>`_, or
`MobaXterm <https://mobaxterm.mobatek.net/>`_ can also be used to
provide SSH capability.  Recent updates to Windows 10 and Windows 11
have added built-in support for SSH.  If it is not installed on your
version of Windows, please refer to Microsoft's `documentation on
OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025>`_.

.. _bastion_hostnames:

Bastion Hostnames
=================
.. |CBHN|	replace:: **CAC Bastion hostnames**
.. |RBHN|	replace:: **RSA Bastion hostnames**
.. |GCPRNG|	replace:: gaea.princeton.rdhpcs.noaa.gov
.. |GCBRNG|	replace:: gaea.boulder.rdhpcs.noaa.gov
.. |GRPRNG|	replace:: gaea-rsa.princeton.rdhpcs.noaa.gov
.. |GRBRNG|	replace:: gaea-rsa.boulder.rdhpcs.noaa.gov

.. |HCPRNG|	replace:: hera.princeton.rdhpcs.noaa.gov
.. |HCBRNG|	replace:: hera.boulder.rdhpcs.noaa.gov
.. |HRPRNG|	replace:: hera-rsa.princeton.rdhpcs.noaa.gov
.. |HRBRNG|	replace:: hera-rsa.boulder.rdhpcs.noaa.gov

.. |JCPRNG|	replace:: bastion-jet.princeton.rdhpcs.noaa.gov
.. |JCBRNG|	replace:: bastion-jet.boulder.rdhpcs.noaa.gov
.. |JRPRNG|	replace:: jet-rsa.princeton.rdhpcs.noaa.gov
.. |JRBRNG|	replace:: jet-rsa.boulder.rdhpcs.noaa.gov

.. |PPPRNG|	replace:: bastion-analysis.princeton.rdhpcs.noaa.gov
.. |PPBRNG|	replace:: bastion-analysis.boulder.rdhpcs.noaa.gov
.. |PAPRNG|	replace:: analysis-rsa.princeton.rdhpcs.noaa.gov
.. |PBPRNG|	replace:: analysis-rsa.boulder.rdhpcs.noaa.gov

.. |MCPRNG|	replace:: mercury-cac.princeton.rdhpcs.noaa.gov
.. |MCBRNG|	replace:: mercury-cac.boulder.rdhpcs.noaa.gov
.. |MRPRNG|	replace:: mercury-rsa.princeton.rdhpcs.noaa.gov
.. |MRBRNG|	replace:: mercury-rsa.boulder.rdhpcs.noaa.gov

.. |UCPRNG|	replace:: ursa-cac.princeton.rdhpcs.noaa.gov
.. |UCBRNG|	replace:: ursa-cac.boulder.rdhpcs.noaa.gov
.. |URPRNG|	replace:: ursa-rsa.princeton.rdhpcs.noaa.gov
.. |URBRNG|	replace:: ursa-rsa.boulder.rdhpcs.noaa.gov

.. |OUG|	replace:: :ref:`orion-user-guide`

+-------------------+-----------------+----------------------------------+
| **RDHPCS System** | |CBHN|          | |RBHN|                           |
+-------------------+-----------------+----------------------------------+
| Gaea              | |GCPRNG|        | |GRPRNG|                         |
|                   |                 |                                  |
|                   | |GCBRNG|        | |GRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| Hera              | |HCBRNG|        | |HRBRNG|                         |
|                   |                 |                                  |
|                   | |HCPRNG|        | |HRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Jet               | |JCBRNG|        | |JRBRNG|                         |
|                   |                 |                                  |
|                   | |JCPRNG|        | |JRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| PPAN              | |PPPRNG|        | |PAPRNG|                         |
|                   |                 |                                  |
|                   | |PPBRNG|        | |PBPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Mercury           | |MCBRNG|        | |MRBRNG|                         |
|                   |                 |                                  |
|                   | |MCPRNG|        | |MRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Ursa              | |UCBRNG|        | |URBRNG|                         |
|                   |                 |                                  |
|                   | |UCPRNG|        | |URPRNG|                         |
+-------------------+-----------------+----------------------------------+

In addition to the Bastions, RDHPCS users have access to computational capacity
on the Orion and Hercules systems, hosted by Mississippi State University. See
the :ref:`MSU-HPC <MSU-HPC-user-guide>` user guide.
for detailed information.

Computational capacity is also available on the RDHPCS Cloud Platform, which
allows NOAA users to create custom HPC clusters on an as-needed basis, through
the Parallel Works platform. The :ref:`Cloud User Guide <cloud-user-guide>`
provides more information.


.. _Common-access:
.. _cac_instructions:

Common Access Card (CAC) SSH Login
==================================

RDHPCS users with a CAC who are logging in from a Windows, Mac, or
Linux system are recommended to use a CAC login. This requires a CAC
reader and software from Tectia. If you recently were issued a new CAC
or renewed CAC, please log into the `Account Information Management`_
website to update the CAC information.

Reference the :ref:`Tectia` pages for complete information on how to
configure Tectia initially for login using SSH with your CAC.

.. code-block:: console

    $ sshg3 CAC-BASTION-HOSTNAME

#. Reference the table above for the appropriate CAC Bastion to use.
#. When prompted, enter your CAC PIN.


.. _yubikey_instructions:

Yubikey SSH Login
=================

RDHPCS users who do not have a CAC, or lack the required hardware or
software, are welcome to use their NOAA issued Yubikey to login. You
must have :ref:`configured and registered your Yubikey for NOAA RDHPCS
access. <yubikey-user-instructions>`

.. code-block:: console

    $ ssh RSA-BASTION-HOSTNAME


#. The RSA bastions are used for Yubikey logins.
#. Reference the table above for the appropriate RSA Bastion to use.
#. When prompted, enter your Yubikey PIN then press and hold your Yubikey
   (long press).

Selecting a Node
================

RDHPCS systems accessed via SSH allow users to select a specific head
node at login.  After successful authentication at the bastion host, a
list of available nodes will be displayed with a 5 second delay to
choose a specific destination.  To select a specific host, press
Control+C (^C) and enter the desired node.

Here is an example of what the display looks like for the Gaea system
mid 2024:

.. code-block:: shell


     Welcome to the NOAA RDHPCS.

     Attempting to renew your proxy certificate...Proxy certificate has 720:00:00  (30.0 days) left.

             Welcome to gaea.rdhpcs.noaa.gov
     Gateway to gaea-c5.ncrc.gov and other points beyond

     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     !! RDHPCS Policy states that all user login sessions shall be terminated     !!
     !! after a maximum duration of seven (7) days. ALL user login sessions will  !!
     !! be dropped from the Princeton Bastions at 4AM ET / 2AM MT each Monday     !!
     !! morning, regardless of the duration. Please note: This will NOT impact    !!
     !! batch jobs, cron scripts, screen sessions, remote desktop, or data        !!
     !! transfers.                                                                !!
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

     Hostname            Description
     gaea                C5 head nodes
     gaea51              C5 head node
     gaea52              C5 head node
     gaea53              C5 head node
     gaea54              C5 head node
     gaea55              C5 head node
     gaea56              C5 head node
     gaea57              C5 head node
     gaea58              C5 head node
     gaea60              T6 Test access only
     gaea61              C6 head node
     gaea62              C6 head node
     gaea63              C6 head node
     gaea64              C6 head node
     gaea65              C6 head node
     gaea66              C6 head node
     gaea67              C6 head node
     gaea68              C6 head node

     You will now be connected to NOAA RDHPCS: Gaea (CMRS/NCRC) C5 system.
     To select a specific host, hit ^C within 5 seconds.


.. note::

    After the 5 second wait, the bastion node will use a load balancer to select
    a node.


X11 Graphics
============

Users can use SSH X11 forwarding to open GUI-based applications (e.g., xterm,
ARM Forge).  This is typically done using an SSH option.  For the :ref:`Tectia`
client :command:`sshg3` or OpenSSH-based clients, use the ``-X`` option:

.. code-block:: console

    $ sshg3 -X host.url

or

.. code-block:: console

    $ ssh -X host.url

Other clients, like PuTTY, will have an option when configuring the host.

The base SSH X11 forwarding is typically slow.  RDHPCS systems use X2Go for
improved X11 performance.  Some users have found it difficult to use X2Go.
Please submit a :ref:`support issue <getting_help>` if you have issues using
X2Go.

.. note::

    Microsoft Windows users can use any of the X11 servers available for
    Windows.  The SSH client will need to be configured to use the X11 server
    for forwarding X11.

.. _ssh-port-tunnels:

SSH Port Tunnels
================

To allow users to easily transfer small files to and from the RDHPCS
systems, the bastion configures SSH port-forwarding tunnels.  To use these
tunnels, the user must configure their local SSH client to create tunnels
to/from the bastion.

See the Port Tunnel section of the :ref:`Tectia` page for details.  You can use
:ref:`this form <openssh-config>` to create a sample SSH configuration for
OpenSSH-based clients.


Web based ParallelWorks Access
==============================

.. _web-parallel-works:

**************
Parallel Works
**************


RDHPCS includes a platform to create and use custom high-performance computing
clusters on an as-needed basis. Users can create these clusters using cloud
computing resources across Amazon Web Services (AWS), Google Compute Platform
(GCP), and Microsoft Azure Cloud Computing Services (Azure) via the NOAA RDHPCS
Portal, customized for NOAA. The same platform can manage computing resources
in on-premise systems.

The platform is Parallel Works, aka ACTIVATE. Operation is identical for both
Cloud and on-premise systems.

The typical process to use Parallel Works is:

* Log in Create or start a cluster
* Transfer data in to the cluster
* Perform computations
* Transfer data out.

To access Parallel Works, sign in to the
`Parallel Works NOAA Portal <https://noaa.parallel.works/sso>`_.

.. image:: /images/pw-portal.png
    :scale: 50%

Authenticate to the system using your CAC, or your Username, Password and MFA
key. The Home page displays:

.. image:: /images/pw-home.png
    :scale: 50%

The Home page shows available workflows and storage clusters, session status,
and the results of any workflow runs. The Workflows pane shows workflows
available right now. The Workflow Runs pane displays the status of the jobs you
have run. The Compute pane shows your active clusters, and lets you turn them
on and off and monitor their progress.  You can set a cluster to notify you
every hour while your cluster is running. The Buckets pane shows your available
storage options.

You can customize your home page. Click the **Customize** button, located on
the top right corner. Click **+Add Widget** to choose your preferred widget.
click **DONE** when completed.

About Marketplace
=================

The Parallel Works (PW) platform offers a set of pre-configured workflows for
your use, on the Marketplace page. To access the Marketplace, click the
Marketplace link located on the left side menu from the Home page.  On the
Marketplace page, you can select pre-configured workflows, storage resources,
and compute resources for your projects.

.. image:: /images/pw-marketplace.png
    :scale: 40%


.. note::

    You create On-Prem Cluster Configurations using the defined on-prem
    configurations located under the Compute Resource section.  You can find the
    cluster definition for Mercury system, Ursa, and PPAN Cluster here. Additional
    information on the workflows can be found at the `Marketplace link
    <https://parallelworks.com/docs/navigating-the-marketplace>`_.


You can load these workflows to your account, and run them in the computing
clusters you create. You can also access predefined storage and compute
resources.

.. Note::

    The Workflows, Storage Resources and Compute Resources that
    you can use depend on your RDHPCS project assignments. You can review your
    current accounts, and request access, using the `Account Information Management
    (AIM) <https://aim.rdhpcs.noaa.gov/>`_ website. AIM accounts are discussed
    `here. <https://docs.rdhpcs.noaa.gov/accounts/accounts_and_projects.html#request-access-to-rdhpcs-projects>`_

Workflows are the shared scripts you can use to complete tasks in Parallel
Works. From the Run tab, click the Workflow button to review available
workflows. To add a workflow to your account, click the **Add** button.

.. image:: /images/pw-add.png
    :scale: 60%

Clusters
========

Clusters are computing resources that you create, either in the Cloud or
on-premise systems. You can create clusters on any system where you have
access. You can create clusters in the Cloud, or on on-prem systems. When you
click Clusters in the Compute menu, a list of your available clusters displays:

.. image:: /images/cluster7.png
    :scale: 60%

When you click an individual cluster, you can review the cluster configuration
and control its operation:

.. image:: /images/cluster1.png
    :scale: 60%

.. note::

    Cloud provider regions often have varying concentrations of specific processor
    types. For instance, the AWS us-east-1 region is recognized for its
    abundance of large Intel processors, whereas another region, also listed as
    us-east-2, is known for having larger AMD processors.

Availability of on-demand VMs can fluctuate based on market conditions. If a
request for instance capacity fails in a specific availability zone (AZ) due to
insufficient quantity, the cluster can be configured to use a multi-zone
option. Enabling multi-zone availability via the "partition" section of the
cluster configuration allows the PW to provision instances across multiple AZs.
While this option helps meet capacity requirements, it may introduce a
marginally higher latency.

To add a new cloud cluster, following the instructions in the
`PW Cluster section <https://parallelworks.com/docs/compute/creating-clusters>`_.

When you create a new cluster configuration, first enter the cluster name. At
the definition page choose the **LOAD FROM MARKETPLACE** link, located at the
top left of the page, to restore the default values. You may want to edit the
definition, for example resizing the partition size to fit your need.

.. image:: /images/cluster2.png
    :scale: 60%

Click Edit to review and adjust an existing cluster definition.

General Settings
================

.. image:: /images/cluster4.png
    :scale: 60%

Use the General Settings tab to name and describe a cluster.


Controller Settings
===================

.. image:: /images/cluster5.png
    :scale: 60%


In this tab, you select the region, zone, and image type for the instance,
also referred to as the head node. For a seamless code migration, choose an
image type with the same Operating System (OS) version as your existing
on-premise OS version.

Controller Disks
================

.. image:: /images/cluster8.png
    :scale: 60%

The Controller Disks incorporate two main application file systems: NOAA RDHPCS
“apps” and PW’s “apps.” The RDHPCS apps disk is a mirrored copy of the
on-premise system Ursa’s apps file system. The PW apps file system contains
specialized libraries that are not included in the RDHPCS apps but are
necessary for utilizing certain instance types, such as those based on NVidia
GPUs.


Partitions
==========

.. image:: /images/partition1.png
    :scale: 60%

Partitions are the worker bees of the HPC computing. You can create as many
partitions with differing instance types as you need to fulfill your workflow
needs.

For minimal latency, we recommend keeping partitions in a single zone. However
you can enable the multi-zone option to achieve the capacity if one AZ is
unable to meet your requirements.

Preemptible instances (also known as Spot VMs) are a cost-effective option for
cloud computing. They are interruptible virtual machines offered by cloud
providers, utilizing their spare capacity. Because they can be taken away with
little notice, they are best suited for short-term, fault-tolerant workloads.

For resources like GPUs or high-end AMD HPC processor instances, which are
typically difficult to find on-demand, you can request a short-term reservation
by contacting the cloud help desk.

Attached Filesystems
====================

Filesystems serve as collaborative workspaces for storing code libraries and
can be shared among project members.

You have the flexibility to attach multiple storage types, such as bucket
(Object storage) and NFS, to a cluster, as required.

.. attention::

    Storage must be provisioned via the "Storage" menu before it can be included in
    the cluster definition. When including storage, you must specify a mount point
    name (e.g., "/contrib").


For additional information, see the `PW user guide <https://parallelworks.com/docs/storage>`_.

Advanced Settings
=================

.. image:: /images/pw-test.png
    :scale: 60%


The Advanced settings provide further customization. Here you can, for example,
incorporate bootstrap scripts to run before the cluster is initialized. You can
also adjust the suspend time for when the partition stops. By default, an idle
partition is released after 5 minutes.

The User Workspace option is necessary if you intend to use the Explorer to
transfer files between the cluster and your workstation.

Alerts
======

You can set runtime alerts to notify you at set intervals as the cluster stays
alive.  We strongly recommend setting this value, as it can help to prevent
incurring charges on an unused cluster.

After the edits are made, click the **SAVE CHANGES** link at the top
of the page.

Start, Resume, Stop and Destroy
===============================

.. image:: /images/pw-test.png
    :scale: 70%

Managing Cluster State
======================

* Click the **Start** link to start a cluster.

* Use the **Stop** link to stop a cluster if you have customized the
   controller node with non-standard software and plan to restart the cluster
   later.  Stopping the cluster deletes the partition cluster and ephemeral
   Lustre but retains the root disk. Persistent Lustre and other persistent
   storage remain active. Charges will still apply for the saved root disk,
   though this amount is minimal per day.

* A stopped cluster can be restarted
   using the **Resume** link.

*  Use the **Destroy** link to completely delete the cluster resources,
   including ephemeral Lustre. Note that the bucket, NFS storage, and
   persistent storages are not deleted.

Explorer
========

The Explorer is a file management tool. You can use the tool for file transfer
to a bucket or filesystems in a cluster.





