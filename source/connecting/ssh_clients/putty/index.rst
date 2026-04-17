.. _putty-client:

*****
PuTTY
*****

.. attention::

   These instructions are for users already familiar with PuTTY who
   want to use it with RDHPCS systems.

`PuTTY`_ is a free, open-source SSH client for Windows.

.. note::

   PuTTY is not compatible with VS Code Remote-SSH.  Use
   :ref:`openssh-client` instead if you use VS Code.


Install PuTTY
=============

Download the installer from the `PuTTY`_ website and run it,
accepting the default installation options.  If you cannot install
software on your workstation, contact your local IT administrator.


Configure for RDHPCS
=====================

Find your bastion hostname in the :ref:`bastion_hostnames` table
before you start.

Create a saved session
-----------------------

#. Open PuTTY.
#. In the **Session** category, enter the bastion hostname in the
   **Host Name** field.  Leave **Port** set to ``22``.

   .. figure:: /images/putty1.png

#. In the left pane, select **Connection > Data**.  Enter your RDHPCS
   username in **Auto-login username**.  Use the ``First.Last``
   format; the username is case sensitive.

   .. figure:: /images/putty2.png

#. In the left pane, select **Session**.  Type a name in the **Saved
   Sessions** field — for example, ``Jet-Boulder`` — then click
   **Save**.
#. Click **Open** to test the connection.


.. _putty-x11:

X11 forwarding
==============

You must install and start a Windows X11 server (`VcXsrv`_ or
`MobaXterm`_) before you connect.  Start the X11 server before
following these steps.

#. Open PuTTY and load your saved session.
#. In the left pane, navigate to **Connection > SSH > X11**.
#. Check **Enable X11 forwarding**.
#. In the left pane, select **Session**, then click **Save**.
#. Click **Open** to connect.


Set up port tunnels
===================

See :ref:`ssh-port-tunnels` for your LocalForward port number before
completing these steps.

#. Open PuTTY.  Select your saved session from the **Saved Sessions**
   list, then click **Load**.
#. In the left pane, navigate to **Connection > SSH > Tunnels**.
#. In the **Source port** field, enter your LocalForward port number.
#. In the **Destination** field, enter ``localhost:LOCAL-PORT``,
   replacing ``LOCAL-PORT`` with the same number you entered in
   step 3.
#. Select the **Local** radio button.

   .. note::

      If tools on other machines on your local network must reach this
      tunnel, also check **Local ports accept connections from other
      hosts**.  For most users this is not required.

#. Click **Add**.

   .. figure:: /images/putty3.png

#. In the left pane, select **Session**, then click **Save**.
#. Click **Open** to connect.  Verify the tunnel from a second
   terminal (see :ref:`ssh-port-tunnels`).

.. warning::

   Tunnels are active only while this PuTTY session remains open.
   Closing the window disconnects the tunnel.

Create a separate saved session for each RDHPCS system, because each
system has a different LocalForward port number.

To add a second bastion for the same system:

#. Load the existing saved session.
#. Change **Host Name** to the other bastion hostname.
#. Enter a new name in **Saved Sessions** — for example,
   ``Jet-Princeton`` — then click **Save**.
#. Click **Open** to verify the new session works.


Reference
=========

* `PuTTY documentation`_ — PuTTY user manual


.. _PuTTY: https://www.putty.org/
.. _PuTTY documentation:
   https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
.. _VcXsrv: https://sourceforge.net/projects/vcxsrv/
.. _MobaXterm: https://mobaxterm.mobatek.net/
