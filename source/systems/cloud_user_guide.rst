
.. _cloud-user-guide:

****************
RDHPCS Cloud Computing 
****************

Welcome to the NOAA RDHPCS Cloud Computing Platform. The Cloud Platform allows NOAA users to create an HPC cluster on an as-needed basis, with the type of resources that are appropriate for the task at hand.

You can find directions to log into the NOAA RDHPCS Cloud Gateway `here. <https://noaa.parallel.works.>`_ 


Parallel Works User Guide
=========================

NOAA Cloud Computing uses the Parallel Works software application, in a version customized for NOAA RDHPCS.  The Parallel Works User Guide is their standard documentation. NOAA users will find minor differences, for example, the login authentication, and project allocation, between the standard and customized applications.

We recommend the Parallel Works User Guide for comprensive information about the product. Users should click the FAQ link located on the sidebar to learn about the NOAA RDHPCS-specific topics.

Click here to access the `Parallel Works User Guide <https://docs.parallel.works/>`_ . Note that when you click this link, you will navigate aways from the NOAA Cloud information page.

Click here for the `NOAA RDHPCS login to Parallel Works <https://noaa.parallel.works/login>`_ .


.. note::
    When you click this link, you will navigate away from the NOAA Cloud information page.

    **User Name** is case sensitive, and is First.Last name, where the first character of first, and last name is an uppercase letter.
    **Password:** Combination of your passphrase and 8 digits PIN from NOAA-RDHPCS RSA token.


Workflow
==========

The typical workflow for using the cloud resources is as follows:


.. image:: /images/CloudProcessing.jpg



Globus Connect
-----------

Globus is a tool for online data transfer.  
See the `Globus Connect documentation <https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/Additional_Topics#Globus_Connect>`_ for further information.

Getting Help
------------

For questions or assistance, email a ticket to: rdhpcs.cloud.help@noaa.gov, with the subject line Cloud Support.
Please send your feedback on product, support, and documentation to Unni Kirandumkara, at: Unni.Kirandumkara@noaa.gov.


Cloud Success Stories
==================

NOAA teams have used the power and flexibilty of Cloud computing in critical situations.

-  `NOS Team: Storm Surge Modelling <https://drive.google.com/file/d/12WWIjj-ULJkkAtxbMnerq8LAdWSvR7gd/view?usp=sharing>`__  September 27, 2023

-  `NWS Team: Rapid Refresh Forecast System <https://drive.google.com/file/d/1ESypA2IRLKAzAvrxjmVAi1mhnIS7OwtK/view?usp=sharing>`__  September 21, 2022

-  `EPIC Cloud Success  Story <https://drive.google.com/file/d/1muXZQ6uTDFEnGNUG5ZJ_R59D9HwBWDP9/view>`__  September 15, 2022

         
Frequently Asked Questions
=====================
.. container:: noprint
   :name: mw-page-base

.. container:: noprint
   :name: mw-head-base

