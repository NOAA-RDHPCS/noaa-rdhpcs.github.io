.. _ppan-user-guide:

###############
PPAN User Guide
###############

.. image:: /images/PPAN.png
   :scale: 75%


Post Processing and Analysis (PPAN) is a small cluster comprised of
over 130 Dell servers located in GFDL in Princeton, NJ. These systems
have over one petabyte of disk storage and access to nearly 200
petabytes of archive storage. Combined with various generations of
Intel processors, from Sandy Bridge to Coffee Lake, each has
specifications that range from 48-512GB of memory and is designed to
provide a system that can meet any user's demand.

PPAN supports GFDL’s science community by providing a place to further
analyze and interpret models generated on other HPC systems. This
gives users a local system to experiment and evaluate with various
degrees of control and validation of complex processes and tasks. PPAN
is also a host to various software packages including MATLAB and other
complex combinations of Python & R libraries.

*************
About Archrpt
*************

| Archprt displays detailed information about archive data usage for
  user and group.

::

   Usage:
           archrpt -r|-s [view] [sort] [date]

           -r show full report
                [view]    group|user
                [sort]    bytes|files
                [date]    YYMMDD
           -s show group summary
                [sort]    bytes|files
                [date]    YYMMDD

   Options:
       -r, --report
               Show full report.

               view|sort|date optins can be used.

       -s, --summary
               Show group summary.

               sort|date options can be used.

       -h, --help
               Display usage.

       -m, --man
               Display man page.

.. _report_option__r:

Report Option [-r]
==================

The report option will output both user and group quota info.

Options:

::

   [view]    group|user
   [sort]    bytes|files
   [date]    YYMMDD

.. _show_archive_report_by_specified_group_view:

Show Archive Report By Specified Group [view]
---------------------------------------------

Command:

::

   archrpt -r o

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   a1f          Ayumi.Fujisaki      o      202,756        3.32T     4.00T/  83.1
   a1g          Anand.Gnanadesi     o      192,901       44.62T    45.00T/  99.2
   ach          Arno.Hammann        o      176,575       36.02T    35.00T/ 102.9
   aja          Alistair.Adcrof     o      293,623       75.68T   121.20T/  62.4
   amb          Agatha.DeBoer       o      110,569       27.36T     5.00T/ 547.2
   anv          Antoine.Venaill     o          160        1.30T     2.00T/  65.2
   avm          Angelique.Melet     o       54,152        7.19T    20.00T/  36.0
   bfk          Baylor.Fox-Kemp     o      200,961       21.02T    20.00T/ 105.1
   bka          Brian.Arbic         o      133,894       15.33T    20.00T/  76.7
   bls          Bonnie.Samuels      o    5,282,350     2463.41T  2626.00T/  93.8
   cbw          Caitlin.Whalen      o           42        0.19T     1.00T/  18.8
   cec          Cara.Cartwright     o            1        0.01T     1.00T/   0.8
   cml          Christopher.Lit     o       55,648        2.12T    10.00T/  21.2
   dng          Daniel.Goldberg     o      905,946        0.94T    10.00T/   9.4
   ecc          Eowyn.Connolly-     o       50,046       14.39T    15.00T/  95.9
   epg          Edwin.Gerber        o       42,614        9.48T     5.00T/ 189.5
   fhx          Fanghua.Xu          o       95,864       36.53T    35.00T/ 104.4
   ......

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   o                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_user_view:

Show Archive Report By Specified User [view]
--------------------------------------------

Command:

::

   archrpt -r rwh

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   rwh          Robert.Hallberg     o      145,105      134.11T   140.00T/  95.8

.. _show_archive_report_by_specified_group_and_sort_by_files_view_sort:

Show Archive Report By Specified Group and Sort By Files [view] [sort]
----------------------------------------------------------------------

Command:

