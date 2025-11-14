.. _rsa-token:

##########
RSA Tokens
##########

Tokens are no longer supported for RDHPCS system access. Instead,
RDHPCS systems use CAC or YubiKey for Multi Factor Authentication
(MFA) for NOAA Single Sign On (SSO). See the :ref:`Yubikey
Instructions <yubikey-user-instructions>` for information and
instructions.


Requesting a new or replacement RSA token
=========================================

New users: Submit the RSA token request form
--------------------------------------------

 1. Access the RDHPCS `AIM <https://aim.rdhpcs.noaa.gov>`_ site. At the top
    of the page, click the **Requests** tab.
 2. Click **Request an RSA Token**, complete the form and submit it. You will
    be issued a token when you have been fully approved for a functional
    project.

.. note::

   If you have problems logging into `AIM`_, you are probably a new or
   returning NOAA user and need to set up the NOAA MFA (Multi Factor
   Authentication).  Please try logging into the `NOAA Staff Directory
   <https://accounts.noaa.gov>`_ and contact your local I/T support
   people if you cannot login.


Existing users: Replacement token
---------------------------------

  1. Access the RDHPCS `AIM <https://aim.rdhpcs.noaa.gov>`_ site.
     At the top of the page, click the **Requests** tab.

  2. Click **Request an RSA Token**, complete the form and submit it.

  3. Open a helpdesk ticket by sending an email from your NOAA.GOV account
     to `rdhpcs.aim.help@noaa.gov <mailto:rdhpcs.aim.help@noaa.gov>`_,
     with the subject of *First.Last: Token for new device*.
     (Replace First.Last with your First Last NOAA username.)

.. note::

   You can set the RSA pin to the same number you currently use.

You will receive email confirming your request. When the request is approved,
you will receive a second email containing token information.

.. important::

   Follow the instructions on this page, rather than those in the email, to
   activate the token.


Activate your Software Token
----------------------------

1. Log into the `RSA User self-service console
<https://rsauser.boulder.rdhpcs.noaa.gov/console-selfservice/SelfService.do>`_.
The Account display will identify your software token as either CTF or
CT-KIP format. Follow these instructions to activate a
:ref:`software-token-CTF` or :ref:`software-token-CT-KIP`.


.. _software-token-ctf:

CTF Token
^^^^^^^^^
If your token is set up as a CTF format, you'll see this on the RSA user
screen.

.. image:: /images/RSACTF1.png

You will need to enter the information from your approval email into the
RSA app. Then you will go back to the RSA User self-service console to
set your PIN.

After the distribution of CTF mode, the SW token is in RSA APP. Log on to the
`RSA User self-service console` with your NOAA ID and the OTP code from
your user email.

.. image:: /images/RSACTF2.png

The PIN Required screen displays.

.. image:: /images/RSACTF3.png

Set and confirm your PIN.
This completes the process. If you have any problems, send an email to
rdhpcs.aim.help@NOAA.gov to open a Helpdesk ticket.


.. _software-token-ct-kip:

CT-KIP Token
^^^^^^^^^^^^

Log on to the `RSA User self-service console` with your NOAA ID.
The token screen displays.

.. image:: /images/RSAKIP1.png

Click **Activate Your Token**. The Activate your Token screen
displays.

.. image:: /images/RSAKIP1.png

On your personal device, open the RSA app. Scan the QR
code from the display.

This completes the process. If you have any problems, send email to
rdhpcs.aim.help@NOAA.gov to open a Helpdesk ticket.
