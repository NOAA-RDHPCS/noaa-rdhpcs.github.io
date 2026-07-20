.. meta::
   :description: Frequently asked questions about RDHPCS accounts, jobs,
    data, software, and connections.
   :keywords: FAQ, frequently asked questions, accounts, jobs, data,
    software, connections, troubleshooting, RDHPCS

.. _FAQ:

##########################
Frequently Asked Questions
##########################


Accounts
========

.. faq:: How do I get an RDHPCS account?
   :id: get-account
   :tags: account application new user access getting started

   See :ref:`Applying for a user account <applying_for_user_account>`.

.. faq:: Why am I getting an "Invalid username or password" error on Parallel Works?
   :id: pw-invalid-password
   :tags: parallel works PW login authentication error invalid password

   If you are an on-premise HPC system user logging into Parallel Works
   for on-prem HPC systems access, follow these steps before requesting help:

   #. Make sure you are using your RSA token to authenticate. CAC
      authentication is not supported.
   #. Make sure you can successfully log into the on-prem HPCS system --
      PPAN, Ursa, Gaea, Hera, or Niagara.
   #. Now try to login to the Parallel Works platform.

   If you continue to get an "Invalid username error", confirm your
   `RDHPCS SSO authentication status
   <https://sso.rdhpcs.noaa.gov/realms/NOAA-RDHPCS/account/>`_.

   As needed, :ref:`request help <getting_help>`.

.. faq:: What do I do if my RSA token is locked?
   :id: rsa-token-locked
   :tags: RSA token locked authentication wait timeout

   Wait 15 minutes and try again.

   As needed, :ref:`request help <getting_help>` for your accounts, with
   a subject line of "Please check RSA token status." If you can, include
   the full terminal output you received when you tried to use your
   token.

.. faq:: How do I reset my passphrase?
   :id: reset-passphrase
   :tags: passphrase password reset forgot forgotten

   On the 4th attempt the system will prompt to recreate a passphrase.
   See :ref:`Connecting for the first time <connecting-to-rdhpcs>`.

.. faq:: How do I use X11 applications with a role account?
   :id: x11-role-account
   :tags: X11 role account shared account xsudo DISPLAY graphics

   A role account is a shared user account used by a project when multiple
   users need to manage some workload. To use X11 applications with a role
   account, use the ``xsudo`` utility:

   .. code-block:: shell

      $ xsudo <role_account_name>

   Before switching to the role account, note your DISPLAY environment
   variable:

   .. code-block:: shell

      $ echo $DISPLAY

   After switching with ``xsudo``, set the DISPLAY variable to the value you
   recorded:

   .. code-block:: shell

      $ export DISPLAY=localhost:14.0   # Use your actual value

   For complete information about role accounts, including how to request one
   and other access methods, see :ref:`role_accounts`.


Jobs
====

.. faq:: Why hasn't my job started after waiting a long time?
   :id: job-not-starting
   :tags: job pending waiting queue scheduler FairShare priority start

   We use the Slurm "FairShare" algorithm for scheduling jobs and
   jobs are scheduled based on job priority.

   You can find the "current" FairShare value of your project(s) by
   running the

   .. code-block:: shell

      saccount_params

   Please see the following link for details about how this algorithm
   works in our environment: :ref:`slurm-priority-and-fairshare`. More often
   than not, your job isn't starting because the system is full.

   The RDHPCS systems are for research and development and instantaneous
   job starts should not be expected. Even when it might appear that
   there are free resources, there are often reservations
   that are securing resources for future use.

   One change you can make that will help the system schedule your job
   sooner is to specify an accurate wall clock time (``--time=hh:mm:ss``).
   You should pick a time that is roughly 10-15%
   longer than your average job length. By doing this, and not just
   putting a default time of 8:00 hours, the system can better optimize
   how resources are used and find space on the system to run your job
   sooner.

   You can also run the following command to check for errors that are
   preventing the job from running:

   .. code-block:: shell

      scontrol show job jobid

   where jobid is the job ID of the job in question.

.. faq:: Why hasn't my job started even though it's in a reservation?
   :id: job-in-reservation
   :tags: job reservation pending queue not starting

   If you have this problem, please run the following commands and send
   the output to the Help Desk so that we can diagnose the problem.

   .. code-block:: shell

      $ squeue --job $JOB_ID
      $ scontrol show job $JOB_ID

