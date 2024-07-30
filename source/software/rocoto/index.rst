.. _rocoto:

######
Rocoto
######


A Workflow Management System addresses the problems of complexity,
scale, reliability, and reusability by providing two things: A
high-level means by which to describe the various codes that need to
be run, along with their runtime requirements and interdependencies
AND an automation engine for reliably managing the execution of the
workflow. Our workflow management system, Rocoto, works differently
than most other workflow management systems. It is designed to be a
self-contained system that runs entirely in the user space. That is,
it is easy for end-users to install, and run without help from systems
administrators.

Rocoto interfaces to the local resource management
system. It does not do any job scheduling itself, it merely submits
jobs to the HPC system as task dependencies allow it. Local policies
and users' allocations of HPC resources are enforced by the local
resource management system (e.g. PBS, Torque, MOAB, SGE, LSF, etc.) so
Rocoto has no control over when jobs start to run. Rocoto is designed
to run weather and climate workflows; it is not a general purpose
workflow management engine. Rocoto runs one instance of the workflow
for a set of user-defined &quot;cycles&quot;. A &quot;cycle&quot;
usually corresponds to a model analysis or initialization time.

Jet, Hera, Gaea Rocoto User Requirements
----------------------------------------

An official release of the latest version is located on Jet/Hera at:

.. code-block:: shell

   /apps/rocoto/default

Please use the following command to get the latest version of rocoto:

.. code-block:: shell

   module load rocoto

It has been installed on Gaea at

.. code-block:: shell

   module use /lustre/f1/pdata/ncep_shared/emc.nemspara/soft/modulefiles
   module load rocoto/1.3.0rc4

Workflow modifications may be required for slurm.  If the content of
all <queue> tags in your workflow is one of “batch”, “urgent”,
“windfall”, “novel”, or “debug”, then no modifications to the workflow
XML are required other than changing the workflow scheduler attribute
from “moabtorque” to “slurm”. If some <queue> tags contain other
things (e.g. service, bigmem, fge), then you must also make some
changes for your workflow to function properly with SLURM. Currently,
“service” and “bigmem” can be requested with <queue>. However, with
the way SLURM is configured on Jet/Hera, this will no longer be the
case. Both Hera and Jet will use partitions as well as quality of
service, and some things that used to be a QOS, will now be a
partition. Rocoto 1.3.1 provides a new tag, <partition>, to allow
specification of both at the same time. You will need to modify your
XML to ensure that <queue> and <partition> are specified correctly
when using SLURM.

The following should be requested via <partition> when using SLURM:
service, fge, bigmem, the various Jet partitions (vjet, xjet, etc.),
eslogin, rdtn, ldtn

The following should be requested via <queue> when using SLURM:
windfall, debug, urgent, novel, fgebatch. Please consult Gaea
documentation for list of partitions and QOSes (rocoto thinks of these
as queues). One annoying unavoidable issue is that some configuration
settings (e.g. service and bigmem) for SLURM conflict with the
configuration settings for Moab/Torque. This means that some
combinations of <queue> and <partition> required for SLURM won’t work
for Moab/Torque, so some final workflow XML adjustments may have to
happen at the time of transition. However, they can all be tested in
advance to ensure that the switchover will work as expected.

Rocoto GitHub Documentation
---------------------------

Rocoto documentation is available on `GitHub
<https://github.com/christopherwharrop/rocoto/wiki/documentation>`_

Rocoto Best Practices
---------------------


* **You should always use the latest Rocoto version.**
* For interactive commands and in batch jobs it is best to load the
  module with **module load rocoto**, rather than specifyign a verion.
* When using Rocoto in **cron**, it is best to use the rocoto
  command by specifying full path for the executable, then use
  **default** in the path rather than aa specific version. The correct
  way to use the rocotorun command in a cron entry is shown below:

  .. code-block:: shell

    */5   *  *   *   *    /apps/rocoto/'''default'''/bin/rocotorun -w /path/to/gefs.xml -d /path/to/gefs.db


Rocoto Help
-----------

For additional help and/or questions, please open Rocoto help tickets
to rdhpcs.rocoto.help@noaa.gov

When you have problems, one thing that will be very helpful in
troubleshooting is to run rocoto with the **-v 10** option to increase
the verbosity level. Below is an example to get more detailed
troubleshooting information:

.. code-block:: shell

    /apps/rocoto/default/bin/rocotorun '''-v 10''' -w gefs.xml -d gefs.db

Please be sure to run with this option before you submit the ticket,
and then point us to the output files and log files.

Need help? Please open Rocoto help tickets to
mailto:rdhpcs.rocoto.help@noaa.gov rdhpcs.rocoto.help@noaa.gov.
