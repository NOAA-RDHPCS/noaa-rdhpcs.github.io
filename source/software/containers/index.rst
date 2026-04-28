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
    <https://en.wikipedia.org/wiki/Apptainer#History>`_ containers on Ursa, Gaea,
    Hera, MSU-HPC (Orion and Hercules), Mercury, and NOAA Cloud providers via
    ParallelWorks.
    Although this allows users to run Singularity containers, we currently do not
    support any new RDHPCS services (i.e. Revision Control, Registries, Mirrors,
    Etc.) to support Containers

.. _containers-introduction:

Introduction
============

As both existing and new NOAA projects endeavor to build software tools and
solutions that are portable across many HPC sites and architectures, the RDHPCS
program must be proactive in providing tools necessary to
support these projects. One such solution that allows users to accomplish this
goal is the use of *software containers*. Using containers,
software developers can build their stack and create encapsulated run-time
environments which may be distributed to their user base. This greatly
minimizes user concerns about software dependencies and
machine-specific user environments.

A single container image stored on disk can be used to launch multiple
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
to lower overhead and more efficient use of the host system's resources.

.. figure:: /images/containers_system1.png
   :width: 60%
   :align: center
   :alt: containers share hardware and OS kernel with the host, and started as regular processes

   Containers share hardware and OS kernel with the host, and are started as regular processes.

Containers are typically stored and distributed as image files, such as
``.img`` (legacy formats) or ``.sif`` (Singularity Image Format). Each image
contains its own filesystem and all necessary software components, built as
several software layers stacked on top of each other. Container software —
such as *SingularityCE* or *Apptainer* — is used to launch these images to
start a container instance. Container is thus a running environment of the
image, and has layers such as `a) Linux base image, b) application image,
c) configuration`.

A container provides its own filesystem, effectively complementing the host
system’s operating system environment, as illustrated in the diagram below.

.. figure:: /images/containers_system2.png
   :width: 60%
   :align: center
   :alt: containers have their own filesystem; they interact with the host at runtime, making a container instance being viewed as regular running application.

Containers have their own filesystem. They interact with the host at runtime,
so the container instance is viewed as a regular running application.

Containers can "bind" directories from the host system, making selected host
filesystems accessible inside the running container. This enables the container
to work with external data and resources while still maintaining an isolated
execution environment.

The example below demonstrates starting a container instance from the image
file ``image.sif``` and opening an interactive shell inside it (the commands
and syntax for launching containers are described later in this chapter). In
this example, host filesystems  ``/work``, ``/scratch``,
and ``/local`` are bound into the container and with the same paths,
preserving their original locations. In contrast, the host filesystem
``/apps`` is bound to a different path, ``/apps2``, inside the
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
ecosystem is `Docker <https://www.docker.com/>_`.  However, Docker is not well
suited to High Performance Computing (HPC) environments. A key limitation is
that Docker typically requires root (or sudo) privileges to build and run
containers, raising security concerns on shared HPC systems. Additionally,
Docker is designed for microservice-based workloads, where numerous small,
loosely coupled applications are deployed. This architecture does not scale
efficiently across large numbers of cores or multiple compute nodes, making
Docker unsuitable for resource-intensive applications typical of HPC
environments.

To address these needs, alternative container technologies have been developed
specifically for HPC environments. One such solution is `Singularity`,
designed to operate securely without requiring elevated privileges
and to integrate effectively with HPC system architectures.

Singularity
===========

Singularity is a container solution created for scientific and
application-driven workloads for shared computing environments such as HPC
systems. It was originally developed by Lawrence Berkeley National
Laboratory (LBL), and initially released in 2015 (see `Singularity/Apptainer
history <https://en.wikipedia.org/wiki/Apptainer#History>`_).