.. faq:: What do Slurm exit codes mean?
   :id: slurm-exit-codes
   :tags: exit code error failed job sacct signal terminated killed

   You can check a completed job's exit code using the ``sacct`` command:

   .. code-block:: shell

      $ sacct -j <jobid> --format=JobID,JobName,State,ExitCode

   The ``ExitCode`` field shows two numbers separated by a colon
   (e.g., ``1:0``). The first number is the exit code returned by the job
   script or application. The second number is the signal number if the job
   was terminated by a signal (0 means no signal).

   **Common Slurm job states and their meanings:**

   .. list-table::
      :header-rows: 1
      :widths: 15 85

      * - State
        - Description
      * - COMPLETED
        - Job finished successfully (exit code 0)
      * - FAILED
        - Job terminated with a non-zero exit code
      * - TIMEOUT
        - Job exceeded its time limit
      * - CANCELLED
        - Job was cancelled by the user or administrator
      * - OUT_OF_MEMORY
        - Job exceeded memory limit and was killed

   **Understanding exit codes:**

   - **Exit code 0**: Job completed successfully
   - **Exit codes 1-127**: Application-specific error codes
   - **Exit codes 128+**: Job was terminated by a signal. Subtract 128 to
     find the signal number.

   For example, exit code 143:

   .. code-block:: shell

      143 - 128 = 15

   To see which signal corresponds to which number:

   .. code-block:: shell

      $ kill -l

   Signal 15 is TERM (**terminated**), which means the job was killed by
   the user, administrator, or the scheduler (e.g., due to time limit).

   **Common signals:**

   - **9 (KILL)**: Forcefully terminated
   - **11 (SEGV)**: Segmentation fault (memory access error)
   - **15 (TERM)**: Graceful termination request

   For more details on job states, see :ref:`slurm-state-codes`.

.. faq:: Why are all my multi-node MPI jobs timing out?
   :id: mpi-timeout
   :tags: MPI multi-node timeout wall time SSH keys permissions

   If you find that all of your multi-node jobs are getting stuck
   and running into **wall time limit exceeded** error, it
   is possible that you have a problem with your keys, or in some cases,
   because of incorrect permissions settings on the
   ``~/.ssh`` directory.

   A simple way to check if this is indeed the problem is to try the
   following:

   While logged into one of the front end nodes, try to ssh to
   another front end node. Normally you should be able to do this without
   being prompted for a password. If you are prompted for a password,
   refer to :ref:`ssh-between-nodes`.

.. faq:: Why do my multi-node jobs fail on mpirun/mpiexec?
   :id: mpi-fail
   :tags: MPI mpirun mpiexec fail stack size ulimit parallel

   If you are able to run some parallel jobs across nodes but not
   others, especially if the failure is right after the **mpirun** (or
   **mpiexec**) command, the most likely cause of that
   failure is the stack size setting. You need to set the stack size to
   be the appropriate value for your application. If you're not sure, you
   could set it to "unlimited". There are some rare instances
   we have seen problems when set to "unlimited", but so far
   most of the time it has been fine. If you're not able to determine a
   good number to set to you could try the unlimited setting.

   How you set the stack size depends on what your login shell is,
   **independent of the shell that is used for launching the job**.

   If your login shell is **csh/tcsh**:

   Add the following line to your ``~/.cshrc`` file:

   .. code-block:: shell

      limit stacksize unlimited

   If your login shell is **bash**:

   Add the following line to your ``~/.bashrc`` file:

   .. code-block:: shell

      ulimit -S -s unlimited

   .. note::

      Capital-S for soft limit

   Please also make sure that you have a ``~/.bash_profile`` file
   that contains the following (in addition to whatever you have for your
   own environment):

   .. code-block:: shell

      # Get the aliases and functions
      if [ -f ~/.bashrc ]; then
      . ~/.bashrc
      fi

   .. note::

      Trying to set the stack size within the job file does not work.
      This is because setting it within the job only changes the setting
      on the head node for the job, but the remaining nodes only get the
      **default** setting, or whatever is set in the initialization
      files.


Data
====

