.. _linar-forge:

************************
Debugging with Forge DDT
************************

`Linaro Forge DDT
<https://docs.linaroforge.com/24.0.3/html/forge/ddt/index.html>`_,
which is part of `Linaro Forge <https://www.linaroforge.com/>`_ is a
powerful, easy to use graphical debugger.

With Linaro Forge DDT, it is possible to debug

- Single process and multithreaded software
- Parallel (MPI) Software
- OpenMP
- Hybrid cores mixing paradigms such as MPI + OpenMP or MPI + CUDA

Linaro Forge DDT supports

- C, C++, and all derivatives of Fortran, including Fortran 90
- Python (CPython 2.7), limited support
- Parallel languages/models including MPI, UPCm, Fortran 2008 Co-arrays

The documentation on this page will help you set up DDT to debug on the RDHPCS
system.  Please refer to the `Linaro Forge DDT documentation
<https://docs.linaroforge.com/24.0.3/html/forge/ddt/index.html>`_ for
information on using DDT.


DDT remote connection
=====================

Since DDT is a graphical debugger, interactions over a wide area
network can be extremely slow. To make running DDT on remote systems
easier, DDT has the ability to use a locally running client to connect
to a remote system.

Download and install `Linaro Forge
<https://www.linaroforge.com/download-documentation/>`__.

.. important::

    The version of the local client must match the version of Forge on
    the RDHPCS system.  You may need to download and install an `older
    Linaro Forge version
    <https://www.linaroforge.com/download-forge-old-version>`_.

.. note::

    You will need to have an SSH connection open, with the :ref:`local
    port forward <ssh-port-tunnels>` active to use this method.

.. figure:: /images/forge_remote_connect.png
    :figwidth: 30%
    :align: right
    :alt: Linaro Forge remote connection configuration

    Enter the remote connection configuration for Linaro Forge.  You must have
    a working local forward port established to the remote RDHPCS system.

In the locally running client:

1. Click the :menuselection:`Remote Launch dropdown --> Configure`
2. In the Configure Remote Connections dialog, click :guilabel:`Add`.
3. Enter the details of your remote host:

    Connection Name
        Enter a name for you remote connection.

    Host Name
        Enter ``First.Last@localhost:<port>``, where ``<port>`` is
        your :ref:`local forward port number <ssh-port-tunnels>`.

    DDT path for Remote Installation
        Run ``sh -c 'dirname $(dirname $(command -v ddt))'`` on the RDHPCS
        system, and copy the returned path.

    Proxy through login node
        Ensure the checkbox is selected.

4. Click :guilabel:`OK`, then close the Configure Remote Connections window.
5. Click the :menuselection:`Remote Launch dropdown` and select your
   configuration.
6. Enter your PIN+passcode.  On RDHPCS systems other than gaea, you
   can use `SSH key authentication
   <https://www.redhat.com/sysadmin/passwordless-ssh>`__.

There are other ways to start Forge DDT.  We find the remote connection gives
the best user experience on the RDHPCS systems.  If you decide to run Forge DDT
directly on the RDHPCS system, you will likely want to use a remote desktop
environment, like the :ref:`x2go-remote-desktop`.  Please refer to the `Linaro
Forge connecting to a remote system
<https://docs.linaroforge.com/24.0.3/html/forge/forge/connecting_to_a_remote_system/index.html>`_
documentation for more information.


Debgging an MPI process
=======================

.. _forge-first-time-config:

First time configuration
------------------------

.. figure:: /images/linaro_forge_systemsettings.png
    :figwidth: 30%
    :align: right
    :alt: Linaro Forge's system settings window.

    Linaro Forge's system settings dialog.  This is where the user will set the
    MPI implementation.

If this is the first time you will debug an application on this remote system,
you will need to set some configuration options.  To do this, click the
:guilabel:`Run and debug a program` option to open the run dialog window. Click
the :guilabel:`options` button in the lower left.

