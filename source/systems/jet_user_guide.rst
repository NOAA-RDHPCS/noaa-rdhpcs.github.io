.. _jet-user-guide:

**************
Jet User Guide
**************

.. rubric .. code-block:: shell Jet System Information

The Jet system includes several partitions that have been
installed over time. Currently Jet consists of six compute
partitions, plus four bigmem nodes, totaling 57,744 coes, @
1.884 PF.

+-------+-------+-------+-------+-------+-------+-------+-------+
| Part  | tJet  | uJet  | sJet  | vJet  | x     | b     | kJet  |
| ition |       |       |       |       | Jet\* | igmem |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Year  | 2010  | 2011  | 2012  | 2014  | 2015  | 2015  | 2018  |
|       |       |       |       |       | /2016 |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | Intel | Intel | Intel | Intel | Intel | Intel | Intel |
| Type  | Wes   | Wes   | S     | IvyB  | Ha    | Ha    | Sk    |
|       | tmere | tmere | andyB | ridge | swell | swell | ylake |
|       |       |       | ridge |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | X5650 | X5650 | X5    | E5-2  | E5-2  | E5-2  | 6148  |
| Model |       |       | -2670 | 650v2 | 670v3 | 670v3 |       |
| #     |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| CPU   | 2.66  | 2.66  | 2.6   | 2.6   | 2.3   | 2.3   | 2.4   |
| Speed | GHz   | GHz   | GHz   | GHz   | GHz   | GHz   | GHz   |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 758   | 238   | 330   | 288   | 812   | 4     | 404   |
| Nodes |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 9096  | 2856  | 5120  | 4608  | 19488 | 96    | 14400 |
| Cores |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Cores | 12    | 12    | 16    | 16    | 24    | 24    | 40    |
| /node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| M     | 2 GB  | 2 GB  | 2GB   | 4 GB  | 2.66  | 10.6  | 2.4   |
| emory |       |       |       |       | GB    | GB    | GB    |
| /Core |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| M     | 24 GB | 24 GB | 32 GB | 64 GB | 64 GB | 256   | 96 GB |
| emory |       |       |       |       |       | GB    |       |
| /Node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Avai  | 21 GB | 21 GB | 29 GB | 61 GB | 61 GB | 253   | 93 GB |
| lable |       |       |       |       |       | GB    |       |
| Mem/N |       |       |       |       |       |       |       |
| ode\* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Peak  | 127.7 | 127.7 | 332.8 | 332.8 | 883   | 883   | 2048  |
| Flops | GF    | GF    | GF    | GF    | GF    | GF    | GF    |
| /node |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Rel   | 1.00  | 1.00  | 1.44  | 1.65  | 1.5   | 1.5   | 1.68  |
| ative |       |       |       |       |       |       |       |
| Perf  |       |       |       |       |       |       |       |
| /Core |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| In    | QDR   | QDR   | QDR   | FDR   | FDR   | FDR   | EDR   |
| terco | Infin | Infin | Infin | Infin | Infin | Infin | Infin |
| nnect | iband | iband | iband | iband | iband | iband | iband |
+-------+-------+-------+-------+-------+-------+-------+-------+
| Total | 96.8  | 30.4  | 113.2 | 93.6  | 717.4 | 3.5   | 827   |
| Fl    | TF    | TF    | TF    | TF    | TF    | TF    | TF    |
| ops\* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+

.. Note .. code-block:: shell
   
Notes:

-  Jet's Front Ends (service partition) are of the same
   architecture as the xJet compute nodes.
-  Total flops is a theoretical peak and does not represent
   actual performance.
-  Relative performance is based on SPEC CPU 2017
   (specifically SPECrate 2017 Floating Point) benchmark. It
   is normalized by the slowest core in production.
-  Available Memory/Node is the total memory available to
   application. The difference between this value and the
   total available memory is due to OS overhead and other
   system buffers.

System Features:

-  Total of 55,984 cores of 64-bit Intel CPU’s,
-  Capability of 1,795 trillion floating point operations
   per second – or 1.79 petaflops,
