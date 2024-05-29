.. _Tectia:

******
Tectia
******

RDHPCS users with a CAC who are logging in from a Windows, Mac, or
Linux workstation/laptop are required to use CAC login. Access to
RDHPCS resources via CAC requires a CAC reader and necessary software.
The Tectia SSH Client software has been selected to meet the remote
CAC login requirements for the RDHPCS program. Two licenses have been
purchased for each RDHPCS user.

The following features are supported:

* Port forwarding
* X11 tunneling

Access to RDHPCS Systems from a system which cannot directly access a
user's CAC is not supported.

Tectia Initial Setup procedure
==============================

Host names for the CAC Bastion Server in Boulder, CO:

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


The following OS-specific sections (Windows, Linux, MAC) describe how
to do the following:

* Download the Tectia software
* Install the Tectia software on your local laptop or workstation
* Install the license file on your local laptop or workstation
* Configure the Tectia software
* Use the client software to connect to R&D HPC Systems
* Set up port tunneling

Install and Configuring Tectia
==============================

SSH Tectia Client provides secure terminal client functionality for
remote users and system administrators for accessing remote hosts
running SSH Tectia Server or other Secure Shell server.

These are the steps to install and configure Tectia for a Windows system:

* Download and install the Tectia software on your local laptop or
  workstation
* Install the license file on your local laptop or workstation.
* Configure the Tectia software
* Use the client software to connect to RDHPCS Systems
* Set tunneling options

.. note::

   Users will likely need to contact their local IT Help Desk to
   download and install Tectia.

**Requirements**

* Your CAC information must be in `AIM <https://aim.rdhpcs.noaa.gov>`_
  for the Tectia CAC logon to work. To confirm that your CAC
  information is correct authenticate using your CAC in `AIM`. If your
  CAC information has been refreshed, wait 15 minutes before
  attempting to log in using Tectia.
* In order to install the Tectia SSH Client, you must have the
  necessary administrator privileges on your system. If you do not
  have this access, contact your IT system administrator for
  assistance.
* The Tectia Client installation requires about 140 megabytes of disk
  space and your system must have a CAC reader.


Install the Tectia Client
-------------------------

