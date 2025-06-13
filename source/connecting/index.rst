.. _connecting-to-rdhpcs:

##########
Connecting
##########

.. _Account Information Management:	https://aim.rdhpcs.noaa.gov

Connecting for the first time
=============================

All connections to the NOAA RDHPCS enclave are done via Secure Shell
(SSH) in a terminal session to a Bastion, or via a web browser to
`ParallelWorks <https://noaa.parallel.works>`__.  See our :ref:`ParallelWorks guide <cloud-user-guide>`.

.. note::

   For access to the MSU HPC systems Orion and Hercules, please review
   the :ref:`MSU-HPC <MSU-HPC-user-guide>` user guide.

Authentication is via a :ref:`CAC/PIV card<common-access>` or
:ref:`RSA SecurID token<rsa_instructions>`.

Internal to the enclave, `X509 certificates
<https://en.wikipedia.org/wiki/X.509>`__ are used to authenticate
between resources.  At first login, and at yearly intervals, a master
certificate valid for one year is created (SSH Bastion login required)
with a user-defined pass-phrase.  At each successive log in, a
thirty-day proxy certificate is created and used for resource access
and data transfers.

.. attention::

   You must have access to an RDHPCS resource (system) in order to log
   into it!  Visit the `Account Information Management`_ website to
   view your RDHPCS profile and system access.


Access to most RDHPCS systems require a signed x.509 certificate.  The
first login attempt will generate a master certificate request.  You
will experience a short (less than 5 minute) delay while the request
is signed. Users cannot fully log on to a system until that
certificate is signed.

The prompt will ask you to create a passphrase. Create a passphrase
with a minimum of three words.

.. note::

    Do not worry if you forget your passphrase -- just continue to
    try.  On the 4th attempt the system will prompt you to recreate
    your master certificate.

.. _ssh_access:

Secure Shell (SSH) Access
=========================

Access to on premise RDHPCS compute resources is done using the Secure Shell
(SSH) protocol to one of the system's bastions, or via ParallelWorks.

MSU systems (Orion, Hercules) are accessed via SSH or OpenOnDemand.
See MSU-HPC :ref:`MSUHPC-logging-in` for instructions.

SSH clients are available for Windows-based systems, such as published
by VanDyke software.  For recent SecureCRT versions, the preferred
authentication setting is shown above.

For Windows systems, `PuTTY
<https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_,
`SecureCRT <https://www.vandyke.com/products/securecrt/>`_, or
`MobaXterm <https://mobaxterm.mobatek.net/>`_ can also be used to
provide SSH capability.  Recent updates to Windows 10 and Windows 11
have added built-in support for SSH.  If it is not installed on your
version of Windows, please refer to Microsoft’s `documentation on
OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025>`_.

.. _bastion_hostnames:

Bastion Hostnames
=================
.. |CBHN|	replace:: **CAC Bastion hostnames**
.. |RBHN|	replace:: **RSA Bastion hostnames**
.. |GCPRNG|	replace:: gaea.princeton.rdhpcs.noaa.gov
.. |GCBRNG|	replace:: gaea.boulder.rdhpcs.noaa.gov
.. |GRPRNG|	replace:: gaea-rsa.princeton.rdhpcs.noaa.gov
.. |GRBRNG|	replace:: gaea-rsa.boulder.rdhpcs.noaa.gov

.. |HCPRNG|	replace:: hera.princeton.rdhpcs.noaa.gov
.. |HCBRNG|	replace:: hera.boulder.rdhpcs.noaa.gov
.. |HRPRNG|	replace:: hera-rsa.princeton.rdhpcs.noaa.gov
.. |HRBRNG|	replace:: hera-rsa.boulder.rdhpcs.noaa.gov

