*******
Common Documentation
*******

This section documents information and procedures common to all REHPCS platforms.

.. note::
    And it will either be a container or one big file; we'll see


Documentation
=============


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
============

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

Singularity
===========

Singularity is a container solution created by necessity for scientific
and application driven workloads. It was originally developed by
Lawrence Berkeley National Laboratory (LBL).

-  `Singularity User Guide <https://singularity.lbl.gov/user-guide>`__

.. _requesting_a_singularity_project:

Requesting a Singularity Project
--------------------------------

Singularity requests are processed through the HPC help desk. Please
submit a ticket to the appropriate `Help
Desk <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests#Submitting_Help_Request_Through_Email>`__
with the following:

-  Project/unix group running the Singularity Container - in order to
   run, container must be readable by group authorized to operate the
   container.
-  Users that will be running Containers
-  Which system(s) they intend to run on
-  What Container they intend to run

The request will then be submitted for approval. Once approved, system
engineers will modify the "limit container group" to allow the
project/unix group to run. Authorized users will then be contacted to
test container configurations. Once it is determined that the container
is operating as expected, additional questions or issues should be
submitted in a completely separate help ticket.

.. _how_to_create_images:

How to Create Images
--------------------

Creating images from Singularity or Docker needs superuser
permissioning. For security reasons, this service is not currently
allowed on NOAA's R&D HPC systems. Users either need to download
available images online or build their own images on other platforms,
and then run them on NOAA's R&D HPC systems. For image building, please
refer to the related documents for Singularity or Docker. Existing
Docker images can be converted to Singularity images and then run on
NOAA's R&D HPC systems.

Please Note: As with any model source code, we expect our users to
download Container images from reputable sources and to fully understand
the contents of the Container prior to running it on R&D HPC systems.

Examples:

.. _where_can_i_download_singularity_containers:

Where Can I download Singularity Containers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Docker and Singularity Hubs have dynamic images. The singularity
images can be downloaded or converted from Docker images outside of
RDHPCS. Singularity build lolcow.simg shub://GodloveD/lolcow

.. _what_can_i_do_if_i_have_a_docker_container:

What Can I do If I have a Docker Container?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can convert it to a Singularity image and then run it on R&D HPC
systems. Currently the Docker Hub is not opened on the R&D HPC systems.
You need to do the conversion externally and then copy the image back to
R&D HPC systems.

``singularity build lolcow.simg docker://godlovedc/lolcow '''``

.. _how_do_i_build_containers:

How do I Build Containers?
~~~~~~~~~~~~~~~~~~~~~~~~~~

On external platforms, ones which you have the root permission. Follow
the documentation for Singularity. For example, given an singularity
recipe to called "Singularity_recipe" to build the image. sudo
singularity build lolcow.simg Singularity_recipe

.. _using_existing_image_files:

Using Existing Image Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have the image files on other machines, you can simply
copy it to the target machine, and use it there. For example, the image
file "loclcow.simg".

.. _how_to_run_single_node_or_single_core_containers:

How to Run Single Node or Single Core Containers
------------------------------------------------

Follow the Singularity documentation. Here is an example to run the
Singularity image hydro.simg.

::

    singularity run hydro.simg -c "echo hello world"

.. _how_to_run_mpi_dependent_containers:

How to Run MPI Dependent Containers
-----------------------------------

The MPI application requires the match of the MPI software between the
Container and target machine. Refer to Singularity documentation for
compatibility. For slurm, you may not need this.

.. _using_container_to_compile_model:

Using Container to Compile Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example to use the hydro.simg, which includes the OS, GNU
compilers, hdf5 and netcdf libraries

| ``singularity exec hydro.simg bash``
| ``$ which mpif90``
| ``/usr/local/bin/mpif90``
| ``## Now you can follow the procedure to configure and compiler WRF model``

.. _using_container_to_run_a_parallel_job:

Using Container to Run a Parallel Job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example to run wrf model with 512 MPI tasks on Jet. The exe
file is not included in the hydro.simg. Under the WRF running directory
on front node of jet,

``sbatch slurm.sh``

The "slurm.sh" will look like:

::


   #!/bin/sh -l
   #SBATCH --job-name=stest
   #SBATCH --ntasks=512
   #SBATCH --tasks-per-node=24
   #SBATCH --time=06:00:00
   #SBATCH --partition=xjet
   #SBATCH --qos batch
   #SBATCH --account=jetmgmt
   #SBATCH --error=cpl.out


   srun singularity exec hydro.simg ./wrf.exe

Note: the hydro.simg and wrf.exe are under the same directory. Under the
running directory, you will not have the soft links from other
directories.

.. _help_and_questions_guidance:

Help and Questions Guidance
===========================

For system related issues, you need to create a user help ticket.
Otherwise, you will need to find an expert for your specific Singularity
image/application.
