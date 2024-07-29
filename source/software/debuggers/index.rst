Debuggers
=========

Debugging with DDT
------------------

Linaro DDT (formerly ARM DDT) is a powerful, easy to use graphical debugger.

With Linaro DDT, it is possible to debug:

- Single process and multithreaded software
- Parallel (MPI) Software
- OpenMP
- Hybrid cores mixing paradigms such as MPI + OpenMP or MPI + CUDA

Linaro Forge supports:

- C, C++, and all derivatives of Fortran, including Fortran 90
- Python (CPython 2.7), limited support
- Parallel languages/models including MPI, UPCm, Fortran 2008 Co-arrays


Using DDT on Different Systems
------------------------------

Gaea
^^^^

**Launch via Login Node**

On a C# login node:

.. code-block:: shell

    $ module load forge
    $ ddt

**Setup and Configuration**
1. Click the Remote Launch dropdown -> Configure

2. In the Configure Remote Connections, Click Add.

3. Enter the details of your remote host:

    :Connection Name: Enter a name for you remote connection.

    :Host Name: First.Last@gaea-c#.ncrc.gov
        Ex: John.Smith@gaea-c5.ncrc.gov

    :DDT path for Remote Installation: use ``which ddt``

    :Proxy through login node: Check

4. Click OK, then close the Configure Remote Connections window.

5. Click the Remote Launch dropdown and select gaea configuration.

6. Enter your pin+passcode for your gaea login.

**Interactive Session on C#**
Once the client is connected, ssh to gaea and start an interactive session.

.. code-block:: shell

    $ salloc --x11 --clusters=c# --nodes=1 -t1:00:00
    $ module unload darshan-runtime/3.4.0
    $ module load forge
    $ ddt --connect srun -n{number of nodes} ./executable

Note that the ``ddt --connect`` command must precede the srun command.

To open a connection with your (now connected) client on your computer.

Submit the job.

When the job begins to run, The  **Reverse Connect Request** prompt displays.

1. Click Accept.

2. Choose any appropriate options, and click Run.

Hera or Jet
^^^^^^^^^^^

.. note::

    Since DDT is GUI debugger, interactions over a wide area network can be extremely slow.
    You may want to consider using a Remote Desktop which in our environment is X2GO.

For debugging, you will need interactive access to the compute nodes.

.. code-block:: shell

    $ salloc --x11=first -N 2 --ntasks=4 -A <project> -t 300 -q batch

At this point you are on a compute node.

**Load the desired modules**

.. code-block:: shell

    $ module load intel impi forge

**Launch the application with the debugger**

.. code-block:: shell


    $ ddt srun -n 4 ./hello_mpi_c-intel-impi-debug


This will open GUI in which you can do your debugging.

Launch Jobs Directly from DDT
-----------------------------

After loading all of the necessary modules, launch DDT GUI from a login node.

.. code-block:: shell

    $ ddt &

.. note::


    If using on Gaea, use the gaea configuration you had set up so your local
    client connects to Gaea.

Once the main window opens, click on **Run** :


.. figure:: /images/RUNmenu.png

**Application**

This lets you specify the path to your application that you want to run.

Click on the 'Details' button on the left to expand this section.

Once expanded, you will be able to enter:

Application: the path to the application

Arguments: the args to pass to the application

stdin file: any input file needed for the application

Working Directory: the working directory from which the job should be started.


**MPI**
Check the MPI box to indicate if your application is using MPI.

By default, you will only see the Implementation option 'no MPI'.

Click on the 'Change..' button and a new window will open.

.. figure:: /images/ddtMPISettings.png

From the MPI/UPC Implemenation dropdown, select 'Slurm (generic)' -> OK.

You will have the option to set the 'Number of Processes' & 'Number of Nodes'.

The 'srun arguments' section allow you to pass any additional arguments.

**Submit to Queue**


Check the 'Submit to Queue' checkbox.

Click on 'Configure...' which will open up the following window.

.. figure:: /images/jobSubmissionSettings.jpg

In 'Submission template file' -->

create a file with the following contents and name it `slurm.qtf`:


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
    # WALL_CLOCK_LIMIT_TAG: {type=text,label="Wall Clock
    Limit",default="00:30:00",mask="09:09:09"}
    #SBATCH --nodes=NUM_NODES_TAG
    #SBATCH --time=WALL_CLOCK_LIMIT_TAG

    #SBATCH --job-name="ddt"
    #SBATCH --output=allinea.stdout
    #SBATCH --error=allinea.stdout
    #SBATCH -M <cluster-name>

    AUTO_LAUNCH_TAG



This script is provided by Linaro Forge.
It can usually be found in ``linaro-forge/{version}/templates/slurm.qtf``)

Now save your ``slurm.qtf`` file and enter the pathname.

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


