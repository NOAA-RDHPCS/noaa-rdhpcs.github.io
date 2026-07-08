.. _common_access_card:

Common Access Card (CAC)
========================

The Common Access Card (CAC) or Personal Identity Verification (PIV)
card is a means of access to RDHPCS resources for both Web and SSH
access. To obtain a CAC, work with your local admin services team as
they need to start the application process.  Some labs can issue CACs
on-site, otherwise you will have to visit a RAPIDS site. The site
locator website is `ID Card Office Online
<https://idco.dmdc.osd.mil/idco/>`_.

.. _cac_piv_ssh_enrollment:

CAC/PIV SSH Key Enrollment
===========================

To register your CAC or PIV for access to the NOAA RDHPCS systems:

1. Insert your CAC/PIV into your reader.

2. Open a web browser and navigate to the RDHPCS AIM portal:

   https://aim.rdhpcs.noaa.gov

Be sure and authenticate with your CAC/PIV.  Once you have
authenticated, the certificate on your CAC/PIV will be used to
automatically register an "SSHKEY Token" for use in the NOAA RDHPCS
environment.

.. image:: /images/sshkey-success.png
   :align: center

.. important::

   If you have a new CAC/PIV you must remove the old CAC/PIV from AIM
   by visiting the `AIM MFA page
   <https://aim.rdhpcs.noaa.gov/cgi-bin/mfa.pl>`_. Once that is done,
   navigate to the main AIM page above to register your new CAC/PIV

.. important::

   CAC/PIV authentication is preferred for interactive RDHPCS logins.
   However, the following services **require** Yubikey and do **not**
   support CAC/PIV authentication:

   - Authenticating to role accounts
   - Authenticating to trusted and untrusted DTNs for data transfers
   - Authenticating to Globus for data transfers
   - Data transfers using the port tunnelling method


Once your key has been registered by performing the above steps, you
may proceed to use your CAC / PIV / SSHKEY to connect to RDHPCS
bastions.  See :ref:`CAC SSH Login<Common-access>` for details.


.. _putty_cac_config:


