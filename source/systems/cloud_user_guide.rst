
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

Training Videos
===============

            Training Videos are available for Cloud Computing Platform
            users. Click a link to view the video.
            
           Parallel Works 
           --------------
            .. rubric:: Parallel Works New Features Training, September
               27, 2023
            | `Workshop with Matt
              Long <https://drive.google.com/file/d/1C8Ouyhg4zw1knkbrHZcAdp9vlptPTvf6/view?ts=6515d57a>`__
            | Matt Long demonstrated enhancements to Parallel Works
              features:
            -  Updates to Notifications, with expanded notification
               types and email notification options
            -  Short term credentials, which can be used effectively for
               cluster and storage resources
            -  Updates to the Marketplace feature. Cluster and storage
               configurations can now be shared with team members
               through the Marketplace.
            -  Lustre configurations can now be designated persistent,
               and saved separately from the clusters. This potentially
               saves storage costs.

            .. rubric:: Parallel Works New Features Training, June 14,
               2023
            `Workshop with Matt
            Long <https://drive.google.com/file/d/1hu1Q-VindCStFtMixCk2Vfie9JK9NJy-/view?ts=648b2fef>`__
            Matt Long demonstrated the Parallel Works platform,
            including the new feature on storage, and enhanced cost
            dashboard. New users start here.

            .. rubric:: Parallel Works New Features Training, March 23,
               2023
            `Workshop with Matt
            Long <https://drive.google.com/file/d/1QeC3WDS2aG3EdxyeTNS84vPECo26dxtP/view?ts=641c5fe3>`__

            The training will cover the following topics:
            - Show estimated costs to run a given cluster configuration,
            - SSH keys configurable from inside platform, at user level,
             -Configurable slurm timeouts (and other slurm settings), and
            - **building a custom snapshot.**

            .. rubric:: Parallel Works Platform Enhancements, February
               16, 2023
            .. rubric:: Training Presentation
            `Slide deck - February 16 2023 <https://docs.google.com/presentation/d/1Uevb_Z2AGkNE0pLO-jc1u43lbJ5vy8UcvUBrshW_NKg/edit#slide=id.g20c4ad86293_1_0>`__

            .. rubric:: Foundation
            **New users start here.** Foundational topics include
            Creation of a cluster configuration, multi-user setup,
            hiding a resource, duplicating a resource, monitor to view
            cluster status, cost dashboard, connect to a controller
            node, running an interactive job, storage options, Scheduler
            and deletion tabs from the Resource monitor link.

            Review the presentation
            `here. <https://drive.google.com/file/d/1Has2qJG6QZsaT3KTKp2VYBKBH4_6hrTO/view?ts=63f3b396>`__

            .. rubric:: Workflows
            Workflow topics include: 
            - subscribing a workflow from the PW
            Marketplace, example **Juypter Notebook**
            - running a job
            from the head node and compute node
            - canceling a job,
            - deletion of a cluster
            - creation and use of a custom image in
            a workflow
            - **RStudio**
            - sharing a cluster with project
            members, and
            - bootstrap script.

            Review the presentation
            `here. <https://drive.google.com/file/d/1dcnPAsXUqt9SWvRo7CEhgXHFdmNCm3qV/view?ts=63f3bd26>`__

            .. rubric:: Workflow Interactive
               Session
            Molecular dynamics simulation and visualization on a multi-cluster model.
            Review the presentation
            `here. <https://drive.google.com/file/d/1rTNz8MNeQwxq_8Xvm-SQa2-0hYDdggfn/view?ts=63f3e2bf>`__

            .. rubric:: Training Q & A
            Review questions and comments
            `here. <https://docs.google.com/document/d/1eXZvqbsg8gpTrqjyA_dDqOs1wMaygVQZq1Rl2yXGbUo/edit#heading=h.6fg85uulj4z9>`__

            .. rubric:: Other Parallel Works
               Training
               Parallel Works Version
               2 <https://drive.google.com/file/d/1-bkcc8k3_2nEKL-xhSAyLNe_K0iXM_r8>`__
               March 23, 2022
            -  `Parallel Works Version 2 <https://drive.google.com/file/d/1Ag12PtVMLu4kHmLZfR04geVOf8g1RwbO>`__
               January 20, 2022
            -  `Parallel Works Platform Training
               II <https://drive.google.com/file/d/1i_1cNkRdpsbMeegpC-ZsiMPhkdAmbpjA>`__
               July 15, 2021. Topics include:

               -  Connecting to a transient cluster head node from a
                  remote host
               -  Configuration settings to re-size the nodes count
               -  Lustre file system; Use of different processors
               -  Monitoring workers
               -  Slurm jobs
               -  workflow Jupyter Notebook
               -  Singularity container example
               -  Budget allocation

            .. rubric:: Use Case Sessions
           -  `JupyterHub Installation on a Conda, and R
               Troubleshooting <https://drive.google.com/file/d/1gA1bv69JMCWQuk8iYApgugmt1W04ctkg/view?ts=6436b22b>`__
               April 7, 2023
               -  This recorded session details JupyterHub installation
                  on a Conda, and R troubleshooting.

            .. rubric:: Globus
            -  `Globus Training: Setup and Data
               Transfer <https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view>`__
               March 17, 2023
               -  This training walks you through the process of setting
                  up an endpoint, and transfering files to the CSP
                  classification.

            -  `Useful tutorials from
               Globus <https://docs.globus.org/how-to/instructional-videos/>`__