.. faq:: How can I recover recently deleted files from /home?
   :id: recover-home-files
   :tags: recover deleted files home snapshot backup restore

   The home filesystem supports snapshots, which allow you to retrieve your
   own files if they have been deleted in the last few days. Access
   snapshots at ``/home/.snapshot`` (or ``$HOME/.snapshot`` for your
   directory).

   .. code-block:: shell

      $ ls /home/.snapshot
      $ cd /home/.snapshot/<snapshot_date>/Your.Username
      $ cp <file> ~/

   For complete details on snapshot availability and usage, see
   :ref:`home_snapshot`.

.. faq:: How can I recover files deleted from my project space?
   :id: recover-project-files
   :tags: recover deleted files project scratch backup restore gone

   You usually cannot.

   Please note that only the /home filesystem is backed up. Project
   space is typically assigned on very large high performance file
   systems and hence cannot be backed up. **Any files deleted from
   project space are gone forever and cannot be recovered.**

   So it is important to have a second copy of files that are
   irreplaceable. Files like source files should typically be stored in
   source code repositories and irreplaceable data files should be
   stored in HPSS tape archive.

.. faq:: How do I find out which directories and partitions I can use?
   :id: find-directories
   :tags: directories partitions scratch work storage access sinfo

   Use the ``saccount_params`` command to see your project associations,
   available partitions, and Quality of Service (QOS) options:

   .. code-block:: shell

      $ saccount_params

   This displays your projects, available partitions, and QOS settings. For
   more detailed information about available partitions on a system:

   .. code-block:: shell

      $ sinfo

   To see which accounts and partitions you have access to:

   .. code-block:: shell

      $ sacctmgr show associations user=$USER format=Account,Partition,QOS

   For information about your project directories on scratch file systems,
   refer to the storage documentation for your specific system. Project
   directories are typically located at:

   - ``/scratch1/<portfolio>/<project>`` or ``/scratch2/<portfolio>/<project>``
     on Hera
   - ``/scratch3/<portfolio>/<project>`` or ``/scratch4/<portfolio>/<project>``
     on Ursa/Hera
   - ``/work/<project>`` or ``/work2/<project>`` on Orion/Hercules

   See :ref:`data-storage` for complete details on available file systems.

.. faq:: How do I find out what my project quota is?
   :id: project-quota
   :tags: quota disk space storage allocation usage limit

   To check your **home directory quota**, use the ``quota`` command:

   .. code-block:: shell

      $ quota -Qs

   To check your **project's scratch space usage and quota**, use the
   ``saccount_params`` command, which displays disk usage and quota
   information along with compute allocation details:

   .. code-block:: shell

      $ saccount_params

   For a more detailed view of scratch space usage by project:

   .. code-block:: shell

      $ shpcrpt -a <account_name>

   On Lustre file systems (such as Orion/Hercules), you can also use:

   .. code-block:: shell

      $ lfs quota -g <project_group> /work

   To check your **compute allocation** (core-hours), use:

   .. code-block:: shell

      $ shpcrpt -a <account_name>

   This shows your project's allocation, usage, and FairShare information.
   See :ref:`allocation` for details on how allocations work and how to
   request increases.


Software
========

.. faq:: Can RDHPCS install Python packages for me?
   :id: python-packages
   :tags: python package install conda pip module

   There are way too many combinations in which users use python so, it
   is not practical to have a "common" python installation that is
   applicable for all users. Python works best when users install the
   packages they need in their own project space.

   We have now opened up access to the conda forge repositories so it is no
   longer necessary to use the RDHPCS mirror for installing the Python
   packages you need. You should now be able to install Python packages
   the same way you would on your local desktop/laptop.

   Please search for "conda" in the search field for
   specific instructions (if any) on how to maintain your own python
   installations in our environment.

.. faq:: Why are my jobs failing intermittently?
   :id: jobs-failing-intermittently
   :tags: intermittent failure timeout MPI I_MPI_FABRICS environment

   We are getting reports of jobs failing intermittently with a job
   timeout error.

   At least in some instances this has been traced to an environment
   variable setting that is no longer valid. We were able to duplicate
   this problem very easily with a simple MPI Hello World program.

   The setting in question is the following environment variable:

   .. code-block:: shell

      export I_MPI_FABRICS=shm:ofa

   This setting should no longer be set.
   When this variable is set we were able to confirm that even a simple
   MPI Hello World code can fail intermittently even when run on the same
   set of nodes. While it is true that it happens only on some nodes and
   rebooting them clears the nodes, not setting the above environment
   variable does not cause this problem. We do plan to reboot the nodes
   that exhibit the problem, but users can take action to avoid running
   into this problem by simply unsetting the above environment variable.

   If you are still seeing this error even though you have not set this
   environment variable please submit a help ticket to report the problem.

