.. _ssh-clients:

***********
SSH Clients
***********

Your platform and authentication method determine which SSH client to
use to connect to RDHPCS systems.

.. list-table::
   :header-rows: 1
   :widths: 25 25 10 40

   * - Platform
     - Client
     - CAC
     - Notes
   * - Windows
     - :ref:`openssh-client` (built-in)
     - No
     - Included in Windows 10 and later.  Open with PowerShell or
       Windows Terminal.  Use the
       :ref:`OpenSSH configuration form <openssh-config>` to generate
       ``~/.ssh/config``.
   * - Windows
     - :ref:`putty-client`
     - No
     - Free, open-source graphical SSH client.
   * - Windows
     - `MobaXterm`_
     - No
     - Includes a built-in X11 server.  Useful for X11 forwarding.
   * - Windows
     - `SecureCRT`_
     - No
     - Commercial SSH client from VanDyke Software.
   * - Windows, macOS, Linux
     - :ref:`Tectia`
     - Yes
     - Required for CAC authentication.  RDHPCS provides two licenses
       per user.
   * - macOS, Linux
     - :ref:`openssh-client` (built-in)
     - No
     - Pre-installed on macOS and Linux.  No installation needed.

After installing your client, configure it for RDHPCS:

* **OpenSSH users** — use the
  :ref:`OpenSSH configuration form <openssh-config>` to generate a
  ready-to-use ``~/.ssh/config`` file with port assignments already
  calculated for each system.
* **Tectia users** — follow the :ref:`Tectia setup guide <Tectia>`
  for installation, configuration, and port forwarding.

.. toctree::
   :maxdepth: 1

   OpenSSH <openssh/index>
   Tectia <tectia/index>
   PuTTY <putty/index>


.. _MobaXterm: https://mobaxterm.mobatek.net/
.. _SecureCRT: https://www.vandyke.com/products/securecrt/
