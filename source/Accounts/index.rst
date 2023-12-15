.. _Accounts:

########
Accounts
########

New Device - Software tokens
--------
When you acquire a new device, follow this three-step process to add an RSA software token:

#. Submit an OTRS ticket by emailing rdhpcs.aim.help@noaa.gov. Use the subject line: Token for New Device- First.Last.
#. Go to AIM, click on the "Make a request for an RSA token" link, fill out the form, and hit the submit button. When that form is received, you'll receive email that includes a URL and activation code. Open that URL from your device and submit the activation code.
#. When the software token is working on your new phone, delete the token from your old device.


Accessing RDHPCS Systems
--------

First Time RSA token Login
-------
.. note::

   If you are using a PC, please install `PuTTY <https://www.putty.org/>`__ prior to logging in for the first time. Mac and Linux users will user a terminal to login.

After you have been added to your first project, you will need to either 

**RSA software token:** Please follow the instructions contained in
the `RSA Software Token USER Instructions <https://docs.google.com/document/d/1-UMv1K62nQkKS0etbuLsXHZE2KBtjLl0/edit>`__.
**RSA hardware token:** Please submit an OTRS ticket by sending an
email to rdhpcs.aim.help@noaa.gov with the subject line: Enable token.
You will be sent an email once your hardware token has been enabled with
instructions about how to set your token pin.

.. _bastion_login_timeouts:

Bastion Login Timeouts
------

-  Bastion login timeouts are applicable to both bastion types (CAC and
   RSA.)
-  Every Sunday morning all Boulder Bastion sessions will terminate at
   0400 ET (0200 MT).
-  Every Monday morning all Princeton Bastion sessions will terminate at
   0400 ET (0200 MT).

This will not impact batch jobs, cron scripts, screen sessions, remote
desktop, or data transfers of any kind.

.. _accessing_rdhpcs_systems:

Accessing RDHPCS Systems
-----------------------

**READ BEFORE CONTINUING:** Please log onto AIM (using ICAM credentials)
and confirm that ALL your account information is up-to-date. If you
recently were issued a new CAC OR renewed your CAC, please check that
the CAC information in AIM matches your current CAC. For more
information on updating the CAC, please see below.

We currently have four (4) NOAA RDHPCS systems and one external system
available to the user community:

-  Gaea
-  Hera
-  Niagara
-  Jet
-  Orion (MSU - external)

.. _aim_access:

AIM Access
----------
| Access to RDHPCS systems depends on your assigned project(s). To
  request access to a project, please go to: `AIM <https://aim.rdhpcs.noaa.gov>`__

For Orion access, see `Logging Into Orion <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Logging_in>`__

Two options exist for authenticating to RDHPCS (Internal Systems),
CAC/PIV and RSA Token. Additionally, X.509 certificates are used within
RDHPCS to authenticate between resources. The X.509 certificates are
created using a user-defined pass-phrase. A validated certificate stays
valid for a set period of time (30 days). You do not have to re-validate
your certificate every time you login to the system.

.. _common_access_card_cac:

Common Access Card (CAC)
------------------------

.. _cac_login:

CAC Login
---------

| RDHPCS users with a CAC who are logging in from Windows, Mac, or Linux
  workstation/laptop are required to use CAC login.
| Please see CAC instructions here: `CAC Login <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/CAC_Login>`__

.. _updating_or_renewing_cac_information_in_aim:

Updating or Renewing CAC Information in AIM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**NEW as of July 2018**: AIM uses the new NOAA single user sign-on -
please proceed through the prompts and sign in with your NEMS
credentials as before:

|aim_single_sign_on.png| |aim_single_sign_on_portal.png|

.. _aim___auto_update_of_cac_entry:

AIM - Auto-update of CAC Entry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IMPACTS: ONLY RDHPCS Users with a NOAA-issued CAC.

RDHPCS Account Management has worked to make improvements in the
function to collect CAC-related information from each user within AIM.
Recent updates to AIM now allow automatic detection and update of
CAC-related information to your respective AIM record. Previously,
RDHPCS users had to manually update their CAC.

RDHPCS Account Management is requesting that you log into AIM to update
your CAC information. Please navigate to the AIM website:
https://aim.rdhpcs.noaa.gov and authenticate via SSO using your CAC.
Please note that you might not always be asked to authenticate with CAC
when logging onto the AIM site.

When you enter the site, the “Updated CAC detected. Information Updated”
message appears at the top of your screen if your CAC needs to be
updated.

.. note::

   If your CAC does not need to be updated, you will not receive this message. It might be worth noting, if your current CAC was updated within AIM or if users do not have a CAC they will not experience this event.

If you experience any issues or have questions, please contact:
rdhpcs.aim.help@noaa.gov

After your CAC has been updated, the AIM home page will appear and in
the upper lefthand corner, you will see the message, “Current CAC cn
detected.”

.. figure:: new_cac_login.png
   :alt: new_cac_login.png
   :width: 500px

NOTE: With current CAC information on file, you should be authenticating
into RDHPCS with CAC as your primary means. If you need assistance with
authenticating via CAC, please visit: `CAC
Login <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/CAC_Login>`__

.. _rsa_token:

RSA Token
-------

.. _rsa_token_login:

RSA Token Login
---------------

| RDHPCS users without a CAC will continue to log in via their current
  RSA token. Alternatively, any RDHPCS user who has a CAC but is having
  problems with their login via CAC, is authorized to login via RSA
  token while they work through their technical issues.
| Please see instructions here: `RSA Token
  Login <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/RSA_Login>`__

.. _rsa_hardware_token_activation:

RSA Hardware Token Activation
-----------------------------

RSA Hardware token activation, please go here: `RSA Token
Activation <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/New_User_Activation#RSA_Token_Activation>`__

.. _rsa_software_token_instructions:

RSA Software Token Instructions
-------------------------------

-  **For new users**: You will be issued a token when you are assigned
   to your first project. The type of token will be determined by you
   when you fill out the token form.
-  **For existing software token holders**: Your current software token
   cannot be transferred to another device. When you acquire a new
   device, you will be issued a replacement token for that device.
   Please follow the guidance on this wiki under the title, "New Device-
   Software Tokens."

.. _other_authentications:

Other Authentications
---------------------

Your current RSA token will be used for all other RDHPCS authentications
(sudo to role accounts, attended data transfers, x2go, etc…)

.. _new_device___software_tokens:

New Device - Software Tokens
--------------------------------

When you acquire a new device that your software token will be stored
on, there is a three step process.

#. Submit an OTRS ticket by emailing
**rdhpcs.aim.help@noaa.gov**. In the email subject line, please type:
**Token for New Device- First.Last**.

#. Go to `AIM <https://aim.rdhpcs.noaa.gov/>`__, click on the
"Make a request for an RSA token" link, fill out the form, and hit the
submit button.

#.  Delete the token from your old device.

.. |aim_single_sign_on.png| image:: aim_single_sign_on.png
   :width: 500px
.. |aim_single_sign_on_portal.png| image:: aim_single_sign_on_portal.png
   :width: 500px


--------
Suspension, Deactivation, Reactivation
--------
text

--------
Role Accounts
--------
text text

-------
Request Additional Projects=
---------
test test

---------
Resetting Master Certificate Passphrase
---------
Use it or lose it


