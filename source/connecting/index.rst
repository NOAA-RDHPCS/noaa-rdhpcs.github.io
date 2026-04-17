.. _connecting-to-rdhpcs:

##########
Connecting
##########

.. _ssh-overview:

********
Overview
********

All RDHPCS on-premise compute systems are accessed through a *bastion
host* — a secure gateway server between your workstation and the
compute system.  You connect to the bastion first, and the bastion
forwards you to the compute system.

.. code-block:: text

   Your workstation  →  Bastion host  →  RDHPCS compute system

RDHPCS supports two authentication methods:

* **Common Access Card (CAC)** — uses your CAC with the Tectia
  Secure Shell (SSH) client.  Recommended for users who have a CAC
  and a card reader.
* **YubiKey** — uses your NOAA-issued YubiKey with a standard SSH
  client.  Use this method if you don't have a CAC or a card reader.

Within the RDHPCS enclave, `X.509`_ certificates authenticate you
to individual compute systems.

.. note::

   Mississippi State University (MSU) hosts the Orion and Hercules
   systems using a separate login process.  See the
   :ref:`MSU-HPC user guide <MSU-HPC-user-guide>`.

.. note::

   Cloud resources are available through the `Parallel Works`_
   platform.  See the :ref:`Cloud User Guide <cloud-user-guide>`.


.. _prerequisites:

****************
Before you begin
****************

Confirm you have the following before connecting for the first time:

* An active RDHPCS account.  Visit `Account Information Management`_
  (AIM) to view your profile.
* Access to the RDHPCS system you want to use.  AIM lists the systems
  your account can access.
* A CAC and card reader, **or** a registered YubiKey.
  See :ref:`yubikey-user-instructions` to register your YubiKey.
* An SSH client installed and configured.
  See :ref:`ssh-client-selection` below.

.. attention::

   You must have access to a system before you can log into it.
   Visit AIM to verify your system access before you begin.


.. _ssh-client-selection:

********************************
Choose and install an SSH client
********************************

Your platform and authentication method determine which SSH client to
use.  See :ref:`ssh-clients` for selection guidance and installation
instructions for each client.


.. _bastion_hostnames:

*****************
Bastion hostnames
*****************

Each RDHPCS system has bastion hosts at two locations: Princeton,
New Jersey, and Boulder, Colorado.  Either location works for login
and data transfer.  Choose the location closest to you for the best
response time.

CAC users must connect to a CAC bastion hostname.
YubiKey users must connect to an RSA bastion hostname.

.. |CBHN|   replace:: **CAC bastion hostnames**
.. |RBHN|   replace:: **RSA bastion hostnames**
.. |GCPRNG| replace:: gaea.princeton.rdhpcs.noaa.gov
.. |GCBRNG| replace:: gaea.boulder.rdhpcs.noaa.gov
.. |GRPRNG| replace:: gaea-rsa.princeton.rdhpcs.noaa.gov
.. |GRBRNG| replace:: gaea-rsa.boulder.rdhpcs.noaa.gov

.. |HCPRNG| replace:: hera.princeton.rdhpcs.noaa.gov
.. |HCBRNG| replace:: hera.boulder.rdhpcs.noaa.gov
.. |HRPRNG| replace:: hera-rsa.princeton.rdhpcs.noaa.gov
.. |HRBRNG| replace:: hera-rsa.boulder.rdhpcs.noaa.gov

.. |JCPRNG| replace:: bastion-jet.princeton.rdhpcs.noaa.gov
.. |JCBRNG| replace:: bastion-jet.boulder.rdhpcs.noaa.gov
.. |JRPRNG| replace:: jet-rsa.princeton.rdhpcs.noaa.gov
.. |JRBRNG| replace:: jet-rsa.boulder.rdhpcs.noaa.gov

.. |PPPRNG| replace:: bastion-analysis.princeton.rdhpcs.noaa.gov
.. |PPBRNG| replace:: bastion-analysis.boulder.rdhpcs.noaa.gov
.. |PAPRNG| replace:: analysis-rsa.princeton.rdhpcs.noaa.gov
.. |PBPRNG| replace:: analysis-rsa.boulder.rdhpcs.noaa.gov

