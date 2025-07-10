.. _slurm-shpcrpt:

*******
Shpcrpt
*******

The ``shpcrpt`` tool will report a project's FairShare factor and rank,
allocation, and the current month to date (MTD) compute usage information on
all your project(s), detailed project information by user, and summary
information for all projects on the system.

On some RDHPCS system, ``shpcrpt`` is available after loading the ``shpcrpt``
module.

.. tab-set::

  .. tab-item:: Gaea

    .. code-block:: shell

      $ module use /usw/shpcrpt/modulefiles
      $ module load shpcrpt
      $ shpcrpt -M clusterID . . .

  .. tab-item:: Hera, Jet

    .. code-block:: shell

        $ shpcrpt

Use ``shpcrpt --help`` for more details.

Use Cases
=========

Summary Report
--------------

The default usage of `shpcrpt` will print all project usage for the current
month.  Useful to get an overview of all projects on the system.

.. code-block:: shell

   $ shpcrpt -c <cluster>
   =================================================================================================================
   Report                           Summary Report
   Report Run:                      Fri 02 Feb 2024 09:48:57 PM  UTC
   Report Period Beginning:         Thu 01 Feb 2024 12:00:00 AM  UTC
   Report Period Ending:            Fri 01 Mar 2024 12:00:00 AM  UTC
   Percentage of Period Elapsed:    6.6%
   Percentage of Period Remaining:  93.4%
   =================================================================================================================
   Project               NormShares   FairShare        Rank  Allocation   Cr-HrUsed    Windfall   TotalUsed       %Used        Jobs
   -------------------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- ----------- -----------
   proj01                  0.010531    0.501784       64/90     476,712      65,412           0      65,412      13.72%       1,600
   proj02                  0.000000    1.000000       90/90           1           0           0           0       0.00%           0
   proj03                  0.001050    0.920788       35/90      47,520         456           0         456       0.96%      23,469
   proj04                  0.154815    0.619112       46/90   7,008,123     505,651           0     505,651       7.22%      27,067
   .
   .
   .

Project Usage
-------------

To see a specific group's hpc report, specify the project using the `-p`
option:

.. code-block:: shell

   $ shpcrpt -p <project> -c <cluster>
   =================================================================================================================
   Report                           Project Report for:projid
   Report Run:                      Fri 02 Feb 2024 09:50:20 PM  UTC
   Report Period Beginning:         Thu 01 Feb 2024 12:00:00 AM  UTC
   Report Period Ending:            Fri 01 Mar 2024 12:00:00 AM  UTC
   Percentage of Period Elapsed:    6.6%
   Percentage of Period Remaining:  93.4%
   =================================================================================================================
   Machines:                               clusterid
   Initial Allocation in Hours:              493,151
   Net Allocation Adjustments:               -16,439
                                    ----------------
   Adjusted Allocation:                      476,712

   Core Hours Used:                           65,444
   Windfall Core Hours Used:                       0
                                    ----------------
   Total Core Hours Used:                     65,444

   Project Normalized Shares:               0.010531
   Project Fair Share:                      0.501784
   Project Rank:                               64/90

   Percentage of Period Elapsed:                6.6%
   Percentage of Period Remaining:             93.4%
   Percentage of Allocation Used:              13.7%

   User                             Cr-HrUsed    Windfall   TotalUsed       %Used      Jobs
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   Proj.User1                          40,085           0      40,085       8.41%     1,547
   Proj.User2                          25,359           0      25,359       5.32%        53
   ------------------------------ ----------- ----------- ----------- ----------- ---------
   Total                               65,444           0      65,444      13.73%     1,600

   Total Report Runtime: 2.49 seconds (ver. 23.07.06-FNJT)

.. note::

   The ``shpcrpt`` command requires the ``-c <clusterid>`` option.

.. note::

   The ``shpcrpt`` command can take a while to return results as ``shpcrpt``
   pulls data directly from Slurm to generate the reports.
