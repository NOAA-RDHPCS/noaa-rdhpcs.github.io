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
    Etc.) to support Containers.

The Chapter outline is as following:

| :ref:`Introduction <containers-introduction>`
| :ref:`Background <containers-background>`
| :ref:`Supported RDHPCS Container Solutions
  <containers-supported-rdhpcs-container-solutions>`
| :ref:`Singularity <containers-singularity>`
| :ref:`User Identity and Execution Model <containers-user-identity>`
| :ref:`Differences Between SingularityCE and Apptainer
  <containers-differences-singularity-apptainer>`
| :ref:`Limitation, Exception, and Liability
  <containers-limitation-exception-liability>`
| :ref:`Downloading and Creating Container Images
  <containers-singularity-images>`
| :ref:`Container Support of MPI Implementaion
  <containers-mpi-implementation-support>`
| :ref:`Bind Mounting Host Directories Into a Container
  <containers-bind-mount-host-directories>`

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


.. _containers-background:

Background
----------

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

   Containers have their own filesystem. They interact with the host at
   runtime, so the container instance is viewed as a regular running
   application.

Containers can "bind" directories from the host system, making selected host
filesystems accessible inside the running container. This enables the container
to work with external data and resources while still maintaining an isolated
execution environment, see Section :ref:`Bind Mounting Host Directories
<containers-bind-mount-host-directories>`.

The example below demonstrates starting a container instance from the image
file ``image.sif``` and opening an interactive shell inside it (the commands
and syntax for launching containers are described later in this chapter). In
this example, host filesystems  ``/work``, ``/scratch``,
and ``/local`` are bound into the container and with the same paths,
preserving their original locations. In contrast, the host filesystem
``/apps`` is bound to a different path, ``/apps2``, inside the
container.

.. code-block:: shell

    singularity shell -B /work -B /scratch -B /local -B /apps:/apps2 image.sif

.. figure:: /images/container_bind_host_fs.png
   :width: 60%
   :align: center
   :alt: example of binding host filesystems into the container with the same name as on the host system, or a different name

   An example of binding host filesystems into the container with the same name as on the host system, or a different name.

.. _containers-supported-rdhpcs-container-solutions:

Supported RDHPCS Container Solutions
------------------------------------

The dominant container platform across the enterprise and broader container
ecosystem is
`Docker <https://www.docker.com/>`_ .  However, Docker is not well
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

.. _containers-singularity:

Singularity
===========

*Singularity* is a container solution created for scientific and
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

Some of the most common commands are the following:

.. code-block:: shell

    singularity pull ...    # converting a remote image into local *.sif image
    singularity build ...   # building an image or sandbox, in one of the supported ways
    singularity shell ...   # for shelling into the container or sandbox_dir
    singularity run ...     # for running a container
    singularity exec ...    # for launching a user's executable with the container

Users could easily access help with these options using ``--help`` command,
e.g.:

.. code-block:: shell

    singularity --help
    singulairty exec --help

.. _containers-user-identity:

User Identity and Execution Model
---------------------------------

Both SingularityCE and Apptainer are designed for shared HPC environments and
thus follow a non-root, user-preserving execution model.
By default, container runtimes in SingularityCE and Apptainer preserve
the invoking user’s identity inside the container, so the same `UID/GID`
(user ID, group ID) is
used and no additional privileges are granted beyond those already held
on the host (unless explicity enabled via limited features like
``--fakeroot`` for iterative development purposes, as discussed later).

.. _containers-differences-singularity-apptainer:

Differences Between SingularityCE and Apptainer
-----------------------------------------------