.. faq:: Why am I getting errors with hpc-stack or NCEPLIBS?
   :id: hpc-stack-errors
   :tags: hpc-stack NCEPLIBS module error library

   If you are using `hpc-stack <https://github.com/NOAA-EMC/hpc-stack>`_
   please keep in mind that this is a software stack that is installed
   and maintained by the NCEPLIBS team. Please refer to the `hpc-stack
   official supported distribution
   <https://github.com/NOAA-EMC/hpc-stack/wiki/>`_.

   If you have problems, particularly with modules or NCEP libraries, it
   is very likely you are using an unsupported version of their
   libraries. If you are using the official version and still having
   problems, you should submit an "issue" ticket at the above link.

.. faq:: Why am I getting errors with spack-stack?
   :id: spack-stack-errors
   :tags: spack-stack EPIC module error library

   The spack-stack software is installed and maintained by the EPIC team,
   and the RDHPCS administrators are not able to provide assistance with
   these issues.

   If you are using `spack-stack <https://github.com/JCSDA/spack-stack>`_
   and are encountering spack-stack related issues, you will need to submit
   an issue on their
   `github repository <https://github.com/JCSDA/spack-stack/issues>`_.

   You will find a link to their documentation at the github site
   above.

.. faq:: Why are my NCL jobs no longer working?
   :id: ncl-not-working
   :tags: NCL NCAR pyncl deprecated python visualization

   .. warning::

      NCAR Command Language (NCL) has been in maintenance mode since
      September 2019 and is no longer actively developed. NCAR recommends
      transitioning to Python-based tools.

   If you have existing NCL scripts, you can still run them using the
   ``pyncl`` module:

   .. code-block:: shell

      module load pyncl

   This provides NCL version 6.6.2 commands, libraries, and headers.

   **For new work**, NCAR recommends using Python with packages such as:

   - `xarray <https://xarray.dev/>`_ for netCDF data handling
   - `matplotlib <https://matplotlib.org/>`_ and
     `cartopy <https://scitools.org.uk/cartopy/>`_ for visualization
   - `geocat-viz <https://geocat-viz.readthedocs.io/>`_ for NCL-style plots
     in Python

   For migration guidance and Python equivalents of NCL functions, see the
   `NCAR GeoCAT documentation <https://geocat.ucar.edu/>`_ and the
   `NCL to Python Transition Guide
   <https://geocat-examples.readthedocs.io/en/latest/ncl-to-python.html>`_.

   If you must continue using NCL and encounter issues with newer Fortran
   features, load a more recent GNU compiler:

   .. code-block:: shell

      module load gnu/9.2.0 pyncl

.. faq:: How do I compile WRF on Hera with Rocky OS?
   :id: compile-wrf-hera
   :tags: WRF compile build Hera Rocky tirpc

   For the earlier versions of WRF model, the user may need the following
   to compile the model on Rocky8 OS. After loading the required
   modules, user needs to add the following to the CPATH in order to
   compile the WRF model.

   .. code-block:: shell

      setenv CPATH /usr/include/tirpc:$CPATH

   After running the configure command, user needs to add "-ltirpc" to
   configure.wrf file.

   .. code-block:: shell

      LIB_EXTERNAL    = \
          -L$(WRF_SRC_ROOT_DIR)/external/io_netcdf -lwrfio_nf \
          -L/apps/netcdf/4.9.2/gnu-9.2.0/lib -lnetcdff -lnetcdf -ltirpc


Connections
===========

.. faq:: How do I change my default login shell?
   :id: change-shell
   :tags: shell bash csh tcsh change default AIM

   To change your default shell:

   * Log into `AIM  <https://aim.rdhpcs.noaa.gov/>`_.
   * Click "view your information in AIM".
   * Navigate down to the "Projects and Account Information" section.
   * Click the dropdown menu (middle panel) next to "Shell selection".
   * Choose your shell from the list and click the "Submit Changes"
     button in the bottom section

   Once your help ticket is processed, the change should be complete
   within 24 hours.

.. _ssh-between-nodes:

.. faq:: Why can't I SSH between nodes without entering a password?
   :id: ssh-between-nodes
   :tags: SSH password nodes keys authorized_keys permissions

   If you are getting prompted for a password while trying to SSH between
   front end nodes there are two possible causes. The causes of those
   problems and their fixes are shown below (please note you may need to
   fix only one of these issues):

   1. You may have generated new keys and not added them to the
      authorized_keys file. The fix is to run the following:

      .. code-block:: shell

         cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

   2. You may have inadvertently changed permissions for your ~/.ssh
      directory. The fix is to run the following command:

      .. code-block:: shell

         chmod -R 700 ~/.ssh

   .. note::

      It is important to note that the keys generated should be created
      without a passphrase. That is, when you are generating the keys
      using **ssh-keygen** please be sure to press **Enter**
      when prompted for the passphrase for the key.

   You should now be able to access the requested node via SSH without
   being prompted for a password.

.. faq:: When is my .bashrc executed?
   :id: bashrc-execution
   :tags: bashrc bash_profile shell initialization login interactive

   Please review :manpage:`bash(1)` and other information on the `bash
   shell <https://www.gnu.org/software/bash/>`_ on the `internet
   <https://opstree.com/blog/2020/02/11/shell-initialization-files/>`__.

.. faq:: What does the "REMOTE HOST IDENTIFICATION HAS CHANGED" error mean?
   :id: host-key-changed
   :tags: SSH host key changed warning known_hosts security

   You may sometimes get an error message such as the one shown below
   when attempting to access a remote machine when using ssh/scp/wget or
   any such command that accesses a remote machine:

   .. code-block:: shell

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
      **Offending RSA key in /Users/first.last/.ssh/known_hosts:5**
      RSA host key for [localhost]:55362 has changed and you have requested strict checking.
      Host key verification failed.

   Most of the time when you get that message, it is likely that the host
   key on the remote machine has indeed changed, and it is not an attack.

   Under rare circumstances it is possible that someone is trying to do
   what is called a "man-in-the-middle" attack. If you are accessing one
   of the RDHPCS machines and you can be reasonably certain you can ignore
   that message, implement the solution given below.

   If the remote machine is a non-RDHPCS system you will have to
   independently verify if the key has actually changed. If it is a well
   known site such as github etc, they generally post an announcement on
   their site that the keys have changed. And if you know that the key
   has changed it is fine to go ahead and implement the solution given
   below.

   After verifying that it is not an attack, the solution is to remove the
   offending key (shown in the error message) from the
   **~/.ssh/known_hosts** file on the machine where you see the above
   error. In the highlighted message above, **5** is the line
   number in the ``~/.ssh/known_hosts`` file.

   In the example shown above, since line 5 is the problem key, you can
   use your favorite editor and delete that line. Alternatively on a
   Linux like systems you use the following command:

   .. code-block:: shell

      sed -i.bak -e '5d' ~/.ssh/known_hosts

.. faq:: How do I enable X11 forwarding using PowerShell on Windows?
   :id: x11-powershell
   :tags: X11 forwarding Windows PowerShell Xming DISPLAY graphics

   **Xming** is a popular X Server for Windows. If you don't have a
   program such as Xming installed on your local machine you have to
   install that first. It is a good idea to have Xming running on your
   machine, so please start that program if you have not done so already.

   Assuming Xming is already installed on your system:

   1. Start Powershell and paste the following command:

      .. code-block:: shell

         $env:DISPLAY= 'localhost:0.0'

      (you need to type this command each time before using X11 forwarding.)

   2. Now connect to SSH server using -X argument:

      .. code-block:: shell

         ssh username@hostname -XY

   X11 forwarding is now enabled on Powershell.

   If the remote system is a Linux system you can quickly check if X
   forwarding is working by running the command **xclock**.

.. faq:: How do I set up an SSH port tunnel?
   :id: ssh-port-tunnel
   :tags: SSH port tunnel transfer data bastion forwarding

   SSH port tunnels allow you to transfer data between your local machine
   and RDHPCS systems. You must establish the tunnel from your **initial**
   bastion session - if you see "Address already in use" errors, you
   already have an open session.

   **Quick steps:**

   1. Find your unique local port number (displayed when you log in)
   2. Establish tunnel:
      ``ssh -L XXXXX:localhost:XXXXX First.Last@bastion_hostname``
   3. Use ``scp -P XXXXX`` or ``rsync`` with the tunnel for transfers

   For complete instructions including PuTTY/Windows setup, troubleshooting,
   and examples, see :ref:`Port_Tunnelling`.

