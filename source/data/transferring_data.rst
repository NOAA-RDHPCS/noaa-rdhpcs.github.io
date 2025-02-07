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
and from HPC systems (Jet/Ursa/Hera/Niagara/Gaea/WCOSS/Orion), so
we highly recommend DTNs over service nodes.

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

By default, trusted Data Transfer Nodes are only accessible from some
hosts within noaa.gov (and Orion). If you need access
to/from a host that is not accessible, we will need to modify system
firewalls. See :ref:`firewall-modifications` for directions.

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
| Ursa      | dtn-ursa.fairmont.rdhpcs.noaa.gov    |
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
  clusters (Niagara, Ursa, Hera, Jet, PPAN, etc.), **you must login
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
     - :file:`/collab1/data_untrusted/$USER`
   * - Ursa
     - noaardhpcs#ursa_untrusted
     - udtn-ursa.fairmont.rdhpcs.noaa.gov
     - :file:`/scratch[34]/data_untrusted/$USER`
   * - Hera
     - noaardhpcs#hera_untrusted
     - udtn-hera.fairmont.rdhpcs.noaa.gov
     - :file:`/scratch[12]/data_untrusted/$USER`
   * - Jet
     - noaardhpcs#jet_untrusted
     - udtn-jet.boulder.rdhpcs.noaa.gov
     - :file:`/lfs[56]/data_untrusted/$USER`
   * - Gaea
     - noaardhpcs#gaea
     - N/A
     - :file:`/gpfs/f[56]`, :file:`/ncrc/home[12]/$USER`
   * - Orion
     - msuhpc2#orion-dtn
     - orion-dtn.hpc.msstate.edu
     - :file:`/work, /work2`
   * - Hercules
     - msuhpc2#hercules
     - hercules-dtn.HPC.MsState.Edu
     - :file:`/work, /work2`
   * - PPAN
     - noaardhpcs#ppan_untrusted
     - N/A
     - :file:`/collab1/data_untrusted/$USER`

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
  First.Last/data_file First.Last@dtn-jet.boulder.rdhpcs.noaa.gov:/mnt/lfs6/SYSADMIN/jetmgmt/First.Last/
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

.. _firewall-modifications:

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

.. _established-tunnel:

Using a Pre-Established SSH Port Tunnel
=======================================

With the SSH port tunnel method, an SSH tunnel is created
between your point of login (typically your desktop) to the remote
host (typically Hera, Jet or other remote hosts). The port tunnel
method will work from any system on the network (that is, your local
machine does not necessarily have to be in the noaa.gov domain). We
recommend using this in cases where DTN is not available.

.. _ssh-tunnel:

SSH Port Tunnel from Linux-like systems
---------------------------------------
This method requires two sessions on your local machine: one to
establish the SSH port tunnel, and the other to actually perform the
copy.

Host names for the CAC bastion Server in Boulder, CO:

.. code:: shell

   bastion-jet.boulder.rdhpcs.noaa.gov
   bastion-ursa.boulder.rdhpcs.noaa.gov (WIP)
   bastion-hera.boulder.rdhpcs.noaa.gov
   bastion-niagara.boulder.rdhpcs.noaa.gov
   bastion-gaea.boulder.rdhpcs.noaa.gov

Host names for the CAC Bastion Server in Princeton, NJ:

.. code:: shell

   bastion-jet.princeton.rdhpcs.noaa.gov
   bastion-ursa.princeton.rdhpcs.noaa.gov (WIP)
   bastion-hera.princeton.rdhpcs.noaa.gov
   bastion-niagara.princeton.rdhpcs.noaa.gov
   bastion-gaea.princeton.rdhpcs.noaa.gov


WinSCP
------

.. note::
  You must have a port tunnel established before you can use WinSCP.
  Configure the port forwarding for WinSCP using the method that
  matches your system configuration.
  For details, see :ref:`create-port-tunnel`.

.. note::
  The port-forwarded session must remain
  active to maintain a connection to WinSCP. Use the word “localhost”
  where indicated. It is not a variable, don't substitute with anything
  else.

Once port forwarding is configured, open and configure WinSCP. Please
be sure to select SFTP as the file protocol.

.. image:: /images/winSCP1.png
  :scale: 50%

When prompted for a password, enter your RSA PIN + RSA Token:

.. image:: /images/winSCP2.png
  :scale: 75%

External Data Transfers (applies to NESCC, ie. Hera and Niagara only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Internally Initiated Transfers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HPC systems do not have specific hosts for internally initiated
transfers ransfers initiated from HPC Systems use the front end nodes
for doing the transfers.

The firewall rules are set up by default to block all outgoing
traffic. However, we permit internally initiated transfers by request,
after the request is reviewed and approved by the security team. If
you need this capability, send an email to the Help System that
contains your request. Use the subject line: <$SYSTEM> FEs to
<$HOSTNAME> with the appropriate system and hostname.

.. code-block:: shell

  Hera:
  Source Systems:  hfe[1-12].fairmont.rdhpcs.noaa.gov
  Source IPs:  140.208.193.[1-12]
  Jet:
  Source Systems:  fe[1-8].boulder.rdhpcs.noaa.gov
  Source IPs:  140.208.160.[1-8]
  Niagara:
  Source Systems:  nfe[1-12].fairmont.rdhpcs.noaa.gov
  Source IPs:140.208.193.[65-76]

Include the following information in the request:

* **Justification**
* **Source Systems**
* **Source IPs**
* **Destination Systems**
* **Destination IPs**
* **Destination Port name (s):** Service name (dns, http, nfs, bluearc-admin)
* **Destination Port number (s) or range:**
* **Destination Port protocol (tcp/udp):**
* **Example command:** Please include a typical command to show how
  you will be doing the data transfers


----

Example
-------

* **Subject:** Hera FEs to podaac-tools.jpl.nasa.gov
* **Justification:** Requesting (permanent) wget access to pull data
  from podaac-tools.jpl.nasa.gov via the Hera front ends to transfer
  weather data to NOAA.
* **Source Systems:** hfe[01-12].fairmont.rdhpcs.noaa.gov,
  fe[1-8].boulder.rdhpcs.noaa.gov, nfe[1-4].boulder.rdhpcs.noaa.gov
  dtn-niagara.fairmont.rdhpcs.noaa.gov
* **Source IPs:** 140.208.192.[9-18], 140.208.160.[1-8],
  140.208.193.[65-68]
* **Destination Systems:** podaac-tools.jpl.nasa.gov
* **Destination IPs:**  128.149.132.160
* **Destination Port name (s):** HTTP/HTTPS, SSH
* **Destination Port number (s) or range:** 80, 22,443
* **Destination Port protocol (tcp/udp):** tcp
* **Direction:** Outbound
* **An example command:**

.. code-block:: shell

  ``wget -r  -A.nc  https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal``

  ``--2019-05-13  15:34:09--https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal``


Tuning Hosts to Improve Data Transfer Rates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The standard tuning parameters for network settings are not optimal
for high-latency transfers, which means any transfers to and from Hera
unless you are in West Virginia. These settings are specific to where
you and the latency between your system and Hera. A good place to
start is to change the settings on your local host to match:

.. code-block:: shell

    net.core.rmem_max=16777216
    net.core.wmem_max=16777216
    net.ipv4.tcp_rmem=4096 87380 16777216
    net.ipv4.tcp_wmem=4096 65536 16777216

A good reference for how to tune your host can be found `here <http://fasterdata.es.net/host-tuning/>`_.

Additional tuning can be done depending on where your system is
located, the type of network interface your host has, and many other
options. Please work with your local network administrators to help
tune your local hosts to maximize network performance.
