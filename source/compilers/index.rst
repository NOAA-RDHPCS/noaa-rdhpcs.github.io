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

**Warning:** Always compile on the login nodes. Never compile on the batch nodes.

**Note:** Gaea also has LDTN and RDTN nodes. These are for combining model output (LDTN) and data transfer (RDTN) only, not compiling. They are not Cray nodes.

============================
Compiling for Compute Nodes
===========================

Cray compute nodes are the nodes that carry out the vast majority of computations on the system. Compute nodes are running the CNL microkernel, which is markedly different than the OS running on the login and batch nodes. Your code will be built targeting the compute nodes. All parallel codes should run on the compute nodes. Compute nodes are accessible only by invoking aprun within a batch job. To build codes for the compute nodes, you should use the Cray compiler wrappers.

**Note** We highly recommend that the Cray-provided cc, CC, and ftn compiler wrappers be used when compiling and linking source code for use on the compute nodes.

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