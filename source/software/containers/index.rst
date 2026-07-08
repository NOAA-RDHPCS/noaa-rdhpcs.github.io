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


**Current Status**

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
   :alt: containers share hardware and OS kernel with the host, and are started as regular processes

   Containers share hardware and OS kernel with the host, and are started as
   regular processes.

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
   :alt: containers have their own filesystem; they interact with the host at runtime, so the container instance is viewed as a regular running application.

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
(`software <https://en.wikipedia.org/wiki/Singularity_(software)>`_ ).

In particular, *SingularityCE* `https://sylabs.io/singularity/
<https://sylabs.io/singularity/>`_ and
*Apptainer* (`https://apptainer.org/ <https://apptainer.org/>`_)
provide a container model
that operates without requiring elevated privileges, and can integrate with
HPC system architecture, batch schedulers, parallel filesystems, and
high-performance interconnects.

Both *SingularityCE* and *Apptainer* are supported on RDHPCS systems.
The table below shows the installed container software on each system
and whether module loading is needed.

.. list-table::
   :header-rows: 1
   :widths: 18 18 25

   * - RDHPCS System
     - Container software
     - Module to load
   * - Gaea
     - ``apptainer``
     - none required
   * - Hera
     - ``singularity``
     - none required
   * -
     - ``apptainer``
     - none required
   * - Mercury
     - ``singularity``
     - (?)
   * - PPAN
     - ``singularity``
     - (?)
   * - Ursa
     - ``appptainer``
     - none required
   * - Hercules/Orion
     - ``singularity``
     - ``module load singularity``
   * -
     - ``apptainer`` (*)
     - ``module load spack-managed-x86-64_v3/v1.0 apptainer``
   * - Derecho
     - ``apptainer``
     - ``module load apptainer``
   * - NOAA Cloud (PW)
     - ``singularity``
     - none required

(*) - The ``apptainer`` module on Hercules/Orion is a Spack-managed install
that loads a separate environment that may not combine well with other system
modules. The ``apptainer`` enables certain container build features that are
otherwise limited in ``singularity`` module by security constraints. The
``singularity`` module could further be used for compile and runtime
environments.


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

.. _containers-singularity-evolution:

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
  `https://www.docker.com/ <https://www.docker.com/>`_
- Docker Documentation:
  `https://docs.docker.com/ <https://docs.docker.com/>`_

- SingularityCE:
  `https://sylabs.io/singularity/ <https://sylabs.io/singularity/>`_
- SingularityCE Documentation:
  `https://docs.sylabs.io/ <https://docs.sylabs.io/>`_
  `https://docs.sylabs.io/guides/latest/user-guide/ <https://docs.sylabs.io/guides/latest/user-guide/>`_

- Apptainer:
  `https://apptainer.org/ <https://apptainer.org/>`_
- Apptainer Documentation:
  `https://apptainer.org/docs/ <https://apptainer.org/docs/>`_
  `https://apptainer.org/docs/user/latest/ <https://apptainer.org/docs/user/latest/>`_

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
(for example, through *bind mounts*) for applications that need
read/write access. This ensures consistent behavior within standard HPC
security policies.

.. _containers-differences-singularity-apptainer:

Differences Between SingularityCE and Apptainer
-----------------------------------------------

One important difference between SingularityCE and Apptainer is their default
privilege model. SingularityCE commonly uses a **setuid-root** helper
program in its default installation to perform selected container setup
operations (for example, for mount and namespace setup), while the
containerized application itself runs as the invoking user.
Apptainer is non-**setuid** by default in current versions
and normally uses unprivileged user namespaces for rootless execution.

Container build support is site- and installation-dependent for both runtimes.
Regular users can commonly pull or convert images from Docker/OCI registries
into ``.sif`` images. Building containers from definition files without
``sudo`` privileges usually requires fakeroot support, user namespace support,
and appropriate users' UID/GID mappings. Apptainer often provides a more
convenient rootless build workflow, but it is not unlimited and remains subject
to operating system support, filesystem constraints, and local HPC security
policy.

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

As with any model source code, it is the user's responsibility to download
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
restricted on NOAA RDHPC systems where SingularityCE is installed. Users can
build their own images on other platforms where Apptainer is available.

.. note::

    *Podman* program is available on PPAN / Analysis for this purpose.
    It is daemonless, open-source container engine used to build, manage,
    run, and share Open Container Initiative (OCI) containers and container
    images.

For additional details, refer to the `SingularityCE Documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_, `Apptainer
documentation <https://apptainer.org/docs/user/main/>`_, or
`Docker documentation <https://docs.docker.com/>`_. Existing
Docker images can be converted to Singularity images and then run on NOAA
RDHPC systems.


.. _containers-pull-convert-images:

Pull and Convert Docker Images to Singularity Format
----------------------------------------------------

Pull an image from DockerHub or another Open Container Initiative (OCI)
registry. This command downloads a prebuilt container image and converts
it to Singularity Image Format (.sif). Root privileges are not required.