A fork in the development of *Singularity* happened few years later,
splitting the initial project into two. One is a direct
continuation of the initial project, `SingularityCE
<https://sylabs.io/singularity/>`_, is an open source with commercial
vendor stewardship. The other is `Apptainer <https://apptainer.org/>`_, more
community-driven and oriented on HPC and Cloud use and integration.
Containers built with either tool are expected to work with the other tool.
SingularityCE can be invoked from the command line using the ``singularity``
command, and Apptainer can be invoked with the ``apptainer`` command.
Apptainer aliases the SingularityCE command, so users can use the
``singularity`` command on all RDHPCS systems without breaking their workflows.

The `Apptainer documentation
<https://apptainer.org/docs/user/latest/>`_, `SingularityCE documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_, and `Docker
documentation <https://docs.docker.com/>`_  provide more extensive
information about containerization, software installations, and users guides.

Differences between SingularityCE and Apptainer
-----------------------------------------------

The installation process is the main difference between SingularityCE and
Apptainer. SingularityCE inherited the legacy Singularity behavior and is
installed with *setuid* bit enabled (effectively running programs with the
permissions of the file's owner, not the user who executes it).
Apptainer by default disables *setuid* and runs in *root-less* mode out of
the box. For a regular user, SingularityCE thus largely disables **`build`**
service for security reasons, with some exceptions for very basics (such
as pulling a container from a Docker repository converting it into ``*.sif``
image. Apptainer users, however, can build containers out of the box.

Either SingularityCE or Apptainer is deployed on any given RDHPCS system.
The below table shows the installed container software on the RDHPCS systems.

===============  =============  =========
RDHPCS System    SingularityCE  Apptainer
===============  =============  =========
Gaea             No             Yes
Hera             Yes            No
Mercury          Yes            No
MSU-HPC          Yes            Yes
Mercury          Yes            No
PPAN             Yes            No
Ursa             No             Yes
NOAA Cloud (PW)  Yes            No
===============  =============  =========

.. _containers-limitation-exception-liability:

Limitation, Exception and Liability
-----------------------------------

Many applications on HPC systems are designed to run in parallel across
multiple CPUs and often multiple nodes for scalable performance.
Communication and coordination between the tasks in such applications
are handled using *MPI* (Message Passing Interface), a standardized
framework for exchanging messages across CPUs and nodes in
distributed-memory systems.

An outlile of supported modes of runtime environment models for
MPI integration is given below.

As with any model source code, it is users to download container
images from reputable sources, to make sure that the images
downloaded from the internet or created by the user will not violate
the NOAA RDHPCS security policy, and to fully understand the contents
of container images prior to running it on RDHPC systems.


.. _containers-mpi-implementation-support:

Container suppport of MPI implementaion
---------------------------------------

SingularityCE and Apptainer typically provide runtime environment for
a few supported MPI intergration models.

#. **Hybrid MPI model**  (host + container MPI) is the most common and
   recommended approach.

   *  The MPI launcher (e.g., ``mpirun`` or Slurm's ``srun``) is executed
      on the host system, which starts ranks across the nodes, assigns
      ranks, nodes, resources
   *  Each MPI rank executes the container runtime, resulting in one
      container instance per rank
   *  MPI communication uses host fabric (*OFI*, *UCX*, *TCP*, etc.)

   A key requirement is that container MPI libraries be compatible
   with the host MPI at the binary level (i.e., *ABI*-compatible). An
   Application Binary Interface (ABI) defines how compiled programs and
   libraries interact, including function calls, data types, symbol names,
   system calls, and linking.  Two main compatibility requirements depend
   on the launch method:

    * Host MPI launcher (``mpirun``) — MPI ABI compatibility:
      The container MPI must be ABI-compatible with the host MPI
      (e.g., matching OpenMPI major version and build conventions)
    * Scheduler launcher (``srun``) — PMI/PMIx compatibility:
      With schedulers such as Slurm, the container MPI must interoperate
      with the host’s Process Management Interface, *PMI*, or PMI for
      Exascale, *PMIx*, which provides process mapping
      and connection information required for MPI initialization.


#. **Host MPI only (bind) model** - the container does not include an MPI
   implementation, creating lighter container images. Instead, the application
   inside the container dynamically links against the compatible host MPI
   libraries, made visible via `bind` mounts.

   * The host MPI launcher (``mpirun`` or scheduler like Slurm ``srun``)
     starts the job, assignes nodes, ranks, resources
   * MPI libraries and dependencies from the host are `bind-mounted`
     into the container
   * The containerized executable resolves MPI symbols from the host
     environment
   * Uses optimized vendor MPI (e.g, Cray, Intel MPI, etc.), access to
     higher-performance networks such as InfiniBand (OFI/libfabric, UCX),
     and may work well on on tightly managed HPC systems

    Key requirements for this model are as follows

     *  `Binary compatibility (critical)`: the application needs to be built
        against an MPI ABI-compatibel libraries with the host MPI
     *  `Library binding`: host MPI, fabric, and vendor libraries
        (e.g., /usr/lib64, /opt, /opt/cray) need to be mounted into the
        container
     *  `Environment propagation`: variables such as ``LD_LIBRARY_PATH``,
        ``I_MPI_*``, ``PMI_*/PMIX_*``, and fabric settings (``FI_*``,
        ``UCX_*``) must be available inside the container
     *  `Scheduler/PMI integration`: access to `PMI/PMIx` services is
        required for correct multi-node initialization


    Certain advantages of this model include: i) smaller container images;
    ii) avoiding MPI duplication and version drift; iii) use of optimized
    vendor MPI (e.g, Cray, Intel MPI, etc.) and access to higher-performance
    networks such as InfiniBand (via OFI/libfabric, UCX libraries), which may
    work well on tightly managed HPC systems.

    However, this approach offers low portability due to container tied to
    a specific system's MPI stack, as well as required knowledge of host
    libraries, fabrics, vendor libraries, and of environmental configuration.
    For Intel MPI, it is generally more tighly version-coupled than other MPI
    implementations.

