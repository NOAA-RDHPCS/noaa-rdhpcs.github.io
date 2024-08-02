.. _FAQ:

####
FAQ
####

Frequently Asked Questions
==========================

Accounts
--------

How Do I Get an RDHPCS Account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Go to AIM: '''https://aim.rdhpcs.noaa.gov/'''
* Fill out your profile information - any organizational questions
  should be directed to your PI (Principal Investigator - the leader
  of your project).
* Select "Request new access to a project"
* Select "Click here to Request Access to a Project". On the project
  dropdown, search for the '''rdhpcs''' project.
* In the justification box, add "Requesting access to rdhpcs".
* Submit the request. Once approved, you will be able to request
  acce
  ss to additional projects. For more information, see `Accounts`_.

Need help, my RSA Token is locked.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the Accounts pages. If you continue to have trouble, send a help request to
rdhpcs.aim.help@noaa.gov with the subject line "Please check RSA token
status." If you can, include the full terminal output you received
when you tried to use your token.

I forgot my passphrase, how do I reset it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to this link: :ref:PASSPHRASE**
then refer to the section titled,
"Resetting Your Master Certificate Passphrase."

How do I use X11 appplication with shared user account (role account)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A shared user account (role account) is one that is typically used by
a project when multiple users need to manage some workload. After a
role account is created (via OTRS help request)
you can access it using sudo. Example:

.. code-block:: shell

  # sudo su - $SHAREDUNAME

Where $SHAREDUNAME is the role account name (ex: role.glopara). When
it asks for a password, use your token.

Using X applications can be tricky, but we have created a wrapper
script to help you. To allow for use of X applications while in the
shared account, use the tool '''xsudo'''. Ex:


.. code-block:: shell

  # xsudo $SHAREDUNAME

If you are planning to use X utilities with role accounts, you should
use the xsudo utility to switch to the role account and need to
explicitly set the DISPLAY environment variable.  So for example, if
you want to use role.rap-chem role account and would like the ability
to use X applications:

* First note the DISPLAY environment variable setting by doing:

.. code-block:: shell

    echo $DISPLAY

* Then use the xsudo command to switch to the role account:

.. code-block:: shell

    xsudo role.rap-chem

* Then set the DISPLAY environment variable to the '''value you
  obtained above''' just before doing xsudo; (please note that the
  next command you use depends on your shell):

  .. code-block:: shell

    export DISPLAY=localhost:14.0

That will enable your X applications to work.
A complete discussion of Role Accounts can be found here: :ref:`accounts`.

Jobs
----

My job hasn't started and I have been waiting a long time. What is wrong?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the Slurm "FairShare" algorithm for scheduling jobs and
jobs are scheduled based on job priority.

You can find the "current" FairShare value of your project(s) by
running the

.. code-block:: shell

  saccount_params

Please see the following link for details about how this algorithm
works in our environment: :ref:`slurm-priority-and-fairshare`. More often
that not, your job isn't starting because the system is full.

The RDHPCS systems are for research and development and instantaneous
job starts should not be expected. Even when it might appear that
there are free resources, there are often reservations (specifically
on Jet) that are securing resources for future use.

One change you can make that will help the system schedule your job
sooner is to specify an accurate wall clock time (''-l
walltime=hh:mm:ss''). You should pick a time that is roughly 10-15%
longer than your average job length. By doing this, and not just
putting a default time of 8:00 hours, the system can better optimize
how resources are used and find space on the system to run your job
sooner.

You can also run the following command to check for errors that are
preventing the job from running:

.. code-block:: shell

  scontrol show job jobid

where jobid is the job ID of the job in question.

My job hasn't started and it is in a reservation, what is wrong?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have this problem, please run the following commands and send
the output to the Help Desk so that we can diagnose the problem.

.. code-block:: shell

  # squeue --job $JOB_ID
  # scontrol show job $JOB_ID


All my multi-node MPI jobs are timing out, even simple jobs! What is wrong?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you find that all of your multi-node jobs are getting stuck
and running into **wall time limit exceeded** error, it
is possible that you have a problem with your keys, or some cases,
because of incorrect permissions settings on the
**/.ssh** directory.

A simple way to check if this is indeed the problem is to try the
following:

While logged into the one of the front end nodes, try to ssh to
another front end node. Normally you should be able to do this without
being prompted for a password. If you are prompted for a password,
refer to the next question.

