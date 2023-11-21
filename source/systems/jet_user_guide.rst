.. _jet-user-guide:

**************
Jet User Guide
**************

.. rubric:: Jet System Information

The Jet system includes several partitions that have been
installed over time. Currently Jet consists of six compute
partitions, plus four bigmem nodes, totaling 57,744 coes, @
1.884 PF.

+-------+-------+-------+-------+-------+-------+-------+-------+
| Part  | tJet  | uJet  | sJet  | vJet  | x     | b     | kJet  |
| ition |       |       |       |       | Jet\* | igmem |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Year  | 2010  | 2011  | 2012  | 2014  | 2015  | 2015  | 2018  |
|       |       |       |       |       | /2016 |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | Intel | Intel | Intel | Intel | Intel | Intel | Intel |
| Type  | Wes   | Wes   | S     | IvyB  | Ha    | Ha    | Sk    |
|       | tmere | tmere | andyB | ridge | swell | swell | ylake |
|       |       |       | ridge |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | X5650 | X5650 | X5    | E5-2  | E5-2  | E5-2  | 6148  |
| Model |       |       | -2670 | 650v2 | 670v3 | 670v3 |       |
| #     |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | 2.66  | 2.66  | 2.6   | 2.6   | 2.3   | 2.3   | 2.4   |
| Speed | GHz   | GHz   | GHz   | GHz   | GHz   | GHz   | GHz   |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 758   | 238   | 330   | 288   | 812   | 4     | 404   |
| Nodes |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 9096  | 2856  | 5120  | 4608  | 19488 | 96    | 14400 |
| Cores |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Cores | 12    | 12    | 16    | 16    | 24    | 24    | 40    |
| /node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| M     | 2 GB  | 2 GB  | 2GB   | 4 GB  | 2.66  | 10.6  | 2.4   |
| emory |       |       |       |       | GB    | GB    | GB    |
| /Core |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| M     | 24 GB | 24 GB | 32 GB | 64 GB | 64 GB | 256   | 96 GB |
| emory |       |       |       |       |       | GB    |       |
| /Node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Avai  | 21 GB | 21 GB | 29 GB | 61 GB | 61 GB | 253   | 93 GB |
| lable |       |       |       |       |       | GB    |       |
| Mem/N |       |       |       |       |       |       |       |
| ode\* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Peak  | 127.7 | 127.7 | 332.8 | 332.8 | 883   | 883   | 2048  |
| Flops | GF    | GF    | GF    | GF    | GF    | GF    | GF    |
| /node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Rel   | 1.00  | 1.00  | 1.44  | 1.65  | 1.5   | 1.5   | 1.68  |
| ative |       |       |       |       |       |       |       |
| Perf  |       |       |       |       |       |       |       |
| /Core |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| In    | QDR   | QDR   | QDR   | FDR   | FDR   | FDR   | EDR   |
| terco | Infin | Infin | Infin | Infin | Infin | Infin | Infin |
| nnect | iband | iband | iband | iband | iband | iband | iband |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 96.8  | 30.4  | 113.2 | 93.6  | 717.4 | 3.5   | 827   |
| Fl    | TF    | TF    | TF    | TF    | TF    | TF    | TF    |
| ops\* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+

.. Note::
Notes:

-  Jet's Front Ends (service partition) are of the same
   architecture as the xJet compute nodes.
-  Total flops is a theoretical peak and does not represent
   actual performance.
-  Relative performance is based on SPEC CPU 2017
   (specifically SPECrate 2017 Floating Point) benchmark. It
   is normalized by the slowest core in production.
-  Available Memory/Node is the total memory available to
   application. The difference between this value and the
   total available memory is due to OS overhead and other
   system buffers.

System Features:

-  Total of 55,984 cores of 64-bit Intel CPU’s,
-  Capability of 1,795 trillion floating point operations
   per second – or 1.79 petaflops,
