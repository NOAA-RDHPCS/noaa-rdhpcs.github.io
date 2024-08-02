.. _accessing_rdhpcs_systems:

************************
Accessing RDHPCS Systems
************************


.. _aim_access:

Access and Identity Management (AIM)
------------------------------------

Access to RDHPCS systems depends on your assigned project(s). Access
to projects is managed in the Access and Identity Management (`AIM
<https://aim.rdhpcs.noaa.gov>`_) software. Users can use AIM to request
access to a project. AIM uses the NOAA single sign-on (SSO) for
authentication. Proceed through the prompts and sign in with your NEMS
credentials.

For access to the MSU HPC systems, please review the :ref:`MSU-HPC
<MSU-HPC-user-guide>` document pages.


Secure Shell (SSH) Access
-------------------------

Access to all RDHPCS compute resources is done using the Secure Shell
(SSH) protocol to one of the system's bastions, using either CAC/PIV
or RSA multi-factor authentication (MFA) options. Additionally the
RDHPCS program uses `X.509 certificates
<https://en.wikipedia.org/wiki/X.509>`__ to authenticate between
resources. A master X.509 certificate is created on a user's initial
login to an RDHPCS system usinga user-defined pass-phrase.  Once
validated, the master X.509 certificate remains valid for one year.
At each successive log in, a new thirty-day certificate is created.
This thriy-day certifiate can be used to initiate password-less access
to other RDHPCS resources.  A typical use of this thirty-day
certificate is to transfer data files between RDHPCS resources.


.. _common_access_card:

Common Access Card (CAC)
========================

RDHPCS users eligible to obtain a Common Access Card (CAC) are
required to use CAC login.  RDHPCS has chosen the :ref:`Tectia SSH
client <Tectia>` for CAC authentication to the RDHPCS compute system.
Please refer to the :ref:`Tectia` pages for details and configuration
instructions.

.. _updating_cac_information_in_aim:

Updating CAC Information in AIM
-------------------------------

.. note::

   This only works for RDHPCS Users with a NOAA-issued CAC.

RDHPCS Account Management collects CAC-related information from each
user in AIM.  AIM automatically detects and updates CAC-related
information to your AIM record.  To allow this, you must log into
AIM using your CAC.

When you enter AIM, the message,
**Updated CAC detected. Information
Updated**, will appear at the top of the screen if your CAC needs to be
updated.

.. image:: /images/AIM_CAC_passed_in.png
   :scale: 50%
   :align: right
   :alt: Sample image showing the CAC login information

After the CAC information is updated, and when you log into AIM with
your CAC, a message displaying the CAC ID will be displayed, as shown
on the right.

Please open a :ref:`help desk ticket <getting_help>` if you have
issues or questions.

.. note::

   With current CAC information on file, you should authenticate into RDHPCS
   with CAC as your primary means. If you need assistance with authenticating
   via CAC, please see: :ref:`common-access`.


.. _rsa_token:

RSA Token
=========

RDHPCS users without a CAC will log in using their current RSA token.
Alternatively, any RDHPCS user who has a CAC but is having problems
with their login via CAC, is authorized to login via RSA token while
they work through their technical issues.

After you have been added to your first project, you will need to
either initialize your RSA software token or enable your hardware
token.

For best use of resources and availability, the preferred approach is
to install the SecurID app on a smart phone for token generation.
Hardware tokens are available on request.

RSA Software Token Activation
-----------------------------

#. Email rdhpcs.aim.help@noaa.gov to open an OTRS ticket. Use the
   subject line: Token for New Device - First.Last.
#. Go to `AIM`_. Click **Make a request
   for an RSA token**, fill out the form and submit. When that form is
   received, you'll receive an email that will include a URL with
   instructions about how to activate and import your software token.

.. _new_device_software_tokens:

New Device
----------

When you acquire a new device, follow this process to add an RSA
software token:

#. Email rdhpcs.aim.help@noaa.gov to open an OTRS ticket. Use the subject
line: Token for New Device - First.Last.
#. Go to `AIM`_.  Click **Make a request for an
RSA token**, fill out the form, submit. When that form is received,
you'll receive an email with instructions about how to activate and
import your software token.
#. Copy and paste the URL from the email
using your device and submit the activation code.
#. When the software
token is working on your new phone, delete the token from your old
device.


.. _rsa_hardware_token_activation:

RSA Hardware Token Activation
-----------------------------

Submit an OTRS ticket by sending an email to rdhpcs.aim.help@noaa.gov,
using **Enable token** as the subject. You will receive a return email
with instructions about how to set your pin and login with it.

.. _other_authentications:

Other Authentications
---------------------

Your current RSA token will be used for all other RDHPCS authentications
(sudo to role accounts, attended data transfers, x2go, etc…)


.. _account_suspension_deactivation_reactivation:

Account Suspension, Deactivation, Reactivation
==============================================

A user's account is suspended when it has been inactive for over 90
days. The user will be notified when their account has been suspended.
To re-activate your account, submit an OTRS ticket by sending an email to
rdhpcs.aim.help@noaa.gov with the subject **Reactivate User.Name**. You
will be notified when your account has been reactivated. A reactivated
user maintains access to all projects.

Depending on the lengh of account suspension, there may be additional
steps to fully reactivate your account:

.. topic:: Reactivate within seven days

   If you reactivate your account within seven days, your token is
   re-enabled at the same time. Once your account and token are
   re-enabled, you may log into your respective resource and project.

.. topic:: Reactivate after seven days

   If your account has been suspended for more than seven days and you
   had a software token, you must apply for a new token. To do this, visit `AIM`_
   and select **Make a Request for an
   RSA Token**. Complete the form and Submit.

   Once your account has been reactivated and your token has been
   re-enabled, you will be required to set a new PIN only if you have
   a software token. After you complete this process, you will be
   required to log into your respective resource and project.

Deactivated Accounts
--------------------

If your account remains suspended for more than 270 days, it will be
deactivated. If your account is deactivated and you would like it
reactivated, you will need to go to `AIM`_ and apply for the rdhpcs
project to begin the vetting process again. When you arrive at the AIM
website, click  the **Request new access to a project** link. When you
are fully approved for the rdhpcs project, you will be emailed further
instructions.

Use AIM to apply for the rdhpcs project. Click **Request new
access to a project**. When you are fully approved for the rdhpcs
project, you will be emailed further instructions.

.. Note::

   Deactivation will reset your default shell to ``/bin/bash``.  If
   you wish it to be anything else, log into AIM, click on the *View
   your information in the system, update the Sponsoring
   Organization*. Scroll down to the section that displays your
   Default shell and change it, then scroll down to the bottom of the
   page and hit the *Submit changes* button.


.. _role_accounts:

Role Accounts
=============

A role account is a user account shared with one or more users as
members, such that all group members share the account equally via the
use of `sudo`, typically for the unified use of a project. Role
accounts must have a name that reflects their project association or
function. All changes to a role account must be submitted by the role
account Principal Investigator (PI) via OTRS ticket. Send email to
rdhpcs.aim.help@noaa.gov with the subject line: Role account changes -
first.last (role account name).

Accessing a Role Account
------------------------

You can access any role account if you are a member of the account.
Use sudo with your RSA token to gain access. For example:

 .. code-block:: shell

   jsmith# sudo su - roleuser
   Access is via First.Last username only. Enter RSA PASSCODE:
   bash-4.1$ whoami
   roleuser

Your RSA passcode is your PIN+Token code.

X Applications With Role Accounts
---------------------------------

If you are planning to use X utilities with role accounts, you should
use the xsudo utility to switch to the role account instead of using
the "sudo" command directly. You need to explicitly set the DISPLAY
environment variable after doing the xsudo to the role account. So for
example, if you want to use role.rap-chem role account and would like
the ability to use X applications:

1. Note the ``DISPLAY`` environment variable in your current session
   before doing the xsudo to the role account:

.. code-block:: shell

   $ echo $DISPLAY

2. Use the ``xsudo`` command to switch to the role account:

.. code-block:: shell

   $ xsudo role.rap-chem

