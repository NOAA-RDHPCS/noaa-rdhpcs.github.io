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

Set up Port Forwarding on your Local client
-------------------------------------------

.. note::
    Each user on the system is assigned a specific Local port number that is
    different for each host. Your assigned Local port on Hera is
    different from the one Jet, but will remain fixed.

On your local machine:

1. Get your assigned **Local port number**.
   If you already know your port number you may skip this step.

2. Login to the appropriate host Hera/Jet/Mercury. In the welcome message look
   for the following line:

  ``Local port <assigned-port-number> forwarded to remote host``

The number after "Local port" is your assigned port number. Note down this
number and log out of the system.

Create a session with the tunnel and keep this session open
-----------------------------------------------------------

.. note::

    Windows users please use PowerShell instead of other clients such as putty.
    Linux users can use the usual ssh command.

Example
^^^^^^^

This example uses **hera** as our host and **12345** as our assigned
Local port number, with a username of First.Last.

.. code-block:: console

  ssh                                  -L12345:localhost:12345 First.Last@hera-rsa.boulder.rdhpcs.noaa.gov    (Linux/Mac users)
  ssh -m hmac-sha2-512-etm@openssh.com -L12345:localhost:12345 First.Last@hera-rsa.boulder.rdhpcs.noaa.gov    (Windows users)

Login, and keep this session open.

Test to make sure the tunnel is working
---------------------------------------

In another local window, type

.. code-block:: console

  ssh -p 12345 First.Last@localhost


Enter your PIN+Token at the prompt. If you are successful, your port tunnel is
all set up and will work long as your session you created is kept
alive.

Login with your VSCode client
-----------------------------

.. note::

    We will assume the following:
    * You have set up the tunnels as mentioned above.
    * You have installed VSCode on your local machine.
    * You have  installed the "Remote-SSH" plugin in your VSCode client.
    * Before you start VSCode, remove any entry containing localhost in your ``~/.ssh/known_hosts`` file

After you start VSCode, you can select the following menu items:

  ``View | Command Palette | Remote-SSH:Connect to host``

When prompted for host, enter:

  ``First.Last@localhost:12345``

.. note::

  Remember to replace First.Last with your user name, and to specify your actual Local Port Number.

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

