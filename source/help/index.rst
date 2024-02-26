.. _getting_help:

############
Getting Help
############

The preferred method for submitting help requests is via email.  Each system
across the RDHPCS has a specific email address to use for requesting help.
Please send help requests to the email address below that corresponds with the
system or function you need help with.  If you have a NOAA email then please
use this address for all of your correspondence.

+------------------+------------------------------+
| System           | Email Address                |
+==================+==============================+
| Jet              | rdhpcs.jet.help@noaa.gov     |
+------------------+------------------------------+
| Hera             | rdhpcs.hera.help@noaa.gov    |
+------------------+------------------------------+
| Niagara          | rdhpcs.niagara.help@noaa.gov |
+------------------+------------------------------+
| Orion / Hercules | rdhpcs.orion.help@noaa.gov   |
+------------------+------------------------------+
| RDHPCS Cloud     | rdhpcs.cloud.help@noaa.gov   |
+------------------+------------------------------+
| HPSS             | rdhpcs.hpss.help@noaa.gov    |
+------------------+------------------------------+
| Gaea / PPAN      | oar.gfdl.help@noaa.gov       |
+------------------+------------------------------+
| AIM / Accounts   | rdhpcs.aim.help@noaa.gov     |
+------------------+------------------------------+

+------------------------------------+-----------------------------+
| Workflow                           | Email Address               |
+====================================+=============================+
| FRE - Flexible Runtime Environment | oar.gfdl.help@noaa.gov      |
+------------------------------------+-----------------------------+
| Rocoto Workflow Manager            | rdhpcs.rocoto.help@noaa.gov |
+------------------------------------+-----------------------------+

The RDHPCS program, along with the RDHPCS integrator manage help requests for
most of the RDHPCS systems:

- Account Management
- Jet
- Hera
- Niagara
- Orion / Hercules
- Cloud (AWS, GCP, Azure)
- HPSS

GFDL manages tickets for Gaea and PPAN.

.. note::
    **Email Communication Policy**

    Per the RDHPCS User Requirements and NOAA Security Policy, all NOAA related
    email communication must be completed utilizing your @noaa.gov email
    address. Please only submit and reply to help tickets from your @noaa.gov
    email address. With the exception of those Orion users who do not have a
    NOAA email address, help requests from other email addresses will not be
    processed until the request is received from @noaa.gov.

.. note::
    **Personal Information (PII)**

    PII is defined as information in a system or online collection that
    directly or indirectly identifies an individual. Per DOC Policy, you should
    never include nor be requested to provide any PII in a help request.

.. note::

    Help tickets are normally addressed by the RDHPCS User Support team from
    0900 - 1700 Eastern Time, Monday - Friday, except Government holidays.

.. _good_hd_requests:

Submitting a Good Help Request
==============================

When you submit a request for help, it is important to give us as much
information about the problem as possible. The more information you provide,
the faster we can diagnose and solve the issue. To help us assist you
efficiently, please include the following information when submitting your help
request:

.. _good_hd_subject:

Use a Good Subject
------------------

Enter a subject that gives a clear and concise summary of the issue, and the
system with the issue.

.. tab-set::

    .. tab-item:: Good Subject Examples

        - Delayed command responses (ex: "ls", "mv") from tfe02 -
          bastion-hera.princeton
        - Downloading data to Jet front-end nodes (fe1) using curl
          hangs/timesout

    .. tab-item:: Bad Subject Example

        Hera slow

.. _good_hd_description:

Provide Detailed Description of the Problem
-------------------------------------------

Include what you did, what didn't work, and why you believe there is a problem.
Specifically, tell us what commands you ran, and what error messages you
received. If this information is short, you can cut and paste it into the
email. If not, please give us paths to files containing this information so
that we can look at it.

.. tab-set::

    .. tab-item:: Good Description Example

        When I tried to log in to Theia from my workstation
        (habanero.fsl.noaa.gov) this morning, about 9:17AM MDT, my ssh command
        hung, and then eventually reported that my connection timed out. See
        below:

        $ ssh -l john.smith bastion-hera.boulder.rdhpcs.noaa.gov
        ssh: connect to host bastion-hera.boulder.rdhpcs.noaa.gov port 22: Connection timed out

    .. tab-item:: Bad Description Example

        I can't log in to Hera


Provide Job Information
-----------------------

Include as much information about the job as possible.  This includes the jobs'
ID, date and time the jobs ran, location of source code, standard out file,
and submitted script.

.. tab-set::

    .. tab-item:: Good Example

        - My WRF job this morning at about 9:24AM MDT crashed with the
          following strange error. The job id was 123456789. Submitted script:
          /path/to/script/wrf.ksh stdout: /path/to/stdout/wrf.out
        - Gaea c4 job 123456789 failed on 2/14/23 at 17:32 EDT.  The stdout
          file /path/to/output/job.log indicates a "bus error".  Source is
          located in /path/to/source.

    .. tab-item:: Bad Example

        Job 123456789 Failed