The installation process is the main difference between SingularityCE and
Apptainer. SingularityCE inherited the legacy Singularity behavior and is
installed with *setuid* bit enabled (effectively running programs with the
permissions of the file's owner, not the user who executes it).
Apptainer by default disables *setuid* and runs in *root-less* mode out of
the box. For a regular user, SingularityCE thus largely disables  **build**
service for security reasons, with some exceptions for few basic builds
(such as pulling a container from a Docker repository converting it into
``*.sif`` image). Apptainer users, however, can build containers out of the
box.

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
are handled using Message Passing Interface (*MPI*), a standardized
framework for exchanging messages across CPUs and nodes in
distributed-memory systems. Different supported models for MPI
integration into container runtime environment are described in the
Section :ref:`Container Support of MPI Implementation
<containers-mpi-implementation-support>` .

As with any model source code, it is users responsibility to download
container images from reputable sources, to make sure that the images
downloaded from the internet or created by the user will not violate
the NOAA RDHPCS security policy, and to fully understand the contents
of container images prior to running it on RDHPC systems.

.. _containers-singularity-images:

Downloading and Creating Container Images
-----------------------------------------

There are several ways to create Singularity container images or pull them
from existing repositories. Some of the methods may be available for
regular users, others require superuser (*sudo/root*) permissions to
to create images using SingularityCE. For security reasons, some
``build`` services are limited on NOAA's RDHPC systems, where SingularityCE
is installed. Users could build their own images on other platforms
where Apptainer is installed.

.. note::

    Podman is available on PPAN / Analysis for this purpose.

For image building, also refer to the related `documents for SingularityCE
<https://docs.sylabs.io/guides/latest/user-guide/>`_, `documents for
Apptainer <https://apptainer.org/docs/user/main/>`_ or
`Docker docs <Docker documentation_>`_. Existing
Docker images can be converted to Singularity images and then run on NOAA's R&D
HPC systems.

.. _containers-pull-image:

Convert Docker Container to Singularity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pull from DockerHub or other Open Container Initiative (*OCI*)
repositories. It downloads a prebuilt container and converts it into
``.sif`` format. No root privilege is required.

.. code-block:: shell

    singularity pull image.sif docker://rockylinux:9
    singularity pull image.sif docker://myrepo/myimage:tag

.. _containers-build-image:

Build from a Docker Container or Other OCI-library Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    singularity build image.sif docker://rockylinux:9
    singularity build image.sif docker://myrepo/myimage:tag

Note that ``pull`` is for simple Docker/OCI-to-SIF convertion, while ``build``
is more general and has many build options. Both produce a ``.sif`` image
file, they do not enable be bit-by-bit reproducibility when converting
Docker/OCI layers.

To ensure that files and directories are readable and executable
by all users, a option ``--fix-perms`` could be used. It may mitigate
permission mismatches between build-time root and run-time user, and
adjusts restrictive permissions inherited from Docker layers, root-owned
files, and package installs. It effectively prevents runtime issues such
as *Permission denied* when accessing files, or non-root users unable to
execute binaries inside the container.

.. code-block:: shell

    singularity build --fix-perms image.sif docker://rockylinux:9

.. _containers-build-writable-sandbox:

Build a Writable Sandbox Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When further development of the container is needed, you may create a
writable sandbox. It appears as a regular directory on the host filesystem
that represents the container root filesystem. It could be built from
a remote repository or from an existing local container image:

.. code-block:: shell

   singularity build --sandbox  sandbox_dir/ docker://rockylinux:9
   singularity build --sandbox --fix-perms sandbox_dir/ docker://rockylinux:9
   singularity build --sandbox  sandbox_dir/ image.sif

This creates a directory structure under ./mydirs with further nested
``bin/``, ``etc/``, ``usr/``, ``var/`` and other container directories,
emulating filesystem in user space. It could be accessed as other user's
directories, and is not compressed, taking more disk space than the image.

In contrary, a ``.sif`` image file has a filesystem in a compressed form,
stored in the SquashFS partition. When container image is launched, it is
mounted as Filesystem in User
space (FUSE), using ``squashfuse/squashfuse_ll``. No mount is needed for
a sandbox container, which is helpful for development and debugging. Note
however that it does not give *sudo/root* privileges inside the container.

When using sandbox for shelling-in or running that requires writing into
the directory, use ``--writable`` option during launch, e.g.:

.. code-block:: shell

    singularity shell --writable sandbox_dir/

.. _containers-build-writable-sandbox-fakeroot:

Build a writable container sandbox with altered privileges
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    This build requires elevated sudo/root privileges when using SingularityCE

The ``--fakeroot`` option can be used to build a sandbox container with
emulated root privileges inside the container namespace, enabling installation
and modification steps that require elevated access while remaining
unprivileged on the host. This option makes it particularly useful for
iterative container development and debugging.

.. code-block:: shell

    singularity build --sandbox --fakeroot image/ docker://rockylinux:9

Mind the warnings in the terminal prompt, e.g.:

.. note::

    | WARNING: The sandbox contain files/dirs that cannot be removed with 'rm'.
    | WARNING: Use 'chmod -R u+rwX' to set permissions that allow removal.
    | WARNING: Use the '--fix-perms' option to 'apptainer build' to modify permissions at build time.

.. _containers-build-image-from-sandbox:

Build a container image from the existing sandbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A container image could also be created from the existing sandbox. If
you used sandbox for any development, it is recommended to convert it
to ``.sif`` image for production runs and batch jobs.

.. code-block:: shell

   singularity build image.sif sandbox_dir/
   singularity build --fix-perms image.sif sandbox_dir/

.. _containers-build-from-definition file:

Build a container or a sandbox from a definition file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::

    This build requires elevated sudo/root privileges when using SingularityCE.
    It could be used with Apptainer

.. code-block:: shell

   apptainer build simple-rocky9.sif simple-rocky9.def

An example of the definition file ``simple-rocky9.def``:

.. code::

    Bootstrap: docker
    From: rockylinux:9

    %labels
        Author Your Name
        Version v1.0
        Description Rocky Linux 9 example container

    %post
        dnf -y update
        dnf -y install gcc gcc-c++ gcc-gfortran
        dnf clean all

    %runscript
        echo "Hello from Rocky Linux 9 example container"
        cat /etc/os-release

Run a simple example:

.. code-block:: shell

   singularity run simple-rocky9.sif


Note that for a more complex cases users may need to list a full (absolute)
container name and *bind mounts* of host directories into the container,
as discussed in the next section.


.. _containers-mpi-implementation-support:

Container Support of MPI Implementaion
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

   .. warning::

      Mismatched MPI versions may result in runtime failures or hangs.
      The container MPI must be ABI-compatible with the host MPI.

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

    Key requirements for this model are as follows:

     *  `Binary compatibility (critical)`: the application needs to be built
        against an MPI ABI-compatible libraries with the host MPI
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
    networks such as InfiniBand (via *OFI/libfabric*, *UCX* libraries), which
    may work well on tightly managed HPC systems.

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

    Advantages:

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
    reproducibility, but is generally less reliable and may not be scalable
    as the hybrid MPI model, for multi-node HPC workloads.

In practice, the **hybrid MPI** model is considered the most robust and widely
recommended method for supporting MPI in containerized HPC workflows.

.. _containers-bind-mount-host-directories:

Bind Mounting Host Directories Into a Container
-----------------------------------------------

A container normally sees its own filesystem, plus a limited set of host
paths that are automatically mounted by the runtime environment.
To make additional host
directories visible inside the container, use *bind mounts*. A bind mount
maps a directory on the host to a directory inside the container, allowing
the application in the container to read input files, write output, and
access shared *project* or *scratch* filesystems. This is especially important
on HPC systems, where user data usually lives outside the container image,
for example under ``/home``, ``/work``, ``/scratch``, ``/lustre``, or
``/gpfs``. These bind mounts are listed in the command line using ``-B`` flag.
If more than a single directory is needed to be bound, it needs to be listed
with its own ``-B`` flag.


.. code-block:: shell

   singularity shell -B /work image.sif
   singularity shell -B /scratch3 -B /scratch4

Some host directories needed at container runtime
may have the same name as native container directories. Host directories
could then be mounted with a different name for container runtime use.
The renaming approach is as following: ``-B dir_host:dir_container``.

.. code-block:: shell

   singularity build -B /local -B /work -B  /apps:/apps2 image.sif
   singularity exec -B /local -B /work -B  /apps:/apps2 image.sif

In this case, ``/work`` and ``/local`` filesystem on the host system are
mounted with the same name, but host's ``/apps`` becomes ``/apps2`` inside
the runtime container. Usually only top-level directories (filesystems)
need to be listed to create a mount point inside the container.


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

    singularity shell container.sif

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
