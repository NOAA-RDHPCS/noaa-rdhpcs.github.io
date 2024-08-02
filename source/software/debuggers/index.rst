Debuggers
=========

Debugging with DDT
------------------

`Linaro DDT
<https://docs.linaroforge.com/24.0.3/html/forge/ddt/index.html>`_,
which is part of `Linaro Forge <https://www.linaroforge.com/>`_ is a
powerful, easy to use graphical debugger.

With Linaro DDT, it is possible to debug

- Single process and multithreaded software
- Parallel (MPI) Software
- OpenMP
- Hybrid cores mixing paradigms such as MPI + OpenMP or MPI + CUDA

Linaro DDT supports

- C, C++, and all derivatives of Fortran, including Fortran 90
- Python (CPython 2.7), limited support
- Parallel languages/models including MPI, UPCm, Fortran 2008 Co-arrays


Using DDT on Different Systems
------------------------------

Gaea
^^^^

**Launch via Login Node**

Load the ``forge`` module on one of the login nodes, and run the
``ddt`` application:

.. code-block:: shell

    $ module load forge
    $ ddt

**Setup and Configuration**

1. Click the :menuselection:`Remote Launch dropdown --> Configure`
2. In the Configure Remote Connections dialog, click :guilabel:`Add`.
3. Enter the details of your remote host:

    :Connection Name: Enter a name for you remote connection.
    :Host Name: ``First.Last@rdhpcs-host``
    :DDT path for Remote Installation: use ``which ddt``
    :Proxy through login node: Check

4. Click :guilabel:`OK`, then close the Configure Remote Connections window.
5. Click the :menuselection:`Remote Launch dropdown` and select your
   configuration.
6. Enter your PIN+passcode for your gaea login.

**Using an Interactive Session**

Once the client is connected, ssh to gaea and start an interactive session.

.. code-block:: shell

    $ salloc --x11 --clusters=c# --nodes=1 -t1:00:00
    $ module unload darshan-runtime/3.4.0
    $ module load forge
    $ ddt --connect srun -n{number of nodes} ./executable

Note that the ``ddt --connect`` command must precede the ``srun`` command.

To open a connection with your (now connected) client on your computer.

Submit the job.

When the job begins to run, The **Reverse Connect Request** prompt displays.

1. Click :guilabel:`Accept`.

2. Choose any appropriate options, and click :guilabel:`Run`.

Hera or Jet
^^^^^^^^^^^

.. note::

    Since DDT is a GUI debugger, interactions over a wide area network
    can be extremely slow. You may want to consider using a remote
    desktop solution, for example :ref:`X2Go <x2go-remote-desktop>`.

For debugging, you will need interactive access to the compute nodes.
Use the `salloc <https://slurm.schedmd.com/salloc.html>`_ command:

.. code-block:: shell

    $ salloc --x11=first -N 2 --ntasks=4 -A <project> -t 300 -q batch

At this point you are on a compute node.

**Load the desired modules**

.. code-block:: shell

    $ module load intel impi forge

**Launch the application with the debugger**

.. code-block:: shell


    $ ddt srun -n 4 ./exe_to_debug

This will open GUI in which you can do your debugging.


Launch Jobs Directly from DDT
-----------------------------

On a login node, load the forge module and other necessary modules,
then launch the ``ddt`` application.

.. code-block:: shell

    $ module load forge [<other_modules> ...]
    $ ddt

.. note::

    If using on Gaea, use the gaea configuration you had set up so your local
    client connects to Gaea.

Once the main window opens, click on :guilabel:`&Run`.


.. figure:: /images/RUNmenu.png

**Application**