-  Total scratch disk capacity of 6.6 Petabytes

.. rubric:: File Systems

==== ====== =======
name type   size
lfs1 Lustre 3540 TB
lfs4 Lustre 4500 TB
==== ====== =======

.. rubric:: NOAA Boulder RDHPCS History

For decades, NOAA weather research has relied on High Performance
Computing to further its mission of developing
leading edge weather observation and prediction
capabilities. This has been accomplished both the
development of leading edge software as well as the adoption
of cutting edge hardware technologies to push forward the
envelope of what is computationally feasible.

.. rubric:: Intel Paragon
 
Intel Paragon was an early parallel system, delivered in
1991 and was used for the development of a parallel RUC
model. Researchers at GSL also developed the Scalable
Modeling System (SMS) to assist in the parallelization of
codes. To further development of parallel programming
standards GSL staff members participated in the development
of the MPI-1 and MPI-2 standards, which provided a common
basis for the parallel computational methods used today.

.. rubric:: Jet

In 2000, GSL took delivery of an HPC system relying on a
relatively new concept, clustering. Very similar to a
Beowulf cluster, the system used off the shelf desktop
servers with Myrinet a high-speed, low-latency network
interconnect. This system provided substantially more
performance that the traditional architectures available at
the time in a much more cost effective manner.

Now Jet refers to any of the clustered systems that have
passed through GSL since 2000 and are used to support NOAA
Research and Development High Performance Computing (RDHPC)
requirements for GSL and other NOAA offices, including the
Hurricane Forecast Improvement Project (HFIP) since 2009. A
history of those systems:

+----------+----------+----------+-------+-------+--------+----------+
| System   | Date     | P        | Nodes | Cores | Gflops | I        |
|          |          | rocessor |       |       |        | ntegrato |
|          |          |          |       |       |        | r/Vendor |
+----------+----------+----------+-------+-------+--------+----------+
| Jet      | Jan 2000 | Compaq   | 276   | 276   | 368    | High     |
|          |          | Alpha    |       |       |        | Per      |
|          |          | 21264,   |       |       |        | formance |
|          |          | 667Mhz   |       |       |        | Tech     |
|          |          |          |       |       |        | nologies |
|          |          |          |       |       |        | Inc.     |
|          |          |          |       |       |        | (HPTi    |
|          |          |          |       |       |        | )/Compaq |
+----------+----------+----------+-------+-------+--------+----------+
| aJet     | Aug 2001 | Alpha    | 276   | 284   | 473    | HP       |
|          |          | P        |       |       |        | Ti/Alpha |
|          |          | rocessor |       |       |        | P        |
|          |          | Inc.     |       |       |        | rocessor |
|          |          | 21264,   |       |       |        | Inco     |
|          |          | 833Mhz   |       |       |        | rporated |
+----------+----------+----------+-------+-------+--------+----------+
| iJet     | Aug 2002 | Intel    | 276   | 1536  | 6758   | HP       |
|          |          | Pentium  |       |       |        | Ti/Aspen |
|          |          | 4,       |       |       |        | Systems  |
|          |          | 2.2Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| eJet     | Aug 2004 | Intel    | 276   | 598   | 3827   | HP       |
|          |          | Nocona,  |       |       |        | Ti/Aspen |
|          |          | 3.2Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| wJet     | Jan 2006 | Intel    | 276   | 1440  | 15321  | R        |
|          |          | Wo       |       |       |        | aytheon/ |
|          |          | odcrest, |       |       |        | Rackable |
|          |          | 2.66Ghz  |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| hJet     | Aug 2008 | Intel    | 276   | 2016  | 23244  | Raythe   |
|          |          | Har      |       |       |        | on/Aspen |
|          |          | pertown, |       |       |        | Systems  |
|          |          | 2.8Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| nJet     | Aug 2009 | Intel    | 448   | 3584  | 40140  | Raythe   |
|          |          | Nehalem, |       |       |        | on/Aspen |
|          |          | 2.8Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| tJet     | Aug 2010 | Intel    | 844   | 10128 | 107762 | Raythe   |
|          |          | W        |       |       |        | on/Aspen |
|          |          | estmere, |       |       |        | Systems  |
|          |          | 2.66Ghz  |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| uJet     | Aug 2011 | Intel    | 504   | 6048  | 64351  | Computer |
|          |          | W        |       |       |        | Sciences |
|          |          | estmere, |       |       |        | Cor      |
|          |          | 2.66Ghz  |       |       |        | poration |
|          |          |          |       |       |        | (CS      |
|          |          |          |       |       |        | C)/Aspen |
|          |          |          |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| sJet     | Aug 2012 | Intel    | 340   | 5440  | 113152 | C        |
|          |          | Sandy    |       |       |        | SC/Appro |
|          |          | Bridge,  |       |       |        |          |
|          |          | 2.6Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| vJet     | Aug 2014 | Intel    | 288   | 4680  | 97344  | C        |
|          |          | Ivy      |       |       |        | SC/Aspen |
|          |          | Bridge,  |       |       |        | Systems  |
|          |          | 2.6Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| xJet     | Aug 2015 | Intel    | 336   | 8064  | 296755 | C        |
|          |          | Haswell, |       |       |        | SC/Aspen |
|          |          | 2.3Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| xJet     | Aug 2016 | Intel    | 480   | 11520 | 423936 | CSRA     |
| E        |          | Haswell, |       |       |        | /Silicon |
| xpansion |          | 2.3Ghz   |       |       |        | M        |
|          |          |          |       |       |        | echanics |
+----------+----------+----------+-------+-------+--------+----------+
| kJet     | Feb 2019 | Intel    | 360   | 14400 | 754688 | CS       |
|          |          | Skylake, |       |       |        | RA/Aspen |
|          |          | 2.4Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| kJet exp | Dec 2019 | Intel    | 44    | 1760  | 92240  | CS       |
|          |          | Skylake, |       |       |        | RA/Aspen |
|          |          | 2.4Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+