::

   archrpt -r o files

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   bls          Bonnie.Samuels      o    5,282,350     2463.41T  2626.00T/  93.8
   sal          Sonya.Legg          o    1,230,605        9.59T    20.00T/  47.9
   dng          Daniel.Goldberg     o      905,946        0.94T    10.00T/   9.4
   lyo          L.Oey               o      806,168       85.51T    85.00T/ 100.6
   mjh          Matthew.Harriso     o      663,947      315.80T   404.00T/  78.2
   ylc          Yu-Lin.Chang        o      531,806       39.15T    39.00T/ 100.4
   aja          Alistair.Adcrof     o      293,623       75.68T   121.20T/  62.4
   twh          Thomas.Haine        o      275,736       12.87T    13.00T/  99.0
   xil          Xiaohua.Lin         o      268,990        4.01T     4.00T/ 100.3
   sjf          Shejun.Fan          o      268,585        4.49T     5.00T/  89.9
   mh2          Matthew.Harriso     o      246,702       46.94T    47.00T/  99.9
   zns          Zhibin.Sun          o      230,762       42.40T    42.00T/ 100.9
   a1f          Ayumi.Fujisaki      o      202,756        3.32T     4.00T/  83.1
   bfk          Baylor.Fox-Kemp     o      200,961       21.02T    20.00T/ 105.1
   a1g          Anand.Gnanadesi     o      192,901       44.62T    45.00T/  99.2
   xqy          Xunqiang.Yin        o      179,048        6.72T     7.00T/  96.0
   ach          Arno.Hammann        o      176,575       36.02T    35.00T/ 102.9
   jas          Jamie.Shutta        o      175,638        0.16T     1.00T/  16.3
   rwh          Robert.Hallberg     o      145,105      134.11T   140.00T/  95.8
   bka          Brian.Arbic         o      133,894       15.33T    20.00T/  76.7
   ...

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   o                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_group_and_sort_by_bytes_view_sort:

Show Archive Report By Specified Group and Sort By Bytes [view] [sort]
----------------------------------------------------------------------

Command:

::

   archrpt -r o bytes

|
| Output:

::

   Report for date: 120125
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   bls          Bonnie.Samuels      o    5,282,350     2463.41T  2626.00T/  93.8
   mjh          Matthew.Harriso     o      663,947      315.80T   404.00T/  78.2
   rwh          Robert.Hallberg     o      145,105      134.11T   140.00T/  95.8
   lyo          L.Oey               o      806,168       85.51T    85.00T/ 100.6
   smg          Stephen.Griffie     o       97,509       79.45T   121.20T/  65.6
   aja          Alistair.Adcrof     o      293,623       75.68T   121.20T/  62.4
   mh2          Matthew.Harriso     o      246,702       46.94T    47.00T/  99.9
   a1g          Anand.Gnanadesi     o      192,901       44.62T    45.00T/  99.2
   zns          Zhibin.Sun          o      230,762       42.40T    42.00T/ 100.9
   ylc          Yu-Lin.Chang        o      531,806       39.15T    39.00T/ 100.4
   fhx          Fanghua.Xu          o       95,864       36.53T    35.00T/ 104.4
   ach          Arno.Hammann        o      176,575       36.02T    35.00T/ 102.9
   amb          Agatha.DeBoer       o      110,569       27.36T     5.00T/ 547.2
   bfk          Baylor.Fox-Kemp     o      200,961       21.02T    20.00T/ 105.1
   m1i          Mehmet.Ilicak       o       21,373       18.73T    35.00T/  53.5
   hfl          Hung-Fu.Lu          o       46,672       17.86T    18.00T/  99.2
   bka          Brian.Arbic         o      133,894       15.33T    20.00T/  76.7
   m1n          Maxim.Nikurashi     o        2,354       14.79T    20.00T/  74.0
   ecc          Eowyn.Connolly-     o       50,046       14.39T    15.00T/  95.9
   twh          Thomas.Haine        o      275,736       12.87T    13.00T/  99.0
   hls          Harper.Simmons      o       73,279       11.30T    12.00T/  94.1
   ...

   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   o                       13,442,932           3638.06T         4040.00T/  90.1

.. _show_archive_report_by_specified_date_date:

Show Archive Report By Specified Date [date]
--------------------------------------------

Date format: YYMMDD

Command:

::

   archrpt -r 120119

The commands above can also be used with the date option.

| Show Archive Report By Specified Group:
| Command:

::

   archrpt -r o 120119

|
| Show Archive Report By Specified User:
| Command:

::

   archrpt -r rwh 120119

|
| Show Archive Report By Specified Group and Sort By Files:
| Command:

::

   archrpt -r o files 120119

|
| Show Archive Report By Specified Group and Sort By Bytes:
| Command:

::

   archrpt -r o bytes 120119

.. _summary_option__s:

Summary Option [-s]
===================

The summary option will output group quota info.

Options:

::

   [sort]    bytes|files
   [date]    YYMMDD

.. _show_archive_summary:

Show Archive Summary
--------------------

Command:

::

   archrpt -s

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   a                          230,642            112.04T          500.00T/  22.4
   ar5c                     5,084,095           1121.27T         2960.00T/  37.9
   ar5d                     3,950,765            728.82T         1440.00T/  50.6
   ar5e                    13,753,399           4188.16T         2910.00T/ 143.9
   ar5h                        89,772            157.31T          427.50T/  36.8
   b                       16,399,064           4045.93T         4160.00T/  97.3
   c                        4,299,030            831.93T        10712.40T/  87.8
   f                        2,512,648            368.41T          393.20T/  93.7
   g                       41,228,072           8181.26T        10712.40T/  87.8
   i                        1,397,244            390.91T        10712.40T/  87.8
   m                       21,527,461           3066.85T         3420.00T/  89.7
   o                       13,442,932           3638.06T         4040.00T/  90.1
   u                            1,640              0.00T                -/     -
   w                        6,109,695           1785.47T         2550.00T/  70.0


   allocations shared by: c,g,i

   Totals                 130,026,459          28616.42T

.. _show_archive_summary_and_sort_by_files_sort:

Show Archive Summary and Sort By Files [sort]
---------------------------------------------

Command:

::

   archrpt -s files

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   g                       41,228,072           8181.26T        10712.40T/  87.8
   m                       21,527,461           3066.85T         3420.00T/  89.7
   b                       16,399,064           4045.93T         4160.00T/  97.3
   ar5e                    13,753,399           4188.16T         2910.00T/ 143.9
   o                       13,442,932           3638.06T         4040.00T/  90.1
   w                        6,109,695           1785.47T         2550.00T/  70.0
   ar5c                     5,084,095           1121.27T         2960.00T/  37.9
   c                        4,299,030            831.93T        10712.40T/  87.8
   ar5d                     3,950,765            728.82T         1440.00T/  50.6
   f                        2,512,648            368.41T          393.20T/  93.7
   i                        1,397,244            390.91T        10712.40T/  87.8
   a                          230,642            112.04T          500.00T/  22.4
   ar5h                        89,772            157.31T          427.50T/  36.8
   u                            1,640              0.00T                -/     -


   allocations shared by: c,g,i

   Totals                 130,026,459          28616.42T

.. _show_archive_summary_and_sort_by_bytes_sort:

Show Archive Summary and Sort By Bytes [sort]
---------------------------------------------

Command:

::

   archrpt -s bytes

Output:

::

   Report for date: 120125
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   g                       41,228,072           8181.26T        10712.40T/  87.8
   ar5e                    13,753,399           4188.16T         2910.00T/ 143.9
   b                       16,399,064           4045.93T         4160.00T/  97.3
   o                       13,442,932           3638.06T         4040.00T/  90.1
   m                       21,527,461           3066.85T         3420.00T/  89.7
   w                        6,109,695           1785.47T         2550.00T/  70.0
   ar5c                     5,084,095           1121.27T         2960.00T/  37.9
   c                        4,299,030            831.93T        10712.40T/  87.8
   ar5d                     3,950,765            728.82T         1440.00T/  50.6
   i                        1,397,244            390.91T        10712.40T/  87.8
   f                        2,512,648            368.41T          393.20T/  93.7
   ar5h                        89,772            157.31T          427.50T/  36.8
   a                          230,642            112.04T          500.00T/  22.4
   u                            1,640              0.00T                -/     -


   allocations shared by: c,g,i

   Totals                 130,026,459          28616.42T

.. _show_archive_summary_by_date_date:

Show Archive Summary By Date [date]
-----------------------------------

Date format: YYMMDD

Command:

::

   archrpt -s 120119

Output:

::

   Report for date: 120119
   -------------------------------- Group Info ---------------------------------

                                                                        Quota
                                                                    Limit / Used
   Group                  Total Files               Used            Bytes     %
   -----                  -----------             ------            ------------
   a                          230,640            112.03T          500.00T/  22.4
   ar5c                     5,052,329           1119.50T         2960.00T/  37.8
   ar5d                     3,950,765            728.82T         1440.00T/  50.6
   ar5e                    13,739,570           4177.11T         2910.00T/ 143.5
   ar5h                        89,727            157.09T          427.50T/  36.7
   b                       16,396,416           4044.23T         4160.00T/  97.2
   c                        4,299,030            831.93T        10712.40T/  87.6
   f                        2,478,836            359.04T          393.20T/  91.3
   g                       41,151,674           8163.63T        10712.40T/  87.6
   i                        1,396,259            388.78T        10712.40T/  87.6
   m                       21,476,500           3036.43T         3420.00T/  88.8
   o                       14,537,855           3758.37T         4040.00T/  93.0
   u                            1,640              0.00T                -/     -
   w                        6,094,376           1750.66T         2550.00T/  68.7

   allocations shared by: c,g,i

   Totals            130,895,617        28627.62T

The commands above can also be used with the date option.

| Show Archive Summary and Sort By Files:
| Command:

::

   archrpt -s files 120119

| Show Archive Summary and Sort By Bytes:
| Command:

::

   archrpt -s bytes 120119

.. _group_quotas:

Group Quotas
============

Group quotas are provided by the front office.

.. _user_quotas:

User Quotas
===========

Info
----

User quotas have been added to archrpt. These quotas are defined by
the group head and are either a percentage of the group quota or an
absolute size.

Example:

::

   Report for date: 120126
   -------------------------------- User Info ----------------------------------
                                                                        Quota
   User         First.Last      Group  Total Files        Used      Limit / Used
                                                                    Bytes     %
   ----         ----------      -----  -----------       ------     ------------
   a1f          Ayumi.Fujisaki      o      202,756        3.32T     4.00T/  83.1
   a1g          Anand.Gnanadesi     o      192,901       44.62T    45.00T/  99.2
   ach          Arno.Hammann        o      176,575       36.02T    35.00T/ 102.9
   aja          Alistair.Adcrof     o      293,623       75.68T   121.20T/  62.4
   amb          Agatha.DeBoer       o      110,569       27.36T     5.00T/ 547.2
   anv          Antoine.Venaill     o          160        1.30T     2.00T/  65.2
   avm          Angelique.Melet     o       54,261        7.24T    20.00T/  36.2
   bfk          Baylor.Fox-Kemp     o      200,961       21.02T    20.00T/ 105.1
   bka          Brian.Arbic         o      133,894       15.33T    20.00T/  76.7
   bls          Bonnie.Samuels      o    5,295,002     2469.56T  2626.00T/  94.0
   cbw          Caitlin.Whalen      o           42        0.19T     1.00T/  18.8
   cec          Cara.Cartwright     o            1        0.01T     1.00T/   0.8
   ...

Configuration
-------------

User quotas are authorized by the group head and defined in a text
file. Group heads may choose any path name for the file, but once
selected please inform Garrett Power and/or Ed Weiss so that it can be
linked into archrpt. This file is owned by the group head or his
designee, and only the owner should have write access to the file.
Once linked to the archrpt configuration directory, the quota file
owner can adjust users' quotas by editing this file. The format of the
user quota file is as follows:

filename: **x.quota**

::

   gwp Garrett.Power   10%
   rwh Robert.Hallberg 140T
   js  John.Smith  500G
   jd  Jane Doe    2%

In the file, each line is a defined user with the **first column being
the user's initials**, **second column user's First.Last name**, and
**third column the user's quota size**. Each column should be
separated with **tab spacing**. If a user in the group is omitted,
that user has no individual quota limit, but is still restricted by
the group quota.

::

   gwp     = user's user initials.
   Garrett.Power   = user's First.Last name.
   10%     = quota size the user should be allocated of the group quota.
             The quota can be either a percentage or a size of the quota.
             The size can be in the form of Percentage, Gigabytes, Terabytes, or Petabytes.
             10% = 10 percent of the group quota
             500G = 500 Gigabytes
             1T = 1 Terabyte
             1P = 1 Petabyte

Again, this file can be created at any path name in the owner's home
directory. It should be **write only** by the owner and **readable by
everyone** (e.g. **chmod 644**). Then to activate the file and make it
available to archrpt, please provide its path name to Garrett Power
and/or Ed Weiss so it can be linked to the archrpt configuration
directory.

.. _enforcing_quotas:

Enforcing Quotas
================

Group and User quotas are enforced by another script that will check
to see if users are over their quotas. If a group is over its quota,
each user in that group will receive an email stating the group is
over its quota limit. If an individual user is over quota, a warning
email is sent to just that user.


