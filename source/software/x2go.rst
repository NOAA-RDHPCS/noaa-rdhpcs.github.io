.. _x2go-remote-desktop:

X2Go Remote Desktop
===================


`X2Go <https://wiki.x2go.org/doku.php>`_ is an open source, `remote desktop
<https://en.wikipedia.org/wiki/Remote_desktop>`__ solution designed to work
well over low and high bandwidth connections.

X2Go is supported on all RDHPCS systems to allow:

* A single graphical `MATE <https://mate-desktop.org/>`__ remote desktop running on one
  front end (FE) node.
* The ability to disconnect and reconnect to a session, even from another
  client.
* Secure traffic through a SSH tunnel.

The RDHPCS does not support these X2Go features:

* support for sound
* file Sharing from client to server
* printer Sharing from client to server
* desktop environments other then MATE
* desktop sharing

.. note::

    The systems at Mississippi State University (MSU) use the web-based
    application `Open OnDemand <https://openondemand.org/>`_ to facilitate
    remote desktop connection.  Please refer to MSU's `Open OnDemand User Guide
    <https://intranet.hpc.msstate.edu/helpdesk/resource-docs/ood_guide.php>`__
    for more information.

Requirements
------------

To use X2Go on an RDHPCS system, you must have an `active SSH Connection
<ssh_access>`_ with properly configured `SSH tunnels <port-tunnels>`_.

`Acquire
<https://wiki.x2go.org/doku.php/download:start#the_client-side_of_x2go>`__ and
`install <https://wiki.x2go.org/doku.php/doc:installation:x2goclient>`__ the
`X2Go client <https://wiki.x2go.org/doku.php/doc:usage:x2goclient>`_ on your
local system.

.. note::

   If you are not allowed to install software on your local computer please see
   your local desktop support representative.

Configure X2Go
--------------

.. figure:: /images/x2go_newSession.png
    :align: right
    :figwidth: 35%
    :alt: X2Go new session dialog

    An example of an RDHPCS configuration for X2Go.


Open the `X2Go client` (you can use the desktop icon or use run the
``x2goclient`` command.), and select :menuselection:`Session --> New session`.
If you do not have any configured X2Go sessions, the X2Go client will open the
new session dialog window automatically.

Set the following conferation items, then click :guilabel:`OK`.

:Session name: Name the session configuration something that has meaning to
    you, for example the system name (Gaea, Hera, etc.)
:Path:   /
:Host: *127.0.0.1* or *localhost*
:Login: Use your RDHPCS *First.Last* username.  This is case sensitive.
:SSH port: <ssh_port>  This must match your unique :ref:`SSH local forward port
    number <ssh-port-tunnels>`
:Session type: MATE

.. hint::

    You can change the desktop window size in the :guilabel:`Input/Output`
    panel of the session preferences dialog.


Launch X2Go Session
-------------------

.. figure:: /images/x2go_session.png
    :align: right
    :figwidth: 33%
    :alt: X2Go session window

    X2Go session window with an RDHPCS host configured.

Open an `SSH connection <ssh_access>`_ that will establish the
`SSH local forward <port-tunnels>`_ to the RDHPCS host.  Once the SSH
connection is established, open the X2Go client and double click the session in
the list in the right side bar. When the authentication dialog box appears,
ensure your user name is correct and enter your :ref:`RSA passcode
<rsa_instructions>`.

.. image:: /images/x2go_password.png
    :scale: 30%

Then click :guilabel:`OK` to initiate the session.  Initial connections may
take some time to complete.  If your login succeeds, a new window will appear
showing you a MATE desktop environment. You are now ready to use your remote
desktop as you would on a local system.

.. important::

    CAC Login in the x2go client is not supported.

