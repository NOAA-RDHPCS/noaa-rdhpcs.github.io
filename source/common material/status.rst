
Current Status
==============
We are now allowing all users and projects to run Singularity Containers
on Hera, Hera-FGE, Jet, and Niagara. Please see below:

Although this change allows users to run Singularity Containers, we are
currently not supporting the following items:

-  RDHPCS Build Environment for creating new Containers
-  Any new RDHPCS services (i.e. Revision Control, Registries, Mirrors,
   Etc.) for supporting Containers

Introduction
---------

A container is a standard unit of software that packages up code and all
its dependencies so the application runs quickly and reliably from one
computing environment to another. Containers are also popular solutions
to run the applications in the cloud environment. The main feature is
the portability. Container images become Containers at run-time.

Background
----------

As both existing and new NOAA projects endeavor to build software tools
and solutions that are portable across many HPC sites and architectures,
it is important that the RDHPCS program be proactive in providing
necessary tools to support these projects. One such solution for
allowing users to accomplish this goal is with the use of Containers.
Through the use of Containers, software developers can build their stack
and create encapsulated run-time environments which may be distributed
to their user base. This greatly minimizes the need for users to have to
worry about software dependencies and user environment.

.. _supported_rdhpcs_container_solutions:

Supported RDHPCS Container Solutions
------------------------------------

Although the leading Container solution across the entire Container
community is Docker, Docker is not a viable solution for High
Performance Computing (HPC) systems. There are security issues
surrounding Docker which make it infeasible for HPC systems. Considering
the possible security issue and capabilities to run the weather model
across the nodes, NOAA's RDHPC systems chose Singularity as a platform
for users to test and run models within Containers. Please refer to
https://sylabs.io/docs/ for more information.

.. _limitation_exception_and_liability:

Limitation, Exception and Liability
-----------------------------------

-  One such exception in regards to software dependencies issues, is
   within HPC where parallel programs require a Message Passing
   Interface (MPI) library for communication across distributed tasks.
   Although there is ongoing work to provide compatibility between
   different MPI solutions, there is still a need to build Containers
   with a matching flavor and in some cases, version of an MPI
   implementation.

-  Building the Container image usually requires root permission, which
   has to be implemented by users on other platforms. NOAA RDHPCS does
   not currently provide this service/permission to our users. Users
   have to create the images outside of RDHPCS and copy them to the R&D
   HPC systems to run with Singularity.

-  **It is user's responsibility to make sure that the images downloaded
   from internet or created by the user will not violate the NOAA RDHPCS
   security policy.**

-  By default, RDHPCS firewall block access to external Container
   repositories. If you would like to request access to an external
   repository, please submit a help ticket.