.. |JCPRNG|	replace:: jet.princeton.rdhpcs.noaa.gov
.. |JCBRNG|	replace:: jet.boulder.rdhpcs.noaa.gov
.. |JRPRNG|	replace:: jet-rsa.princeton.rdhpcs.noaa.gov
.. |JRBRNG|	replace:: jet-rsa.boulder.rdhpcs.noaa.gov

.. |PPPRNG|	replace:: bastion-analysis.princeton.rdhpcs.noaa.gov
.. |PPBRNG|	replace:: bastion-analysis.boulder.rdhpcs.noaa.gov
.. |PAPRNG|	replace:: analysis-rsa.princeton.rdhpcs.noaa.gov
.. |PBPRNG|	replace:: analysis-rsa.boulder.rdhpcs.noaa.gov

.. |MCPRNG|	replace:: mercury-cac.princeton.rdhpcs.noaa.gov
.. |MCBRNG|	replace:: mercury-cac.boulder.rdhpcs.noaa.gov
.. |MRPRNG|	replace:: mercury-rsa.princeton.rdhpcs.noaa.gov
.. |MRBRNG|	replace:: mercury-rsa.boulder.rdhpcs.noaa.gov

.. |UCPRNG|	replace:: ursa-cac.princeton.rdhpcs.noaa.gov
.. |UCBRNG|	replace:: ursa-cac.boulder.rdhpcs.noaa.gov
.. |URPRNG|	replace:: ursa-rsa.princeton.rdhpcs.noaa.gov
.. |URBRNG|	replace:: ursa-rsa.boulder.rdhpcs.noaa.gov

.. |OUG|	replace:: :ref:`orion-user-guide`

+-------------------+-----------------+----------------------------------+
| **RDHPCS System** | |CBHN|          | |RBHN|                           |
+-------------------+-----------------+----------------------------------+
| Gaea              | |GCPRNG|        | |GRPRNG|                         |
|                   |                 |                                  |
|                   | |GCBRNG|        | |GRBRNG|                         |
+-------------------+-----------------+----------------------------------+
| Hera              | |HCBRNG|        | |HRBRNG|                         |
|                   |                 |                                  |
|                   | |HCPRNG|        | |HRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Jet               | |JCBRNG|        | |JRBRNG|                         |
|                   |                 |                                  |
|                   | |JCPRNG|        | |JRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| PPAN              | |PPPRNG|        | |PAPRNG|                         |
|                   |                 |                                  |
|                   | |PPBRNG|        | |PBPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Mercury           | |MCBRNG|        | |MRBRNG|                         |
|                   |                 |                                  |
|                   | |MCPRNG|        | |MRPRNG|                         |
+-------------------+-----------------+----------------------------------+
| Ursa              | |UCBRNG|        | |URBRNG|                         |
|                   |                 |                                  |
|                   | |UCPRNG|        | |URPRNG|                         |
+-------------------+-----------------+----------------------------------+

In addition to the Bastions, RDHPCS users have access to computational capacity
on the Orion and Hercules systems, hosted by Mississippi State University. See
the :ref:`MSU-HPC <MSU-HPC-user-guide>` user guide.
for detailed information.

Computational capacity is also available on the RDHPCS Cloud Platform, which
allows NOAA users to create custom HPC clusters on an as-needed basis, through
the Parallel Works platform. The :ref:`Cloud User Guide <cloud-user-guide>`
provides more information.


.. _Common-access:
.. _cac_instructions:

Common Access Card (CAC) SSH Login
==================================

RDHPCS users with a CAC who are logging in from a Windows, Mac, or
Linux system are recommended to use a CAC login. This requires a CAC
reader and software from Tectia. If you recently were issued a new CAC
or renewed CAC, please log into the `Account Information Management`_
website to update the CAC information.

Reference the :ref:`Tectia` pages for complete information on how to
configure Tectia initially for login using SSH with your CAC.

.. code-block:: console

    $ sshg3 CAC-BASTION-HOSTNAME

#. Reference the table above for the appropriate CAC Bastion to use.
#. When prompted, enter your CAC PIN.