.. tab-set::

   .. tab-item:: Windows
      :sync: windows

      The Windows installation package is provided in the MSI
      (Microsoft Installer) format. The same package is compatible
      with the supported 32-bit (x86) and the 64-bit (x64) versions of
      Microsoft Windows. Time to complete is approximately 10 minutes.

      1. Download the Tectia client.

         Follow the `Tectia client link
         <https://drive.google.com/file/d/18Wc0W3d_ESuPBubwW8I8oESNhI6QJvfJ>`_
         to open new tab on your browser. You may have to authenticate
         using your NOAA email and password.

         * Once you have authenticated and the folder is shown in your
           browser, select
           ``tectia-client-6.4.13.36-windows-upgrd-eval.zip``
         * Select one of the .msi packages for 32-bit (x86) or 64-bit (x86-64)
           machines.

      2. Extract the installation zip file contents to a temporary
         location. The download package includes Tectia documentation
         .pdf files that can be used after the basic install described
         here to learn more, customize, etc. Please review this
         documentation before requesting help beyond the scope of this
         basic setup procedure.

      3. Locate the Windows Installer file:

         * ``ssh-tectia-client-<version>-windows.msi`` for 32-bit
           Windows systems.
         * ``ssh-tectia-client-<version>-windows_64.msi`` for 64-bit
           Windows systems.

         Where ``<version>`` corresponds to the version and build
         number, for example ``6.4.10.123``. On some Windows versions,
         the ``.msi`` file extension is not shown for the installer
         file.

      4. Double-click the installation file, and the installation
         wizard will start.

      5. Select **Typical** and click **Next**.

         .. figure:: /images/cactest1.png

      6. Click **Install**.

         .. figure:: /images/cactest2.png

      7. When the client is fully installed, click **Finish**.

         .. figure:: /images/cactest3.png

         You will now see two icons on your desktop. One is named
         “Tectia – SSH Terminal” and the second one is named “Tectia –
         Secure File Transfer.

      8. Reboot your computer.

      9. Request a Tectia license. The Tectia software you just
         installed only has a 45-day evaluation license and works for
         all RDHPCS logons. To request an extended license, please
         email **ONE** help request to the help desk of the system you
         use the most. Please use the subject "Tectia license
         request".

      10. Install the Tectia license. Complete this step before your
          45-day **stc64.data** Tectia license file from the help
          system, move the file to the following location:

          * 64-bit Windows versions:

            .. code:: shell

               C:\Program Files (x86)\SSH Communications Security\SSH Tectia\SSH Tectia AUX\licenses&quot;

          * 32-bit Windows versions

            .. code:: shell

               C:\Program Files\SSH Communications Security\SSH Tectia\SSH Tectia AUX\licenses&quot;

   .. tab-item:: RHEL
      :sync: rhel

      .. note:: Tectia SSH will install on RHEL-based Linux systems, e.g., RHEL, Centos, Fedora, Rocky Linux

      .. note::

         The Tectia client uses Coolkey to access the certificates on
         your CAC. Coolkey should be available in your distribution.

         .. code:: shell

            $ sudo yum install coolkey

         Once Coolkey is installed you will need to know the full path
         to the library, for example ``/usr/lib/pkcs11/libcoolkeypk11.so``

      1. Download the Tectia client.

         Follow the `Tectia client link
         <https://drive.google.com/file/d/18Wc0W3d_ESuPBubwW8I8oESNhI6QJvfJ>`_
         to open new tab on your browser. You may have to authenticate
         using your NOAA email and password.

         Once you have authenticated and the file is shown in your
         browser, click on the appropriate file.

      2. Expand the archive.

         .. code:: shell

            $ tar xf tectia-client-6.4.13.36-linux-x86_64-upgrd-eval.tar

         .. note::

            The download package includes Tectia documentation .pdf
            files that you can use after the basic install described
            here to learn more, customize, etc. Please review this
            documentation before requesting help beyond the scope of
            this basic setup procedure.

      3. Change into the client directory.

         .. code:: shell

            $ cd tectia-client-6.4.13.36-linux-x86_64-upgrd-eval/

      4. Run the installer

         .. code:: shell

            $ rpm -i *.rpm

      5. Modify Path

         The Tectia client is installed in ``/opt/tectia/``. It is
         advisable to add the binary directory to your path.

         If your default shell is bash, you can add the following to
         your ``~/.profile`` file.

         .. code:: shell

            if [ -d "/opt/tectia/bin" ] ; then
               export PATH="$PATH:/opt/tectia/bin"
            fi

            if [ -d "/opt/tectia/man" ] ; then
               export MANPATH="$MANPATH:/opt/tectia/man"
            fi

         If your default shell is csh, you need to edit your ``~/.cshrc`` file.

         .. code:: shell

            if ( -d "/opt/tectia/bin" ) ; then
               setenv PATH "$PATH:/opt/tectia/bin"
            endif

            if ( -d "/opt/tectia/man" ) ; then
               setenv MANPATH "$MANPATH:/opt/tectia/man"
            endif

      6. Request a Tectia license.

         The Tectia software you just installed has a 45 day
         evaluation license, and works for all RDHPCS logons. To
         request an extended license, email ONE help request to the
         help desk of the system you use the most. Please use the
         subject **Tectia license request**.

      7. Install the Tectia license.

         Complete this step before your 45 day evaluation license
         expires. Once you have received your Tectia "stc64.dat"
         license file via the help system, create the proper directory
         for it and move the file to the directory.

         .. code:: shell

            $ cd <download directory>
            $ mkdir /etc/ssh2/licenses/
            $ mv stc64.dat /etc/ssh2/licenses/

   .. tab-item:: MacOS
      :sync: macos

      The Mac installation package includes installers for both the
      Tectia software and the license.

      1. Follow the `Tectia client link
         <https://drive.google.com/file/d/18Wc0W3d_ESuPBubwW8I8oESNhI6QJvfJ>`_
         to open new tab on your browser. You may have to authenticate
         using your NOAA email and password. Once you have
         authenticated and the file is shown in your browser, click
         "Download."

      2. Locate the packages under your Downloads folder
         ``SshTectiaClient-<version>.pkg``, where ``<version>``
         corresponds to the version and build number, for example
         6.5.0.1087).

      3. Double-click the box icon to the right of the package name to
         start the installation wizard.

         .. figure:: /images/mactectia1.png

      4. Click continue. The Wizard lets you specify the destination
         and installation type. Click "Continue" to accept the
         destination and standard installation, then click "Install".

         .. figure:: /images/mactectia3.png

      5. Enter the password for your desktop/laptop login and click
         "Install Software". You'll see a confirmation message when
         the installation is complete.
      6. Reboot your computer.
      7. The Tectia software you just installed requires a new license
         and once installed, works for all RDHPCS logons. To request a
         license, please email ONE help request to the help desk of
         the system you use the most. Please use the subject "Tectia
         Mac license request".
      8. Download the license file.
      9. Locate the packages under your Downloads folder
         ``ssh-tectia-client-license-<version>.pkg``, where
         ``<version>`` corresponds to the version and build number,
         for example 6.5.0.1087).
      10.  Double-click the box icon to the right of the package name
           and the installation wizard will start.
      11. Repeat the installation steps above until you get "The
          installation was successful" message.