3. Set the ``DISPLAY`` environment variable to the value you obtained
   above just before doing ``xsudo``.

   .. tab-set::

      .. tab-item:: bash

         .. code-block:: shell

            $ export DISPLAY=localhost:14.0

      .. tab-item:: csh

         .. code-block:: shell

            $ setenv DISPLAY localhost:14.0

This will enable your X applications.

Using CRON
----------

Since Role accounts are  shared by multiple users in a project, the
project members need a way to know which member is responsible for
which section of the cron entries. The person responsible for the
section of a cron entry of a role account should use the following
guidelines:

At the beginning of the section:

- Add a comment about the who is adding these cron entries
- Add a comment about when this entry was added
- Add a comment about an end date if applicable
- Add other comments as needed to document the purpose
- Add a ``MAILTO=First.Last@noaa.gov`` at the beginning of the section
- Add a ``MAILTO=`` at the end of the section so that whoever is
  responsible for the next section sets their own MAILTO filed.

.. note::

   Without the ``MAILTO`` directive, any errors/logs from the cron
   commands end up getting lost and one may never know there was a
   problem/failure!

***************************
Request Additional Projects
***************************

These are instructions for current RDHPCS users on an active project
who need to request access to an additional project resource on Jet,
Hera, Gaea, Niagara, or any Cloud project.

#. Go to AIM.
#. Select *Request new access to a project*.
#. Select the project from the dropdown list. Note that system access
   (Jet/Hera/Gaea/Niagara) is determined by project.
#. Add justification for requesting project access
#. Submit the request

Approvals needed: PI, HR, ISSO

Your request will automatically be approved from the HR and ISSO roles
because you are a current user. You'll need actual approval from the
PI of the project. Once that approval is submitted, your request will
be considered fully approved and various admins will configure your
access to the project. Once that is done, you will receive an approval
email from Account Management and you will be able to access the
project.


.. note::

   If you have been advised to apply for a project that is not listed in
   AIM, first verify the project name with your Project team. If the
   project name is correct, email rdhpcs.aim.help@NOAA.gov to contact
   the Account Management team for assistance.

   If you have further questions, send email to rdhpcs.aim.help@noaa.gov
   for assistance.


*************************
RDHPCS X.509 Certificates
*************************

When a user first logs into a R&D HPC system, a one-year master
certificate must be generated. On the next login, after the master
certificate is signed, a 30-day proxy certificate is generated. Every
future login renews the 30-day proxy certificate.

.. topic:: Master Certificate

   The master certificate is valid across all bastions, for one year
   from date of creation. After one year the master certificate will
   need to be renewed. When it expires, any related proxy
   certificate expires as well.

.. topic:: Proxy Certificate

   The proxy certificate is local to each bastion, is valid for 30
   days and is renewed every time you login to each bastion. If you do
   not log in at least once every 30 days, you may be prompted to
   enter your master certificate passphrase To renew your certificate,
   you will have to log in to the bastion and enter your master
   certificate passphrase. This will renew the proxy certificate, as
   usual, for 30 days.

   The proxy certificate is local to each bastion, is valid for 30
   days and is renewed every time you login to each bastion. If you do
   not log in a bastion at least once every 30 days, you will be
   prompted to enter your master certificate passphrase and then wait
   for your certificate to be signed. The certificate is valid across
   all bastions.  For example, if you have access to Hera and Jet, and
   renew your certificate by logging into Hera, it will also be
   renewed on Jet as well. This will renew the proxy certificate for
   30 days. However, when you log into Jet, you may be asked to enter
   your master certificate passphrase, but you will not have to wait
   for your certificate to be signed again.


Generating a Master Certificate
-------------------------------

1. Prepare your Master Certificate Passphrase

   A passphrase must consist of at least three separate words and be
   at least 30 characters in length.

   You will be prompted for your Master Certificate Passphrase from
   time to time. Therefore, your certificate passphrase should be
   something you can remember. For example: "G0 Down The 4lley & Yell
   Fi$h ." Notice that this passphrase is made more complex by the use
   of numbers in place of look-alike letters and the use or omission
   of spaces.