.. |MCPRNG| replace:: mercury-cac.princeton.rdhpcs.noaa.gov
.. |MCBRNG| replace:: mercury-cac.boulder.rdhpcs.noaa.gov
.. |MRPRNG| replace:: mercury-rsa.princeton.rdhpcs.noaa.gov
.. |MRBRNG| replace:: mercury-rsa.boulder.rdhpcs.noaa.gov

.. |UCPRNG| replace:: ursa-cac.princeton.rdhpcs.noaa.gov
.. |UCBRNG| replace:: ursa-cac.boulder.rdhpcs.noaa.gov
.. |URPRNG| replace:: ursa-rsa.princeton.rdhpcs.noaa.gov
.. |URBRNG| replace:: ursa-rsa.boulder.rdhpcs.noaa.gov

+-------------------+-----------------+----------------------------------+
| **RDHPCS system** | |CBHN|          | |RBHN|                           |
+-------------------+-----------------+----------------------------------+
| Gaea              | |GCPRNG|        | |GRPRNG|                         |
|                   |                 |                                  |
|                   | |GCBRNG|        | |GRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| Hera              | |HCPRNG|        | |HRPRNG|                         |
|                   |                 |                                  |
|                   | |HCBRNG|        | |HRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| Jet               | |JCPRNG|        | |JRPRNG|                         |
|                   |                 |                                  |
|                   | |JCBRNG|        | |JRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| PPAN              | |PPPRNG|        | |PAPRNG|                         |
|                   |                 |                                  |
|                   | |PPBRNG|        | |PBPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Mercury           | |MCPRNG|        | |MRPRNG|                         |
|                   |                 |                                  |
|                   | |MCBRNG|        | |MRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| Ursa              | |UCPRNG|        | |URPRNG|                         |
|                   |                 |                                  |
|                   | |UCBRNG|        | |URBRNG|                         |
+-------------------+-----------------+----------------------------------+


.. _ssh_access:
.. _login-instructions:

******
Log in
******

.. _first-login:

First login and certificate setup
==================================

On your first login, RDHPCS creates an `X.509`_ master certificate
that authenticates you to RDHPCS systems.  The certificate request
must be signed before you can fully log in.  Signing takes less than
five minutes.

The system prompts you to create a passphrase for your master
certificate.  Create a passphrase of at least three words.

.. note::

   Your master certificate is valid for one year.  Each login renews
   a thirty-day proxy certificate used for resource access and data
   transfers.

.. note::

   If you forget your passphrase, keep attempting to log in.  On the
   fourth failed attempt, the system prompts you to regenerate your
   master certificate.


.. _Common-access:
.. _cac_instructions:

Log in with a CAC
==================

CAC login requires a card reader and the :ref:`Tectia <Tectia>` SSH
client.  Install and configure Tectia before following these steps.

#. Find your CAC bastion hostname in the :ref:`bastion_hostnames`
   table above.
#. Open a terminal and connect to the bastion:

   .. code-block:: console

      $ sshg3 CAC-BASTION-HOSTNAME

#. When prompted, enter your CAC Personal Identification Number (PIN).

If you recently received a new or renewed CAC, update your card
information in `Account Information Management`_ before logging in.


.. _yubikey_instructions:

Log in with a YubiKey
======================

:ref:`Configure and register your YubiKey <yubikey-user-instructions>`
before following these steps.

#. Find your RSA bastion hostname in the :ref:`bastion_hostnames`
   table above.
#. Open a terminal and connect to the bastion:

   .. code-block:: console

      $ ssh RSA-BASTION-HOSTNAME

#. When prompted, enter your YubiKey PIN, then press and hold the
   YubiKey button (long press).


.. _select-a-node:

*************
Select a node
*************

After you authenticate at the bastion, a list of available compute
nodes is displayed.  The bastion waits five seconds, then connects
you to a node that the load balancer selects.

To connect to a specific node, press :kbd:`Control+C` within five
seconds and enter the node name when prompted.

The following example shows the selection prompt as it appears on the
Gaea system.  The node list varies by system.

.. code-block:: shell

   Welcome to the NOAA RDHPCS.

   Attempting to renew your proxy certificate...
   Proxy certificate has 720:00:00  (30.0 days) left.

           Welcome to gaea.rdhpcs.noaa.gov
   Gateway to gaea-c5.ncrc.gov and other points beyond

   Hostname            Description
   gaea                C5 head nodes
   gaea51              C5 head node
   gaea52              C5 head node
   ...
   gaea61              C6 head node
   ...

   To select a specific host, hit ^C within 5 seconds.

