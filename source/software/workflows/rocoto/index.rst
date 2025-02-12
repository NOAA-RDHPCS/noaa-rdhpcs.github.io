.. _rocoto:

******
Rocoto
******

A Workflow Management System addresses the problems of complexity, scale,
reliability, and reusability by providing two things: A high-level means by
which to describe the various codes that need to be run, along with their
runtime requirements and interdependencies AND an automation engine for
reliably managing the execution of the workflow. Our workflow management
system, Rocoto, works differently than most other workflow management systems.
It is designed to be a self-contained system that runs entirely in the user
space. That is, it is easy for end-users to install, and run without help from
systems administrators.

Rocoto interfaces to the local resource management system. It does not do any
job scheduling itself, it merely submits jobs to the HPC system as task
dependencies allow it. Local policies and users' allocations of HPC resources
are enforced by the local resource management system (e.g. PBS, Torque, MOAB,
SGE, LSF, etc.) so Rocoto has no control over when jobs start to run. Rocoto is
designed to run long range weather pattern workflows; it is not a general
purpose workflow management engine. Rocoto runs one instance of the workflow
for a set of user-defined cycles. A cycle usually corresponds to a model
analysis or initialization time.

Rocoto on RDHPCS Systems
========================

An official release of the latest version is located on Jet and Hera at
:file:`/apps/rocoto` and on gaea at :file:`/ncrc/proj/epic/rocoto`.
Modulefiles are available at :file:`/apps/modules/modulefiles` on hera and jet
and at :file:`/ncrc/proj/epic/rocoto/modulefiles` on gaea.

To add Rocoto to your environment, run the following commands:

.. code-block:: shell

    $ module use <rocoto_module_path>
    $ module load rocoto

where ``<rocoto_module_path>`` is the location of the rocoto modulefiles.

Rocoto Documentation
====================

Rocoto documentation is available on `GitHub
<https://github.com/christopherwharrop/rocoto/wiki/documentation>`_

Rocoto Help
===========

For help using Rocoto, please reach out to the `Rocoto developers
<https://github.com/christopherwharrop/rocoto/>`_.

The RDHPCS technicians can offer some help with system issues that affect
Rocoto.  Please open a :ref:`help request <rdhpcs-workflow-help>`.

When you have problems, one thing that will be very helpful in troubleshooting
is to run rocoto with the ``-v 10`` option to increase the verbosity level.
Below is an example to get more detailed troubleshooting information:

.. cSpell:ignore rocotorun gefs

.. code-block:: shell

    $ rocotorun -v 10 -w gefs.xml -d gefs.db

Please be sure to run with this option before you submit the ticket,
and then point us to the output files and log files.

Need help? Please open Rocoto help tickets to
rdhpcs.rocoto.help@noaa.gov.

Rocoto Best Practices
=====================

To have the best results with Rocoto on the RDHPCS, please do the following:

* Always use the latest Rocoto version
* Always load the Rocoto module (``module load rocoto``) instead than
  specifying a version or using the full path, when running Rocoto in an
  interactive shell
* When using Rocoto in :command:`cron`, it is best to use the full path to the
  executable.  As an example:

  .. code-block:: shell

      */5   *  *   *   *    /apps/rocoto/<version>/bin/rocotorun -w /path/to/gefs.xml -d /path/to/gefs.db
