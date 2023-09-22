.. _common-material:


#######
Common Material: FAQs
#######

.. _account_how_do_i_get_an_rdhpcs_account:

Account: How Do I Get an RDHPCS Account?
========================================

-  Go to AIM: https://aim.rdhpcs.noaa.gov/
-  Fill out your profile information - any organizational questions
   should be directed to your PI (Principal Investigator - the leader of
   your project).
-  Select "Request new access to a project"
-  Select "Click here to Request Access to a Project". On the project
   dropdown, search for the **rdhpcs** project.
-  In the justification box, add "Requesting access to rdhpcs".
-  Submit the request. Once approved, you will be able to request access
   to additional projects. For more information, please see
   `here <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_an_RDHPCS_Account>`__\ **.**

.. _python_can_you_please_install_the_xyz_python_packages:

Python: Can you please install the xyz python package(s)?
=========================================================

There are way too many combinations in which users use python so, it is
not practical to have a "common" python installation that is applicable
for all users. Python works best when users install the packages they
need in their own project space.

We have now opened up access to the anaconda repositories so it is no
longer necessary to use the RDHPCS mirror for installing the Python
packages you need. You should now be able to install Python packages the
same way you would on your local desktop/laptop.

Please search for "anaconda" in the search field in the wiki for
specific instructions (if any) on how to maintain your own python
installations in our environment.

.. _account_my_rsa_token_is_locked_please_help:

Account: My RSA Token is locked, please help!
=============================================

If you entered the wrong PIN and RSA token value 3 times during any of
our login attempts, it will be automatically locked for 15 minutes.
After 15 minutes, the token will automatically unlock and you will be
able to attempt to authenticate again by entering your correct
credentials.

If you are still experiencing issues with your token, it is possible
that it might be out of sync. Please open a help ticket to
**rdhpcs.aim.help@noaa.gov** with the title "Please check RSA token
status." To expedite troubleshooting, please include the full terminal
output you received when you tried to use your token.

.. _account_i_forgot_my_passphrase_how_do_i_reset_it:

Account: I forgot my passphrase, how do I reset it?
===================================================

Just request a new passphrase certificate; the process is automated and
will respond to you within 15 minutes.

-  Type in a bad passphrase 4 times
-  The system will ask you if you want to reset your passphrase, say yes
-  Choose your passphrase; you will be asked to reconfirm your new
   passphrase and then you will be logged out

**Please Note:** The certificate will need to be signed by an
administrator, this can take up to one business day. You will be able to
login once your certificate has been signed.

.. _user_how_do_i_change_my_default_shell:

User: How do I change my default shell?
=======================================

To change your default shell:

-  Log into AIM at https://aim.rdhpcs.noaa.gov/
-  Click on the "Verify or change my information in the system" link
-  Navigate down to the "Account Information" section
-  Click the dropdown menu next to "Shell selection"
-  Choose your shell from the list
-  Scroll down to the "Update Information" button
-  Open a help ticket to **rdhpcs.aim.help@noaa.gov** with the subject:
   **Shell Change Request**. Include in the ticket what you would like
   your shell changed to.

Once your help ticket is processed, the change should be complete within
24 hours.

.. _user_how_can_i_recover_recently_deleted_files_from_home:

User: How can I recover recently deleted files from /home?
==========================================================

| Different between the HPCS
| The home filesystem is backed up regularly. However, the filesystem
  also supports snapshots, which will allow you to retrieve your own
  files if they have been deleted over the last few days. The number of
  days is different for Hera and Jet clusters.

Look at the snapshot directory (/home/.snapshot) to see what options are
available. Each directory listed there represent a day. As an example on
Jet:

::

   2021-09-09_0015-0600.daily  2021-09-12_0015-0600.daily 2021-09-15_0015-0600.daily  2021-09-18_0015-0600.daily  2021-09-21_0015-0600.daily
   2021-09-10_0015-0600.daily  2021-09-13_0015-0600.daily  2021-09-16_0015-0600.daily  2021-09-19_0015-0600.daily  2021-09-22_0015-0600.daily
   2021-09-11_0015-0600.daily  2021-09-14_0015-0600.daily  2021-09-17_0015-0600.daily  2021-09-20_0015-0600.daily  2021-09-23_0015-0600.daily

Hera is slightly different:

::

   2021-09-17_0015+0000.homeSnap  2021-09-20_0015+0000.homeSnap  2021-09-23_0015+0000.homeSnap
   2021-09-18_0015+0000.homeSnap  2021-09-21_0015+0000.homeSnap  AUTO_SNAPSHOT_8820a150-8f27-11d5-95ff-040403080604_694
   2021-09-19_0015+0000.homeSnap  2021-09-22_0015+0000.homeSnap

