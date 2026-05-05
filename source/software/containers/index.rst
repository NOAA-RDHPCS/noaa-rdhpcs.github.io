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

.. note:: **Current Status**

    We now allow all users and projects to run `Singularity
    <https://en.wikipedia.org/wiki/Apptainer#History>`_ containers on Ursa, Gaea,
    Hera, MSU-HPC (Orion and Hercules), Mercury, and NOAA Cloud providers via
    ParallelWorks.
    Although users are allowed to run Singularity containers, we currently do not
    support any new RDHPCS services (i.e. Revision Control, Registries, Mirrors,
    Etc.) to support Containers.

.. _containers-introduction:

Introduction
============

As both existing and new NOAA projects endeavor to build software tools and
solutions that are portable across multiple HPC sites and architectures,
the RDHPCS program aims to provide the tools and infrastructure necessary to
support these efforts. One such solution is the use of *software containers*.
Unlike traditional environments based
on modules or system-installed libraries, containers encapsulate the full
runtime stack while operating within a shared, multi-user HPC system without
requiring elevated privileges.

This chapter describes how to use containers effectively on RDHPCS systems,
including how to obtain and build container images, how to use containers
for software development, and how to run applications in batch and
MPI-enabled workflows. Particular emphasis is placed on practical usage
patterns, such as integrating containers with system schedulers, managing
environment variables, and accessing host filesystems.

While containers provide a high degree of portability, their correct use
in HPC environments requires an understanding of several key concepts,
including: 

* the container execution model
* filesystem access through bind mounts
* interaction with system-provided Message-Passing Interface
  (MPI) implementations.

These topics are introduced in the following sections.


.. _containers-background:

Background
----------

A container is a standardized unit of software that packages an application
together with its dependencies into a self-contained runtime environment.
This encapsulation allows applications to run consistently across different
systems and improves reproducibility of results.

Containers provide lightweight virtualization by sharing the host system’s
OS kernel (typically Linux), unlike virtual machines (VMs), which rely on
hardware emulation and run separate operating systems. This design reduces
overhead while maintaining isolation at the application level, as illustrated
in the figure below.

.. figure:: /images/containers_system1.png
   :width: 60%
   :align: center
   :alt: containers share hardware and OS kernel with the host, and started as regular processes

   Containers share hardware and OS kernel with the host, and are executed as regular processes.

Container environments are typically stored and distributed as image files,
such as ``.sif`` (Singularity Image Format). An image contains a complete
filesystem with all required software components and is commonly constructed
from layered components. Container software — such as *SingularityCE*
or *Apptainer* — is used to launch these images on the host system to start a
container instance. A *container* is thus a running instance of an image.

Each container provides its own filesystem while interacting with the host
system at runtime, as illustrated in the diagram below.

.. figure:: /images/containers_system2.png
   :width: 60%
   :align: center
   :alt: containers have their own filesystem; they interact with the host at runtime, making a container instance being viewed as regular running application.

   Containers have their own filesystem. They interact with the host at
   runtime, so the container instance is viewed as a regular running
   application.

Although containers provide an isolated environment, they rely on the host
system for access to filesystems, hardware, and other resources. Host
directories can be made available inside the container at runtime through
*bind mounts*, enabling applications to read input data and write output
results (see :ref:`Bind Mounting Host Directories Into a Container
<containers-bind-mount-host-directories>`).

Effective use of containers in HPC workflows therefore requires an
understanding of how containerized applications interact with the host
system, particularly with respect to filesystem access and environment
configuration. These aspects are described in the sections that follow.

.. _containers-supported-rdhpcs-container-solutions:

Supported RDHPCS Container Solutions
------------------------------------

The dominant container platform across the enterprise and broader container
ecosystem is `Docker <https://www.docker.com/>`_. However, *Docker* is not well
suited to High Performance Computing (HPC) environments. A key limitation is
that Docker typically requires *root* (or ``sudo``) elevated privileges to
build and run containers, which raises security concerns on shared HPC systems.
In addition, *Docker* is designed for microservice-oriented workloads, where
many small, loosely coupled services are deployed, a model that does not align
well with large-scale, resource-intensive applications typical of
HPC environments.

To address these needs, alternative technologies have been developed
specifically for HPC environments, such as *Singularity* containers
(`software <https://en.wikipedia.org/wiki/Singularity_(software)>`_).
In particular, *SingularityCE*
`https://sylabs.io/singularity/<https://sylabs.io/singularity/>`_ and
*Apptainer*(`https://apptainer.org/ <https://apptainer.org/>`_)
provide a container model
that operates without requiring elevated privileges, and could integrate with
HPC system architecture, batch schedulers, parallel filesystems, and
high-performance interconnects.

