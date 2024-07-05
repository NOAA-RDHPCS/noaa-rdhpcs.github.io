.. _transferring-data:

*****************
Transferring Data
*****************

Globus Connect Service (GCS) is now available on RDHPCS systems, and
we encourage its use over any other method whenever possible. Some use
cases that involve sites outside the RDHPCS program that may not
support Globus may still use other methods described in this document.

Many users are accustomed to using scp/sftp via service (same as
login) nodes. However, we would like to point out that Data Transfer
Nodes (DTN's) provides a much faster method for transferring data to
and from HPC systems (Jet/Hera/Niagara/Gaea/WCOSS/Orion), so we highly
recommend DTNs over service nodes.

Much data on RDHPCS servers are protected by confidentiality
agreements, may be sensitive, or are otherwise proprietary. Our
obligation includes the enforcement of all policies that make curating
such data even possible. This involves maintaining tight security that
adheres to NOAA OCIO guidelines. We also recognise the need for
sharing data with collaborators who may not be vetted by us to ensure
that NOAA/DOC standards are met. The so-called untrusted DTN was
created so that less secure channels may be open for the smooth
transfer of data essential for projects to conduct their research.

The following section is common for most operating systems and
exceptions are noted.

Only the High-Performance Filesystems (the scratch filesystems) are
available, not your /home filesystem. When you are asked for a
password, provide your RSA Token’s PIN + current 6 or 8 digit number
from your token (a.k.a Passcode).

For Niagara, each user must complete their initial login in order to
set up their user account directories before you can transfer data.
For more information regarding this process and the Niagara directory
structure, see the :ref:`niagara-user-guide`.

Globus Connect
==============

Details and examples are available in the
:ref:`globus_online_data_transfer` section.

Trusted Data Transfer Nodes (DTN)
=================================

By default, trusted DTNs are only accessible from some (but not
necessarly all) hosts within noaa.gov (and Orion). If you need access
to/from a host that is not accessible, we will need to modify system
firewalls.

DTNs support ssh-based authentication transfer methods, which
currently include scp, rsync, and bbcp (Jet and Hera only). Default
authentication uses your RSA token.

.. note::
    If you're using WinSCP on Windows, choose SFTP as the protocol rather than SCP.

+-----------+--------------------------------------+
| Site      | Fully Qualified Host Name            |
+===========+======================================+
| Niagara   | dtn-niagara.fairmont.rdhpcs.noaa.gov |
+-----------+--------------------------------------+
| Hera      | dtn-hera.fairmont.rdhpcs.noaa.gov    |
+-----------+--------------------------------------+
| Jet       | dtn-jet.boulder.rdhpcs.noaa.gov      |
+-----------+--------------------------------------+
| Orion     | orion-dtn.hpc.msstate.edu            |
+-----------+--------------------------------------+
| Hercules  | hercules-dtn.hpc.msstate.edu         |
+-----------+--------------------------------------+


Untrusted Data Transfer Nodes (UDTN)
====================================

Untrusted DTNs (UDTNs) are open systems that are accessible from
anywhere, including your personal machine. It is possible to do data
transfers from most external sites including your local
desktop/laptop. However, note the following important points:

* Before you can use the UDTNs for data transfers on any of the
  clusters (Niagara, Hera, Jet, PPAN, etc.), **you must login
  at least once to set up the necessary directories.**
* File space on the UDTNs is very limited. So it is important to move
  to your project space as soon as possible and clean up
  temporary files. Failure to comply with this policy will force us to
  remove your data and disable your access to this directory.
* You can use Globus Online Data Transfer to transfer data to/from the
  UDTNs. Details and examples are available in the
  :ref:`globus_online_data_transfer` section
* Using "globus flows" may be a good way to accomplish two-step
  transfers since most of the time the data has to be moved off of the
  destination!

.. note::
    If you're using WinSCP on Windows, choose SFTP as the protocol rather than SCP.

* Unattended data transfers are only allowed on the Trusted DTN's, and
  not allowed on any of the Untrusted DTNs.
* **All files under your allocated directories which have not been
  accessed in the last 5 days will be automatically purged!!!**
* You don't have access to all of the file systems on the respective
  systems. Instead, you are only able access the temporary directories
  specific to the system mentioned in the table below:

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Host
     - Globus Collection
     - Hostname for scp, sftp, etc.
     - Accessible top level directories
   * - Niagara
     - noaardhpcs#niagara_untrusted
     - udtn-niagara.fairmont.rdhpcs.noaa.gov
     - /collab1/data_untrusted/$USER
   * - Hera
     - noaardhpcs#hera_untrusted
     - udtn-hera.fairmont.rdhpcs.noaa.gov
     - /scratch[1,2]/data_untrusted/$USER
   * - Jet
     - noaardhpcs#jet_untrusted
     - udtn-jet.boulder.rdhpcs.noaa.gov
     - /lfs[1,4]/data_untrusted/$USER
   * - Gaea
     - ncrc#dtn
     - N/A
     - /lustre/f2/scratch/$USER,
       /ncrc/home1/$USER,
       /ncrc/home2/$USER
   * - PPAN
     - noaardhpcs#ppan_untrusted
     - N/A
     - /collab1/data_untrusted/$USER

Because of the limited space available on the uDTNs, you will be using
two-step transfers:
#. Transfer to the uDTN to the data_untrusted tree above.
#. Transfer to the allocated project space.

The Globus Flows may be useful here in setting up automated 2-step
transfers.

Transfer and Syntax Examples
============================

.. Note::
    Username is case sensitive in the scp command. For example, the username should be in the
    form **First.Last**, rather than **first.last**.
    Replace dtn-<name>.<site>.rdhpcs.noaa.gov with the correct host name listed above.

.. code-block::

    scp /path/to/local/file First.Last@dtn-<name>.<site>.rdhpcs.noaa.gov:/path/on/HPC/System
    First.Last@dtn-<name>.<site>.rdhpcs.noaa.gov's password:

(This is the point where you enter your PIN+RSA Token response)

Transfer a file on Hera to a destination on Jet
-----------------------------------------------

.. code-block::

  [First.Last@hfe04 ~]$ scp /scratch1/SYSADMIN/nesccmgmt/
  First.Last/data_file First.Last@dtn-jet.boulder.rdhpcs.noaa.gov:/mnt/lfs5/SYSADMIN/jetmgmt/First.Last/
  Warning: Permanently added the RSA host key for IP address '140.208.168.55' to the list of known hosts.
  First.Last@dtn-jet.boulder.rdhpcs.noaa.gov's password:
  data_file                                                                  100%   30     0.3KB/s   00:00
  [First.Last@hfe04 First.Last]$

Globus transfer from an external endpoint to the GFDL untrusted endpoint
------------------------------------------------------------------------

This example transfers a file named 'myDataFileName_here.txt' from
'my-personal-endpoint-id' to the untrusted GFDL endpoint,
'6ba73d87-08f2-463e-bf8f-83cc3e7a871f'. The data string
'6ba73d87-08f2-463e-bf8f-83cc3e7a871f' is the actual Globus ID of the
GFDL untrusted endpoint.

To issue the command, replace First.Last in the example with your own
credentials.

.. code-block:: shell

    [First.Last@an001 ~]$ globus transfer my-personal-external-endpoint-id:myDataFileName_here.txt \
    6ba73d87-08f2-463e-bf8f-83cc3e7a871f:First.Last/myDataFileName_there.txt

Firewall Modification Requests for DTNs
=======================================

By default, only hosts in the noaa.gov domain are able to access the
DTNs. If you need to transfer data using the DTNs from hosts that are
not within the noaa.gov domain, you must submit a request to
open the firewall. Please provide the following information:

* **Summary/Justification for transfer:** Why do you need this and for
  how long (permanent or temporary - specify timeframe if temporary)?
* **Source Systems (DNS name)**: dtn-hera.fairmont.rdhpcs.noaa.gov,
  dtn-jet.boulder.rdhpcs.noaa.gov,
  dtn-niagara.fairmont.rdhpcs.noaa.gov
* **Source IPs**: See below for dtn IPs
* **Destination Systems** (DNS name):
* **Destination IPs**: Use the "host" command to find IPs, see below
* **Destination Port name (s):** Service name (dns, http, nfs, bluearc-admin)
* **Destination Port number (s) or range:**
* **Destination Port protocol (tcp/udp):**
* **Direction:** Which way is the connection being initiated? To NOAA
  RDHPCS Systems (inbound) or out from NOAA RDHPCS Systems (outbound)?
* **An example command:** Please include a typical command to show how
  you will be doing the data transfers

  .. code-block:: shell

    dtn-hera.fairmont.rdhpcs.noaa.gov = 140.208.202.[4-5]
    dtn-jet.boulder.rdhpcs.noaa.gov = 140.208.171.[1-4]
    dtn-niagara.fairmont.rdhpcs.noaa.gov = 140.208.202.[76-77]

* Use the "host" command to find IPs

 .. code-block:: shell

    First.Last@hfe04$ host ruc.noaa.gov
    ruc.noaa.gov has address 140.172.12.92

Example
-------

* **Summary/Justification for transfer:** Requesting (permanent) wget
  access to pull data from ruc.noaa.gov via the Hera DTNs to transfer
  weather data to NOAA R&D systems.
* **Source Systems (DNS name):** dtn-hera.fairmont.rdhpcs.noaa.gov,
  dtn-jet.boulder.rdhpcs.noaa.gov,
  dtn-niagara.fairmont.rdhpcs.noaa.gov
* **Source IPs**: 140.208.202.[4-5], 140.208.171.[1-4], 140.208.202.[76-77]
* **Destination Systems:** ruc.noaa.gov
* **Destination IPs:** 140.172.12.92
* **Destination Port name (s):** HTTP/HTTPS, SSH
* **Destination Port number (s) or range:** 80, 22,443
* **Destination Port protocol (tcp/udp):** tcp
* **Direction:** Outbound
* **An example command:** ``wget -r -A "a-deck-ecmwf-wmo*" https://ruc.noaa.gov/hfip/fiorino/tc/ecmwf/2019/wmo/``

Once the information is reviewed and approved by the security team you
will be able to do your data transfers. Please plan ahead for firewall
requests, review by the security team can take up to two weeks, not
including troubleshooting implementation issues.

Unattended Data Transfers or Password-less Transfers to/from RDHPCs Systems
===========================================================================

For real-time experiments that require data to be transferred
automatically, we support unattended data transfers from @noaa.gov
hosts and other trusted hosts. The actual data flow can be in either
direction, but the connection must be initiated from the remote host.

.. Note::
    Unattended data transfers are only allowed on the Trusted DTNs. They are not allowed on Niagara's Untrusted DTNs (UDTNs).

This capability is intended mainly for projects that can demonstrate a
need where unattended data transfer is required. If you need this
capability, answer the following questions and follow the steps below:


* What command will you be using to do the transfers?
* What is the name of the machine where you'll be running the transfer
  command? In the instructions below we will refer to this as the
  **Remote Host.**
* What is the name of the NOAA-RDHPCS machine that you're trying to
  access? We will refer to this as **RDHPCS-HOST**.

1. Copy the ~/.ssh/id_rsa.pub from Remote Host above and place it
on the RDHPCS-HOST in the directory: **~/scp-pubkeys/**.
2. On the RDHPCS-HOST, rename this file so that is is clear where it came
from. For example, if **Remote Host** was "tide", you can rename the file
as follows:

.. code-block:: shell

    mv ~/scp-pubkeys/id_rsa.pub ~/scp-pubkeys/id_rsa.pub-tide

3. Once this is done, send a help request with subject line **Request
   for unattended data transfer capability"** Include the following
   information:

    * Your username on the RDHPCS-HOST.
    * The full path of the file containing the key from Remote Host.
    * The IP address of the Remote Host

.. note::

    **Do not put keys in your home .ssh directory. Put them in
    $HOME/scp-pubkeys directory on RDHPCS-HOST.**

**NOTE TO WCOSS USERS ONLY:** in your ~/.ssh directory. It is located
in this file on WCOSS2: **/u/sshKeys/$USER/id_rsa.pub**. You don't
have to provide the IP addresses when you fill out the information
requested.

If you do not have an RSA key on the remote system (that is, if you do
not have an id_rsa.pub file in your $HOME/.ssh directory) you can
generate it with (at least on Linux) with the command:

.. code-block:: shell

    # ssh-keygen -t rsa

.. warning::

    When you are prompted for a Passphrase, simply press <Enter>.
    Otherwise you will be prompted for "Passphrase" even if you are
    set up for unattended data transfers and will defeat the purpose!

Jet users can use their public key in their /home/$USER/.ssh directory.
If you have difficulties, contact the support staff for help.

Using a Pre-Established SSH Port Tunnel
=======================================

With the SSH port tunnel method, an SSH tunnel is created
between your point of login (typically your desktop) to the remote
host (typically Hera, Jet or other remote hosts). The port tunnel
method will work from any system on the network (that is, your local
machine does not necessarily have to be in the noaa.gov domain). We
recommend using this in cases where DTN is not available.

SSH Port Tunnel from Linux-like systems
---------------------------------------
This method requires two sessions on your local machine: one to
establish the SSH port tunnel, and the other to actually perform the
copy.

Host names for the CAC bastion Server in Boulder, CO:

.. code:: shell

   bastion-jet.boulder.rdhpcs.noaa.gov
   bastion-hera.boulder.rdhpcs.noaa.gov
   bastion-niagara.boulder.rdhpcs.noaa.gov
   bastion-gaea.boulder.rdhpcs.noaa.gov

Host names for the CAC Bastion Server in Princeton, NJ:

.. code:: shell

   bastion-jet.princeton.rdhpcs.noaa.gov
   bastion-hera.princeton.rdhpcs.noaa.gov
   bastion-niagara.princeton.rdhpcs.noaa.gov
   bastion-gaea.princeton.rdhpcs.noaa.gov

Before You Begin
^^^^^^^^^^^^^^^^

In the steps below, replace First.Last with your own HPC username, and
XXXXX with the unique Local Port Number assigned to you when you log
in to your specified HPC system (Hera/Jet). Use the word "localhost"
where indicated. It is not a variable, don't substitute anything else.
Before you perform the first step, close all current sessions on the
HPC where system you are trying to connect. Once the first session has
been opened with port forwarding, any further connections (login via
ssh, copy via scp) will work as expected. You are running these
commands on your local machine, not within the HPC system terminal.

As long as this ssh window remains open, you will be able to use this
forwarded port for data transfers. After the first session has been
opened with the port forwarding, any further connections (login via
ssh, copy via scp) will work as expected.

**1. Find your local port number**

To find your unique local port number, log onto your specified HPC
system (Hera/Jet). Make a note of this number - once you've recorded
it, close all sessions. Note that this number will be different on Jet and
Hera.

.. image:: /images/linux_xfer1.png
   :scale: 75%

.. note::
    Open two terminal windows for this process

**Local Client Window #1**

Enter the following command. Remember to replace XXXXX with the local port
number identified in Step 1 or as needed:

.. code-block:: shell

     ssh -m hmac-sha2-512-etm@openssh.com -L12345:localhost:12345 First.Last@hera-rsa.boulder.rdhpcs.noaa.gov
     ssh -L12345:localhost:12345 First.Last@hera-rsa.boulder.rdhpcs.noaa.gov

If you will be running X11 applications with x2go or normal terminals,
remember to add the -X parameter as follows:

.. code-block:: shell

    ssh -X -LXXXXX:localhost:XXXXX $USER@hera-rsa.boulder.rdhpcs.noaa.gov

Note that objects emphasized in this figure should be unique to your
configuration:

.. image:: /images/linux_xfer2.png
   :scale: 75%

Verify that the tunnel is working by doing the following in another local
window from your local machine:

.. code-block:: shell

   ssh -p <port> First.Last@localhost


Note that <port> is your local port number used above, First.Last is
your user ID on the RDHPCS systems and localhost is typed as-is.

You should be prompted for your password; enter your PIN + RSA token
and you should be able to login. Once you are able to log in, you can
log out of that session as that was only for testing the tunnel.

**2. Use SCP to Complete the Transfer**

**Local Client Window #2**

Once the session is open, you can use this forwarded port
for data transfers, as long as this ssh window is kept open. After the
first session has been opened with the port forwarding, any
further connections (login via ssh, copy via scp) will work as
expected.


Remember that this is the second terminal session opened on your local
machine

To transfer a file **to** HPC Systems

.. code-block:: shell

    scp -P XXXXX /local/path/to/file $USER@localhost:/path/to/file/on/HPCSystems
    rsync <put rsync options here> -e 'ssh -l $USER -p XXXXX' /local/path/to/files $USER@localhost:/path/to/files/on/HPCSystems

.. note::

   Your username is case sensitive when used in the scp command. Username should be in the form of First.Last.

To transfer a file **from** HPC Systems:

.. code-block:: shell

    scp -P XXXXX $USER@localhost:/path/to/file/on/HPCSystems /local/path/to/file
    rsync <put rsync options here> -e 'ssh -l $USER -p XXXXX' $USER@localhost:/path/to/files/on/HPCSystems /local/path/to/files


In either case, you will be asked for a password. Enter the password
from your RSA token (not your passphrase). Your response should be
your PIN+Token code.

SSH Port Tunnel For PuTTy Windows Systems
-----------------------------------------

PuTTY is an SSH client, used to configure and initiate connection.
Navigate to a separate tab to install `PuTTY
<http://www.putty.org/>`_. If you cannot install software on your
machine, contact your local systems administrator.

**Configuration**

Enter host information to configure an SSH Terminal Session. The
example below defines a session to Jet via the Boulder Bastion:

.. image:: /images/putty1.png
   :scale: 75%

1. Enter Username
In the left pane under Connection, select "Data" and enter your NOAA
user name as it appears in your NOAA email address. (Ex: Robin.Lee
if your NOAA email is Robin.Lee@noaa.gov). User name is case
sensitive - First.Last. If you do not create a username, you will have
to enter your user name each time your open a session.

.. image:: /images/putty2.png
   :scale: 75%

Complete the configuration:

* Select "Session" from the top of the left pane.
* Select "Save" (between Load and Delete).

**Open a First System Session**

Open the session to make sure it's working, and to record your Local
Port number to complete the Port Tunneling setup.

* Select the configured session from the "Saved Sessions" list. Select
  Load, then Open.
* Enter your unique RSA Passcode.

The RSA passcode is your RSA token PIN followed by 8 digits displayed
on your RSA token. The digits must be on display when you press enter,
or access will be denied. When you open a new SSH session, wait for
the RSA token code to refresh before you enter it.

* Find and record your Local Host number.

.. image:: /images/linux_xfer1.png
    :scale: 75%

* Click **Exit**, or close the Putty window to end the session.

**Port Tunnel Setup**

To enable data transfers, you will need to set up a Port Tunnel.

* Open Putty.
* Select the session from the Saved Sessions list, then Load.
* In the left pane under Connection>SSH select Tunnels.
* Check Local ports accept connections from other hosts.
* In the Source Port field, enter your Local Port number
* In the Destination Port field, enter "localhost:<local port
  number>", where your local port number matches what was entered in
  the Source port.
* Select Local and Auto Radio Buttons.
* Click the Add Button.

.. image:: /images/putty3.png

To save the configuration change:

* In the left pane, select Session.
* Select Save.

Select **Open** to Login and verify that the updated session works correctly.

Create a new Port Tunnel for each SSH system you intend to use. Each
one will have a unique Local Port number.

To add extra saved sessions (ex: for another Bastion) for the same
system (you already have the Local Port number):

* Load your current saved session
* Enter the new host name for the other Bastion
* Give the new session a new name (ex: Jet - Princeton)
* Select Save. The new session will appear in the list of saved sessions.
* Select Open to Login and verify the new session works correctly.



SSH Port Tunnel For Tectia Windows Systems
------------------------------------------

WinSCP
------

