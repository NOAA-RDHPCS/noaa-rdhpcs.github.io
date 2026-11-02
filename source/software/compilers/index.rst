.. meta::
   :description: Overview of available compilers and MPI stacks on RDHPCS
    systems, including Intel and NVIDIA compilers with Intel MPI,
    and how to load and use them.
   :keywords: compilers, Intel, MPI, Intel MPI, NVIDIA, Fortran,
    C, C++, parallel, HPC, HPC-X

.. _compilers:

Compilers and MPI Stacks
========================

The following compilers and MPI stacks are available on RDHPCS systems:

* Compilers: Intel oneapi compilers, NVIDIA compilers from NVIDIA HPC SDK (nvhpc), GNU compilers
* MPI stacks: Intel oneapi MPI, HPCX-MPI (LTS), HPCX-MPI from NVIDIA HPC SDK (nvhpc)

Using the Intel oneapi compilers with Intel oneapi MPI
------------------------------------------------------

To see the available modules, run the  command
``module spider intel-oneapi-mpi intel-oneapi-mpi``,
which will print a list of available Intel compiler and Intel MPI modules.

Load the desired version of the module files as follows:

.. code-block:: shell

    module load intel-oneapi-compilers/<version> intel-oneapi-mpi/<version>

Then use the following commands/wrappers to compile your applications.

For non-MPI applications, use the following commands:

.. code-block:: shell

    ifx: for non-MPI Fortran applications
    icx: for non-MPI C/C++ applications


For MPI applications, use the following commands/wrappers:

.. code-block:: shell

    mpiicx: for C/C++ MPI applications
    mpiifx: for Fortran MPI applications
    mpif90 -fc=ifx:  for Fortran MPI applications


Use the man pages, or the ``--help`` option on these commands, to get more
detailed information about the options available with those commands.

Recommended Intel Compiler Options for Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following options are a starting point to optimize code. Users
should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell

   -O3 -xHOST -ip   -align array64byte
   -O3 -qopt-zmm-usage=high -axCORE-AVX512  -align array64byte -ip      # For Skylake processors (Hera)

.. note::

   Using the AVX-512 instructions may or may not improve performance. We
   recommended that you experiment with and without these options and use the
   one that performs the best.


Compiling for reproducible results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some applications may need to use the ``-fp-model`` option to obtain consistent
arithmetic results across core counts. This option better controls the order of
execution and may affect performance. See ``man ifx``; for additional
information.

.. code-block:: shell

   -fp-model strict
   -fp-model precise


Recommended Intel compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code. The
``-gen-interfaces`` can also be useful for finding errors.

.. code-block:: shell

   -O0 -g -traceback -check all -fpe0

Thread-safe compilation
^^^^^^^^^^^^^^^^^^^^^^^

If thread-safe compilation is desired, be sure to use one of the following
options (this is an issue with only Intel Fortran compiler):

.. code-block:: shell

   -qopenmp (if the source file has OpenMP directives that need to be honored)
   -recursive    # or -auto (these two are equivalent)


Other potentially useful Intel compiler options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your code has very large arrays you may see an error of the type:

.. code-block:: shell

   : relocation truncated to fit: R_X86_64_PC32 out_fem


This usually indicates very large arrays (>2GB of data section). In these
situations you will have to compile the application with the flag:

``-mcmodel=medium -static-intel``

If you use this option, keep in mind that al l dependent libraries must also be
compiled, either with this option or with ``-fpic`` option.

Run the command: ``ifx --help`` to see all the available options.

Using the NVIDIA compilers
--------------------------

The NVIDIA compilers are available on Ursa only.
To see the available versions of the NVIDIA HPC compilers, use the
command ``module spider nvhpc``.

You need to load a module for a specific version of the compiler before you are
can use that compiler: ``module load nvhpc/<version>``. Loading this module
also loads the necessary libraries and environment variables for the NVIDIA
compilers and HPCX-MPI that is provided by NVIDIA.

Then use the following commands/wrappers for compiling your applications.

For non-MPI applications:

.. code-block:: shell

   nvfortran - for Fortran sources
   nvc       - for C sources
   nvcc      - for Cuda C sources
   nvc++     - for C++ sources

For MPI applications:

.. code-block:: shell

   mpif90  - for Fortran 90 MPI sources
   mpic    - for C MPI sources
   mpicc   - for Cuda C MPI sources
   mpic++  - for C++ MPI sources

Documentation on NVIDIA compiler options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The man pages are the best resource for documentation on compiler options.
After you've loaded the modules as instructed above, run

.. code-block:: shell

   man nvfortran
   man nvcc


NVIDIA compiler options for optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for optimizing code.
Users should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell


   -O3 -fastsse -tp=sandybridge,ivybridge,haswell,skylake


NVIDIA compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code.

.. code-block:: shell

   -O0 -g -traceback -Mbounds -Mchkfpstk -Mchkptr -Mchkstk

Using the HPCX-MPI MPI implementation
-------------------------------------

The HPCX-MPI implementation is available on Ursa for use with
GNU and Intel compilers. To see the available versions of the
HPCX-MPI implementation, use the command
``module spider hpcx-mpi``.

Once the module is loaded, use the following commands/wrappers for
compiling your applications.

.. code-block:: shell

   mpif90  - for Fortran 90 MPI sources
   mpic++  - for C and C++ MPI sources