Both *SingularityCE* and *Apptainer* are supported On RDHPCS systems.
The table below shows the installed container software on each system.

===============  =============  =========
RDHPCS System    SingularityCE  Apptainer
===============  =============  =========
Gaea             No             Yes
Hera             Yes            No
Mercury          Yes            No
MSU-HPC          Yes            Yes
PPAN             Yes            No
Ursa             No             Yes
NOAA Cloud (PW)  Yes            No
===============  =============  =========

.. note::

   Availability of *SingularityCE* and *Apptainer* may change as systems are
   updated. Use ``module avail`` to verify installed versions.

Containers built with either tool are expected to work with the other tool.
*SingularityCE* can be invoked from the command line using the ``singularity``
command, and *Apptainer* can be invoked with the ``apptainer`` command.
*Apptainer* provides compatibility with the ``singularity`` command,
allowing users to use the same command across RDHPCS systems. Differences
primarily relate to configuration defaults and installation details, but
generally do not affect typical user workflows.

.. _containers-singularit-evolution:

Singularity Containers
======================

*Singularity* was introduced in 2015 as a container solution designed
specifically for HPC environments (see `Singularity/Apptainer
history <https://en.wikipedia.org/wiki/Apptainer#History>`_),
with a focus on security, portability, and integration with existing system
architectures. Unlike Docker,
Singularity allows users to run containers without elevated privileges,
making it suitable for shared, multi-user systems.

In 2021, the project transitioned to a community-driven model under the
Linux Foundation and continued as *Apptainer*. In parallel, *SingularityCE*
(Community Edition) continued development under separate stewardship.
Both projects retain a common design and are widely used across HPC systems.

Further information is available at:

- Docker:
  `https://www.docker.com/<https://www.docker.com/>`_
- Docker Documentation:
  `https://docs.docker.com/<https://docs.docker.com/>`_

- SingularityCE:
  `https://sylabs.io/singularity/<https://sylabs.io/singularity/>`_
- SingularityCE Documentation:
  `https://docs.sylabs.io/<https://docs.sylabs.io/>`_
  `https://docs.sylabs.io/guides/latest/user-guide/<https://docs.sylabs.io/guides/latest/user-guide/>`_

- Apptainer:
  `https://apptainer.org/<https://apptainer.org/>`_
- Apptainer Documentation:
  `https://apptainer.org/docs/<https://apptainer.org/docs/>`_
  `https://apptainer.org/docs/user/latest/<https://apptainer.org/docs/user/latest/>`_

.. _containers-user-identity:

Container User Identity
-----------------------

Both SingularityCE and Apptainer are designed for shared HPC environments
and follow a non-root execution model that preserves the invoking user’s
identity inside the container. Processes run with the same ``UID/GID`` as
on the host, so file permissions, access controls, and resource limits are
enforced consistently. As a result, no additional privileges are granted
beyond those already held on the host, unless explicitly enabled through
limited features such as ``--fakeroot`` for development purposes.
Host directories must be explicitly made accessible inside the container
(e.g., through *bind mounts*) for applications that need read/write access.
This ensures consistent behavior within standard HPC security
policies.

.. _containers-differences-singularity-apptainer:

Differences Between SingularityCE and Apptainer
-----------------------------------------------

