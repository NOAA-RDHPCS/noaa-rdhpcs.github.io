.. _common_access_card:

Common Access Card (CAC)
========================

The Common Access Card (CAC) is a means of access to RDHPCS
resources for both Web and SSH access. To obtain a CAC, work with your
local admin services team as they need to start the application
process.  Some labs can issue CACs on-site, otherwise you will have to
visit a RAPIDS site. The site locator website is `ID Card Office
Online <https://idco.dmdc.osd.mil/idco/>`_.  SSH logins with a CAC
require additional software.

.. _cac_piv_ssh_enrollment:

CAC/PIV SSH Key Enrollment
===========================

A Common Access Card (CAC) or Personal Identity Verification (PIV)
card can be used to establish SSH connections to NOAA RDHPCS resources
such as bastions and RDHPCS login nodes.  These instructions guide you
through extracting your PIV authentication certificate as an OpenSSH
public key and enrolling it for use in the RDHPCS systems.

.. important::

   The SSH public key enrollment only needs to be completed **once**,
   unless you have renewed your CAC.  Do not re-enroll once per
   platform or per system.

.. important::

   CAC/PIV authentication is preferred for interactive RDHPCS logins.
   However, the following services **require** Yubikey and do **not**
   support CAC/PIV authentication:

   - Authenticating to role accounts
   - Authenticating to trusted and untrusted DTNs for data transfers
   - Authenticating to Globus for data transfers
   - Data transfers using the port tunnelling method

----

Prerequisites
-------------

- A valid CAC or PIV card with a PIV Authentication certificate
- A CAC/PIV card reader connected to your workstation
- Your CAC/PIV PIN
- An active NOAA RDHPCS account
- Windows only: Putty-CAC

----

Windows Only Step: Install PuTTY-CAC
------------------------------------

PuTTY-CAC is a fork of PuTTY that uses Microsoft's built-in CryptoAPI (CAPI)
to interface with smart cards. No additional middleware (e.g., OpenSC) is
required.

**For NOAA Government Furnished Equipment (GFE):**
   Submit a software installation request to your local I/T office for
   the latest **PuTTY-CAC** release.

**For non-GFE Windows systems:**
   Download the latest ``putty.exe`` (64-bit) directly from the
   PuTTY-CAC releases page:

   https://github.com/NoMoreFood/putty-cac/releases

   No installation is required — the single ``.exe`` is self-contained.

----

Step 1: Extract Your PIV SSH Public Key
----------------------------------------

These steps retrieve the ``ssh-rsa`` public key that corresponds to
the PIV Authentication certificate on your card.  The exact steps vary
depending on your environment.  Choose the correct path:

Linux
-----

1. Insert your PIV/CAC into your card reader.

2. Ensure you have the ``pkcs15-tool`` available

.. code-block:: console

   pkcs15-tool --help

If "Command not found" is returned, install the ``opensc`` package
using your Linux package manager and try again.

3. If you have a CAC, try the following command in a terminal window:
.. code-block:: console

   pkcs15-tool --read-ssh-key 4

The output will be two lines. Copy the line that starts with "ssh-rsa"
and proceed to step 4.

If that produced no output, or no lines that started with ssh-rsa, try:

.. code-block:: console

   pkcs15-tool --read-ssh-key 5

The output will be two lines. Copy the line that starts with "ssh-rsa"
and proceed to step 4.

If this doesn't work, proceed to the PIV instructions.

4. If you have a PIV card:

In a terminal window, list the keys available. Look for "PIV AUTH" or
"CAC Cert":

.. code-block:: console

        pkcs15-tool --list-public-keys

Sample output:

.. code-block:: console

        ~]$ pkcs15-tool --list-public-keys
        … snip …
        Public RSA Key [CAC Cert 5]
                Object Flags    : [0x00]
                Usage           : [0xC0], verify, verifyRecover
                Access Flags    : [0x02], extract
                ModLength       : 2048
                Key ref         : 5 (0x05)
                Native          : yes
                ID              : 0005
                DirectValue     : <absent>

The label and ID numbers vary based on the version of OpenSC and the
smart card. Record the existence of either “PIV AUTH” or “CAC Cert.”
If “CAC Cert” is present, refer to either “CAC Cert 5” or “CAC Cert
4.” Record the ID number associated with the Public RSA Key.

5. Use the ID number to view your SSH key.

.. code-block:: console

        pkcs15-tool --read-ssh-key ####

The output will be two lines. Copy the line that starts with "ssh-rsa"
and proceed to step 4.

Mac OS
------

1. Insert your PIV/CAC into your reader.

2. Open a terminal window, and use the ``ssh-keygen`` command to get
   the OpenSSH-format public key fingerprint.

.. code-block:: console

   ssh-keygen -D /usr/lib/ssh-keychain.dylib