.. rubric:: GPU Clusters

As GSL was researching and experimenting with clustered HPC
systems in the late 1990s which drove adoption of clustered
systems in 2000, GSL is continuing to research potentially
disruptive, next generation HPC technologies. Graphical
Processing Units, GPUs, are traditionally used for graphics
and video gaming, but their design is applicable to
numerical modelling as well. Since their architecture is <br>
fundamentally different from traditional CPUs, existing
software usually does not run without modification.

At GSL, we have been using GPU clusters since 2009 and are
developing new tools and techniques that will allow these
systems to be used in the future by scientists to solve
tomorrow's weather and hurricane prediction challenges.

Using Modules
==========
.. container:: noprint
   :name: mw-page-base

.. container:: noprint
   :name: mw-head-base

.. container:: mw-body
   :name: content

   .. container::
      :name: siteNotice

   .. container:: mw-indicators

   .. rubric:: Using Modules
      :name: firstHeading
      :class: firstHeading mw-first-heading

   .. container:: vector-body
      :name: bodyContent

      .. container:: noprint
         :name: siteSub

         From jetdocs

      .. container::
         :name: contentSub

         .. container::
            :name: mw-content-subtitle

      .. container::
         :name: contentSub2

      .. container::
         :name: jump-to-nav

      `Jump to navigation <#mw-head>`__ `Jump to
      search <#searchInput>`__

      .. container:: mw-body-content mw-content-ltr
         :name: mw-content-text

         .. container:: mw-parser-output

            .. rubric:: About
               Modules[\ `edit </index.php?title=Using_Modules&action=edit&section=1>`__\ ]
               :name: about-modulesedit

            Modules is a tool that is used to manage the use of software
            when multiple versions are installed. For packages that are
            not provided with the OS (compilers, debuggers, MPI stacks,
            etc), we install so that new versions to not overwrite old
            versions.

            By default, no modules are loaded. Therefore you must load
            any modules that you wish to use. To see what modules are
            available, run:

            ::

               # module avail

            At a minimum you will want to load a compiler and an MPI
            stack:

            ::

               # module load intel
               # module load mvapich2

            Note: Since you have to do this explicitly (for now), you
            also have to do it in your job scripts. Or, you can put it
            in your .profile and make it permanent.

            .. rubric:: Modules on
               Jet[\ `edit </index.php?title=Using_Modules&action=edit&section=2>`__\ ]
               :name: modules-on-jetedit

            The way to find the latest modules on Jet is to run module
            avail:

            ::

               # module aval

               --------------------------------------------------------------------------------------------------------- /apps/Modules/versions ----------------------------------------------------------------------------------------------------------
               3.2.9

               ----------------------------------------------------------------------------------------------------- /apps/Modules/3.2.9/modulefiles -----------------------------------------------------------------------------------------------------
               bbcp/12.01.30.01.0(default)    grads/2.0.1(default)           intel/12.1.4(default)          modules                        pgi/12.5-0(default)            udunits/1.12.11
               cnvgrib/1.2.3(default)         hpss                           intel/12.1.5                   ncl/6.0.0                      rocoto/1.0.2                   udunits/2.1.24(default)
               cuda/4.2.9(default)            idl/8.2(default)               lahey/8.10b(default)           nco/4.1.0                      rocoto/1.0.3(default)          use.own
               dot                            imagemagick/6.2.8(default)     module-cvs                     ncview/2.1.1(default)          szip/2.1                       wgrib/1.8.1.0b(default)
               gempak/6.7.0-gfortran(default) intel/11.1.080                 module-info                    null                           totalview/8.9.2-2(default)     wgrib2/0.1.9.6a(default)

               ---------------------------------------------------------------------------------------------------- /apps/Modules/default/admintools -----------------------------------------------------------------------------------------------------
               cit   devel

            In the above, each module name represents a different
            package. In cases where there are multiple versions of a
            package, one will be set as a default. For example, for the
            intel compiler there are multiple choices:

            ::

               intel/11.1.080
                intel/12-12.1.4(default)
                intel/12-12.1.5

            So if you run:

            ::

               # module load intel

            Then default version will be loaded, in this case 12-12.1.4

            If you want to load a specific version, you can. We highly
            recommend you use the system defaults unless something is
            not working or you need a different feature. To load a
            specific version, specify the version number.

            ::

               # module load intel/11.1.080
                # module list
               Currently Loaded Modulefiles:
                1) intel/11.1.080

            If you already have a particular module loaded and you want
            to switch to a different version of the same module, you can
            either do

            ::

               # module unload intel
               # module load intel/11.1.080

            or

            ::

               # module switch intel intel/11.1.080

            Notes:

            -  When unloading modules, only unload those that you have
               loaded. The others are done automatically from master
               modules.
            -  Modules is a work in progress, and we will be improving
               their uses and making which modules you load more clear.

         .. container:: printfooter

            Retrieved from
            "http://localhost:8180/index.php?title=Using_Modules&oldid=521"

      .. container:: catlinks catlinks-allhidden
         :name: catlinks