This lets you specify the path to your application that you want to
run.  Click on the :guilabel:`Details`` button on the left to expand
this section.  Once expanded, you will be able to enter:

    :Application: the path to the application

    :Arguments: the args to pass to the application

    :stdin file: any input file needed for the application

    :Working Directory: the working directory from which the job
        should be started.


**MPI**

Check the MPI box to indicate if your application is using MPI.  By
default, you will only see the implementation option *no MPI*.  Click
on the :guilabel`Change` button and a new window will open.

.. figure:: /images/ddtMPISettings.png

From the MPI/UPC Implemenation dropdown, select *Slurm (generic)*, and
then click :guilabel:`OK`.  You will have the option to set the number
of processes and the number of nodes.  In the srun arguments section
you may add additional ``srun`` arguments.

**Submit to Queue**

First, create a file (``slurm.qtf``) with content similar to the
following:

.. code-block:: shell

    #!/bin/sh
    #
    # NOTE: if using with srun then you should select "SLURM (MPMD)" as the MPI
    # implementation on the System Settings page of the Options window.
    #
    # WARNING: If you install a new version of Linaro Forge to the same
    # directory as this installation, then this file will be overwritten.
    # If you customize this script at all, please rename it.
    #
    # Name: SLURM
    #
    # submit: sbatch
    # display: squeue
    # job regexp: (\d+)
    # cancel: scancel JOB_ID_TAG
    #
    # WALL_CLOCK_LIMIT_TAG: {type=text,label="Wall Clock Limit",default="00:30:00",mask="09:09:09"}
    #SBATCH --nodes=NUM_NODES_TAG
    #SBATCH --time=WALL_CLOCK_LIMIT_TAG

    #SBATCH --job-name="ddt"
    #SBATCH --output=allinea.stdout
    #SBATCH --error=allinea.stdout
    ## The following line is only needed on Gaea
    #SBATCH -M <cluster-name>

    AUTO_LAUNCH_TAG





Now save your ``slurm.qtf`` file and enter the pathname.

Check the :guilabel:`Submit to Queue` checkbox.  Click on
:guilabel:`Configure` which will open up the following window.

.. figure:: /images/jobSubmissionSettings.png

In *Submission template file* box, enter the full path to the
``slurm.qtf`` file you created above, then click :guilabel:`&Edit
Queue Parameters` and enter values for the available paremeters.



Click OK once done to close this window.

Now click on the 'Parameters' button to enter the wall clock time for your job.

Now you can click on the Submit button.

After the job submission starts, the Forge debug window will become active.

Run DDT via Remote Client
-------------------------

The remote client can overcome latencies that arise when using X Forwarding.

**Record Local Port Number**

To configure a remote launch, you need your local port number.
You can obtain the local port number from your Tectia/CAC or your RSA login tunneling configuration, or when you log into a System's Front End (FE) node.

Installation

1. From your workstation, download the Arm forge client.
2. Extract the tarball

   - tar -xf arm-forge-{version}-linux-x86_64.tar

3. Run a GUI installer, or textinstall.sh for a text-based install

Configuration

1. With typical tunnels set up, SSH into HPC system.

2. Launch DDT from local machine. Click Remote Launch dropdown -> Configure.

3. Enter the details of your remote host:

    :Connection Name: Enter a name for your remote connection

    :Host Name: your_workstation_username@localhost:<local port number>

    :DDT path for Remote installation: use ``which ddt``

    :KeepAlive Packets: Enable

    :Proxy through login node: uncheck

4. Click OK to save your changes.

5. Select your new host from the “Remote Launch” combo box.

6. At the prompt, enter your PASSCODE.

Forge will then launch jobs, browse for files, and use/set the configuration.

Reverse Connect
^^^^^^^^^^^^^^^

The remote client program runs entirely on your workstation.

Once connected to a remote host, Reverse Connect launches DDT jobs.

1. Launch the Forge remote client and connect to a remote host

2. Load the forge module, run a DDT ``--connect`` command:

.. code-block:: shell

    $ module load forge
    $ ddt --connect srun -n ./mpitest

The remote client notifies you of the new connection.
Optionally, configure debugging options before you launch the program.

3. Click Run to begin the DDT session.