.. note::

   After five seconds, the bastion connects you to the load-balanced
   default node.  See the user guide for your system for the complete
   list of available nodes.


.. _ssh-port-tunnels:

****************
SSH port tunnels
****************

RDHPCS bastions support SSH port forwarding, also called *port
tunneling*.  Port tunnels let you:

* Transfer files using tools like :command:`scp` and :command:`rsync`.
* Use remote development tools such as
  :ref:`VS Code Remote-SSH <rdhpcs-VSCode>` and the
  :ref:`ARM Forge debugger <linaro-forge>`.
* Access Jupyter notebooks running on compute nodes.
* Forward other network services between your workstation and RDHPCS
  systems.

.. note::

   SSH port forwarding is not supported on MSU HPC systems
   (Orion and Hercules).

Port assignment
===============

Each user gets unique port numbers calculated from a base port for
each system and your user ID (UID).  Run :command:`id -u` on any
RDHPCS system to find your UID.

**Port formula:** LocalForward port = base port + UID

If the result exceeds 65,535, the port wraps around:
port = (base port + UID - 65,535) + 2,000.

.. list-table:: Port tunnel base ports by system
   :header-rows: 1
   :widths: 20 40 40

   * - System
     - LocalForward base port
     - RemoteForward base port
   * - Gaea
     - 30,000
     - 20,000
   * - Hera
     - 45,000
     - 55,000
   * - Jet
     - 11,300
     - 21,300
   * - Mercury
     - 25,000
     - 35,000
   * - PPAN
     - 40,000
     - 50,000
   * - Ursa
     - 35,000
     - 45,000

Use the :ref:`OpenSSH configuration form <openssh-config>` to
generate a complete SSH configuration with your port assignments
already calculated.  Your assigned port numbers also appear in the
login banner each time you connect.

Set up port tunnels
===================

For client-specific port tunnel setup, see:

* :ref:`openssh-client` — OpenSSH on Linux, macOS, and Windows
* :ref:`putty-client` — PuTTY on Windows
* :ref:`Tectia` — Tectia on Windows, macOS, and Linux

.. warning::

   The tunnels are active only while this SSH session remains open.
   Closing the terminal window or letting the session time out
   disconnects all tunnels.  Keep this session running the entire
   time you need access.

To verify a tunnel, open a second terminal and connect through the
local port:

.. code-block:: console

   $ ssh -p LOCAL-PORT First.Last@localhost

Replace ``LOCAL-PORT`` with your calculated LocalForward port for
the system.  You are prompted for your normal credentials (PIN + RSA
token or YubiKey).  A successful login confirms the tunnel is working.
You can log out of the test session immediately.


.. _x11-graphics:

***********************
X11 and remote graphics
***********************

SSH X11 forwarding lets you run graphical applications on RDHPCS
systems and display them on your local workstation.

For X11 setup with your SSH client, see :ref:`openssh-x11`,
:ref:`putty-x11`, or :ref:`tectia-x11`.

Windows X11 servers
===================

To display graphical output on Windows, an X11 server must be running
on your workstation before you connect.  Options include:

* `MobaXterm`_ — includes a built-in X11 server.  No separate
  installation is needed.
* `VcXsrv`_ — a free, open-source X11 server for Windows.

X2Go
====

Basic X11 forwarding can be slow over high-latency connections.
RDHPCS systems support X2Go for faster graphical application
performance.

.. .. TODO: Add a dedicated X2Go setup and usage guide.

If you have trouble with X2Go, :ref:`contact the help desk
<getting_help>`.


.. _web-based-access:

****************
Web-based access
****************

The RDHPCS Cloud Platform is available from a web browser through the
`Parallel Works`_ platform.  `Parallel Works`_ lets you create and
manage on-demand High Performance Computing (HPC) clusters without an
SSH connection.

See the :ref:`Cloud User Guide <cloud-user-guide>` for details.


.. toctree::
   :maxdepth: 1
   :hidden:

   SSH Clients <ssh_clients/index>


.. _Account Information Management: https://aim.rdhpcs.noaa.gov
.. _X.509: https://en.wikipedia.org/wiki/X.509
.. _MobaXterm: https://mobaxterm.mobatek.net/
.. _VcXsrv: https://sourceforge.net/projects/vcxsrv/
.. _Parallel Works: https://noaa.parallel.works