You can then access the old files in your copy of your home directory
under the appropriate snapshot.

For example, if you want to recover Hera files in your ``$HOME`` from
September 22nd, 2021, and your user name is John.Smith

::

   $ cd /home/.snapshot/2021-09-22_0015+0000.homeSnap/John.Smith
   # – Copy the files you want from the here, the snapshot,  to anywhere in your real home.

.. _user_how_can_i_recover_files_that_i_accidentally_deleted_from_my_project_space:

User: How can I recover files that I accidentally deleted from my project space?
================================================================================

You usually cannot.

Please note that only the /home filesystem is backed up. Project space
is typically assigned on very large high performance file systems and
hence cannot be backed up. **Any files deleted from project space are
gone forever and cannot be recovered.**

So it is important to have a second copy of files that are
irreplaceable. Files like source files should typically stored in some
source code repositories and irreplaceable data files should be stored
in HPSS tape archive.

.. _user_how_do_i_find_out_which_directories_i_can_use_how_my_project_quota_is_and_which_partitions_i_can_use:

User: How do I find out which directories I can use, how my project quota is, and which partitions I can use?
=============================================================================================================

Please see

`Getting Information About Your Account -
SLURM <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_Information_About_Your_Account_-_SLURM>`__
and

`Managing File System
Allocations <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Managing_File_System_Allocations>`__

.. _user_i_can_no_longer_transfer_files_via_the_port_tunnel_please_help:

User: I can no longer transfer files via the port tunnel, please help!
======================================================================

From a given machine, your first login has to establish the port tunnel.
If you do not, the port used will be blocked and you cannot establish
the port tunnel with subsequent ssh commands. If you cannot use scp to
transfer files, look for an error message similar to this the following
when you are trying to establish your tunnel:

::

   ssh: connect to host localhost port 2083: Connection refused

The number above will match the port you are trying to use.

To resolve this problem, do the following:

#. Exit all ssh sessions from your host
#. Restart ssh to Jet, and this session must have the port tunnel
   options included (-L $PORT:localhost:$PORT).
#. Try using scp to transfer a file.

.. _job_my_job_hasnt_started_and_i_have_been_waiting_a_long_time._what_is_wrong:

Job: My job hasn't started and I have been waiting a long time. What is wrong?
==============================================================================

We are using the Slurm "FairShare" algorithm for scheduling jobs and
jobs are scheduled based on job priority. Please see the following link
for details about how this algorithm works in our environment:

https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/SLURM_FairShare

More often that not, your job isn't starting because the system is full.

The RDHPCS systems are for research and development and instantaneous
job starts should not be expected. Even when it might appear that there
are free resources, there are often reservations (specifically on Jet)
that are securing resources for future use.

One change you can make that will help the system schedule your job
sooner is to specify an accurate wall clock time (*-l
walltime=hh:mm:ss*). You should pick a time that is roughly 10-15%
longer than your average job length. By doing this, and not just putting
a default time of 8:00 hours, the system can better optimize how
resources are used and find space on the system to run your job sooner.

You can also run the following command to check for errors that are
preventing the job from running:

::

   scontrol show job jobid

where jobid is the job ID of the job in question.

.. _job_my_job_hasnt_started_and_it_is_in_a_reservation_what_is_wrong:

Job: My job hasn't started and it is in a reservation, what is wrong?
=====================================================================

If you have this problem, please run the following commands and send the
output to the Help
Desk\ `https://rdhpcs-common-docs-test.rdhpcs.noaa.gov/wiki/index.php/Help_Requests
Help
Requests <https://rdhpcs-common-docs-test.rdhpcs.noaa.gov/wiki/index.php/Help_Requests_Help_Requests>`__
so that we can diagnose the problem.

::

   # squeue --job $JOB_ID
   # scontrol show job $JOB_ID

.. _job_all_my_multi_node_mpi_jobs_are_timing_out_even_simple_jobs_what_is_wrong:

Job: All my multi-node MPI jobs are timing out, even simple jobs! What is wrong?
================================================================================

If you're finding that all of your multi-node jobs are getting stuck and
running into "**wall time limit exceeded**" error, it is possible that
you have a problem with your keys, or some cases, because of incorrect
permissions settings on the "**~/.ssh**" directory.

A simple way to check if this is indeed the problem is to try the
following:

While logged into the one of the front end nodes, try to ssh to another
front end node. Normally you should be able to do this without being
prompted for a password. If you are prompted for a password, please see
the answer to the next question on how to fix this problem.

.. _user_why_am_i_not_able_to_ssh_between_nodes_it_is_asking_me_for_a_password:

User: Why am I not able to ssh between nodes, it is asking me for a password!
=============================================================================

If you are getting prompted for a password while trying to SSH between
FE nodes there are generally two possible causes. The causes of those
problems and their fixes are shown below (please note you may need to
fix only one of these issues):

-  You may have generated new keys and not added them to the
   authorized_keys file. The fix is to run the following:

::

   cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys

-  You may have inadvertently changed permissions for your ~/.ssh
   directory. The fix is to run the following command:

::

   chmod -R 700 ~/.ssh

**Please note:** It is important to note that the keys generated should
be crated without a passphrase; that is, when you are generating the
keys using "ssh-keygen" please be sure to press <Enter> when prompted
for the passphrase for the key.

You should now be able to access the requested node via SSH without
being prompted for a password.

.. _job_my_multi_node_jobs_fail_on_mpirunmpiexec_please_help:

Job: My multi-node jobs fail on mpirun/mpiexec, please help!
============================================================

If you are able to run some parallel jobs across nodes but not others,
especially if the failure is right after the "mpirun" (or "mpiexec")
command, then the most likely cause of that failure is the stack size
setting. You need to set the stack size to be the appropriate value for
your application. If you're not sure it could set it to "unlimited".
There are some rare instances we have seen problems when set to
"unlimited", but so far most of the time it has been fine. If you're not
able to determine a good number to set to you could try the unlimited
setting.

How you set the stack size depends on what your login shell is,
**independent of the shell that is used for lunch and the job**.

.. _if_your_login_shell_is_cshtcsh:

If your login shell is csh/tcsh:
--------------------------------

Add the following line to your "~/.cshrc" file:

::

   limit stacksize unlimited

.. _if_your_login_shell_is_bash:

If your login shell is bash:
----------------------------

Add the following line to your "~/.bashrc" file:

::

   ulimit -S -s unlimited               # Note &quot;Capital-S&quot; for soft limit

Please also make sure to you have a "~/.bash_profile" file that has the
following (in addition to whatever you have for your own environment):

::

   # Get the aliases and functions
   if [ -f ~/.bashrc ]; then
      . ~/.bashrc
   fi

**Note: Please note that trying to set the stack size within the job
file does not work!** This is because setting it within the job only
changes the setting on the head node for the job, but the remaining
nodes only get the "default" setting or whatever is set in the
initialization files.

.. _job_what_is_the_meaning_of_the_exit_code:

Job: What is the meaning of the exit code?
==========================================

When checking job status with the showq -c or checkjob command, it is
good to know the meaning of the completion code, or the CCODE column for
showq. Here is a list of exit code Moab reported from Torque:

::

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

143 - 128 = 15

To see which signaled the response to what number you can use the
command:

kill -l

Which lists the signals in order. And you will see that 15 is TERM (for
"terminated").

So when a job has a completion code of 143, the job was terminated with
signal 15 (which is the TERM signal), which suggests that the job was
killed by the user or system administrator.

.. _account_how_do_i_access_a_shared_user_account_role_account:

Account: How do I access a shared user account (role account)?
==============================================================

A shared user account (role account) is one that is typically used by a
project when multiple users need to manage some workload. After a role
account is created (via `Help
Request <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wikis/rdhpcs-common-docs/doku.php?id=submitting_help_request>`__),
you can access it using sudo. Example:

::

   # sudo su - $SHAREDUNAME

Where $SHAREDUNAME is the role account name (ex: role.glopara). When it
asks for a password, use your token.

Using X applications can be tricky, but we have created a wrapper script
to help you. To allow for use of X applications while in the shared
account, use the tool **xsudo**. Ex:

::

   # xsudo $SHAREDUNAME

If you are planning to use X utilities with role accounts, you should
use the xsudo utility to switch to the role account and need to
explicitly set the DISPLAY environment variable. So for example, if you
want to use role.rap-chem role account and would like the ability to use
X applications:

-  First note the DISPLAY environment variable setting by doing:

``   ``\ ``echo $DISPLAY``

-  Then use the xsudo command to switch to the role account:

``   ``\ ``xsudo role.rap-chem``

-  Then set the DISPLAY environment variable to the **value you obtained
   above** just before doing xsudo; (please note that the next command
   you use depends on your shell):

``   ``\ ``export DISPLAY=localhost:14.0``

That will enable your X applications to work.