-  Total scratch disk capacity of 6.6 Petabytes

.. rubric .. code-block:: shell File Systems

==.. rubric:: ====.. rubric:: =======
name type   size
lfs1 Lustre 3540 TB
lfs4 Lustre 4500 TB
==.. rubric:: ====.. rubric:: =======

.. rubric .. code-block:: shell NOAA Boulder RDHPCS History

For decades, NOAA weather research has relied on High Performance
Computing to further its mission of developing
leading edge weather observation and prediction
capabilities. This has been accomplished both the
development of leading edge software as well as the adoption
of cutting edge hardware technologies to push forward the
envelope of what is computationally feasible.

.. rubric .. code-block:: shell Intel Paragon
 
Intel Paragon was an early parallel system, delivered in
1991 and was used for the development of a parallel RUC
model. Researchers at GSL also developed the Scalable
Modeling System (SMS) to assist in the parallelization of
codes. To further development of parallel programming
standards GSL staff members participated in the development
of the MPI-1 and MPI-2 standards, which provided a common
basis for the parallel computational methods used today.

.. rubric .. code-block:: shell Jet

In 2000, GSL took delivery of an HPC system relying on a
relatively new concept, clustering. Very similar to a
Beowulf cluster, the system used off the shelf desktop
servers with Myrinet a high-speed, low-latency network
interconnect. This system provided substantially more
performance that the traditional architectures available at
the time in a much more cost effective manner.

Now Jet refers to any of the clustered systems that have
passed through GSL since 2000 and are used to support NOAA
Research and Development High Performance Computing (RDHPC)
requirements for GSL and other NOAA offices, including the
Hurricane Forecast Improvement Project (HFIP) since 2009. A
history of those systems:

+----------+----------+----------+-------+-------+--------+----------+
| System   | Date     | P        | Nodes | Cores | Gflops | I        |
|          |          | rocessor |       |       |        | ntegrato |
|          |          |          |       |       |        | r/Vendor |
+----------+----------+----------+-------+-------+--------+----------+
| Jet      | Jan 2000 | Compaq   | 276   | 276   | 368    | High     |
|          |          | Alpha    |       |       |        | Per      |
|          |          | 21264,   |       |       |        | formance |
|          |          | 667Mhz   |       |       |        | Tech     |
|          |          |          |       |       |        | nologies |
|          |          |          |       |       |        | Inc.     |
|          |          |          |       |       |        | (HPTi    |
|          |          |          |       |       |        | )/Compaq |
+----------+----------+----------+-------+-------+--------+----------+
| aJet     | Aug 2001 | Alpha    | 276   | 284   | 473    | HP       |
|          |          | P        |       |       |        | Ti/Alpha |
|          |          | rocessor |       |       |        | P        |
|          |          | Inc.     |       |       |        | rocessor |
|          |          | 21264,   |       |       |        | Inco     |
|          |          | 833Mhz   |       |       |        | rporated |
+----------+----------+----------+-------+-------+--------+----------+
| iJet     | Aug 2002 | Intel    | 276   | 1536  | 6758   | HP       |
|          |          | Pentium  |       |       |        | Ti/Aspen |
|          |          | 4,       |       |       |        | Systems  |
|          |          | 2.2Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| eJet     | Aug 2004 | Intel    | 276   | 598   | 3827   | HP       |
|          |          | Nocona,  |       |       |        | Ti/Aspen |
|          |          | 3.2Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| wJet     | Jan 2006 | Intel    | 276   | 1440  | 15321  | R        |
|          |          | Wo       |       |       |        | aytheon/ |
|          |          | odcrest, |       |       |        | Rackable |
|          |          | 2.66Ghz  |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| hJet     | Aug 2008 | Intel    | 276   | 2016  | 23244  | Raythe   |
|          |          | Har      |       |       |        | on/Aspen |
|          |          | pertown, |       |       |        | Systems  |
|          |          | 2.8Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| nJet     | Aug 2009 | Intel    | 448   | 3584  | 40140  | Raythe   |
|          |          | Nehalem, |       |       |        | on/Aspen |
|          |          | 2.8Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| tJet     | Aug 2010 | Intel    | 844   | 10128 | 107762 | Raythe   |
|          |          | W        |       |       |        | on/Aspen |
|          |          | estmere, |       |       |        | Systems  |
|          |          | 2.66Ghz  |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| uJet     | Aug 2011 | Intel    | 504   | 6048  | 64351  | Computer |
|          |          | W        |       |       |        | Sciences |
|          |          | estmere, |       |       |        | Cor      |
|          |          | 2.66Ghz  |       |       |        | poration |
|          |          |          |       |       |        | (CS      |
|          |          |          |       |       |        | C)/Aspen |
|          |          |          |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| sJet     | Aug 2012 | Intel    | 340   | 5440  | 113152 | C        |
|          |          | Sandy    |       |       |        | SC/Appro |
|          |          | Bridge,  |       |       |        |          |
|          |          | 2.6Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| vJet     | Aug 2014 | Intel    | 288   | 4680  | 97344  | C        |
|          |          | Ivy      |       |       |        | SC/Aspen |
|          |          | Bridge,  |       |       |        | Systems  |
|          |          | 2.6Ghz   |       |       |        |          |
+----------+----------+----------+-------+-------+--------+----------+
| xJet     | Aug 2015 | Intel    | 336   | 8064  | 296755 | C        |
|          |          | Haswell, |       |       |        | SC/Aspen |
|          |          | 2.3Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| xJet     | Aug 2016 | Intel    | 480   | 11520 | 423936 | CSRA     |
| E        |          | Haswell, |       |       |        | /Silicon |
| xpansion |          | 2.3Ghz   |       |       |        | M        |
|          |          |          |       |       |        | echanics |
+----------+----------+----------+-------+-------+--------+----------+
| kJet     | Feb 2019 | Intel    | 360   | 14400 | 754688 | CS       |
|          |          | Skylake, |       |       |        | RA/Aspen |
|          |          | 2.4Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+
| kJet exp | Dec 2019 | Intel    | 44    | 1760  | 92240  | CS       |
|          |          | Skylake, |       |       |        | RA/Aspen |
|          |          | 2.4Ghz   |       |       |        | Systems  |
+----------+----------+----------+-------+-------+--------+----------+

.. rubric:: GPU Clusters

As GSL was researching and experimenting with clustered HPC
systems in the late 1990s which drove adoption of clustered
systems in 2000, GSL is continuing to research potentially
disruptive, next generation HPC technologies. Graphical
Processing Units, GPUs, are traditionally used for graphics
and video gaming, but their design is applicable to
numerical modelling as well. Since their architecture is 
fundamentally different from traditional CPUs, existing
software usually does not run without modification.

At GSL, we have been using GPU clusters since 2009 and are
developing new tools and techniques that will allow these
systems to be used in the future by scientists to solve
tomorrow's weather and hurricane prediction challenges.

About Modules
=============
Modules is a tool that is used to manage the use of softwarewhen multiple versions are installed. For packages that arenot provided with the OS (compilers, debuggers, MPI stacks,etc), we install so that new versions to not overwrite oldversions.
By default, no modules are loaded. Therefore you must loadany modules that you wish to use. To see what modules areavailable, run:

.. code-block:: shell

   # module avail

At a minimum you will want to load a compiler and an MPIstack:

.. code-block:: shell

   # module load intel   # module load mvapich2

**Note:** Since you have to do this explicitly (for now), you also have to do it in your job scripts. Or, you can put it in your .profile and make it permanent.

.. rubric:: Modules on Jet
The way to find the latest modules on Jet is to run module avail:

 .. code-block:: shell 
    
   # module aval

to see the list of available modules for the compiler and the MPI modules currently loaded. 

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

h3a03.hera%


In the above, each module name represents a different package. In cases where there are multiple versions of a package, one will be set as a default. For example, for the intel compiler there are multiple choices:

.. code-block:: shell

   intel/11.1.080    intel/12-12.1.4(default)    intel/12-12.1.5