The examples below show how to pull the latest Rocky Linux 9 image, how
to pull a generic DockerHub image using the myrepo/myimage:tag naming format,
and how to pull a custom named image from the NOAA-EPIC Docker repository.
The NOAA-EPIC image is used later in this chapter for workflow examples (See
:ref:`Container Execution Workflows <containers-execution-workflows>`).

.. code-block:: shell

    singularity pull image.sif docker://rockylinux:9
    singularity pull myimage.sif docker://myrepo/myimage:tag
    singularity pull rocky9-gnu13-ompi416.sif docker://noaaepic/rocky9-gnu:13.3.1-ompi416

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

.. _containers-build-image-noaaepic:

.. code-block:: shell

   singularity build --fix-perms rocky9-gnu13-ompi416.sif docker://noaaepic/rocky9-gnu:13.3.1-ompi416

.. _containers-build-writable-sandbox:

Build a Writable Sandbox Container
----------------------------------

When additional development of a container is needed, a writable sandbox
may be created. The sandbox appears as a directory on the host filesystem
representing the container’s root filesystem and can be built from either
a remote repository or an existing local image:

.. code-block:: shell

   singularity build --sandbox  sandbox_dir/ docker://rockylinux:9
   singularity build --sandbox  sandbox_dir/ image.sif
   singularity build --sandbox --fix-perms sandbox_dir/ docker://rockylinux:9

When the sandbox is built without the ``--fix-perms`` option (first two
command lines), builds may create files with restrictive permissions that
cannot be removed with ``rm``. Note the prompt warnings that indicate how to
address these issues, such as:

.. warning::

    | WARNING: The sandbox contain files/dirs that cannot be removed with 'rm'.
    | WARNING: Use 'chmod -R u+rwX' to set permissions that allow removal.
    | WARNING: Use the '--fix-perms' option to 'apptainer build' to modify permissions at build time.


The build of a sandbox creates a directory structure under ``./sandbox_dir``
with further nested ``bin/``, ``etc/``, ``usr/``, ``var/`` and other container
directories, emulating filesystem in user space. Note, however, that it does
not give *sudo/root* privileges inside the container. The container filesystem
can be accessed as other user's directories, and is not compressed,
taking more disk space than the container image.

In contrast, a ``.sif`` image file has a filesystem in a compressed
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
the directory, use ``--writable`` option during launch, for example:

.. code-block:: shell

   singularity shell --writable [-B dir_host:dir_container] sandbox_dir/

where the ``-B`` option is used to bind mount host directories into the
container, see :ref:`Bind Mounting Host Directories Into a Container
<containers-bind-mount-host-directories>`.

.. _containers-build-writable-sandbox-fakeroot:

Build a Writable Sandbox for Development (Fakeroot)
---------------------------------------------------

.. note::

   The ``--fakeroot`` option is supported by Apptainer. In SingularityCE,
   ``--fakeroot`` support is installation-dependent and may require
   administrator configuration of user namespaces and subordinate UID/GID
   mappings. If ``--fakeroot`` is not available, building or modifying a
   writable sandbox with SingularityCE may require elevated ``sudo`` or
   root privileges.

The ``--fakeroot`` option allows building a sandbox container with
emulated root privileges inside the container namespace. This enables
installation and modification steps that require elevated access,
while the user remains unprivileged on the host system. It is
particularly useful for iterative container development and debugging.

.. code-block:: shell

    apptainer build --sandbox --fakeroot sandbox_dir docker://rockylinux:9

.. _containers-build-image-from-sandbox:

Build an Image from the Existing Sandbox
-------------------------------------------------

A container image can also be created from the existing sandbox. If
you used the sandbox for any development, it is recommended to convert it
to a ``.sif`` image for production runs and batch jobs.

.. code-block:: shell

   singularity build --fix-perms image2.sif sandbox_dir/

.. _containers-build-from-definition-file:

Build a Container from a Definition File
----------------------------------------

A definition file describes how to build a container image. The following
basic example builds a Rocky Linux 9 SIF image and can be adapted for either
SingularityCE or Apptainer.

Building from a definition file may require elevated privileges or site
configuration, especially with SingularityCE. Apptainer often supports
unprivileged builds more directly, but availability depends on the local
installation. You may want to use ``--fix-perms`` and ``--fakeroot`` options.

.. code-block:: shell

   singularity build [--fix-perms] [--fakeroot] simple-rocky9.sif simple-rocky9.def

An example definition file, ``simple-rocky9.def``, is shown below:

.. code-block:: singularity

   Bootstrap: docker
   From: rockylinux:9

   %labels
      Author Your Name
      Version v1.0
      Description Rocky Linux 9 example container

   %runscript
      echo "Hello from Rocky Linux 9 example container"
      cat /etc/os-release

Run the resulting image with:

.. _containers-run1:

.. code-block:: shell

   singularity run simple-rocky9.sif

