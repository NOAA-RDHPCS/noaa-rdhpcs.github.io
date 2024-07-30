.. _FAQ:

####
FAQ
####


Recent User-Facing Changes
==========================

Apr 29, 2024: The new LFS5 filesystem on Jet
--------------------------------------------

The new LFS5 filesystem is now available on Jet and will be replacing
LFS1.  Users are urged to migrate from LFS1 to LFS5 as soon as
possible.  Please see data-transfer-overview TBD LINK **manageing data
to local file systems** for information on some of the utilities to
facilitate the move from LFS1 to LFS5

The new LFS5 file system has"hot pools" enabled and
uses part of the filesystem as cache.

You should use the output of '''saccount_prarms''' to see usage by
your project.   Since we have only project based quotas that is the
only quota that is enforced.

.. note::

    Please do not rely on the output of "du" to compare your file space usage.

To find information of usage by user, please see the following
link on where to find that information:

TBD -- **SLURM#Project_Disk_Space_Usage_By_User_Information**

Apr25, 2024: Rocoto updateto version rocoto/1.3.7 on Hera/Jet/Niagara
---------------------------------------------------------------------

There were some performance
issues and some minor bugs in rocoto/1.3.6
after the migration to Rocky8, mostly caused by the performance of
Ruby that comes with the OS.  So Ruby/3.2.3 was installed as module
and the latest version of rocoto/1.3.7 has been built in installed as
the default version.

Please see the following document on Best Practices for using Rocoto:

TBD **Rocoto Best Practices**

Apr 9, 2024: The aging uJet and tJet clusters are being turned off
------------------------------------------------------------------

The uJet and tJet clusters are being turned off as they are based on very old
hardware, and it is becoming difficult to support them on the newer OS.

This means the '''ujet''' and '''tjet''' partitions are no longer
available, so please use one of the other available partitions.

Apr 2, 2024: Migration to Rocky8 in phases (Complete)
-----------------------------------------------------

.. note::

    Hera/Niagara/Jet are all now on Rocky8 and the transition
    to Rocky8 is complete.

Please see the following Google Doc for `information about the transition
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.9971adjl0yrd>`_

This is an evolving document and will be updated with new information
as needed.

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Mar 19, 2024: Migration to Rocky8 in phases
-------------------------------------------

We continue to make progress on the gradual Migration from CentOS7 to Rocky8.

.. code-block:: shell

    |=========================================================|
    |  Unless you select a specific node, you will land       |
    |  on a Rocky8 node and any jobs you submit from there    |
    |  will run on the Rocky8 nodes.                          |
    |                                                         |
    |  If you need to use CentOS7 for some reason, you can    |
    |  do so by pressing ^C when the list of hosts is         |
    |  presented and pick a CentOS7 node.n                    |
    |                                                         |
    |  Please begin migrating to Rocky8 ASAP!                 |
    |=========================================================|


See the weekly announcements for the schedule and the latest updates.

Current migration status
^^^^^^^^^^^^^^^^^^^^^^^^

* Jet:

  - All clusters except kJet on Rocky8
  - When you login the default login node will be a Rocky8 login node

* Hera:

  - 2/3rd of Hera and 1/2 of FGE nodes are on Rocky8
  - When you login the default login node will be a Rocky8 login node

* Niagara:

  - All of Niagara is on Rocky8

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Feb 20, 2024: Migration to Rocky8 in phases
-------------------------------------------

Both Hera and Jet have begun the migration to Rocky8 in phases.
Please see the weekly announcements for the schedule.

.. code-block:: shell

    |=========================================================|
    |  Unless you select a specific node, you will land       |
    |  on a CentOS-7 node and any jobs you submit from there  |
    |  will run on the CentOS-7 nodes.                        |
    |                                                         |
    |  Please exercise Rocky8 nodes by explicitly selecting   |
    |  one of the nodes from fe[5-8] and jobs submitted from  |
    |  will run on the Rocky8 nodes.                          |
    |=========================================================|


Please see the following Google Doc for `information about the transition
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.9971adjl0yrd>`_

This is an evolving document and will be updated with new information
as needed.

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Jan 17, 2024: Rocoto updated to version 1.3.6
---------------------------------------------

The Rocoto Workflow Manage has been updated to the latest version,
version 1.3.6. This version has some very important fixes, so it is
very important to switch this version as soon as possible.

Please keep in mind the following general guidelines for using Rocoto:

For your module loads:
    **module load rocoto**            is preferable to
    module load rocoto/1.3.6

For your crontab entries:
   **/apps/rocoto/default/bin/rocotorun**        is preferable to
   /apps/rocoto/1.3.6/bin/rocotorun

Please be sure to modify your scripts and also your **crontab**
entries!