The output will be two lines that start with ssh-rsa.  Copy the line
that contains “Key for PIV Authentication” and proceed to step 4


Windows
-------

1. **Insert** your CAC/PIV card into the card reader.

2. **Open** PuTTY-CAC (``putty.exe``).

3. In the PuTTY Configuration window, navigate to
   **Connection → SSH → Certificate**.

4. Under **Authentication methods**, check
   **Attempt certificate / key authentication**.

5. Under **Authentication parameters**, click **Set CAPI Cert…**

   A Windows Security dialog titled *"PuTTY: Select Certificate Or Key"*
   will appear.

   .. note::

      There may be multiple certificates on your card. Select the one
      intended for authentication:

      - **CAC** cards: the certificate is identified by a ``number@mil``
        notation.
      - **PIV** cards: the certificate uses an email address notation,
        such as ``username@noaa.gov``.

      If your certificate is not immediately visible, click
      **More choices** to locate it.

6. Select your authentication certificate and click **OK**.

7. Back in the PuTTY Configuration window, click the
   **Copy To Clipboard** button next to the SSH keystring field.

8. **Paste** the clipboard contents into a plain text editor (e.g.,
   Notepad). The raw output will look similar to::

      ssh-rsa AAAAB3Nza…b3c25 CAPI:abc123def… CN=JOHN.PAUL.SMITH.123456789, OU=FEDERAL, OU=PKI, OU=DoD, O=U.S. Government, C=US

   Save this file — you will need it in the next step.

----

Step 3: Trim the Key Comment
------------------------------

The registration process enforces a **79-character limit** on the SSH
public key comment field. The raw PuTTY-CAC output exceeds this limit
and must be trimmed before enrollment.

From the raw output, retain only the ``CN=...`` value up to (but not
including) the first comma. Discard the ``CAPI:...`` thumbprint and all
``OU=`` / ``O=`` / ``C=`` fields.

**Before trimming:**

.. code-block:: text

   ssh-rsa AAAAB3Nza…b3c25 CAPI:abc123def… CN=JOHN.PAUL.SMITH.123456789, OU=FEDERAL, OU=PKI, OU=DoD, O=U.S. Government, C=US

**After trimming:**

.. code-block:: text

   ssh-rsa AAAAB3Nza…b3c25 JOHN.PAUL.SMITH.123456789

The trimmed key must follow this format:
``ssh-rsa <base64-key-blob> <comment-under-79-chars>``

.. warning::

   The **Enroll Token** button will not become active if the SSH public
   key comment exceeds 79 characters. Verify your trimmed comment length
   before proceeding.

----

Step 4: Enroll Your SSH Public Key
------------------------------------

1. Open a web browser and navigate to the RDHPCS AIM portal:

   https://aim.rdhpcs.noaa.gov

2. Log in with your RDHPCS username using CAC, PIV, or Yubikey.

3. Select the green **Update your NOAA MFA** button.

4. At the enrollment screen:

   a. Paste the trimmed SSH public key (from Step 3) into the
      **SSH public key** field.
   b. Click **Register SSHKEY**.

----

Step 5: Connect to RDHPCS Resources
-------------------------------------

Once your key has been registered by performing the above steps, you
may proceed to use your CAC / PIV / SSHKEY to connect to RDHPCS
bastions.  See :ref:`CAC SSH Login<Common-access>` for details.

----

Troubleshooting
----------------

**Certificate not appearing in the selection dialog**
   Click **More choices** in the Windows Security dialog. Ensure your
   card is fully inserted and recognized by Windows before opening
   PuTTY-CAC.

**"Enroll Token" button is greyed out**
   Your SSH public key comment exceeds 79 characters. Re-trim the
   comment field as described in Step 3.

**Authentication fails after enrollment**
   - Confirm you received the activation email from RDHPCS staff.
   - Verify you are using ``First.Last`` username format.
   - Ensure the correct PIV Authentication certificate is selected
     (not an email signing or encryption certificate).

**Key needs to be re-enrolled (e.g., new card issued)**
   Repeat Steps 2–4. Contact the RDHPCS help desk if your old key
   needs to be removed from the system first.

----

Additional Resources
---------------------

- `RDHPCS Account Management <https://docs.rdhpcs.noaa.gov/accounts/accounts_and_projects.html>`_
- `RDHPCS Yubikey Registration <https://docs.rdhpcs.noaa.gov/accounts/yubikey_token.html>`_
- `ID Management SSH with PIV Guide <https://playbooks.idmanagement.gov/piv/engineer/ssh/>`_
- RDHPCS Help Desk: `rdhpcs.help@noaa.gov <mailto:rdhpcs.help@noaa.gov>`_

.. _putty_cac_config:

fill me in.
