.. _Common:

######
Common
######

CommonDocs Topics
-----------------

+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| General Information                          | Getting Things Done                           | Data Transfers                                 |
+==============================================+===============================================+================================================+
| **Help Requests**                            | **Applications**                              | Globus Online Data Transfer                    |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Account Management**                       | Applications and Libraries                    |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Getting an Account                           | Containers                                    | Migrating Data Between Local Filesystems       |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| New Device: Software                         | **Running and Monitoring Jobs**               | **Frequently Asked Questions**                 |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Suspension and Reactivation                  | Introduction to SLURM                         |  Recent User-Facing Changes                    |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Role Accounts                                | How SLURM with Fair Share Works               |  Training Documentation                        |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Request    Access to Additional Projects     | Getting Information about your Projects       |  HPC Definitions                               |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| Reset your Master Certificate Password       | Allocations and Quotas                        |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Accessing RDHPCS Systems**                 | Compilers                                     | **Using the HMS HPSS**                         |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+
| **Policies and Best Practices**              | Editing Tools                                 |                                                |
+----------------------------------------------+-----------------------------------------------+------------------------------------------------+


Introduction
============

`Globus Globus Connect Service
(GCS) <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer>`__\ 
is now available on RDHPCS systems, and we encourage its use over any
other method whenever possible. Some use cases that involve sites
outside the RDHPCS program that may not support Globus may still use
other methods described in this document.