So if you run:

.. code-block:: shell 

   # module load intel

The default version will be loaded, in this case 12-12.1.4
If you want to load a specific version, you can. We highly recommend you use the system defaults unless something is not working or you need a different feature. To load a specific version, specify the version number.

.. code-block:: shell 

   # module load intel/11.1.080    # module list   Currently Loaded Modulefiles:    1) intel/11.1.080

If you already have a particular module loaded and you want to switch to a different version of the same module, you can either do

 .. code-block:: shell

   # module unload intel   # module load intel/11.1.080

or

 .. code-block:: shell

   # module switch intel intel/11.1.080

**Note:** When unloading modules, only unload those that you have loaded. The others are done automatically from master   modules.-  Modules is a work in progress, and we will be improving their uses and making which modules you load more clear.


Using Math Libraries
================

The intel math kernel library (MKL) provides a wide variety
of optimized math libraries including "BLAS, LAPACK,
ScaLAPACK, sparse solvers, fast Fourier transforms, vector
math, and more." The product documentation can be found `here <https://software.intel.com/en-us/articles/intel-math-kernel-library-documentation/>`__.

Below are provided several examples that should help most of
the users on our system.


.. rubric:: Location of MKL on Jet
**MKL** is specific to the version of the Intel compiler used.
After loading the compiler version you require, the variable
**$MKLROOT** will be defined that specifies the path to the
MKL library. Use this variable.

.. rubric:: Basic Linking with BLAS and LAPACK
To link with the mathematical libraries such as BLAS,
LAPACK, and the FFT routines, it is best to just add the
following option to your link line:

.. code-block:: shell

   -mkl=sequential

**Note:** There is no lower case L in front of mkl.
This will include all of the libraries you will need. The
sequential option is important because by default Intel MKL
will use threaded (OpenMP like) versions of the library. In
MPI applications you rarely want to do this. Even if you are
using OpenMP/MPI hybrids, only consider removing the
sequential option if you want the actual math routines to be
parallel, not the whole code (Ex: GFS uses OpenMP, but
relies on sequential math routines, so you would want to use
sequential for that code).

.. rubric:: Linking with FFT, and the FFTW interface
Intel provides highly optimized FFT routines within MKL.
They are documented `here <https://software.intel.com/en-us/articles/the-intel-math-kernel-library-and-its-fast-fourier-transform-routines/>`__.
While Intel has a specific interface (DFTI), we recommend
that you use the FFTW interface. `FFTW <http://www.fftw.org/>`__ is an open-source, highly
optimized FFT library, that supports many different
platforms. FFTW (specifically FFTW3 interface) can be
supported on Intel, AMD, and IBM Power architectures. IBM is
even supporting the FFTW interface through ESSL, meaning
that using the FFTW3 interface will allow codes to be
portable across the NOAA architectures.

The best reference for the fftw interface can be found `here <http://www.fftw.org/>`__. For Fortran, you need to
include the wrapper script **fftw3.f** in your source before
using the functions. Add the following statement:

.. code-block:: shell 

   include 'fftw3.f'

In the appropriate place in your source code.
When compiling, add:

.. code-block:: shell 

    '-I$(MKLROOT)/include/fftw'

to your CFLAGS and/or FFLAGS. When linking, use the steps
described above.

.. rubric:: Linking with Scalapack
Linking with Scalapack is more complicated because it uses
MPI. You have to specify which version of the MPI library
you are using when linking with Scalapack. Examples are:

.. rubric:: Linking with Scalapack and mvapich

.. code-block:: shell 

   LDFLAGS=-L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core

.. rubric:: Linking with Scalapack and OpenMPI

.. code-block:: shell 

   LDFLAGS=-L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core

In the example above, the variable $(MKLROOT) is used. Use
this variable name, not the explicit path for the Intel
compiler.

.. rubric:: Linking math libraries with Portland Group
For the PGI compiler, all you need to do is specify the
library name.

For blas:

.. code-block:: shell 

   -lblas

For lapack:

.. code-block:: shell 

   -llapack

Options for Editing on Jet
========
To use any of these editors, type the name in at the command line:

+----------+--------------------------------------------------------------+
| vi       | `<http://www.linuxlookup.com/howto/using_vi_text_editor>`_   |
|          | - The old school standard editor. It is a text based         |
|          | editor (although X window versions do exist).                |
+----------+--------------------------------------------------------------+
| emacs    | `<http://www.nedit.org/help/index.php>`_ - An editor mos t   |
|          | like what you would find in Windows.                         |
+----------+--------------------------------------------------------------+
| nedit    | `<http://www.nedit.org/help/index.php>`_ - An editor most    |
|          | like what you would find in Windows.                         |
+----------+--------------------------------------------------------------+
| nano     | It is just like nedit, easier to learn than vi, and does     |
|          | not require X11.                                             |
+----------+--------------------------------------------------------------+
| vimdiff  | extremely useful for visualizing the difference between      |
|          | source code files. It opens many files vi windows            |
|          | side-by-side and highlights any differences between the      |
|          | files. The user can edit the differences directly. Super     |
|          | useful for code development.                                 |
+----------+--------------------------------------------------------------+
| gvimdiff | X11 version of vimdiff with mouse support.                   |
+----------+--------------------------------------------------------------+


Starting a Parallel Application
================================

.. rubric:: Supported MPI Stacks

We currently support two MPI stacks on Jet,
`Mvapich2 <https://mvapich.cse.ohio-state.edu/overview/>`__
and `OpenMPI <http://www.open-mpi.org/>`__. We consider
Mvapich2 our primary MPI stack. OpenMPI is provided for
software development and regression testing. In our
experience, Mvapich2 provides better performance without
requiring tuning. We do not have the depth of staff to fully
support multiple stacks, but we will try our best. If you
feel you need to use OpenMPI as your production stack,
please send us a note through `Help
Requests <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__
and explain why so we can better understand your
requirements.

.. rubric:: Load MPI Stacks Via Modules
The MPI libraries are compiler specific. Therefore a
compiler must be loaded first before the MPI stacks become
visible.

.. code-block:: shell

   # module load intel
   # module avail

   ...
   ------------------------- /apps/Modules/default/modulefamilies/intel -- -------------------
   hdf4/4.2.7(default)      mvapich2/1.6 netcdf/3.6.3(default)    netcdf4/4.2.1.1(default)
   hdf5/1.8.9(default)      mvapich2/1.8(default)    netcdf4/4.2  openmpi/1.6.3(default)

You can see now that mvapich2 and openmpi available to be
loaded. You can load the module with command:

.. code-block:: shell

   # module load mvapich2

.. warning::
Please use the default version of the MPI stack you
require unless you are tracking down bugs or by request of
the Jet Admin staff.

.. rubric:: Launching Jobs
On Jet, please use mpiexec. This is a wrapper script that
sets up your run environment to match your batch job and use
process affinity (which provides better performance).

.. code-block:: shell

   mpiexec -np $NUM_OF_RANKS

.. rubric:: Launching MPMD jobs
MPMD (multi-program, multi-data) programs are typically used
for coupled MPI jobs, for example oceans and atmosphere.
Colons are used to separate the requirements of each launch.
For example:

.. code-block:: shell

   mpiexec -np 36 ./ocean.exe : -np 24 ./atm.exe

Of the 60 MPI ranks, the first 36 will be ocean.exe process,
and the last 24 will be the atm.exe process.

.. rubric:: MPI Library Specific Options
The MPI standard does not explicitly define how
implementations are done between the libraries. Therefore, a
single call to mpiexec can never be guaranteed to work
across different libraries. Below are the important
differences between the the ones that we support.

.. rubric:: Passing Environment Variables
There are two methods to pass variables to MPI processes,
global (-genv) and local (-env). The global ones are applied
to every executable. The local ones are only applied to the
executable specified. The two methods are the same if the
job launch is not MPMD. If you need to pass different
variables with different values to different MPMD
executables, use the local version. When using the global
versions you should put them before the -np specification as
that defines where the local parameters start.

To pass a variable with its value:

.. code-block:: shell

   -genv VARNAME=VAL

To pass multiple variables with values, list them all out:

.. code-block:: shell

   -genv VARNAME1=VAL1 -genv VARNAME2=VAL2

If the variables are already defined, then you can just pass
the list on the mpiexec line:

.. code-block:: shell

   -genvlist VARNAME1,VARNAME2

If you want to just pass the entire environment, you can
just do:

.. code-block:: shell

   -genvall

**Note:** This may have unintended consequences and may not work
depending how large your environment is. We recommend you
explicitly pass what you need to pass to the MPI processes.

If you need to pass different variables to different
processes in an MPMD configuration, an example of the syntax
would be:

.. code-block:: shell

   mpiexec -np 4 -env OMP_NUM_THREADS=2 ./ocean.exe | -np 8 -env OMP_NUM_THREADS=3 ./atm.exe

.. rubric:: OpenMPI Specific Options
.. rubric:: Passing Environment Variables
    
The option -x is used to pass variables.
To pass a variable with its value:

.. code-block:: shell

   -x VARNAME=VAL

To pass the contents of an existing variable:

.. code-block:: shell

   -x VARNAME

To pass multiple variables:

.. code-block:: shell

   -x VARNAME1,VARNAME2=VAL2,VARNAME3

When comparing this to Mvapich2, these are all local
definitions. There is no way to pass a variable to all
processes of an MPMD application with a single usage of
**-x**.



Policies and Best Practices
=========
.. rubric:: Project Data Management

`Project Data
Management <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Usage_and_Software_Support_Policies#File_System_Usage_Practices>`__
, in RDHPCS CommonDocs. This includes the High Performance
File System (HPFS, Scratch), HFS (Home File System), the
HPSS HSMS (tape).