2. Create your Passphrase

   Log into the system with your username (First.Last). The system will
   prompt you to create your master certificate passphrase. Your
   master certificate must be signed by the system before further
   access is allowed. This takes approximately fifteen minutes. You
   will receive an email stating that your certificate has been
   signed. After you receive the notification, please wait one hour
   before attempting to sign on to any resource. Following the waiting
   period, login with your username (First.Last) as usual.

   You will be prompted for your master certificate passphrase. Enter
   the passphrase that you created with your master certificate, and
   your proxy will be renewed. After this step, you will only need
   your master certificate passphrase if your proxy completely expires
   (after 30 days).

Resetting Master Certificate Passphrase
---------------------------------------

.. note::

   You will have to renew your Master Certificate annually. About a
   month before it expires, you will be prompted to renew your master
   certificate, with a Y/N option. When you renew the master
   certificate, you may have to wait for one day before you can log in
   again. Plan ahead for a time when you can be offline for up to a
   day, and choose that time to renew the Master Certificate.

If you do not remember your Master Certificate passphrase, it can be
reset. First check the guidance in the Prepare your Master Certificate
Passphrase section, and choose an appropriate passphrase. Then follow
the instructions below:

Hit Enter 4 times. The system will ask: "Have you forgotten your
master certificate passphrase?" Answer "Yes". Answer the questions,
then enter the new master certificate passphrase at the prompt. Once
the new master certificate has been created, it will automatically be
signed by the system. You will receive an email, confirming that the
certificate has been signed. Wait for an hour, then sign into the
system. When you are prompted for the Master Certificate passphrase,
enter your new passphrase.

If you have further issues, submit an RDHPCS help ticket. Send an
email to rdhpcs.aim.help@noaa.gov with the subject Master Certificate
Passphrase.

************************
Quickstart for New Users
************************


Getting Access
--------------

This figure is an overview of the timeline and process for system
access.

.. image:: /images/access1.png

Once you have a NOAA.gov email address, you can request an RDHPCS
account through the Account Information Managment system, AIM. Visit
the Account Information Management (`AIM`_) website and request
access to the RDHPCS project.  Log into AIM using your NOAA email
credentials, review your profile for accuracy, and request the RDHPCS
project.

.. image:: /images/AIM2.png

Once this request is approved, you will receive an email containing
instructions about your next steps. These include requesting access to
further projects and completing the RSA token request form.  Confer
with your supervisor and colleagues to identify the  project(s) to
request.

.. _RSA-software-token:

RSA Software Token
------------------

RSA software tokens provide two factor authentication (2FA) for NOAA
RDHPCS systems for SSH access. When you’re assigned to your first
project, the RSA token form will be used to assign your software
token. Your RSA token will include instructions about how to
initialize it. You can find more information at
:ref:`rsa-software-token-user-instructions`.`

.. NOTE::

     While RSA software tokens are preferred, if you don’t have a
     smartphone you can request an RSA hardware token. The activation
     process is found at :ref:`rsa_hardware_token_activation`.


Accessing the RDHPCS Systems
============================

The Common Access Card (CAC), is the preferred means of access to
RDHPCS resources for both Web and SSH access. To obtain a CAC, work
with your local admin services team as they need to start the
application process.  Some labs can issue CACs on-site, otherwise you
will have to visit a RAPIDS site. The site locator website is `ID Card
Office Online <https://idco.dmdc.osd.mil/idco/>`_.
SSH logins with a CAC require additional software.

.. NOTE::

   To access a system, you must be on a project assigned to that system.

**Cloud Computing**

The Cloud Platform allows RDHPCS users to create a high-performance
computational cluster on a cloud-based platform (AWS, Azure or GCP)
with resources that are appropriate for specific processing tasks.
Cloud access is mediated through the `NOAA Parallel Works application
<https://noaa.parallel.works>`__.

MSU systems (Orion, Hercules) are accessed via SSH or OpenOnDemand.
See MSUHPC :ref:`MSUHPC-logging-in` for detailed instructions.