Many users are accustomed to using scp/sftp via service (same as login)
nodes. However, we would like to point out that Data Transfer Nodes
(DTN's) provides a much faster method for transferring data to and from
HPC systems (Jet/Hera/Niagara/Gaea/WCOSS/Orion), so we highly recommend
DTNs over service nodes.

Much data on RDHPCS servers are protected by confidentiality agreements,
may be sensitive, or are otherwise proprietary. Our obligation includes
the enforcement of all policies that make curating such data even
possible. This involves maintaining tight security that adheres to NOAA
OCIO guidelines. We also recognise the need for sharing data with
collaborators who may not be vetted by us to ensure that NOAA/DOC
standards are met. The so-called *untrusted DTN* was created so that
less secure channels may be open for the smooth transfer of data
essential for projects to conduct their research.

The following section is common for most operating systems and
exceptions are noted.

Only the High-Performance Filesystems (the scratch filesystems) are
available, **not your /home filesystem**. When you are asked for a
password, provide your RSA Token’s PIN + current 6 digit number (a.k.a
Passcode).

For Niagara each user must complete their initial login in order to set
up their user account directories before you can transfer data. For more
information regarding this process and the Niagara directory structure,
please visit the
`NiagaraDocs <https://niagaradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page>`__
wiki page.

.. _globus_connect:

Globus Connect
==============

For complete details, please visit `Globus Online Data
Transfer <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Globus_Online_Data_Transfer>`__

.. _trusted_data_transfer_node:

Trusted Data Transfer Node
==========================

By default, trusted DTN's (dtn) are only accessible from some hosts
within noaa.gov (and Orion). If you need access to a host not within the
noaa.gov domain, we will need to modify system firewalls. Please see:
`Firewall Modifications for
DTNs <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Transferring_Data#Firewall_Modification_Requests_for_DTNs>`__

| DTN's support ssh-based authentication transfer methods, which
  currently include scp, rsync, and bbcp (Jet and Hera only). Default
  authentication uses your RSA token.
| **Note for Windows Users:** For Windows users using **WinSCP**, please
  choose **SFTP** as the protocol rather than **SCP**.

| \ **Hera:** ``dtn-hera.fairmont.rdhpcs.noaa.gov``
| \ **Niagara:** ``dtn-niagara.fairmont.rdhpcs.noaa.gov``
| \ **Jet:** New DTN's (as of 01/22/21)
  ``dtn-jet.boulder.rdhpcs.noaa.gov``
| \ **Jet:** Old DTN's (until 2/9/21) ``dtn-jet.rdhpcs.noaa.gov``
| \ **Orion:** ``orion-dtn.hpc.msstate.edu``

.. _untrusted_data_transfer_node_available_on_niagara_only:

Untrusted Data Transfer Node (Available on Niagara Only)
========================================================

Unlike Trusted DTNs (Used on Jet and Hera), Untrusted DTNs (udtn) are
accessible from anywhere on the internet. They are designed to allow
data to brought in to the RDHPCS program from external sites (Non-NOAA
HPC sites, Cloud providers, Universities, etc...).

**IMPORTANT NOTE:** Before you can use the udtn for doing data
transfers, it is important to login to Niagara once to set up the
necessary directories including your home directory. In order to login
to Niagara, please use one of the following methods for logging in:

RSA login:

| ``   ssh niagara-rsa.princeton.rdhpcs.noaa.gov``
| ``   ssh niagara-rsa.boulder.rdhpcs.noaa.gov``

CAC login:

| ``   ssh bastion-niagara.princeton.rdhpcs.noaa.gov``
| ``   ssh bastion-niagara.boulder.rdhpcs.noaa.gov``

Once you login to Niagara your directories will be created automatically
and ready for use. Then you can use the DTNs available on Niagara for
doing your data transfers.

| DTN's support ssh-based authentication transfer methods, which
  currently include scp, rsync, and bbcp. Default authentication uses
  your RSA token.
| **Note for Windows Users:** For Windows users using **WinSCP**, please
  choose **SFTP** as the protocol rather than **SCP**.

| \ **Niagara:** ``udtn-niagara.fairmont.rdhpcs.noaa.gov``
| **Please note** The udtn (untrusted DTNs) on only access the following
  file system: /collab1/data_untrusted/

So typically you will be copying files in and out of
**/collab1/data_untrusted/$USER**.

**Unattended data transfers are only allowed on the Trusted DTN's;
therefore they are not allowed on Niagara's Untrusted DTNs.**

.. _transfer_syntax_and_examples:

Transfer Syntax and Examples
============================

| **Note:** Username is case sensitive in the scp command. For example,
  the username should be in the form **J**\ ohn.\ **S**\ mith rather
  than **j**\ ohn.\ **s**\ mith.
| Replace \ **dtn-..rdhpcs.noaa.gov**\  with the correct host name
  listed above.

| ``scp /path/to/local/file First.Last@``\ \ **``dtn-``\ \ ``.``\ \ ``.rdhpcs.noaa.gov``**\ \ ``:/path/on/HPC/System``
| ``First.Last@dtn-``\ \ ``.``\ \ ``.rdhpcs.noaa.gov's password:``
| ``(This is the point where you enter your PIN+RSA Token response)``

**Example of a transfer for a file on Hera to a destination on Jet:**

::

   [First.Last@hfe04 ~]$ scp /scratch1/SYSADMIN/nesccmgmt/First.Last/data_file First.Last@dtn-jet.boulder.rdhpcs.noaa.gov:/mnt/lfs1/SYSADMIN/jetmgmt/First.Last/
   Warning: Permanently added the RSA host key for IP address '140.208.168.55' to the list of known hosts.
   First.Last@dtn-jet.boulder.rdhpcs.noaa.gov's password: 
   data_file                                                                           100%   30     0.3KB/s   00:00    
   [First.Last@hfe04 First.Last]$ 

.. _firewall_modification_requests_for_dtns:

Firewall Modification Requests for DTNs
=======================================

As mentioned above, by default only hosts in the noaa.gov domain are
able to access the DTNs. If you need to transfer data using the DTNs
from hosts that are not within the noaa.gov domain, you will have to
submit a request to open the firewall. Please provide the following
information:

| \ **Summary/Justification for transfer:**\  Why do you need this and
  for how long (permanent or temporary - specify timeframe if
  temporary)?
| \ **Source Systems (DNS name):**\ 
  \ **dtn-hera.fairmont.rdhpcs.noaa.gov**\ ,
  \ **dtn-jet.boulder.rdhpcs.noaa.gov**\ ,
  \ **dtn-niagara.fairmont.rdhpcs.noaa.gov**\ 
| \ **Source IPs:**\  See below for dtn IPs
| \ **Destination Systems (DNS name):**\ 
| \ **Destination IPs:**\  Use the "host" command to find IPs, see below
| \ **Destination Port name (s):**\  Service name, i.e. dns, http, nfs,
  bluearc-admin)
