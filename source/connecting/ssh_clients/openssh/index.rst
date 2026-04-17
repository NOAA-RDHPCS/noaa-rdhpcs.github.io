.. _openssh-client:

*******
OpenSSH
*******

OpenSSH is a free, open-source SSH implementation included by default
on macOS, most Linux distributions, and Windows 10 and later.


Install OpenSSH
===============

OpenSSH is pre-installed on macOS and most Linux distributions.  No
additional installation is needed on those platforms.

On Windows 10 (version 1809 and later) and Windows 11, OpenSSH is
available in PowerShell and Windows Terminal.  Verify it is installed:

.. code-block:: console

   > ssh -V

If the command is not found, see `Windows OpenSSH`_ for installation
instructions.


Configure for RDHPCS
=====================

Use the :ref:`OpenSSH configuration form <openssh-config>` to
generate your ``~/.ssh/config`` file.  The form calculates your
unique port numbers and writes ``LocalForward`` and ``RemoteForward``
directives for each RDHPCS system.

A generated host entry looks like this:

.. code-block:: text

   Host hera-rsa.boulder.rdhpcs.noaa.gov
       User              First.Last
       LocalForward      LOCAL-PORT localhost:LOCAL-PORT
       RemoteForward     REMOTE-PORT localhost:REMOTE-PORT

After you copy the generated configuration into ``~/.ssh/config``,
connect to an RSA bastion to open the tunnels:

.. code-block:: console

   $ ssh RSA-BASTION-HOSTNAME

See :ref:`bastion_hostnames` for RSA bastion hostnames.


.. _openssh-x11:

X11 forwarding
==============

Add the ``-X`` flag to enable X11 forwarding when you connect:

.. code-block:: console

   $ ssh -X RSA-BASTION-HOSTNAME

To open a port tunnel and enable X11 forwarding in the same session,
combine ``-X`` and ``-L``:

.. code-block:: console

   $ ssh -X -L LOCAL-PORT:localhost:LOCAL-PORT RSA-BASTION-HOSTNAME

.. note::

   Before using X11 forwarding, make sure you have an X11 server
   available on your workstation:

   * **Linux** — X11 is available if a desktop environment is running.
   * **macOS** — install `XQuartz`_.
   * **Windows** — install `VcXsrv`_ or `MobaXterm`_.


Port tunnels
============

See :ref:`ssh-port-tunnels` for your LocalForward port number and the
port assignment formula.

Using ``~/.ssh/config``
-----------------------

If you used the configuration form, ``LocalForward`` is already in
your ``~/.ssh/config``.  Connect normally to open the tunnel:

.. code-block:: console

   $ ssh RSA-BASTION-HOSTNAME

.. note::

   Windows PowerShell users must add
   ``-m hmac-sha2-512-etm@openssh.com`` to specify the MAC algorithm:

   .. code-block:: console

      > ssh -m hmac-sha2-512-etm@openssh.com RSA-BASTION-HOSTNAME

   To avoid typing the flag every time, add a ``MACs`` line to the
   host block in ``~/.ssh/config``:

   .. code-block:: text

      Host RSA-BASTION-HOSTNAME
          MACs    hmac-sha2-512-etm@openssh.com

.. warning::

   Tunnels are active only while this SSH session remains open.
   Keep the session running the entire time you need tunnel access.

Manual tunnel command
---------------------

If you prefer to pass tunnel options on the command line instead of
using ``~/.ssh/config``, use the ``-L`` flag.  Replace ``LOCAL-PORT``
with your LocalForward port (see :ref:`ssh-port-tunnels`) and
``RSA-BASTION-HOSTNAME`` with the hostname from the
:ref:`bastion_hostnames` table.

*Linux and macOS:*

.. code-block:: console

   $ ssh -L LOCAL-PORT:localhost:LOCAL-PORT \
     First.Last@RSA-BASTION-HOSTNAME

*Windows PowerShell:*

.. code-block:: console

   > ssh -m hmac-sha2-512-etm@openssh.com `
     -L LOCAL-PORT:localhost:LOCAL-PORT `
     First.Last@RSA-BASTION-HOSTNAME

Verify the tunnel
-----------------

In a second terminal, connect through the local port:

.. code-block:: console

   $ ssh -p LOCAL-PORT First.Last@localhost

You are prompted for your normal credentials (PIN + RSA token or
YubiKey).  A successful login confirms the tunnel works.  Log out of
the test session immediately.


Reference
=========

* `OpenSSH website <https://www.openssh.com/>`__ — project home and
  documentation
* `ssh manual page <https://man.openbsd.org/ssh>`__ — full command
  reference
* `ssh_config manual page <https://man.openbsd.org/ssh_config>`__ —
  configuration file reference
* `Windows OpenSSH`_ — installation and setup for Windows


.. _Windows OpenSSH:
   https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui
.. _XQuartz: https://www.xquartz.org/
.. _VcXsrv: https://sourceforge.net/projects/vcxsrv/
.. _MobaXterm: https://mobaxterm.mobatek.net/
