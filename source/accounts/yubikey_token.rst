.. _yubikey-user-instructions:

Yubikey
=======

.. _configure_yubikey:

Configuring Yubikey for the NOAA RDHPCS
---------------------------------------

A Yubikey is an “electronic physical keyring” that is plugged into an
available USB slot on your computer. Like a keyring, a Yubikey holds
(stores) several sets of keys (authentication tokens and
certificates), and helps prevent the compromise of accounts used to
access computers, networks and web applications by requiring the
physical possession of a key for successful login.

.. image:: /images/yubi-usbac.png
   :align: center

.. important::

   As of **October 1, 2025** Yubikey or CAC will be required to
   access the NOAA RDHPCS.  Contact your security office to request a
   Yubikey.

Please note that even though either CAC or Yubikey may be used for
RDHPCS logins,
the following services will **require** the use of Yubikey
for authentication as CAC authentication is not
supported for these services:

* Authenticating to role accounts
* Authenticating to “trusted” and “untrusted” DTNs for doing data transfers
* Authenticating to Globus for doing data transfers
* Authenticating when doing data transfers using the port tunnelling method

Yubikey Registration
--------------------

.. important::

   Once you have followed these registrations instructions, you will
   be using your Yubikey to authenticate into the RDHPCS.  **Your RSA
   token will no longer work.**

The NOAA Yubikey is issued by your security office.

**If you do not have a NOAA issued Yubikey, contact your local I/T
staff, your primary email admin, or your security office.**

If you do not know *any* of those details, start by contacting your
mail admin.  Log into the `NOAA Staff Directory
<https://nsd.rdc.noaa.gov/member/details>`_.  Click your name on
the right hand side, then click **View my Info**.  Click the link
**Primary Mail Admin** to send an email to your mail admin to start your
Yubikey request.

You must register your NOAA issued Yubikey for use with your NOAA
accounts at https://accounts.noaa.gov, **and** follow the additional
steps below to configure and register your Yubikey for RDHPCS use.

.. note::

   If you have lost your NOAA issued Yubikey and have a replacement
   Yubikey, you will need to delete the lost Yubikey at the
   `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_.

**These steps create a** *new* **token on your Yubikey in** *Slot 2*,
**the** *Long Press* **slot.  It is separate and different from the**
*Short Press* **you have been using.**

.. note::

   A *Long Press* means touch **and hold for three (3) seconds.**


Follow these steps to configure **Long Press Slot 2** with a **Yubico
OTP** credential.  You can safely restart these instructions and
re-register the *Yubico OTP* credential **in Long Press Slot 2**:

1. You must have registered your NOAA issued Yubikey at
   https://accounts.noaa.gov.  Navigate to your `NOAA Accounts profile
   page
   <https://accounts.noaa.gov/enduser/?realm=noaa-online#/profile>`_
   and check **MFA Enrollment** for a green checkmark and **Yubikey
   registered** confirmation.

.. image:: /images/noaa-accounts-profile.png
        :scale: 70%

.. important::

   DO NOT PROCEED until you have registered your NOAA issued Yubikey
   at https://accounts.noaa.gov.

2. Download and install the `Yubico Authenticator <https://www.yubico.com/products/yubico-authenticator/>`_.

.. note::

   If you are working on a Government Provided System (Government
   Furnished Equipment (GFE)), you will need to request a software
   installation from your local I/T office.  You may find it simpler
   and easier to use a personal computer for the following steps.

3. Insert your NOAA issued Yubikey into an available USB slot.

4. For Windows or Mac systems, follow the steps below using the
   **Yubico Authenticator**.  *Linux users, skip ahead to the Linux
   section*

.. note::

   If you are using a non-US standard (QWERTY) keyboard, such as
   Dvorak or Colemak, you must switch to the US keyboard layout when
   using the Yubikey.  See the `Yubico support article on keyboard
   layouts
   <https://support.yubico.com/s/article/Using-YubiKeys-with-various-keyboard-layouts>`_.


Yubico Authenticator Setup Instructions for Windows/Mac
-------------------------------------------------------

.. important::

   **Apple Mac users** will need to allow `Input Monitoring` to allow the
   **Yubico Authenticator** to work properly.  `System Settings` =>
   `Privacy & Security` => `Input Monitoring`, toggle `Yubico
   Authenticator` on.


A. Open the **Yubico Authenticator** from the **Start Menu** (Windows) or
**Applications** folder (Mac).

.. image:: /images/yc-auth-main.png
              :scale: 40%

B. Select **Slots**.

.. image:: /images/yc-auth-slots.png
              :scale: 40%

C. Select **Slot 2 Long Touch**.

.. image:: /images/yc-auth-slot2.png
              :scale: 40%

D. Select **Yubico OTP.**

.. image:: /images/yc-auth-slot2-otp.png
              :scale: 40%

E. Configure **Yubico OTP** credential:

  - Under **Yubico OTP**, check and set the following:
  - Under **Public ID**, select **Use serial**.
  - Under **Private ID**, select **Generate**.
  - Under **Secret Key**, select **Generate**.

.. image:: /images/yc-auth-otp-register.png

F. Record the **Public ID** and **Secret Key** in your favorite plain
   text editor. You will not be able to retrieve this information again
   after completion. We will use this information to complete the
   Yubikey enrollment process.

G. Select **Save** to confirm the changes on the Yubikey. The changes
   will be written to the Yubikey.

   .. image:: /images/yc-auth-otp-register2.png

  .. note::
     **Slot 2** may show as being configured.  It is safe to overwrite the configuration.

