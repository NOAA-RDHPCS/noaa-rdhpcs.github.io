##########
Compilers
##########

.. toctree::
   :maxdepth: 2

Compiling code on Cray machines is different than compiling code for commodity or beowulf-style HPC linux clusters. Among the most prominent differences:

- Cray provides a sophisticated set of compiler wrappers to ensure that the compile environment is setup correctly. Their use is highly encouraged.
- In general, linking/using shared object libraries on compute partitions is not supported.

-----------
Available Compilers
-------------------

The following compilers are available:

- PGI, the Portland Group Compiler Suite (default) (12.5.0)
- GCC, the GNU Compiler Collection (4.7.0)
- The Cray Compiler Suite (8.1.3)
- The Intel Compiler Suite (12.1.3.293)

--------------
Cray Compiler wrappers
---------------
Cray provides a number of compiler wrappers that substitute for the traditional compiler invocation commands. The wrappers call the appropriate compiler, add the appropriate header files, and link against the appropriate libraries based on the currently loaded programming environment module. To build codes for the compute nodes, you should invoke the Cray wrappers via:

- cc To use the C compiler
- CC To use the C++ compiler
- ftn To use the FORTRAN 90 compiler

These wrappers are provided by PrgEnv-[intel|gnu|pgi|cray] modules. PrgEnv-pgi is the default module when you login to Gaea.

----------------------
Compiling and Node Types
---------------------
Cray systems are comprised of different types of nodes:

- Login nodes running traditional Linux
- Batch nodes running traditional Linux
- Compute nodes running the Cray Node Linux (CNL) microkernel
- Your code will run on these nodes

.. warning::
    Always compile on the login nodes. Never compile on the batch nodes.

.. note::
    
    Gaea also has LDTN and RDTN nodes. These are for combining model output (LDTN) and data transfer (RDTN) only, not compiling. They are not Cray nodes.

============================
Compiling for Compute Nodes
===========================

Cray compute nodes are the nodes that carry out the vast majority of computations on the system. Compute nodes are running the CNL microkernel, which is markedly different than the OS running on the login and batch nodes. Your code will be built targeting the compute nodes. All parallel codes should run on the compute nodes. Compute nodes are accessible only by invoking aprun within a batch job. To build codes for the compute nodes, you should use the Cray compiler wrappers.

.. note::
    We highly recommend that the Cray-provided cc, CC, and ftn compiler wrappers be used when compiling and linking source code for use on the compute nodes.

========================
Support for Shared Object Libraries
=================================

On Cray machines, compiled executables to be run on compute nodes must always be linked statically.

**Warning:** In general, shared object libraries are not supported on Cray compute nodes.

====================
Do Not Compile on Batch Nodes
=======================

When you log into a Cray system you are placed on a login node. When you submit a job for execution on c1/c2, your job script is launched on one of a small number of shared batch nodes. To run your application, use the Cray utility aprun. aprun will run your application on the compute nodes associated with your job. All tasks not launched through aprun will run on a batch node. Users should note that there are a small number of these login and batch nodes, and they are shared by all users. Because of this, long-running or memory-intensive work should not be performed on login nodes or batch nodes.

**Warning:** Long-running or memory-intensive codes should not be compiled for use on login nodes nor batch nodes.

**Warning:** Always compile on the login nodes. Never compile on the batch nodes.

------------------------
Controlling the Programming Environment
------------------------

Upon login, the default versions o zf the PGI compiler and associated Message Passing Interface (MPI) libraries are added to each user's environment through a programming environment module. Users do not need to make any environment changes to use the default version of PGI and MPI.

==============
Changing Compilers
==================

If a different compiler is required, it is important to use the correct environment for each compiler. To aid users in pairing the correct compiler and environment, programming environment modules are provided. The programming environment modules will load the correct pairing of compiler version, message passing libraries, and other items required to build and run. We highly recommend that the programming environment modules be used when changing compiler vendors. The following programming environment modules are available:

- PrgEnv-pgi
- PrgEnv-gnu
- PrgEnv-cray
- PrgEnv-intel

To change the default loaded PGI environment to the default version of GNU use:

.. code-block:: shell

    $ module unload PrgEnv-pgi $ module load PrgEnv-gnu
    
==============================
Changing Versions of the Same Compiler
===================================
     
To use a specific compiler version, you must first ensure the compiler's PrgEnv module is loaded, and then swap to the correct compiler version. For example, the following will configure the environment to use the GCC compilers, then load a non-default GCC compiler version:

.. code-block:: shell

    $ module swap PrgEnv-pgi PrgEnv-gnu $ module swap gcc gcc/4.6.2
    
=================
General Programming Environment Guidelines
=======================

We recommend the following general guidelines for using the programming environment modules:

- Do not purge all modules; rather, use the default module environment provided at the time of login, and modify it.
- Do not swap or unload any of the Cray provided modules (those with names like xt-*).
- Do not swap moab, torque, or MySQL modules after loading a programming environment modulefile

------------------------
Compiling Threaded Codes
-----------------------

======
OpenMP
=======

For PGI, add "-mp" to the build line:

.. code-block:: shell

    $ cc -mp test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

For Cray and GNU no additional flags are required:

.. code-block:: shell

    $ module swap PrgEnv-pgi PrgEnv-cray $ cc test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

For Intel:

.. code-block:: shell

    $ module swap PrgEnv-pgi PrgEnv-intel $ cc -openmp test.c -o test.x $ setenv OMP_NUM_THREADS 2 $ aprun -n2 -d2 ./test.x

=====
SHMEM
======

For SHMEM codes, users must load the xt-shmem module before compiling:

.. code-block:: shell

   $ module load xt-shmem