.. important::

    Your initial SSH Terminal session to the System *must remain open*'''* for
    the X2Go session to work for that system.




X2Go Tips
---------

Some users have found that ensuring that only one connection, the first
connection that estabilshes the SSH port forwards, when starting an X2Go
session allows for the best chance of allowing X2Go to launch the desktop
session.  After the X2Go session is active, you can open additional SSH
sessions as you desire.

You must have no previous X2Go sessions open on any other nodes on a given
RDHPCS system.  This is because X2Go places session items in your home
directory, and X2Go will try and fail to connect to another, existing session
on the current front end node.  This can lead to an X2Go configuration that is
unusable on that system.

On some systems, you can use the ``/apps/local/bin/x2go-killallsessions.sh``
application to make sure you do not have any active X2Go sessions on the
system.

It is generally a good idea to exit the session cleanly by logging out or
suspending a session. Avoid ending a session by simply closing the window.

.. note::

    The :ref:`Gaea <gaea-user-guide>` and :ref:`PPAN <ppan-user-guide>` systems
    do not have the ``x2go-killallsessions.sh`` application.


Troubleshooting X2Go
--------------------

.. attention::

    Not all users have had success configuring X2Go sessions, including members
    of the RDHPCS support team.  We are looking for other, more reliable remote
    desktop application.

.. note::

    Please read thoroughly through the troubleshooting section before
    submitting a :ref:`help request <getting_help>`.

Getting X2Go to work can, at times, be difficult.  The RDHPCS support team is
not sure why this is.  If you have difficulties getting X2Go to work, please
try the following.

.. topic:: Terminate all SSH sessions

    Sometimes, exiting all current open SSH sessions, waiting a moment and then
    opening just the initial connection to establish the local forward port
    will help.

.. topic:: Ensure your login scripts are causing an issue

    Sometimes user settings in their shell login scripts can cause problems
    with X2Go.  For example, ``.cshrc``, ``.tcshrc``, ``.profile``,
    ``.bash_profile``, ``.bashrc``.  This is especially true if messages are
    printed to the terminal at login.  Try moving these scripts out of the way,
    and then try establishing the X2Go session.

.. topic:: Try a different bastion

    Try a different bastion host for the connections.  For example, if you
    tried using the Boulder bastion, try the Princeton bastion.

.. topic:: Wait a few minutes before restoring an X2Go session

    Sometimes waiting a few minutes to connect to a suspended X2Go session will
    allow you to restore the suspended session.

.. topic:: Avoid editing session configurations with active sessions

    The X2Go client can hang if you edit a session while you have an active
    session.  Avoid creating new, or editing existing configurations with open
    sessions.

.. topic:: .config/caja setting error

    X2Go needs to write to the path ``.config/caja``.  At times, this path may
    have the wrong owner information.  If you get an error similar to:

        The path for the directory containing caja settings needs read and
        write permissions: /home/First.Last/.config/caja

    open a :ref:`help desk request <getting_help>`.

.. topic:: Access Denied

    If your login fails with "Access Denied", you will be sent back to the
    login screen. This can happen for a number of reasons. Please wait for your
    RSA token number to change and then try again. If this does not work,
    please close all SSH sessions to the RDHPCS system and try again.

.. topic:: Cannot connect to 127.0.0.1 or localhost

    This error generally occurs when your X2Go session is not working off of a
    port forwarded RDHPCS session.  Please close all RDHPCS system sessions for
    the system you are attempting to connect to and try again.

.. topic:: Bind address already in use

    If you get the message ``bind: Address already in use`` on your initial
    login, this typically indicates wilyou have more than one system session
    open.  For example, you have multiple Hera sessions open.  Please close all
    sessions and open one new session with your configured port tunnel.

.. topic:: Remove stale X2Go sessions and files

    If you've killed all X2Go sessions, but X2Go is still telling you there are
    sessions open, run the following command
    ``/apps/local/bin/x2go-killallsessions.sh``.  This should find and kill any
    lingering sessions and session files that may remain.

    If, after running the above command, you are still unable to open an X2Go
    session, please try the following files:

    .. code-block:: shell

        $ rm -rf /tmp/.x2go-$USER
        $ rm -rf $HOME/.x2go/C-*

.. topic:: Connection failed errors with .ssh issues

    This kind of error can surface if you have something in your startup
    scripts (``.bashrc``, ``.cshrc``, etc.) that would alter the way your shell
    reacts when it is invoked. For example, starting ssh helper programs, such
    as ``ssh-agent`` from your startup scripts would generate output that could
    confuse the process of connecting properly for X2Go. Therefore, it is best
    to remove anything from your startup script that would create any output to
    stderr, or stdout.

    To see if your shell is behaving well in this respect is simple. Start a
    subshell, and see if you get any output. If you do, eliminate anything in
    your startup script that is responsible for it.

.. topic:: Additional Checks

    Below are some additional items to check if the above have not worked.

    * Use `pdsh` to execute ps commands on a set of nodes looking for any
      active X2Go sessions. The below example shows how to do this on Hera.

      .. code-block:: shell

         $ pdsh -w "hfe[01-12]" "ps -eo pid,uname:18,comm | grep x2go | grep $USER | grep -v grep"
         pdsh@hfe03: hfe01: ssh exited with exit code 1
         pdsh@hfe03: hfe03: ssh exited with exit code 1
         pdsh@hfe03: hfe10: ssh exited with exit code 1
         hfe08:  93232 First.Last         /usr/lib64/nx/../x2/x2goagent -extension XFIXES -nolisten tcp -nolisten tcp -dpi 120 -D -auth /home/Raghu.Reddy/.Xauthority -geometry 800x600 -name X2GO-Raghu.Reddy-56-1511972370_stDMATE_dp32 :56
         hfe08:  93345 First.Last         /bin/bash /usr/bin/x2goruncommand 56 93232 Raghu.Reddy-56-1511972370_stDMATE_dp32 37673 mate-session nosnd D
         pdsh@hfe03: hfe07: ssh exited with exit code 1
         pdsh@hfe03: hfe06: ssh exited with exit code 1
         pdsh@hfe03: hfe04: ssh exited with exit code 1
         pdsh@hfe03: hfe05: ssh exited with exit code 1
         pdsh@hfe03: hfe09: ssh exited with exit code 1
         pdsh@hfe03: hfe02: ssh exited with exit code 1


    * Clean up the ``$HOME/.x2go`` directory on both the local and remote
      system.  Please note that removing the ``$HOME/.x2go`` on your local
      machine may remove your X2Go configuration.
    * You may consider rebooting your local machine to clear any lingering
      processes.
    * You can try disabling X forwarding for the just the initial ssh session.
      At least one user found that this eliminated the problem, even though the
      particular session was not used for anything other than setting up the
      X2Go session.

.. warning::

    There are pages on the internet that talk about the ``x2gocleansessions``
    command.  Please do not launch this program, it will not help.

X2Go Help Desk Requests
-----------------------

If you still need assistance after reading the documentation, please contact
the :ref:`help desk <getting_help>` with the following attached to your help
ticket:

* The OS you are using
* The RDHPCS system you are using
* The SSH Client you are using (for example, Tectia, PuTTY, OpenSSH, etc.)
* Include a copy of your SSH client configuration

    * If using CAC, take a snapshot of your CAC Tectia Configuration (the
      :menuselection:`Connection Profile --> Connection Page` **and** the
      :menuselection:`User Authentication --> Keys and Certificates` pages.)
    * If using RSA, take a snapshot of your login session configuration or your
      ``~/.ssh/config`` file.

* Snapshot of your x2go session preferences configuration settings.
* Any error messages you encountered or where you were stuck in the process
* The bastion you are using (Princeton or Boulder)
* Steps you have already attempted

.. seealso::

    `X2Go client`_
        The X2Go client documentation has some help on configuring the client,
        and useful shortcut keys.

    `X2Go FAQ <https://wiki.x2go.org/doku.php/doc:faq:start>`_
        The X2Go FAQ has some additional troubleshooting tips, and includes
        information on how X2Go works.