Cloud Success Stories! 
======================
            -  `NOS Team: Storm Surge
               Modelling <https://drive.google.com/file/d/12WWIjj-ULJkkAtxbMnerq8LAdWSvR7gd/view?usp=sharing>`__
               September 27, 2022
            -  `NWS Team: Rapid Refresh Forecast
               System <https://drive.google.com/file/d/1ESypA2IRLKAzAvrxjmVAi1mhnIS7OwtK/view?usp=sharing>`__
               September 21, 2022
            -  `EPIC Cloud Success
               Story <https://drive.google.com/file/d/1muXZQ6uTDFEnGNUG5ZJ_R59D9HwBWDP9/view>`__
               September 15, 2022 -->!



Office Hours
============

            The Cloud Computing support team hosts bi-weekly sessions
            for demonstrations, questions and answers. Submit questions
            in advance to unni.kirandumkara@noaa.gov.

            | `14 September
              2023 <https://drive.google.com/file/d/1INH-x7Cz025UtwMQDjlQX9Yn5MdQ_xE5/view?ts=6504735f>`__
            | Workshop with Matt and Steve.

            | `30 August
              2023 <https://drive.google.com/file/d/1qbZHqXSfH2V5J_SL2Nt7Huq86v4nqjBK/view?ts=64f0bb3e>`__
            | In this session, users submitted questions in advance, and
              Matt and Unni responded.

            -  A user is trying to balance the relative cost of
               computation and storage capacity -- storage costs are
               especially high. The user may switch from GCP to AWS in
               the coming year, to access available GPUs, which have
               been hard to access in GCP.

            **Answer:** Matt suggested where information on GPUs could
            be found, and how one might deduce where GPUs could be
            expected, based naming connections. G4 nodes should contain
            GPUs.

            -  A user had a question about Allocation questionnaire for
               the coming year.

            **Answer:** The questionnaire comes from the Program
            Management team. Specific questions can be raised to PIs and
            PMs.

            -  A user had issues with GPUs, storage costs and
               reservations.

            **Answer:** GPUs from GCP are harder to access. However, AWS
            platform with On-Demand Capacity reservation (large capacity
            for four weeks) is working out. Switching from GCP to AWS
            would reduce costs, with a higher probability of getting
            GPUs. Reservations are available in AWS only, with admin
            support. Parallel Works has not yet been able to mirror that
            functionality on Google.

            -  A user requested that estimation costs and GPU
               information should be added to documentation/Wiki.

            **Answer:** Will investigate.

            -  A user had question about using a Jupityr notebook, and
               whether it can be set up on Contrib.

            **Answer:** That's a right way to proceed. Installation
            takes a lot of time, but everything should be fine once it’s
            installed. If the user knows in advance what packages he
            needs, he can make a custom snapshot of the package.
            Singularity and Docker and Podman are all available.

            -  A user needs to request more allocation on AWS.

            **Answer:** Send an email to Gonzalo Lassally to request
            allocation. Can be done in a few days.

            -  A user is used to a Linux environment and is slowly
               getting used to Cloud. He's been looking at available
               videos and finding resolution to be poor -- are there
               other videos available.

            **Answer:** Probably not many, but the Cloud team will
            research for them.

            |  `16 August
              2023 <https://drive.google.com/file/d/1Sybufzev_MEl7o0k41B5wKaCM1Nne6qG/view?ts=64de6f71>`__
            | In this Q&A session, Matt and Unni answered questions as
              follows:

            -  For questions concerning Azure file transfers - Matt gave
               a demonstration
            -  Andy raised issues with access. Matt discussed firewalls,
               and export and send commands.
            -  Issue concerning the file path from Parallel Works.
            -  Questions on Jupyter
            -  Andy asked how users can know what's updated and what's
               obsolete in Parallel Works, and requested that users be
               informed when changes are made, because of impacts to
               their work.
            -  Questions concerning confidential data.
            -  Question about ssh key versus api key.
            -  Question concerning R Studio.
            -  Kimani asked about cluster persistence.

         
            | `2 August 2023
               <https://drive.google.com/file/d/1yRvdLWIsQo9K7sSCs01Gm9fRduizekcZ/view?ts=64cd5bb3>`__
              This Q&A session was attended by some new GFDL team
              members, looking for the information they needed to get
              started. There's a dataset that can only be accessed on
              AWS Cloud, and these users need background and transfer
              information.

            -  Matt gave an overview of new features in Parallel Works,
               particularly temporary credentials for buckets. The
               Buckets and Storage pages can be used obtain temporary
               credentials. (This feature is not yet available on
               Azure.) Matt also mentioned ephemeral lustres, a new
               enhancement.
            -  Unni pointed the new users to the Clouddocs wiki, citing
               a June training that provides background to access
               storage, and links to Parallel Works documentation. This
               may help the new users to get started.
            -  Raghu offered some specific guidance.
            -  Unni proposed a meeting with the new users, himself and
               Matt, to move their task forward.

            | 19 July 2023
            | A technical difficulty prevented the team from recording
              the Office Hours session. Questions and responses are
              summarised
              `here. <https://docs.google.com/document/d/1S1162ePlycBjpylL0cggp-6p_RtEX_LQZ_0kLbG3qrk/edit>`__

            | `5 July
              2023 <https://drive.google.com/file/d/1e7lkH3esEToYEBvL53P0DJm8Sm0L4G33/view?ts=64a6ee9f>`__
            | In this Q&A session, Matt and Unni addressed the following
              topics:

            -  GPU selection and constraints, especially on Azure
            -  Can a user configure the Cloud account to send email when
               a job completes or fails? More than one user has this
               request; Matt will assist them.
            -  Users have had clusters that completed work but did not
               shut down. This results in extensive charges for nothing.
               Matt says this is a known issue being actively worked. In
               the meantime he recommends users look in the Log tabs for
               job and cluster status.
            -  Matt demonstrated the new Properties tab in Parallel
               Works. Among other things it can be used to enable email
               alerts.
            -  Unni mentioned the upcoming Super Computing Conference in
               Denver, 12-17 November. Anyone interested in submitting a
               paper to the Birds of a Feather session may do so
               `here <https://sc23.supercomputing.org/program/birds-of-a-feather/>`__.

            | `21 June
              2023 <https://drive.google.com/file/d/1PPj6ZM6cZTPE6FVGt9luDDiouAo9RRty/view?ts=64944e9f>`__
            | No questions were submitted prior to this session, but a
              lively discussion took place.

            -  Some users discussed their challenges in getting
               on-demand Nvidia GPU processors.
            -  Matt recommended on-demand reservations and described how
               reservations work in some detail.
            -  Users discussed the cost of jobs submitted under the
               reservation system.
            -  Unni recommended the Cost Estimation feature available
               with the AWS system.

            | 
            | `7 June
              2023 <https://drive.google.com/file/d/1N7PwnfYu5aD0Fo8Z8GYwCF9brw0m9J72/view?ts=6481d78c>`__
            | In this open Q&A session, Matt and Unni addressed the
              following topics:

            -  Account problems
            -  Studio workflows
            -  The new COST dashboard
            -  Lustre configuration issues
            -  Azure cold storage options.

            Notes from this session can be found
            `here. <https://docs.google.com/document/d/1FUDebrZ_lYv3VgUTKvxWGvpDE6VMNQaJmwVy5g_8Jx8/edit>`__

            | `24 May 2023 <https://drive.google.com/file/d/1r9AFrctc-OuhQpWlxzjeFmXEbs-kxGob/view?ts=646f6dcf>`__
            | In this session, users submitted questions in advance,
              including:

            -  Disk space allowance on /contrib, /home, and the Cloud
               environment.
            -  The difference between MDS and OST boot disk size, and
               access to each.
            -  Cluster activation and de-activation, and timing and
               configuration changes.
            -  Methods currently in use to move data to and from the
               Cloud.
            -  Syncing global-workflow fixed files for \`develop\` to
               AWS s3, and related AWS s3 issues
            -  Optimized IC staging for regression testing
            -  Mitigating FS latency
            -  Azure operation questions.

            | 
            | `10 May 2023 <https://drive.google.com/file/d/1zL8TQ68qa3Nh0s3JB11VnvrJtwqEhvaH/view?ts=646d0527>`__
            | This was an open question-answer session covering the
              following:

            -  The Podman application
            -  Reported queueing problems in Parallel Works
            -  Could the frequent version incrementation in Parallel
               Work have an impact on clusters or other operations in
               progress. (Parallel Works said no.)
            -  Features in future update:

               -  Partition settings in Google Cloud configuration

            | 
            | `26 April 2023 <https://drive.google.com/file/d/1ZtZuZoJ28-M8qEvwZERvOENaUrNcCdmU/view?ts=64528126>`__
            | This video references the creation of a cloud/custom
              snapshot in these steps:

            -  Resource definition
            -  Activate conda at boot
            -  Update “.bashrc” using bootstrap script
            -  Copy files from laptop to contrib using scp, rsync, and
               Globus
            -  Cluster health check
            -  Copy file between contrib and bucket using gsutil

            | 

            | `12 April 2023 <https://drive.google.com/file/d/1WEhr5aJ37FLTqIoCbFbxt1vXi4I0yZtd/view?ts=64381afa>`__
            | Topics discussed in this session include:

            -  Google contrib storage use best practices
            -  Finding a project bucket
            -  gsutil command
            -  Azure’s contrib and block storage as the same storage
            -  Storage issues, including centralized storage of user
               public ssh keys
            -  upcoming features, storage,
            -  health check scripts and custom snapshots
 .. rubric:: Features in Development

            There are new features and capabilities under discussion at
            Parallel Works. If you are interested in these features,
            send an email ticket to: rdhpcs.cloud.help@noaa.gov, with
            the subject line PW Features.

          
