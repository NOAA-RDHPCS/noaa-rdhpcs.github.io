:orphan:

##############################
Help Ticket System User Portal
##############################

*****
Login
*****

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

*****************
Reply to a Ticket
*****************

In order to reply to a ticket, locate the "Reply" button found at the
end of the most recient ticket thread.

.. image:: /images/help_portal/otrsreply.png

Ticket replies can be expanded and collapsed by using the "Show All Articles"
button, as shown below circled in red.  Select "Submit" to send the ticket to
the RDHPCS Help Desk. Select Submit to send the ticket to the RDHPCS Help Desk.

.. image:: /images/help_portal/showallarticles.png

.. warning::

    Replying to a closed ticket will reopen the ticket.


*******************
Search for a Ticket
*******************

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

*******************
Create a New ticket
*******************

New help tickets can be created by going to :menuselection:`Tickets --> New
Ticket`.  Please only report one issue per help ticket. This will assist us in
routing your tickets to the appropriate resource.

.. image:: /images/help_portal/otrsnewticket.png

.. note:: Ignore the Service and SLA text boxes when creating a new ticket.

Enter a Ticket Type
===================

Please assign the appropriate type to the ticket based on your issue.

Enter a Subject
===============

Enter a subject that gives a clear and concise summary of the issue following
the :ref:`guidelines <good_hd_subject>`.

Enter Detailed Issue Description
================================

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
