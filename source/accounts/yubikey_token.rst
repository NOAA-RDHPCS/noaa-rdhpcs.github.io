.. _yubikey-user-instructions:

Configuring Yubikey for the NOAA RDHPCS
=======================================

A Yubikey is an “electronic physical keyring” that is plugged into an
available USB slot on your computer. Like a keyring, a Yubikey holds
(stores) several sets of keys (authentication tokens and
certificates), and helps prevent the compromise of accounts used to
access computers, networks and web applications by requiring the
physical possession of a key for successful login.

.. image:: /images/yubi-usbc.png
   :align: center

.. important::

   As of **October 1, 2025** YubiKeys or CAC will be required to
   access the NOAA RDHPCS.  Contact your security office to request a
   Yubikey.

Yubikey Registration
--------------------

The NOAA Yubikey is issued by your security office.  You must register
it for use with your NOAA accounts at https://accounts.noaa.gov,
**and** follow the additional steps below to configure and register
your NOAA issued Yubikey for RDHPCS use.

Follow these steps to configure **Slot 2** with a **Yubico OTP** credential:

1. You must have registered your NOAA issued Yubikey at https://accounts.noaa.gov.

2. Download and install the `YubiKey Manager <https://www.yubico.com/support/download/yubikey-manager/>`_

3. Insert your NOAA issued Yubikey into an available USB slot

4. Open the **YubiKey Manager** from the **Start Menu** (Windows) or
   **Applications** folder (Mac).

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