It will print the message from the runscript and display the contents of
``/etc/os-release`` inside the container.
Users may need to specify the full (absolute) path
to the container image and **bind mount** host directories into the container,
as described in the :ref:`Bind Mounting Host Directories Into a Container
<containers-bind-mount-host-directories>` section.

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
(for example, ``APPTAINERENV_*``) and avoids ambiguity when configuring or
debugging runtime behavior.

In simple examples below we omit binding host directories into the container
for simplicity. In practice, it is often necessary; see
:ref:`Bind Mounting Host Directories Into a Container
<containers-bind-mount-host-directories>` for details.

.. _containers-running:

Running Containers
------------------

Containers can be executed directly using the container runtime. The
``run`` command starts the container and executes its default runscript.
See the earlier :ref:`container run example <containers-run1>` for running
a container image built from a definition file. Test running another container
image built in earlier examples from the Docker image:

.. code-block:: shell

   singularity run image.sif

The resulting action will be shelling into the container as marked by
``Apptainer>`` or ``Singularity>`` prompt. Exiting the container shell
returns to the host environment.
Use ``exec`` to execute a different command directly
(:ref:`Executing Applications in Containers <containers-exec>`).

.. note::

    In HPC environments, container images and sandbox directories are
    typically specified using absolute paths (for example,
    ``/work/.../image.sif`` or ``/scratch/.../sandbox_dir``). This ensures
    that the container is accessible on all compute nodes, particularly
    in batch jobs and multi-node runs. The examples in this chapter may
    omit full paths for brevity.

Additional arguments can be provided after the image name. These arguments
are passed to the container’s runscript, as in the generic example
with a custom ``myimage.sif`` below:

.. code-block:: shell

   singularity run myimage.sif input.dat output.dat

If the container defines a runscript such as:

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

Actual testing examples for running containers with arguments are given in
the section for :ref:`Container Execution Workflows
<containers-execution-workflows>`.

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
directory), with a standard Linux directory layout (for example, ``/bin``,
``/usr``, ``/etc``, ``/home``). Some host directories may also be visible
if they are *bind-mounted* into the container ( see :ref:`Bind Mounting Host
Directories Into a Container <containers-bind-mount-host-directories>`) .

If write access is required (for example, for sandbox containers), use:

.. code-block:: shell

   singularity shell --writable sandbox_dir/

.. _containers-exec:

Executing Applications in Containers
------------------------------------

To execute a specific command or binary inside a container, use the
``exec`` command as in the generic example below:

.. code-block:: shell

   singularity exec myimage.sif my_application

This is the most common method for running applications in batch jobs and
scripts. The specified command is executed directly within the container
environment, without invoking the container’s runscript.

Multiple commands can be executed by invoking a shell:

.. code-block:: shell

   singularity exec myimage.sif bash -c "command1 && command2"

In more complex workflows, a sequence of commands can be executed within
the container by invoking a shell and running a short command script. This
is commonly used to initialize the runtime environment, load modules, and
compile applications. See examples with command scripts in section
:ref:`Container Execution Workflows <containers-execution-workflows>`.

The container exits automatically once the command sequence completes.
Availability of modules inside the container depends on whether the module
system (for example, Lmod) is installed in the container or made available from
the host environment.

.. note::

   The ``-H`` (or ``--home``) option can be used to override the home
   directory inside the container. By default, the container uses the
   user's host ``$HOME`` directory.

   This option may be useful to isolate configuration or cache files, or
   when the default home directory is not writable. For example:

   .. code-block:: shell

      singularity exec -H /scratch/$USER image.sif my_application


   The specified directory ``/scratch/$USER`` is then used as ``$HOME``
   inside the container.

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
variables (for example, MPI, network, or I/O settings) into the container.

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
Comparing the output of the following two commands illustrates the effect
of the ``-e`` option:

.. code-block:: shell

   export MY_HOST_VAR=value
   apptainer exec image.sif env | grep MY_HOST_VAR

   apptainer exec -e image.sif env | grep MY_HOST_VAR

The first command shows MY_HOST_VAR exported earlier in the host environment;
the second will not.

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

.. _containers-env-considerations:

Environment Variable Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
   singularity shell -B /scratch3 -B /scratch4 image.sif

Some host directories needed at container runtime
may have the same name as native container directories. Host directories
could then be mounted with a different name for container runtime use.
The renaming approach is as following: ``-B dir_host:dir_container``.

.. code-block:: shell

   singularity build -B /local -B /work -B /apps:/apps2 image.sif
   singularity exec -B /local -B /work -B /apps:/apps2 image.sif

In this case, ``/work`` and ``/local`` filesystem on the host system are
mounted with the same name, but host's ``/apps`` becomes ``/apps2`` inside
the runtime container. Most of the times only top-level directories
(filesystems) need to be listed to create a mount point inside the container.


The following table lists the typical bind directories for a number of NOAA
RDHPC Tier 1 platforms. These paths are to be entered each with its ``-B``
flag. The directories usually include a local filesystem hosting work
directory, any other temporary space that a system may use for building
containers, any non-standard filesystems for home directories, and any
additional filesystems that may host input data or output results.
The list is not exhaustive, and users should consult the system documentation
for additional bind mount points that may be required for specific applications
or workflows.

