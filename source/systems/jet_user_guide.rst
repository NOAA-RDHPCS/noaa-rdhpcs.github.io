.. _jet-user-guide:

**************
Jet User Guide
**************

.. _jet-system-overview:

System Overview
===============

The Jet system includes several partitions that have been
installed over time. Currently Jet consists of six compute
partitions, plus four bigmem nodes, totaling 57,744 coes, @
1.884 PF.

+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| Partition              | tJet           | uJet           | sJet           | vJet           | xJet\*         | bigmem         | kJet           |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| Year                   | 2010           | 2011           | 2012           | 2014           | 2015/16        | 2015           | 2018           |
+========================+================+================+================+================+================+================+================+
| **CPU Type**           | Intel          | Intel          | Intel          | Intel          | Intel          | Intel          | Intel          |
|                        | Westmere       | Westmere       | SandyBridge    | IvyBridge      | Haswell        | Haswell        | Skylake        |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **CPU Model**          | X5650          | X5650          | X5-2670        | E5-2650v2      | E5-2670v3      | E5-2670v3      | 6148           |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **CPU Speed**          | 2.66 GHz       | 2.66 GHz       | 2.6 GHz        | 2.6 GHz        | 2.3 GHz        | 2.3 GHz        | 2.4 GHz        |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Total Nodes**        | 758             | 238           | 330            | 288            | 812            | 4              | 404            |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Total Cores**        | 9096           | 2856           | 5120           | 4608           | 19488          | 96             | 14400          |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Cores/node**         | 12             | 12             | 16             | 16             | 24             | 24             | 40             |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Memory/Core**        | 2 GB           | 2 GB           | 2GB            | 4 GB           | 2.66 GB        | 10.6 GB        | 2.4 GB         |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Memory/Node**        | 24 GB          | 24 GB          | 32 GB          | 64 GB          | 64 GB          | 256            | 96 GB          |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Available Mem/Node** | 21 GB          | 21 GB          | 29 GB          | 61 GB          | 61 GB          | 253            | 93 GB          |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Peak FLOPS/Node**    | 127.7 GF       | 127.7          | 332.8          | 332.8          | 883            | 883            | 2048           |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Relative Perf/Core** | 1.00           | 1.00           | 1.44           | 1.65           | 1.5            | 1.5            | 1.68           |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Interconnect**       | QDR Infiniband | QDR Infiniband | QDR Infiniband | FDR Infiniband | FDR Infiniband | FDR Infiniband | EDR Infiniband |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| **Total FLOPS** [#f1]_ | 96.8 TF        | 30.4 TF        | 113.2 TF       | 93.6 TF        | 717.4 TF       | 3.5 TF         | 827 TF         |
+------------------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+

.. [#f1] Total FLOPS is a theoretical peak and does not represent
    actual performance.

.. Note ::

   - Jet's Front Ends (service partition) are of the same architecture
     as the xJet compute nodes.
   - Relative performance is based on `SPEC CPU 2017
     <https://www.spec.org/cpu2017/>`_ (specifically SPECrate 2017
     Floating Point) benchmark. It is normalized by the slowest core
     in production.
   -  Available Memory/Node is the total memory available to
      application. The difference between this value and the total
      available memory is due to OS overhead and other system buffers.

System Features
---------------

-  Total of 55,984 cores of 64-bit Intel CPU’s,
-  Capability of 1,795 trillion floating point operations
   per second, or 1.79 petaFLOPS,
-  Total scratch disk capacity of 6.6 Petabytes

File Systems
------------

+------+--------+---------+
| Name | Type   | Size    |
+------+--------+---------+
| lfs1 | Lustre | 3540 TB |
+------+--------+---------+
| lfs4 | Lustre | 4500 TB |
+------+--------+---------+

NOAA Boulder RDHPCS History
===========================

For decades, NOAA weather research has relied on High Performance
Computing to further its mission of developing leading edge weather
observation and prediction capabilities. This has been accomplished
both the development of leading edge software as well as the adoption
of cutting edge hardware technologies to push forward the envelope of
what is computationally feasible.

Intel Paragon was an early parallel system, delivered in 1991 and was
used for the development of a parallel RUC model. Researchers at GSL
also developed the Scalable Modeling System (SMS) to assist in the
parallelization of codes. To further development of parallel
programming standards GSL staff members participated in the
development of the MPI-1 and MPI-2 standards, which provided a common
basis for the parallel computational methods used today.

In 2000, GSL took delivery of an HPC system relying on a relatively
new concept, clustering. Very similar to a Beowulf cluster, the system
used off the shelf desktop servers with Myrinet a high-speed,
low-latency network interconnect. This system provided substantially
more performance that the traditional architectures available at the
time in a much more cost effective manner.

Now Jet refers to any of the clustered systems that have passed
through GSL since 2000 and are used to support NOAA Research and
Development High Performance Computing (RDHPC) requirements for GSL
and other NOAA offices, including the Hurricane Forecast Improvement
Project (HFIP) since 2009.

GPU Clusters
------------

GSL researched and experimented with clustered HPC systems in the late
1990s, which drove adoption of clustered systems in 2000. GSL
continues to research potentially disruptive, next generation HPC
technologies. Graphical Processing Units, GPUs, are traditionally used
for graphics and video gaming, but their design is applicable to
numerical modelling as well. Since their architecture is fundamentally
different from traditional CPUs, existing software usually does not
run without modification.

At GSL, we have been using GPU clusters since 2009 and are developing
new tools and techniques that will allow these systems to be used in
the future by scientists to solve tomorrow's weather and hurricane
prediction challenges.

Modules
=======

Modules is a tool to manage the use of software when multiple versions
are installed. For packages that are not provided with the OS
(compilers, debuggers, MPI stacks,etc), we install them so that new
versions to not overwrite old versions. By default, no modules are
loaded. Therefore you must loadany modules that you wish to use. To
see what modules areavailable, run:

.. code-block:: shell

   $ module avail

At a minimum you will want to load a compiler and an MPIstack:

.. code-block:: shell

   $ module load intel
   $ module load mvapich2

.. note::

   Since you have to do this explicitly (for now), you also have to do
   it in your job scripts. Or, you can put it in your .profile and
   make it permanent.

Modules on Jet
---------------

To find the latest modules on Jet, run module avail:

.. code-block:: shell

   $ module aval

to see the list of available modules for the compiler and the MPI
modules currently loaded.

.. code-block:: shell

   --------------------------------- /apps/lmod/lmod/modulefiles/Core ---------------------------------
   lmod/7.7.18    settarg/7.7.18

   ------------------------------------ /apps/modules/modulefiles -------------------------------------
   advisor/2019         g2clib/1.4.0     intel/19.0.4.243   rocoto/1.3.1
   antlr/2.7.7          gempak/7.4.2     intelpython/3.6.8  szip/2.1
   antlr/4.2     (D)    grads/2.0.2      matlab/R2017b      udunits/2.1.24
   cairo/1.14.2         hpss/hpss        nag-fortran/6.2    vtune/2019
   cnvgrib/1.4.0        idl/8.7          nccmp/1.8.2        wgrib/1.8.1.0b
   contrib   imagemagick/7.0.8-53        ncview/2.1.3       xxdiff/3.2.Z1
   ferret/6.93          inspector/2019   performance-reports/19.1.1
   forge/19.1intel/18.0.5.274     (D)    pgi/19.4

  Where:
   D:  Default Module

   Use "module spider" to find all possible modules.
   Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

In the above, each module name represents a different package. In
cases where there are multiple versions of a package, one will be set
as a default. For example, for the intel compiler there are multiple
choices:

.. code-block:: shell

   intel/11.1.080    intel/12-12.1.4(default)    intel/12-12.1.5

So if you run:

.. code-block:: shell

   $ module load intel

The default version will be loaded, in this case 12-12.1.4 If you want
to load a specific version, you can. We highly recommend you use the
system defaults unless something is not working or you need a
different feature. To load a specific version, specify the version
number.

.. code-block:: shell

   $ module load intel/11.1.080
   $ module list
   Currently Loaded Modulefiles:
     1) intel/11.1.080

If you already have a particular module loaded and you want to switch
to a different version of the same module, you can either do

 .. code-block:: shell

   $ module unload intel
   $ module load intel/11.1.080

or

 .. code-block:: shell

   $ module switch intel intel/11.1.080

.. Note::

   When unloading modules, only unload those that you have loaded. The
   others are done automatically from master modules.  Modules is a
   work in progress, and we will be improving their uses and making
   which modules you load more clear.


Math Libraries
===============

The Intel Math Kernel Library (MKL) provides a wide variety of
optimized math libraries including BLAS, LAPACK, ScaLAPACK, sparse
solvers, fast Fourier transforms, vector math, and more.

Please refer to the `product documentation
<https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-documentation.html>`_
for information on the availale APIs.

Below are provided several examples that should help most of
the users on our system.

Location of MKL on Jet
----------------------

MKL is specific to the version of the Intel compiler used. After
loading the compiler version you require, the environment variable
``$MKLROOT`` will be defined that specifies the path to the MKL
library. Use this variable.

Linking with BLAS and LAPACK
----------------------------

To link with the mathematical libraries such as BLAS, LAPACK, and the
FFT routines, it is best to just add ``-mkl=sequential`` option to
your link line:

.. code-block:: shell

   icc ... -mkl=sequential

.. Note::

   There is no lower case L in front of mkl.  The ``-mkl`` option will
   include all of the libraries you will need. The sequential option
   is important because by default Intel MKL will use threaded (OpenMP
   like) versions of the library. In MPI applications you rarely want
   to do this. Even if you are using OpenMP/MPI hybrids, only consider
   removing the sequential option if you want the actual math routines
   to be parallel, not the whole code (Ex: GFS uses OpenMP, but relies
   on sequential math routines, so you would want to use sequential
   for that code).

Linking with FFT, and the FFTW interface
----------------------------------------

Intel provides highly optimized FFT routines within MKL. While Intel
has a specific direct Fourier Transform Interface (DFTI), we recommend
that you use the FFTW interface. `FFTW <http://www.fftw.org/>`_ is an
open-source, highly-optimized FFT library, that supports many
different platforms. FFTW (specifically the FFTW3 interface) can be
supported on Intel, AMD, and IBM Power architectures. IBM is even
supporting the FFTW interface through ESSL, meaning that using the
FFTW3 interface will allow codes to be portable across the NOAA RDHPCS
architectures.

The `FFTW orgainzation <http://www.fftw.org/>`_ has the best reference
for the FFTW interface. For Fortran, you need to ``include`` the FFTW
wrapper source ``fftw3.f`` in your source before using the functions
in the appropriate place in your source code.

.. code-block:: fortran

   include 'fftw3.f'

When compiling, add ``-I$(MKLROOT)/include/fftw`` to your ``CFLAGS``
and/or ``FFLAGS``. When linking, use the ``-mkl=sequential`` as
described above.

Linking with ScaLAPACK
----------------------

Linking with ScaLAPACK is more complicated because it uses MPI. You
have to specify which MPI library you are using when
linking.

When using the MVAPICH MPI library, use

.. code-block:: shell

   LDFLAGS=-L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core


When using the OpenMPI MPI library, use

.. code-block:: shell

   LDFLAGS=-L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core


.. note::

   Use the environment variable ``$(MKLROOT)`` and not the explicit
   path for the Intel compiler.

Linking math libraries with Portland Group
------------------------------------------

For the PGI compiler, all you need to do is specify the
library name.

For BLAS:

.. code-block:: shell

   -lblas

For LAPACK:

.. code-block:: shell

   -llapack


Starting a Parallel Application
===============================

Supported MPI Stacks
--------------------

We currently support two MPI stacks on Jet, `MVAPICH
<https://mvapich.cse.ohio-state.edu/overview/>`_ and `OpenMPI
<https://www.open-mpi.org/>`__. We consider MVAPICH our primary MPI
stack. OpenMPI is provided for software development and regression
testing. In our experience, MVAPICH provides better performance
without requiring tuning. We do not have the depth of staff to fully
support multiple stacks, but we will try our best. If you feel you
need to use OpenMPI as your production stack, please send us a note
through :ref:`Help Requests <getting_help>` and explain why so we can
better understand your requirements.

Load MPI Stacks Via Modules
---------------------------

The MPI libraries are compiler specific. Therefore a compiler must be
loaded first before the MPI stacks become visible.

.. code-block:: shell

   $ module load intel
   $ module avail

   ...
   ------------------------- /apps/Modules/default/modulefamilies/intel -- -------------------
   hdf4/4.2.7(default)      mvapich2/1.6             netcdf/3.6.3(default)    netcdf4/4.2.1.1(default)
   hdf5/1.8.9(default)      mvapich2/1.8(default)    netcdf4/4.2              openmpi/1.6.3(default)

One the compiler module is loaded, the ``mvapich2`` and ``openmpi``
modules are available to be loaded. You can load the module with
command:

.. code-block:: shell

   $ module load mvapich2

.. warning::

   Please use the default version of the MPI stack you require unless
   you are tracking down bugs or by request of the Jet admin staff.

Launching Jobs
--------------

On Jet, please use the command ``mpiexec`` to launch an MPI job. This
is a wrapper script that sets up your run environment to match your
batch job and use process affinity (which provides better
performance).

.. code-block:: shell

   $ mpiexec -np $NUM_OF_RANKS /mpi/application/to/run

Launching MPMD jobs
-------------------

MPMD (multi-program, multi-data) programs are typically used for
coupled MPI jobs, for example oceans and atmosphere. Colons are used
to separate the requirements of each launch. For example:

.. code-block:: shell

   $ mpiexec -np 36 ./ocean.exe : -np 24 ./atm.exe

Of the 60 MPI ranks, the first 36 will be for the ``ocean.exe``
process, and the last 24 will be for the ``atm.exe`` process.

MPI Library Specific Options
----------------------------

The MPI standard does not explicitly define how implementations are
done between the libraries. Therefore, a single call to ``mpiexec``
can never be guaranteed to work across different libraries. Below are
the important differences between the the ones that we support.

Passing Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MVAPICH
"""""""

There are two methods to pass variables to MPI processes, global
(``-genv``) and local (``-env``). The global ones are applied to every
executable.  The local ones are only applied to the executable
specified.  The two methods are the same if the job launch is not MPMD.
If you need to pass different variables with different values to
different MPMD executables, use the local version. When using the
global versions you should put them before the -np specification as
that defines where the local parameters start.

To pass a variable with its value:

.. code-block:: shell

   $ mpiexec -genv VARNAME=VAL ...

To pass multiple variables with values, list them all out:

.. code-block:: shell

   $ mpiexec -genv VARNAME1=VAL1 -genv VARNAME2=VAL2 ...

If the variables are already defined, then you can just pass a comma
separated list on the ``mpiexec`` line using the ``-genvlist`` option:

.. code-block:: shell

   $ mpiexec -genvlist VARNAME1,VARNAME2 ...

If you want to just pass the entire environment, you can use the
``-genvall`` option:

.. code-block:: shell

   $ mpiexec -genvall ...

.. Note::

   Passing all environment variables may have unintended consequences
   and may not work depending how large your environment is. We
   recommend you explicitly pass what you need to pass to the MPI
   processes.

If you need to pass different variables to different processes in an
MPMD configuration, an example of the syntax would be:

.. code-block:: shell

   mpiexec -np 4 -env OMP_NUM_THREADS=2 ./ocean.exe | -np 8 -env OMP_NUM_THREADS=3 ./atm.exe

OpenMPI
"""""""

The option ``-x`` is used to pass environment variables.

To pass a variable with its value:

.. code-block:: shell

   $ mpiexec -x VARNAME=VAL ...

To pass the contents of an existing variable:

.. code-block:: shell

   $ mpiexec -x VARNAME ...

To pass multiple variables, supply a comma separated list.  Variable
and value pairs can be mixed in the list:

.. code-block:: shell

   $ mpiexec -x VARNAME1,VARNAME2=VAL2,VARNAME3 ...

When comparing this to MVAPICH, these are all local definitions. There
is no way to pass a variable to all processes of an MPMD application
with a single usage of ``-x``.

Profiling Applications
======================

Application profiling is the process by which performance deficiencies
are identified in applications. Gaining this insight is the first step
to improving the performance of your code (which is always good).

If you work with any of the techniques below, please let us know how
things go so that we can improve the documentation and the process
over time.

Profiling Serial Applications
-----------------------------

The standard Linux tool, ``gprof`` can be used to obtain stastical
sampling.  Please refer to the `resources on the internet
<https://www.google.com/search?q=gprof>`_ on how to use ``gprof``.

Profiling Parallel applications
-------------------------------

Open|SpeedShop (O|SS)
^^^^^^^^^^^^^^^^^^^^^

`Open|SpeedShop (O|SS) <https://openspeedshop.org>`_ is an
open-source, multi-platform performance tool.  The O|SS page contains
the `documentation <https://openspeedshop.org/documentation/>`_, a
quick-start guide, and other tutorials.

TAU
^^^

The `TAU Performance System®
<https://www.cs.uoregon.edu/research/tau/home.php>`_ is a portable
profiling and tracing toolkit for performance analysis of parallel
programs written in Fortran, C, C++, Java, Python.  TAU Supports
application use of MPI and/or OpenMP. Portions of the TAU toolkit are
used to instrument code at compile time. Environment variables control
a number of things at runtime. A number of controls exist, permitting
users to:

-  specify which routines to instrument or to exclude
-  specify loop level instrumentation
-  instrument MPI and/or OpenMP usage
-  throttle controls to limit overhead impact of small, high
   frequency called routines
-  generate event traces
-  perform memory usage monitoring

The toolkit includes the Paraprof visualizer (a Java app) permitting
use on most desk and laptop systems (Linux, MacOS, Windows) for
viewing instumentation data. The 3D display can be very useful.
Paraprof supports the creation of user defined metrics based on the
metrics directly collected (ex: FLOPS/CYCLE).

The event traces can be displayed with the `Vampir
<https://vampir.eu/>`_, `Paraver <https://tools.bsc.es/paraver>`_, or
`Jumpshot
<https://www.anl.gov/mcs/jumpshot-performance-visualization-tool>`_
tools.

MPI and OpenMP support
""""""""""""""""""""""

TAU supports profiling of both MPI and OpenMP applications.

The Quick-start Guide mentions using
``Makefile.tau-icpc-papi-mpi-pdt``. This supports profiling of MPI
applications. You must use
``Makefile.tau-icpc-papi-mpi-pdt-openmp-opari`` for OpenMP profiling.
``Makefile.tau-icpc-papi-mpi-pdt-openmp-opari`` can be used for either
MPI or OpenMP or both.

GPTL
^^^^

`GPTL <https://jmrosinski.github.io/GPTL/>`_ is an open source
profiling package that allows for profiling both parallel and serial
applications.  It is covered by a GNU General Public License. GPTL is
an auto-instrumentation tool that can profile serial, MPI, or
MPI/OpenMP applications.

Please refer to the `GPTL Documentation
<https://jmrosinski.github.io/GPTL>`_.

The first installation supports use of the Intel Compiler and is set
not to profile MPI routines. The tool is installed in
``/contrib/GPTL/PMPINO``. A module will be generated.

Policies and Best Practices
===========================

/tmp Usage Policy
-----------------

Every node in the Jet system has a ``/tmp`` directory. In most other
Unix/Linux systems, users use this space used for temporary files.
This generally works when the size of ``/tmp`` is somewhat similar to
the working space (like ``/home``) on a traditional workstation.

However, Jet is not a workstation. The size of ``/tmp`` on Jet is much
smaller than the working space of the project directories. In many
cases, a typical file written in a project directory could be as large
as the entire ``/tmp`` space. On the compute nodes, the problem is
worse. The compute nodes have no disk, and the size of ``/tmp`` is on
the order of 1 GB.

For these reasons:

-  Users should refrain from using ``/tmp``. The ``/tmp`` directory is
   for system tools and processes.
-  All users have project space, use that space for manipulating
   temporary files.

The ``/tmp`` filesystem can be faster for accessing small files there
are valid reasons to use ``/tmp`` for your processing. Only consider
using ``/tmp`` if:

-  The size of your files are less than a few MB
-  Your files will not be need after the process is done running

Please clean up your temporary files after you are done using them.

Software Support Policy
-----------------------

Our goal is to enable science on any RDHPCS system. This often
includes installing additional software to improve the utility and
usefulness of the system.

Systems Administrator Managed Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The HPCS support staff is not an unlimited resource and since every
additional software package installed increases our effort level, we
have to evaluate each request. The systems administrators will take on
the responsibility of maintaining packages based on the usefulness of
the tool to the user community, their complexity of installation and
maintenance, as well as other factors.

-  If the package is a part of the current OS base (Redhat), these
   requests will *normally be honored*

One notable exception is for 32-bit applications. 32-bit support
requires a huge increase of installed packages which makes they system
images harder to maintain and secure. We expect all applications to
work in 64-bit mode.

-  If the package is available from the `EPEL repository
   <https://docs.fedoraproject.org/en-US/epel/>`_, it is likely that
   we can install it unless it causes additional complexities.
   However, if EPEL stops supporting it, we may as well.
-  If the software is not a part of the Redhat or EPEL repositories,
   we can still consider it. Each request will be considered on a case
   by case basis based on the value to the community.

Single-user Managed Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users are always free to install software packages and maintain them
in their home or project directories.

Contributor Managed Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have one other method to support software on the system. As we
cannot be the experts of all system packages, we have to rely on the
community to help out to provide as much value from the system as
possible. To enable this, we have a user contributed software section.
The user will be given access to a system level directory in which
they can install software. We will make the minimal changes necessary
to allow access to the installed tool. Any questions from the help
system that we cannot answer will be forwarded to the package
maintainer.

If you wish to contribute a package to the system, please open a
:ref:`system help ticket: <getting_help>`.


System Software
===============

How Software is Organized Through Modules
-----------------------------------------

Many software packages have compiler dependencies, and some also have
MPI stack dependencies. To ensure that the correct packages are
loaded, the module installation has been designed so that only valid
packages are presented to you. For example, there are multiple
versions of NetCDF, one for each compiler family we have. So when you
run module avail:

.. code-block:: shell

   $ module avail

   -------------------------------------------- /apps/Modules/3.2.9/modulefiles --------------------------------------------
   bbcp/12.01.30.01.0(default) hpssmodule-cvs        module-info         pgi/12.5-0(default)        use.own
   cnvgrib/1.2.3(default)      intel/11.1.080        modules             rocoto/1.0.1(default)      wgrib/1.8.1.0b(default)
   cuda/4.2.9(default)         intel/12.1.4(default) ncl/6.0.0           szip/2.1                   wgrib2/0.1.9.6a(default)
   dot                         intel/12.1.5          nco/4.1.0           totalview/8.9.2-2(default)
   grads/2.0.1(default)        lahey/8.10b(default)  nulludunits/1.12.11 udunits/2.1.24(default)

There is no option for netcdf3. However, after load a compiler, then
you have access to the packages that are dependent on that compiler.

.. code-block:: shell

   $ module load mvapich
   $ module avail

   --------------------- /apps/Modules/default/modulefamilies/intel --------------------
   hdf4/4.2.7(default)      mvapich2/1.6            netcdf/3.6.3(default)    openmpi/1.6
   hdf5/1.8.9(default)      mvapich2/1.8(default)   netcdf4/4.2

The same method exists for packages that are dependent on both a
compiler and MPI stack. If you wanted to use parallel HDF5 or parallel
NetCDF, you would have to first specify the MPI stack you wanted to
use.

.. code-block:: shell

   $ module avail

   --------------------- /apps/Modules/default/modulefamilies/intel-mvapich2/1.8 ---------------------
   hdf5parallel/1.8.9(default)       netcdf4-hdf5parallel/4.2(default)

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

For all packages on the system, environment variables have been set to
ensure consistency in their use. We have defined the following
variables for your use when using the different packages on the
system:

:$NETCDF: Base directory of NetCDF3
:$NETCDF4: Base directory of NetCDF4
:$NCO: Base directory of NCO
:$HDF4: Base directory of HDF4
:$HDF5: Base directory of HDF5
:$UDUNITS: Base directory of Udunits
:$SZIP: Base directory of szip
:$NCARG_ROOT: Base directory of NCAR Graphics and NCL
:$GEMPAK: Base directory of GEMPAK
:$GEMLIB: Location of GEMPAK libraries
:$CUDA: Base directory of Cuda
:$GADDIR: Location of Grads libraries

When you are specifying the location of the libraries when
compiling, use the variable name. For example:

.. code-block:: shell

   icc mycode.c -o mycode -I$NETCDF/include -L$NETCDF/lib -lnetcdf

User Supported Software
------------------------

Users who require access to packages not currently supported by the
HPC staff are welcome to submit requests through the help system to
install and support unique modules. To access these user supported
modules you must first update the module path to include the
``/contrib/modulefiles``. To access these additional modules execute
the following commands.

.. code-block:: shell

   $ module use /contrib/modulefiles
   $ module avail

   ...

   ----------------------------- /contrib/modulefiles -----------------------------

   anaconda/2.0.1               papi/5.3.2(default)
   ferret/v6.9(default)         sbt/0.13.7(default)
   gptl/5.3.2-mpi               scala/2.11.5(default)
   gptl/5.3.2-mpi-papi(default) tau/2.22-p1-intel(default)
   gptl/5.3.2-nompi             tau/2.23-intel
   papi/4.4.0                   tau/2.23.1-intel
   papi/5.0.1                   test/1.0
   papi/5.3.0                   tm/1.1


Using OpenMP and Hybrid OpenMP/MPI on Jet
=========================================

`OpenMP <https://www.openmp.org/>`_ is a programming extension for
supporting parallel computing in Fortran and C using shared memory. It
is relative easy to parallelize code using OpenMP. However,
parallelization is restricted to a single node. As any programming
model, there can be tricks to make to write efficient code.

We support OpenMP on Jet, however, it is infrequently used and we have
not figured out all the issues. If you want to use OpenMP, please
submit a :ref:`help request <getting_help>` and let us know so we can
keep track of the users interested in using it.

Compiling codes with OpenMP
---------------------------

For Intel, add the option ``-openmp``. For Portland Group, add the
option ``-mp``.

Specifying the Number of Threads to use
---------------------------------------

Depending on the compiler used, the the default number of threads to
use is different. Intel will use all the core available. PGI will
default to using 1. It is best to always explicitly set what you want.
Use the ``OMP_NUM_THREADS`` environment variable to do this. Ex:

.. tab-set::

   .. tab-item:: bash
      :sync: bash

      .. code-block:: shell

         $ export OMP_NUM_THREADS=4

   .. tab-item:: csh

      .. code-blocK:: shell

         $ setenv OMP_NUM_THREADS 4

The number you want to use would generally be the total available on a
node. Refer to the :ref:`System Information <jet-system-overview>` for
how many cores there are on each system's nodes.

Programming Tips for OpenMP
---------------------------

Do not use implicit array setting when initializing arrays in Fortran.
Since memory is not allocated until it is first used, there is no way
for the implicit statement to understand what to do. What this will
lead to is that your program won't understand memory locality and
cannot allocate memory in the 'closest' memory. This will lead to
performance and scalability issues.

So, don't do this:

.. code-blocK:: fortran

   A=0.

Do this:

.. code-block:: fortran

   !$OMP PARALLEL DO SHARED(A)
   for j=1,n
      for i=1,m
         A(i,j)=0.
      end do
   end do

This is not a Jet issue, but affects all architectures. By structuring
your code in the fashion above then your code will be more portable.

Using MPI calls from OpenMP critical sections
---------------------------------------------

When using MPI and OpenMP, it is not necessary to worry about how
threading is managed in MPI unless the MPI calls are from within
OpenMP sections. You must disable processor affinity for this to work.
To do this, you must pass the environment variable
``MV2_ENABLE_AFFINITY=0`` to your application at run time. For
example:

.. code-block:: shell

   $ mpiexec -env MV2_ENABLE_AFFINITY=0 ...

See the `MVAPICH documentation
<https://mvapich.cse.ohio-state.edu/userguide/>`_ for more
information.

Managing Packages in Contrib
============================

The system staff do not have the resources to maintain every piece of
software requested. There are also cases where developers of the
software are the system users, and putting a layer in between them and
the rest of the system users is inefficient. To support these needs,
we have developed a /contrib package process. A ``/contrib`` package
is one that is maintained by a user on the system. The system staff
are not responsible for the use or maintenance of these packages.

The system staff do not have the resources to maintain every piece of
software requested. There are also cases where developers of the
software are the system users, and putting a layer in between them and
the rest of the system users is inefficient. To support these needs,
we have developed a /contrib package process. A /contrib package is
one that is maintained by a user on the system. The system staff are
not responsible for the use or maintenance of these packages.

Responsibilities of a Contrib Package Maintainer
------------------------------------------------

Maintainers are expected to:

-  Apply security updates as quickly as possible after they become
   availble
-  Update software for bug fixes and functionality as users request
-  Respond to user email requests for help using the software

Guidelines for Contrib Packages
-------------------------------

The package should be a single program or toolset.  We want to prevent
having a single directory being a repository for many different
packages.  If you support multiple functions, please request multiple
packages.

We expect each package to be less than 100MB.  If you need more,
please tell us when you request your package. We can support larger
packages but we need to monitor the space used.

We expect each package to have less than 100 files.  If you need more,
please tell us when you request your package.

Requesting to be a Contrib Package Maintainer
---------------------------------------------

If you wish to maintain a package in contrib, please send :ref:`Help
Request <getting_help>` with:

-  a list of the packages you wish to maintain
-  justification why each is needed
-  the user who will be maintaining the package.

In certain cases, multiple users can manage a package, and Unix group
write permissions may be granted for the directory. In that case,
specify the Unix group that will be maintaining the package.

Managing a Contrib Package
--------------------------

After your request has been approved to use space in the ``/contrib``
directory, two directories will be created for you:

- ``/contrib/$MYDIR``
- ``/contrib/modulefiles/$MYDIR``

Where ``$MYDIR`` is the name of the package requested.  This is where
you will install your software for this package and optionally install
a module to allow users to load the environmental settings necessary
to use this package.

The directory convention of ``/contrib`` is designed to match that of
``/apps``. This means that one piece of software goes into a
subdirectory under the ``/contrib`` level. If you want to manage
multiple package, please request multiple ``/contrib`` package. You
can do this all at one time when submitting your Help Request.

Contrib Package Directory Naming Conventions
--------------------------------------------

When installing software into your ``/contrib`` directory, first
determine if this is software that should be versioned (multiple
versions may exist at one time) or unversioned (there will only ever
be one version installed, and upgrade will overwrite the existing
software).  For verisoned software, please install it into a
subdirectory of your package that is named after the version number.
For supporting multiple versions of software the install path should
be ``/contrib/$MYDIR/$VER``

Where ``$MYDIR`` is the directory assigned to you and ``$VER`` is the
version number. So if your package is named ``ferret``, and you are
installing the version 3.2.6, the software should be installed in
``/contrib/ferret/3.2.6``.

For supporting unversioned software, just install the software
directly into your package directory ``/contrib/$MYDIR/``.

Providing Modules to Access Contrib Installed Software
------------------------------------------------------

For each contrib package, a corresponding directory will be created
for modules. The base directory name is ``/contrib/modulefiles``. Each
package will have a subdirectory created named after the package. For
example, for the ferret package example, there will also be a directory
created named ``/contrib/modulefiles/ferret``

The ``/contrib/modulefiles`` directory will already be on the modules
path by default, so all users will be able to see the modules when
they run module list. Modules should follow the same naming convention
as the directories that contain the software. Use some name that
represents what it is (ex: tools or dat). For versioned software, the
name of the module file should be the version number (``$VER``). See
:ref:`Creating Modules for Contrib Packages
<jet-creating-modules-for-contrib-packages>` for information on how to
create modules.

.. _jet-creating-modules-for-contrib-packages:

Creating Modules for Contrib Packages
-------------------------------------

There are example modules found in
``/contrib/modulefiles.example/ferret``.  Please use those as a
template.

Contrib package maintainers must follow these conventions:

-  Modules must display the notice when loaded providing contact
   information on how to get help.
-  Module naming convention should be based on the version number of
   the software.
-  Please ask questions through via a :ref:`Help Request
   <getting_help>` regarding how to construction modules.

Specifying a Default Module
---------------------------

If you have multiple versions of a package installed, it is good
practice to set which one is the default for the user. This way, the
user does not have to explicitly specify which version they want to
load. This is done by using a file called ``.version`` that is placed
in the module directory, with the following format:

.. code-block:: tcl

   #%Module
   ##
   ## version file for default module version
   ##
   set ModulesVersion      "<default_version>"

Where ``<default_version>`` is the chosen default version for the
package.