.. rubric:: Login (Front End) Node Usage Policy
`Login (Front_End) Node Usage
Policy <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Login_(Front_End)_Node_Usage_Policy>`__
, in RDHPCS CommonDocs

.. rubric:: Cron Usage Policy
`Cron Usage
Policy <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Cron_Usage_Policy>`__
, in RDHPCS CommonDocs

.. rubric:: Maximum Job Length Policy
See the section: `Specifying a Queue
(QOS) <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php?title=Running_and_Monitoring_Jobs_on_Jet_and_Theia_-_SLURM&action=edit&section=23>`__\ for
maximum job length per partition and QOS. If you require
jobs to run longer than this, it is expected that you use
checkpoint/restart to save the state of your model. Then you
can resubmit the job and have it pickup where it left off.
This policy has been developed over a decade of different
job patterns as a balance between user needs, fairness
within the system, and reducing risk of losing too many CPU
hours from failed jobs or system interruptions.

.. rubric:: /tmp Usage Policy

Every node in the Jet system has a /tmp directory. In most
other Unix/Linux systems, users use this space used for
temporary files. This generally works when the size of /tmp
is somewhat similar to the working space (like /home) on a
traditional workstation.

However, Jet is not a workstation. The size of /tmp on Jet
is much smaller than the working space of the project
directories. In many cases, a typical file written in a
project directory could be as large as the entire /tmp
space. On the compute nodes, the problem is worse. The
compute nodes have no disk, and the size of /tmp is on the
order of 1 GB.

For these reasons:

-  Users should refrain from using /tmp. The /tmp directory
   is for system tools and processes.
-  All users have project space, use that space for
   manipulating temporary files.

The /tmp filesystem can be faster for accessing small files
there are valid reasons to use /tmp for your processing.
Only consider using /tmp if:

-  The size of your files are less than a few MB
-  Your files will not be need after the process is done
   running

Please clean up your temporary files after you are done
using them.

.. rubric:: Software Support Policy
Our goal is to enable science on any RDHPCS system. This
often includes installing additional software to improve the
utility and usefulness of the system.

.. rubric:: Systems Administrator Managed Software

