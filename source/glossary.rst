.. _glossary:

Glossary
========

.. glossary::

    bastion host
        A secure gateway server between your workstation and an RDHPCS
        compute system.  You authenticate to the bastion first; the
        bastion then forwards your session to the compute system.
        See :ref:`connecting-to-rdhpcs`.

    CAC
        Common Access Card.  A United States Department of Defense smart
        card used for authentication.  CAC login on RDHPCS systems
        requires a card reader and the :ref:`Tectia <Tectia>` SSH client.

    Common Access Card
        See :term:`CAC`.

    compute node
        A node type where parallel and threaded applications should be run.
        These nodes typically have large core counts, and a high amount of
        memory per core.  The :command:`srun` is typically used to launch
        parallel jobs on these nodes.

    data transfer node
        A node type that is configured for the transfer of data files across
        local and remote file systems.

    :abbr:`DTN (data transfer node)`
        See :term:`data transfer node`.

    front-end node
        See :term:`login node`.

    login node
        A node type that is mainly used for interactive, and single threaded
        application usage.  This is the node type where users are placed when
        accessing a system.

    master certificate
        An :term:`X.509` certificate created on your first RDHPCS login.
        Valid for one year.  Each login derives a short-lived
        :term:`proxy certificate` from the master certificate to
        authenticate you to compute systems.

    port forwarding
        An SSH feature that routes network traffic through an encrypted
        tunnel between two hosts.  RDHPCS bastions use port forwarding
        to enable tools such as VS Code Remote-SSH, Jupyter notebooks,
        and file-transfer utilities.  Also called a port tunnel.
        See :ref:`ssh-port-tunnels`.

    port tunnel
        See :term:`port forwarding`.

    proxy certificate
        A short-lived :term:`X.509` credential derived from your
        :term:`master certificate`.  Each login renews a 30-day proxy
        certificate that authenticates you to RDHPCS compute systems
        and data transfer services.

    Slurm
        An open source cluster management and job scheduling system.

    X.509
        A standard for public-key infrastructure (PKI) digital
        certificates.  RDHPCS uses X.509 :term:`master certificate`\s
        and :term:`proxy certificate`\s to authenticate users to
        compute systems within the enclave.

    X11 forwarding
        An SSH feature that lets you run graphical applications on a
        remote system and display their output on your local
        workstation.  Requires an X11 server on Windows (VcXsrv or
        MobaXterm) or XQuartz on macOS.  See :ref:`x11-graphics`.

    YubiKey
        A hardware security key issued by NOAA.  Used with a standard
        SSH client for two-factor authentication to RDHPCS systems.
        Requires registration through
        `Account Information Management <https://aim.rdhpcs.noaa.gov>`__.
