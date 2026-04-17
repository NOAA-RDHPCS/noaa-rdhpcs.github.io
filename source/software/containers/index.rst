.. meta::
   :description: Guide to running Singularity containers on RDHPCS systems
    including Ursa, Gaea, Hera, MSU-HPC systems (Orion and Hercules),
    Mercury, and NOAA Cloud providers via ParallelWorks (AWS and Azure)
    for portable and reproducible software environments.
   :keywords: Singularity, containers, Docker, Apptainer, container images,
    portability, HPC, Ursa, Gaea, Hera, Orion, Hercules, NOAA Cloud, Mercury

.. _rdhpcs-containers:

**********
Containers
**********

.. note:: Current Status

    We now allow all users and projects to run `Singularity
    <https://en.wikipedia.org/wiki/Singularity_(software)>`_ containers on Ursa, Gaea,
    Hera, MSU-HPC (Orion and Hercules), Mercury, and NOAA Cloud providers via
    ParallelWorks.
    Although this allows users to run Singularity containers, we currently do not
    support any new RDHPCS services (i.e. Revision Control, Registries, Mirrors,
    Etc.) for supporting Containers

.. _containers-introduction:

Introduction
============

As both existing and new NOAA projects endeavor to build software tools and
solutions that are portable across many HPC sites and architectures, it is
important that the RDHPCS program be proactive in providing necessary tools to
support these projects. One such solution for allowing users to accomplish this
goal is with the use of *software containers*. Through the use of containers,
software developers can build their stack and create encapsulated run-time
environments which may be distributed to their user base. This greatly
minimizes the need for users to have to worry about software dependencies and
user environment.

A single container image stored on disk can be used for launching multiple
container instances, including by different users. Each running container
is treated by the host system as a regular process.

A key advantage of containers is portability. They allow applications to be
deployed quickly on new systems while preserving a consistent execution
environment, eliminating the need to manually resolve dependencies.
Containers are widely used in cloud computing, where they provide a scalable
and reproducible way to run applications across diverse infrastructure.

Background
----------

.. _containers-background:

A container is a standardized unit of software that packages an application
together with all of its dependencies, providing a self-contained operating
system (OS)–like environment. This encapsulation ensures that the application
can run consistently and results are reproducibile across different systems.

Containers can be viewed as a form of lightweight virtualization, similar to
virtual machines (VMs). However, unlike VMs, containers share the host
system’s OS kernel (typically the Linux kernel), as illustrated in the
figure below. This interaction with host at the application level leads
to lower overhead and more efficient use of the host system resources.

.. figure:: /images/containers_system1.png
   :width: 60%
   :align: center
   :alt: containers share hardware and OS kernel with the host, and started as regular processes

   Containers share hardware and OS kernel with the host, and are started as regular processes.

Containers are typically stored and distributed as image files, such as `.img`
(legacy formats) or `.sif` (Singularity Image Format). Each image contains its
own filesystem and all necessary software components. Container software —
such as *SingularityCE* or *Apptainer* — is used to launch these images to
start a container instance. Container is thus a running environment of the
image, and has layers such as `a) Linux base image, b) application image,
c) configuration`.

A container provides its own filesystem, effectively complementing the host
system’s operating system environment, as demonstrated in the diagram below.

.. figure:: /images/containers_system2.png
   :width: 60%
   :align: center
   :alt: containers have their own filesystem; they interact with the host at runtime, providing virtualication at the application level

   Containers have their own filesystem. They interact with the host at runtime, providing virtualication at the application level.

Containers can "bind" directories from the host system, making selected host
filesystems accessible inside the running container. This enables the container
to work with external data and resources while still maintaining an isolated
execution environment.

The example below demonstrates starting a container instance from the image
file :file:`image.sif` and opening an interactive shell inside it (the commands
and syntax for launching containers are described later in this chapter). In
this example, host filesystems  :file:`/work`, :file:`/scratch`,
and :file:`/local` are bound into the container and with the same paths,
preserving their original locations. In contrast, the host filesystem
:file:`/apps` is bound to a different path, :file:`/apps2`, inside the
container.

.. code-block:: shell

    $ singularity shell -B /work -B /scratch -B /local -B /apps:/apps2 image.sif

.. figure:: /images/container_bind_host_fs.png
   :width: 60%
   :align: center
   :alt: example of binding host filesystems into the container with the same name as on the host system, or a different name

   An example of binding host filesystems into the container with the same name as on the host system, or a different name.

.. _containers-supported-rdhpcs-container-solutions:

Supported RDHPCS Container Solutions
------------------------------------

The dominant container platform across the enterprise and broader container
ecosystem is Docker <https://www.docker.com/>_; however, it is not well suited
for High Performance Computing (HPC) environments. A key limitation is that
Docker typically requires root (or sudo) privileges to build and run
containers, raising security concerns on shared HPC systems. Additionally,
Docker is designed for microservice-based workloads, where numerous small,
loosely coupled applications are deployed. This architecture does not scale
efficiently across large numbers of cores or multiple compute nodes, making
Docker unsuitable for resource-intensive applications typical of HPC
environments.

To address these needs, alternative container technologies have been developed
specifically for HPC environments. One such solution is `Singularity`, which
was later split into `SingularityCE` (Community Edition) and `Apptainer`. These
packages are designed to operate securely without requiring elevated privileges
and to integrate effectively with HPC system architectures. In the remainder
of this text, the term “Singularity” is used in a general sense, with
distinctions between *SingularityCE* and *Apptainer* software packages noted
where relevant.

Singularity
===========

Singularity is a container solution created for scientific and
application-driven workloads for shared computing environments such as HPC
systems. It was originally developed by Lawrence Berkeley National
Laboratory (LBL).

Please note that there is a fork in the development of singularity into two
projects, `Apptainer <https://apptainer.org/>`_ and `SingularityCE
<https://sylabs.io/singularity/>`_. Containers
built with either tool are expected to work with the other tool.
SingularityCE can be invoked from the command line using the `singularity`
command, and Apptainer can be invoked with the `apptainer` command.
Apptainer aliases the SingularityCE command, so users can use the
`singularity` command on all RDHPCS systems without breaking their workflows.
However, there are small but important differences between Apptainer and
SingularityCE. For convenience, when the word *Singularity* is used, it
implies either *SingularityCE* or *Apptainer* or both depending on the context.

The `Apptainer documentation
<https://apptainer.org/docs/user/latest/>`_ and `Docker documentation
<https://docs.docker.com/>`_ may provide useful information.
Please refer to the `SingularityCE documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_ for additional information.

Differences between SingularityCE and Apptainer
-----------------------------------------------

The installation process is the main difference between SingularityCE and
Apptainer. SingularityCE inherited the legacy Singularity behavior and is
installed with *setuid* bit enabled. However, Apptainer by default
disables *setuid* and runs in *root-less* mode out of the box. As a
result, wherever SingularityCE is installed, container build service is
disabled for security reasons. However, users can build containers
with Apptainer out of the box.


Additional differences arise when users try to run MPI applications through
containers. An Apptainer MPI task is not allowed to access the memory
associated with the other MPI tasks, so direct copying of memory is not
possible with Apptainer in the default mode. For newer versions of Apptainer,
this limitation is eased by specifying a flag. When older versions of Apptainer
are deployed, users have to specify MPI options that disable
features such as Cross Memory Attach. Using OpenMPI or HPCX, this can be
accomplished by disabling *vader* shared memory transport mechanism for single
node jobs. Similar workarounds are needed in other cases.


Either SingularityCE or Apptainer is deployed on any given RDHPCS system.
The below table shows the installed container software on the RDHPCS systems.

=============  =============  =========
RDHPCS System  SingularityCE  Apptainer
=============  =============  =========
Gaea           No             Yes
Hera           Yes            No
Mercury        Yes            No
MSU-HPC        Yes            Yes
Mercury        Yes            No
PPAN           Yes            No
Ursa           No             Yes
NOAA Cloud PW  Yes            No
=============  =============  =========

.. _containers-limitation-exception-liability:

Limitation, Exception and Liability
-----------------------------------

One exception regarding software dependencies issues, is
within HPC where parallel programs require a Message Passing
Interface (MPI) library for communication across distributed tasks.
Although there is ongoing work to provide compatibility between
different MPI solutions, there is still a need to build containers
with a matching flavor and in some cases, version of an MPI
implementation.

..
  ** Apptainer circumvents the issue **
  Building the Container image usually requires root permission, which
  has to be implemented by users on other platforms. NOAA RDHPCS does
  not currently provide this service/permission to our users. Users
  have to create images outside of RDHPCS and copy them to the R&D
  HPC systems to run with Singularity.

It is user's responsibility to make sure that the images
downloaded from the internet or created by the user will not violate
the NOAA RDHPCS security policy.

.. _containers-singularity:


How to create images
--------------------

Superuser permissions are required to create images from SingularityCE.
For security reasons, this service is not currently allowed on NOAA's R&D HPC
systems, where SingularityCE is installed.
Users either need to download available images online, or build their
own images on other platforms where Apptainer is installed.

.. note::

    Podman is available on PPAN / Analysis for this purpose.

For image building, please refer to the related `documents for SingularityCE
<https://docs.sylabs.io/guides/latest/user-guide/>`_  or
`Docker <Docker documentation_>`_. Existing
Docker images can be converted to Singularity images and then run on NOAA's R&D
HPC systems.

