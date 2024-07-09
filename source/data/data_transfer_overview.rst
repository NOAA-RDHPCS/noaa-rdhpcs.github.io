.. _data-transfer-overview:

**********************
Data Transfer Overview
**********************

RDHPCS provides several methods to transfer data to and from RDHPCS
systems. Each method has  advantages and
disadvantages or limitations. Users should pick the approach that best
suits their needs based on the information provided here.

For security reasons, access to most external
hosts or sites (including your laptop/desktop) is blocked, and access is
opened up on an as-needed basis.  Sites that have been allowed access
are referred to as *trusted hosts* and all other sites/hosts will be
considered *untrusted” sites/hosts*

Please see the '''Firewall''' section below for more details if you
need access to/from a machine that is currently considered as an
“untrusted” host/site.

.. _data_transfer_methods:

Data Transfer Methods
=====================

* Globus Connect Service is a utility system, Web or CLI-based, for
  efficient data transfer between DTNs and external storage systems.
  Where Globus endpoints are available, it is the recommended method
  for high-speed transfer. Note that some sites outside the RDHPCS
  program do not support Globus.
* Data Transfer Nodes (DTNs)are dedicated systems (typically servers)
  deployed and configured specifically for data transfer. As such,
  they provide a comparatively fast method for data transfer.  DTNs
  can only be used within RDHPCS, and transfers are limited to
  High-Performance File Systems (HPFS).
* Untrusted Data Transfer Nodes (UDTNs). Nodes available from anywhere
  on the Internet, to support transfers in and out of the RDHPCS
  program to external sites. Globus, or typical data transfer
  commands, can be used for transfer to and from UDTNs.
* Port Tunnelling. SSH tunnels can be created from a point of login to
  any remote host. Once a tunnel has been created you can use the
  tunnels for data transfers, even from “untrusted hosts). This
  method is available when other choices are not available or optimal.

.. _globus:

Globus
------

Globus Connect Service is available on all RDHPCS systems (Hera,
Niagara, Jet, PPAN, Gaea, Orion and Hercules) and we encourage its use
over a other methods whenever possible. Globus Connect Service is used
to transfer data between 2 Globus endpoints. A Globus endpoint is a
file transfer location (computer/server) accessible to Globus. To
transfer data, use your browser to connect to the Globus app,
authenticate to both endpoints, navigate to the desired directory for
each endpoint, select the file(s)/directory(s) to be transferred, and
initiate the transfer.  The movement of data will then be managed and
supervised in the background. You may close the browser or leave the
browser open. The current status of your request is displayed if you
need it. When the transfer is complete, you will be notified by email.
Please see the '''[[Globus Online Data Transfer]]''' page for complete
details.

Some use cases that involve sites outside the RDHPCS program may not
support Globus. In these cases, you can use the other methods
described below.

.. _DTNs:

Data Transfer Nodes (DTNs)
--------------------------

We highly recommend using this method to transfer data when available,
as it provides a fast method for transferring TO and FROM HPC Systems
- Jet, Hera, Niagara, Gaea, and Orion.  Please see the
Transferring Data page for complete details.

Note the follow:
* DTNs cannot be accessed from a home network. For
transfers from systems that cannot access the DTNs, refer to UDTN,
below.
* DTNs can only access the High-Performance Filesystems
(HPFS-scratch file systems), not the /home filesystems.
* DTNs can only be used for inbound connections.
The connection cannot be started
on the DTNs, but data can flow in either direction. Typically, users
should be able to log in to the remote system and initiate a transfer
from the remote machine.
* Unattended data transfers can only be done using the DTNs.

If you are unable to use the DTNs, please review the other available options.

.. _UDTNs:

Untrusted Data Transfer Nodes (UDTNs)
-------------------------------------

Untrusted DTNs (UDTNs) are accessible from anywhere on the internet.
They are designed to allow data to be transferred in and out of the
RDHPCS program from external (non-NOAA HPC) sites -- Cloud
providers, Universities, for example. UDTNs only access the following
directories on the host system:

``/*/data_untrusted/$USER``

For occasional transfers to/from untrusted hosts, you can use two stage
copying to copy data from an remote host to an RDHPCS host.

.. note::

    Before you use the UDTN for data transfers, you MUST have logged
    into the appropriate host for the necessary directories to appear -
    including your /home.

    Please see the Transferring Data page
    for complete details.

.. _Port_Tunnelling:

Port Tunnelling
---------------

In the SSH port tunnel method, an SSH tunnel is created between your
point of login (typically your desktop) to the remote host (typically
Hera, Jet or other remote hosts). The port tunnel method works
from any system on the network (that is, your local machine does not
necessarily have to be in the noaa.gov domain). We recommend using
this method when the options above are not available or
are not optimal for your use case.  Please see the
Transferring Data page for complete details.

.. _requests_for_firewall_exceptions:

Requests for Firewall Exceptions
================================

For security reasons, access to/from all external sites is controlled
by a Firewall and most external sites are blocked and allowed to
connect only through an exception to the Firewall rules. Please see
the Transferring Data page for complete details.

.. _firewall_exception_terms:

Firewall Exception Terms
========================

* Data Transfer Method: scp, sftp, rsync, globus, wget, curl, "globus"
* Local Machine: Where you will be logged in when initiating the transfer
* Remote Machine: The other machine that will be involved in the transfer.

.. note::

    If you need to access an external site on a routine basis
    for your work, you will need to request a Firewall Exception. Submit a
    helpdesk ticket with the subject line: Firewall Exception request and
    provide the information requested below.

* Justification: Some information about why this is needed
* Data Transfer Method: The utility that will be used for doing data transfer
* Local Machine: DNS name, IP address (or endpoint for Globus)
* Remote Machine: DNS name, IP address (or endpoint for Globus)
* Sample command: A typical transfer command

.. note::
    If you have a globus endpoint, please provide it, as that would be the preferred method for data transfers.

.. note::
    Using Globus, you can have a third party transfer where both the ends of a transfer are remote.


