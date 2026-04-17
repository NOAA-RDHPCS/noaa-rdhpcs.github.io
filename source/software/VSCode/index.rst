.. _rdhpcs-VSCode:

******
VSCode
******

.. attention::

    VSCode (Visual Studio Code) is a popular IDE used by a number of
    developers. These instructions are intended for users who are already
    familiar with VSCode, but are not familiar with using it in the RDHPCS
    environment. This section assumes that you have installed this code on your
    local client.


Setting up VSCode for use on RDHPCS systems
===========================================

Set up the install directory
----------------------------

VSCode installs the VSCode server and other plugins on the remote system (on
Hera/Jet for example). Since there is limited space in home directory, we
recommend that you install all VSCode software in your project space.

Create a directory for installation of the VSCode server.
Issue the following commands on each remote host:

.. code-block:: console

   mkdir -p /in/your/project/dir/$USER/vscode-server
   ln -s    /in/your/project/dir/$USER/vscode-server ~/.vscode-server

Set up a port tunnel
--------------------

VSCode Remote-SSH connects to RDHPCS systems through an SSH port
tunnel.  Set up your tunnel using the instructions in
:ref:`ssh-port-tunnels`, then keep that session open while you work
in VSCode.

.. note::

   Windows users must use PowerShell to establish the tunnel, not
   PuTTY.  PuTTY is not compatible with VSCode Remote-SSH.

Login with your VSCode client
-----------------------------

.. note::

   Before connecting, confirm that:

   * Your port tunnel is active.  See :ref:`ssh-port-tunnels`.
   * VSCode is installed on your local machine.
   * The **Remote-SSH** plugin is installed in VSCode.
   * Any ``localhost`` entry is removed from your
     ``~/.ssh/known_hosts`` file.

After you start VSCode, you can select the following menu items:

  ``View | Command Palette | Remote-SSH:Connect to host``

When prompted for host, enter:

  ``First.Last@localhost:LOCAL-PORT``

.. note::

   Replace ``First.Last`` with your username and ``LOCAL-PORT`` with
   your LocalForward port for the system.  See
   :ref:`ssh-port-tunnels` for port number assignments.

.. note::

    VSCode asks you to select the OS of the remote system after you
    enter this information. Select Linux and it will proceed to establish a
    connection.

    The first time you do this, it takes a while (about 2-5 min) to install the server.

.. note::

    If you are already familiar with setting up ``~/.ssh/config`` file, it
    should be possible select an entry from the displayed list of options!

.. CAUTION::

    While VSCode has a plethora of plugins available to help with programming
    tasks, it your responsibility to use them responsibly. In particular, watch
    out for malicious plugins masquerading as genuine plugins!

    When searching for a plugin to install, please be sure to check the spelling and
    make sure you are installing the plugin you think you want before confirming
    the install!