.. container:: mw-body
   :name: content

   .. container::
      :name: siteNotice

   .. container:: mw-indicators

   .. rubric:: FAQ
      :name: firstHeading
      :class: firstHeading mw-first-heading

   .. container:: vector-body
      :name: bodyContent

      .. container:: noprint
         :name: siteSub

         From clouddocs

      .. container::
         :name: contentSub

         .. container::
            :name: mw-content-subtitle

      .. container::
         :name: contentSub2

      .. container::
         :name: jump-to-nav

      `Jump to navigation <#mw-head>`__ `Jump to
      search <#searchInput>`__

      .. container:: mw-body-content mw-content-ltr
         :name: mw-content-text

         .. container:: mw-parser-output

            Frequently Asked Questions

            .. container:: toc
               :name: toc

               .. container:: toctitle

                  .. rubric:: Contents
                     :name: mw-toc-heading

               -  `1 General Cloud Issues <#General_Cloud_Issues>`__

                  -  `1.1 How do I open a cloud help desk
                     ticket? <#How_do_I_open_a_cloud_help_desk_ticket?>`__
                  -  `1.2 Where do I find instructions to connect the
                     controller node from outside the
                     network? <#Where_do_I_find_instructions_to_connect_the_controller_node_from_outside_the_network?>`__
                  -  `1.3 What are the project allocation usage limits
                     and
                     actions? <#What_are_the_project_allocation_usage_limits_and_actions?>`__
                  -  `1.4 How do I get a project allocation or an
                     allocation
                     increase? <#How_do_I_get_a_project_allocation_or_an_allocation_increase?>`__
                  -  `1.5 Storage
                     functionalities <#Storage_functionalities>`__
                  -  `1.6 How do I resize the root
                     disk? <#How_do_I_resize_the_root_disk?>`__
                  -  `1.7 Where do I get detailed Workflow
                     instructions? <#Where_do_I_get_detailed_Workflow_instructions?>`__
                  -  `1.8 What are the different storage types and costs
                     available on the PW
                     platform? <#What_are_the_different_storage_types_and_costs_available_on_the_PW_platform?>`__

               -  `2 Parallel Works <#Parallel_Works>`__

                  -  `2.1 Where do I find the Parallel Works User
                     Guide? <#Where_do_I_find_the_Parallel_Works_User_Guide?>`__
                  -  `2.2 How do I get access to the Parallel Works
                     Platform? <#How_do_I_get_access_to_the_Parallel_Works_Platform?>`__
                  -  `2.3 How is a new user added to a project on the
                     Parallel
                     Works? <#How_is_a_new_user_added_to_a_project_on_the_Parallel_Works?>`__
                  -  `2.4 How do I set up a new project in the Parallel
                     Works
                     Platform? <#How_do_I_set_up_a_new_project_in_the_Parallel_Works_Platform?>`__
                  -  `2.5 What is the certified browser for Parallel
                     Works
                     Platform? <#What_is_the_certified_browser_for_Parallel_Works_Platform?>`__
                  -  `2.6 Cost Calculator <#Cost_Calculator>`__
                  -  `2.7 Cost dashboard
                     explained <#Cost_dashboard_explained>`__
                  -  `2.8 How do I find a real time cost estimate of my
                     session? <#How_do_I_find_a_real_time_cost_estimate_of_my_session?>`__
                  -  `2.9 How do I estimate
                     core-hours? <#How_do_I_estimate_core-hours?>`__
                  -  `2.10 How to access the head node from the Parallel
                     Works [PW] web
                     interface? <#How_to_access_the_head_node_from_the_Parallel_Works_%5BPW%5D_web_interface?>`__
                  -  `2.11 How do I add a workflow to my
                     account? <#How_do_I_add_a_workflow_to_my_account?>`__
                  -  `2.12 How do I request a new feature or report
                     feedback? <#How_do_I_request_a_new_feature_or_report_feedback?>`__
                  -  `2.13 How to address an authentication issue on the
                     Parallel Works [PW]
                     login? <#How_to_address_an_authentication_issue_on_the_Parallel_Works_%5BPW%5D_login?>`__

               -  `3 Clusters and Snapshots <#Clusters_and_Snapshots>`__

                  -  `3.1 Cluster Cost types
                     explained. <#Cluster_Cost_types_explained.>`__
                  -  `3.2 How do I resize my resource cluster
                     size? <#How_do_I_resize_my_resource_cluster_size?>`__
                  -  `3.3 How do I create a custom snapshot [a.k.a AMI,
                     Snapshot, Boot disk, or machine
                     image]? <#How_do_I_create_a_custom_snapshot_%5Ba.k.a_AMI,_Snapshot,_Boot_disk,_or_machine_image%5D?>`__
                  -  `3.4 How to automatically find the hostname of a
                     cluster? <#How_to_automatically_find_the_hostname_of_a_cluster?>`__
                  -  `3.5 How do I setup an ssh tunnel to my
                     cluster? <#How_do_I_setup_an_ssh_tunnel_to_my_cluster?>`__
                  -  `3.6 How do I turn off Lustre filesystem from the
                     cluster? <#How_do_I_turn_off_Lustre_filesystem_from_the_cluster?>`__
                  -  `3.7 How do I activate conda at cluster
                     login? <#How_do_I_activate_conda_at_cluster_login?>`__
                  -  `3.8 How do I create a resource
                     configuration? <#How_do_I_create_a_resource_configuration?>`__
                  -  `3.9 How do I enable run time alerts on my
                     cluster? <#How_do_I_enable_run_time_alerts_on_my_cluster?>`__
                  -  `3.10 Missing user directory in the group's contrib
                     volume. <#Missing_user_directory_in_the_group's_contrib_volume.>`__
                  -  `3.11 Why does the owner's home directory look
                     different from the shared users’ home
                     directory? <#Why_does_the_owner's_home_directory_look_different_from_the_shared_users’_home_directory?>`__
                  -  `3.12 What are “Compute” and “Batch” sections in a
                     cluster
                     definition? <#What_are_“Compute”_and_“Batch”_sections_in_a_cluster_definition?>`__
                  -  `3.13 How do I manually shutdown the compute
                     nodes? <#How_do_I_manually_shutdown_the_compute_nodes?>`__
                  -  `3.14 How to sudo in as root or a role account on a
                     cluster? <#How_to_sudo_in_as_root_or_a_role_account_on_a_cluster?>`__
                  -  `3.15 How to enable a role
                     account? <#How_to_enable_a_role_account?>`__
                  -  `3.16 Bootstrap script
                     example <#Bootstrap_script_example>`__

               -  `4 Configuration
                  Questions <#Configuration_Questions>`__

                  -  `4.1 How do I create Parallel Works resource
                     configuration on my
                     account? <#How_do_I_create_Parallel_Works_resource_configuration_on_my_account?>`__
                  -  `4.2 How do I get AMD processor resources
                     configuration? <#How_do_I_get_AMD_processor_resources_configuration?>`__
                  -  `4.3 How do I restore a default
                     configuration? <#How_do_I_restore_a_default_configuration?>`__
                  -  `4.4 What is a default instance/vm
                     type? <#What_is_a_default_instance/vm_type?>`__
                  -  `4.5 How do I restore customization after the
                     default configuration
                     restore? <#How_do_I_restore_customization_after_the_default_configuration_restore?>`__
                  -  `4.6 What is NOAA RDHPCS preferred container
                     solution? <#What_is_NOAA_RDHPCS_preferred_container_solution?>`__
                  -  `4.7 Best practice in resource configuration
                     page. <#Best_practice_in_resource_configuration_page.>`__
                  -  `4.8 An example Singularity Container build, job
                     array that uses bind
                     mounts <#An_example_Singularity_Container_build,_job_array_that_uses_bind_mounts>`__

               -  `5 Working with SLURM <#Working_with_SLURM>`__

                  -  `5.1 How to send emails from a Slurm job
                     script? <#How_to_send_emails_from_a_Slurm_job_script?>`__
                  -  `5.2 Introduction to
                     SLURM <#Introduction_to_SLURM>`__
                  -  `5.3 Running and monitoring
                     SLURM <#Running_and_monitoring_SLURM>`__
                  -  `5.4 How to set custom memory for slurm
                     jobs? <#How_to_set_custom_memory_for_slurm_jobs?>`__
                  -  `5.5 How do I change the slurm Suspend time on an
                     active cluster? [shutdown early or shutdown
                     delay] <#How_do_I_change_the_slurm_Suspend_time_on_an_active_cluster?_%5Bshutdown_early_or_shutdown_delay%5D>`__
                  -  `5.6 What logs are needed for the support to
                     research slurm or node not terminated
                     issues? <#What_logs_are_needed_for_the_support_to_research_slurm_or_node_not_terminated_issues?>`__
                  -  `5.7 How do I distribute slurm scripts on different
                     nodes? <#How_do_I_distribute_slurm_scripts_on_different_nodes?>`__
                  -  `5.8 User Bootstrap fails when copy files to
                     lustre <#User_Bootstrap_fails_when_copy_files_to_lustre>`__
                  -  `5.9 What is the command to get max nodes count on
                     a
                     cluster? <#What_is_the_command_to_get_max_nodes_count_on_a_cluster?>`__
                  -  `5.10 Manually reset the node
                     status <#Manually_reset_the_node_status>`__

               -  `6 Errors <#Errors>`__

                  -  `6.1 Error: Error launching source instance:
                     InvalidParameterValue: User data is limited to
                     16384
                     bytes <#Error:_Error_launching_source_instance:_InvalidParameterValue:_User_data_is_limited_to_16384_bytes>`__
                  -  `6.2 Where do I enter my public SSH key in the PW
                     platform? <#Where_do_I_enter_my_public_SSH_key_in_the_PW_platform?>`__
                  -  `6.3 Error “the requested VM size not available in
                     the current region”, when requesting a non-default
                     compute
                     VM/instance <#Error_“the_requested_VM_size_not_available_in_the_current_region”,_when_requesting_a_non-default_compute_VM/instance>`__
                  -  `6.4 What is causing access denied message when
                     trying to access a project’s
                     cluster? <#What_is_causing_access_denied_message_when_trying_to_access_a_project’s_cluster?>`__
                  -  `6.5 Why is my API script reporting “No cluster
                     found”? <#Why_is_my_API_script_reporting_“No_cluster_found”?>`__
                  -  `6.6 What is causing the "Permission denied
                     (publickey,gssapi-keyex,gssapi-with-mic)." ? <#What_is_causing_the_%22Permission_denied_(publickey,gssapi-keyex,gssapi-with-mic).%22_?>`__
                  -  `6.7 What is causing the "do not have sufficient
                     capacity for the requested VM size in this
                     region."? <#What_is_causing_the_%22do_not_have_sufficient_capacity_for_the_requested_VM_size_in_this_region.%22?>`__

               -  `7 Miscellaneous <#Miscellaneous>`__

                  -  `7.1 Parallel Works new features blog
                     posts <#Parallel_Works_new_features_blog_posts>`__
                  -  `7.2 Instance Types
                     explained <#Instance_Types_explained>`__
                  -  `7.3 How to find cores and threads on a
                     node? <#How_to_find_cores_and_threads_on_a_node?>`__
                  -  `7.4 How do I remove my project’s GCP contrib
                     volume? <#How_do_I_remove_my_project’s_GCP_contrib_volume?>`__
                  -  `7.5 How do I find my project’s object storage [aka
                     bucket or block storage] and access keys from
                     Parallel
                     Works? <#How_do_I_find_my_project’s_object_storage_%5Baka_bucket_or_block_storage%5D_and_access_keys_from_Parallel_Works?>`__
                  -  `7.6 Can I transfer files with external object
                     storage [aka bucket or block storage] from Parallel
                     Works's
                     cluster? <#Can_I_transfer_files_with_external_object_storage_%5Baka_bucket_or_block_storage%5D_from_Parallel_Works's_cluster?>`__
                  -  `7.7 Azure: How to copy a file from the controller
                     node to the project's permanent
                     storage? <#Azure:_How_to_copy_a_file_from_the_controller_node_to_the_project's_permanent_storage?>`__
                  -  `7.8 How do I use GCP gsutil transfer files to a
                     project
                     bucket? <#How_do_I_use_GCP_gsutil_transfer_files_to_a_project_bucket?>`__
                  -  `7.9 How do I get nvhpc NVidia HPC compiler, and
                     netcdf, and hdf5 packages in my
                     environment? <#How_do_I_get_nvhpc_NVidia_HPC_compiler,_and_netcdf,_and_hdf5_packages_in_my_environment?>`__
                  -  `7.10 Which AWS Availability Zones [AZ] AMD and
                     Intel processors are concentrated [Answer to
                     InsufficientInstanceCapacity]? <#Which_AWS_Availability_Zones_%5BAZ%5D_AMD_and_Intel_processors_are_concentrated_%5BAnswer_to_InsufficientInstanceCapacity%5D?>`__
                  -  `7.11 What does GCP resource GVNIC and Tier_1 flags
                     represent? <#What_does_GCP_resource_GVNIC_and_Tier_1_flags_represent?>`__
                  -  `7.12 Why are all instance types are labeled as
                     AMD64? <#Why_are_all_instance_types_are_labeled_as_AMD64?>`__
                  -  `7.13 Data access via globus CLI tools in the
                     cloud <#Data_access_via_globus_CLI_tools_in_the_cloud>`__
                  -  `7.14 Container singularity replaced by
                     singularity-ce, and syntax remains the
                     same <#Container_singularity_replaced_by_singularity-ce,_and_syntax_remains_the_same>`__
                  -  `7.15 How to list the files in an s3 bucket using a
                     script? <#How_to_list_the_files_in_an_s3_bucket_using_a_script?>`__
                  -  `7.16 What is the best practice in hiding
                     credentials, when code is pushed in
                     Github? <#What_is_the_best_practice_in_hiding_credentials,_when_code_is_pushed_in_Github?>`__
                  -  `7.17 Where should I clone the GitHub
                     repository? <#Where_should_I_clone_the_GitHub_repository?>`__
                  -  `7.18 GCP Region/AZs on GPUs and
                     models <#GCP_Region/AZs_on_GPUs_and_models>`__
                  -  `7.19 What are the GPU models available on AWS,
                     Azure, and
                     GCP <#What_are_the_GPU_models_available_on_AWS,_Azure,_and_GCP>`__
                  -  `7.20 What are the Cloud regions supported by
                     Parallel
                     Works? <#What_are_the_Cloud_regions_supported_by_Parallel_Works?>`__
                  -  `7.21 X2go Passwordless authentication using
                     ssh-keys <#X2go_Passwordless_authentication_using_ssh-keys>`__
                  -  `7.22 How to tunnel back from a compute node to the
                     controller/head
                     node? <#How_to_tunnel_back_from_a_compute_node_to_the_controller/head_node?>`__
                  -  `7.23 On Azure, missing /apps fs system or modules
                     not loaded
                     case <#On_Azure,_missing_/apps_fs_system_or_modules_not_loaded_case>`__

            .. rubric:: General Cloud
               Issues[\ `edit </index.php?title=FAQ&action=edit&section=1>`__\ ]
               :name: general-cloud-issuesedit

            .. rubric:: How do I open a cloud help desk
               ticket?[\ `edit </index.php?title=FAQ&action=edit&section=2>`__\ ]
               :name: how-do-i-open-a-cloud-help-desk-ticketedit

            Send an email to rdhpcs.cloud.help@noaa.gov. Your email
            automatically generates a case in the OTRS system.

            The OTRS system does not have an option to set a priority
            level. Typically, your ticket is responded to within 2
            hours.

            .. rubric:: Where do I find instructions to connect the
               controller node from outside the
               network?[\ `edit </index.php?title=FAQ&action=edit&section=3>`__\ ]
               :name: where-do-i-find-instructions-to-connect-the-controller-node-from-outside-the-networkedit

            Refer the Parallel works user guide, section From outside
            the platform:-
            https://docs.parallel.works/interacting-with-clusters/logging-in-controller

            .. rubric:: What are the project allocation usage limits and
               actions?[\ `edit </index.php?title=FAQ&action=edit&section=4>`__\ ]
               :name: what-are-the-project-allocation-usage-limits-and-actionsedit

            **Used allocation at 85% of the budget allocation:**  When
            an existing project usage reaches 85% of the allocation, the
            Parallel Works [PW] platform sends an email message to
            principal investigator [PI], tech lead [TL] and admin
            staff.   

            -  Users can continue to start new clusters and continue the
               currently running clusters. 
            -  A warning message appears on the PW compute dashboard
               against the project.
            -  PI should work with the allocation committee on
               remediation efforts. 

            **Used allocation at 90% of the budget allocation: ** When
            an existing project usage reaches 90% of the allocation, the
            Parallel Works platform sends an email message to principal
            investigator, tech lead and admin staff.   

            -  Users can no longer start a new cluster and may continue
               the currently running clusters, but no new jobs can be
               started. 
            -  Users must move data from the contrib and object storage
               to on-premise storage. 
            -  A “Freeze” message appears on the PW compute dashboard
               against the project.
            -  PI should work with the allocation committee on
               remediation efforts. 

            **Used allocation at 95% of the budget allocation: ** When
            an existing project usage reaches 95% of the allocation, the
            Parallel Works platform sends an email message to principal
            investigator, tech lead and admin staff.   

            -  Terminate and remove all computing/cluster resources.
            -  Data at buckets will remain available as will data in
               /contrib. However, only data in the object storage will
               be directly available to users.
            -  Notify all affected users, PI, Tech Lead, Accounting Lead
               via email that all resources have been removed.
            -  Disable the project. 

            **Used allocation at 99.5% of the budget allocation:** 

            -  Manually remove the project resources. 
            -  Notify COR/ACORS, PI and Tech Lead, Accounting Lead via
               email all resources have been removed.

            .. rubric:: How do I get a project allocation or an
               allocation
               increase?[\ `edit </index.php?title=FAQ&action=edit&section=5>`__\ ]
               :name: how-do-i-get-a-project-allocation-or-an-allocation-increaseedit

            RDHPCS System compute allocations are decided upon by the
            RDHPCS Allocation Committee (AC), with oversight from the
            NOAA HPC Board. The information for allocation is contained
            on the RHPCS common docs wiki:

            https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Allocations_and_Quotas#Request_an_Increase_in_Allocations

            Update the the Allocation Request Form located under the
            section "Allocations" from the above link.

            .. rubric:: Storage
               functionalities[\ `edit </index.php?title=FAQ&action=edit&section=6>`__\ ]
               :name: storage-functionalitiesedit

            **Cluster runtime notification**

            A cluster owner can set up to send an email notification
            based on the number of hours/days a cluster is up. You can
            enable the notification from the Parallel Works resource
            configuration page and apply it on a live cluster or set as
            a standard setting on a resource configuration, so that will
            take effect on clusters started using the configuration.

            **Mounting permanent storage on a cluster**

            Your project’s permanent storage [AWS s3 bucket, Azure’s
            Block blob storage, or GCP’s bucket] can be mounted on an
            active cluster, or set to attach a bucket when starting a
            cluster, as a standard setting on a resource configuration.
            Having the permanent storage mounted on a cluster allows a
            user to copy files from contrib or lustre to a permanent
            storage using familiar Linux commands.

            **Sharing storage between the projects, enhanced capacity,
            and configuration**

            Note that the permanent storage and persistent storage must
            be started separately before it can be attached to a
            cluster. Storage resources can be started from the Compute
            dashboard, Storage Resources section.

            If you are a user belonging to more than one project, now
            you can share storage between the projects. You can attach
            other project storage from the resource configuration page.
            Note that, a persistent lustre file system must be started
            separately before it can be attached to a cluster.

            Users may create as many permanent object storage [AWS S3
            bucket, Azure’s block blob storage, and GCP’s bucket], and
            lustre file system [ephemeral and persistent storage] on
            your Cloud platform.

            .. rubric:: How do I resize the root
               disk?[\ `edit </index.php?title=FAQ&action=edit&section=7>`__\ ]
               :name: how-do-i-resize-the-root-diskedit

            Open up the resource name definition, click on the \_JSON
            tab, add a parameter "root_size" with a value in the
            cluster_config section, that fits your need, save and
            restart the cluster.

            In the below example, the root disk size is set to 256 GiB

            "cluster_config": {

            ::

               ..

            ::

               ..

            ::

                  "root_size": "256",

            ::

               ..

            .. rubric:: Where do I get detailed Workflow
               instructions?[\ `edit </index.php?title=FAQ&action=edit&section=8>`__\ ]
               :name: where-do-i-get-detailed-workflow-instructionsedit

            If you're running a workflow for the first time, you will
            need to add it to your account first. From the Parallel
            Works main page, click the workflow marketplace button
            located on the top right menu bar, looks like an Earth icon.

            Refer the link below to learn on the workflow

            https://docs.google.com/document/d/1o2jY2IDuqVbkN3RIDXSMaic5ofi9glJSzlAPsEArhqk/edit?usp=sharing

            .. rubric:: What are the different storage types and costs
               available on the PW
               platform?[\ `edit </index.php?title=FAQ&action=edit&section=9>`__\ ]
               :name: what-are-the-different-storage-types-and-costs-available-on-the-pw-platformedit

            There are three types of storage available on a cluster,
            those are lustre, object storage [ for backup & restore,
            output files], and contrib file system [a project's custom
            software library].

            **Lustre file system**

            Parallel file system, available as ephemeral, and persistent
            storage on the AWS, Azure, and GCP cloud platforms. You can
            create as many lustre file systems as you want from the PW
            Storage tab by selecting the “add storage” button.

            | 
            | Refer the user guide section on adding storage link :
              https://docs.parallel.works/managing-storage/creating-storage

            | 
            | Cost for lustre storage can be found at the definition
              page when creating storage.

            | 
            | Lustre file system can be attached and mounted on a
              cluster. It is accessible only from an active cluster.

            | 
            | **Bucket/Block blob storage**

            | 
            | A bucket or Block blob storage is a container for objects.
              An object is a file and any metadata that describes that
              file.

            | 
            | Use cases, such as data lakes, websites, mobile
              applications, backup and restore, archive, enterprise
              applications, IoT devices, and big data analytics.

            | 
            | On AWS, and GCP, the storage is called S3 bucket, and
              bucket respectively, whereas in Azure, the storage used is
              Block blob storage, which functions as a bucket and an NFS
              storage.

            | 
            | AWS S3 bucket pricing [us-east-1]: $0.021 per GB per
              Month. The cost is calculated based on the storage usage.
              For example, 1 PB storage/month will cost $21,000.

            | 
            | Pricing refer: https://aws.amazon.com/s3/pricing/

            | 
            | Azure object storage and contrib file system are the
              storage type. The pricing for the first 50 terabyte (TB) /
              month is $0.15 per GB per Month. The cost is calculated
              based on the storage usage. See: Azure Pricing

            | 
            | Google cloud bucket storage pricing: Standard storage
              cost: $0.20 per GB per Month. The cost is calculated based
              on the storage usage. See: Cloud Bucket pricing

            | 
            | Projects using AWS, and GCP platforms can create as many
              buckets as needed, and mount on a cluster. Project’s
              default bucket is accessible from the public domain using
              the keys.

            | 
            | **Contrib file system**

            Contrib file system concept is similar to on-prem contrib,
            used to store files for team collaboration. This storage can
            be used to install custom libraries or user scripts.

            | 
            | AWS Contrib storage [efs] pricing [us-east-1]: $0.30 per
              GB per Month. The cost is calculated based on the storage
              usage. See: AWS Pricing

            Azure contrib cost is explained above in the block blob
            storage section.

            Both AWS and Azure charge based on the usage, as a
            pay-as-you-go model like your electricity bill. GCP charges
            on allocated storage, so whether the storage is used or not,
            the project will pay for the provisioned capacity.

            The default provisioned capacity of Google Cloud contrib
            file system is 2.5 TiB, costs $768.00 per month. The contrib
            volume can be removed from a project by request, email to
            rdhpcs.cloud.help@noaa.gov [ OTRS ticket on RDHPCS help.]

            | 
            | **Reference on data egress charges:**

            AWS

            Traffic between regions will typically have a $0.09 per GB
            charge for the egress of both the source and destination.
            Traffic between services in the same region is charged at
            $0.01 per GB for all four flows.

            AWS's monthly data transfer costs for outbound data to the
            public internet are $0.09 per GB for the first 10 TB,
            dropping to $0.085 per GB for the next 40 GB, $0.07 per GB
            for the next 100 TB, and $. 05/GB greater than 150 TB.

            Azure:

            https://azure.microsoft.com/en-us/pricing/details/bandwidth/

            GCP:

            https://cloud.google.com/network-tiers/pricing

            .. rubric:: Parallel
               Works[\ `edit </index.php?title=FAQ&action=edit&section=10>`__\ ]
               :name: parallel-worksedit

            .. rubric:: Where do I find the Parallel Works User
               Guide?[\ `edit </index.php?title=FAQ&action=edit&section=11>`__\ ]
               :name: where-do-i-find-the-parallel-works-user-guideedit

            The link to the user guide below:-
            https://docs.parallel.works/

            .. rubric:: How do I get access to the Parallel Works
               Platform?[\ `edit </index.php?title=FAQ&action=edit&section=12>`__\ ]
               :name: how-do-i-get-access-to-the-parallel-works-platformedit

            Pre-requisite for getting an account access to the Parallel
            Works platform is to have a NOAA email address.

            The next step is to request access to a project and RSA
            token from the “Account Management Home”.

            Use the URL AIM: https://aim.rdhpcs.noaa.gov/ to request for
            a project and RSA token. No CAC is necessary to access the
            Parallel Works platform.

            From the Account Management Home, click the link: “Click
            here to Request Access to a Project” and select a project
            the list of projects.

            The drop-down list is long. You can type the first character
            to move the cursor towards your project name.

            The nomenclature on cloud project names are, AWS projects
            start with letters “ca-“, Azure projects start with letters
            “cz-“, and GCP projects with “cg-”

            Example cloud project names are: ca-budget-test: This is the
            AWS platform project used for cost specific tests.
            cz-budget-test: This is the Azure platform project used for
            cost specific tests. cg-budget-test: This is the GCP
            platform project used for cost specific tests.

            After selecting the project, click the “Submit Request”
            button.

            Click the link: “Make a request for an RSA token”

            After your request is approved, you can login on to the
            platform: https://noaa.parallel.works/

            .. rubric:: How is a new user added to a project on the
               Parallel
               Works?[\ `edit </index.php?title=FAQ&action=edit&section=13>`__\ ]
               :name: how-is-a-new-user-added-to-a-project-on-the-parallel-worksedit

            If you would like to join an existing project, ask your PI,
            TL, or Portfolio manager the project name. The cloud project
            name starts like ca, cz, or cg implying AWS, Azure, or
            Google platform, and followed by the project name. An
            example, ca-budget-test implies that project budget-test
            runs from the AWS platform.

            Use the AIM link https://aim.rdhpcs.noaa.gov/ and click on
            the link "Request new access to a project" to add yourself
            to a project.

            Access to the project is contingent on PI's approval.

            .. rubric:: How do I set up a new project in the Parallel
               Works
               Platform?[\ `edit </index.php?title=FAQ&action=edit&section=14>`__\ ]
               :name: how-do-i-set-up-a-new-project-in-the-parallel-works-platformedit

            To set up your project setup in Parallel Works follow the
            below steps.

            | 
            | [1] Get your project’s allocation approved by NOAA RDHPCS
              allocation committee.

            If you are unsure of an allocation amount for your project,
            create a cloud help desk ticket by emailing to
            rdhpcs.cloud.help@noaa.gov to schedule a meeting. An SME can
            help you translate your business case into an allocation
            estimate.

            Email to POC for allocation approval: Gonzalo Lassally,
            NOAA.

            Follow the link to update allocation form.

            | 
            | https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#How_do_I_get_a_project_allocation_or_an_allocation_increase.3F

            | 

            | 
            | [2] Send an email to the AIM administrator to create your
              project.

            A Portfolio Manager or Principal Investigator can send an
            email to AIM administrator rdhpcs.aim.help@noaa.gov with a
            request to create a project by providing the following
            information:

            [a] Project short name. Please provide in this format:
            <cloud platform abbreviation>-<project name>

            Example ca-epic stands for AWS Epic, cz-epic for Azure epic,
            and cg-epic for Google cloud Epic.

            [b] Brief description of your project.

            | 
            | [c] Portfolio name.

            | 
            | [d] Principal Investigator [PI] name.

            | 
            | [e] Technical lead name [TL]. In some case, a project's PI
              and TL may be the same person. If that is the case, repeat
              the name.

            | 
            | [f] Allocation amount.

            | 
            | Setting up a project in AIM can take a day.

            [3] AIM system administrator creates a cloud help desk
            ticket to create a project on the Parallel Works platform.

            Setting up a project in Parallel Works can take a day. Upon
            the project creation, the AIM administrator will email to PI
            informing the project status.

            Read the cloud FAQ to learn on adding users to a project.

            .. rubric:: What is the certified browser for Parallel Works
               Platform?[\ `edit </index.php?title=FAQ&action=edit&section=15>`__\ ]
               :name: what-is-the-certified-browser-for-parallel-works-platformedit

            Google Chrome browser.

            .. rubric:: Cost
               Calculator[\ `edit </index.php?title=FAQ&action=edit&section=16>`__\ ]
               :name: cost-calculatoredit

            You can estimate an hourly cost of your experiment’s from
            the Parallel Works(PW) platform. After login on the
            platform, click on the “Resources” tab, and double click on
            your resource definition. There is a definition tab, where
            when you update the required compute and lustre file system
            size configuration, the form dynamically shows an hourly
            estimate.

            | 
            | You can derive an estimated cost of a single experiment by
              multiplying the run time with the hourly cost.

            | 
            | For example, if the hourly estimate is $10, and your
              experiment would run for 2 hours then the estimated cost
              for your experiment would be $10 multiplied by 2, equals
              to $20.

            | 
            | You can derive project allocation cost by multiplying the
              run time cost with the number of runs required to complete
              the project.

            | 
            | For example, if your project would require a model run 100
              times, then multiply that number by a single run cost, the
              cost would be 100x$20 = $2,000.00.

            | 
            | Note that there are costs associated with maintaining your
              project, like contrib file system, object storage to store
              backup, and egress. Use the link below to find the
              `cost <https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#What_are_the_different_storage_types_and_costs_available_on_the_PW_platform.3F>`__.

            | 
            | https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#What_are_the_different_storage_types_and_costs_available_on_the_PW_platform.3F

            .. rubric:: Cost dashboard
               explained[\ `edit </index.php?title=FAQ&action=edit&section=17>`__\ ]
               :name: cost-dashboard-explainededit

            Refer the user guide link:
            https://parallelworks.com/docs/monitoring-costs

            .. rubric:: How do I find a real time cost estimate of my
               session?[\ `edit </index.php?title=FAQ&action=edit&section=18>`__\ ]
               :name: how-do-i-find-a-real-time-cost-estimate-of-my-sessionedit

            Cloud vendors publish the cost once every 24 hours, that is
            not an adequate measure in an HPC environment. PW Cost
            dashboard offers an almost real time estimate of your
            session.

            Real time estimate is refreshed every 5 minutes on the Cost
            dashboard. Click on the Cost link from your PW landing page.
            Under the “Time Filter”, choose the second drop down box and
            select the value “RT” [Real time]. Make sure the “User
            Filter” section has your name. The page automatically
            refreshes with the cost details.

            .. rubric:: How do I estimate
               core-hours?[\ `edit </index.php?title=FAQ&action=edit&section=19>`__\ ]
               :name: how-do-i-estimate-core-hoursedit

            An example, your project requests a dedicated number of HPC
            compute nodes or has an HPC system reservation for some
            number of HPC compute nodes. Let’s say that the
            dedicated/reserved nodes have 200 cores and the length of
            the dedication/reservation is 1 week (7 days), then the
            core-hours used would be 33,600 core-hours (200 cores \* 24
            hrs/day \* 7 days).

            GCP's GPU to vCPUs conversation can be found here:
            https://cloud.google.com/compute/docs/gpus In GCP, two vCPUs
            makes one physical core.

            So, a2-highgpu-1 has 12 vCPUs that means 6 physical core. If
            your job is taking 4 hours to complete so that means the
            number of core hours = number of nodes x number of hour x
            number of cores = 1 x 4 x 6 = 24 core hours.

            PW’s cost dashboard is a good tool to find unit cost, and
            extrapolate it to estimate usage for PoP.

            https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#How_do_I_find_a_real_time_cost_estimate_of_my_session.3F

            | 

            .. rubric:: How to access the head node from the Parallel
               Works [PW] web
               interface?[\ `edit </index.php?title=FAQ&action=edit&section=20>`__\ ]
               :name: how-to-access-the-head-node-from-the-parallel-works-pw-web-interfaceedit

            You can connect to the head node from the PW portal, or
            Xterm window if you have added your public key in the
            resource definition prior to launching a cluster.

            If you have not added a public key at the time of launching
            a cluster, you can login to the head node by IDE and update
            the public key in ~/.ssh/authorized_keys file.

            [1] From the PW “Compute” dashboard, click on your name with
            an IP address and make a note of it. You can also get the
            head node IP address by clicking ‘i” icon of the Resource
            monitor.

            [2] Click on the IDE link located on the top right side of
            the PW interface to launch a new terminal.

            [3] From the menu option “Terminal”, click on the “New
            Terminal” link.

            [4] From the new terminal, type

            $ ssh <Paste the username with IP address> and press the
            enter key.

            This will let you login to the head node from the PW
            interface.

            Example:

            First.Lastname@pw-user-firstlastname:/pw$ ssh
            First.Last@54.174.136.76

            Warning: Permanently added '54.174.136.76' (ECDSA) to the
            list of known hosts.

            You can use the toggle button to restore lustre file system
            setting. You can also resize the LFS at a chunk size
            multiple of 2.8 TB.

            Note that LFS is an expensive storage.

            .. rubric:: How do I add a workflow to my
               account?[\ `edit </index.php?title=FAQ&action=edit&section=21>`__\ ]
               :name: how-do-i-add-a-workflow-to-my-accountedit

            If you're running a workflow for the first time, you will
            need to add it to your account first. From the PW main page,
            click the workflow marketplace button on the top menu bar.
            This button should be on the right side of the screen, and
            looks like an Earth icon.

            How do I ssh to other nodes in my cluster?

            It is possible to ssh to compute nodes in your cluster from
            the head node by using the node's hostname. You do not
            necessarily need to have a job running on the node, but it
            does need to be in a powered on state (most resource
            configurations suspend compute nodes after a period of
            inactivity)

            #. Use \`sinfo\` or \`squeue\` to view active nodes:

            [Matt.Long@awsnoaa-4 Matt.Long]$ sinfo PARTITION AVAIL
            TIMELIMIT NODES STATE NODELIST compute\* up infinite 4 idle~
            compute-dy-c5n18xlarge-[2-5] compute\* up infinite 1 mix
            compute-dy-c5n18xlarge-1

            [Matt.Long@awsnoaa-4 Matt.Long]$ squeue

            ::

                           JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
                               2   compute     bash Matt.Lon  R       0:33      1 compute-dy-c5n18xlarge-1 

            #. ssh to the compute node

            [Matt.Long@awsnoaa-4 Matt.Long]$ ssh
            compute-dy-c5n18xlarge-1 [Matt.Long@compute-dy-c5n18xlarge-1
            ~]$

            .. rubric:: How do I request a new feature or report
               feedback?[\ `edit </index.php?title=FAQ&action=edit&section=22>`__\ ]
               :name: how-do-i-request-a-new-feature-or-report-feedbackedit

            You may request a new feature on the PW platform or provide
            a feedback to the NOAA RDHPCS leadership using the link:
            https://forms.gle/FGkdQoCUkAGm63mc7

            .. rubric:: How to address an authentication issue on the
               Parallel Works [PW]
               login?[\ `edit </index.php?title=FAQ&action=edit&section=23>`__\ ]
               :name: how-to-address-an-authentication-issue-on-the-parallel-works-pw-loginedit

            Authentication to the PW system can be due to an expired RSA
            Token or inconsistent account status in the PW system. If
            you have not accessed on-prem HPC system last 30 days, it is
            likely your RSA token is expired, in such cases contact
            rdhpcs.aim.help@noaa.gov for assistance.

            To verify RSA Token issue, follow the steps:

            Remember that userIDs are case sensitive, and most usernames
            are First.Last and not first.last)! Re-enter your userID in
            this format as a first step.

            If you enter an incorrect username or PIN and token value
            three times during a login attempt, your account will
            automatically lock for fifteen minutes. This is a fairly
            common occurrence. Wait for 15 minutes and resync as
            follows:

            • Use ssh to login to one of the hosts such as one of
            Hera/Niagara/Jet, using your RSA Token.

            • After the host authenticates once, it will ask you wait
            for the token to change. Enter your PIN + RSA token again
            after the token has changed.

            • After a successful login your token will be resynched and
            you should be able to proceed.

            | 
            | If you are still experiencing issues with your token, send
              a help request to rdhpcs.aim.help@noaa.gov with the title
              "Please check RSA token status." To expedite
              troubleshooting, please include the full terminal output
              you received when you tried to use your token.

            If RSA token is working and still unable to login to the PW
            system, open a ticket by emailing to
            rdhpcs.cloud.help@noaa.gov.

            On the PW login site, after entering your username is not
            navigating to two-factor authentication box or taking too
            long, it could be an issue with your VPN. In that case,
            disconnect the VPN and try login. If the login succeeds, it
            implies an issue with the VPN.

            .. rubric:: Clusters and
               Snapshots[\ `edit </index.php?title=FAQ&action=edit&section=24>`__\ ]
               :name: clusters-and-snapshotsedit

            .. rubric:: Cluster Cost types
               explained.[\ `edit </index.php?title=FAQ&action=edit&section=25>`__\ ]
               :name: cluster-cost-types-explained.edit

            There are several resource types that are part of a user
            cluster.

            We are working on adding more clarity on the resource cost
            type naming and cost. Broadley, the following cost types are
            explained below.

            UnknownUsageType: Network cost related virtual private
            network. Additional reading,
            https://cloud.google.com/vpc/network-pricing,
            https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/

            Other Node : Controller node cost.

            Storage-BASIC_SSD  : On the Google cloud, “contrib” volume
            billing is based on the allocated storage. Contrib volume
            allocated storage 2.5TB. On other cloud platforms, the cost
            is based on the storage used.

            Storage-Disk : Boot disk and apps volume disk cost.

            .. rubric:: How do I resize my resource cluster
               size?[\ `edit </index.php?title=FAQ&action=edit&section=26>`__\ ]
               :name: how-do-i-resize-my-resource-cluster-sizeedit

            The default CSP resource definition in the platform is
            fv3gfs model at 768 resolution 48-hours best performance
            optimized benchmark configuration.

            From the PW platform top ribbon, click on the “Resources”
            link.

            Click on the edit button of a PW v2 cluster [aka elastic
            clusters, CSP slurm] resource definition.

            By default, there are two partitions, “Compute” and “batch”
            as you can see on the page. You can change the number of
            partitions based on your workflow.

            From the resource definition page, navigate to the compute
            partition.

            Max Node Amount parameter is the maximum number of nodes in
            a partition. You can change that value to a non-zero number
            to resize the compute partition size.

            You may remove the batch partition by clicking on the
            “Remove Partition” button. You can also edit the value for
            Max Node Count parameter to resize this partition.

            Lustre filesystem is an expensive resource. You can disable
            the filesystem or resize it. The default lustre filesystem
            size is about 14TiB.

            .. rubric:: How do I create a custom snapshot [a.k.a AMI,
               Snapshot, Boot disk, or machine
               image]?[\ `edit </index.php?title=FAQ&action=edit&section=27>`__\ ]
               :name: how-do-i-create-a-custom-snapshot-a.k.a-ami-snapshot-boot-disk-or-machine-imageedit

            If a user finds specific packages are not present in the
            base boot image, the user can add it by creating own custom
            image. Follow the steps to create a custom snapshot.

            Refer the user guide to learn on `creating a
            snapshot <https://docs.parallel.works/cloud-snapshots/>`__

            After a snapshot is created, the next step is to reference
            it in the cluster Resource configuration.

            From the Parallel Works banner, click on the “Compute” tab,
            and double click on the resource link to edit it.

            From the Resource Definition page, look for the “Controller
            Image” name. Select your newly created custom snapshot name
            from the drop down list box.

            Scroll down the page to the partition section. Change the
            value of "Elastic Image" to your custom image. If you have
            more than one partitions, then change "Elastic Image" value
            to your custom image name.

            Click on the “Save Resource” button located on the top right
            of the page.

            Now launch a new cluster using the custom snapshot from the
            “Compute” page. After the cluster is up, verify the
            existence of custom installed packages.

            .. rubric:: How to automatically find the hostname of a
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=28>`__\ ]
               :name: how-to-automatically-find-the-hostname-of-a-clusteredit

            By default, the host names are always going to be different
            each time you start a cluster.

            You can find CSP information as below: $ echo $PW_CSP google

            There's a few other "PW" vars that might be useful for you
            as well: PW_PLATFORM_HOST,

            PW_POOL_ID,

            PW_POOL_NAME,

            PWD,

            PW_SESSION_ID,

            PW_SESSION,

            PW_USER,

            PW_GROUP,

            PW_SESSION_LONG,

            PW_CSP

            .. rubric:: How do I setup an ssh tunnel to my
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=29>`__\ ]
               :name: how-do-i-setup-an-ssh-tunnel-to-my-clusteredit

            ssh tunnels are a useful way to connect to services running
            on the head node when they aren't exposed to the internet.
            The Jupyterlab and R workflows available on the PW platform
            utilize ssh tunnels to allow you to connect to their
            respective web services from your local machine's web
            browser.

            Before setting up an ssh tunnel, it is probably a good idea
            to verify standard ssh connectivity to your cluster (see how
            do I connect to my cluster). Once connectivity has been
            verified, an ssh tunnel can be setup like so:

            Option 1: ssh CLI

            ::

                $ ssh -N -L <Local Port>:<Remote Host>:<Remote Port> <Remote User>@<Remote Host>

            ex:

            ::

                $ ssh -N -L 8888:mattlong-gclustera2highgpu1g-00012-controller:8888 matt.Long@34.134.251.102

            In this example, I am tunneling port 8888 from the host
            'mattlong-gclustera2highgpu1g-00012-controller' to port 8888
            on my local machine. This lets me direct my browser to the
            URL 'localhost:8888' and see the page being served by the
            remote machine over that port.

            .. rubric:: How do I turn off Lustre filesystem from the
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=30>`__\ ]
               :name: how-do-i-turn-off-lustre-filesystem-from-the-clusteredit

            From the Resources tab, select a configuration and click the
            edit link.

            Scroll down the configuration page to the "Lustre file
            system" section. Use the toggle button to "No" to turn off
            the lustre file system [LFS]. This setting lets you create a
            cluster without a lustre file system.

            .. rubric:: How do I activate conda at cluster
               login?[\ `edit </index.php?title=FAQ&action=edit&section=31>`__\ ]
               :name: how-do-i-activate-conda-at-cluster-loginedit

            Running conda init bash will setup the ~/.bashrc file so it
            will activate the default environment when you login.

            If you want to use a different env than what is loaded by
            default, you could run this to change the activation:

            echo "conda activate <name of env>" >> ~/.bashrc

            Since your .bashrc shouldn't really change much, it might be
            ideal to set the file up once and then back it up to your
            contrib (somewhere like
            /contrib/Nastassia.Patin/home/.bashrc), then your user boot
            script could simply do:

            cp /contrib/Nastassia.Patin/home/.bashrc ~/.bashrc

            or

            ln -s /contrib/Nastassia.Patin/home/.bashrc ~/.bashrc

            .. rubric:: How do I create a resource
               configuration?[\ `edit </index.php?title=FAQ&action=edit&section=32>`__\ ]
               :name: how-do-i-create-a-resource-configurationedit

            If your cluster requires lustre file system [ephemeral or
            persistent], or additional storage for backup, start at the
            "Storage" section and then use the "Resource" section.

            Managing the Storage:

            https://docs.parallel.works/managing-storage/

            Create a cluster configuration:

            https://docs.parallel.works/interacting-with-clusters/configuring-clusters

            .. rubric:: How do I enable run time alerts on my
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=33>`__\ ]
               :name: how-do-i-enable-run-time-alerts-on-my-clusteredit

            You can enable this functionality on your active or new
            cluster. This setup will help you send a reminder when your
            cluster is up a predefined number of hours.

            You can turn on this functionality when creating a new
            resource name. When you click on the “add resource” button
            under the “Resource”, you find the run time alert option.

            You can enable this functionality on a running cluster, by
            navigating to the “properties” tab of your resource name
            under the “Resource” tab.

            Reference:
            https://docs.parallel.works/interacting-with-clusters/creating-clusters

            .. rubric:: Missing user directory in the group's contrib
               volume.[\ `edit </index.php?title=FAQ&action=edit&section=34>`__\ ]
               :name: missing-user-directory-in-the-groups-contrib-volume.edit

            A user directory on a group's contrib volume can only be
            created by an owner of a cluster, as the cluster owner only
            has "su" access privilege. Follow the steps to create a
            directory on contrib.

            [1] Start a cluster. Only the owner has the sudo su
            privilege to create a directory on contrib volume.

            [2] Start a cluster, login to the controller node, and
            create your directory on the contrib volume.

            Start a cluster by clicking on the start/stop button

            When your cluster is up, it shows your name with an IP
            address. Click on this link that copies username and IP
            address to the clipboard.

            Click on the IDE button located top right on the ribbon.

            Click on the ‘Terminal’ link and select a ‘New Terminal’

            SSH into the controller node by pasting the login
            information from the clipboard.

            $ ssh User.Name<IP address>

            | 

            List your user name and group:

            $ id

            [Unni.Kirandumkara@awsv22-50 contrib]$ id

            uid=20674(Unni.Kirandumkara) gid=9001(pwuser)
            groups=9001(pwuser)
            context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

            $ sudo su -

            [root@awsv22-50 ~]$

            [root@awsv22-50 ~]$ cd /contrib

            [root@awsv22-50 contrib]$

            [root@awsv22-50 contrib]$mkdir <user name as appeared above>

            Example:

            [root@awsv22-50 contrib]$ mkdir Unni.Kirandumkara

            [root@awsv22-50 contrib]$ chown username:group directory

            [root@awsv22-50 contrib]$ chown Unni.Kirandumkara:pwuser
            Unni.Kirandumkara

            [root@awsv22-50 contrib]$ ls -l

            drwxr-xr-x. 2 Unni.Kirandumkara pwuser 6 May 12 13:06
            Unni.Kirandumkara

            [root@awsv22-50 contrib]$ exit

            logout

            [Unni.Kirandumkara@awsv22-50$cd /contrib

            [Unni.Kirandumkara@awsv22-50 contrib]$

            | 
            | Your directory with access permission is now complete.

            Your directory is now accessible from your group’s clusters.
            Contrib is a permanent storage for your group.

            You may shutdown the cluster if the purpose was to create
            your contrib directory.

            .. rubric:: Why does the owner's home directory look
               different from the shared users’ home
               directory?[\ `edit </index.php?title=FAQ&action=edit&section=35>`__\ ]
               :name: why-does-the-owners-home-directory-look-different-from-the-shared-users-home-directoryedit

            Every cluster is set up where the owner of it has an
            ephemeral home directory that isn't linked from contrib, but
            on multi-user clusters, all additional users that are added
            do get home linked from contrib.

            The projects using Google cloud can request to drop their
            contrib volume to save cost. Google charges on provisioned
            nfs capacity, whereas others charge on the used storage.

            So when people start clusters in some cases they may not
            have a contrib dir so owners don't want to link home
            directory to their contrib directory.

            .. rubric:: What are “Compute” and “Batch” sections in a
               cluster
               definition?[\ `edit </index.php?title=FAQ&action=edit&section=36>`__\ ]
               :name: what-are-compute-and-batch-sections-in-a-cluster-definitionedit

            The sections “Compute” and “Batch” are partitions. You may
            change the partition name at the name field to fit your
            naming convention. The cluster can have many partitions with
            different images and instance types, and can be manipulated
            at the “Code” tab.

            You may resize the partitions by updating "max_node_num", or
            remove batch partition to fit your model requirements.

            Default Partition details.

            PartitionName=compute
            Nodes=mattlong-azv2-00115-1-[0001-0096] MaxTime=INFINITE
            State=UP Default=YES OverSubscribe=NO

            PartitionName=batch Nodes=mattlong-azv2-00115-2-[0001-0013]
            MaxTime=INFINITE State=UP Default=NO OverSubscribe=NO

            .. rubric:: How do I manually shutdown the compute
               nodes?[\ `edit </index.php?title=FAQ&action=edit&section=37>`__\ ]
               :name: how-do-i-manually-shutdown-the-compute-nodesedit

            $ sinfo PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
            compute\* up infinite 144 idle~
            mattlong-gcp-00141-1-[0001-0144] batch up infinite 8 idle~
            mattlong-gcp-00141-2-[0003-0010] batch up infinite 2 idle
            mattlong-gcp-00141-2-[0001-0002]

            | 
            | In this case, there are two nodes that are on and idle
              (mattlong-gcp-00141-2-[0001-0002]) You can ignore the
              nodes with a ~ next to their state. That means they are
              currently powered off.

            | 
            | You can then use that list to stop the nodes:

            | 
            | $ sudo scontrol update
              nodename=mattlong-gcp-00141-2-[0001-0002] state=power_down

            .. rubric:: How to sudo in as root or a role account on a
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=38>`__\ ]
               :name: how-to-sudo-in-as-root-or-a-role-account-on-a-clusteredit

            The owner of a cluster can sudo in as root and grant sudo
            privilege to the project members by adding their user id in
            the sudoers file.

            Only the named cluster owner can become root. If the cluster
            owner is currently su'd as another user, they will need to
            switch back to their regular account before becoming root.

            Sudoers file is: ls -l /etc/sudoers

            Other project members' user id can be found at /etc/passwd
            file. You may update this file manually or by bootstrap
            script, the change is taken effect immediately.

            Example:

            echo "Unni.Kirandumkara ALL=(ALL) NOPASSWD:ALL" \| sudo tee
            /etc/sudoers.d/100-Unni.Kirandumkara

            Assuming the cluster setup as multi-user in the resource
            definition, and in the sharing tab, view and edit button are
            selected.

            .. rubric:: How to enable a role
               account?[\ `edit </index.php?title=FAQ&action=edit&section=39>`__\ ]
               :name: how-to-enable-a-role-accountedit

            A role account is a shared workspace for project members on
            a cluster. By su'd to a role account, project members can
            manage and monitor their jobs.

            There are two settings that must be enabled prior on a
            resource definition in order to create a role account in a
            cluster. On the resource definition page, select the "Multi
            User" tab to "Yes", and from the "Sharing" tab, check the
            "View and Edit" button.

            The command to find the name of your project's role account
            from /etc/passwd is.

            $ grep -i role /etc/passwd

            .. rubric:: Bootstrap script
               example[\ `edit </index.php?title=FAQ&action=edit&section=40>`__\ ]
               :name: bootstrap-script-exampleedit

            By default bootstrap script changes only runs on the MASTER
            node of a cluster.

            To run on all nodes (master and compute) have your user
            script first line be ALLNODES.

            The following example script installs a few packages, and
            reset the dwell time from 5 minutes to an hour on the
            controller and compute nodes. Do not add any comments on the
            bootstrap script, as that would cause in code execution
            failure.

            ALLNODES

            | 
            | set +x set -e

            | 
            | echo "Starting User Bootstrap at $(date)"

            | 
            | sudo rm -fr /var/cache/yum/\*

            | 
            | sudo yum clean all

            | 
            | sudo yum groups mark install "Development Tools" -y sudo
              yum groupinstall -y "Development Tools"

            | 
            | sudo yum --setopt=tsflags='nodocs'
              --setopt=override_install_langs=en_US.utf8 --skip-broken
              install -y awscli bison-devel byacc bzip2-devel
              ca-certificates csh curl doxygen emacs expat-devel file
              flex git gitflow git-lfs glibc-utils gnupg gtk2-devel ksh
              less libcurl-devel libX11-devel libxml2-devel lynx
              lz4-devel kernel-devel make man-db nano ncurses-devel
              nedit openssh-clients openssh-server openssl-devel pango
              pkgconfig python python3 python-devel python3-devel
              python2-asn1crypto pycairo-devel pygobject2
              pygobject2-codegen python-boto3 python-botocore
              pygtksourceview-devel pygtk2-devel pygtksourceview-devel
              python2-netcdf4 python2-numpy python36-numpy
              python2-pyyaml pyOpenSSL python36-pyOpenSSL PyYAML
              python-requests python36-requests python-s3transfer
              python2-s3transfer scipy python36-scipy python-urllib3
              python36-urllib3 redhat-lsb-core python3-pycurl screen
              snappy-devel squashfs-tools swig tcl tcsh texinfo
              texline-latex\* tk unzip vim wget

            | 
            | echo "USER=${USER}" echo "group=$(id -gn)" echo
              "groups=$(id -Gn)"

            | 

            | 
            | sudo sed -i 's/SuspendTime=300/SuspendTime=3600/g'
              /mnt/shared/etc/slurm/slurm.conf if `$HOSTNAME ==
              mgmt\* </index.php?title=$HOSTNAME_%3D%3D_mgmt*&action=edit&redlink=1>`__
              ; then

            ::

                sudo scontrol reconfigure 

            fi

            | 

            sudo sacctmgr add cluster cluseter -i sudo systemctl restart
            slurmdbd sudo scontrol reconfig

            | 
            | echo "Finished User Bootstrap at $(date)"

            | 

            .. rubric:: Configuration
               Questions[\ `edit </index.php?title=FAQ&action=edit&section=41>`__\ ]
               :name: configuration-questionsedit

            .. rubric:: How do I create Parallel Works resource
               configuration on my
               account?[\ `edit </index.php?title=FAQ&action=edit&section=42>`__\ ]
               :name: how-do-i-create-parallel-works-resource-configuration-on-my-accountedit

            Follow the instructions on this link:

            https://docs.google.com/presentation/d/1gITqB-uaJTF8GupYg3bxX_h5JvpNZYEBK3IV5bUHekU/edit#slide=id.g11424a5fc64_0_29

            .. rubric:: How do I get AMD processor resources
               configuration?[\ `edit </index.php?title=FAQ&action=edit&section=43>`__\ ]
               :name: how-do-i-get-amd-processor-resources-configurationedit

            AMD processor based instances or VMs are relatively less
            expensive than Intel. Cloud services providers have
            allocated processor quota on the availability zones where
            AMD processors are concentrated. In Parallel Works, the AMD
            configurations are created pointing to these availability
            zones.

            To create an AMD resource configuration, follow the steps
            explained in the link below. The instructions will direct
            you to restore configuration, then choose the AMD Config
            option from the list.

            https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#How_do_I_create_Parallel_Works_version_2_resource_configuration_on_my_account.3F

            You may resize the cluster size by adjusting max node count,
            and enable or disable lustre as appropriate to your model.

            .. rubric:: How do I restore a default
               configuration?[\ `edit </index.php?title=FAQ&action=edit&section=44>`__\ ]
               :name: how-do-i-restore-a-default-configurationedit

            You can restore a configuration by navigating to the
            “Resources” tab, double click on a resource name, shows up
            it’s “Definition” page. Scroll down on the page and click on
            the “(restore configuration)” link, then select a resource
            configuration from the drop down list, click on the
            "Restore" button, and then click “Save Resource”.

            .. rubric:: What is a default instance/vm
               type?[\ `edit </index.php?title=FAQ&action=edit&section=45>`__\ ]
               :name: what-is-a-default-instancevm-typeedit

            By "default instance/vm type" we refer to the instance/vm
            types in a precreated cluster configuration. This
            configuration is included when an account is first setup,
            and also when creating a new configuration by selecting a
            configuration from the "Restore Configuration" link at the
            resource definition page.

            .. rubric:: How do I restore customization after the default
               configuration
               restore?[\ `edit </index.php?title=FAQ&action=edit&section=46>`__\ ]
               :name: how-do-i-restore-customization-after-the-default-configuration-restoreedit

            The Parallel Works default configuration release updates
            depend on the changes made to the platform. You can protect
            your configuration customization by backing up changes prior
            to restoring the default configuration.

            From the Parallel Works Platform click on the “Resources”
            tab, select the chicklet, and click on the “Duplicate
            resource” icon, and create a duplicate configuration.

            Use the original configuration for restoring the default
            configuration to bring the latest changes. Manually update
            customization on the original configuration from the backup
            copy.

            You can drop the backup copy or hide it from appearing from
            the "Compute" dashboard. Hide a resource configuration
            option can be found on the “Settings” box on the Resource
            definition page.

            .. rubric:: What is NOAA RDHPCS preferred container
               solution?[\ `edit </index.php?title=FAQ&action=edit&section=47>`__\ ]
               :name: what-is-noaa-rdhpcs-preferred-container-solutionedit

            NOAA RDHPCS official communication on containers:-

            https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Containers

            On security issues and capabilities to run the weather model
            across the nodes, NOAA's RDHPC systems chose Singularity as
            a platform for users to test and run models within
            Containers.

            **Accessing bucket from a Remote Machine (such as: Niagara)
            or Cluster's controller node**

            Obtain your project's keys from the PW platform. The project
            key can be found by navigating from the PW banner.

            Click on the IDE box located on the top right of the page,
            navigate to PW/project_keys/gcp/<project key file>.

            [1] Double click the project key file, and copy the json
            file content. [2] Write the copied content into a file in
            your home directory file. Example:

            Write json to ~/project-key.json (or another filename)

            [2] Source the credential file in your environment.

            source ~/.bashrc

            | 
            | [3] Test access

            Once these variables are added to your host terminal
            environment, you can test gsutils is authenticated by
            running the command:

            | 
            | gsutil ls < bucket name >

            Example:

            gsutil ls gs://noaa-sysadmin-ocio-cg-discretionary gsutil ls
            gs://noaa-coastal-none-cg-mdlcloud

            gsutil cp local-location/filename gs://bucketname/

            | 
            | You can use the -r option to upload a folder.

            gsutil cp -r folder-name gs://bucketname/

            | 
            | You can also use the -m option to upload large number of
              files which performs a parallel
              (multi-threaded/multi-processing) copy.

            gsutil -m cp -r folder-name gs://bucketname

            .. rubric:: Best practice in resource configuration
               page.[\ `edit </index.php?title=FAQ&action=edit&section=48>`__\ ]
               :name: best-practice-in-resource-configuration-page.edit

            **1. Maintain SSH authentication key under account, and use
            it in all clusters.**

            The resource configuration has an “Access Public Key” box,
            to store your SSH public key, and the key stored there is
            only available in a cluster launched with that
            configuration. Instead store your key under “account” ->
            “Authentication” tab
            `[1] <https://noaa.parallel.works/u/settings/authentication>`__
            that automatically populates into your all clusters.

            Reference:
            https://docs.parallel.works/navigating-the-platform#account

            **2. User bootstrap script**

            In the resource config page, user bootstrap script pointing
            to a folder in contrib fs is a good idea. This helps to
            share it in a centralized location and allows other team
            members to use it.

            Example:

            ALLNODES

            /contrib/Unni.Kirandumkara/pw_support/config-cluster.sh

            Reference:

            https://docs.parallel.works/managing-organizations/organization-bootstrap-script#testing-a-sample-bootstrap-script

            Configuration page has a 16k metadata size limitation.
            Following these settings can reduce your possibility of a
            cluster provisioning error.

            .. rubric:: An example Singularity Container build, job
               array that uses bind
               mounts[\ `edit </index.php?title=FAQ&action=edit&section=49>`__\ ]
               :name: an-example-singularity-container-build-job-array-that-uses-bind-mountsedit

            Example that demonstrates a Singularity container build, and
            a job array that uses two bind mounts (input and output
            directories ) and creates an output file for each task in
            the array.

            Recipe file:-

            Bootstrap: docker From: debian

            %post

            ::

                apt-get -y update
                apt-get -y install fortune cowsay lolcat

            %environment

            ::

                export LC_ALL=C
                export PATH=/usr/games:$PATH

            %runscript

            ::

                cat ${1} | cowsay | lolcat > ${2}

            | 
            | Job script:-

            ::

               #!/bin/bash
               #SBATCH --job-name=out1
               #SBATCH --nodes=1
               #SBATCH --array=0-10
               #SBATCH --output sing_test.out
               #SBATCH --error sing_test.err

            mkdir -p /contrib/$USER/slurm_array/output echo "hello
            $SLURM_ARRAY_TASK_ID" >
            /contrib/$USER/slurm_array/hello.$SLURM_ARRAY_TASK_ID

            singularity run --bind
            /contrib/$USER/slurm_array/hello.$SLURM_ARRAY_TASK_ID:/tmp/input/$SLURM_ARRAY_TASK_ID,/contrib/$USER/slurm_array/output:/tmp/output
            /contrib/$USER/singularity/bind-lolcow.simg
            /tmp/input/$SLURM_ARRAY_TASK_ID
            /tmp/output/out.$SLURM_ARRAY_TASK_ID

            | 
            | Expected output:-

            $ ls /contrib/Matt.Long/slurm_array hello.0 hello.1 hello.10
            hello.2 hello.3 hello.4 hello.5 hello.6 hello.7 hello.8
            hello.9 output

            $ ls /contrib/$USER/slurm_array/output/ out.0 out.1 out.10
            out.2 out.3 out.4 out.5 out.6 out.7 out.8 out.9

            $ cat /contrib/$USER/slurm_array/output/out.0

            ::

               _________

            < hello 0 >

            ::

               ---------

            The "bootstrap" line basically is just saying to use the
            debian docker container as a base and build a singularity
            image out of it

            sudo singularity build <image file name> <recipe file name>
            should do the trick with that recipe file.

            .. rubric:: Working with
               SLURM[\ `edit </index.php?title=FAQ&action=edit&section=50>`__\ ]
               :name: working-with-slurmedit

            .. rubric:: How to send emails from a Slurm job
               script?[\ `edit </index.php?title=FAQ&action=edit&section=51>`__\ ]
               :name: how-to-send-emails-from-a-slurm-job-scriptedit

            Below is an example of a job script with a couple sbatch
            options that should notify you when a job starts and ends
            (you will want to replace the email address with your own of
            course):

            | 

            #. !/bin/bash

            #. SBATCH -N 1

            #. SBATCH --mail-type=ALL

            #. SBATCH --mail-user=<your noaa email address>

            hostname -- Optional, this will include the hostname of the
            controller noder.

            The emails are simple, with only a subject line that looks
            something like this:

            Slurm Job_id=5 Name=test.sbatch Ended, Run time 00:00:00,
            COMPLETED, ExitCode 0

            This email may go to your spam folder as it is not domain
            validated, that is one downside.

            .. rubric:: Introduction to
               SLURM[\ `edit </index.php?title=FAQ&action=edit&section=52>`__\ ]
               :name: introduction-to-slurmedit

            https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Introduction_to_SLURM

            .. rubric:: Running and monitoring
               SLURM[\ `edit </index.php?title=FAQ&action=edit&section=53>`__\ ]
               :name: running-and-monitoring-slurmedit

            Use sinfo command to find the status of your job.

            [Unni.Kirandumkara@gcpv2-94 ~]$ sinfo

            PARTITION AVAIL TIMELIMIT NODES STATE NODELIST

            compute\* up infinite 1 down~
            unnikirandumkara-gcpv2-00094-1-0001

            The compute nodes can take several minutes to provision.
            These nodes should automatically shut down once they've
            reached their "Suspend Time", which defaults to 5 minutes
            but can be adjusted. If you submit additional jobs to the
            idle nodes before they shut down, the scheduler should
            prefer those ones (if they are sufficient for the job) and
            the jobs would start a lot quicker. Below is a
            list/description of the possible state codes that a slurm
            node might have. Bolded the ones that you are most likely to
            see while using the cluster:

            | 

            ::

                     *   The  node  is  presently  not responding and will not be allocated any new work.  If the node remains non-responsive, it will be placed in the
                         DOWN state (except in the case of COMPLETING, DRAINED, DRAINING, FAIL, FAILING nodes).

            | 

            ::

                     ~   The node is presently in a power saving mode (typically running at reduced frequency).

            | 

            ::

                     #   The node is presently being powered up or configured.

            ::

                     %   The node is presently being powered down. 

            | 

            ::

                     $   The node is currently in a reservation with a flag value of "maintenance".

            | 

            ::

                     @   The node is pending reboot.

            You can manually start by:

            sudo scontrol update nodename=<nodename> state=resume

            | 
            | [Unni.Kirandumkara@gcpv2-94 ~]$ sudo scontrol update
              nodename=unnikirandumkara-gcpv2-00094-1-0001 state=resume
              [Unni.Kirandumkar@gcpv2-94 ~]$ sinfo PARTITION AVAIL
              TIMELIMIT NODES STATE NODELIST compute\* up infinite 1
              mix# unnikirandumkara-gcpv2-00094-1-0001

            The content references on-prem systems, but somewhat
            applicable in the cloud.

            https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Running_and_Monitoring_Jobs

            .. rubric:: How to set custom memory for slurm
               jobs?[\ `edit </index.php?title=FAQ&action=edit&section=54>`__\ ]
               :name: how-to-set-custom-memory-for-slurm-jobsedit

            In order to get non-exclusive scheduling to work with Slurm,
            you need to reconfigure the scheduler to treat memory as a
            "consumable resource", and then divide the total amount of
            available memory on the node by the number of cores.

            | 
            | Since Parallel Works platform doesn't currently support
              automating this, we have to do it manually, so the user
              script below only works as is on the two instance types
              you're using on your clusters ( AWS p3dn.24xlarge &
              g5.48xlarge). If you decide to use other instance types
              the same base script could be used as a template, but the
              memory configurations would have to be adjusted.

            The script itself looks like this:

            ::

                #!/bin/bash
                # configure /mnt/shared/etc/slurm/slurm.conf to add the realmemory to every node

            sudo sed -i '/NodeName=/ s/$/ RealMemory=763482/'
            /mnt/shared/etc/slurm/slurm.conf sudo sed -i
            '/PartitionName=/ s/$/ DefMemPerCPU=15905/'
            /mnt/shared/etc/slurm/slurm.conf

            ::

                # configure /etc/slurm/slurm.conf to set memory as a consumable resource

            sudo sed -i
            's/SelectTypeParameters=CR_CPU/SelectTypeParameters=CR_CPU_Memory/'
            /etc/slurm/slurm.conf export HOSTNAME="$(hostname)" if
            `$HOSTNAME ==
            mgmt\* </index.php?title=$HOSTNAME_%3D%3D_mgmt*&action=edit&redlink=1>`__
            ; then

            ::

                sudo service slurmctld restart

            else

            ::

                sudo service slurmd restart

            fi

            .. rubric:: How do I change the slurm Suspend time on an
               active cluster? [shutdown early or shutdown
               delay][\ `edit </index.php?title=FAQ&action=edit&section=55>`__\ ]
               :name: how-do-i-change-the-slurm-suspend-time-on-an-active-cluster-shutdown-early-or-shutdown-delayedit

            You can modify a cluster’s slurm suspend time from the
            Resource Definition form prior to starting a cluster.
            However if you want to modify the suspend time after a
            cluster is started, the commands must be executed by the
            owner from the controller node.

            You can modify an existing slurm suspend time from the
            controller node by running the following commands. In the
            following example, the Suspend time is set to 3600 seconds.
            In your case, you may want to set it to 60 seconds.

            sudo sed -i 's/SuspendTime=.*/SuspendTime=3600/g'
            /mnt/shared/etc/slurm/slurm.conf

            if `$HOSTNAME ==
            mgmt\* </index.php?title=$HOSTNAME_%3D%3D_mgmt*&action=edit&redlink=1>`__
            ; then

            ::

                sudo scontrol reconfigure 

            fi

            This example sets the value to 3600 seconds

            before:

            $ scontrol show config \| grep -i suspendtime

            SuspendTime = 60 sec

            after:

            $ scontrol show config \| grep -i suspendtime

            SuspendTime = 3600 sec

            .. rubric:: What logs are needed for the support to research
               slurm or node not terminated
               issues?[\ `edit </index.php?title=FAQ&action=edit&section=56>`__\ ]
               :name: what-logs-are-needed-for-the-support-to-research-slurm-or-node-not-terminated-issuesedit

            The following four log files required to research the root
            cause. Please copy the following log files from the
            controller node [a.k.a head node] to the project's permanent
            storage and share the location in an OTRS help desk ticket.
            In the case, also include the cloud platform name, and the
            resource configuration pool name in the ticket description.

            These files are owned by root. The cluster owner should
            change user as root when copying the files, for example.

            $ sudo su - root

            [1] slurmctld: This is the Slurm control daemon log. It's
            useful for scaling and allocation issues, job-related
            issues, and any scheduler-related launch and termination
            issues.

            /var/log/slurm/slurmctld.log

            [2] slurmd: This is the Slurm compute daemon log. It's
            useful for troubleshooting initialization and compute
            failure related issues.

            /var/log/slurm/slurmd.log

            | 
            | [3] syslog: Reports global system messages.

            /var/log/syslog

            [4] messages: Reports system operations.

            /var/log/messages

            .. rubric:: How do I distribute slurm scripts on different
               nodes?[\ `edit </index.php?title=FAQ&action=edit&section=57>`__\ ]
               :name: how-do-i-distribute-slurm-scripts-on-different-nodesedit

            By default the slurm sbatch job lands on a single node. You
            can distribute the scripts to run on different nodes by
            using “sbatch - -exclusive” flag. The easiest solution would
            probably be to submit the job with an exclusive option, IE:

            \`sbatch --exclusive ...\`

            Or, you can add it to your submit script: \``\`

            #. SBATCH --exclusive

            \``\`

            For example, I have this simple job script: \``\`

            #. !/bin/bash

            #. SBATCH --exclusive

            hostname sleep 120 \``\`

            Submitting the job three times in succession, see how each
            job lands on its own node: \``\` [Matt.Long@gcpv2-60 ~]$
            sinfo PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
            compute\* up infinite 141 idle~
            mattlong-gcpv2-00060-1-[0004-0144] compute\* up infinite 3
            alloc mattlong-gcpv2-00060-1-[0001-0003] batch up infinite
            10 idle~ mattlong-gcpv2-00060-2-[0001-0010]
            [Matt.Long@gcpv2-60 ~]$ squeue

            ::

                           JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
                               3   compute testjob. Matt.Lon  R       0:18      1 mattlong-gcpv2-00060-1-0001 
                               4   compute testjob. Matt.Lon  R       0:09      1 mattlong-gcpv2-00060-1-0002 
                               5   compute testjob. Matt.Lon  R       0:05      1 mattlong-gcpv2-00060-1-0003 

            \``\`

            If I remove the exclusive flag and resubmit, the jobs all
            land on a single node: \``\` [Matt.Long@gcpv2-60 ~]$ squeue

            ::

                           JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
                               6   compute testjob. Matt.Lon  R       0:11      1 mattlong-gcpv2-00060-1-0001 
                               7   compute testjob. Matt.Lon  R       0:10      1 mattlong-gcpv2-00060-1-0001 
                               8   compute testjob. Matt.Lon  R       0:08      1 mattlong-gcpv2-00060-1-0001

            .. rubric:: User Bootstrap fails when copy files to
               lustre[\ `edit </index.php?title=FAQ&action=edit&section=58>`__\ ]
               :name: user-bootstrap-fails-when-copy-files-to-lustreedit

            A recent modification on the cluster provisioning starts
            compute and lustre clusters execution in parallel to speed
            up the deployment. Previously this was a sequential step,
            and took longer to provision a cluster. Since the compute
            cluster comes up earlier than lustre, any user bootstrap
            command to copy files to lustre will fail.

            For example, this step may fail when included as part of the
            user-bootstrap script:

            ::

                 cp -rf /contrib/Andrew.Penny/psurge_dev /lustre

            | 
            | You can use the following code snippet as a workaround.

            ::

               LFS="/lustre"

               until mount -t lustre | grep ${LFS}; do
                 echo "User Bootstrap: lustre not mounted. wait..."
                 sleep 10
               done

               cp -rf /contrib/Andrew.Penny/psurge_dev /lustre

            .. rubric:: What is the command to get max nodes count on a
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=59>`__\ ]
               :name: what-is-the-command-to-get-max-nodes-count-on-a-clusteredit

            Default sinfo output (including a busy node so it shows
            outside of the idle list)

            [Matt.Long@aws-137 ~]$ sinfo

            PARTITION AVAIL TIMELIMIT NODES STATE NODELIST

            compute\* up infinite 1 mix# mattlong-aws-00137-1-0001

            compute\* up infinite 101 idle~
            mattlong-aws-00137-1-[0002-0102]

            batch up infinite 10 idle~ mattlong-aws-00137-2-[0001-0010]

            | 
            | You might prefer to use the summarize option, which shows
              nodes by state as well as total:

            $ sinfo --summarize

            PARTITION AVAIL TIMELIMIT NODES(A/I/O/T) NODELIST

            compute\* up infinite 1/101/0/102
            mattlong-aws-00137-1-[0001-0102]

            batch up infinite 0/10/0/10 mattlong-aws-00137-2-[0001-0010]

            Note the **NODES(A/I/O/T)** section, which indicates nodes
            that are **Active, Idle, Offline, and Total**

            .. rubric:: Manually reset the node
               status[\ `edit </index.php?title=FAQ&action=edit&section=60>`__\ ]
               :name: manually-reset-the-node-statusedit

            You may manually resume the nodes like this:

            % sinfo

            Set the nodename and reset the status to "idle" as given
            below:

            sudo scontrol update
            nodename=philippegion-azurestream5-00002-1-[0001-0021]
            state=idle

            .. rubric:: Errors[\ `edit </index.php?title=FAQ&action=edit&section=61>`__\ ]
               :name: errorsedit

            .. rubric:: Error: Error launching source instance:
               InvalidParameterValue: User data is limited to 16384
               bytes[\ `edit </index.php?title=FAQ&action=edit&section=62>`__\ ]
               :name: error-error-launching-source-instance-invalidparametervalue-user-data-is-limited-to-16384-bytesedit

            Resource configuration page has a 16k metadata size
            limitation. Recent feature updates on the configuration page
            has reduced the free space available for user data, that
            includes SSH public key stored in "Access Public Key", and
            "User Bootstrap".

            Below settings can lower the user data size, and avoid a
            provisioning error due to page size limit.

            Maintain SSH authentication key under the account, and as it
            is shared across all your clusters.

            Click on the “User” icon located at the top right of the
            page, then navigate to the “account” -> “Authentication”
            tab, and your SSH public keys.

            Remove the SSH key from the “Access Public Key” box, and
            save your configuration.

            Reference:
            https://docs.parallel.works/navigating-the-platform#account

            .. rubric:: Where do I enter my public SSH key in the PW
               platform?[\ `edit </index.php?title=FAQ&action=edit&section=63>`__\ ]
               :name: where-do-i-enter-my-public-ssh-key-in-the-pw-platformedit

            Navigate to your account, the Account -> Authentication,
            then click on the "add SSH key" button to your public SSH
            Keys. There is a system key "User Workspace", which is used
            by the system to connect from a user's workspace to your
            cluster.

            .. rubric:: Error “the requested VM size not available in
               the current region”, when requesting a non-default
               compute
               VM/instance[\ `edit </index.php?title=FAQ&action=edit&section=64>`__\ ]
               :name: error-the-requested-vm-size-not-available-in-the-current-region-when-requesting-a-non-default-compute-vminstanceedit

            Each Cloud provider offers a variety of VMs/Instances to
            meet the user requirements. The Parallel Works platform’s
            default configurations have VM/Instances that are tested for
            the peak FV3GFS benchmark performance.

            Hence, the current VM/instance quota is for these default
            instance types, for example c5n.18xlarge, Standard_HC44rs
            and c2-standard-60.

            If your application requires a different VM/instance type,
            it is advised to open a support case with the required
            number of instances, so we can work with the cloud provider
            for an a on-demand quota. Depending on the VM/instance type
            and count, quota allocation may take a day or up to 2 weeks
            depending on the cloud provider.

            .. rubric:: What is causing access denied message when
               trying to access a project’s
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=65>`__\ ]
               :name: what-is-causing-access-denied-message-when-trying-to-access-a-projects-clusteredit

            This message appears if a user account was created after the
            cluster was started. The cluster owner can check whether
            that user account exists by checking in /etc/passwd file as
            below.

            $ grep -i <user-name> /etc/passwd

            Cluster owner can fix the access denied error by restarting
            the cluster. When you restart the cluster, a user record
            will be added in the /etc/passwd file.

            .. rubric:: Why is my API script reporting “No cluster
               found”?[\ `edit </index.php?title=FAQ&action=edit&section=66>`__\ ]
               :name: why-is-my-api-script-reporting-no-cluster-foundedit

            PW made a change on storing the resource pool name
            internally in order to prevent naming edge cases where
            resources with underscores and without underscores were
            treated as the same resource. Underscores will still show up
            on the platform if you were using one before, however now
            internally the pool name is stored without an underscore and
            so some API responses may show different results than
            previously.

            As a result, any API requests that references the pool name
            should now be updated to use the name without underscores.

            .. rubric:: What is causing the "Permission denied
               (publickey,gssapi-keyex,gssapi-with-mic)." ?[\ `edit </index.php?title=FAQ&action=edit&section=67>`__\ ]
               :name: what-is-causing-the-permission-denied-publickeygssapi-keyexgssapi-with-mic.-edit

            The message appears in the Resource Monitor log file is:

            Waiting to establish tunnel, retrying in 5 seconds

            Permission denied
            (publickey,gssapi-keyex,gssapi-with-mic).  

            During a cluster launch process, an ssh tunnel is created
            between the controller node and the user container. The user
            container is trying to create the tunnel before the host can
            accept it, so a few attempts are failed before the host is
            ready to accept the request.  You may ignore this message.

            Also you may also notice an "x" number of failed login
            attempts when log in on the controller node.  This is from
            the failed ssh tunnel attempts.

            If the message is getting when trying to access the
            controller node from an external network, check if the
            public key entered in the configuration is correctly
            formatted. You can verify root cause by ssh'ing to the
            controller node from the PW's IDE located at the top right
            of the page. Access from IDE uses an internal public and
            private key, and therefore you can narrow down the cause.

            | 

            .. rubric:: What is causing the "do not have sufficient
               capacity for the requested VM size in this
               region."?[\ `edit </index.php?title=FAQ&action=edit&section=68>`__\ ]
               :name: what-is-causing-the-do-not-have-sufficient-capacity-for-the-requested-vm-size-in-this-region.edit

            You can find error message from the "Logs", navigate to tab
            "scheduler".

            The above message means there is not enough requested
            resource in the Azure region. You may attempt a different
            region or submit the request later.

            You may manually resume the nodes like this:

            % sinfo

            Set the nodename and reset the status to "idle" as given
            below:

            sudo scontrol update
            nodename=philippegion-azurestream5-00002-1-[0001-0021]
            state=idle

            .. rubric:: Miscellaneous[\ `edit </index.php?title=FAQ&action=edit&section=69>`__\ ]
               :name: miscellaneousedit

            .. rubric:: Parallel Works new features blog
               posts[\ `edit </index.php?title=FAQ&action=edit&section=70>`__\ ]
               :name: parallel-works-new-features-blog-postsedit

            https://parallelworks.com/blog/2023-august-recap

            .. rubric:: Instance Types
               explained[\ `edit </index.php?title=FAQ&action=edit&section=71>`__\ ]
               :name: instance-types-explainededit

            https://parallelworks.com/docs/compute/instance-types

            .. rubric:: How to find cores and threads on a
               node?[\ `edit </index.php?title=FAQ&action=edit&section=72>`__\ ]
               :name: how-to-find-cores-and-threads-on-a-nodeedit

            cat /proc/cpuinfo \|grep -i proc \| wc -l

            lscpu \| grep -e Socket -e Core -e Thread Thread(s) per
            core: 2 Core(s) per socket: 1 Socket(s): 1

            The other option is use “nproc”

            | 

            ::

               There are a couple ways. You can use scontrol  and a node name to print a lot of info about it, including number of available cores:

            $ scontrol show node
            natalieperlin-gclusternoaav2usc1-00049-1-0001 \| grep CPUTot

            ::

                 CPUAlloc=0 CPUTot=30 CPULoad=0.43

            $ scontrol show node
            natalieperlin-gclusternoaav2usc1-00049-1-0001

            NodeName=natalieperlin-gclusternoaav2usc1-00049-1-0001
            Arch=x86_64 CoresPerSocket=30

            ::

                 CPUAlloc=0 CPUTot=30 CPULoad=0.43

            ::

                 AvailableFeatures=shape=c2-standard-60,ad=None,arch=x86_64

            ::

                 ActiveFeatures=shape=c2-standard-60,ad=None,arch=x86_64

            ::

                 Gres=(null)

            ::

                 NodeAddr=natalieperlin-gclusternoaav2usc1-00049-1-0001 NodeHostName=natalieperlin-gclusternoaav2usc1-00049-1-0001 Port=0 Version=20.02.7

            ::

                 OS=Linux 3.10.0-1160.88.1.el7.x86_64 #1 SMP Tue Mar 7 15:41:52 UTC 2023 
                 RealMemory=1 AllocMem=0 FreeMem=237905 Sockets=1 Boards=1
                 State=IDLE+CLOUD ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
                 Partitions=compute 
                 BootTime=2023-07-19T18:47:46 SlurmdStartTime=2023-07-19T18:50:04
                 CfgTRES=cpu=30,mem=1M,billing=30
                 AllocTRES=
                 CapWatts=n/a
                 CurrentWatts=0 AveWatts=0
                 ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s

            You can also look at the node config directly in the slurm
            config file:

            $ grep -i nodename /mnt/shared/etc/slurm/slurm.conf \| head
            -n 1

            NodeName=natalieperlin-gclusternoaav2usc1-00049-1-0001
            State=CLOUD SocketsPerBoard=1 CoresPerSocket=30
            ThreadsPerCore=1 Gres=""
            Features="shape=c2-standard-60,ad=None,arch=x86_64"

            | 
            | General rule of thumb will pretty much be that any Intel
              based instance has HT disabled, and core counts will be
              half of the vCPU count advertised for the instance.

            .. rubric:: How do I remove my project’s GCP contrib
               volume?[\ `edit </index.php?title=FAQ&action=edit&section=73>`__\ ]
               :name: how-do-i-remove-my-projects-gcp-contrib-volumeedit

            Contrib volume is a permanent storage for custom software by
            project members. In Google cloud this storage is charged on
            the allocated storage, that is 2.5TB and costs about $768.00
            per month. If the project does not require this storage, PI
            may create a cloud help desk ticket to remove it. Only
            Parallel Works Cloud administrator can remove this storage.

            .. rubric:: How do I find my project’s object storage [aka
               bucket or block storage] and access keys from Parallel
               Works?[\ `edit </index.php?title=FAQ&action=edit&section=74>`__\ ]
               :name: how-do-i-find-my-projects-object-storage-aka-bucket-or-block-storage-and-access-keys-from-parallel-worksedit

            From the login page, click on the IDE icon located at the
            top right of the page, you will see file manager with
            folders.

            From the File Manager, navigate under the
            “storage/project_keys/<CSP>” folder to locate your project’s
            object storage name and access key. **The file name is your
            project’s bucket name**. Open the file by double clicking to
            view the bucket access key information.

            To access the project's permanent object storage, copy and
            paste the contents from the key file on the controller node,
            then execute the CSP commands. For example:-

            On AWS platform:

            aws s3 ls s3://(enter your file name here)/

            On Azure platform:

            azcopy ls https://noaastore.blob.core.windows.net/ (enter
            your file name here)/

            On GCP platform:

            gsutil ls gs://(enter your file name here)/

            | 
            | You may use the Globus Connect or Cloud service provider’s
              command line interface to access the object storage.
              Globus training material link : `12 Aug 2021
              Training <https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/Training_Videos#Globus_Connect_for_CSPs_-_August_13.2C_2021>`__

            .. rubric:: Can I transfer files with external object
               storage [aka bucket or block storage] from Parallel
               Works's
               cluster?[\ `edit </index.php?title=FAQ&action=edit&section=75>`__\ ]
               :name: can-i-transfer-files-with-external-object-storage-aka-bucket-or-block-storage-from-parallel-workss-clusteredit

            If you have the access credentials of external AWS/Azure/GCP
            object storage, you can transfer files. Use the Globus
            connector or cloud provider's command line interface for
            file transfer.

            .. rubric:: Azure: How to copy a file from the controller
               node to the project's permanent
               storage?[\ `edit </index.php?title=FAQ&action=edit&section=76>`__\ ]
               :name: azure-how-to-copy-a-file-from-the-controller-node-to-the-projects-permanent-storageedit

            [1] Start a cluster and login into the controller node.

            An example use the project cz-c4-id’s secret file.

            Your project’s permanent storage file name is the same as
            the secret key file name.

            [2] Copy and paste the secret key file located at PW’s file
            manager storage:storage/project_keys/azure/gfdl-non-cz-c4-id
            in the controller node terminal.

            It will show an authentication message as below:

            INFO: SPN Auth via secret succeeded.

            Indicating Service Principal Name (SPN) by using a secret
            succeeded.

            [3] Copy a file:

            Use the Azure destination as:

            https://noaastore.blob.core.windows.net/\ <Name of the
            secret key file>/

            [FName.Lastname@devcimultiintel-41 ~]$ azcopy cp test.txt
            https://noaastore.blob.core.windows.net/gfdl-none-cz-c4-id/
            INFO: Scanning... INFO: Authenticating to destination using
            Azure AD INFO: azcopy: A newer version 10.16.2 is available
            to download

            INFO: Any empty folders will not be processed, because
            source and/or destination doesn't have full folder support

            Job c7a7d958-f741-044e-58e8-8c948489e5f1 has started Log
            file is located at:
            /home/FName.Lastname/.azcopy/c7a7d958-f741-044e-58e8-8c948489e5f1.log

            0.0 %, 0 Done, 0 Failed, 1 Pending, 0 Skipped, 1 Total,

            | 
            | Job c7a7d958-f741-044e-58e8-8c948489e5f1 summary Elapsed
              Time (Minutes): 0.0334 Number of File Transfers: 1 Number
              of Folder Property Transfers: 0 Total Number of Transfers:
              1

            [4] To list the file, use the command: azcopy ls
            https://noaastore.blob.core.windows.net/gfdl-none-cz-c4-id/test.txt

            Copying a file to Niagara’s untrusted location is done using
            a ssh key file. The firewall settings on the GFDL are not
            open to allow a file copy.

            .. rubric:: How do I use GCP gsutil transfer files to a
               project
               bucket?[\ `edit </index.php?title=FAQ&action=edit&section=77>`__\ ]
               :name: how-do-i-use-gcp-gsutil-transfer-files-to-a-project-bucketedit

            GCP uses the gsutil utility to transfer data into HPC
            on-prem system. The “gsutil” command can run either from the
            user’s local machine or the RDHPCS systems, such as Niagara.
            The gsutil utility is preinstalled on clusters launched
            through Parallel Works.

            | 

            | 

            | 

            .. rubric:: How do I get nvhpc NVidia HPC compiler, and
               netcdf, and hdf5 packages in my
               environment?[\ `edit </index.php?title=FAQ&action=edit&section=78>`__\ ]
               :name: how-do-i-get-nvhpc-nvidia-hpc-compiler-and-netcdf-and-hdf5-packages-in-my-environmentedit

            Parallel Works Platform is installed with Intel processors
            and compilers for the FV3GFS performance benchmark test. It
            also has all the on-prem libraries [/apps] to provide a
            seamless on-prem experience.

            The platform offers flexibility to use other processors such
            as ARM, and NVIDIA GPU, and install nvhpc compilers to fit
            the researchers' specific experiments.

            You can install custom software and create a modified image
            [root disk] to use in your experiments. The other option is
            to install on your project’s contrib volume and reference
            it. Contrib is a permanent storage for your project's custom
            software management. Note that you are responsible for your
            custom software stack, although we will try our best to help
            you.

            Instructions to create a custom image can be found at the
            Cloud Wiki doc:
            https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/FAQ#How_do_I_create_a_custom_image_.5Ba.k.a_AMI_or_machine_image.5D.3F

            Instructions to install NVidia HPC compiler can be found
            here:
            https://docs.nvidia.com/hpc-sdk/hpc-sdk-install-guide/index.html

            Various netcdf and hdf5 packages are available from the yum
            repos. yum search netcdf and yum search hdf

            | 

            | 

            .. rubric:: Which AWS Availability Zones [AZ] AMD and Intel
               processors are concentrated [Answer to
               InsufficientInstanceCapacity]?[\ `edit </index.php?title=FAQ&action=edit&section=79>`__\ ]
               :name: which-aws-availability-zones-az-amd-and-intel-processors-are-concentrated-answer-to-insufficientinstancecapacityedit

            This information is subject to change based on the demand.
            This is in-order by best opportunity for capacity.

            AMD

            hpc6a.48xlarge : us-east-2b

            Intel

            c5n.18xlarge : us-east-1b us-east-1f us-east-2a

            | 
            | c6i.24xlarge : us-east-1f

            c6i.32xlarge : us-east-2b us-east-1f us-east-2a

            .. rubric:: What does GCP resource GVNIC and Tier_1 flags
               represent?[\ `edit </index.php?title=FAQ&action=edit&section=80>`__\ ]
               :name: what-does-gcp-resource-gvnic-and-tier_1-flags-representedit

            Tier1 is the 100gbps network. GVNIC is a high performance
            interconnect that bypasses their virtual interconnect for
            better network performance.

            Tier 1 bandwidth configuration is only supported on N2, N2D
            EPYC Milan, C2 and C2D VMs. Tier 1 bandwidth configuration
            is only compatible with VMs that are running the gVNIC
            virtual network driver.

            Default bandwidth ranges from 10 Gbps to 32 Gbps depending
            on the machine family and VM size. Tier 1 bandwidth
            increases the maximum egress bandwidth for VMs, and ranges
            from 50 Gbps to 100 Gbps depending on the size of your N2,
            N2D, C2 or C2D VM.

            Additional reference:
            https://cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration

            | 

            .. rubric:: Why are all instance types are labeled as
               AMD64?[\ `edit </index.php?title=FAQ&action=edit&section=81>`__\ ]
               :name: why-are-all-instance-types-are-labeled-as-amd64edit

            AMD64 is the name of the architecture, not the cpu platform.
            Intel and AMD chips are both "amd64". Additional reference:
            https://en.m.wikipedia.org/wiki/X86-64

            .. rubric:: Data access via globus CLI tools in the
               cloud[\ `edit </index.php?title=FAQ&action=edit&section=82>`__\ ]
               :name: data-access-via-globus-cli-tools-in-the-cloudedit

            This capability is similar to what has been recently made
            available on NOAA HPC systems. Implementation is simply the
            installation of the globus-cli tools in /apps for global
            availability. Alternately, the user can install the tools
            using Anaconda/Miniconda:

            | 
            | $ conda install -c conda-forge globus-cli

            **Globus Connect Personal**

            However, unlike the on-prem HPC systems, the user will need
            to use Globus Connect Personal tool as well. If not already
            installed, the user can install it and set up the service to
            create an endpoint on that master node by downloading the
            tool, untarring it, and running setup:

            | 
            | $ wget
              https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz

            $ tar xzf globusconnectpersonal-latest.tgz

            cd globusconnectpersonal-3.1.2

            Creating the new Endpoint

            $ ./globusconnectpersonal -setup

            Globus Connect Personal needs you to log in to continue the
            setup process.

            | 
            | We will display a login URL. Copy it into any browser and
              log in to get a single-use code. Return to this command
              with the code to continue setup.

            | 
            | Login here:

            --------------

            https://auth.globus.org/v2/oauth2/authorize?client_id=4d6448ae-8ca0-40e4-aaa9-8ec8e8320621&redirect_uri=https...d_grant=AnthonyDelSorbo-pclusternoaa-00003

            --------------

            Enter the auth code: T7J06mJZIdnBVXXXXXXXXXXXvDgK ==
            starting endpoint setup Input a value for the Endpoint Name:
            pcluster-Tony registered new endpoint, id:
            5c085198-2a9a-11eb-8fc1-0a34088e79f9 setup completed
            successfully

            | 
            | Show some information about the endpoint: $
              ep0=5c085198-2a9a-11eb-8fc1-0a34088e79f9

            $ globus endpoint show $ep0

            Display Name: pcluster-Tony ID:
            5c085198-2a9a-11eb-8fc1-0a34088e79f9 Owner:
            delsorbo@globusid.org Activated: False Shareable: True
            Department: None Keywords: None Endpoint Info Link: None
            Contact E-mail: None Organization: None Department: None
            Other Contact Info: None Visibility: False Default
            Directory: None Force Encryption: False Managed Endpoint:
            False Subscription ID: None Legacy Name:
            delsorbo#5c085198-2a9a-11eb-8fc1-0a34088e79f9 Local User
            Info Available: None GCP Connected: False GCP Paused (macOS
            only): False

            | 
            | Activate the endpoint:

            $ ./globusconnectpersonal -start &

            | 
            | Now we can begin using the end point:

            $ globus ls $ep0

            globusconnectpersonal-3.1.2/ miniconda3/
            globusconnectpersonal-latest.tgz miniconda.sh

            | 
            | Transferring Data

            Once the tools are installed, the process of transferring
            data requires that you first authenticate with your globus
            credentials by using:

            | 
            | $ globus login

            User is presented with a link to the globus site to
            authenticate and get an Authorization code for this new
            endpoint.

            Please authenticate with Globus here:

            --------------

            https://auth.globus.org/v2/oauth2/authorize?client_id=5a51be3c-4859-4750-bc40-04afb9c2f0f6&redirect_u...access_type=offline&prompt=login

            --------------

            Enter the resulting Authorization Code here:
            vaxqcWY8k8b0Mn3pkvzBHlAqdU1yW1

            You have successfully logged in to the Globus CLI!

            | 
            | $ globus whoami

            delsorbo@globusid.org

            $ globus session show

            Username \| ID \| Auth Time

            --------------

            \| ---------- ... ------ \| --------------------

            delsorbo@globusid.org \| c7937222-d ... 657448 \| 2020-11-18
            03:43 UTC

            | 
            | $ globus whoami --linked-identities

            delsorbo@globusid.org

            $ globus endpoint search "niagara"

            ID \| Owner \| Display Name

            --------------

            ... --- \| -------------------------- \|
            ------------------------------

            775060 ... 68 \| computecanada@globusid.org \|
            computecanada#niagara 21467dd ...9b \|
            noaardhpcs@globusid.org \| noaardhpcs#niagara 0026a4e ...93
            \| noaardhpcs@globusid.org \| noaardhpcs#niagara-untrusted
            B59545d ...4b \| negregg@globusid.org \| Test Share on
            noaardhpcs#nia ... ...

            $ ep1=0026a4e4-afd2-11ea-beea-0e716405a293

            $ globus endpoint show $ep1

            Display Name: noaardhpcs#niagara-untrusted ID:
            0026a4e4-afd2-11ea-beea-0e716405a293 Owner:
            noaardhpcs@globusid.org Activated: True Shareable: True
            Department: None Keywords: None Endpoint Info Link: None
            Contact E-mail: None Organization: None Department: None
            Other Contact Info: None Visibility: True Default Directory:
            /collab1/ Force Encryption: False Managed Endpoint: True
            Subscription ID: 826f2768-8216-11e9-b7fe-0a37f382de32 Legacy
            Name: noaardhpcs#niagara-untrusted Local User Info
            Available: True

            List the directory in that endpoint:

            $ globus ls $ep1:/collab1/data_untrusted/Anthony.DelSorbo

            | 
            | Create a new directory:

            $ globus mkdir
            $ep1:/collab1/data_untrusted/Anthony.DelSorbo/cloudXfer

            The directory was created successfully.

            | 
            | Conduct a Transfer:

            $globus transfer $ep0:globusconnectpersonal-latest.tgz
            $ep1:/collab1/data_untrusted/Anthony.DelSorbo/cloudXfer
            --label "TonyCloudTransferTest1"

            Message: The transfer has been accepted and a task has been
            created and queued for execution Task ID:
            d1b7bd5c-2a9f-11eb-8fc1-0a34088e79f9

            .. rubric:: Container singularity replaced by
               singularity-ce, and syntax remains the
               same[\ `edit </index.php?title=FAQ&action=edit&section=83>`__\ ]
               :name: container-singularity-replaced-by-singularity-ce-and-syntax-remains-the-sameedit

            When it comes to the software package on the PW platform, it
            follows on-prem guidance to provide a consistent user
            experience between the environments.

            The prior lineage of Singularity was forked twice.
            SingularityCE and Apptainer. Singularity has not been
            renamed.

            Singularity container executable name is same as
            singularity, community edition consistent with on-prem
            usage.

            $ rpm -ql singularity-ce \| grep bin /usr/bin/singularity

            | 

            .. rubric:: How to list the files in an s3 bucket using a
               script?[\ `edit </index.php?title=FAQ&action=edit&section=84>`__\ ]
               :name: how-to-list-the-files-in-an-s3-bucket-using-a-scriptedit

            ::

               #!/usr/bin/python3

            | 

            import fsspec

            | 

            fs = fsspec.filesystem('s3')

            urls = ['s3://' + f for f in
            fs.glob("s3://noaa-sysadmin-ocio-ca-cloudmgmt/mlong/\*.nc")]

            | 

            print(urls)

            | 
            | This generates some output like this:

            ['s3://noaa-sysadmin-ocio-ca-cloudmgmt/mlong/test1.nc',
            's3://noaa-sysadmin-ocio-ca-cloudmgmt/mlong/test2.nc',
            's3://noaa-sysadmin-ocio-ca-cloudmgmt/mlong/test3.nc']

            | 
            | S3 credentials should be set automatically in your
              environment on the cluster, but these credentials are
              scoped at a project level, and not to individual users.

            .. rubric:: What is the best practice in hiding credentials,
               when code is pushed in
               Github?[\ `edit </index.php?title=FAQ&action=edit&section=85>`__\ ]
               :name: what-is-the-best-practice-in-hiding-credentials-when-code-is-pushed-in-githubedit

            Use your programming language command to call out
            environment variables. For example in Python: key_value =
            os.environ['AWS_ACCESS_KEY_ID']

            It is very important not to commit a full print out of the
            shell environment.

            .. rubric:: Where should I clone the GitHub
               repository?[\ `edit </index.php?title=FAQ&action=edit&section=86>`__\ ]
               :name: where-should-i-clone-the-github-repositoryedit

            If you want to keep the repository around between cluster
            sessions, working with it from contrib would be the right
            choice. If you aren’t doing anything too complex in the repo
            (like editing files), or if anything compiling is fairly
            small, doing everything from the controller would be fine.
            Big compiles would probably be better on a compute node
            since you can assign more processors to the build.

            .. rubric:: GCP Region/AZs on GPUs and
               models[\ `edit </index.php?title=FAQ&action=edit&section=87>`__\ ]
               :name: gcp-regionazs-on-gpus-and-modelsedit

            From the below link, select a location “North America” and
            machine type “A2” to view different types of GPUs available
            on different regions/AZs.

            https://cloud.google.com/compute/docs/regions-zones#available

            To learn more about GPU models, refer to the link below.

            https://cloud.google.com/compute/docs/gpus/gpu-regions-zones#gpu_regions_and_zones

            .. rubric:: What are the GPU models available on AWS, Azure,
               and
               GCP[\ `edit </index.php?title=FAQ&action=edit&section=88>`__\ ]
               :name: what-are-the-gpu-models-available-on-aws-azure-and-gcpedit

            AWS GPUs can be found by typing P3,P4,G3,G4,G5,or G5g.

            https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html

            | 
            | Azure GPUs can be found by typing Standard_NC,
              Standard_ND, Standard_NV, and Standard_NG

            https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu

            GCP GPUs can be found by typing a2. Other GPUs are found to
            be unavailable.

            https://cloud.google.com/gpu

            .. rubric:: What are the Cloud regions supported by Parallel
               Works?[\ `edit </index.php?title=FAQ&action=edit&section=89>`__\ ]
               :name: what-are-the-cloud-regions-supported-by-parallel-worksedit

            AWS: us-east1 and us-east2. Preferred region is us-east-1
            Azure: EastUS and SouthCentralUS. Preferred region is
            EastUS. GCP regions are us-central1, and us-east-1.
            Preferred region is us-central1

            .. rubric:: X2go Passwordless authentication using
               ssh-keys[\ `edit </index.php?title=FAQ&action=edit&section=90>`__\ ]
               :name: x2go-passwordless-authentication-using-ssh-keysedit

            Refer the link:

            https://wiki.x2go.org/doku.php/wiki:advanced:authentication:passwordless-ssh

            .. rubric:: How to tunnel back from a compute node to the
               controller/head
               node?[\ `edit </index.php?title=FAQ&action=edit&section=91>`__\ ]
               :name: how-to-tunnel-back-from-a-compute-node-to-the-controllerhead-nodeedit

            A case where the users have added their keys to the account
            and can login to the head node and run jobs. However, when
            they start a job on compute node and then try to tunnel back
            to the head node it fails.

            Users on the cluster can create an ssh key on the cluster
            that will allow access back to the head node from compute.
            If you want to use a different key name that would work, but
            you might need to configure the ssh client to look for it.
            This works.

            ssh-keygen -t rsa -f ~/.ssh/id_rsa -N *&& cat
            ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys*

            .. rubric:: On Azure, missing /apps fs system or modules not
               loaded
               case[\ `edit </index.php?title=FAQ&action=edit&section=92>`__\ ]
               :name: on-azure-missing-apps-fs-system-or-modules-not-loaded-caseedit

            We are working to fix this bug. If you own the Azure
            cluster, please run the command : sudo /root/run_ansible

            It will take about 2 mins to complete, and will mount /apps
            file system.

         .. container:: printfooter

            Retrieved from
            "http://localhost:8180/index.php?title=FAQ&oldid=798"

      .. container:: catlinks catlinks-allhidden
         :name: catlinks