On-Premises RDHPCS systems (Gaea, Hera, Jet, Niagara, PPAN) are
accessed via SSH.  See the RSA and CAC login sections for further
information.

Tectia SSH solution
-------------------

RDHPCS users with a CAC who are logging in from a Windows, Mac, or
Linux workstation/laptop are required to use CAC login. Access to
RDHPCS resources via CAC requires a CAC reader and necessary software.
The Tectia SSH Client software has been selected to meet the remote
CAC login requirements for the RDHPCS program. Two licenses have been
purchased for each RDHPCS user.

The following features are supported:

* Port forwarding
* X11 tunneling

Access to RDHPCS Systems from a system which cannot directly access a
user's CAC is not supported.

Tectia Initial Setup procedure
------------------------------
Host names for the CAC Bastion Server in Boulder, CO:

.. code:: shell

   bastion-jet.boulder.rdhpcs.noaa.gov
   bastion-hera.boulder.rdhpcs.noaa.gov
   bastion-niagara.boulder.rdhpcs.noaa.gov
   bastion-gaea.boulder.rdhpcs.noaa.gov

Host names for the CAC Bastion Server in Princeton, NJ:

.. code:: shell

   bastion-jet.princeton.rdhpcs.noaa.gov
   bastion-hera.princeton.rdhpcs.noaa.gov
   bastion-niagara.princeton.rdhpcs.noaa.gov
   bastion-gaea.princeton.rdhpcs.noaa.gov


The following OS-specific sections (Windows, Linux, MAC) describe how
to do the following:

* Download the Tectia software
* Install the Tectia software on your local laptop or workstation
* Install the license file on your local laptop or workstation
* Configure the Tectia software
* Use the client software to connect to R&amp;D HPC Systems
* Set up port tunneling


See the :ref:`Tectia` pages for complete information.

MSU systems (Orion, Hercules) are accessed via SSH or OpenOnDemand.
See MSU-HPC :ref:`MSUHPC-logging-in` for instructions.

On-Premises RDHPCS systems (Gaea, Hera, Jet, Niagara, PPAN) are
accessed via SSH.

.. _Common-access:

Common Access Card (CAC) Login
==============================

Tectia SSH Client software has been selected to meet the remote CAC
login requirements for the RDHPCS program. Two licenses have been
purchased for each RDHPCS user (if you currently have an RDHPCS RSA
token).

The following features are supported:

* Port forwarding
* X11 tunneling

Access to RDHPCS Systems is not supported from a system which does not
have the ability to access a user's CAC directly.

RDHPCS users with a CAC who are logging in from a Windows, Mac, or
Linux workstation/laptop are required to use CAC login. This requires
a CAC reader and necessary software. If you recently were issued a new
CAC or renewed your CAC, please check that the CAC information in AIM
matches your current CAC.

Tectia Initial Setup Procedures
-------------------------------

Host names for the CAC bastion Server in Boulder, CO:

.. code:: shell

   bastion-jet.boulder.rdhpcs.noaa.gov
   bastion-hera.boulder.rdhpcs.noaa.gov
   bastion-niagara.boulder.rdhpcs.noaa.gov
   bastion-gaea.boulder.rdhpcs.noaa.gov

Host names for the CAC Bastion Server in Princeton, NJ:

.. code:: shell

   bastion-jet.princeton.rdhpcs.noaa.gov
   bastion-hera.princeton.rdhpcs.noaa.gov
   bastion-niagara.princeton.rdhpcs.noaa.gov
   bastion-gaea.princeton.rdhpcs.noaa.gov

The Tectia pages (Windows, Linux, MAC) describe how to do the following:

   * Download the Tectia software
   * Install the Tectia software on your local laptop or workstation
   * Install the license file on your local laptop or workstation
   * Configure the Tectia software
   * Use the client software to connect to R&amp;D HPC Systems
   * Set up port tunneling


Role Accounts
-------------

A role account is a user account shared with one or more users as
members. All group members share the account equally via the use of
`sudo`, typically for the unified use of a project. The role accounts
name should reflects their project association or function.

