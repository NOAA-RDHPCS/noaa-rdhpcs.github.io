
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


Workflow
==========

The typical workflow for using the cloud resources is as follows:


.. image:: /images/CloudProcessing.jpg



Globus Connect
==============

Globus is a tool for online data transfer.  
See the `Globus Connect documentation <https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/Additional_Topics#Globus_Connect>`_ for further information.

Getting Help
------------

For questions or assistance, email a ticket to: rdhpcs.cloud.help@noaa.gov, with the subject line Cloud Support.</br>
Please send your feedback on product, support, and documentation to Unni Kirandumkara, email address: Unni.Kirandumkara@noaa.gov.

Training Videos
===============

Training Videos are available for Cloud Computing Platform users.  Click a link to view the video.

Parallel Works
---------------

`Parallel Works New Features Training, March 23, 2023
<https://drive.google.com/file/d/1QeC3WDS2aG3EdxyeTNS84vPECo26dxtP/view?ts=641c5f>`_  

The training covers following topics:
- mShow estimated costs to run a given cluster configuration
- SSH keys configurable from inside platform, at user level
- Configurable slurm timeouts (and other slurm settings)
- **building a custom snapshot**

Parallel Works Platform Enhancements, February 16, 2023 
`Training Presentation Slides <https://docs.google.com/presentation/d/1Uevb_Z2AGkNE0pLO-jc1u43lbJ5vy8UcvUBrshW_NKg/edit#slide=id.g20c4ad86293_1_01>`_

**Foundation -- New users start here**
Foundational topics include Creation of a cluster configuration, multi-user setup, hiding a resource, duplicating a resource, monitor to view cluster status, cost dashboard, connect to a controller node, running an interactive job, storage options, Scheduler and deletion tabs from the Resource monitor link.
`Review the presentation here <https://drive.google.com/file/d/1Has2qJG6QZsaT3KTKp2VYBKBH4_6hrTO/view?ts=63f3b396>`_

**Workflows**
Workflow topics include: subscribing a workflow from the PW Marketplace, example '''Juypter Notebook''', running a job from the head node and compute node, canceling a job, deletion of a cluster, creation and use of a custom image in a workflow, *RStudio*, sharing a cluster with project members, and bootstrap script.
`Review the presentation here <https://drive.google.com/file/d/1dcnPAsXUqt9SWvRo7CEhgXHFdmNCm3qV/view?ts=63f3bd26>`_

**Workflow Interactive Session: **
Molecular dynamics simulation and visualization on a multi-cluster model.
`Review the presentation here <https://drive.google.com/file/d/1rTNz8MNeQwxq_8Xvm-SQa2-0hYDdggfn/view?ts=63f3e2bf>`_

**Training Q & A**
`Review questions and comments here <https://docs.google.com/document/d/1eXZvqbsg8gpTrqjyA_dDqOs1wMaygVQZq1Rl2yXGbUo/edit#heading=h.6fg85uulj4z9>`_

Other Parallel Works Training
------------------------------
`<https://drive.google.com/file/d/1-bkcc8k3_2nEKL-xhSAyLNe_K0iXM_r8 Parallel Works Version 2,  March 23, 2022>`_
`<https://drive.google.com/file/d/1Ag12PtVMLu4kHmLZfR04geVOf8g1RwbO Parallel Works Version 2 January 20, 2022>`_
`<https://drive.google.com/file/d/1i_1cNkRdpsbMeegpC-ZsiMPhkdAmbpjA Parallel Works Platform Training II]''' July 15, 2021.>`_

Topics include:
- Connecting to a transient cluster head node from a remote host
- Configuration settings to re-size the nodes count
- Lustre file system; Use of different processors
- Monitoring workers
-  Slurm jobs
- workflow Jupyter Notebook
- Singularity container example
- Budget allocation

Use Case Sessions
-----------------

`<https://drive.google.com/file/d/1gA1bv69JMCWQuk8iYApgugmt1W04ctkg/view?ts=6436b22b JupyterHub Installation on a Conda, and R Troubleshooting> April 7, 2023>`_`
This recorded session details JupyterHub installation on a Conda, and R troubleshooting.

Globus
------

`<https://drive.google.com/file/d/1jKAcRGAInmWarUQ_OV7_xsiUesZPX5Ck/view Globus Training:  Setup and Data Transfer March 17, 2023>`_`
** This training walks you through the process of setting up an endpoint, and transfering files to the CSP classification.
* ''' [https://docs.globus.org/how-to/instructional-videos/ Useful tutorials from Globus]'''
= Cloud Success Stories! = 

* '''[https://drive.google.com/file/d/12WWIjj-ULJkkAtxbMnerq8LAdWSvR7gd/view?usp=sharing NOS Team:  Storm Surge Modelling]'''  September 27, 2022
* '''[https://drive.google.com/file/d/1ESypA2IRLKAzAvrxjmVAi1mhnIS7OwtK/view?usp=sharing NWS Team: Rapid Refresh Forecast System]'''  September 21, 2022
* '''[https://drive.google.com/file/d/1muXZQ6uTDFEnGNUG5ZJ_R59D9HwBWDP9/view EPIC Cloud Success Story]'''  September 15, 2022

= Features in Development = 

There are new features and capabilities under discussion at Parallel Works. If you are interested in these features, send an email ticket to: rdhpcs.cloud.help@noaa.gov, with the subject line PW Features.

* '''[https://drive.google.com/file/d/1PtDEvKcfrovH4MgRUwcNdVbn1MBFCOq1/view?ts=63518294 Parallel Works - Logging and Connecting to an On-Premises Cluster]'''  October 20, 2022
* '''[https://drive.google.com/file/d/1LSSGiYodg7RMXGA-FJ6-4klBGrF6C87l/view?ts=635181fe Parallel Works - Running an Interactive Session Workflow on an On-prem Cluster]  October 20, 2022