| \ **Destination Port number (s) or range:**\ 
| \ **Destination Port protocol (tcp/udp):**\ 
| \ **Direction:**\  Which way is the connection being initiated? To HPC
  Systems (inbound) or out from HPC Systems (outbound)?
| \ **An example command showing the command you will be using to do the
  data transfers:**\ 

::

   dtn-hera.fairmont.rdhpcs.noaa.gov = 140.208.202.[4-5]
   dtn-jet.boulder.rdhpcs.noaa.gov = 140.208.171.[1-4]
   dtn-niagara.fairmont.rdhpcs.noaa.gov = 140.208.202.[76-77]

-  Use the "host" command to find IPs

::

   [First.Last@hfe04]$ host ruc.noaa.gov
   ruc.noaa.gov has address 140.172.12.92

**Completed Example:**

| \ **Summary/Justification for transfer:**\  requesting (permanent)
  wget access to pull data from ruc.noaa.gov via the Hera DTNs to
  transfer weather data to NOAA R&D systems.
| \ **Source Systems (DNS name):**\  dtn-hera.fairmont.rdhpcs.noaa.gov,
  dtn-jet.boulder.rdhpcs.noaa.gov, dtn-niagara.fairmont.rdhpcs.noaa.gov
| \ **Source IPs:**\  140.208.202.[4-5], 140.208.171.[1-4],
  140.208.202.[76-77]
| \ **Destination Systems (DNS name):**\  ruc.noaa.gov
| \ **Destination IPs:**\  140.172.12.92
| \ **Destination Port name (s):**\  HTTP/HTTPS, SSH
| \ **Destination Port number (s) or range:**\  80, 22,443
| \ **Destination Port protocol (tcp/udp):**\  tcp
| \ **Direction:**\  Outbound
| \ **An example command showing the command you will be using to do the
  data transfers:**\ 
  ``wget -r -A "a-deck-ecmwf-wmo*"``\ ```https://ruc.noaa.gov/hfip/fiorino/tc/ecmwf/2019/wmo/`` <https://ruc.noaa.gov/hfip/fiorino/tc/ecmwf/2019/wmo/>`__

Once the information is reviewed and approved by the security team you
will be able to do your data transfers. Please plan ahead for firewall
requests, review by the security team can take up to two weeks, not
including troubleshooting implementation issues.

.. _unattended_data_transfers_or_password_less_transfers_tofrom_hpc_systems:

Unattended Data Transfers or Password-less Transfers to/from HPC Systems
========================================================================

For real-time experiments that require data to be transferred
automatically, we support unattended data transfers from **.noaa.gov**
hosts and other trusted hosts. The actual data flow can be in either
direction, but the connection **must be initiated from the remote
host**.

**Unattended data transfers are only allowed on the Trusted DTN's;
therefore they are not allowed on Niagara's Untrusted DTNs.**

This capability is intended mainly for projects that can demonstrate a
need where unattended data transfer is required. If you need this
capability please do the following:

Please answer the following questions and follow the steps indicated
below:

-  What is the command you will be using to do the transfers?
-  What is the name of the machine where you'll be running the transfer
   command? In the instructions below we will refer to this as the
   **Remote Host**.
-  What is the name of the NOAA-RDHPCS machine that you're trying to
   access? We will refer to this as **RDHPCS-HOST**.

　