.. faq:: How do I set up an SSH port tunnel with PuTTY on Windows?
   :id: ssh-port-tunnel-putty
   :tags: SSH port tunnel PuTTY Windows transfer

   For Windows users using PuTTY, configuration involves setting up port
   forwarding in the Connection > SSH > Tunnels settings.

   For step-by-step instructions with screenshots, see the
   :ref:`PuTTY port tunnel documentation <Port_Tunnelling>`.

.. faq:: How do I transfer small files to/from an RDHPCS system?
   :id: transfer-small-files
   :tags: transfer files scp rsync small data port tunnel

   For small file transfers, use SSH port tunnelling with ``scp`` or
   ``rsync``. For larger transfers or frequent use, consider using Globus
   or the Data Transfer Nodes (DTNs).

   See :ref:`data-transfer-overview` for complete information on all
   transfer methods.

.. faq:: Why can't I transfer files via the port tunnel anymore?
   :id: port-tunnel-blocked
   :tags: port tunnel transfer failed blocked connection refused

   Your first login from a given machine must establish the port tunnel. If
   you logged in without establishing the tunnel first, the port becomes
   blocked.

   **To resolve:**

   #. Exit all SSH sessions from your local machine
   #. Reconnect with port tunnel options: ``ssh -L XXXX:localhost:XXXX ...``
   #. Try your transfer again

   See :ref:`Port_Tunnelling` for detailed troubleshooting.


Other
=====

.. faq:: Where can I find operational data from WCOSS2 on Hera?
   :id: wcoss2-data
   :tags: WCOSS2 operational data Hera HPSS NCO

   Some operational data from WCOSS2 is available on Hera/HPSS.

   However RDHPCS doesn't keep track of the locations of the operational
   data stored on Hera/HPSS. Please reach out to the NCO SPA team that is
   responsible for making that data available by contacting them at
   nco.spa@noaa.gov.

.. faq:: What are the RDHPCS Office Hours?
   :id: office-hours
   :tags: office hours support help meeting

   Office Hours are held regularly. The Support team offers shared
   solutions to acute and common problems.

   Transcripts and recordings can be found in `RDHPCS Internal Documentation
   <https://sites.google.com/d/1QJ-MHpl1y0IEtzQUnIbjF2hUmMNQUMAo/p/1VimyvTrM3ilw2Eug4wrDHJsU9Zi5n5PW/edit>`__.


Known Issues
============

*Last reviewed: July 2026*

.. faq:: What is the Intel MPI Collective Algorithms issue?
   :id: intel-mpi-collective
   :tags: Intel MPI collective algorithms Ursa AMD NUMA

   It has been observed that the default algorithms configured by Intel
   oneAPI MPI for collective operations are causing instability on AMD
   systems. Users have reported instances of code hanging, and system
   monitoring indicates highly uneven Non-Uniform Memory Access (NUMA)
   load, leading to node performance issues.

   To mitigate these issues, a module has been created to set the
   collective algorithms to empirically tested values. We strongly
   recommend loading this module whenever utilizing Intel oneAPI for code
   execution on the Ursa cluster.

   .. code-block:: shell

      module load impi-collective-settings/1.0.0

   Please be advised that this module must be loaded in addition to the
   intel-oneapi-mpi module that your application needs.


Recent User-Facing Changes
==========================

*Last reviewed: July 2026*

.. faq:: Jan 22, 2025: DTNs for Ursa are now available
   :id: ursa-dtn-available
   :tags: Ursa DTN data transfer Globus scratch

   DTNs and the new file systems for Ursa are now available for your use.

   .. list-table::
      :header-rows: 1
      :stub-columns: 1
      :align: left

      * -
        - Host Name
        - File System
        - Globus Endpoints
      * - Trusted
        - dtn-ursa.fairmont.rdhpcs.noaa.gov
        - /scratch[34]
        - noaardhpcs#ursa
      * - Untrusted
        - udtn-ursa.fairmont.rdhpcs.noaa.gov
        - /scratch[34]/data_untrusted
        - noaardhpcs#ursa_untrusted

   Using these new DTNs you can do data transfers to the ``/scratch3``
   and ``/scratch4`` filesystems either using Linux tools such
   as scp and rsync, or by using Globus Online.

   Please see the :ref:`data-transfer-overview` for more details.