Configure the Tectia Client
---------------------------

.. tab-set::

   .. tab-item:: Windows
      :sync: windows

      1. Double-click the “Tectia – SSH Terminal” icon on your
         desktop. The following screen appears:

         .. figure:: /images/tectiawin1.png

      2. In the menu bar, select "Edit" > “Tectia Connections”.

      3. Set your default username

         * In the sidebar menu select "General" > "Default Connection"
         * In the default "Connection" tab select "Specify user name",
           and enter your user name, which must match your NOAA Email
           user name in AIM. The user name is case sensitive, and
           should be in the form of "Firstname.Lastname" or
           "Firstname.M.Lastname" (ex: John.Smith, John.P.Smith). Do
           not include the @noaa.gov.
         * Select "Apply"

         .. figure:: /images/tectiawin2.png

      4. Optional: Set X windows forwarding

         Select the "Tunneling" tab.

         .. figure:: /images/tectiawin3.png

         Check the two boxes as illustrated, and click "Apply".

      5. In the sidebar menu:

         * Select "User Authentication" > "Key Providers" .
         * Select the "Enable Microsoft Crypto API" check box. This is
           needed to view your CAC card certificates.
         * Select "Apply"

         .. figure:: /images/tectiawin4.png

      6. Set up a connection profile for each hostname that you want
         to use. There are two bastions, one in Boulder, CO and one in
         Princeton, NJ. It is highly recommended that you set up a
         profile from each bastion for each RDHPCS system you need to
         use, as bastions are typically down during maintenance
         periods.

         * In the sidebar menu select "Connection Profiles".
         * Select "Add Profile".
         * In the "Connection" tab: Fill out the information for the
           hostname you are configuring. * Enter the "Profile Name"
           you want to assign to the hostname (ex: Jet-BLDR bastion).
           Leave "Port number" =22.
         * Enter the Host Name from the bastion list.
         * Select "Apply".
         * To add another profile select "Add Profile" in the lower
           left, and repeat the above steps.
         * Select "OK" when all profiles are set.

      The example below shows a profile for the CAC Gaea bastion in
      Princeton. The port used (22) is correct, as is the User Name
      selection. This can be set here, or just select the radio button
      next to “Use the Default Connection’s username”.

      .. figure:: /images/tectiawin5.png

   .. tab-item:: RHEL
      :sync: rhel

      Tectia stores its configuration in
      ``${HOME}/.ssh2/ssh-broker-config.xml``. It is recommended to
      use the graphical configuration tool, ``ssh-tectia-configuration``.

      1. Launch the configuration client (ssh-tectia-configuration).

         .. figure:: /images/rheltectia1.png

      2. In the Default Connection item, set a default user name.

         .. figure:: /images/rheltectia2.png

      3. Enable X11 Forwarding

         .. figure:: /images/rheltectia3.png

      4. Add a PKCS 11 library under the “Key Providers” item and
         click on the “Add” button.

         .. figure:: /images/rheltectia4.png

         * Add the full path to the Coolkey library. It should be
           ``/usr/lib64/pkcs11/libcoolkeypk11.so``.

         .. figure:: /images/rheltectia5.png

         * Check to make sure this is the correct location.
         * Confirm that the PKCS 11 key providers contains the Coolkey
           library.

      5. Under "Connection Profiles, add a new connection profile.

         .. figure:: /images/rheltectia6.png

         * Set a profile name, for example “jet”.
         * Set the full hostname, for exmaple
           *bastion-jet.boulder.rdhpcs.noaa.gov*.
         * Apply the changes and then click OK.

      **Using the Tectia SSH Client**

         Once Tectia has been configured and the binary directory has
         been added to your path. You can ssh into to Jet using your
         CAC. The Tetica ssh command is ``sshg3``.

         1. In a terminal window type ``sshg3 jet`` where *jet* is the name of
            the connection profile created under step 5 of the
            configuration.
         2. You will be prompted to save and accept a key for this bastion.
            Then type “save”.
         3. Once the key is accepted you will be prompted for your CAC
            Pin (“Passphrase for the private key:”); Please note that
            the prompt is very misleading! It is *not* asking for your
            "pass phrase for the certificate" (which the 3 word that
            you use to renew your certificate)!
         4. If successful you will see the message “Authentication
            successful.” and you will be forwarded to a front-end host.

   .. tab-item:: MacOS
      :sync: macos

      Tectia stores its configuration in
      ``${HOME}/.ssh2/ssh-broker-config.xml``. It is recommended to
      use the graphical configuration tool,
      ``ssh-tectia-configuration``.

      1. Launch the configuration client (``ssh-tectia-configuration``) or
         from the Applications directory
         (``/Applications/SshTectiaClient``)

         .. figure:: /images/rheltectia1.png

      2. Set a default username under the “Default Connection” item.
         This should be your case sensitive NOAA RDHPCS login
         username.

         .. figure:: /images/rheltectia2.png

      3. Enable X11 Forwarding

         .. figure:: /images/rheltectia3.png

      4. If no Key Provider is specified (if the Dynamic Library list
         is blank), add a PKCS 11 library under the “Key Providers”
         item.

         * Click the “Add” button.

           .. figure:: /images/rheltectia4.png

         * Select "Browse." This should pull up the full path to the
           opensc-pkcs11 library.
         * The full path is
           ``/Applications/SshTectiaClient.app/Contents/PlugIns/OpenSC/opensc-pkcs11.so``.

           .. figure:: /images/mactectia4.png

           Please check to make sure this is the correct location.

      5. Under "Connection Profiles, add a new connection profile.

         .. figure:: /images/rheltectia6.png

         * Set a profile name, for example “jet”.
         * Set the full hostname, for exmaple
           “bastion-jet.boulder.rdhpcs.noaa.gov”.
         * Apply the changes and then click OK.

      Once the Tectia Client has been configured, you can connect to any of the following CAC bastions.

      **Using the Tectia SSH Client**

         Once Tectia has been configured and the binary directory has
         been added to your path, you can ssh into to any RDHPCS
         system using your CAC with the ``sshg3`` command.

         1. With the CAC card inserted in the reader, in a terminal
            window type “sshg3 jet” where “jet” is the name of the
            connection profile created under step 5 of the
            configuration.
         2. You will be prompted to save and accept the key for this
            bastion. You need to type “save”.
         3. Once the key is accepted you will be prompted for your
            CAC Pin.

