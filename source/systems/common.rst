######
Common
######

Welcome to RDHPCS CommonDocs -- Information and procedures that pertain across all RDHPCS systems.

The RDHPCS Maintenance Downtime Calendar has events for NESCC (Hera, HPSS, Niagara), Jet, Boulder and Princeton Bastions, and other RDHPCS system downtimes.
View the Calendar `here <https://calendar.google.com/calendar/u/1/r?id=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`_

.. raw:: html

   <div>
   <iframe src="https://calendar.google.com/calendar/embed?src=noaa.gov_f1ggu43tm9lfeeg45t59a063cs%40group.calendar.google.com&ctz=America%2FNew_York"
           style="border: 0"
           width="800"
           height="600"
           frameborder="0"
           scrolling="no"></iframe>
   <p>You must be logged in to your NOAA Gmail account to see the calendar.</p>
   </div>

CommonDocs Topics
-----------------

+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| General Information                          | Getting Things Done                           | Data Transfers                                 |
+==============================================+===============================================+================================================+
| **Help Requests**                            | **Applications**                              | Globus Online Data Transfer                    |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Account Management**                       | Applications and Libraries                    |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Getting an Account                           | Containers                                    | Migrating Data Between Local Filesystems       |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| New Device: Software                         | **Running and Monitoring Jobs**               | **Frequently Asked Questions**                 |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Suspension and Reactivation                  | Introduction to SLURM                         |  Recent User-Facing Changes                    |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Role Accounts                                | How SLURM with Fair Share Works               |  Training Documentation                        |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Request    Access to Additional Projects     | Getting Information about your Projects       |  HPC Definitions                               |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Reset your Master Certificate Password       | Allocations and Quotas                        |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Accessing RDHPCS Systems**                 | Compilers                                     | **Using the HMS HPSS**                         |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Policies and Best Practices**              | Editing Tools                                 |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+

================
Data Transfer
==============


`Globus Globus Connect Service
(GCS) <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer>`__\ 
is now available on RDHPCS systems, and we encourage its use over any
other method whenever possible. Some use cases that involve sites
outside the RDHPCS program that may not support Globus may still use
other methods described in this document.

