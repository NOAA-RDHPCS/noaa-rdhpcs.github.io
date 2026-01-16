.. _parallel-works:

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
--------

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

When you create a new cluster configuration, first enter the cluster name.
At the definition page choose the **LOAD FROM MARKETPLACE** link, at the
top left of the page, to restore the default values. You may want to edit the
definition, for example resizing the partition size to fit your need.

.. image:: /images/cluster2.png
    :scale: 60%

Click Edit to review and adjust an existing cluster definition.

General Settings
^^^^^^^^^^^^^^^^

.. image:: /images/cluster4.png
    :scale: 60%

Use the General Settings tab to name and describe a cluster.


Controller Settings
^^^^^^^^^^^^^^^^^^^

.. image:: /images/cluster5.png
    :scale: 60%


In this tab, you select the region, zone, and image type for the instance,
also referred to as the head node. For a seamless code migration, choose an
image type with the same Operating System (OS) version as your existing
on-premise OS version.

Controller Disks
^^^^^^^^^^^^^^^^

.. image:: /images/cluster8.png
    :scale: 60%

The Controller Disks incorporate two main application file systems: NOAA RDHPCS
“apps” and PW’s “apps.” The RDHPCS apps disk is a mirrored copy of the
on-premise system Ursa’s apps file system. The PW apps file system contains
specialized libraries that are not included in the RDHPCS apps but are
necessary for utilizing certain instance types, such as those based on NVidia
GPUs.


Partitions
^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^


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
^^^^^^^^^^^^^^^^^

.. image:: /images/pw-test.png
    :scale: 60%


The Advanced settings provide further customization. Here you can, for example,
incorporate bootstrap scripts to run before the cluster is initialized. You can
also adjust the suspend time for when the partition stops. By default, an idle
partition is released after 5 minutes.

The User Workspace option is necessary if you intend to use the Explorer to
transfer files between the cluster and your workstation.

Alerts
^^^^^^

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
----------------------

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