Describe How to Reproduce the Problem
-------------------------------------

Remember, the technician is likely not an expert on the model, workflow, or
application you are using.  Including step-by-step instructions on how to
reproduce the problem will help identify the issue and resolve the problem.

Also include how to identify the issue.

Only Report One Problem Per Help Ticket
---------------------------------------

Please submit one ticket per issue.  Combining multiple issues in one ticket
may confuse the technician, and will likely lead to a delay in getting all
issues resolved.  Likewise, searching for previous solutions for similar issues
reported in the ticket system is difficult.

Follow up With Additional Information or Questions
--------------------------------------------------

Often problems don't happen just once and may not occur in a repeatable
fashion. If you have additional information that is potentially useful for your
issue, please submit the new information to your **existing help ticket
number**. You can do this by simply replying to the last email sent to you by
the help system (the ticket ID should be in the subject line), or replying to
the ticket in the `customer portal
<https://helpdesk.rdhpcs.noaa.gov/otrs/customer.pl>`_.  For Gaea and PPAN
tickets use the `GFDL customer portal
<https://helpdesk.gfdl.noaa.gov/otrs/customer.pl>`_.

Required Information for Specific Types of Help
===============================================

The information required for a technician to quickly investigate and resolve an
issue differ based on the issue.  Adhering to the following guidelines will
generally be helpful in getting assistance in a timely fashion.

Basic Ticket Information
------------------------

Please include a brief description in the subject line.  Doing so will help us
in directing ticket to the best resource possible.  In the body of the message
please provide a good description of the problem.  In particular, if the
problem is about a job that is failing, it is very helpful to provide the
following:

* Job number
* The location of the script that was used for submitting the job
* Your working directory
* Modules you have loaded (the output of ``module list`` command)
* The command line that was used for submitting the job
* The location of the job output files
* How to identify the problem (e.g., "grep for fortl in the output file")

Ideally, it will be very helpful if you can describe the procedure for
replicating the problem, including the location of the source files, the data
files, the Makefiles, etc.

File System Problems
--------------------

For help with file system problems, please provide the following information:

* The node you are seeing this problem on.
* Your working directory.
* The directory you are trying to list or access files from.
* The actual command that seems to be causing the problem.

Compilation Problems
--------------------

If you are having problems at compile time, generally including the following
will be helpful:

* Your working directory
* Modules you have loaded (output of ``module list``)
* The command you are using to start the compilation process:  "make",
  "compile", or whatever command you are using to compile the program
* Actual cut-and-paste of the command line and the resulting output
* If the output is fairly big, then it is better to capture the output to
  a file and indicate the location of the file.  For example if you typically
  do:

  .. code-block:: shell

      make FC=ifort

  You can do:

  .. code-block:: shell

      make FC=ifort |& tee make.log


Job Submission Problems
-----------------------

If you are receiving an error message when you submit your job, we will need
the following information:

* What is your working directory (output of ``pwd``)
* What modules have been loaded (output of ``module list``)
* What is the command you used to submit the job
* What was response to the command above

A copy-and-paste of your screen session (copy the text on the screen and not a
picture) is preferred.

Job Completion Problems
-----------------------

If you have successfully submitted a job and have questions about it, we will
need at the following information:

* What is the JobID of the job in question
* What is your working directory (output of ``pwd``)
* What modules were loaded at the time of job submission
* What was the command you used to submit the job
* What was response to the command above
* The location of the job stdout/stderr files
* The location of the program output files (which is sometimes different from
  above)

A copy-and-paste of your screen session (copy the text on the screen and not a
picture) is preferred.

Providing a Reproducer
----------------------

There are times when the only way to troubleshoot a problem is to actually for
us to be able to duplicate the problem by running as ourselves.  In those
instance we will ask for a simple reproducer. Ideally a reproducer is a simple
test case that we can experiment with, but we also understand that that may not
always be possible.  In those instances we will need detailed instructions on
what we need to do to duplicate the problem.  At first we will simply want to
be able to run the test case that is failing.  If we need additional debugging
help we may also need a way build your executable from source code. The
instructions below are combining both instances, first about building the code,
and second about running a test case.

Below are general things we will be looking for:

.. rubric:: Building Source

* Which directory to copy
* Which modules need to be loaded
* Any environment variables need to be set before starting the build
* What is the command to start the build process
* Where will the resulting executable be

.. rubric:: Running a Test Case

