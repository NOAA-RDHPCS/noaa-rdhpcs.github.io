.. _slurm-sreport:

#######
Sreport
#######

Sreport is used to generate reports of cluster utilization for jobs saved to
the Slurm database. Sreport has the ability to provide CPU hours and job count
for a given user and, or project. As of now, sreport does not provide a qos
option for reports.

Sreport can display the following:

- Total core-hours used per user
- Total core-hours used per project
- Number of jobs ran per user
- Number of jobs ran per project

See ``man sreport`` for more details.


Use Cases
=========

.. note::

    The default time format for reporting CPU usage is minutes.  Use the ``-t
    Hours`` option to specify CPU Hours. The ``Used`` column is the number of
    CPU Minutes consumed over the period.

Usage Report for Specific Users
-------------------------------

.. code-block:: shell

    $ sreport cluster UserUtilizationByAccount -M <cluster> -t Hours Users=<user>

Usage Report for Account Utilization by User
--------------------------------------------

.. code-block:: shell

    $ sreport cluster AccountUtilizationByUser -M <cluster> -t Hours account=<account>

Usage Report for All Users
--------------------------

.. code-block:: shell

    $ sreport cluster AccountUtilizationByUser -t Hours -M <cluster> Start=<YYYY-MM-DD>

Report Number of Jobs by a User
-------------------------------

.. code-block:: shell

    $ sreport job sizes PrintJobCount -M <cluster> Users=<user> account=<account>

Report Top Usage
----------------

.. code-block:: shell

    $ sreport user TopUsage -M <cluster>


Report Descriptions and Formats
===============================

:cluster AccountUtilizationByUser: This report will display account utilization
    as it appears on the hierarchical tree. Starting with the root account by
    default this report will list the underlying usage with a sum on each
    level.
:cluster UserUtilizationByAccount: This report will display users by account in
    order of utilization without grouping multiple account by user into one,
    but displaying them on separate lines.
:cluster UserUtilizationByWCKey: This report will display users by wckey in
    order of utilization without grouping multiple wckey by user into one, but
    displaying them on separate lines.
:job SizesByAccount: This report will display the amount of time used for job
    ranges specified by the 'grouping=' option. Only a single level in the tree
    is displayed defaulting to the root dir. If you specify other accounts with
    the 'account=' option sreport will use those accounts as the root account
    and you will receive the aggregated totals of each listed account plus
    their sub accounts.
:user TopUsage: Displays the top users on a cluster, i.e. users with the
    highest usage. By default users are sorted by CPUTime, but the -T, --tres
    option will sort users by the first TRES specified. Use the group option to
    group accounts together.


Format Options for Cluster Reports
----------------------------------

AccountUtilizationByUser
    Accounts, Cluster, Login, Proper, TresCount, Used

UserUtilizationByAccount
    Accounts, Cluster, Login, Proper, TresCount, Used

UserUtilizationByWckey
    Cluster, Login, Proper, TresCount, Used, Wckey


Format Options for Job Reports
------------------------------

SizesByAccount
    Account, Cluster

SizesByAccountAndWckey
    Account, Cluster

SizesByWckey
    Wckey, Cluster


Time Formats
============

Use ``Start=<>`` and ``End=<>`` to collect usage from a specific period.

The default for ``Start`` is 00:00:00 of previous day. The default for ``End``
is  23:59:59 of previous day.

- Valid Formats:

  - HH:MM[:SS] [AM|PM]
  - MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
  - MM/DD[/YY]-HH:MM[:SS]
  - YYYY-MM-DD[THH:MM[:SS]]


Example:

Display CPU usage for August 2023 for account <account> on cluster <cluster>

.. code-block:: shell

    $ sreport cluster AccountUtilizationByUser -M <cluster> -t Hours account=<account> Start=2023-08-01 End=2023-08-31


References
==========

* `Slurm Sreport Documentation <sreport>`_

.. _`sreport`: https://slurm.schedmd.com/sreport.html