Proceed to Step 5.

Yubico Authenticator Setup Instructions for Linux
-------------------------------------------------

A. Open a terminal window.

B. Type (or copy and paste) the following **ykman** command:

.. code-block:: console

   ykman otp yubiotp 2 --serial-public-id --generate-private-id --generate-key

**Example:**

.. code-block:: console

        ykman otp yubiotp 1 --serial-public-id --generate-private-id --generate-key
        Using Yubikey serial as public ID: vvcccbn*****
        Using a randomly generated private ID: a36ad3d*****
        Using a randomly generated secret key: 4de7b4a69faa75e779a8b0869b0*****
        Program a YubiOTP credential in slot 2? [y/N]: y

C. Record the **Public ID** and **Secret Key** in your favorite plain
   text editor. You will not be able to retrieve this information again
   after completion. We will use this information to complete the
   Yubikey enrollment process.

D. Type **y** and press **<ENTER>** to confirm the changes on the
   Yubikey. The changes will be written to the Yubikey.

  .. note::
     **Slot 2** may show as being configured.  It is safe to overwrite the configuration.

Continue onwards to the next step, Step 5.

5. In a web browser, navigate to the `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_.

.. image:: /images/yk-aim.png
              :scale: 70%

- Enter the **Secret Key.**

- Enter a 6 to 8 digit PIN. You may choose to re-use the PIN you use
  for your RSA token to make it easier to remember.

- Confirm the PIN.

6. Click on **Register Yubikey** to complete the registration.

.. important::

   Once you have followed these registrations instructions, you will
   be using your Yubikey to authenticate into the RDHPCS.  **Your RSA
   token will no longer work.**

Wait for web page to return a green confirmation message.

.. image:: /images/aim-mfa-registration.png
              :scale: 70%

Now test the registration of your Yubikey.

Testing your Yubikey Registration for NOAA RDHPCS
-------------------------------------------------

You must have completed the registration steps above.

1. In a web browser, navigate to the `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_.

2. Click the **Test Yubikey** button.

   .. image:: /images/aim-mfa-test-open.png
              :scale: 70%

3. In the entry box, enter your PIN, then press and hold the Yubikey.
   **DO NOT PRESS ENTER.**

   .. image:: /images/aim-mfa-test-entry.png
              :scale: 70%

4. If the PIN and Yubikey OTP are correct, a success message is returned.

   .. image:: /images/aim-mfa-test-success.png
              :scale: 70%

.. note::

    These steps configure your Yubikey for use on RDHPCS systems.
    Once this is done you will generally not need to use your Yubikey
    Authenticator again, unless you need to re-register your Yubikey
    if you are issued a replament Yubikey.


**FINAL STEP: SUCCESS!**

Proceed to log into NOAA RDHPCS resources using SSH or ParallelWorks.
Remember to use the correct username, and type in your PIN then
**touch and hold** the Yubikey.



Troubleshooting RDHPCS Yubikey Authentication
---------------------------------------------

The most common problem we have seen from users that are having
problems when logging in with Yubikey is the failure to do the
"long touch" correctly.

So here are a couple of guidlines that should help:

* When logging into the RHPCS bastions using a terminal program
  you should **keep touching** the key until the cursor moves
  to the next line.
* When logging in using any of the GUIs, Globus login using
  a browser for example, you should **keep touching**
  until the authentication fails or succeeds.  You should
  keep your finger on the Yubikey even after it looks like
  it has completed entering the token.  There should be
  no need to press the "Enter" key when using GUIs for
  logging in.

If you are doing the right things as mentioned above and are
still having problems, please read through the following
troubleshooting suggestions.

Be advised there are at least three Yubikey registrations needed to
set up your all NOAA accounts to use your NOAA issued Yubikey.  Please
keep in mind that registering for one service doesn't automatically
imply that you have registered for the other services.

As a NOAA RDHPCS user, you have to register your Yubikey for at least
three different areas:

#. Register your Yubikey for accessing Gmail for your NOAA.GOV email.
#. Register your Yubikey for ICAM (NOAA SSO), which is required for
   accessing most NOAA web applications.
#. Register your Yubikey for RDHPCS,which is required to access
   RDHPC resources.
#. There may also be lab-specific Yubikey registrations (GFDL)
   required to access lab-level resources.

You must have registered your NOAA issued Yubikey for Gmail and NOAA
SSO before registering it for NOAA RDHPCS use.  Check to see if you have
registered for RDHPCS access by going to `AIM
<https://aim.rdhpcs.noaa.gov/>`_.

If you are having trouble logging into RDHPCS systems with your
Yubikey:

#. Confirm you have registered for NOAA RDHPCS use at the
   `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_.

   If AIM shows that you have not registered your Yubikey with RDHPCS,
   go to the top of this page and follow the instructions.

#. Confirm proper registration by clicking on the blue
   "Test Yubikey" button and confirming that your authentication
   is working.

   If the PIN is incorrect, the message returned will indicate that.

#. If the registration test in AIM fails then try to re-register your
   Yubikey; delete the current registration and follow the steps on
   this page, making sure that all commands were successful.


#. If the registration test in AIM succeeds, but you cannot log into
   NOAA RDHPCS resources, remember that:

   - You must already have access to the RDHPCS resource.  Registering
     a yubikey does not grant any access.

   - You must use the correct username, First.Last format.

   - You must enter your PIN, then **press and hold** the Yubikey
     when authenticating.