* What all directories have to be copied
* Which directory should we be in to run the test case
* The location of the job file
* What modules need to be loaded
* Any environment variables need set
* What is the command to submit the job

    * Pointers to some of the things that may need to be changed
    * For example input file may be hardwired with full path and that would
      have to be modified to run from our environment.
    * Some of the scripts may have hardwired paths

* Location of the output files and where we should expect to find the error
  message

One general thing to keep in mind is if you're able to provide us with detailed
instructions on how we can see the problem ourselves that will help us in
troubleshooting the problem and helping you.

Reporting Data Transfer Issues
------------------------------

When you are having problems related to data transfer issues we will need the
following information to assist you:

* What is the full hostname on which you are initiating the transfer?
* What is the full hostname of the destination?
* What is the command you are using to do the transfer (scp, rsync, globus,
  etc.)?
* What is your working directory?
* Please include the command and the response from the system that illustrates
  the problem.

    * If the command does not include the source and destination directories
      please include that information too.

Managing Help Tickets
=====================

Help Tickets can be managed in two ways:

.. tab-set::

    .. tab-item:: Email

        This method is recommended when you have only a few open tickets.
        Reply to the email thread that is started by the OTRS system after you
        submit a help request.  The subject of that email thread starts with
        the assigned ticket number (e.g., [RDHPCS#2018041954000023]), followed
        by the subject in your original email request. DO NOT reply to your
        original email request you sent or it will start a new ticket and add
        confusion to the process.

    .. tab-item:: User Portal

        This method is recommended when you need to manage several open tickets
        and can be used for viewing and relying to open or closed tickets.
        Please refer to the :ref:`user portal documentation
        <help_user_portal>`.


.. _help_user_portal:

Help Ticket System User Portal
==============================

Login
-----

The ticket system allows an alternative access point to view RDHPCS help
tickets. It is recommended to use the portal if you have multiple open help
tickets and/or need to search through old help tickets. Log on to the `RDHPCS
portal <https://helpdesk.rdhpcs.noaa.gov/otrs/customer.pl>`_ NOAA SSO
credentials.  Gaea and PPAN tickets can be accessed using the `GFDL portal
<https://helpdesk.gfdl.noaa.gov/otrs.customer.pl>`_ using the GFDL Active
Directory (AD) password.

.. image:: /images/help_portal/otrswiki.png

.. note::

    RDHPCS users that do not also have an active GFDL account will not be able
    to access Gaea and PPAN tickets.


When you first log in, you'll be on the **Open** ticket tab, with additional
options to see **All** or only **Closed** tickets.

.. image:: /images/help_portal/otrswikiuseroverview.png


Reply to a Ticket
-----------------

In order to reply to a ticket, locate the "Reply" button found at the
end of the most recient ticket thread.

.. image:: /images/help_portal/otrsreply.png

Ticket replies can be expanded and collapsed by using the "Show All Articles"
button, as shown below circled in red.  Select "Submit" to send the ticket to
the RDHPCS Help Desk. Select Submit to send the ticket to the RDHPCS Help Desk.

.. image:: /images/help_portal/showallarticles.png

.. warning::

    Replying to a closed ticket will reopen the ticket.


Search for a Ticket
-------------------

Search for an OTRS ticket by selecting the "Search" option in the
Tickets Menu:

.. image:: /images/help_portal/otrsticketsearch.png

There are multiple options that can be used to search for a ticket.

* RDHPCS Ticket #
* Full Text Search (From, To, CC, etc)
* Attachment names
* Ticket Types
* States
* Time

It is not necessary to use all of these search options at once. The more
information provided, the more refined your ticket search will be.

.. image:: /images/help_portal/otrssearchwindow.png

The search feature also includes an option to save the search as a template,
which allows for quick access to searches that you find yourself repeating.
After building the search, check the "Save search as a template" checkbox.


Create a New Ticket
-------------------

New help tickets can be created by going to :menuselection:`Tickets --> New
Ticket`.  Please only report one issue per help ticket. This will assist us in
routing your tickets to the appropriate resource.

.. image:: /images/help_portal/otrsnewticket.png

.. note:: Ignore the Service and SLA text boxes when creating a new ticket.

**Enter a Ticket Type**
Assign the appropriate type to the ticket based on your issue.

**Enter a Subject**
Use a subject that gives a clear and concise summary of the issue following
the :ref:`guidelines <good_hd_subject>`.

**Enter Detailed Issue Description**
Enter a detailed description of the issue following the :ref:`guidelines
<good_hd_description>`.

- Job number
- Commands used
- Error messages
- The location of the script that was used for submitting the job
- Your working directory
- The command line that was used for submitting the job
- The location of the job output files
- How to identify the problem (“grep for fortl in the output file” for example)

Select Submit to send the ticket to the RDHPCS Help Desk. The ticket can now be
viewed in the Open tickets tab.

.. image:: /images/help_portal/otrsopentickettab.png