The installation process is the main difference between SingularityCE and
Apptainer. SingularityCE inherited the legacy *Singularity* behavior and is
installed with *setuid* bit enabled (effectively running programs with the
permissions of the file's owner, not the user who executes it).
Apptainer by default disables *setuid* and runs in *root-less* mode out of
the box. For a regular user, SingularityCE thus largely disables  **build**
service for security reasons, with some exceptions for few basic builds
(such as pulling a container from a Docker repository converting it into
``*.sif`` image). Apptainer users, however, can build containers out of the
box.

SingularityCE and Apptainer provide similar user workflows, but differ
in that SingularityCE relies more on privileged kernel operations,
while Apptainer emphasizes a rootless, user-space model that is more
secure and portable but requires more explicit configuration in HPC
environments.

.. _containers-limitation-exception-liability:

Usage Considerations and Security Responsibilities
--------------------------------------------------

Many applications on HPC systems are designed to run in parallel across
multiple CPUs and often multiple nodes for scalable performance.
Communication and coordination between the tasks in such applications
are handled using Message Passing Interface (*MPI*), a standardized
framework for exchanging messages across CPUs and nodes in
distributed-memory systems. Different approaches for MPI integration
in container runtime environments are described in
Section :ref:`MPI Integration Models <containers-mpi-integration>`.
Users should evaluate the
available approaches and select the one that best fits their application
and workflow requirements.

As with any model source code, it is users responsibility to download
container images from reputable sources, to make sure that the images
downloaded from the internet or created by the user will not violate
the NOAA RDHPCS security policy, and to fully understand the contents
of container images prior to running it on RDHPC systems.

.. _containers-building-images:

Obtaining and Building Container Images
=======================================

There are several ways to obtain or build container images using
SingularityCE or Apptainer, including pulling images from existing
repositories or creating them locally. Some methods are available to regular
users, while others require superuser (``sudo``/root) privileges when using
SingularityCE. For security reasons, some ``build`` capabilities are
restricted on NOAA RDHPC systems where SingularityCE is installed. Users could
build their own images on other platforms where Apptainer is available.

.. note::

    Podman is available on PPAN / Analysis for this purpose.

For additional details, refer to the `SingularityCE Documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_, `Apptainer
documentation <https://apptainer.org/docs/user/main/>`_, or
`Docker documentation <https://docs.docker.com/>`_. Existing
Docker images can be converted to Singularity images and then run on NOAA
RDHPC systems.

.. _containers-pull-convert-images:

Pull and Convert Docker Images to Singularity Format
----------------------------------------------------

Pull from DockerHub or other Open Container Initiative (*OCI*)
repositories. It downloads a prebuilt container and converts it into
``.sif`` format. No root privilege is required.

.. code-block:: shell

    singularity pull image.sif docker://rockylinux:9
    singularity pull image.sif docker://myrepo/myimage:tag

.. _containers-build-image:

Build from a Docker Container
-----------------------------

.. code-block:: shell

    singularity build image.sif docker://rockylinux:9
    singularity build image.sif docker://myrepo/myimage:tag

The ``pull`` command performs a simple conversion from Docker/OCI images
to ``.sif`` format, while ``build`` provides more general functionality
and additional options. Both produce a ``.sif`` image
file, but would not be bit-for-bit identical when converting
Docker/OCI layers.

To ensure that files and directories are accessible to all users, the
``--fix-perms`` option can be used. It mitigates permission mismatches
between build-time root and run-time users by adjusting restrictive
permissions inherited from Docker layers or package installations.
It effectively prevents runtime issues such as *Permission denied* when
accessing files, or non-root users unable to
execute binaries inside the container.

.. code-block:: shell

    singularity build --fix-perms image.sif docker://rockylinux:9

.. _containers-build-writable-sandbox:

Build a Writable Sandbox Container
----------------------------------

When additional development of a container is needed, a writable sandbox
may be created. The sandbox appears as a directory on the host filesystem
representing the container’s root filesystem and can be built from either
a remote repository or an existing local image:

.. code-block:: shell

   singularity build --sandbox  sandbox_dir/ docker://rockylinux:9
   singularity build --sandbox --fix-perms sandbox_dir/ docker://rockylinux:9
   singularity build --sandbox  sandbox_dir/ image.sif

This creates a directory structure under ``./mydirs`` with further nested
``bin/``, ``etc/``, ``usr/``, ``var/`` and other container directories,
emulating filesystem in user space. Note however that it does not give
*sudo/root* privileges inside the container. The container filesystem
could be accessed as other user's directories, and is not compressed,
taking more disk space than the image.

In contrary, a ``.sif`` image file has a filesystem in a compressed
read-only *SquashFS* format, efficiently storing files inside the image.
When a container image is launched in Apptainer runtime, it is mounted
using Filesystem in Userspace (FUSE) interface/tool,
``squashfuse``, that allows filesystems run in user space without
sudo/root privileges.
For a default *setuid* mode in SingularityCE runtime, the *SquashFS*
partition is mounted using kernel filesystem drivers
(``squashfs``, not using *FUSE*).  However, running SingularityCE
in the alternative/rootless mode implements *FUSE* mount with
``squashfuse``, when kernel mounts are not permitted.

No runtime mount is needed for a sandbox container, which is already
mounted during build time, and has a directory structure integrated
with the host filesystem.
This allows for faster execution and could be helpful for
development and debugging.

When using sandbox for shelling-in or running that requires writing into
the directory, use ``--writable`` option during launch, e.g.:

.. code-block:: shell

    singularity shell --writable sandbox_dir/

.. _containers-build-writable-sandbox-fakeroot:

Build a Writable Sandbox for Development (Fakeroot)
---------------------------------------------------

.. note::

    This build requires elevated sudo/root privileges when using SingularityCE

The ``--fakeroot`` option allows building a sandbox container with
emulated root privileges inside the container namespace. This enables
installation and modification steps that require elevated access,
while the user remains unprivileged on the host system. It is
particularly useful for iterative container development and debugging.

.. code-block:: shell

    singularity build --sandbox --fakeroot image/ docker://rockylinux:9

Sandbox builds may create files with restrictive permissions that cannot be
removed with ``rm``. Note the prompt warnings, such as:

.. warning::

    | WARNING: The sandbox contain files/dirs that cannot be removed with 'rm'.
    | WARNING: Use 'chmod -R u+rwX' to set permissions that allow removal.
    | WARNING: Use the '--fix-perms' option to 'apptainer build' to modify permissions at build time.

.. _containers-build-image-from-sandbox:

Build an Image from the Existing Sandbox
-------------------------------------------------

A container image could also be created from the existing sandbox. If
you used sandbox for any development, it is recommended to convert it
to ``.sif`` image for production runs and batch jobs.

.. code-block:: shell

   singularity build image.sif sandbox_dir/
   singularity build --fix-perms image.sif sandbox_dir/

.. _containers-build-from-definition file:

Build a Container from a Definition File
----------------------------------------

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

.. _containers-runtime-model:

Runtime Model
=============

The most commonly used container commands are:

.. code-block:: shell

    singularity pull ...    # convert a remote image to a local .sif file
    singularity build ...   # build an image or sandbox
    singularity shell ...   # open an interactive shell inside a container (exit with ``exit``)
    singularity run ...     # run a container using its default runscript
    singularity exec ...    # execute a specific command or application in a container

Detailed command usage is available via the built-in help system:

.. code-block:: shell

    singularity --help
    singularity exec --help

Apptainer provides the same command interface and supports the
``singularity`` command for compatibility on most systems by legacy reasons.
However, use of the ``apptainer`` command
is recommended on systems with Apptainer, which ensures consistency with
environment variable naming
(e.g., ``APPTAINERENV_*``) and avoids ambiguity when configuring or
debugging runtime behavior.

.. _containers-running:

Running Containers
------------------

Containers can be executed directly using the container runtime. The
``run`` command starts the container and executes its default runscript:

.. code-block:: shell

   singularity run image.sif

The ``run`` command always invokes the container’s predefined runscript.
Use ``exec`` to execute a different command directly
(:ref:`Executing Applications in Containers <containers-exec>`).

.. note::

    In HPC environments, container images and sandbox directories are
    typically specified using absolute paths (e.g.,
    ``/work/.../image.sif`` or ``/scratch/.../sandbox_dir``). This ensures
    that the container is accessible on all compute nodes, particularly
    in batch jobs and multi-node runs.

Additional arguments can be provided after the image name. These arguments
are passed to the container’s runscript:

.. code-block:: shell

   singularity run image.sif input.dat output.dat

For example, if the container defines a runscript such as:

.. code-block:: shell

   #!/bin/bash
   echo "Running application with arguments:"
   echo "$@"
   my_application "$@"

then the arguments are accessible within the runscript via ``$@``, and are
forwarded to the application. The output would be:

.. code-block:: shell

   Running application with arguments:
   input.dat output.dat


.. _containers-shell:

Interactive Shell in Containers
-------------------------------

To interactively explore or debug a container environment, use the
``shell`` command:

.. code-block:: shell

   singularity shell image.sif

This opens an interactive shell inside the container, where commands are
executed within the container environment while still running as processes
on the host system. The
container provides its own filesystem rooted at ``/`` (the *root*
directory), with a standard Linux directory layout (e.g., ``/bin``,
``/usr``, ``/etc``, ``/home``). Some host directories may also be visible
if they are *bind-mounted* into the container ( see :ref:`Bind Mounting Host
Directories Into a Container <containers-bind-mount-host-directories>`) .

If write access is required (e.g., for sandbox containers), use:

.. code-block:: shell

   singularity shell --writable sandbox_dir/

.. _containers-exec:

Executing Applications in Containers
------------------------------------

To execute a specific command or binary inside a container, use the
``exec`` command:

.. code-block:: shell

   singularity exec image.sif my_application

This is the most common method for running applications in batch jobs and
scripts. The specified command is executed directly within the container
environment, without invoking the container’s runscript.

Multiple commands can be executed by invoking a shell:

.. code-block:: shell

   singularity exec image.sif bash -c "command1 && command2"

In more complex workflows, a sequence of commands can be executed within
the container by invoking a shell and running a short command script. This
is commonly used to initialize the runtime environment, load modules, and
compile applications:

.. code-block:: shell

   singularity exec image.sif bash -c "
       source /usr/share/lmod/lmod/init/bash && \
       cd my_application_build && \
       module load gcc && \
       module load openmpi && \
       make -j
   "

This approach allows users to perform setup and build steps inside the
container in a non-interactive manner. Alternatively, commands can be placed
in a shell script and executed inside the container:

.. code-block:: shell

   singularity exec image.sif bash build.sh

Where ``build.sh`` contains:

.. code-block:: shell

   #!/bin/bash
   source /usr/share/lmod/lmod/init/bash
   cd my_application_build
   module load gcc
   module load openmpi
   make -j

The container exits automatically once the command sequence completes. Note
that availability of modules inside the container depends on whether
the module system is installed in the container or made available from the
host environment.

.. note::

   The ``-H`` (or ``--home``) option can be used to override the home
   directory inside the container. By default, the container uses the
   user's host ``$HOME`` directory.

   This option may be useful to isolate configuration or cache files, or
   when the default home directory is not writable. For example:

   .. code-block:: shell

      singularity exec -H /scratch/$USER image.sif my_application

    The specified directory is used as ``$HOME`` inside the container.

For parallel execution using MPI, see
:ref:`MPI Integration Models for Containers <containers-mpi-integration>`.

.. _containers-env-propagation:

Environment Variable Propagation
--------------------------------

Container runtimes such as *SingularityCE* and *Apptainer* inherit
environment variables from the host system at runtime. By default, most
variables defined in the user’s shell are available inside the container.

Environment variables inside the container may originate from the host,
the container image, or values explicitly passed at runtime. The resulting
environment is a combination of these sources, with precedence determined
by the runtime configuration.  Environment variables can also be overridden
or explicitly set at runtime, as described in the following sections.

Passing Environment Variables into Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Environment variables can be explicitly passed into a container at runtime.
This is commonly used to configure application behavior, control library
settings, or provide runtime parameters without modifying the container image.
This approach is particularly useful for passing runtime configuration
variables (e.g., MPI, network, or I/O settings) into the container.

In SingularityCE, environment variables are passed into the container by
prefixing them with ``SINGULARITYENV_``. In Apptainer, the equivalent
mechanism uses the ``APPTAINERENV_`` prefix. For example:

.. code-block:: shell

   export APPTAINERENV_MY_VAR=value
   apptainer exec image.sif env | grep MY_VAR

Inside the container, the variable is available as:

.. code-block:: shell

   MY_VAR=value

On systems where Apptainer is used, the ``APPTAINERENV_`` prefix is
recommended to ensure consistent behavior. The ``SINGULARITYENV_`` prefix
may still be supported for compatibility, particularly when using the
``singularity`` command.

.. note::

   Variables set with ``APPTAINERENV_`` or ``SINGULARITYENV_`` override
   variables defined inside the container image.

Overriding the Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``-e`` option (equivalent to ``--cleanenv``) prevents most host
environment variables from being propagated into the container. This is
useful for reducing unintended interactions with the host environment.

.. code-block:: shell

   export MY_HOST_VAR=value

   apptainer exec image.sif env | grep MY_HOST_VAR
   apptainer exec -e image.sif env | grep MY_HOST_VAR

The first command may show MY_HOST_VAR; the second usually will not,
because ``-e`` starts the container with a cleaner environment.

To pass a variable while using a clean environment and  ``--env``:

.. code-block:: shell

   apptainer exec -e --env MY_VAR=value image.sif env | grep MY_VAR

Using Environment Files
~~~~~~~~~~~~~~~~~~~~~~~

For workflows that require multiple environment variables, an environment
file can be used:

.. code-block:: shell

   apptainer exec --env-file my_env.list image.sif my_application

Where ``my_env.list`` contains:

.. code-block:: text

   VAR1=value1
   VAR2=value2

This approach is particularly useful in batch jobs and reproducible
workflows.

Environment Variables for MPI in HPC Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In HPC workflows, environment variables are often used to configure MPI
behavior, communication libraries, and network settings. These variables
can be passed into the container in the same way. For example:

.. code-block:: shell

   export APPTAINERENV_FI_PROVIDER=tcp
   export APPTAINERENV_OMPI_MCA_pml=ob1
   export APPTAINERENV_OMP_NUM_THREADS=1
   apptainer exec image.sif my_mpi_application

Inside the container, these variables are available as:

.. code-block:: shell

   FI_PROVIDER=tcp
   OMPI_MCA_pml=ob1
   OMP_NUM_THREADS=1


This approach is commonly used to control communication backends,
threading behavior, and performance tuning parameters without modifying
the container image.

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

Considerations
--------------

Environment variables play an important role in configuring application
behavior, including compiler settings, library paths, MPI configuration,
and hardware-specific options.

Users should be aware that:

- variables defined on the host may override container defaults
- missing or incorrect variables can lead to runtime failures
- MPI and communication libraries often rely on environment variables
  for correct operation

Careful management of environment variables is therefore essential for
reliable and reproducible container execution in HPC workflows.


.. _containers-mpi-integration:

MPI Integration Models
======================

Running MPI applications in containers requires coordination between
the container runtime, the MPI implementation, and the system scheduler.
SingularityCE and Apptainer support several MPI integration models
in HPC environments.

.. _containers-hybrid-mpi-model:

Hybrid MPI Model (Host + Container MPI)
---------------------------------------

This is the most common and recommended approach.

The MPI launcher (e.g., ``mpirun`` or scheduler launchers such as
``srun``) is executed on the host system and starts ranks across
compute nodes. Each rank then launches a container instance, resulting
in one container per MPI task. MPI communication uses the host system’s
communication stack (e.g., *OFI/libfabric*, *UCX*, *TCP*).

A key requirement is that the MPI library inside the container is
compatible with the host MPI at the binary (*ABI*) level.
Application Binary Interface (*ABI*) defines how compiled programs and
libraries interact, including function calls, data types, symbol names,
system calls, and linking.

Compatibility requirements depend on the launch method:

* **Host MPI launcher (``mpirun``, ``mpiexec``)**
    Requires MPI ABI compatibility
    between container and host (e.g., matching *OpenMPI* major versions
    or compatible *Intel/OneAPI MPI* ).

* **Scheduler launcher (``srun``)**
    Requires compatibility with the
    host Process Management Interface (*PMI*) or *PMIx*, which provides
    process mapping and initialization information for MPI.

.. warning::

   Mismatched MPI implementations or versions may result in runtime
   failures, hangs, or incorrect behavior.

.. _containers-host-mpi-only:

Host MPI Only (Bind) Model
--------------------------

In this model, the container does not include an MPI implementation.
Instead, the application dynamically links against MPI libraries
provided by the host system.

The MPI launcher runs on the host, and required libraries are made
available inside the container through *bind mounts*.

Key requirements:

*  The application must be compiled against an MPI ABI-compatible
   interface
*  Host MPI, fabric, and vendor libraries must be visible inside the
   container (via *bind mounts*)
*  Required environment variables (e.g., ``LD_LIBRARY_PATH``,
   ``PMI_*``, ``PMIX_*``) and fabric settings (e.g., ``FI_*``,
   ``UCX_*``) must be propagated

Advantages include smaller container images and access to optimized
vendor MPI implementations. However, this approach reduces portability
and requires careful configuration of the runtime environment.

.. _containers-full-containerized-mpi:

Fully Containerized MPI Model
-----------------------------

In this model, the MPI stack is entirely contained within the image.
The container includes:

*  MPI implementation (e.g., *Open MPI*, *MPICH*, or *Intel MPI*)
*  MPI launcher (``mpirun``, ``mpiexec``), with no intentional reliance on
   host MPI installations.
*  All required dependencies

Advantages:

*  High portability and reproducibility
*  Self-contained execution environment

Limitations:

*  Multi-node support is possible but depends on correct interaction with
   host scheduler, MPI implementation, and PMI/PMIx services
*  May require additional configuration for network fabrics
   (*InfiniBand*, etc.) and/or shared-memory transports
*  Typically less robust for large-scale, multi-node HPC workloads and
   may be sensitive to system-specific configuration

In practice, the **hybrid MPI model** provides the best balance of performance,
portability, and integration with HPC systems, and is generally recommended
for production workflows.

.. _containers-execution-workflows:

Container Execution Workflows
=============================

.. _containers-serial-execution-single-node:

Serial Execution on a Single Node
---------------------------------

Applications that do not use MPI can be executed directly inside a
container. This simple execution model is commonly used for
preprocessing, postprocessing, testing, or building applications.

.. code-block:: shell

   singularity exec -B /work /work/.../image.sif /work/.../my_application input.dat

This runs a single process without invoking MPI and can be used
interactively or within a batch job, typically without requiring
scheduler launchers (e.g., ``srun``).

.. _containers-mpi-single-node-containerized:

MPI Execution on a Single Node (Containerized)
----------------------------------------------

For multi-rank jobs, users typically run the container from a batch
script so that CPU cores and other resources are allocated by the scheduler.
For example, a small single-node *Slurm* job may look like:

.. code-block:: shell

   #!/bin/bash
   #SBATCH --job-name=container_mpi_test
   #SBATCH --nodes=1
   #SBATCH --ntasks=24
   #SBATCH --tasks-per-node=24
   #SBATCH --time=00:30:00
   #SBATCH --partition=mypartition
   #SBATCH --account=myaccount

   singularity exec -B /work /work/.../image.sif \
       mpirun -n ${SLURM_NTASKS} /work/.../my_mpi_application

This command starts one container instance and then launches multiple MPI
ranks inside that container instance on the allocated node. The number of
MPI ranks specified with ``-n`` should normally match the number of tasks
requested from the scheduler, for example ``${SLURM_NTASKS}``.

This approach is useful for single-node testing because it avoids
cross-node process launch and scheduler integration issues. However, it
assumes that the MPI launcher inside the container can correctly start and
manage all ranks on the allocated node.

For production multi-node jobs, a tighter integraion is required between
the host scheduler, the host MPI runtime, and the containerized application.
See :ref:`MPI Integration Models <containers-mpi-integration>` for the
recommended multi-node approaches.

.. _containers-compile-model:

Compiling a Model Inside a Container
------------------------------------

Containers can also be used to provide a consistent build environment for
compiling applications. In this case, the scheduler allocates CPU cores and
other resources on a compute node, and the build is executed inside the
container.

For example, a single-node *Slurm* build job may look like:

.. code-block:: shell

   #!/bin/bash
   #SBATCH --job-name=container_build_test
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=8
   #SBATCH --time=00:30:00
   #SBATCH --partition=mypartition
   #SBATCH --account=myaccount

   singularity exec -B /work /work/.../image.sif /bin/bash -c '
       source /usr/share/lmod/lmod/init/bash
       module use /work/.../modulefiles
       module load my_build_stack
       cd /work/.../my_application_build
       export BUILD_JOBS=${SLURM_CPUS_PER_TASK}
       make -j ${BUILD_JOBS}
   '

In this example, the job requests one task with four CPU cores using
--cpus-per-task=4. The build then uses those cores through
make -j ${BUILD_JOBS}. This is different from an MPI run: only one
container process is started by the batch script, and the build system
creates the parallel compilation jobs inside that container.

The exact module initialization command depends on how module environment
or Lmod is installed inside the container. Common examples include:

.. code-block:: shell

   source /usr/share/lmod/lmod/init/bash

or, on some systems:

.. code-block:: shell

   source /etc/profile.d/lmod.sh

If the container image already initializes Lmod through its shell startup
files, this step may not be required. However, explicitly initializing
Lmod in batch scripts is often clearer and more reproducible.

Alternatively, the build commands can be placed in a separate script, for
example ``build_inside_container.sh``:

.. code-block:: shell

   #!/bin/bash
   set -euo pipefail

   source /usr/share/lmod/lmod/init/bash
   module use /work/.../modulefiles
   module load my_build_stack
   cd /work/.../my_application_build
   export BUILD_JOBS=${BUILD_JOBS:-6}
   make -j ${BUILD_JOBS}

Then the batch script becomes:

.. code-block:: shell

   #!/bin/bash
   #SBATCH --job-name=container_build_test
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=6
   #SBATCH --time=00:30:00
   #SBATCH --partition=mypartition
   #SBATCH --account=myaccount

   export BUILD_JOBS=${SLURM_CPUS_PER_TASK}

   singularity exec -B /work /work/.../image.sif \
       /bin/bash /work/.../build_inside_container.sh

.. _containers-mpi-execution-multiple-nodes:

MPI Execution on Multiple Nodes Using Host MPI
----------------------------------------------

Many HPC applications are built with MPI and require coordination between the
scheduler, MPI launcher, host MPI runtime, and containerized application.

For production HPC jobs, the recommended approach is usually to let the host
scheduler and host MPI launcher start the MPI ranks, while each rank executes
the application inside the container. This is often referred to as a
*Hybrid MPI Model* (see :ref:`Hybrid MPI Model <containers-hybrid-mpi-model>`),
because the process launch is managed by the host system
while the application environment is provided by the container.

In this model:

* the scheduler allocates the nodes and tasks;
* the host MPI launcher starts the MPI ranks across the allocated nodes;
* each MPI rank starts a container instance;
* the application runs inside the container;
* MPI communication uses the configured MPI runtime and the host system's
  high-speed network when available

For example, a *Slurm* job may look like:

.. code-block:: shell

   #!/bin/bash
   #SBATCH --job-name=container_mpi_job
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=24
   #SBATCH --time=00:30:00
   #SBATCH --partition=mypartition
   #SBATCH --account=myaccount

   srun singularity exec -B /work /work/.../image.sif \
       /work/.../my_mpi_application

In this example, ``srun`` is executed on the host system. Slurm starts the MPI
tasks across the allocated nodes, and each task enters the container before
running ``my_mpi_application``. This is different from running ``mpirun`` inside
a single container instance.

On *Slurm* systems, users can check which MPI launch plugins are available on
the host system with:

.. code-block:: shell

   srun --mpi=list

The output is system dependent, but may include options such as ``pmi2``,
``pmix``, or other site-supported MPI launch interfaces.

On some *Slurm* systems, the application inside the container may use an MPI
library that was built with PMI2 support. In this case, Slurm can launch the
MPI ranks through its PMI2 interface, while each rank enters the container and
starts the MPI application. The launch line from the last example would look
like the following:

.. code-block:: shell

   srun --mpi=pmi2 singularity exec -B /work /work/.../image.sif \
       /work/.../my_mpi_application

A similar pattern can be used with other MPI launchers. For example, on systems
where ``mpirun`` or ``mpiexec`` is the recommended launcher, the job may look
like:

.. code-block:: shell

   #!/bin/bash

   mpirun -n 48 singularity exec -B /work /work/.../image.sif \
       /work/.../my_mpi_application

In this case, ``mpirun`` is executed on the host system, and each MPI rank runs
the application inside a container instance.

Users should also make sure that the required host directories are visible
inside the container. These may include application input directories, working
directories, scratch directories, and system-specific paths required by the MPI
runtime or network fabric. For example:

.. code-block:: shell

   singularity exec \
       -B /work \
       -B /scratch \
       -B /dev/infiniband \
       /work/.../image.sif \
       /work/.../my_mpi_application

The exact bind mounts and MPI options are system dependent. Some systems may
require additional host paths for MPI, network fabric, or vendor runtime
libraries. For example, Cray/HPE systems may require site-specific paths such as
``/opt/cray`` or other vendor-provided directories. Users should follow the
guidance for the target HPC platform.

This model is generally more robust for production multi-node jobs than
starting ``mpirun`` from inside the container, because the host scheduler and
host MPI runtime remain responsible for process placement, rank launch, and
network integration.

.. _containers-wrapper-scripts:

Using Wrapper Scripts to Launch Application Binaries
----------------------------------------------------

Some HPC workflows expect application binaries to be available directly in the
run directory or through the user's ``PATH``. For example, a workflow may call
an executable such as ``./fv3.exe`` from a batch script, Rocoto task, or other
workflow driver.

When the application is provided inside a container, a wrapper script can be
used in place of the application binary. The wrapper script has the same name
as the expected executable, but instead of being the real binary, it starts the
container and then runs the actual application inside the container.

This approach can be useful when:

* an existing workflow should not be modified extensively;
* the batch script or workflow driver expects a specific executable name;
* container options, bind mounts, and environment variables need to be managed
  consistently;
* the same wrapper pattern is used for several application binaries.

For example, a workflow may launch the application as:

.. code-block:: shell

   srun ./my_mpi_application

or:

.. code-block:: shell

   mpirun -n 48 ./my_mpi_application

In this case, ``./my_mpi_application`` can be a wrapper script:

.. code-block:: shell

   #!/bin/bash
   set -euo pipefail

   img="/work/.../image.sif"

   exec singularity exec \
       -B /work \
       -B /scratch \
       "${img}" \
       /work/.../bin/my_mpi_application "$@"

The ``exec`` command replaces the wrapper script process with the containerized
application process. The ``"$@"`` argument forwards all command-line arguments
from the wrapper script to the application binary inside the container.

In the above example, the host launcher starts the MPI ranks, and each MPI
rank then enters the container and runs the application binary.
This preserves the host scheduler and MPI launch behavior while keeping the
application environment inside the container.

.. note::

   The wrapper script should normally not call ``srun``, ``mpirun``, or
   ``mpiexec`` itself. For multi-node jobs, the scheduler or MPI launcher
   should call the wrapper script so that rank placement, process management,
   and
   network initialization remain under control of the host launch environment.

Container help, questions, and guidance
=======================================

The complexities involving containers, particularly MPI and containers,
can make containers difficult to use. RDHPCS system administrators and help
staff have limited knowledge on using containers on HPC systems. Open a
:ref:`help request <getting_help>` to obtain what help can be offered.
In practice, you will likely find that your fellow scientists and the
greater container communities have better knowledge for your specific
Singularity image/application.