Please copy the **~/.ssh/id_rsa.pub** from **Remote Host** above and
place it on the **RDHPCS-HOST** in the following directory:
**~/scp-pubkeys/**; Then on the **RDHPCS-HOST**, rename this file so
that is is clear where it came from; for example, if "Remote Host" was
"tide" you can rename the file as follows:

``mv ~/scp-pubkeys/id_rsa.pub ~/scp-pubkeys/id_rsa.pub-tide``

Once this is done, please send a help request with the following
information with the subject line "Request for unattended data transfer
capability":

-  Your username on the RDHPCS-HOST.
-  The full path of the file that contains the key from "Remote Host"
   mentioned above
-  The IP address of the "Remote Host"

**Please do not put your key in your home .ssh directory. Put them in
$HOME/scp-pubkeys directory on RDHPCS-HOST as mentioned above.**

.. _generating_an_rsa_key_only_if_you_do_not_already_have_an_rsa_key:

Generating an RSA key (only if you do not already have an RSA key)
------------------------------------------------------------------

If you do not have an RSA key (that is if you do not have an id_rsa.pub
file in your $HOME/.ssh directory) on the remote system, you can
generate it with (at least on Linux):

::

   # ssh-keygen -t rsa -b 1024

**Note: It is important to simply press when prompted for "Passphrase".
If not, you will be prompted for "Passphrase" even if you are set up for
unattended data transfers and will defeat the purpose!**

Note, this might not work on all systems and if it doesn't you should
contact your local support staff for help.

Jet users can use their public key in their /home/$USER/.ssh directory

.. _using_a_pre_established_ssh_port_tunnel:

Using a Pre-Established SSH Port Tunnel
=======================================

The SSH port tunnel method is one where an SSH tunnel is created between
your point of login (typically your desktop) to the remote host
(typically Hera, Jet or other remote hosts). The port tunnel method will
work from any system on the network (that is, your local machine does
not necessarily have to be in the **noaa.gov** domain). We recommend
using this in the case where DTN is not available.

.. _ssh_port_tunnel_from_linux_like_systems:

SSH Port Tunnel From Linux-like Systems
---------------------------------------

Please see the following link:

-  `SSH Port Tunnel - Linux-like
   Systems <transferring_data_pt_linux-like_systems>`__

.. _ssh_port_tunnel_from_windows_systems:

SSH Port Tunnel From Windows Systems
------------------------------------

Please see the following links for establishing the port tunnel and then
resume the remaining steps from this page:

-  `SSH Port Tunnel for PuTTY - Windows
   Systems <Transferring_Data_for_Windows_Systems_-_Putty>`__
-  `SSH Port Tunnel for Tectia - Windows
   Systems <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/CAC_Login#Port_Tunneling_Setup>`__

WinSCP
------

**BEFORE** you use WinSCP, you must have a port tunnel established.
Please see the above instructions to do so.

| Configure the port forwarding for WinSCP using the above method that
  matches your system configuration. Once port forwarding is configured,
  open and configure WinSCP. Please be sure to select **SFTP** as the
  file protocol as shown below.
| **NOTE:** The port-forwarded session ** must stay active** to maintain
  a connection to WinSCP. Use the word “localhost” where indicated. It
  is **not** a variable, don't substitute with anything else.

.. figure:: WinSCP.JPG
   :alt: WinSCP.JPG
   :width: 700px

When prompted for a password, enter your RSA PIN + RSA Token:

.. figure:: WinSCP_Password.JPG
   :alt: WinSCP_Password.JPG

.. _external_data_transfers_applies_to_nescc_ie._hera_and_niagara_only:

External Data Transfers (applies to NESCC, ie. Hera and Niagara only)
---------------------------------------------------------------------

The eDTNs that facilitated data transfers between non-NOAA sites and
NESCC is being decommissioned as this same functionality is available by
using the untrusted DTN (udtn-niagara.fairmont.rdhpcs.noaa.gov).

Please see the following for using the UDTN for Niagara for doing your
data transfer to/from untrusted hosts:

https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Transferring_Data#Untrusted_Data_Transfer_Node_.28Available_on_Niagara_Only.29

.. _internally_initiated_transfers:

Internally Initiated Transfers
------------------------------

HPC systems do not have any specific hosts for internally initiated
transfers (unlike the Data Transfer Nodes (known as dtns) which permit
data transfers **to** HPC Systems that are initiated externally).
Transfers initiated from HPC Systems will be using the front end nodes
for doing the transfers.

**The firewall rules are set up by default to block all outgoing
traffic**. However, we will permit internally initiated transfers by
request, after the request is reviewed and approved by the security
team. If you need this capability please send an email to the `Help
System <Help_Requests>`__ that contains your request along with the
following information (please use the following subject line:
\ **<$SYSTEM> FEs to <$HOSTNAME>**\  and use the appropriate system and
hostname):

::

   Hera:
   Source Systems:  hfe[1-12].fairmont.rdhpcs.noaa.gov
   Source IPs:  140.208.193.[1-12]

   Jet:
   Source Systems:  fe[1-8].boulder.rdhpcs.noaa.gov
   Source IPs:  140.208.160.[1-8]

   Niagara:
   Source Systems:  nfe[1-12].fairmont.rdhpcs.noaa.gov
   Source IPs:140.208.193.[65-76]

| Justification:
| Source Systems:
| Source IPs:
| Destination Systems (DNS name):
| Destination IPs: (done via the terminal command ``host``\ 
| Destination Port name (s) (service name, i.e. dns, http, nfs,
  bluearc-admin):
| Destination Port number (s) or range:
| Destination Port protocol (tcp/udp):
| Example of a command that will be used to do the transfers:

**Example:**

**Subject:** Hera FEs to podaac-tools.jpl.nasa.gov

| Justification: requesting (permanent) wget access to pull data from
  podaac-tools.jpl.nasa.gov via the Hera front ends to transfer weather
  data to NOAA.
| Source Systems: hfe[01-12].fairmont.rdhpcs.noaa.gov,
  fe[1-8].boulder.rdhpcs.noaa.gov, nfe[1-4].boulder.rdhpcs.noaa.gov
| Source IPs: 140.208.192.[9-18], 140.208.160.[1-8], 140.208.193.[65-68]
| Destination Systems (DNS name): podaac-tools.jpl.nasa.gov
| Destination IPs: 128.149.132.160
| Destination Port name (s) (service name, i.e. dns, http, nfs,
  bluearc-admin): HTTP/HTTPS, ssh
| Destination Port number (s) or range: 80, 22,443
| Destination Port protocol (tcp/udp): tcp
| Using the command:
  ``wget -r -A.nc``\ ```https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal`` <https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal>`__\ ``--2019-05-13 15:34:09--``\ ```https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal`` <https://podaac-tools.jpl.nasa.gov/measures-drive/files/mur_sst/tmchin/seasonal>`__

.. _using_bbcp_fromto_hera:

Using BBCP from/to Hera
-----------------------

To begin, most all tools are not loaded by default. You need to load
bbcp before you can use it:

::

   # module load bbcp

BBCP is a high performance transfer tool that can sustain 100s of MB/s
(depending on your transfer link). The syntax is mostly similar to scp.
**However, you have to use one of the dtn1 names explicitly such as
tdtn1-vip, tdtn2-vip, tdtn3-vip, or tdtn4-vip below**:

::

   # bbcp myfile hdtn1.fairmont.rdhpcs.noaa.gov:/scratch2/blah/myfile

**You have to use a specific dtn such as tdtn1-vip as opposed to
dtn-hera because the latter picks up a specific DTN in a roundrobin
fashion and that will not work.**

However, to make things go fast, you need to include additional options.
Below are some good settings (please note that you can use one of four
DTNs by changing the number for tdtn1-vip) :

::

   # bbcp -s 8 -w 16M myfile hdtn1.rdhpcs.noaa.gov:/scratch2/blah/myfile

Other useful options:

::

   -f Force an overwrite
   -P 1 display the transfer statics every N seconds, in this case 1 second.
   -r Transfer data recursively
   -z Reverse connection initiation (You may need this option of dtn-hera is not the destination)

**Note**: Please try the "-z" option above if you are experiencing
problems with the default options.

Also see:

::

   # bbcp -v

For more options.

.. _tuning_hosts_to_improve_data_transfer_rates:

Tuning Hosts to Improve Data Transfer Rates
-------------------------------------------

The standard tuning parameters for network settings are not optimal for
high-latency transfers, which means any transfers to and from Hera
unless you are in West Virginia. These settings are specific to where
you and the latency between your system and Hera. A good place to start
is to change the settings on your local host to match:

::

   net.core.rmem_max=16777216
   net.core.wmem_max=16777216
   net.ipv4.tcp_rmem=4096 87380 16777216
   net.ipv4.tcp_wmem=4096 65536 16777216

A good reference for how to tune your host can be found
`here <http://fasterdata.es.net/host-tuning/>`__.

But additional tuning can be done depending on where your system is
located, the type of network interface your host has, and many other
options. Please work with your local network administrators to help tune
your local hosts to maximize network performance.

.. _troubleshooting_data_transfer_issues:

Troubleshooting Data Transfer Issues
====================================

.. _i_am_unable_to_do_scp_transfers_which_were_working_fine_until_recently:

I am unable to do scp transfers which were working fine until recently
----------------------------------------------------------------------

| When you enter your incorrect token ID at any time (either with ssh or
  scp), your account may get locked. One way to reset your locked token
  is to open an new SSH session.
| Open a new ssh session using one of the RSA bastions - see host names
  here: `RSA Login
  Instructions <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/RSA_Login>`__

After you log in, it will ask you to confirm your token by asking you to
reenter the token after waiting for it to change. Once you do that your
account will be unlocked, and then your normal scp commands will work.

**Please note that you have to use RSA authentication for this step even
if you normally use Tectia with CAC authentication.**

.. _warning_remote_host_identification_has_changed:

WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
------------------------------------------------

::

   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
   Someone could be eavesdropping on you right now (man-in-the-middle attack)!
   It is also possible that a host key has just been changed.
   The fingerprint for the RSA key sent by the remote host is
   SHA256:lU91/IcK9rcFKIh1txPP1nfI0+JgNaj9IElGqftsc5H.
   Please contact your system administrator.
   Add correct host key in /Users/first.last/.ssh/known_hosts to get rid of this message.
   Offending RSA key in /Users/first.last/.ssh/known_hosts:5
   RSA host key for [localhost]:55362 has changed and you have requested strict checking.
   Host key verification failed.

Remove the key located in the file specified in the error message from
your **local host - NOT Jet/Hera/Gaea**:

::

   /Users/first.last/.ssh/known_hosts

The **:5** tells you the line where the key is located in the file:

::

   Offending RSA key in /Users/first.last/.ssh/known_hosts:5

.. _i_am_unable_to_do_data_transfers_using_the_tectia_file_tranfer_client:

I am unable to do data transfers using the Tectia file tranfer client
---------------------------------------------------------------------

Please keep in mind that when using the Tectia software, it is only the
ssh client that should be used for interactive logins. For all other
activities such as file transfers, remote desktop clients, etc. you
should be using your regular scp clients with your RSA token
authenication:

-  Typically WinSCP for windows users
-  Typically scp for non-Windows users

So please do not use the Tectia file transfer plans at all! Whether you
are using the DTN (Data Transfer Nodes) or the port tunneling method
please use the file transfer methods mentioned above and use RSA token
for authentication (and not CAC authentication).

#######
Elements
#######

.. toctree::
   :maxdepth: 2

Transferring_Data
   