.. list-table:: Typical bind directories on NOAA RDHPC Tier 1 platforms
   :widths: 25 35 40
   :header-rows: 1

   * - Machine
     - Main bind directory
     - Additional bind directory
   * - Derecho
     - ``/glade``
     - none
   * - Hera/Ursa
     - ``/scratch3``
     - ``/scratch4``
   * - Gaea-C6
     - ``/gpfs``
     - ``/ncrc/home2``
   * - Hercules / Orion
     - ``/work``
     - ``/work2``, ``/local``
   * - NOAA Cloud (AWS/Azure)
     - ``/contrib``
     - ``/lustre``


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

The MPI launcher (for example, ``mpirun`` or scheduler launchers such as
``srun``) is executed on the host system and starts ranks across
compute nodes. Each rank then launches a container instance, resulting
in one container per MPI task. MPI communication uses the host system’s
communication stack (for example, *OFI/libfabric*, *UCX*, *TCP*).

A key requirement is that the MPI library inside the container is
compatible with the host MPI at the binary (*ABI*) level.
Application Binary Interface (*ABI*) defines how compiled programs and
libraries interact, including function calls, data types, symbol names,
system calls, and linking.

Compatibility requirements depend on the launch method:

* **Host MPI launcher (``mpirun``, ``mpiexec``)**
    Requires MPI ABI compatibility
    between container and host (for example, matching *Open MPI* major versions
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
*  Required environment variables (for example, ``LD_LIBRARY_PATH``,
   ``PMI_*``, ``PMIX_*``) and fabric settings (for example, ``FI_*``,
   ``UCX_*``) must be propagated

Advantages include smaller container images and access to optimized
vendor MPI implementations. However, this approach reduces portability
and requires careful configuration of the runtime environment.

.. _containers-full-containerized-mpi:

Fully Containerized MPI Model
-----------------------------

In this model, the MPI stack is entirely contained within the image.
The container includes:

*  MPI implementation (for example, *Open MPI*, *MPICH*, or *Intel MPI*)
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

The examples in this section use the container image built earlier from
the NOAA-EPIC Docker repository, ``rocky9-gnu13-ompi416.sif`` (see
:ref:`Pull and Convert Docker Images to Singularity Format
<containers-pull-convert-images>`
or :ref:`Build from a Docker Container with --fix-perms
<containers-build-image-noaaepic>`). The image contains an ``mpi-tests``
directory with simple "Hello, World"-type Fortran test programs to give
examples of different workflows and MPI integration models.
These examples demonstrate building and running a Fortran application
inside a Singularity/Apptainer container, both as a serial application
and as an MPI application on a single node or across multiple nodes.

The directory can be copied out to the user's own space, using bind
mount directories (``-B``) as required by the target system:

.. code-block:: shell

   singularity exec [-B /host_dir] rocky9-gnu13-ompi416.sif \
       cp -r /opt/mpi-tests .
   cd ./mpi-tests

The directory contains:

* ``README.md`` -- a description of the examples and instructions for running
  the tests.
* ``hello-world.f90`` -- a simple serial Fortran test program.
* ``hello-world-parallel.f90`` -- an MPI hello-world test program.
* ``Makefile`` -- builds both test executables.
* ``wrapper.sh`` -- starts the container and launches the executable
  inside it.
* ``job_card_compile`` -- builds the executables in a batch job.
* ``job_card1`` / ``job_card1_args`` -- run the MPI test on one node,
  with and without command-line arguments.
* ``job_card2`` / ``job_card2_args`` -- run the MPI test on two nodes,
  with and without command-line arguments.

The examples below assume a *Slurm* scheduler, MPI ranks launched with
``srun`` or ``mpirun``, and a working directory under ``/lustre``,
matching the NOAA AWS Cloud environment.

.. _containers-compile-application:

Compiling an Application Inside a Container
-------------------------------------------

Containers can also be used to provide a consistent build environment
for compiling applications. The ``Makefile`` in the example directory
builds both ``hello-world`` and ``hello-world-parallel`` using
``mpif90``:

.. code-block:: makefile

   EXECS     =  hello-world hello-world-parallel

   all: $(EXECS)
       rm -f *.o

   hello-world.o: hello-world.f90
       $(F90) $(FFLAGS) -c $<

   hello-world-parallel.o: hello-world-parallel.f90
       $(F90) $(FFLAGS) -c $<

   hello-world: hello-world.o
       $(F90LINKER) -o $@ $^

   hello-world-parallel: hello-world-parallel.o
       $(F90LINKER) -o $@ $^

   clean:
       rm -f *.o  $(EXECS) core


.. _containers-compile-option-a:

**Option A**. The executables can be built interactively, after starting a
shell inside the container first. Make sure to load any singularity/apptainer
modules if needed, adapt the bind mount directory (or directories),
and define the image path for your environment. For example:

.. code-block:: shell

   export img="/lustre/rocky9-gnu13-ompi416.sif"
   singularity shell -B /lustre "${img}"

After the Singularity or Apptainer prompt appears indicating a successful
shell session, initialize the module environment and load
the compiler/MPI environment as follows:

.. code-block:: shell

   singularity shell -B /lustre "${img}"
   source /usr/share/lmod/lmod/init/bash
   module use /opt/modulefiles
   module load gnu openmpi
   module list

Proceed to the test directory staged locally and build the executables
using the ``Makefile``:

.. code-block:: shell

   cd /lustre/mpi-tests
   make clean
   make

.. _containers-compile-option-b:

**Option B**. While shelled into the container as shown in Option A,
the executables can be also built without the ``Makefile``,
directly with ``mpif90``:

.. code-block:: shell

   mpif90 -o hello-world-parallel hello-world-parallel.f90
   mpif90 -o hello-world hello-world.f90

After successful compilation, exit the container shell with ``exit``
and return to the host environment to test other build methods.

.. _containers-compile-option-c:

**Option C**. A single command can be used to build the executables without
opening an interactive shell, by running several commands inside the container.

.. code-block:: shell

   singularity exec "${img}" bash -c "
      source /usr/share/lmod/lmod/init/bash && \
      cd /lustre/mpi-tests && \
      module use /opt/modulefiles && \
      module load gnu openmpi && \
      make -j
   "

Add ``-B /lustre`` or ``-B /path/to/bind/mount`` to the command line if needed
for your environment.

.. _containers-compile-option-d:

**Option D**. Note that the same set of commands can be placed inside a
script file to be executed inside the container. Such a script, named
``build.sh``, may look as follows:

.. code-block:: shell

   #!/bin/bash
   source /usr/share/lmod/lmod/init/bash
   cd /lustre/mpi-tests
   module use /opt/modulefiles
   module load gcc openmpi
   make -j

You can make it executable using ``chmod +x build.sh``. Then execute
the script inside the container with the ``exec`` command, as shown below; adjust paths
as required for your environment.

.. code-block:: shell

   singularity exec [-B /lustre] "${img}" bash build.sh

.. _containers-compile-option-e:

**Option E**. Alternatively, the build can run non-interactively in a batch
job, as shown in ``job_card_compile`` below. This example requests one node
with one task and four CPU cores, which ``make -j`` uses to build in parallel.
Adapt the SBATCH directives (at the very least, *account*, *qos*),
the image path, and the work directory as needed for your environment.
The batch script also demonstrates
how to start a container and run commands inside it, including loading modules
and building the executables.

.. code-block:: shell

   #!/bin/sh
   #SBATCH -e err
   #SBATCH -o out
   #SBATCH --account=ca-epic
   #SBATCH --qos=batch
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=4
   #SBATCH --time=00:00:30
   #SBATCH --job-name="hello-world-compile"

   img="/lustre/rocky9-gnu13-ompi416.sif"
   workdir="/lustre/mpi-tests"
   cd ${workdir}

   singularity exec -B /lustre ${img} bash -c '
      source /usr/share/lmod/lmod/init/bash
      module use /opt/modulefiles
      module load gnu openmpi
      module list
      make clean
      make -j "${SLURM_CPUS_PER_TASK}"
      '

Submit the batch compile job with the standard Slurm command:

.. code-block:: shell

   sbatch job_card_compile

In this example, the job requests one task with four CPU cores using
``--cpus-per-task=4``, which ``make -j`` uses to build in parallel. This
is different from running an MPI application: only one container process is
started by the job scheduler, and ``make`` creates the parallel build jobs
inside that container.

.. _containers-serial-single-node:

Running a Serial Application
----------------------------

Applications that do not use MPI can be executed directly inside a
container. This simple execution model is commonly used for
preprocessing, postprocessing, testing, or building applications.

The ``hello-world.f90`` program in the example directory is a minimal
serial test:

.. code-block:: fortran

   program hello_world
       implicit none

       print *, 'Hello, World!'

   end program hello_world

After building it with any method from :ref:`Compiling an Application Inside a
Container <containers-compile-application>`, you can run it either from
an interactive shell inside the container or directly from the host
environment using the ``exec`` command.

.. _containers-run-serial-option-a:

**Option A**. Start an interactive shell inside the container as during
the build, as in :ref:`Building using a container, Option A
<containers-compile-option-a>`:

.. code-block:: shell

   export img="/lustre/rocky9-gnu13-ompi416.sif"
   singularity shell -B /lustre "${img}"

Initialize Lmod module environment, load the modules, and then run the
executable from the test directory:

.. code-block:: shell

   singularity shell -B /lustre "${img}"
   source /usr/share/lmod/lmod/init/bash
   module use /opt/modulefiles
   module load gnu openmpi
   cd /lustre/mpi-tests
   ./hello-world

.. _containers-run-serial-option-b:

**Option B**. Run the executable directly from the host environment by
invoking the container with the ``exec`` command, without opening an
interactive shell, similar to the :ref:`Building using a container, Option C
<containers-compile-option-c>`:

.. code-block:: shell

   singularity exec -B /lustre "${img}" bash -c '
      source /usr/share/lmod/lmod/init/bash
      module use /opt/modulefiles
      module load gnu openmpi
      cd /lustre/mpi-tests
      ./hello-world
   '

This runs a single process without invoking MPI and can be used
interactively or within a batch job, typically without requiring
scheduler launchers (for example, ``srun``).

.. _containers-run-serial-option-c:

**Option C**. Similarly to the build example in
:ref:`Building using a container, Option D <containers-compile-option-d>`,
the commands can be placed in a script, for example, ``run.sh``, and executed
inside the container with the ``exec`` command.
A script file ``run.sh`` may look as follows:

.. code-block:: shell

   #!/bin/bash
   source /usr/share/lmod/lmod/init/bash
   module use /opt/modulefiles
   module load gnu openmpi
   cd /lustre/mpi-tests
   ./hello-world

Run the script inside the container with:

.. code-block:: shell

   singularity exec -B /lustre "${img}" bash run.sh

.. _containers-mpi-single-node-containerized:

Running an MPI Application on a Single Node (Containerized)
-----------------------------------------------------------

For multi-rank jobs involving a single node, users have options to run a
container application from the interactive container shell with or without
a script, or by submitting a batch script to the job scheduler. On most of
the NOAA RDHPC platforms, you may need to allocate a compute node for
"on the node" MPI execution using ``salloc`` command (for Slurm job
schedulers). After a compute node has been allocated, make sure to load
apptainer/singularity modules and any other modules if required.

**Option A**. Start an interactive shell inside the container as in
:ref:`Running a Serial Application, Option A
<containers-run-serial-option-a>`, and then run the MPI executable with
the ``mpirun`` invoked *inside* the container. Specify the number of ranks
with ``-n`` option. For example, to run on 8 ranks you can use:

.. code-block:: shell

   singularity shell -B /lustre "${img}"
   source /usr/share/lmod/lmod/init/bash
   module use /opt/modulefiles
   module load gnu openmpi
   cd /lustre/mpi-tests
   mpirun -n 8 ./hello-world-parallel

The output should be similar to the following, with each rank printing its own
message. The order of ranks may vary between runs:

.. code-block:: text

   nprocs,nnodes,ntpn = 8,1,8
    Hello, World! I am process           6 of           8
    Hello, World! I am process           1 of           8
    Hello, World! I am process           2 of           8
    Hello, World! I am process           3 of           8
    Hello, World! I am process           4 of           8
    Hello, World! I am process           7 of           8
    Hello, World! I am process           0 of           8
    Hello, World! I am process           5 of           8


**Option B**. Alternatively, after the compute node has been allocated and all
the necessary host system modules are loaded, you can run the MPI executable
directly from the host environment by invoking the container with the ``exec``
command, similar to the :ref:`Running a Serial Application, Option B
<containers-run-serial-option-b>`. The above example with 8 ranks can be run
as follows:

.. code-block:: shell

   singularity exec -B /lustre "${img}" bash -c '
      source /usr/share/lmod/lmod/init/bash
      module use /opt/modulefiles
      module load gnu openmpi
      cd /lustre/mpi-tests
      mpirun -n 8 ./hello-world-parallel
   '

The output should be similar to the previous example.

**Option C**. A batch job can be submitted to the scheduler with a
script so that CPU cores and other resources are allocated by the
scheduler, and ``mpirun`` is still invoked *inside* the container.
The batch script ``job_card1`` in the ``mpi-tests`` directory demonstrates
this approach for the ``hello-world-parallel`` executable. Note that the
script needs to be adapted to user's account, queue, and any other
SBATCH directives required on a particular system, besides the usual
container image path and working directory.

.. code-block:: shell

   #!/bin/sh
   #SBATCH -e err
   #SBATCH -o out
   #SBATCH --account=ca-epic
   #SBATCH --qos=batch
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=8
   #SBATCH --time=00:00:30
   #SBATCH --job-name="hello-world-parallel"

   nprocs=${SLURM_NTASKS}
   nnodes=${SLURM_NNODES}
   ntpn=${SLURM_NTASKS_PER_NODE}
   echo "nprocs,nnodes,ntpn = ${nprocs},${nnodes},${ntpn}"

   img="/lustre/rocky9-gnu13-ompi416.sif"
   workdir="/lustre/mpi-tests"

   singularity exec -B /lustre "${img}" bash -c '
      source /usr/share/lmod/lmod/init/bash
      module use /opt/modulefiles
      module load gnu openmpi
      mpirun -n "${nprocs}" "./hello-world-parallel"
      '

Submit the job with:

.. code-block:: shell

   sbatch job_card1

The ``out`` file should contain output similar to:

.. code-block:: text

   nprocs,nnodes,ntpn = 8,1,8
    Hello, World! I am process           6 of           8
    Hello, World! I am process           1 of           8
    Hello, World! I am process           2 of           8
    Hello, World! I am process           3 of           8
    Hello, World! I am process           4 of           8
    Hello, World! I am process           7 of           8
    Hello, World! I am process           0 of           8
    Hello, World! I am process           5 of           8

The order of MPI ranks may vary between runs.

Passing Arguments to the MPI Application on a Single Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A second script, ``job_card1_args`` in the ``mpi-tests`` directory, runs the
same example while passing command-line arguments to the executable, showing
that arguments given to ``mpirun`` inside the container are forwarded to each
rank. Edit the script ``job_card1_args`` shown below as in the previous example
to adapt it to your environment:

.. code-block:: shell

   #!/bin/sh
   #SBATCH -e err
   #SBATCH -o out
   #SBATCH --account=ca-epic
   #SBATCH --qos=batch
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=8
   #SBATCH --time=00:00:30
   #SBATCH --job-name="hello-world-parallel"

   nprocs=${SLURM_NTASKS}
   nnodes=${SLURM_NNODES}
   ntpn=${SLURM_NTASKS_PER_NODE}
   echo "nprocs,nnodes,ntpn = ${nprocs},${nnodes},${ntpn}"

   img="/lustre/rocky9-gnu13-ompi416.sif"
   workdir="/lustre/mpi-tests"
   cd ${workdir}

   singularity exec -B /lustre "${img}" bash -c '
      source /usr/share/lmod/lmod/init/bash
      module use /opt/modulefiles
      module load gnu openmpi
      mpirun -n "${nprocs}" "./hello-world-parallel" \
            "${nprocs}" "${nnodes}" "${ntpn}"
      '

Submit it with ``sbatch job_card1_args``. The output should be similar to the
previous example, but each rank will also print the command-line arguments
passed to it.

This approach is useful for single-node testing because it avoids
cross-node process launch and scheduler integration issues. However, it
assumes that the MPI launcher inside the container can correctly start
and manage all ranks on the allocated node.

For production multi-node jobs, a tighter integration is required
between the host scheduler, the host MPI runtime, and the containerized
application. See :ref:`MPI Integration Models <containers-mpi-integration>`
for the recommended multi-node approaches.

.. _containers-mpi-execution-multiple-nodes:

MPI Execution on Multiple Nodes Using Host MPI
----------------------------------------------

Many HPC applications are built with MPI and require coordination
between the scheduler, MPI launcher, host MPI runtime, and containerized
application.

For production HPC jobs, the recommended approach is usually to let the
host scheduler and host MPI launcher start the MPI ranks, while each
rank executes the application inside the container. This is often
referred to as a *Hybrid MPI Model* (see :ref:`Hybrid MPI Model
<containers-hybrid-mpi-model>`), because the process launch is managed
by the host system while the application environment is provided by the
container.

In this model:

* the scheduler allocates the nodes and tasks;
* the host MPI launcher (``srun``) starts the MPI ranks across the
  allocated nodes;
* each MPI rank runs a wrapper script that starts a container instance;
* the application runs inside the container;
* MPI communication uses the configured MPI runtime and the host
  system's high-speed network when available.

The two-node example uses ``job_card2`` together with the supplementary
script ``wrapper.sh``:

.. code-block:: shell

   #!/bin/sh
   #SBATCH -e err
   #SBATCH -o out
   #SBATCH --account=ca-epic
   #SBATCH --qos=batch
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=8
   #SBATCH --time=00:00:30
   #SBATCH --job-name="hello-world-parallel"

   nprocs=${SLURM_NTASKS}
   nnodes=${SLURM_NNODES}
   ntpn=${SLURM_NTASKS_PER_NODE}
   echo "nprocs,nnodes,ntpn = ${nprocs},${nnodes},${ntpn}"

   wrapper="/lustre/mpi-tests/wrapper.sh"

   srun --mpi=pmi2 -n ${nprocs} ${wrapper}

A sample ``wrapper.sh`` script sets the ``SINGULARITYENV_*`` variables needed
inside the container (``PATH``, ``LD_LIBRARY_PATH``, ``CPATH``, MPI/PMI tuning,
and the network fabric provider), then starts containers on each rank, followed
by launching the MPI executable:

.. code-block:: shell

   #!/bin/bash
   export SINGULARITYENV_FI_PROVIDER=tcp
   export SINGULARITYENV_CPATH=/opt/slurm/include:/opt/openmpi/4.1.6/include
   export SINGULARITYENV_PREPEND_PATH=/opt/openmpi/4.1.6/bin
   export SINGULARITYENV_LD_LIBRARY_PATH=/opt/slurm/lib:/opt/openmpi/4.1.6/lib:/.singularity.d/libs
   export SINGULARITYENV_LIBRARY_PATH=/opt/slurm/lib:/opt/openmpi/4.1.6/lib
   export SINGULARITYENV_PMIX_MCA_gds=hash
   export SINGULARITYENV_OMPI_MCA_btl="^openib"
   export SINGULARITYENV_OMPI_MCA_btl_tcp_if_include=eth0
   export SINGULARITYENV_OMPI_MCA_pml=ob1

   img="/lustre/rocky9-gnu13-ompi416.sif"
   cmd="/lustre/mpi-tests/hello-world-parallel"

   singularity exec -B /lustre "${img}" "${cmd}" "$@"

For *Apptainer*, use the corresponding ``APPTAINERENV_*`` variables and
replace ``singularity exec`` with ``apptainer exec``.

Submit the job with:

.. code-block:: shell

   sbatch job_card2

The expected ``out`` file should look similar to:

.. code-block:: text

   nprocs = 16
    Hello, World! I am process           0 of          16
    Hello, World! I am process           8 of          16
    Hello, World! I am process           1 of          16
    Hello, World! I am process           2 of          16
    Hello, World! I am process           5 of          16
    Hello, World! I am process           3 of          16

...and so on, with each rank printing its own message.

The rank order may vary between runs. A second script,
``job_card2_args``, passes additional command-line arguments through
``srun`` and the wrapper script to the executable running inside each
container instance.

This model is generally more robust for production multi-node jobs than
starting ``mpirun`` from inside a single container instance (see
:ref:`MPI Execution on a Single Node (Containerized)
<containers-mpi-single-node-containerized>`), because the host scheduler
and host MPI runtime remain responsible for process placement, rank
launch, and network integration.

On *Slurm* systems, users can check which MPI launch plugins are
available on the host system with:

.. code-block:: shell

   srun --mpi=list

The output is system dependent, but may include options such as
``pmi2``, ``pmix``, or other site-supported MPI launch interfaces. The
wrapper script above assumes that Slurm launches ranks through its PMI2
interface, and that Open MPI inside the container was built with PMI2
support.

.. _containers-wrapper-scripts:

Using Wrapper Scripts to Launch Application Binaries
----------------------------------------------------

Some HPC workflows expect application binaries to be available at a
fixed path or under a fixed name, for example
``${workdir}/bin/hello-world-parallel``. When the real executable is
provided inside a container, a symbolic link with the expected name can
point to a wrapper script that starts the container and then runs the
real executable inside it.

Starting from the ``wrapper.sh`` script used in the previous section,
edit it so that the command name is taken from the name used to invoke
the wrapper, and prepend the directory with the real executable to the
container's search path:

.. code-block:: shell

   cmd=$(basename "$0")
   export SINGULARITYENV_PREPEND_PATH=${workdir}

With ``${workdir}`` set to ``/lustre/mpi-tests``, create the expected
``bin`` directory and link the expected executable name to the wrapper
script:

.. code-block:: shell

   mkdir -p ${workdir}/bin
   ln -s ${workdir}/wrapper.sh ${workdir}/bin/hello-world-parallel

Then update the batch script to launch the expected executable path
instead of the wrapper directly. In ``job_card2``, replace:

.. code-block:: shell

   wrapper="/lustre/mpi-tests/wrapper.sh"
   srun --mpi=pmi2 -n ${nprocs} ${wrapper}

with:

.. code-block:: shell

   executable="/lustre/mpi-tests/bin/hello-world-parallel"
   srun --mpi=pmi2 -n ${nprocs} ${executable}

Make sure to adapt the paths of ``wrapper`` and ``executable`` variables
to your environment.

Slurm now launches ``/lustre/mpi-tests/bin/hello-world-parallel``, which
is a symbolic link to the wrapper script. The wrapper starts the
container and runs the real ``hello-world-parallel`` executable from
the container ``PATH``, producing the same output as the original
``job_card2`` example.

This approach is useful when:

* an existing workflow should not be modified extensively;
* the batch script or workflow driver expects a specific executable
  name;
* container options, bind mounts, and environment variables need to be
  managed consistently in one wrapper script;
* the same wrapper pattern is used for several application binaries.

.. note::

   The wrapper script should normally not call ``srun``, ``mpirun``, or
   ``mpiexec`` itself. For multi-node jobs, the scheduler or MPI launcher
   should call the wrapper script so that rank placement, process
   management, and network initialization remain under control of the
   host launch environment.

Container help, questions, and guidance
=======================================

The complexities involving containers, particularly MPI and containers,
can make containers difficult to use. RDHPCS system administrators and help
staff have limited knowledge on using containers on HPC systems. Open a
:ref:`help request <getting_help>` to obtain what help can be offered.
In practice, you will likely find that your fellow scientists and the
greater container communities have better knowledge for your specific
Singularity image/application.

.. note::

   The general examples shown in this chapter have been successfully tested on
   most NOAA RDHPC platforms, including Hera, Ursa, Gaea, Orion/Hercules, and
   NOAA AWS/Azure (via ParallelWorks), using the container software available
   on those platforms. Some examples, such as building a sandbox container
   and opening an interactive shell inside it, may require bind-mounting the
   corresponding host filesystems. This ensures that the expected mount-point
   directories are available inside the sandbox and helps avoid errors or
   warnings when entering the container.

   In contrast, examples for more complex workflows, such as batch scripts
   that launch containers to compile and/or run applications, are intended
   as templates for user-specific use cases. These examples should be edited
   to match the target platform, platform-specific scheduler directives,
   filesystem layout, container image, application, and site-specific
   environment.