The HPCS support staff is not an unlimited resource and
since every additional software package installed increases
our effort level, we have to evaluate each request. The
systems administrators will take on the responsibility of
maintaining packages based on the usefulness of the tool to
the user community, their complexity of installation and
maintenance, as well as other factors.

-  If the package is a part of the current OS base (Redhat),
   these requests will *normally be honored*

One notable exception is for 32-bit applications. 32-bit
support requires a huge increase of installed packages which
makes they system images harder to maintain and secure. We
expect all applications to work in 64-bit mode.

-  If the package is available from the `EPEL repository
   <http://fedoraproject.org/wiki/EPEL>`_, it is likely that
   we can install it unless it causes additional
   complexities. However, if EPEL stops supporting it, we
   may as well.
-  If the software is not a part of the Redhat or EPEL
   repositories, we can still consider it. Each request will
   be considered on a case by case basis based on the value
   to the community.

.. rubric:: Single-user Managed Software
Users are always free to install software packages and
maintain them in their home or project directories.

.. rubric:: "Contributor" Managed Software

We have one other method to support software on the system.
As we cannot be the experts of all system packages, we have
to rely on the community to help out to provide as much
value from the system as possible. To enable this, we have a
user contributed software section. The user will be given
access to a system level directory in which they can install
software. We will make the minimal changes necessary to
allow access to the installed tool. Any questions from the
help system that we cannot answer will be forwarded to the
package maintainer.

If you wish to contribute a package to the system, please
start a `system help ticket: <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests>`__.


System Software
============
.. rubric:: How Software is Organized Through Modules
Many software packages have compiler dependencies, and some
also have MPI stack dependencies. To ensure that the correct
packages are loaded, the module installation has been
designed so that only valid packages are presented to you.
For example, there are multiple versions of netcdf3, one for
each compiler family we have. So when you run module avail:

.. code-block:: shell

   # module avail
   
   ------------------------------ /apps/Modules/3.2.9/modulefil------------------------------------------------
   bbcp/12.01.30.01.0(default) hpssmodule-cvs      nulludunits/1.12.11
   cnvgrib/1.2.3(default)      intel/11.1.080  module-info     pgi/12.5-0(default)         udunits/2.1.24(default)
   cuda/4.2.9(default)         intel/12.1.4(default)       modules         rocoto/1.0.1(default)       use.own
   dot intel/12.1.5    ncl/6.0.0       szip/2.1        wgrib/1.8.1.0b(default)
   grads/2.0.1(default)        lahey/8.10b(default)        nco/4.1.0       totalview/8.9.2-2(default)  wgrib2/0.1.9.6a(default)

There is no option for netcdf3. However, after load a
compiler, then you have access to the packages that are
dependent on that compiler.

.. code-block:: shell

   # module load mvapich
   # module avail

   ---------------------------- /apps/Modules/default/modulefamilies/intel -------------------------------------------
   hdf4/4.2.7(default)   hdf5/1.8.9(default)   mvapich2/1.6    mvapich2/1.8(default) netcdf/3.6.3(default) netcdf4/4.2   openmpi/1.6

The same method exists for packages that are dependent on
both a compiler and MPI stack. If you wanted to use parallel
hdf5 or parallel netcdf4, you would have to first specify
the MPI stack you wanted to use.

.. code-block:: shell

   [ctierney@fe8 ~]$ module avail

   -------------------------------------- /apps/Modules/default/modulefamilies/intel-mvapich2/1.8 ----------------------
   hdf5parallel/1.8.9(default)       netcdf4-hdf5parallel/4.2(default)

.. rubric:: Environment Variables
For all packages on the system, environment variables have
been set to ensure consistency in their use. We have defined
the following variables for your use when using the
different packages on the system:

-  $NETCDF - Base directory of NetCDF3
-  $NETCDF4 - Base directory of NetCDF4
-  $NCO - Base directory of NCO
-  $HDF4 - Base directory of HDF4
-  $HDF5 - Base directory of HDF5
-  $UDUNITS - Base directory of Udunits
-  $SZIP - Base directory of szip
-  $NCARG_ROOT - Base directory of NCAR Graphics and NCL
-  $GEMPAK - Base directory of GEMPAK
-  $GEMLIB - Location of GEMPAK libraries
-  $CUDA - Base directory of Cuda
-  $GADDIR - Location of Grads libraries