.. container::
   :name: mw-navigation

   .. rubric:: Navigation menu
      :name: navigation-menu

   .. container::
      :name: mw-head

      .. rubric:: Personal tools
         :name: p-personal-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  Not logged in
         -  `Talk </index.php/Special:MyTalk>`__
         -  `Contributions </index.php/Special:MyContributions>`__
         -  `Create
            account </index.php?title=Special:CreateAccount&returnto=FAQ>`__
         -  `Log in </index.php?title=Special:UserLogin&returnto=FAQ>`__

      .. container::
         :name: left-navigation

         .. rubric:: Namespaces
            :name: p-namespaces-label
            :class: vector-menu-heading

         .. container:: vector-menu-content

            -  `Page </index.php/FAQ>`__
            -  `Discussion </index.php?title=Talk:FAQ&action=edit&redlink=1>`__

         English

         .. container:: vector-menu-content

      .. container::
         :name: right-navigation

         .. rubric:: Views
            :name: p-views-label
            :class: vector-menu-heading

         .. container:: vector-menu-content

            -  `Read </index.php/FAQ>`__
            -  `Edit </index.php?title=FAQ&action=edit>`__
            -  `View history </index.php?title=FAQ&action=history>`__

         More

         .. container:: vector-menu-content

         .. container::
         vector-search-box-vue vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box
            :name: p-search

            .. container::

               .. container:: vector-search-box-inner
                  :name: simpleSearch

   .. container:: vector-legacy-sidebar
      :name: mw-panel

      .. container::
         :name: p-logo

         ` </index.php/Main_Page>`__

      .. rubric:: 
         :name: p--label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Cloud Computing User Information </index.php/Main_Page>`__
         -  `Additional Topics </index.php/Additional_Topics>`__
         -  `Training Videos </index.php/Training_Videos>`__
         -  `Office Hours </index.php/Office_Hours>`__
         -  `Cloud Success Stories </index.php/Cloud_Success_Stories>`__
         -  `Utilization </index.php/Utilization>`__
         -  `User Meetings </index.php/User_Meetings>`__
         -  `Getting Help </index.php/Getting_Help>`__
         -  `FAQ </index.php/FAQ>`__

      .. rubric:: Tools
         :name: p-tb-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `What links here </index.php/Special:WhatLinksHere/FAQ>`__
         -  `Related
            changes </index.php/Special:RecentChangesLinked/FAQ>`__
         -  `Special pages </index.php/Special:SpecialPages>`__
         -  `Printable version <javascript:print();>`__
         -  `Permanent link </index.php?title=FAQ&oldid=798>`__
         -  `Page information </index.php?title=FAQ&action=info>`__

-  This page was last edited on 22 September 2023, at 15:02.

-  `Privacy policy </index.php/clouddocs:Privacy_policy>`__
-  `About clouddocs </index.php/clouddocs:About>`__
-  `Disclaimers </index.php/clouddocs:General_disclaimer>`__

-  |Powered by MediaWiki|

.. |Powered by MediaWiki| image:: /resources/assets/poweredby_mediawiki_88x31.png
   :width: 88px
   :height: 31px
   :target: https://www.mediawiki.org/