Frequently Asked Questions
=====================

.            .. rubric:: General Cloud
               Issues

            .. rubric:: How do I open a cloud help desk ticket?

            Send an email to rdhpcs.cloud.help@noaa.gov. Your email
            automatically generates a case in the OTRS system.

            The OTRS system does not have an option to set a priority
            level. Typically, your ticket is responded to within 2
            hours.

            .. rubric:: Where do I find instructions to connect the
               controller node from outside the
               network?

            Refer the Parallel works user guide, section From outside
            the platform:-
            https://docs.parallel.works/interacting-with-clusters/logging-in-controller

            .. rubric:: What are the project allocation usage limits and
               actions?

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
               allocatin increase?

            RDHPCS System compute allocations are decided upon by the
            RDHPCS Allocation Committee (AC), with oversight from the
            NOAA HPC Board. The information for allocation is contained
            on the RHPCS common docs wiki:

            `<https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Allocations_and_Quotas#Request_an_Increase_in_Allocations>`_

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

                  "root_size": "256",

          

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
            | [2] Create an AIM ticket to create your project by
              emailing to the AIM administrator.

            A Portfolio Manager or Principal Investigator can send a
            request to AIM administrator rdhpcs.aim.help@noaa.gov, by
            providing the following information:

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
            | [f] Allocation amount [optional].

            | 
            | Setting up a project in AIM can take two days.

            AIM system administrator creates a cloud help desk ticket to
            create a project on the Parallel Works platform.

            Setting up a project in Parallel Works can take a day. Upon
            the project creation, the AIM administrator will email back
            with the project status.

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