You can access any role account if you are a member of the account.
Use sudo with your RSA token to gain access.

Any changes to a role account must be submitted by the role account
Principal Investigator (PI) via OTRS ticket. Send email to
rdhpcs.aim.help@noaa.gov with the subject line: Role account changes -
first.last (role account name).

**************************
First Time RSA token Login
**************************

.. note::

      If you are using a PC, install `PuTTY
      <https://www.putty.org/>`__ prior to logging in for the first
      time. Mac and Linux users will user a terminal to login.

After you have been added to your first project, you will need to
either initialize your RSA software token or enable your hardware
token.

**RSA software token:** Please follow the instructions contained in
the :ref:`RSA-software-token` User Instructions.

.. _RSA-hardware-token:

**RSA hardware token:** Submit an OTRS ticket to obtain a hardware
token. Send an email to rdhpcs.aim.help@noaa.gov using the subject
line: Enable token. You will be sent an email once your hardware token
has been enabled with instructions about how to set your token pin.


**********************************************
Overview: Getting an Internal Account - RDHPCS
**********************************************

The following steps must be completed before you receive an RDHPCS
account.


1. Security Investigation: An inquiry into a person's identifiable
   character traits and conduct. You must undergo the appropriate type
   of suitability check/security including

   - favorable background investigation, with an FBI fingerprint check
   - Department of Commerce public trust security investigation. This
     can take 6-12 weeks

2. Obtain a valid @noaa.gov email address your NOAA IT department you
   are associated with. Use your NOAA email address to communicate
   regarding all NOAA issues. Note that you may have a NOAA email
   account prior to concluding the security review.

3. NOAA IT Security Awareness Training: An annual MANDATORY
   requirement for all NOAA employees, contractors, and temporary
   personnel.

4. RDHPCS Account Request: Request Access to vetting project RDHPCS.

   - Navigate to `AIM`_ and submit a request to be added as a New User to
     the RDHPCS (vetting) project.  RDHPCS is an AIM-only project to
     verify account details.
   - Once you have been approved for vetting project RDHPCS, request
     membership to the project(s)as direced by your PI(s) or PfM(s).

5. Request a RSA token.

   - Once you are fully approved you will receive an email with
     directions to initialize your RSA token and log on.

Currently AIM manages and maintains the following functionality on
Niagara, Gaea,Hera, and Jet RDHPCS compute resources:

*  user information.
*  project information and membership.
*  role account information and membership.


***********************************************
Overview: Getting an External Account - MSU-HPC
***********************************************

The Hercules and Orion systems comprise MSU-HPC, managed by
Mississippi State University. Follow these steps to get an Account for
MSU-HPC.



General Access Requirements
---------------------------

-  All users, regardless of citizenship, follow the same process to
   receive MSU-HPC access.
-  NOAA's RDHPCS users will need to use MSU’s HPC Account Management
   System and Process. RDHPCS Portfolio Managers have access to MSU's
   Account Management Tool.
-  The PfM must have allocations to use the MSU-HPC system.
-  MSU's Account Management system requires user authentication. PIs
   and Portfolio Managers must maintain an active MSU account to
   manage their projects online.

 .. note::

   The designated PI or Portfolio Manager (PfM) must request that a
   MSU user account be created and the user assigned to their project.


Complete the following steps for MSU-HPC access.

- Collaborate with a NOAA research lab and be associated with an
  active NOAA research project. Each project has an assigned Principal
  Investigator (PI) who is responsible for the project and the project
  members. The PI or PfM requests both project assignment and account
  creation.
- New user completes NOAA account request form.
- New user receives an email from MSU to change password, complete
  required training, and setup the Duo dual-factor authentication.
- Within three days, the user changes their password.
- The user completes required training.
- The user sets up the Duo App on their device.

The User now has login access to MSU-HPC.

.. note::

   A Portfolio Manager or PI who loses MSU account access must issue a
   help request. Send email to rdhpcs.orion.help@noaa.gov to open an
   OTRS ticket. A new user who has any issues with completing MSU
   process, should send email to rdhpcs.orion.help@noaa.gov to open a
   help ticket.