.. container::
   :name: mw-navigation

   .. rubric:: Navigation menu
      :name: navigation-menu

   .. container::
      :name: mw-head

      .. rubric:: Personal tools
         :name: p-personal-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  Not logged in
         -  `Talk </index.php/Special:MyTalk>`__
         -  `Contributions </index.php/Special:MyContributions>`__
         -  `Create
            account </index.php?title=Special:CreateAccount&returnto=Using+Modules>`__
         -  `Log
            in </index.php?title=Special:UserLogin&returnto=Using+Modules>`__

      .. container::
         :name: left-navigation

         .. rubric:: Namespaces
            :name: p-namespaces-label
            :class: vector-menu-heading

         .. container:: vector-menu-content

            -  `Page </index.php/Using_Modules>`__
            -  `Discussion </index.php?title=Talk:Using_Modules&action=edit&redlink=1>`__

         English

         .. container:: vector-menu-content

      .. container::
         :name: right-navigation

         .. rubric:: Views
            :name: p-views-label
            :class: vector-menu-heading

         .. container:: vector-menu-content

            -  `Read </index.php/Using_Modules>`__
            -  `Edit </index.php?title=Using_Modules&action=edit>`__
            -  `View
               history </index.php?title=Using_Modules&action=history>`__

         More

         .. container:: vector-menu-content

         .. container::
         vector-search-box-vue vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box
            :name: p-search

            .. container::

               .. container:: vector-search-box-inner
                  :name: simpleSearch

   .. container:: vector-legacy-sidebar
      :name: mw-panel

      .. container::
         :name: p-logo

         ` </index.php/Start>`__

      .. rubric:: Navigation
         :name: p-navigation-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Start </index.php/Start>`__

      .. rubric:: Quick Links
         :name: p-Quick_Links-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Running
            Jobs <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Running_and_Monitoring_Jobs_on_Jet_and_Hera(Theia)_-_SLURM>`__
         -  `Project
            Information <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_Information_About_Your_Projects_-_SLURM>`__
         -  `System
            Overview <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Jet_System_Overview>`__
         -  `Project Data
            Management <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Project_Data_Management>`__

      .. rubric:: Submitting a Help Request
         :name: p-Submitting_a_Help_Request-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Help
            Requests <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__

      .. rubric:: Accessing RDHPCS Systems
         :name: p-Accessing_RDHPCS_Systems-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Logging
            In <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Logging_in>`__
         -  `Using
            X2Go <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/X2go>`__

      .. rubric:: Account Management
         :name: p-Account_Management-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Getting An RDHPCS
            Account <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Getting_an_RDHPCS_Account>`__
         -  `Role
            Accounts <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Role_Accounts>`__

      .. rubric:: Policies and Best Practices
         :name: p-Policies_and_Best_Practices-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Cron Usage
            Policy <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Cron_Usage_Policy>`__
         -  `Project Data
            Management <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Project_Data_Management>`__
         -  `Projecting Restricted
            Data <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Protecting_Restricted_Data>`__
         -  `Managing Packages in
            /contrib <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Managing_Packages_in_/contribManaging_Packages_in_/contrib>`__

      .. rubric:: FAQs and Known Issues
         :name: p-FAQs_and_Known_Issues-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `FAQs <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/FAQs_-_Frequently_Asked_Questions>`__

      .. rubric:: Applications
         :name: p-Applications-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `Compiling
            Applications <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Compiling_Applications>`__
         -  `Starting a Parallel
            Application <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Starting_a_Parallel_Application>`__
         -  `Profiling
            Applications <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Profiling_Applications>`__
         -  `Debugging a Parallel
            Application <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Debugging_a_Parallel_Application>`__

      .. rubric:: Tools
         :name: p-tb-label
         :class: vector-menu-heading

      .. container:: vector-menu-content

         -  `What links
            here </index.php/Special:WhatLinksHere/Using_Modules>`__
         -  `Related
            changes </index.php/Special:RecentChangesLinked/Using_Modules>`__
         -  `Special pages </index.php/Special:SpecialPages>`__
         -  `Printable version <javascript:print();>`__
         -  `Permanent
            link </index.php?title=Using_Modules&oldid=521>`__
         -  `Page
            information </index.php?title=Using_Modules&action=info>`__



Using Math Libraries
================

Software
========

Shell & Programming Environments
================================

Compiling
=========

Running Jobs
============

Debugging
=========

Optimizing and Profiling
========================

Known Issues
============