.. note::

    As with any model source code, we expect our users to download container
    images from reputable sources and to fully understand the contents of the
    Container prior to running it on R&D HPC systems.


Download Singularity containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Docker Hub <https://hub.docker.com>`_ and `Singularity Hub
<https://singularityhub.com/>`_ contain dynamic images. The singularity images can
be downloaded or converted from Docker images outside of RDHPCS. This can be
done with Singularity using ``singularity build lolcow.sif
shub://GodloveD/lolcow`` where ``lolcow.sif`` is the name of the Singularity
image file, and ``shub://GodloveD/lolcow`` is the Singularity Hub container to
download.


Convert Docker container to Singularity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can convert Docker containers to a Singularity image and then run the image
on R&D HPC systems.

..
  Currently the `Docker Hub`_ is not opened on the R&D HPC systems.
  You need to do the conversion externally and then copy the image back to R&D
  HPC systems.

.. code-block:: shell

    $ singularity pull lolcow.sif docker://godlovedc/lolcow

Build containers
^^^^^^^^^^^^^^^^

Follow the `build documentation for Singularity <https://docs.sylabs.io/guides/latest/user-guide/build_a_container.html>`_. In
brief, given an singularity definition file called :file:`lolcow.def`, run
the command ``singularity build lolcow.sif lolcow.def`` to build
the image.

.. important::

    You may need sudo/root permissions on the system where SingularityCE is installed.

Use an existing image file
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you already have an image file on other machines, you can simply
copy it to the target machine, and use it there.

Run a Single Node or Single Core Containers
-------------------------------------------

Follow the `Singularity documentation <https://docs.sylabs.io/guides/latest/user-guide/>`_. Here is an example to run the
Singularity image :file:`hydro.sif`.

.. code-block:: shell

    $ singularity run hydro.sif echo "hello world"

Run an MPI-dependent container
------------------------------

The MPI application requires the match of the MPI software between the
container and target machine. Refer to `Singularity documentation`_ for
compatibility.

Using a container to compile a model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build a model within a container, the container must have the compiler and
all required libraries and library headers.  An easy way to accomplish this is
to launch an interactive shell in the container, then build the model as is
typically done on any system.

.. code-block:: shell

    $ singularity shell container.sif

Using a container to run a parallel job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example Slurm script to run the wrf model with 512 MPI tasks. In
this example, the :file:`wrf.exe` executable is compiled on the host machine
using the :file:`hydro.sif` container. The :file:`wrf.exe` and
:file:`hydro.sif` files are all in the working directory of the run.

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


    srun singularity exec hydro.sif ./wrf.exe

.. note::

    The :file:`hydro.sif` and :file:`wrf.exe` are under the same directory.
    Under the running directory, you will not have the soft links from other
    directories.

Container help, questions, and guidance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The complexities involving containers, particularly MPI and containers,
can make containers difficult to use. RDHPCS system administrators and help
staff have limited knowledge on using containers on HPC systems. Open a
:ref:`help request <getting_help>` to what help can be offered. However,
you will likely find your fellow scientists and the greater container
communities have better knowledge for your specific Singularity
image/application.
