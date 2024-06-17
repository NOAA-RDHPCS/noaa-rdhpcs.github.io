.. _logging_in:

NOTE:  I'm unable to search for topics that exist in the Wiki Documentation today.  Example: searching for  "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED" and it gives you unrelated links.
On Wiki it gives you this : https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php?title=FAQs_-_Frequently_Asked_Questions#WARNING:_REMOTE_HOST_IDENTIFICATION_HAS_CHANGED!
And it doesn't give a lot of false links.  This will make users unable to find simple things in the documentation.  Overall, I could probably provide 100 examples if I had enough time to add them all here.  
Another good one is "reset passphrase" - it should take you right to the spot in the documentation where we reset the passphrase, but it does not and I think users will get lost.

##########
Logging In
##########

Access to Gaea requires an RDHPCS account.  Please review the :ref:`Obtaining an
Account <accounts>` page, or `see the link below
<https://rdhpcs2.common2.docs.rdhpcs.noaa.gov/wiki/index.php/Logging_in>`_

Obtaining an Account
====================

1. User gets NEMS/Gmail account from sponsoring lab's process.
   (Get this done before starting the Gaea account request process.)
2. User uses NEMS/Gmail (First.Last username and password) to access the RDHPCS
   `Account Information Management (AIM) <https://aim.rdhpcs.noaa.gov>`_ and
   requests access to one or more projects.
3. The principle investigator (PI) of project approves.
4. HR approves.
5. The Information System Security Officer (ISSO) approves.
6. The resource manager (RM) approves.  This last is the system owner for e.g. Gaea,
   Hera, Jet, Niagara.
7. Automation and manual account creation processes proceed. If needed, an RSA
   fob is issued.

.. note::

    NOAA RDHPCS systems use a **long user name** which is usually the same as your
    NOAA email user name. These pages frequently refer to this long user name as
    *First.Last*.

First Time Login
=================

Access to most RDHPCS systems require a signed x.509 certificate.  The first
login attempt will generate a master certificate and send a request to have it
signed.  Users cannot fully log on to a system until that certificate is signed.
It can take up to one business day for the certificate to be signed.

The prompt will ask you to create a passphrase. Create a minimum of three words pass
phrase for your grid certificate. This only occurs if you did not already
generate a passphrase. Confirm the passphrase. Once confirmed it will take up to
24 hours for the certificate to be processed. Once the certificate is processed,
login using the regular login instructions.

.. note::

    If your certificate is not processed in a timely manner, please contact
    :ref:`support <getting_help>`

Connecting
==========

.. _cac_instructions:

Connecting with a CAC
---------------------

The preferred method to to access RDHPCS systems is to use the CAC bastion.
This uses your CAC for authentication.  This method requires the TECTIA SSH
client. RDHPCS has obtained licenses for all RDHPCS users.

.. code-block:: shell

    sshg3 host.url

When propted, enter your CAC PIN.

+---------------+-----------------------------------+
| RDHPCS System | CAC Bastion URL                   |
+===============+===================================+
| Jet           | jet.princeton.rdhpcs.noaa.gov     |
+               +                                   +
|               | jet.boulder.rdhpcs.noaa.gov       |
+---------------+-----------------------------------+
| Gaea          | gaea.princeton.rdhpcs.noaa.gov    |
+               +                                   +
|               | gaea.boulder.rdhpcs.noaa.gov      |
+---------------+-----------------------------------+
| Niagara       | niagara.boulder.rdhpcs.noaa.gov   |
+               +                                   +
|               | niagara.princeton.rdhpcs.noaa.gov |
+---------------+-----------------------------------+
| Hera          | hera.boulder.rdhpcs.noaa.gov      |
+               +                                   +
|               | hera.princeton.rdhpcs.noaa.gov    |
+---------------+-----------------------------------+

.. _rsa_instructions:

Connecting with an RSA token
----------------------------

Users who do not have a CAC, or are connecting through a system that does not have
a TECTIA client (e.g., Mac OS, Android, ChromeOS, etc.) will need to use the RSA
bastion.

.. code-block:: shell

    ssh host-url

When propted, enter your PASSCODE which consists of your PIN+RSA_CODE.  The
RSA_CODE is the 6-8 digit code from the RSA fob or RSA app.

+---------------+---------------------------------------+
| RDHPCS System | CAC Bastion URL                       |
+===============+=======================================+
| Jet           | jet-rsa.boulder.rdhpcs.noaa.gov       |
+               +                                       +
|               | jet-rsa.princeton.rdhpcs.noaa.gov     |
+---------------+---------------------------------------+
| Gaea          | gaea-rsa.boulder.rdhpcs.noaa.gov      |
+               +                                       +
|               | gaea-rsa.princeton.rdhpcs.noaa.gov    |
+---------------+---------------------------------------+
| Niagara       | niagara-rsa.boulder.rdhpcs.noaa.gov   |
+               +                                       +
|               | niagara-rsa.princeton.rdhpcs.noaa.gov |
+---------------+---------------------------------------+
| Hera          | hera-rsa.boulder.rdhpcs.noaa.gov      |
+               +                                       +
|               | hera-rsa.princeton.rdhpcs.noaa.gov    |
+---------------+---------------------------------------+

.. note::

    At the first connection with an RSA token, you will be prompted for a new PIN,
    which must be at least 6 alphanumeric characters.

Selecting a Node
----------------

Many RDHPCS systems allow users to select a specific host at login.  After successful
authentication at the bastion host, the output displays a list of available
nodes, and then waits for 5 seconds.  An example is below.

The gaea bastion host then displays the menu:

.. code-block:: shell

    The RDHPCS destinations are:
    Hostname            Description
    rdhpcs01              RDHPCS head nodes
    rdhpcs02              RDHPCS head node
    rdhpcs03              RDHPCS head node

    You will now be connected to OneNOAA RDHPCS: RDHPCS system.
    To select a specific host, hit ^C within 5 seconds.

To select a specific host, press Control+C (^C) and enter the desired host.  The
last selected node will be the default node.

.. note::

    After the 5 second wait, the bastion node will use a load balancer to select
    a node.


X11 Graphics
============

Users can use SSH X11 forwarding to open GUI-based applications (e.g., xterm,
ARM Forge).  This is typically done using an SSH option.  For the TECTIA client
``sshg3`` or OpenSSH-based clients, use the ``-X`` option:

.. code-block:: shell

    gsissh -X host.url

or

.. code-block:: shell

    ssh -X host.url

Other clients, like PuTTY, will have an option when configuring the host.

The base SSH X11 forwarding is typically slow.  RDHPCS systems use X2Go for
improved X11 performance.  Some users have found it difficult to use X2Go.
Please submit a :ref:`support issue <getting_help>` if you have issues using
X2Go.

.. note::

    Microsoft Windows users can use any of the X11 servers available for
    Windows.  The SSH client will need to be configured to use the X11 server
    for forwarding X11.

SSH Port Tunnels
================

To allow users to easily transfer small files to and from the RDHPCS
systems, the bastion configures SSH port-forwarding tunnels.  To use these
tunnels, the user must configure their local SSH client to create tunnels
to/from the bastion.

.. note::

    **TODO**

    Need to add this information.
