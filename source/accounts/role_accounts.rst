.. _role_accounts:

Role Accounts
=============

A role account is a user account shared with one or more users as
members, such that all group members share the account equally via the
use of ``sudo``, typically for the unified use of a project. Role
accounts must have a name that reflects their project association or
function.


Requesting a new role account
------------------------------------

All requests for a new role account must be submitted as helpdesk tickets.
Send email to rdhpcs.aim.help@noaa.gov with the subject line:
**Role account request**.  Include:

#. the proposed account name and generic description of purpose.
#. an active project where role account is a member.
#. the PI for the role account. Reference existing role accounts as
   appropriate.

Requesting changes to a role account
------------------------------------

All changes to a role account must be submitted via the helpdesk.
Send email to rdhpcs.aim.help@noaa.gov with the subject line: **Role
account changes - Role.Account.Name.Here.** All changes require PI
approval.


Accessing a role account from your user account
-----------------------------------------------

If you are a member of a role account, you can access the account by running
the command ``sudo su - <ROLE_ACCOUNT>``.
Use ``sudo -l`` to list the access you have.

You will authenticate with your Yubikey to gain access. For example:

 .. code-block:: shell

   jsmith# sudo su - role.user
   [sudo] password for First.Last:
   bash-4.1$ whoami
   role.user

Accessing a role account for Data Transfers or Bastion SSH Login
----------------------------------------------------------------

Access to log in **as the role account directly** for (Globus) data
transfers, or SSH login access, can be assigned to members of a role
account.  They will use their RDHPCS registered Yubikey when prompted
to authenticate.  Request this assignment via the helpdesk; send email
to rdhpcs.aim.help@noaa.gov with the subject line: **Role account
changes - Role.Account.Name.Here - Assign login access to First.Last**
All changes require PI approval.


X Applications With role accounts
---------------------------------

.. note::

   X applications with role accounts are not supported on Pan or Gaea.

Before continuing, make sure you can use X applications with your
regular user account.

If you are planning to use X applications with role accounts, you
should use the ``xsudo`` utility to switch to the role account instead
of using the ``sudo`` command directly. You need to explicitly set the
DISPLAY environment variable after doing the ``xsudo`` to the role
account. For example, if you want to use ``role.rap-chem`` role
account and would like the ability to use X applications:

1. Note the ``DISPLAY`` environment variable in your current session
   before doing the ``xsudo`` to the role account:

.. code-block:: shell

   $ echo $DISPLAY

2. Use the ``xsudo`` command to switch to the role account:

.. code-block:: shell

   $ xsudo role.rap-chem

3. Set the ``DISPLAY`` environment variable to the value you obtained
   above just before doing ``xsudo``.

   .. tab-set::

      .. tab-item:: bash

         .. code-block:: shell

            $ export DISPLAY=localhost:14.0

      .. tab-item:: csh

         .. code-block:: shell

            $ setenv DISPLAY localhost:14.0

This will enable your X applications.

Using CRON or SCRON
-------------------

As role accounts are shared by multiple users in a project, the
project members need a way to know which member is responsible for
which section of the cron entries. The person responsible for the
section of a cron or scron entry of a role account should use the
following guidelines:

At the beginning of the section:

- Add a comment about the who is adding these cron entries
- Add a comment about when this entry was added
- Add a comment about an end date if applicable
- Add other comments as needed to document the purpose
- Add a ``MAILTO=First.Last@noaa.gov`` at the beginning of the section
- Add a ``MAILTO=`` at the end of the section so that whoever is
  responsible for the next section sets their own MAILTO filed.

.. note::

   Without the ``MAILTO`` directive, any errors/logs from the cron or
   scron commands end up getting lost and one may never know there was
   a problem/failure!