My multi-node jobs fail on mpirun/mpiexec.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are able to run some parallel jobs across nodes but not
others, especially if the failure is right after the **mpirun** (or
**;mpiexec**) command, the most likely cause of that
failure is the stack size setting. You need to set the stack size to
be the appropriate value for your application. If you're not sure it
could set it to &quot;unlimited&quot;. There are some rare instances
we have seen problems when set to &quot;unlimited&quot;, but so far
most of the time it has been fine. If you're not able to determine a
good number to set to you could try the unlimited setting.

How you set the stack size depends on what your login shell is,
**independent of the shell that is used for lunch and the job**.

If your login shell is csh/tcsh
""""""""""""""""""""""""""""""""

Add the following line to your **/.cshrc** file:

.. code-block:: shell

  limit stacksize unlimited

If your login shell is bash:
""""""""""""""""""""""""""""

Add the following line to your **/.bashrc** file:

.. code-block:: shell

  ulimit -S -s unlimited

.. note::

  Capital-S for soft limit

Please also make sure to you have a **.bash_profile** file
that has the following (in addition to whatever you have for your own
environment):

.. code-block:: shell

    # Get the aliases and functions
    if [ -f ~/.bashrc ]; then
    . ~/.bashrc
    fi

.. note::

  Trying to set the stack size within the job file does not work!'''
  This is because setting it within the job only changes the setting
  on the head node for the job, but the remaining nodes only get the
  **default** setting, or whatever is set in the initialization
  files.

What is the meaning of the exit code?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When checking job status with the showq -c or checkjob command, it is
good to know the meaning of the completion code, or the CCODE column
for showq. Here is a list of exit code Moab reported from Torque:

.. code-block:: shell

  0   /* job exec successful */
 -1   /* job exec failed, before files, no retry */
 -2   /* job exec failed, after files, no retry  */
 -3   /* job execution failed, do retry    */
 -4   /* job aborted on MOM initialization */
 -5   /* job aborted on MOM init, checkpoint, no migrate */
 -6   /* job aborted on MOM init, checkpoint, ok migrate */
 -7   /* job restart failed */
 -8   /* exec() of user command failed */
 -9   /* could not create/open stdout stderr files */
 -10   /* job exceeded a memory limit */
 -11   /* job exceeded a walltime limit */
 -12   /* job exceeded a cpu time lim


When the number for the exit code is more than 128, subtract 128 from
the given exit code to see what signal was used to kill the job. For
example 143 is another common exit code seen:

.. code-block:: shell

  143 - 128 = 15

To see which signaled the response to what number you can use the command:

.. code-block:: shell

  kill -l

Which lists the signals in order. And you will see that 15 is TERM
(**terminated**).

So when a job has a completion code of 143, the job was terminated
with signal 15 (which is the TERM signal), which suggests that the job
was killed by the user or system administrator.

User
----

How do I change my default login shell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To change your default shell:

* Log into AIM.
* Click "view your information in AIM".
* Navigate down to the "Projects and Account Information" section.
* Click the dropdown menu (middle panel) next to "Shell selection".
* Choose your shell from the list and click the "Submit Changes"
  button in the bottom section

Once your help ticket is processed, the change should be complete
within 24 hours.

How can I recover recently deleted files from /home?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The home filesystem is backed up
regularly. However, the filesystem also supports snapshots, which will
allow you to retrieve your own files if they have been deleted over
the last few days. The number of days is different for Hera and Jet
clusters.

Look at the snapshot directory (/home/.snapshot) to see what
options are available. Each directory listed there represent a day. As an
example on Jet:

.. code-block:: shell

  2021-09-09_0015-0600.daily
  2021-09-12_0015-0600.daily	2021-09-15_0015-0600.daily
  2021-09-18_0015-0600.daily	2021-09-21_0015-0600.daily
  2021-09-10_0015-0600.daily  2021-09-13_0015-0600.daily
  2021-09-16_0015-0600.daily  2021-09-19_0015-0600.daily
  2021-09-22_0015-0600.daily 2021-09-11_0015-0600.daily
  2021-09-14_0015-0600.daily	2021-09-17_0015-0600.daily
  2021-09-20_0015-0600.daily	2021-09-23_0015-0600.daily

Hera is slightly different:

.. code-block:: shell

  2021-09-17_0015+0000.homeSnap  2021-09-20_0015+0000.homeSnap
  2021-09-23_0015+0000.homeSnap
  2021-09-18_0015+0000.homeSnap  2021-09-21_0015+0000.homeSnap
  AUTO_SNAPSHOT_8820a150-8f27-11d5-95ff-040403080604_694
  2021-09-19_0015+0000.homeSnap  2021-09-22_0015+0000.homeSnap

You can then access the old files in your copy of your home directory
under the appropriate snapshot.

For example, if you want to recover Hera files in your
<code>$HOME</code> from September 22nd, 2024, and your user name is
Robin.Lee:

.. code-block:: shell

  $ cd /home/.snapshot/2021-09-22_0015+0000.homeSnap/Robin.Lee


Copy the files you want from the here, the snapshot,  to anywhere in
your real home.

Why am I not able to ssh between nodes, it is asking me for a password!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are getting prompted for a password while trying to SSH between
FE nodes there are two possible causes. The causes of those
problems and their fixes are shown below (please note you may need to
fix only one of these issues):

1. You may have generated new keys and not added them to the authorized_keys
file. The fix is to run the following:


.. code-block:: shell

  cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys


1. You may have inadvertently changed permissions for your ~/.ssh
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

How can I recover files that I accidentally deleted from my project space?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You usually cannot.

Please note that only the /home filesystem is backed up.  Project
space is typically assigned on very large high performance file
systems and hence cannot be backed up. '''Any files deleted from
project space are gone forever and cannot be recovered.'''

So it is important to have a second copy of files that are
irreplaceable.  Files like source files should typically stored in
some source code repositories and irreplaceable data files should be
stored in HPSS tape archive.

How do I find out which directories and partitions I can use?

Refer to the Slurm pages.

How do I find out what my project quota is?

Refer to the allocation pages.

How to transfer small files to/from an RDHPCS system?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Port Tunnelling approach is useful for transferring small amount
data to/from RDHPCS systems from your local machine.

Transferring data using scp/WinSCP is a 2 step process:

1. Establish a Tunnel by following the steps documented here:
2. Transfer file using WinSCP

See the Data Transfer pages for complete information.

I can no longer transfer files via the port tunnel, please help!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From a given machine, your first login has to establish the port
tunnel. If you do not, the port used will be blocked and you cannot
establish the port tunnel with subsequent ssh commands. If you cannot
use scp to transfer files, look for an error message similar to this
the following when you are trying to establish your tunnel:

.. code-block:: shell

  ssh: connect to host localhost port 2083: Connection refused


The number above will match the port you are trying to use.

To resolve this problem:

#. Exit all ssh sessions from your host
#. Restart ssh to Jet. This session must have the port tunnel options included

.. code-block:: shell

  -L $PORT:localhost:$PORT

#. Try using scp to transfer a file.

Python
------

Can you please install the xyz python package(s)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are way too many combinations in which users use python so, it
is not practical to have a "common" python installation that is
applicable for all users.  Python works best when users install the
packages they need in their own project space.

We have now opened up access to the anaconda repositories so it is no
longer necessary to use the RDHPCS mirror for installing the Python
packages you need. You should now be able to install Python packages
the same way you would on your local desktop/laptop.

Please search for "anaconda" in the search field for
specific instructions (if any) on how to maintain your own python
installations in our environment.

Why are my jobs failing intermittently?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
set of nodes.  While it is true that it happens only some nodes and
rebooting them clears the nodes, not setting the above environment
variable does not cause this problem.  We do plan to reboot the nodes
that reboot the problem, but users can take action to avoid running
into this problem by simply unsetting the above environment variable.

If you are still seeing this error even though you have not set this
environment variable please submit a help tickdet to report the problem.

Why am I getting these errors? I am using hpc-stack for NCEPLIBS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using "hpc-stack" please keep in mind that this is a
software stack that is installed and maintained by the NCEPLIBS team.

Here is the link for their `official supported distribution
<https://github.com/NOAA-EMC/hpc-stack/wiki/Official-Installations>`_.

If you have problems, particularly with modules or NCEP libraries, it
is very likely you are using an unsupported version of their
libraries. If you are using the official version and still having problems, you
should submit an "issue" ticket at the above link.

I am using spack-stack and getting some errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using spack-stack and are having issues you will have to
submit an "issue" on their `github <https://github.com/NOAA-EMC/spack-stack>`_

The modules and associated software are not maintained by the system
administrators so you will have to work the spack-stack team through
the link above.

When is my .bashrc executed? When would it be ignored?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This `Opstree link <https://blog.opstree.com/2020/02/11/shell-initialization-files>`_
may help.

.. warning::

  REMOTE HOST IDENTIFICATION HAS CHANGED!

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
    '''<big>Offending RSA key in /Users/first.last/.ssh/known_hosts:5</big>'''
    RSA host key for [localhost]:55362 has changed and you have requested strict checking.
    Host key verification failed.


Most of the time when you get that message it is likely that the host
key on the remote machine has indeed changed and not an attack.

Under rare circumstances it is possible that someone is trying to do
what is called a "man-in-the-middle" attack.  If you are accessing one
of the RDHPCS machines you can be reasonably certain you can ignore
that message implement the solution given below.

If the remote machine is a non-RDHPCS system you will have to
independently verify if the key has actually changed.  If it is a well
known site such as github etc, they generally post an announcement on
their site that the keys have changed.  And if you know that the key
has changed it is fine to go ahead and implement the solution given
below.

After verifying that it is not an attach the solution is to remove the
offending key shown in the error message above from the
**~/.ssh/known_hosts** file on the machine where you seeing the above
error.  In the highlighted message above, **5** is the line
number in the **/.ssh/known_hosts** file.

In the example shown above, since line 5 is the problem key, you can
use your favorite editor and delete that line.  Alternatively on a
Linux like systems you use the following command:

.. code-block:: shell

   sed -i.bak -e '5d' ~/.ssh/known_hosts


Where can I find "Operational Data" from WCOSS2 on Hera?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some operational data from WCOSS2 is available on Hera/HPSS.

However RDHPCS doesn't keep track of the locations of the operational
data stored on Hera/HPSS. Please reach out the NCO SPA team that is
responsible for making that data available by contacting them at
'''nco.spa@noaa.gov'''.


My jobs using NCL are no longer working
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NCL has decided to switch to Python and have indicated the PyNCL will
be replacing NCL.

So if you are used to using:

.. code-block:: shell

   module load ncl

please load

.. code-block:: shell

   module load pyncl

That will make NCL version 6.6.2 commands and libraries and headers
available. If you use other ncl modules, we found that the gmeta files
created will be dodgy, and not show any content with idt, for example.

Also, we have seen some of the programs that use NCL are using the
newer features of the Fortran standard, so in addition to loading the
"pyncl" module you may consider loading a more recent version of the
GNU module.

So if you are working with NCL please use the following module load command:

.. code-block:: shell

   module load gnu/9.2.0 pyncl

Compile WRF on Hera/Jet with Rocky OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the earlier versions of WRF model, the user may need following
to compile the model on Rocky8 OS. After loading the required
modules, user needs to add the following to the CPATH in order to
compile the WRF model.

.. code-block:: shell

 setenv CPATH /usr/include/tirpc:$CPATH


After running the configure command, user needs to add "-ltirpc" to
configure.wrf file.

.. code-block:: shell

 LIB_EXTERNAL    = \
                      -L$(WRF_SRC_ROOT_DIR)/external/io_netcdf -lwrfio_nf -L/apps/netcdf/4.9.2/gnu-9.2.0/lib -lnetcdff -lnetcdf  -ltirpc

How do I enable x11 forwarding using PowerShell on a Windows system?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Xming** is a popular X Server for Windows, if you don't have a
program such as Xming installed on your local machine you have to
install that first. It is a good idea to have Xming running on your
machine, so please start that program if you have not done so already.

Assuming Xming is already installed on your system:

1. Start Powershell and paste the following command :

.. code-block:: shell

   $env:DISPLAY= 'localhost:0.0'

(you need to type this command each time before using x11 forwarding.)

2. Now connect to SSH server using -X argument :

.. code-block:: shell

   ssh username@hostname -XY

X11 forwarding is now enabled on Powershell.

If the remote system is a Linux system you can quickly check if X
forwarding is working by running the command **xclock**.

Recent User-Facing Changes
==========================

Apr 29, 2024: The new LFS5 filesystem on Jet
--------------------------------------------

The new LFS5 filesystem is now available on Jet and will be replacing
LFS1.  Users are urged to migrate from LFS1 to LFS5 as soon as
possible.  Please see data-transfer-overview TBD LINK **manageing data
to local file systems** for information on some of the utilities to
facilitate the move from LFS1 to LFS5

The new LFS5 file system has"hot pools" enabled and
uses part of the filesystem as cache.

You should use the output of '''saccount_prarms''' to see usage by
your project.   Since we have only project based quotas that is the
only quota that is enforced.

.. note::

    Please do not rely on the output of "du" to compare your file space usage.

To find information of usage by user, refer to the Slurm pages.


Apr25, 2024: Rocoto updateto version rocoto/1.3.7 on Hera/Jet/Niagara
---------------------------------------------------------------------

There were some performance
issues and some minor bugs in rocoto/1.3.6
after the migration to Rocky8, mostly caused by the performance of
Ruby that comes with the OS.  So Ruby/3.2.3 was installed as module
and the latest version of rocoto/1.3.7 has been built in installed as
the default version.

Please see the Rocoto pages under Software.


Apr 9, 2024: The aging uJet and tJet clusters are being turned off
------------------------------------------------------------------

The uJet and tJet clusters are being turned off as they are based on very old
hardware, and it is becoming difficult to support them on the newer OS.

This means the '''ujet''' and '''tjet''' partitions are no longer
available, so please use one of the other available partitions.

Apr 2, 2024: Migration to Rocky8 in phases (Complete)
-----------------------------------------------------

.. note::

    Hera/Niagara/Jet are all now on Rocky8 and the transition
    to Rocky8 is complete.

Please see the following Google Doc for `information about the transition
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.9971adjl0yrd>`_

This is an evolving document and will be updated with new information
as needed.

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Mar 19, 2024: Migration to Rocky8 in phases
-------------------------------------------

We continue to make progress on the gradual Migration from CentOS7 to Rocky8.

.. code-block:: shell

    |=========================================================|
    |  Unless you select a specific node, you will land       |
    |  on a Rocky8 node and any jobs you submit from there    |
    |  will run on the Rocky8 nodes.                          |
    |                                                         |
    |  If you need to use CentOS7 for some reason, you can    |
    |  do so by pressing ^C when the list of hosts is         |
    |  presented and pick a CentOS7 node.n                    |
    |                                                         |
    |  Please begin migrating to Rocky8 ASAP!                 |
    |=========================================================|


See the weekly announcements for the schedule and the latest updates.

Current migration status
^^^^^^^^^^^^^^^^^^^^^^^^

* Jet:

  - All clusters except kJet on Rocky8
  - When you login the default login node will be a Rocky8 login node

* Hera:

  - 2/3rd of Hera and 1/2 of FGE nodes are on Rocky8
  - When you login the default login node will be a Rocky8 login node

* Niagara:

  - All of Niagara is on Rocky8

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Feb 20, 2024: Migration to Rocky8 in phases
-------------------------------------------

Both Hera and Jet have begun the migration to Rocky8 in phases.
Please see the weekly announcements for the schedule.

.. code-block:: shell

    |=========================================================|
    |  Unless you select a specific node, you will land       |
    |  on a CentOS-7 node and any jobs you submit from there  |
    |  will run on the CentOS-7 nodes.                        |
    |                                                         |
    |  Please exercise Rocky8 nodes by explicitly selecting   |
    |  one of the nodes from fe[5-8] and jobs submitted from  |
    |  will run on the Rocky8 nodes.                          |
    |=========================================================|


Please see the following Google Doc for `information about the transition
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.9971adjl0yrd>`_

This is an evolving document and will be updated with new information
as needed.

To report Rocky8 issues, submit a helpdesk ticket with subject
"Rocky8:<description>".

Jan 17, 2024: Rocoto updated to version 1.3.6
---------------------------------------------

The Rocoto Workflow Manage has been updated to the latest version,
version 1.3.6. This version has some very important fixes, so it is
very important to switch this version as soon as possible.

Please keep in mind the following general guidelines for using Rocoto:

For your module loads:
    **module load rocoto**            is preferable to
    module load rocoto/1.3.6

For your crontab entries:
   **/apps/rocoto/default/bin/rocotorun**        is preferable to
   /apps/rocoto/1.3.6/bin/rocotorun

Please be sure to modify your scripts and also your **crontab**
entries!

RDHPCS Office Hours
===================

Office Hours are held at regularly. The Support team offers shared
solutions to acute and common problems.

20 June 2024
------------

Ron Millikan presented `Tensorflow Jumpstart Training <https://drive.google.com/file/d/1WklYsbKrp8_4tydqkayAM6EwCVKDNG-9/view>`_.
A `transcript the training <https://docs.google.com/document/d/1Ys5S0YGeREmJgXy_KQ6tOygidVV7zGdmmzJDqIZTDzY/edit>`_ of the training is available as well.

4 June 2024
-----------

The Support Team discussed `issues concerning the
transition of Orion from Rocky8 to Rocky9
<https://mail.google.com/mail/u/0/?pli=1#inbox/FMfcgzQVwxHbVFPQmVbgbXmkhCrzXlKq?projector=1
here.>`_

10 May 2024
-----------

`Issues concerning data transfer in the Cloud
<https://drive.google.com/file/d/13TZiHRBi4ISAALmrxXY0J3Wv8ccm4oex/view>`_
A `transcript of the meeting is available
<https://docs.google.com/document/d/1vbYrndTaAeiy7qAs2alx9proKmHwtK5x-C2YFXDbPt4/edit#heading=h.rqoqmdvh8gtp>`_

26 April 2024

The Support Team fielded issues with Hercules and Rocoto. The team
discussed Gaea, and that cron is not allowed to run there. This may
present issues when the C6 system comes on line.


29 March 2024
-------------

The transition to Rocky8 remains a matter of concern. Raj suggested
that Centos7 might be maintained in Google Cloud in a single
environment, on an emergency basis. Unni is testing Rocky8 in the
Globus and Azure space in the Cloud; he expects to report at the next
Office Hours meeting. Several users raised specific Rocky8 issues in
this call.

A `recording of the meeting is available
<https://drive.google.com/file/d/18Uigf1mtdKNXt9GAdB4y8zwbTeG_9lRL/view>`_

15 March 2024
-------------

The upgrade from Centos7 to Rocky8 Operating Systems remains a key
issue. System users and the Support Team `discussed plans, benchmarks
and the effects of the transition.
<https://drive.google.com/file/d/1a6xNqxFZ9SPVzZRtuBEW_P1GuZ2U40CA/view>`_

Note that there is `transition documentation for system users
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.cheodqg1384>`_

1 March 2024
------------

Currently the most critical issue in the RDHPCS environment is the
planned upgrade from Centos7 to Rocky8 Operating Systems.
Transition documentation for system users is available
Note that there is `transition documentation for system users
<https://docs.google.com/document/d/1oLqDkslD-99-zpkKD4MtKMmqdm2D4oAo1l7gHHfvKBM/edit#heading=h.cheodqg1384>`_

You can review the `meeting notes
<https://docs.google.com/document/d/17l8MHlKo_Dx6IXdHODFY3iEdkpH6A_XNtqf_WiwMEzs/edit?usp=sharing>`_

New User Office Hour 28 Feb 2024
--------------------------------

This was a pilot session for new RDHPCS system users. It was offered
as an open session for asking technical questions! In addition, the
User Support team requested feedback on what would have helped new
users getting introduced to the RDHPCS environment.

The team shared `notes from the meeting
<https://docs.google.com/document/d/1Y0ggCrYGcY4yrMeV8SSX4nh2POIbzVFhzGyMmKtozYY/edit>`_

4 Jan 2024
----------

`Cumulative notes
<https://docs.google.com/document/d/18RbFULSZ9wppSnXrXAN0_327tKJJjbIy1st2d8Bc67w/edit#heading=h.om52ynf0dwon>`_

Topics for discussion:

* Would there be interest in short presentations to cover those topics?

  - Setting up Python on RDHPCS systems
  - Using Globus CLI for data transfer
  - Brown Bag Session items proposed by Leslie

* Discussion on Operating System migration from Centos7 to Rocky8,
  to be completed by June 2024.
* Wikis, errors and room for improvement
* File transfer issues
* Regional models working on Hera
* Cluster creation
* Containerization
* Supercomputing conference and applicability to RDHPCS
* What information should be provided as background to new users?

15 December 2023
----------------

`Office hour notes <https://docs.google.com/document/d/1C303IDoCM4wpkHkKl4QFbJlNvBesz66d2nEhBpQ_Ddo/edit>`_

30 Nov 2023
-----------

The premier session for RDHPCS Office Hours was held on 30 November 2023.
`Office hour notes <https://docs.google.com/document/d/1mXpRHhp909ybqyjhU0LXRNCkuWhwS41v-aLK7EWn588/edit>`_`

