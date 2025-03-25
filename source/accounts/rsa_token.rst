.. _rsa-token:

##########
RSA Tokens
##########

.. |android icon|	image:: /images/rsa_app_android.png
.. |apple icon|		image:: /images/rsa_app_apple.png
.. |fob|		image:: /images/rsa_securid_fob.gif



+--------------+----------------+--------------+
| Hardware fob | Android App    | Apple App    |
+--------------+----------------+--------------+
| |fob|        | |android icon| | |apple icon| |
+--------------+----------------+--------------+

RSA tokens provide multi-factor authentication (MFA) for NOAA RDHPCS
systems. With the widespread adaption of smart phones, it is preferred
that users install the RSA SecurID app on their device.  Hardware
fobs are available on request, but expect a several week lead time.

As part of obtaining a NOAA RDHPCS Account, you will request an RSA
token, and follow the below steps to activate or configure it.

.. attention::

   The token code displayed on the fob or app **is a single use code.**
   Do not re-use a token code; wait for it to change.


RSA Hardware Token Instructions
===============================

If you have been allocated a hardware token, confirm receipt by
opening a helpdesk ticket.  Send an email from your NOAA.gov account
to `rdhpcs.aim.help@noaa.gov <mailto:rdhpcs.aim.help@noaa.gov>`_ Use a
subject of 'First.Last: Enable token' (replace First.Last with your
First Last NOAA username).  Once enabled, proceed with the activation
steps below.

.. _rsa-software-token-user-instructions:

Requesting a new or replacement RSA token
=========================================

New users: Submit the RSA token request form
--------------------------------------------

1. Access the RDHPCS `AIM <https://aim.rdhpcs.noaa.gov>`_ site and follow
the link labeled **Make a request for an RSA token**.  Make sure you are
logged into Google with your NOAA.GOV credentials, and fill out the
form.

.. note::

   If you have problems logging into `AIM`_, you are probably a new or
   returning NOAA user and need to set up the NOAA MFA (Multi Factor
   Authentication).  Please try logging into the `NOAA Staff Directory
   <https://accounts.noaa.gov>`_ and contact your local I/T support
   people if you cannot login.

2. Open an OTRS ticket. Send email to `rdhpcs.aim.help@noaa.gov
<mailto:rdhpcs.aim.help@noaa.gov>`_, with the subject of
'First.Last: Token for new device' (replace
First.Last with your First Last NOAA username).


Current users: Replacement token for a new smart phone
------------------------------------------------------

1. Log into the `RSA User self-service console
   <https://rsauser.boulder.rdhpcs.noaa.gov/console-selfservice/SelfService.do>`_.

.. image:: /images/newrsa1.png

Click **request replacement**. The Request Replacement window displays.

.. image:: /images/newrsa2.png

2. Complete the replacement request.

.. note::

   You can set the RSA pin to the same number you currently use.

Click **Submit Request**. A confirmation window displays.

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

You will need to enter the information
from your approval email into the RSA app. Then, you will go back into Web Tier
to set your PIN.

After the distribution of CTF mode, the SW token is in RSA APP. Log on to the
`RSA User self-service console` with your NOAA ID and the OTP code from
your user email.

.. image:: /images/RSACTF2.png

The PIN Required screen displays.

.. image:: /images/RSACTF3.png

Set and confirm your PIN.
This completes the process. If you have any problems, send email to
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



Scan the QR code
If your token
