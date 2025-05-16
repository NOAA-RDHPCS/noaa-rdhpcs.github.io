.. _rdhpcs-containers:

**********
Containers
**********

.. note:: Current Status

    We now allow all users and projects to run `Singularity
    <https://sylabs.io/singularity/>`_ Containers on Hera,
    Hera-FGE, Jet, and Mercury.

    Although this allows users to run Singularity Containers, we currently do not
    support the following items:

    - RDHPCS Build Environment for creating new Containers
    - Any new RDHPCS services (i.e. Revision Control, Registries, Mirrors,
      Etc.) for supporting Containers

.. _containers-introduction:

Introduction
============

A container is a standard unit of software that packages up code and all its
dependencies so the application runs quickly and reliably from one computing
environment to another. Containers are also popular solutions to run the
applications in the cloud environment. The main feature is the portability.
Container images become Containers at run-time.

.. _containers-background:

Background
----------

As both existing and new NOAA projects endeavor to build software tools and
solutions that are portable across many HPC sites and architectures, it is
important that the RDHPCS program be proactive in providing necessary tools to
support these projects. One such solution for allowing users to accomplish this
goal is with the use of containers. Through the use of containers, software
developers can build their stack and create encapsulated run-time environments
which may be distributed to their user base. This greatly minimizes the need
for users to have to worry about software dependencies and user environment.

.. _containers-supported-rdhpcs-container-solutions:

Supported RDHPCS Container Solutions
------------------------------------

Although the leading Container solution across the entire Container community
is `Docker <https://www.docker.com/>`_, Docker is not a viable solution for
High Performance Computing (HPC) systems. There are security issues surrounding
Docker which make it infeasible for HPC systems. Considering the possible
security issue and capabilities to run the weather model across the nodes,
NOAA's RDHPC systems chose `Singularity`_ as a platform for users to test and
run models within Containers.

.. _containers-limitation-exception-liability:

Limitation, Exception and Liability
-----------------------------------

One such exception in regards to software dependencies issues, is
within HPC where parallel programs require a Message Passing
Interface (MPI) library for communication across distributed tasks.
Although there is ongoing work to provide compatibility between
different MPI solutions, there is still a need to build Containers
with a matching flavor and in some cases, version of an MPI
implementation.

Building the Container image usually requires root permission, which
has to be implemented by users on other platforms. NOAA RDHPCS does
not currently provide this service/permission to our users. Users
have to create the images outside of RDHPCS and copy them to the R&D
HPC systems to run with Singularity.

It is user's responsibility to make sure that the images
downloaded from internet or created by the user will not violate the
NOAA RDHPCS security policy.

By default, RDHPCS firewall block access to external Container
repositories. If you would like to request access to an external
repository, please submit a help ticket.


.. _containers-singularity:

Singularity
===========

Singularity is a container solution created by necessity for scientific and
application driven workloads. It was originally developed by Lawrence Berkeley
National Laboratory (LBL).

Please note that there is a fork in the development of singularity into two
projects, `Apptainer <https://apptainer.org/>`_ and `SingularityCE
<Singularity_>`_. At the present time we are using the singularity-ce solution.

Please refer to the `Singularity documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_ for additional information
than what is presented here.  The `Apptainer documentation
<https://apptainer.org/docs/user/latest/>`_ and `Docker documentation
<https://docs.docker.com/>`_ may provide useful information.

How to create images
--------------------

Creating images from Singularity or Docker needs superuser permissions. For
security reasons, this service is not currently allowed on NOAA's R&D HPC
systems. Users either need to download available images online or build their
own images on other platforms, and then run them on NOAA's R&D HPC systems. For
image building, please refer to the related documents for `Singularity
<Singularity documentation_>`_ or `Docker <Docker documentation_>`_. Existing
Docker images can be converted to Singularity images and then run on NOAA's R&D
HPC systems.

.. note::

    As with any model source code, we expect our users to download container
    images from reputable sources and to fully understand the contents of the
    Container prior to running it on R&D HPC systems.


Download Singularity containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Docker Hub <https://hub.docker.com>`_ and `Singularity Hub
<https://singularityhub.com/>`_ have dynamic images. The singularity images can
be downloaded or converted from Docker images outside of RDHPCS. This can be
done with Singularity using ``singularity build lolcow.simg
shub://GodloveD/lolcow`` where ``lolcow.simg`` is the name of the Singularity
image file, and ``shub://GodloveD/lolcow`` is the Singularity Hub container to
download.


Convert Docker container to Singularity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can convert Docker containers to a Singularity image and then run it on R&D
HPC systems. Currently the `Docker Hub`_ is not opened on the R&D HPC systems.
You need to do the conversion externally and then copy the image back to R&D
HPC systems.

.. code-block:: shell

    $ singularity build lolcow.simg docker://godlovedc/lolcow

Build containers
^^^^^^^^^^^^^^^^

On external platforms, ones which you have the root permission. Follow the
`build documentation for Singularity
<https://docs.sylabs.io/guides/latest/user-guide/build_a_container.html>`__. In
brief, given an singularity recipe file called :file:`Singularity_recipe`, run
the command ``sudo singularity build lolcow.simg Singularity_recipe`` to build
the image.

.. important::

    You must have sudo/root permissions on the system where you build the
    container image.  As mentioned, users are not granted permission to build
    container images on the NOAA R&D HPCS systems.

Use an existing image file
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you already have the image files on other machines, you can simply
copy it to the target machine, and use it there.

Run a Single Node or Single Core Containers
-------------------------------------------

Follow the `Singularity documentation`_. Here is an example to run the
Singularity image :file:`hydro.simg`.

.. code-block:: shell

    $ singularity run hydro.simg echo "hello world"

Run an MPI-dependent container
------------------------------

The MPI application requires the match of the MPI software between the
container and target machine. Refer to `Singularity documentation`_ for
compatibility.

Using a container to compile a model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build a model within a container, the container must have the compiler and
all required libraries and library headers.  An easy way to accomplish this, is
to launch an interactive shell in the container, and build the model as is
typically done on any system.

.. code-block:: shell

    $ singularity exec container_image.simg bash

Using a container to run a parallel job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example Slurm run script to run the wrf model with 512 MPI tasks. In
this example, the :file:`wrf.exe`` file is not included in the
:file:`hydro.simg` image file.  The :file:`wrf.exe` and :file:`hydro.simg`
files are all in the working directory of the run.

.. code-block:: shell

    #!/bin/sh -l
    #SBATCH --job-name=singularity_wrf
    #SBATCH --ntasks=512
    #SBATCH --tasks-per-node=24
    #SBATCH --time=06:00:00
    #SBATCH --partition=mypartition
    #SBATCH --qos batch
    #SBATCH --account=myaccount
    #SBATCH --error=singularity_wrf.out


    srun singularity exec hydro.simg ./wrf.exe

.. note::

    The :file:`hydro.simg` and :file:`wrf.exe` are under the same directory.
    Under the running directory, you will not have the soft links from other
    directories.

Container help, questions, and guidance

The R&D HPCS system administrators and help staff have very little knowledge on
using containers on HPC systems.  Open a :ref:`help request <getting_help>` to
what help can be offered.  However, you will likely find your fellow scientists
and the greater container communities have better knowledge for your specific
Singularity image/application.