Select :menuselection:`system`.  In the *systems settings* area, use the
*MPI/UPC implementation* drop down menu and select :menuselection:`SLURM
(generic)`.

Linaro Forge has the ability to submit a Slurm job.  To allow this, first
download correct queue template file for the given system, and place it on the
remote RDHPCS system:

* :download:`Gaea </_downloads/gaea_slurm.qtf>`
* :download:`Hera </_downloads/hera_slurm.qtf>`
* :download:`Jet </_downloads/jet_slurm.qtf>`

Please review the downloaded queue template file.  You may need to modify it to
ensure the correct modules are loaded for your application to run.

.. note::
    You can use :command:`curl` on the remote system to download the queue
    template file.  Copy the link address for the file, and run:

    .. code-block:: shell

        $ curl -o slurm.qtf <past_url_link>

.. figure:: /images/linaro_forge_jobsubmitsettings.png
    :figwidth: 30%
    :align: right
    :alt: Linaro Forge's job submission settings window.

    Linaro Forge's job submission settings dialog.  This is where the user can
    set the queue template file and other job submission information.

With the Slurm template file on the remote system, in the Linaro Forge run
dialog window select guilabel:`job submission`. In the *job submission
settings* area, in the *submission template file* box, enter the full path to
the :file:`slurm.qtf` file you downloaded.  Alternatively, you can click on the
file icon (:octicon:`file-directory-fill;1em;sd-text-warning`) and navigate to
the Slurm template file.  The other Slurm items will be updated whith the Slurm
template file.  Ensure the :guilabel:`quick restart` option is selected.

Finally, select :guilabel:`Ok` to close the settings.

.. note::

    You can learn about the Linaro Forge DDT options in the `Forge
    configuration documentation
    <https://docs.linaroforge.com/24.0.3/html/forge/configuration_appendix/optional_configuration.html>`_.

Submit a debug job
------------------

.. figure:: /images/linaro_ddt_run.png
    :figwidth: 30%
    :align: right
    :alt: Linaro Forge run dialog

    The Linary Forge run dialog box.  This is where users will select the MPI
    type (Slurm), number of processors, and the queue submission information.

In the DDT client window, select :guilabel:`Run and debug a program`.  This
will bring up the run dialog window.

In the run dialog window, expand the :guilabel:`application` section and in the
*applicatoin* text box enter the path to the executable or use the file icon
(:octicon:`file-directory-fill;1em;sd-text-warning`) and navigate to the
executable.  In the *working directory* text box, you should also enter the
full path to the directory from where the debug job should be run.

Select the :guilabel:`MPI` section.  Enter the total number of MPI processes,
and the number of nodes required.  If needed, change the MPI implementation and
add any additional :command:`srun` arguments to run your application.

.. important::

    Ensure the number of processes and the number of nodes required for that
    many processes is correct for the RDHPCS system and partition.  You can set
    the *processe per node* option with the correct number of processes per
    node, and the link button (:octicon:`link;1em;sd-text-secondary`) to
    automatically set the correct number of required nodes.

If debugging a hybrid MPI+OpenMP applicaiton, select the :guilabel:`OpenMP` and
enter the number of OpenMP threads.  Please note you may need to use the MPI
implementation *Slurm (MPMD)* if debugging an MPI+OpenMP application.

Select the :guilabel:`submit to queue` section.  If you haven't already
configured DDT to lauch Slurm jobs, please refer to
:ref:`forge-first-time-config`.  Click the :guilabel:`parameters` button to
verify the Slurm submit settings.

Verify all the settings are correct, and click the :guilabel:`submit` button.
Forge will submit your job to the Slurm scheduler and wait for the job to
start.  Once the job starts, Forge will attach to the running application.  At
this point, you can use Forge to debug your application.

.. seealso::

    * `DDT Training Video <https://www.youtube.com/watch?v=Q8HwLg22BpY>`_ from
      `Sharcnet HPC <https://www.youtube.com/@SHARCNET_HPC>`_
    * `Linaro Forge DDT documentation`_
