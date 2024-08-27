
.. _role_accounts:

Role Accounts
=============

A role account is a user account shared with one or more users as
members, such that all group members share the account equally via the
use of `sudo`, typically for the unified use of a project. Role
accounts must have a name that reflects their project association or
function. All changes to a role account must be submitted by the role
account Principal Investigator (PI) via OTRS ticket. Send email to
rdhpcs.aim.help@noaa.gov with the subject line: Role account changes -
first.last (role account name).

Accessing a Role Account
------------------------

You can access any role account if you are a member of the account.
Use sudo with your RSA token to gain access. For example:

 .. code-block:: shell

   jsmith# sudo su - roleuser
   Access is via First.Last username only. Enter RSA PASSCODE:
   bash-4.1$ whoami
   roleuser

Your RSA passcode is your PIN+Token code.

X Applications With Role Accounts
---------------------------------

If you are planning to use X utilities with role accounts, you should
use the xsudo utility to switch to the role account instead of using
the "sudo" command directly. You need to explicitly set the DISPLAY
environment variable after doing the xsudo to the role account. So for
example, if you want to use role.rap-chem role account and would like
the ability to use X applications:

1. Note the ``DISPLAY`` environment variable in your current session
   before doing the xsudo to the role account:

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

Using CRON
----------

Since Role accounts are  shared by multiple users in a project, the
project members need a way to know which member is responsible for
which section of the cron entries. The person responsible for the
section of a cron entry of a role account should use the following
guidelines:

At the beginning of the section:

- Add a comment about the who is adding these cron entries
- Add a comment about when this entry was added
- Add a comment about an end date if applicable
- Add other comments as needed to document the purpose
- Add a ``MAILTO=First.Last@noaa.gov`` at the beginning of the section
- Add a ``MAILTO=`` at the end of the section so that whoever is
  responsible for the next section sets their own MAILTO filed.

.. note::

   Without the ``MAILTO`` directive, any errors/logs from the cron
   commands end up getting lost and one may never know there was a
   problem/failure!



