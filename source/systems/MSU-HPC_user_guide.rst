.. _MSU-HPC-user-guide:

****************
MSU-HPC User Guide
****************

.. _orion-system-overview:

General Information
==========

Logging In
----------

Running Jobs on MSU-HPC Systems
==========

Getting Information about your Projects
----------

MSU-HPC System Configuration
========

Managing Packages in /contrib
--------------------

Account Management
=========

Getting An Account
----------
MSU-HPC users are not allowed to request their own account
on the system. A new account request must come from a project's Account Manager (like a RDHPCS Principal
Investigator - PI) or a project's Portfolio Manager (PfM) who holds an MSU account.
**If you need an account on MSU-HPC, contact your
project's Account Manager to submit an account request for
you.**

.. rubric:: **Submit a New User Account Request (Account Manager/PI/PfM Responsibility)**
The following procedure is intended for the Account Manager
or the Portfolio Manager who has an active MSU account.

.. rubric:: **Assemble User Information**
Before you begin, collect the following details:

-  First Name
-  Last Name
-  Desired Login Name - Typcially first initial, last name
   (John Doe = jdoe)
-  Email address. Preferably the user's @noaa.gov address.
   Otherwise use a business email address that best aligns
   with the user's work or university.
-  Effective Date. Typically today
-  Expiration Date. 1 year or less from the Effective Date.
-  Project(s) As Account Manager, you can only assign a user
   to your projects.

.. Note::
    When you request a new account, you become the
    account supervisor. As supervisor, you are responsible to
    renew the user's account when it approaches the Expiration
    Date. 
    
See `Account Renewal <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Account_Renewal>`__

.. rubric:: **Login to the MSU account management
   system**

-  Navigate to MSU's account management system: `MSU Account
   Management <https://intranet.hpc.msstate.edu/services/external_accounts/noaa>`__
-  Authenticate using your MSU username and password.

.. Note::
    If you do not remember your password, see: `Logging In - Password <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in#Password>`__

.. rubric:: **Check to see if the user already has an
   account. If not, request account.**

-  `NOAA-HPC Project Management by User <https://intranet.hpc.msstate.edu/services/external_accounts/noaa/manageProjects.php>`__
-  If the user appears in the drop-down, their MSU account
   already exists. Select the user and assign them to your
   projects. If not, navigate to: `NOAA-HPC Computer Account Request <https://intranet.hpc.msstate.edu/services/external_accounts/noaa/requestAccount.php>`__
-  Complete the form.
-  **Click save and Submit** This completes the initial account request. It's good
  practice to notify the prospective new user that the
  request has been made, so they can expect email from MSU.

Once the initial account request has been submitted, MSU
will send the prospective user email similar to the
following, to request the additional information needed for
the background check and account finalization.

.. code-block::
   From: help@hpc.msstate.edu
   Date: Fri, Jan 31, 2020 at 12:21 PM
   Subject: NOAA-HPC Users Agreement confirmation
   To: <john.doe@noaa.gov>

   A computer account request has been submitted to the the Mississippi State University High Performance Computing Collaboratory (MSU HPC2) on your behalf.  In order to facilitate continued processing of this account request, you must complete the application via the below web address.

   `<https://www.hpc.msstate.edu/computing/external_accounts/noaa/confirmAccount.php>`__

   This request will be removed from the queue if no response is received by 02/14/20.

   For problems related to your computer account request, please reply to this message and provide details of the problem.

   If you received this email in error, you can simply ignore the email.

   -- 
   Systems Administration Team
   High Performance Computing Collaboratory
   Mississippi State University
   help@hpc.msstate.edu

.. rubric:: **Complete the HPC2-NOAA User Account Request Confirmation form (User)**

-  Click on the link provided in the email, fill out the
   form, agree to the terms and conditions, and submit the
   form.

.. note::
    If you have an NOAA RDHPCS account, use the same Organization, Phone, and Address you use in AIM. Otherwise, use your business contact information.

