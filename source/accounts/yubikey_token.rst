.. _yubikey-user-instructions:

.. important::

   **THESE ARE PRELIMINARY INSTRUCTIONS THAT CANNOT BE FOLLOWED COMPLETELY YET**

.. important::

   **THESE ARE PRELIMINARY INSTRUCTIONS THAT CANNOT BE FOLLOWED COMPLETELY YET**

YubiKey
=======

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

   As of **October 1, 2025** YubiKeys or CAC will be required to
   access the NOAA RDHPCS.  Contact your security office to request a
   Yubikey.

Yubikey Registration
--------------------

The NOAA Yubikey is issued by your security office.

**If you do not have a NOAA issued YubiKey, contact your local I/T
staff, your primary email admin, or your security office.**

If you do not know *any* of those details, start by contacting your
mail admin.  Log into the `NOAA Staff Directory
<https://nsd.rdc.noaa.gov/member/details>`_.  Click your name on
the right hand side, then click **View my Info**.  Click the link
**Primary Mail Admin** to send an email to your mail admin to start your
Yubikey request.

You must register your NOAA issued YubiKey for use with your NOAA
accounts at https://accounts.noaa.gov, **and** follow the additional
steps below to configure and register your Yubikey for RDHPCS use.

.. note::

   If you have lost your NOAA issued Yubikey and have a replacement
   Yubikey, you will need to delete the lost Yubikey at the
   `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_

**These steps create a** *new* **token on your Yubikey in** *Slot 2*,
**the** *Long Press* **slot.  It is separate and different from the**
*Short Press* **you have been using.**

.. note::

   A *Long Press* means touch **and hold for three (3) seconds**


Follow these steps to configure **Long Press Slot 2** with a **Yubico
OTP** credential.  You can safely restart these instructions and
re-register the *Yubico OTP* credential **in Long Press Slot 2**:

1. You must have registered your NOAA issued Yubikey at
   https://accounts.noaa.gov.  Navigate to your `NOAA Accounts profile
   page
   <https://accounts.noaa.gov/enduser/?realm=noaa-online#/profile>`_
   and look at **MFA Enrollment** for a green checkmark and **Yubikey
   registered**

.. image:: /images/noaa-accounts-profile.png
        :scale: 70%

.. important::

   DO NOT PROCEED until you have registered your NOAA issued YubiKey
   at https://accounts.noaa.gov

2. Download and install the `YubiKey Manager <https://www.yubico.com/support/download/yubikey-manager/>`_

.. note::

   If you are working on a Government Provided System (Government
   Furnished Equipment (GFE)) you will need to request a software
   installation from your local I/T office.  You may find it simpler
   and easier to use a personal computer for the following steps.

3. Insert your NOAA issued Yubikey into an available USB slot

4. Open the **YubiKey Manager** from the **Start Menu** (Windows) or
   **Applications** folder (Mac).  Linux users start it from the
   command-line or wherever it gets installed.

   .. image:: /images/yk-mgr-main.png
              :scale: 40%

5. From the **Applications** menu, select **OTP**.

.. image:: /images/yk-mgr-app-otp.png
              :scale: 40%

6. Under **Long Touch (Slot 2)**, select **Configure**

.. image:: /images/yk-mgr-otp.png
              :scale: 40%

7. Under **Select Credential Type**, select **Yubico OTP**

.. image:: /images/yk-mgr-otp-cred.png
              :scale: 40%

8. Select **Next** to continue to the **Yubico OTP** configuration.

9. Configure **Yubico OTP** credential

  - Under **Yubico OTP**, check and set the following:
  - Under **Public ID**, select **Use serial**.
  - Under **Private ID**, select **Generate**.
  - Under **Secret Key**, select **Generate**.
  - Ensure **Upload** is not checked.

.. image:: /images/yk-mgr-otp-register.png
              :scale: 40%

- Record the **Public ID** and **Secret Key** in your favorite plain
  text editor. You will not be able to retrieve this information again
  after completion. We will use this information to complete the
  YubiKey enrollment process.

- Select Finish to confirm the changes on the YubiKey. The changes
  will be written to the YubiKey.

  .. note::
     **Slot 2** may show as being configured.  It is safe to overwrite.

10. In a web browser, navigate to the `AIM MFA page <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_

.. image:: /images/yk-aim.png

- Enter the **Secret Key** from Step 9

- Enter a 6 to 8 digit PIN.  You may choose to re-use the PIN you use
  for your RSA token to make it easier to remember.

- Confirm the PIN.

11. Click on **Submit Changes** to complete the registration.