When you are specifying the location of the libraries when
compiling, use the variable name. For example:

.. code-block:: shell

   icc mycode.c -o mycode -I$NETCDF/include -L$NETCDF/lib -lnetcdf

.. rubric:: User supported modules
    
Users who require access to packages not currently
supported by the HPC staff are welcome to submit requests
through the help system to install and support unique
modules. To access these user supported modules you must
first update the module path to include the
/contrib/modulefiles. To access these additional modules
execute the following commands.

.. code-block:: shell

   $ module use /contrib/modulefiles
   $ module avail

   . . .

   ----------------------------- /contrib/modulefiles -----------------------------

   anaconda/2.0.1   papi/5.3.2(default)
   ferret/v6.9(default)         sbt/0.13.7(default)
   gptl/5.3.2-mpi   scala/2.11.5(default)
   gptl/5.3.2-mpi-papi(default) tau/2.22-p1-intel(default)
   gptl/5.3.2-nompi tau/2.23-intel
   papi/4.4.0       tau/2.23.1-intel
   papi/5.0.1       test/1.0
   papi/5.3.0       tm/1.1


Using OpenMP and Hybrid OpenMP/MPI on Jet
=========
.. rubric:: Using OpenMP and Hybrid OpenMP/MPI on Jet 

`OpenMP <http://en.wikipedia.org/wiki/OpenMP OpenMP>`_ is a programming extension for supporting parallel computing in Fortran and C using shared memory. It is relative easy to parallelize code using OpenMP. However, parallelization is restricted to a single node. As any programming model, there can be tricks to make to write efficient code.

We support OpenMP on Jet, however, it is infrequently used and we have not figured out all the issues. If you want to use OpenMP, please submit a `help request <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wikis/rdhpcs-common-docs/doku.php?id=submitting_help_request>`_ and let us know so we can keep track of the users interested in using it.

.. rubric:: Compiling codes with OpenMP 

For Intel, add the option '''-openmp'''. For Portland Group, add the option '''-mp'''

.. rubric:: Specifying the Number of Threads to use 

Depending on the compiler used, the the default number of threads to use is different. Intel will use all the core available. For PGI, it will default to using 1. It is best to always explicitly set what you want. Use the OMP_NUM_THREADS variable to do this. Ex:

.. code-blocK:: shell

    setenv OMP_NUM_THREADS 4

The number you want to use would generally be the total available on a node. See the [[system_information|System Information]] page for how many cores there are on each system.

.. rubric:: Programming Tips for OpenMP ==

Do not use implicit array setting when initializing arrays in Fortran. Since memory is not allocated until it is first used, there is no way for the implicit statement to understand what to do. What this will lead to is that your program won't understand memory locality and cannot allocate memory in the 'closest' memory. This will lead to performance and scalability issues.

So, don't do this:

.. code-blocK:: shell

  A=0.

Do this:

.. code-block:: shell

 !$OMP PARALLEL DO SHARED(A)
    for j=1,n
    for i=1,m
     A(i,j)=0.
   enddo 
  enddo


This is not a Jet issue, but affects all architectures. By structuring your code in the fashion above then your code will be more portable.

.. rubric:: Using MPI calls from OpenMP critical sections ==

When using MPI and OpenMP, it is not necessary to worry about how threading is managed in MPI unless the MPI calls are from within OpenMP sections. You must disable processor affinity for this to work. To do this, you must pass the variable MV2_ENABLE_AFFINITY=0 to your application at run time. For example:

.. code-block:: shell
 
 mpiexec -v MV2_ENABLE_AFFINITY=0 ......

See the `mvapich2 documentation <https://mvapich.cse.ohio-state.edu/userguide/>`_  for more information.


Final Tuesday
========================

Known Issues
============
