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

==== ====== =======
name type   size
lfs1 Lustre 3540 TB
lfs4 Lustre 4500 TB
==== ====== =======

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
   advisor/2019         g2clib/1.4.0                intel/19.0.4.243              rocoto/1.3.1
   antlr/2.7.7          gempak/7.4.2                intelpython/3.6.8             szip/2.1
   antlr/4.2     (D)    grads/2.0.2                 matlab/R2017b                 udunits/2.1.24
   cairo/1.14.2         hpss/hpss                   nag-fortran/6.2               vtune/2019
   cnvgrib/1.4.0        idl/8.7                     nccmp/1.8.2                   wgrib/1.8.1.0b
   contrib              imagemagick/7.0.8-53        ncview/2.1.3                  xxdiff/3.2.Z1
   ferret/6.93          inspector/2019              performance-reports/19.1.1
   forge/19.1           intel/18.0.5.274     (D)    pgi/19.4

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

**Notes:** When unloading modules, only unload those that you have loaded. The others are done automatically from master   modules.-  Modules is a work in progress, and we will be improving their uses and making which modules you load more clear.


Using Math Libraries
================

The intel math kernel library (MKL) provides a wide variety
of optimized math libraries including "BLAS, LAPACK,
ScaLAPACK, sparse solvers, fast Fourier transforms, vector
math, and more." The product documentation can be found here
`<https://software.intel.com/en-us/articles/intel-math-kernel-library-documentation/>`__.

Below are provided several examples that should help most of
the users on our system.


.. rubric:: Location of MKL on Jet
MKL is specific to the version of the Intel compiler used.
After loading the compiler version you require, the variable
**$MKLROOT** will be defined that specifies the path to the
MKL library. Use this variable.

.. rubric:: Basic Linking with BLAS and LAPACK
To link with the mathematical libraries such as BLAS,
LAPACK, and the FFT routines, it is best to just add the
following option to your link line:

.. code-block:: shell

   -mkl=sequential

Note, there is no lower case L in front of mkl.
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

Editing on Jet
========



Shell & Programming Environments
================================

Compiling
=========

Running Jobs
============

Debugging
=========

Optimizing and Profiling
========================

Known Issues
============