.. _rsa_instructions:

RSA SSH Login
=============

RDHPCS users who do not have a CAC, or lack the required hardware or
software, are welcome to use an RSA login.

.. code-block:: console

    $ ssh RSA-BASTION-HOSTNAME


#. Reference the table above for the appropriate RSA Bastion to use.
#. When prompted, enter your PASSCODE which consists of your
   PIN+RSA_CODE.  The RSA_CODE is the 6-8 digit code from the RSA fob or
   RSA app.


Selecting a Node
================

RDHPCS systems accessed via SSH allow users to select a specific head
node at login.  After successful authentication at the bastion host, a
list of available nodes will be displayed with a 5 second delay to
choose a specific destination.  To select a specific host, press
Control+C (^C) and enter the desired node.

Here is an example of what the display looks like for the Gaea system
mid 2024:

.. code-block:: shell


     Welcome to the NOAA RDHPCS.

     Attempting to renew your proxy certificate...Proxy certificate has 720:00:00  (30.0 days) left.

             Welcome to gaea.rdhpcs.noaa.gov
     Gateway to gaea-c5.ncrc.gov and other points beyond

     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     !! RDHPCS Policy states that all user login sessions shall be terminated     !!
     !! after a maximum duration of seven (7) days. ALL user login sessions will  !!
     !! be dropped from the Princeton Bastions at 4AM ET / 2AM MT each Monday     !!
     !! morning, regardless of the duration. Please note: This will NOT impact    !!
     !! batch jobs, cron scripts, screen sessions, remote desktop, or data        !!
     !! transfers.                                                                !!
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

     Hostname            Description
     gaea                C5 head nodes
     gaea51              C5 head node
     gaea52              C5 head node
     gaea53              C5 head node
     gaea54              C5 head node
     gaea55              C5 head node
     gaea56              C5 head node
     gaea57              C5 head node
     gaea58              C5 head node
     gaea60              T6 Test access only
     gaea61              C6 head node
     gaea62              C6 head node
     gaea63              C6 head node
     gaea64              C6 head node
     gaea65              C6 head node
     gaea66              C6 head node
     gaea67              C6 head node
     gaea68              C6 head node

     You will now be connected to NOAA RDHPCS: Gaea (CMRS/NCRC) C5 system.
     To select a specific host, hit ^C within 5 seconds.


.. note::

    After the 5 second wait, the bastion node will use a load balancer to select
    a node.


X11 Graphics
============

Users can use SSH X11 forwarding to open GUI-based applications (e.g., xterm,
ARM Forge).  This is typically done using an SSH option.  For the :ref:`Tectia`
client :command:`sshg3` or OpenSSH-based clients, use the ``-X`` option:

.. code-block:: console

    $ sshg3 -X host.url

or

.. code-block:: console

    $ ssh -X host.url

Other clients, like PuTTY, will have an option when configuring the host.

The base SSH X11 forwarding is typically slow.  RDHPCS systems use X2Go for
improved X11 performance.  Some users have found it difficult to use X2Go.
Please submit a :ref:`support issue <getting_help>` if you have issues using
X2Go.

.. note::

    Microsoft Windows users can use any of the X11 servers available for
    Windows.  The SSH client will need to be configured to use the X11 server
    for forwarding X11.

.. _ssh-port-tunnels:

SSH Port Tunnels
================

To allow users to easily transfer small files to and from the RDHPCS
systems, the bastion configures SSH port-forwarding tunnels.  To use these
tunnels, the user must configure their local SSH client to create tunnels
to/from the bastion.

See the Port Tunnel section of the :ref:`Tectia` page for details.  You can use
:ref:`this form <openssh-config>` to create a sample SSH configuration for
OpenSSH-based clients.



Web based ParallelWorks Access
==============================

See the :ref:`cloud-user-guide` for details on using ParallelWorks in
a web browser to access on-premise and cloud HPCS.