If you find you are unable to submit the form, try another password. **Do not use the # character** as it has
  periodically caused problems. Certain other characters in the password might block the form submission, please
  submit a help ticket if you experience a problem `Orion
  Help <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.

.. note:: 
  The password that you enter will be your 
  temporary password. So please remember your password.
  This is critical to the next step of the on-boarding
  process.

.. rubric:: **Set Password and Complete Training (User)**

MSU vets the account request and creates the user account
(1-2 weeks). MSU then sends email, similar to the one below,
will be to the new prospective user. To find the email, search your emails with the following:
-  From: @hpc.msstate.edu
-  Subject: new user account

::

   The following account has been created:

   ReqDate     EffDate     Supervisor  MSU_Status  Account_Type   Login   UserName
   -----------------------------------------------------------------------------------------------
   2020-01-31  2020-01-29  name        NonMSU      Orion          jdoe    John Doe


   Two-Factor authentication (2FA) registration and password changing is required within 3 days. Security training must then be completed before HPC2 resources can be accessed.

   Visit https://taps.hpc.msstate.edu to complete these requirements.


.. rubric:: **Login to MSU's Training and Password System**
-  Within 3 days of receiving the email, navigate to
   `<https://taps.hpc.msstate.edu>`__

- Authenticate using your username and your temporary
   password.

.. note::
    If your temporary 3-day password has expired, it will need to be reset. See: `Logging In - Reset Password <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in#Password>`__

-  Upon successful login, you will see the **TAPS Home
   page**.

.. rubric:: **Take MSU Security Training**

-  Click on the IT Security "Start training" button.
-  Upon successful completion of the training, you will get
   a confirmation.
-  Go back to the TAPS Home page.

.. rubric:: **Take MSU Insider Threat Training**

-  Click on the Insider Threat "Start training" button. Upon successful completion of the training, you will get
   a confirmation.
-  Go back to the TAPS Home page.

.. rubric:: **Dual-factor authentication and Password Change (User)**

-  Navigate to `TAPS <https://taps.hpc.msstate.edu>`_

.. rubric:: **Setup Dual-factor authentication App**
-  Click on the "Manage Duo and Password" button.
.. rubric:: **Specify Duo Mobile Phone Device**
.. rubric:: **Specify Duo Mobile Phone Number**
.. rubric:: **Specify Duo Phone Type**
.. rubric:: **Install Duo App**
.. rubric:: **Activate Duo App**
.. rubric:: **Change Temporary Password**
.. rubric:: **Password Change Successful**
.. rubric:: **Logout and log back in again**

**Congratulations! Your account is now fully set up and you can login to MSU-HPC.**

.. rubric:: **Account Reactivation**

If your account has expired, you will need to reactivate. To
begin the process, start a Help ticket: `MSU-HPC Help
Request <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.

         
Account Renewal
----------
To keep your MSU account current and active:

-  Log on to the system every 90 days (successful login to
   MSU-HPC or authentication to one of the MSU Account
   Management web pages).
-  Complete yearly password changes and security training
   updates, which are required each January (regardless of
   your **Effective Date**). Users have until the end of
   January to comply, using the online MSU HPC2 Training and
   Password System `TAPS <https://taps.hpc.msstate.edu/>`__,
   otherwise the user account will be locked.
-  Make sure your supervisor renews your Account before the
   Account **Expiration Date**.

If an MSU account is not renewed by the expiration date, the
account will be locked. The **Expiration Date** is set by
the account supervisor when the user account is created or
renewed, and cannot be more than one (1) year from the
**Effective Date**. The user account renewal request can
only be completed by the supervisor of record. If the
supervisor is to be on an extend absence, then the
supervisor should start an Orion help ticket `Orion Help
Requests </index.php/Help_Requests>`__ to assign an new
supervisor so the user may maintain their account during
your absence.

.. note::
  A users Home File System directory
  (/home/userID) is **DELETED** when a user's account is
  deleted. User account deletion can occur any time after a
  user account is scheduled for deletion. User accounts are
  scheduled for deletion 2 weeks after a user accounts
  **Expiration Date** and the account is not renewed. Once
  your HFS data is deleted it will **NOT be recoverable**.
  Project data (/work) is **NOT** deleted when a users
  account is deleted.

.. rubric:: **Renewal Request Email from MSU (Supervisor)**

