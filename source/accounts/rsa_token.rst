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

RSA tokens provide multi factor authentication (MFA) for NOAA RDHPCS
systems. With the widespread adaption of smart phones, it is preferred
that users install the RSA SecurID app on their device.  Hardware
fobs are available on request, but expect a several week lead time.

As part of obtaining a NOAA RDHPCS Acount, you will request an RSA
token, and follow the below steps to activate or configure it.

.. attention::

   The token code displayed on the fob or app **is a single use code.**
   Do not re-use a token code; wait for it to change.


Regardless of RSA type, your first step is to fill out a form.


Requesting a new or replacement RSA token
=========================================

New users: submit the RSA token request form
---------------------------------------------

Access the RDHPCS `AIM <https://aim.rdhpcs.noaa.gov>`_ site and follow
the link labeled "Make a request for an RSA token".  Make sure you are
logged into Google with your NOAA.GOV credentials, and fill out the
form.

.. note::

   If you have problems logging into `AIM`_, you are probably a new or
   returning NOAA user and need to set up the NOAA MFA (Multi Factor
   Authentication).  Please try logging into the `NOAA Staff Directory
   <https://accounts.noaa.gov>`_ and contact your local I/T support
   people if you cannot login.


Current users: Replacement token for a new smart phone
------------------------------------------------------

Send an email from your NOAA.gov account to `rdhpcs.aim.help@noaa.gov
<mailto:rdhpcs.aim.help@noaa.gov>`_ requesting a new RSA activation
URL.  Use a subject of 'First.Last: Token for new device' (replace
First.Last with your First Last NOAA username).Wait for responses to
your helpdesk ticket, then proceed.

RSA Hardware Token Instructions
===============================

If you have been allocated a hardware token, confirm receipt by
opening a helpdesk ticket.  Send an email from your NOAA.gov account
to `rdhpcs.aim.help@noaa.gov <mailto:rdhpcs.aim.help@noaa.gov>`_ Use a
subject of 'First.Last: Enable token' (replace First.Last with your
First Last NOAA username).  Once enabled, proceed with the activation
steps below.

.. _rsa-software-token-user-instructions:


RSA Software Token Instructions
===============================

.. attention::

   Users are allowed *one* RSA token.  Choose one mobile platform --
   Apple or Android -- to use your RSA soft token on.

.. attention::

   You **cannot reuse** an authentication token or URL.  If you get a
   new mobile device, see the above section.


Before proceeding, you must have an email from the RDHPCS Accounts
Team that provides the activation URL.  Forward that email or URL to
your smart phone.

.. attention:: The activation URL is only good for seven (7) days!

Step 1: Install the application
-------------------------------

.. hint::

   If you already have the RSA application installed on your device,
   do not install it again.  You only need to add a token by using the
   “+” in the app.

Use these links to install the app on your mobile device.  If you
cannot use the links, search the app store for "RSA Authenticator".
The app icons will look like these:

.. |android url|	replace:: https://play.google.com/store/apps/details?id=com.rsa.securidapp&hl=en_US
.. |mac url|		replace:: https://apps.apple.com/us/app/rsa-authenticator-securid/id318038618



+--------------+----------------+--------------------------------+
| Type         | Link           | Icon                           |
+==============+================+================================+
| Android      |  |android url| | |android icon|                 |
+--------------+----------------+--------------------------------+
| iPhone, iPad |  |mac url|     | |android icon| or |apple icon| |
+--------------+----------------+--------------------------------+


Step 2: Click the activation URL
--------------------------------

.. attention::

   If at all possible, read or forward the "RDHPCS Software Token
   Activation" email to your mobile device so the activation URL can
   be copy and pasted.  It is permitted to forward that email to a
   personal address for the purposes of RSA activation.


As of mid 2024, it should be possible on both Apple and Android
platforms to simply click on the Activation URL in the email.


Once the RSA credential has been imported, you will want to rename it
from the default name of "SecurID OTP Credential".  Use the ``...``
menu to select ``Rename`` and rename the credential to "NOAA-RDHPCS"


Alternate Step 2: Manually enter the activation URL
---------------------------------------------------

If clicking on the URL does not work, select and copy the Activation
URL.

.. important::

   **COPY THE ENTIRE ACTIVATION URL**

- On your mobile device, open the RSA application.

- Click on the **+** in the upper right corner

- Click the 'Registration Code or URL' field

- Paste, or type in, the activation URL.  **Make sure the URL starts
  with https://authenticator.securid.com/securid/ctf/**

.. |android fillin|     image:: /images/rsa_android_fillin.png
        :scale: 30 %
        :alt: Android (new) fillin
.. |apple fillin|       image:: /images/rsa_apple_fillin.png
        :scale: 60 %
        :alt: Apple fillin
.. |popup activation|   image:: /images/rsa_popup_activation_code.png
        :scale: 30 %


Refer to this screenshot:

 |android fillin|

.. attention::

   **Leave the email and organization fields blank!!**

You have filled in the URL field **and the email and organization
fields are blank.**

- The **Submit** button should now be active.  Click it.

Now proceed with the below activation steps.




RSA Activation
==============

Step 3: RSA Activation and PIN setting
--------------------------------------

When you have just configured your RSA soft token, or have just
confirmed receipt of your RSA hardware token (fob), it will be
inactive.  Follow these steps to activate your RSA token:

#. Access the `RDHPCS SSLVPN <https://sslvpn.rdhpcs.noaa.gov/>`_
#. Enter your username; the "First.Last" portion of your NOAA email
   address.
#. For the password, enter the 6-digit code shown on the fob.
#. Follow the prompts to set a PIN. Use 4 to 8 alphanumeric characters.
#. Confirm the PIN by re-entering it.
#. Once complete, you may close that browser window.

.. note::

   Do remember your PIN.  When you are asked to enter your RSA
   passcode, you will enter your PIN followed by the 8 digit number
   displayed in the RSA app on your mobile device.


.. attention::

   The token code displayed on the fob or app **is a single use code.**
   Do not re-use a token code; wait for it to change.


Step 4: Success!  Mark helpdesk ticket as completed
---------------------------------------------------

You have now activated your NOAA RDHPCS RSA token. **Reply to the
helpdesk ticket confirming success.** You may now proceed with
accessing the desired HPCS resources.


