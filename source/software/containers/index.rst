.. _rdhpcs-containers:

**********
Containers
**********

.. note:: Current Status

    We now allow all users and projects to run `SingularityCE
    <https://sylabs.io/singularity/>`_ or `Apptainer <https://apptainer.org/>`_ Containers on Ursa, Hera,
    Jet, and Mercury. Users can build containers whereever Apptainer is installed.

    Although this allows users to run Singularity/Apptainer containers, we currently do not
    support the following items:

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
NOAA's RDHPC systems chose Singularity as the platform for users to test and
run models within Containers.

Singularity
===========

Singularity is a container solution created by necessity for scientific and
application driven workloads. It was originally developed by Lawrence Berkeley
National Laboratory (LBL).

Please note that there is a fork in the development of singularity into two
projects, `Apptainer <https://apptainer.org/>`_ and `SingularityCE`_.  Containers
built with either of the two tools are expected to work with the other tool.
SingularityCE can be invoked from the command line using the *singularity* command,
whereas Apptainer can be invoked with the *apptainer* command.
Apptainer aliases the SingularityCE command, so users can use the
`singularity` command on all RDHPCS systems without breaking their workflows.
However, there are small but important differences between Apptainer and SingularityCE. 
For convenience, when the word *Singularity* is used,
it implies either *SingularityCE* or *Apptainer* or both depending on the context.

Please refer to the `SingularityCE documentation
<https://docs.sylabs.io/guides/latest/user-guide/>`_ for additional information
than what is presented here.  The `Apptainer documentation
<https://apptainer.org/docs/user/latest/>`_ and `Docker documentation
<https://docs.docker.com/>`_ may provide useful information.

Differences between SingularityCE and Apptainer
-----------------------------------------------

The main difference is in how SingularityCE and Apptainer are installed.
SingularityCE inherited the legacy Singularity behavior and is installed
with *setuid* bit enabled. However, Apptainer by default
disables *setuid* and runs in *root-less* mode out of the box. As a result,
wherever SingularityCE is installed, container build service is disabled
for security reasons. However, users can build containers with Apptainer out of the box.


Additional differences arise when users try to run MPI applications through
containers. An Apptainer MPI task is not allowed to access the memory
associated with the other MPI tasks, so direct copying of memory is not
possible with Apptainer in the default mode. For newer versions of Apptainer,
this limitation is eased by specifying a flag. When older versions of Apptainer
are deployed, users have to resort to specifying MPI options that disable
features such as Cross Memory Attach. If using OpenMPI or HPCX, it can be
accomplished by disabling *vader* shared memory transport mechanism for single
node jobs. Similar workarounds are needed in other cases.


Either SingularityCE or Apptainer is deployed on a RDHPCS system.
The below table shows the installed software on the RDHPCS systems.

=============  =============  =========
RDHPCS System  SingularityCE  Apptainer
=============  =============  =========
Gaea           No             Yes
Hera           Yes            No
Jet            Yes            No
Mercury        Yes            No
PPAN           Yes            No
Ursa           No             Yes
=============  =============  =========

.. _containers-limitation-exception-liability:

Limitation, Exception and Liability
-----------------------------------

One such exception in regards to software dependencies issues, is
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
  have to create the images outside of RDHPCS and copy them to the R&D
  HPC systems to run with Singularity.

It is user's responsibility to make sure that the images
downloaded from internet or created by the user will not violate the
NOAA RDHPCS security policy.

..
  ** Not true anymore **
  By default, RDHPCS firewall block access to external Container
  repositories. If you would like to request access to an external
  repository, please submit a help ticket.


.. _containers-singularity:


How to create images
--------------------

Creating images from SingularityCE needs superuser permissions. For
security reasons, this service is not currently allowed on NOAA's R&D HPC
systems, where SingularityCE is installed. 
Users either need to download available images online or build their
own images on other platforms, where Apptainer is installed. For
image building, please refer to the related documents for `Singularity
<https://docs.sylabs.io/guides/latest/user-guide/>`_  or `Docker <Docker documentation_>`_. Existing
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
done with Singularity using ``singularity build lolcow.sif
shub://GodloveD/lolcow`` where ``lolcow.sif`` is the name of the Singularity
image file, and ``shub://GodloveD/lolcow`` is the Singularity Hub container to
download.


Convert Docker container to Singularity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can convert Docker containers to a Singularity image and then run it on R&D
HPC systems. 

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

If you already have the image files on other machines, you can simply
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
all required libraries and library headers.  An easy way to accomplish this, is
to launch an interactive shell in the container, and build the model as is
typically done on any system.

.. code-block:: shell

    $ singularity shell container.sif

Using a container to run a parallel job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example Slurm run script to run the wrf model with 512 MPI tasks. In
this example, the :file:`wrf.exe` executable is compiled on the host machine using 
the :file:`hydro.sif` container.  The :file:`wrf.exe` and :file:`hydro.sif`
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


    srun singularity exec hydro.sif ./wrf.exe

.. note::

    The :file:`hydro.sif` and :file:`wrf.exe` are under the same directory.
    Under the running directory, you will not have the soft links from other
    directories.

Container help, questions, and guidance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The complexities involving containers, particularly MPI and containers, can make 
containers difficult to use. RDHPCS system administrators and help staff have limited knowledge on
using containers on HPC systems.  Open a :ref:`help request <getting_help>` to
what help can be offered.  However, you will likely find your fellow scientists
and the greater container communities have better knowledge for your specific
Singularity image/application.