.. note::

   The prompt for the CAC reads: “Passphrase for the private key:”;
   and the prompt is very misleading! It is not asking for your
   "passphrase for the certificate" (the 3 words that you use to
   renew your certificate)!'''

If successful you will see the message “Authentication successful.”
You will be forwarded to a front-end host.

Port Tunnelling
===============

If you plan to do file transfers from non-NOAA domains, or if you plan
to use remote Desktop features (such as X2Go), you will have to set
port forwarding for each profile.  Please keep in mind that different
bastions use different port numbers. Log in to each specific host to
make sure you have your correct port number.

* Select the "Tunneling" Tab
* Select "Use Defaults" so that it will use the X11 forwarding setting
  that is set in Default Setting
* Select the "Add" button

In the steps below, replace "12345" with the unique **local port**
number assigned to you when you login to Jet. Port numbers are
dependent on the host you are trying to connect.

* "Type"= TCP
* "Listen Port"= 12345
* Select "Allow local connections only"
* "Destination host"=localhost
* "Destination port"= 12345

Click "OK". This will populate the "Local Tunnels" tab in the
configuration window:

.. figure:: /images/mactectia5.png

* Click "Apply" to save the profile

Repeat these steps for each profile you create.

Set Up Port Tunnelling
----------------------

Complete the following sequence to set up port tunnelling.

1. Edit your connection profile. Navigate to the "Tunneling" tab.

   .. figure:: /images/tectiawin6.png

2. Check "Use Defaults". Tunnel X11 connections" and "Allow Agent
   Forwarding" should be checked. If not, check them.

   .. figure:: /images/tectiawin7.png

3. Select "Add".

   * Select "TCP" for Type
   * Listen Port should match your Local port number listed on your
     session login.
   * Check "Allow local connections only"
   * Destination host: 127.0.0.1
   * Destination Port should match your Local port number listed on
     your session login.

     .. figure:: /images/tectiawin8.png

   * Select "OK"

4. Selecting "Test connection" to test.

   .. figure:: /images/tectiawin9.png

   * Completed configuration should look like the following:

   .. figure:: /images/tectiawin10.png

Once the session is open, you will be able to use this forwarded port
for data transfers as long as this ssh window is kept open. After the
first session has been opened with the port forwarding, any further
connections (login via ssh, copy via scp) will work as expected.

Testing Port Tunnels
--------------------

Once you have set up port tunneling, it's useful test that the tunnel
has been established correctly.

To do this, after the port tunnel has been established, try to login
using the local host and port combination. Please keep in mind you
will have to use your RSA authentication for this test. You should try
to connect using the following settings with your ssh client (with
Windows you could use a client like putty, and with linux/Mac you
should use ssh):

* Host: localhost (This is literal string, that is, enter the word
  "localhost")
* Port: Your-assigned-local-port-on-thiea-jet (This is the number
  listed as Local Port when you login)
* User: Your user name

When prompted, enter your PIN + RSA Token as the password. If you're
able to login successfully and see your home directory, that confirms
that your port tunneling is correct.