RDHPCS Office Hours
===================

Office Hours are held at regularly. The Support team offers shared
solutions to acute and common problems.

20 June 2024
------------

Ron Millikan presented `Tensorflow Jumpstart Training <https://drive.google.com/file/d/1WklYsbKrp8_4tydqkayAM6EwCVKDNG-9/view>`_.
A `transcript the training <https://docs.google.com/document/d/1Ys5S0YGeREmJgXy_KQ6tOygidVV7zGdmmzJDqIZTDzY/edit>`_ of the training is available as well.

4 June 2024
-----------

The Support Team discussed `issues concerning the
transition of Orion from Rocky8 to Rocky9
<https://mail.google.com/mail/u/0/?pli=1#inbox/FMfcgzQVwxHbVFPQmVbgbXmkhCrzXlKq?projector=1
here.>`_

10 May 2024
-----------

`Issues concerning data transfer in the Cloud
<https://drive.google.com/file/d/13TZiHRBi4ISAALmrxXY0J3Wv8ccm4oex/viewS>`_
A `transcript of the meeting is available
<https://docs.google.com/document/d/1vbYrndTaAeiy7qAs2alx9proKmHwtK5x-C2YFXDbPt4/edit#heading=h.rqoqmdvh8gtp>`_

26 April 2024

The Support Team fielded issues with Hercules and Rocoto. The team
discussed Gaea, and that cron is not allowed to run there. This may
present issues when the C6 system comes on line.

A `recording of the meeting is available
<https://drive.google.com/file/d/1r2i0OLVz9XepaXVmo6aSkfbHGvB7ceoL/view>`_

29 March 2024
-------------

The transition to Rocky8 remains a matter of concern. Raj suggested
that Centos7 might be maintained in Google Cloud in a single
environment, on an emergency basis. Unni is testing Rocky8 in the
Globus and Azure space in the Cloud; he expects to report at the next
Office Hours meeting. Several users raised specific Rocky8 issues in
this call.

A `recording of the meeting is available
<https://drive.google.com/file/d/18Uigf1mtdKNXt9GAdB4y8zwbTeG_9lRL/view>`_

15 March 2024
-------------

The upgrade from Centos7 to Rocky8 Operating Systems remains a key
issue. System users and the Support Team `discussed plans, benchmarks
and the effects of the transition.
<https://drive.google.com/file/d/1a6xNqxFZ9SPVzZRtuBEW_P1GuZ2U40CA/view>`_

Note that there is `transition documentation for system users
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.cheodqg1384>`_

1 March 2024
------------

Currently the most critical issue in the RDHPCS environment is the
planned upgrade from Centos7 to Rocky8 Operating Systems.
Transition documentation for system users is available
Note that there is `transition documentation for system users
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.cheodqg1384>`_

You can review the `meeting notes
<https://docs.google.com/document/d/17l8MHlKo_Dx6IXdHODFY3iEdkpH6A_XNtqf_WiwMEzs/edit?usp=sharing>`_

New User Office Hour 28 Feb 2024
--------------------------------

This was a pilot session for new RDHPCS system users. It was offered
as an open session for asking technical questions! In addition, the
User Support team requested feedback on what would have helped new
users getting introduced to the RDHPCS environment.

The team shared `notes from the meeting
<https://docs.google.com/document/d/1Y0ggCrYGcY4yrMeV8SSX4nh2POIbzVFhzGyMmKtozYY/edit>`_

4 Jan 2024
----------

`Cumulative notes
<https://docs.google.com/document/d/18RbFULSZ9wppSnXrXAN0_327tKJJjbIy1st2d8Bc67w/edit#heading=h.om52ynf0dwon>`_

Topics for discussion:

* Recurrent questions -  would there be interest in short presentations to cover those topics?

  - Setting up Python on RDHPCS systems
  - Using Globus CLI for data transfer
  - Brown Bag Session items proposed by Leslie

* Discussion on Operating System migration from Centos7 to Rocky8,
  to be completed by June 2024.
* Wikis, errors and room for improvement
* File transfer issues
* Regional models working on Hera
* Cluster creation
* Containerization
* Supercomputing conference and applicability to RDHPCS
* What information should be provided as background to new users?

15 December 2023
----------------

`Office hour notes <https://docs.google.com/document/d/1C303IDoCM4wpkHkKl4QFbJlNvBesz66d2nEhBpQ_Ddo/edit>`_

30 Nov 2023
-----------

The premier session for RDHPCS Office Hours was held on 30 November 2023.
`Office hour notes <https://docs.google.com/document/d/1mXpRHhp909ybqyjhU0LXRNCkuWhwS41v-aLK7EWn588/edit>`_`

