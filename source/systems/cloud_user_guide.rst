.. _cloud-user-guide:

****************
Cloud User Guide
****************

.. grid:: 1 1 2 2

    .. grid-item::

        1. Log into the `NOAA RDHPCS Cloud gateway <https://noaa.parallel.works>`_

        2. :ref:`Create a cluster <create_cluster>` with the desired size and
           configuration.  Start the Cluster.

        3. Data transfer can be completed either after the cluster has been started
           by pulling th data from the master node, or pushing the data from the
           remote machine to a project space in the user's object storage.

           If the user is planning to use object storage and needs to move data
           between the cloud and a remote resource, install the cloud provider's
           command line utility (e.g., awscli (aws), gsutil (gcp), Azure CLI
           (Azure)).

           The preferred location for staging data to and from NOAA is the
           :ref:`Niagara System <niagara-user-guide>` using the :ref:`Niagara
           Untrusted DTN <niagara-data-transfer>`.

        4. Complete the necessary computations.

        5. Transfer data back to an on-premise location or to the user's S3 (AWS),
           GCP, or Azure bucket.

           If it doesn't already exist, create a directory with your username before
           using it.  This space can be considered as *permanent* as it will
           continue to exist after the cluster has been shutdown.  It will be
           available for subsequent cluster instantiations.

           Even though files in this file sysytem are directly accessible to the
           cluster, copying frequently used file in Luster before the application is
           run is recommended.

        6. Shut down the cluster.

           .. warning::

                When the cluster is shut down, all data in the Lustre and local file
                systems will be lost!  Only the data in the object storage bucket and
                ``/contrib`` will remain.  It is important to copy the data to an object
                store or to a remote location.

    .. grid-item::

        .. mermaid::

            flowchart TD
                step1[1. Log into the Cloud Gateway]
                step2[2. Create a cluster]
                step3[3. Transfer data to the Cloud]
                step4[4. Complete necessary computations]
                step5[5. Transfer data back from Cloud]
                step6[6. Shut down the cluster]
                step1-->step2-->step3-->step4-->step5-->step6
                click step1 "https://noaa.parallel.works"
                click step2 "#create-cluster"
.. _cloud-system-overview:

System Overview
===============

Connecting
==========

Data and Storage
================

Software
========

.. _create_cluster:

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

Training
========

Training videos available:

.. toctree::
   :maxdepth: 1

   cloud/workshop_20230323
   cloud/workshop_20230216