#. **Fully containerized MPI** model (contained MPI approach) builds and runs
   the application entirely against the MPI stack provided inside the
   container. The container image includes:

   *  MPI implementation (e.g., *Open MPI*, *MPICH*, or *Intel MPI*)
   *  MPI launcher (``mpirun``, ``mpiexec``), with no intentional reliance on
      host MPI installations
   *  Execution initiated from within the container

    Advantages of this approach:

     *   Portable and reproducible — self-contained MPI stack independent of
         the host
     *   Isolated environment — avoids conflicts with system MPI and modules
     *   Simple packaging into a single image with all dependencies

    Disadvantages:
     *   Limited multi-node support — weaker integration with schedulers
         (e.g., *Slurm*, *PBS*)
     *   PMI/PMIx dependency — still must interoperate with host process
         management
     *   Network fabric dependence and performance risks — requires correct
         configuration and access to network fabrics (*InfiniBand*, etc.)
         and/or shared-memory transports
     *   Less robust for production HPC environments and potentially fragile in
         operational environments, as it may work in one environment but fail
         in another due to subtle system differences

    The fully containerized MPI approach maximizes portability and
    reproducibility, but is generally less reliable and less scalable than the
    hybrid MPI model, for multi-node HPC workloads.

In practice, the **hybrid MPI** model is considered the most robust and widely
recommended method for supporting MPI in containerized HPC workflows.

.. _containers-singularity:


Creating container images
-------------------------

Superuser permissions are required to create images from SingularityCE.
For security reasons, this service is not currently allowed on NOAA's R&D HPC
systems, where SingularityCE is installed.
Users must either download available images online, or build their
own images on other platforms where Apptainer is installed.

.. note::

    Podman is available on PPAN / Analysis for this purpose.

For image building, refer to the related `documents for SingularityCE
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

Here is a sample Slurm script to run the wrf model with 512 MPI tasks. In
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
:ref:`help request <getting_help>` to obtain what help can be offered.
In practice, you will likely find that your fellow scientists and the
greater container communities have better knowledge for your specific
Singularity image/application.
