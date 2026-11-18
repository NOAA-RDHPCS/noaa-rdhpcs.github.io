.. meta::
   :description: Guide to installing and using Remote Desktop (Parallel Works) on
    RDHPCS systems
   :keywords: Remote Desktop, Parallel Works, ACTIVATE

.. _parallel-works:

*************************************************
Remote Desktop (Parallel Works) on RDHPCS Systems
*************************************************

This section provides an overview of the directions, workflows, operations,
and best practices to use the Parallel Works
platform on the NOAA RDHPCS environment across AWS, GCP, and Azure, as well as
RDHPCS on-premises systems.


Prerequisites & Account Setup
=============================

Access Requirements
-------------------
   * Active NOAA user account. (See :ref:`applying_for_user_account`
     for details.)
   * NOAA-issued YubiKey registered for RDHPCS access.
     (See :ref:`yubikey-user-instructions` for details.)
   * Active cloud project allocation (e.g., ca- for AWS, cg- for GCP,
     cz- for Azure). (see :ref:`project_request` for details.)


Authentication
--------------

   #. Log into the Parallel Works NOAA Portal.
   #. Authenticate via NOAA Single Sign-On (SSO) using CAC or YubiKey.

Managing Workflows
=====================

To create a new workflow:

   #. Select the desired cloud provider (AWS, GCP, Azure) or
      on-premises system.
   #. Configure the workflow parameters (e.g., compute
      resources, storage, etc.).
   #. Upload your input data and scripts.
   #. Submit the workflow for execution.
   #. Monitor the workflow status and retrieve results upon completion.


To add an existing workflow to your account:

  #. Click the Marketplace (Earth icon) in the sidebar menu.
  #. Browse available workflow scripts (e.g., Jupyter, VS Code,
     default HPC templates).
  #. Click Fork to subscribe and add a workflow template to your account.

Accessing Head / Controller Nodes
=================================

Web Interface / Web Terminal Access
-----------------------------------

   #. Navigate to the Compute dashboard.
   #. Click the "i" (info) icon to retrieve the cluster's IP address.
   #. Click the IDE link (top right) to open a web terminal.
   #. Select Terminal > New Terminal.
   #. Connect via SSH: ssh <username@head-node-IP>.

SSH CLI / External Tunneling
----------------------------

   #. Add your SSH public key under Account > Authentication for
      auto-population across all clusters.
   #. Set up local SSH tunnels for remote port forwarding:

.. code-block:: shell

     ssh -N -L <local_port>:<remote_host>:<remote_port> <remote_user>@<remote_host_IP>

Running Development Tools & Workflows
=====================================

VS Code Workflows & Sessions
-----------------------------

Via Cluster Web GUI
^^^^^^^^^^^^^^^^^^^

   #. Navigate to the Compute dashboard.
   #. Click the "i" (info) icon to retrieve the cluster's IP address.
   #. Click the IDE link (top right) to open a web terminal.
   #. Select Terminal > New Terminal.
   #. Connect via SSH: ssh <username@head-node-IP>.
   #. Launch VS Code:

   .. code-block:: shell

      code --no-sandbox --user-data-dir=/tmp/vscode --extensions-dir=/tmp/vscode-extensions
      code --no-sandbox --user-data-dir=/tmp/vscode --extensions-dir=/tmp/vscode-extensions


Via PW Command Line Interface (PW CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. Verify Workspace version ≥ 7.96.0 under Account profile.
   2. Generate API key or access token under Authentication > API Keys.
   3. Authenticate locally: pw auth apikey (or pw auth token).
   4. Launch VS Code targeting a Slurm partition:

.. code-block:: shell

      ``pw vscode --environment u1-compute --param account=<account> --param qos=<qos> --param
      walltime=00:30:00 --param nodes=1 --param ntasks-per-node=1 <cluster_name>``


Upon completion of your VS Code session, terminate the worker session to
free up resources:

      .. code-block:: shell

         pw.exe workers delete <worker_ID>

Working with Slurm Scheduler
============================

Monitoring Nodes & Jobs
-----------------------

   #. Check partition status: sinfo or sinfo --summarize
   #. View active queue: squeue
   #. State indicator symbols: ~ (power saving/off), # (powering up),
      % (powering down), idle (active & ready).

Job Distribution & Power Management
-----------------------------------

   1. Submit jobs across isolated nodes using sbatch --exclusive
      or #SBATCH --exclusive.
   2. Modify Slurm suspend idle timeout on live cluster

   .. code-block:: shell

      sudo sed -i 's/SuspendTime=.*/SuspendTime=3600/g' /mnt/shared/etc/slurm/slurm.conf
      sudo scontrol reconfigure

   3. Manually power down idle nodes:

      ``sudo scontrol update nodename=<node_list> state=power_down``

   4. Manually resume nodes:

      ``sudo scontrol update nodename=<node_list> state=resume``

File Transfers & Storage Management
===================================

Overview of Storage Types
-------------------------

+--------------------+-----------------------------------------+-----------------------------------------+
| Storage Type       | Description                             | Common Use Cases                        |
+====================+=========================================+=========================================+
| Object Storage     | Persistent object storage               | Long-term data archiving, backups,      |
| (Bucket / Blob)    | (S3, GCP Bucket, Azure Blob)            | and large input/output datasets         |
+--------------------+-----------------------------------------+-----------------------------------------+
| Shared EFS/NFS     | Shared filesystem across project users  | Team software libraries, shared scripts |
|                    |                                         | and persistent custom packages          |
+--------------------+-----------------------------------------+-----------------------------------------+
| Lustre File System | High-performance parallel filesystem    | High-IOPS active model execution and    |
|                    | (ephemeral or persistent)               | scratch space during                    |
+--------------------+-----------------------------------------+-----------------------------------------+

Data Transfer Methods
---------------------

PW Short-Term Bucket Token (up to 24hours)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   pw buckets get-token s3://<bucket_name> > aws-creds
   source aws-creds
   aws s3 ls s3://<bucket_name>

Command Line Utilities
^^^^^^^^^^^^^^^^^^^^^^^

   * AWS CLI: ``aws s3 cp <file> s3://<bucket_name>/``
   * GCP CLI: ``gsutil cp <file> gs://<bucket_name>/``
   * Azure CLI: ``azcopy copy <file> "https://<account>.blob.core.windows.net/<container>"``

Globus Personal Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^

 #. Run ``./globusconnectpersonal -setup`` on master node and authenticate.
 #. Start service: ``./globusconnectpersonal -start &``
 #. Initiate transfers via Globus CLI (``globus transfer``).


Browser File Explorer
^^^^^^^^^^^^^^^^^^^^^

Map Home/Bucket/Contrib under
:gui-label:`Advanced Settings > User workspace mount points`, then
upload/download via Editor.

Operational Best Practices & Cost Management
============================================

Prevent Home Quota Errors ($HOME/pw)
-------------------------------------

Symlink $HOME/pw to your project directory space to avoid exceeding strict
home quotas during workflow software installs:

.. code-block:: shell

   mv $HOME/pw /path/to/project/space/pw
   ln -s /path/to/project/space/pw $HOME/pw

Cost Optimization Strategies
----------------------------

   * **Cluster Shutdown**: Select **Destroy** when shutting down
     standard clusters. Use **Stop/Hibernation** only if retaining
     un-snapshotted boot disk modifications (incurs disk storage fees).
   * **Runtime Alerts & Limits**: Enable hourly runtime alerts and session cost
     limits in cluster resource properties.
   * **Regional Co-location**: Ensure compute clusters and storage buckets
     remain in the same cloud region (e.g., us-east-1) to prevent egress
     charges.