Many users are accustomed to using scp/sftp via service (same as login)
nodes. However, we would like to point out that Data Transfer Nodes
(DTN's) provides a much faster method for transferring data to and from
HPC systems (Jet/Hera/Niagara/Gaea/WCOSS/Orion), so we highly recommend
DTNs over service nodes.

Much data on RDHPCS servers are protected by confidentiality agreements,
may be sensitive, or are otherwise proprietary. Our obligation includes
the enforcement of all policies that make curating such data even
possible. This involves maintaining tight security that adheres to NOAA
OCIO guidelines. We also recognise the need for sharing data with
collaborators who may not be vetted by us to ensure that NOAA/DOC
standards are met. The so-called *untrusted DTN* was created so that
less secure channels may be open for the smooth transfer of data
essential for projects to conduct their research.

The following section is common for most operating systems and
exceptions are noted.

Only the High-Performance Filesystems (the scratch filesystems) are
available, **not your /home filesystem**. When you are asked for a
password, provide your RSA Token’s PIN + current 6 digit number (a.k.a
Passcode).

For Niagara each user must complete their initial login in order to set
up their user account directories before you can transfer data. For more
information regarding this process and the Niagara directory structure,
please visit the
`NiagaraDocs <https://niagaradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page>`__
wiki page.

.. _globus_connect:

Globus Connect
==============

For complete details, please visit `Globus Online Data
Transfer <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer>`__

.. _trusted_data_transfer_node:

Trusted Data Transfer Node
==========================

By default, trusted DTN's (dtn) are only accessible from some hosts
within noaa.gov (and Orion). If you need access to a host not within the
noaa.gov domain, we will need to modify system firewalls. Please see:
`Firewall Modifications for
DTNs <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Transferring_Data#Firewall_Modification_Requests_for_DTNs>`__

| DTN's support ssh-based authentication transfer methods, which
  currently include scp, rsync, and bbcp (Jet and Hera only). Default
  authentication uses your RSA token.
| **Note for Windows Users:** For Windows users using **WinSCP**, please
  choose **SFTP** as the protocol rather than **SCP**.

| \ **Hera:** ``dtn-hera.fairmont.rdhpcs.noaa.gov``
| \ **Niagara:** ``dtn-niagara.fairmont.rdhpcs.noaa.gov``
| \ **Jet:** New DTN's (as of 01/22/21)
  ``dtn-jet.boulder.rdhpcs.noaa.gov``
| \ **Jet:** Old DTN's (until 2/9/21) ``dtn-jet.rdhpcs.noaa.gov``
| \ **Orion:** ``orion-dtn.hpc.msstate.edu``

.. _untrusted_data_transfer_node_available_on_niagara_only:

Untrusted Data Transfer Node (Available on Niagara Only)
========================================================

Unlike Trusted DTNs (Used on Jet and Hera), Untrusted DTNs (udtn) are
accessible from anywhere on the internet. They are designed to allow
data to brought in to the RDHPCS program from external sites (Non-NOAA
HPC sites, Cloud providers, Universities, etc...).

**IMPORTANT NOTE:** Before you can use the udtn for doing data
transfers, it is important to login to Niagara once to set up the
necessary directories including your home directory. In order to login
to Niagara, please use one of the following methods for logging in:

RSA login:

| ``   ssh niagara-rsa.princeton.rdhpcs.noaa.gov``
| ``   ssh niagara-rsa.boulder.rdhpcs.noaa.gov``

CAC login:

| ``   ssh bastion-niagara.princeton.rdhpcs.noaa.gov``
| ``   ssh bastion-niagara.boulder.rdhpcs.noaa.gov``

Once you login to Niagara your directories will be created automatically
and ready for use. Then you can use the DTNs available on Niagara for
doing your data transfers.

| DTN's support ssh-based authentication transfer methods, which
  currently include scp, rsync, and bbcp. Default authentication uses
  your RSA token.
| **Note for Windows Users:** For Windows users using **WinSCP**, please
  choose **SFTP** as the protocol rather than **SCP**.

| \ **Niagara:** ``udtn-niagara.fairmont.rdhpcs.noaa.gov``
| **Please note** The udtn (untrusted DTNs) on only access the following
  file system: /collab1/data_untrusted/

So typically you will be copying files in and out of
**/collab1/data_untrusted/$USER**.

**Unattended data transfers are only allowed on the Trusted DTN's;
therefore they are not allowed on Niagara's Untrusted DTNs.**


==================
 RDHPCS Platforms
==================

.. tab-set::

   .. tab-item:: Gaea

      Climate Modeling and Research System (CMRS) at Oak Ridge National Laboratory
      `More Information <https://www.noaa.gov/organization/information-technology/gaea>`_

   .. tab-item:: Hera

      Predicting high-impact weather events
      `More Information <https://www.noaa.gov/organization/information-technology/hera>`_

   .. tab-item:: Jet

      Hurricane Forecast Improvement Program (HFIP)
      `More Information <https://www.noaa.gov/organization/information-technology/jet>`_

   .. tab-item:: Niagara

      Collaborative resource for data transfer
      `More Information <https://www.noaa.gov/organization/information-technology/niagara>`_

   .. tab-item:: MSU-HPC

      High-performance Computing collaboration with Mississippi State University (MSU)
      `More Information <https://www.noaa.gov/organization/information-technology/MSU-HPC>`_


   .. tab-item:: Cloud

      Platform to create and use HPC computatational clusters on an as-needed basis.
      `More Information <https://www.noaa.gov/information-technology/hpcc>`_

Documents
---------

.. raw:: html

   <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSXDvIeFif0_RJ5Po3y1i2gJdVVPpfbJ0QQUVATXBBqy68Ughdu9rkWI2lN9CsoaEwUa6449m2Nh7ZA/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

.. note::

   You must be logged in to your NOAA Google account to view the documents.