When an active user's account approaches the **Expiration
Date**, an email will be sent to the supervisor from MSU so
that the supervisor can request a renewal or decide not to
renew the account.

Here is an example of the email:

::

   From: <null@hpc.msstate.edu>
   Date: Thu, Jan 21, 2021 at 8:11 AM
   Subject: HPC-NOAA Computer Account Expiration Notice
   To: <eschnepp@hpc.msstate.edu>

   The external users agreement for Forrest Hobbs will expire on 02/05/21.  If you wish to renew this agreement, please go to: 
   https://intranet.hpc.msstate.edu/services/external_accounts/noaa/requestAccount.php?id=#####&user=fhobbs

   to request a renewal of the agreement.  If you do not wish to renew this agreement, please ignore this email.
   --
   Systems Administration Team
   High Performance Computing Collaboratory
   Mississippi State University
   help@hpc.msstate.edu

If the renewal time has passed, or the initial account
renewal email was missed, request an account renewal `here:
<https://intranet.hpc.msstate.edu/services/external_accounts/noaa/>`_

.. rubric::  **Fill out the NOAA-HPC Computer Account Request Form

-  **Note the Expiration Date in the email.**
-  **Follow the link to open a pre-populated webform.** You
   may be required to provide your MSU login credentials. If
   you don't know your password start an `Orion help
   ticket <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.

-  **Verify the email address:** Change if needed.
-  **Set the Effective Date:** The effective date may
   pre-populate with the current date instead of the
   Expiration Date. Change the Effective Date to be the
   Expiration Date in the email.
-  **Set the new Expiration Date:** This should be set to 1
   year after the new Effective Date (if your Effective Date
   is 02/05/21, the Expiration Date should be 02/05/22),
   unless you want the user account to expire sooner than 1
   year. 1 year is the max allowed by MSU.
-  **Save Request when complete**

| This completes the renewal request. The supervisor should
  consider notifying the user that the renewal request has
  been made so they will be vigilant for an email from MSU.
  MSU will email the user to provide additional information
  and confirm the request.

.. rubric:: **HPC2-NOAA User Account Request Confirmation (User)**

Once the account renewal request has been submitted by the
supervisor, an email similar to the one below will be sent
from MSU directly to the user, asking for additional
information and request confirmation.

::

   From: help@HPC.MsState.Edu <help@HPC.MsState.Edu> 
   Sent: January 21, 2021 13:03
   To: forrest.hobbs@noaa.gov
   Subject: NOAA-HPC Users Agreement confirmation

   A computer account request has been submitted to the the Mississippi State University High Performance Computing Collaboratory (MSU HPC2) by Eric Schnepp on your behalf.  In order to facilitate continued processing of this account request, you must complete the application via the below web address.

   https://www.hpc.msstate.edu/computing/external_accounts/noaa/confirmAccount.php?confCode=XXXXXXXX   

   This request will be removed from the queue if no response is received by 02/04/21.

   For problems related to your computer account request, please reply to this message and provide details of the problem. 

   If you received this email in error, you can simply ignore the email. 
   -- 
   Systems Administration Team
   High Performance Computing Collaboratory Mississippi State University 

   help@hpc.msstate.edu

.. rubric::  **Fill out the HPC2-NOAA User Account Request Confirmation Form
-  **Click on the link provided in the email**
-  **Fill out the form.**

   -  Your password is your current MSU password. If you
      don't know your password start an `Orion help
      ticket <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.
   -  If you have an NOAA RDHPCS account use the same
      Organization, Phone, and Address you use in AIM.
      Otherwise, use your business contact information.

-  **Agree to the terms and conditions, and submit the form.

| The form will then be submitted back to MSU for final
  approval.

-  If the renewal is approved you will not be notified, and
   your access is maintained.

-  If the renewal is denied the supervisor will be notified
   by email.

Managing Portfolios, Projects and Allocation
----------

Role Accounts
----------

Help, Policies, Best Practices, Issues
============

MSU-HPC Help Requests
---------------

Known Issues
------------

Policies and Best Practices
---------------------

Protecting Restricted Data
----------------

User Training and Notifications
-------------------

FAQs
============
