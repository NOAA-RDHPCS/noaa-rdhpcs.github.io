.. _Getting Started:

#######
Getting Started
#######

===========
Documentation
=============

Visit the RDHPCS CommonDocs page (rdhpcs-common-docs (noaa.gov) for information on HPC processes and activities. This page also provides links to system-specific documentation. 

==============
Maintenance Schedule
================

System maintenance will affect access to RDHPCS systems. Click `here:
<https://calendar.google.com/calendar/u/1/r?cid=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`_ to view the RDHPCS Maintenance Downtime Calendar.



=============
Getting Access
=============

This figure is an overview of the timeline and process for system access. 

.. image:: /images/access1.png

Once you have  a NOAA.gov email address, you can request an RDHPCS account. 
Visit the `Account Information Management (AIM) website <https://aim.rdhpcs.noaa.gov>`_ and  request access to the RDHPCS project.  Log into AIM using your NOAA email credentials, review your profile for accuracy, and request the RDHPCS project.

.. image:: /images/AIM2.png

Once this request is approved, you will receive an email containing instructions about your next steps. These include requesting access to further projects and completing the RSA token request form.  Confer with your supervisor and colleagues to identify the  project(s) to request.

**RSA Software Token**


RSA software tokens provide two factor authentication (2FA) for NOAA RDHPCS systems for SSH access. When you’re assigned to your first project, the RSA token form will be used to assign your software token. Your RSA token will include instructions about how to initialize it. You can find more information on RSA tokens here: Logging in - rdhpcs-common-docs (noaa.gov). NOTE:  If you don’t have a smartphone, you can request an RSA hardware token. The activation process is found here: `New User Activation <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/New_User_Activation#RSA_Token_Activation>`_.  RSA software tokens are preferred.

**CAC Access**

The Common Access Card (CAC), is the preferred means of access to RDHPCS resources for both Web and SSH access. To obtain a CAC, work with your local admin services team as they need to start the application process.  Some labs can issue CACs on-site, otherwise you will have to visit a RAPIDS site. The site locator website is ID Card Office Online (osd.mil).  SSH logins with a CAC require additional software detailed  `here.<https://rdhpcs-common-docs>'_ . 

================
Accessing the Systems
=====================

**NOTE:** To access a system, you must be on a project assigned to that system.

On-Premise RDHPCS systems (Gaea, Hera, Jet, Niagara, PPAN) are accessed via SSH.  See the following pages for detailed instructions:

* `RSA logins <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/RSA_Login>`_
* `CAC logins <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/CAC_Login>`_

MSU systems (Orion, Hercules) are accessed via SSH or OpenOnDemand. See `Orion login: <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in>`_ for detailed instructions.

Cloud RDHPCS platforms (AWS, Azure, GCP) are accessed via ParallelWorks in a web browser.  Login `here <https://noaa.parallel.works/log>`_`

**Cloud Computing**

The Cloud Platform allows RDHPCS users to create a high-performance computational cluster on a cloud-based platform (AWS, Azure or GCP) with resources that are appropriate for specific processing tasks. Cloud access is mediated through the Parallel Works application. An overview of the Cloud workflow, and links to detailed instructions, can be found here: Cloud Computing User Information - clouddocs (noaa.gov). 

=============
Data Transfer
=============

Globus Connect Transfer is the most efficient way to transfer data between NOAA RDHPCS sites and external collaborators, such as NCAR, NCEP, and Princeton. You can manage transfers through a web interface, as well as from the command line interface (CLI). See  Globus Quickstart - rdhpcs-common-docs (noaa.gov) for a brief overview of the transfer process, and tps://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer for complete information. 

