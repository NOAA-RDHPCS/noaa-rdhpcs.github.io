*******************
General Information
*******************

Welcome to RDHPCS CommonDocs -- Information and procedures that
pertain across all RDHPCS systems.

The RDHPCS Maintenance Downtime Calendar has events for NESCC (Hera,
HPSS, Niagara), Jet, Boulder and Princeton Bastions, and other RDHPCS
system downtimes. `View the Calendar
<https://calendar.google.com/calendar/u/1/r?id=bm9hYS5nb3ZfZjFnZ3U0M3RtOWxmZWVnNDV0NTlhMDYzY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ>`__

.. raw:: html

   <div>
   <iframe src="https://calendar.google.com/calendar/embed?src=noaa.gov_f1ggu43tm9lfeeg45t59a063cs%40group.calendar.google.com&ctz=America%2FNew_York"
           style="border: 0"
           width="800"
           height="600"
           frameborder="0"
           scrolling="no"></iframe>
   <p>You must be logged in to your NOAA Gmail account to see the calendar.</p>
   </div>



Locations and Systems of the RDHPCS
===================================

The `NOAA Information Technology Locations and Systems page
<https://www.noaa.gov/organization/information-technology/hpcc-locations-and-systems>`_
gives sone high technical and geographical information about NOAA's High
Performance Computing program.

.. |hpcc_gaea_url|	replace:: https://www.noaa.gov/organization/information-technology/gaea
.. |hpcc_hera_url|	replace:: https://www.noaa.gov/organization/information-technology/hera
.. |hpcc_jet_url|	replace:: https://www.noaa.gov/organization/information-technology/jet
.. |hpcc_niagara_url|	replace:: https://www.noaa.gov/organization/information-technology/niagara
.. |hpcc_cloud_url|	replace:: https://www.noaa.gov/information-technology/hpcc
.. |hpcc_orion_url|	replace:: https://www.noaa.gov/organization/information-technology/orion
.. |gaeaP|		replace:: Climate Modeling and Research System (CMRS) at Oak Ridge National Laboratory
.. |heraP|		replace:: Predicting high-impact weather events
.. |jetP|		replace:: Hurricane Forecast Improvement Program (HFIP)
.. |niagaraP|		replace:: Collaborative resource for data transfer
.. |cloudP|		replace:: Platforms to create and use HPC computatational clusters on an ad-hoc basis
.. |msuP|		replace:: Collaboration with Mississippi State University (MSU)


+---------------+-------------+-------------------+-------------------------+
| RDHPCS System |  Purpose    | OCIO HPCC Info    | RDHPCS Documentation    |
+---------------+-------------+-------------------+-------------------------+
| Gaea          | |gaeaP|     | |hpcc_gaea_url|   |:ref:`gaea-user-guide`   |
+---------------+-------------+-------------------+-------------------------+
| Hera          | |heraP|     | |hpcc_hera_url|   |:ref:`hera-user-guide`   |
+---------------+-------------+-------------------+-------------------------+
| Jet           | |jetP|      | |hpcc_jet_url|    |:ref:`jet-user-guide`    |
+---------------+-------------+-------------------+-------------------------+
| Niagara       | |niagaraP|  | |hpcc_niagara_url||:ref:`niagara-user-guide`|
+---------------+-------------+-------------------+-------------------------+
| Cloud         | |cloudP|    | |hpcc_cloud_url|  |:ref:`cloud-user-guide`  |
+---------------+-------------+-------------------+-------------------------+
| MSU-HPC Orion | |msuP|      | |hpcc_orion_url|  |:ref:`MSU-HPC-user-guide`|
+---------------+-------------+-------------------+-------------------------+

Bastion Hostnames
=================


.. |CBHN|	replace:: **CAC Bastion hostnames**
.. |RBHN|	replace:: **RSA Bastion hostnames**
.. |GCPRNG|	replace:: gaea.princeton.rdhpcs.noaa.gov
.. |GCBRNG|	replace:: gaea.boulder.rdhpcs.noaa.gov
.. |GRPRNG|	replace:: gaea-rsa.princeton.rdhpcs.noaa.gov
.. |GRBRNG|	replace:: gaea-rsa.boulder.rdhpcs.noaa.gov

.. |HCPRNG|	replace:: hera.princeton.rdhpcs.noaa.gov
.. |HCBRNG|	replace:: hera.boulder.rdhpcs.noaa.gov
.. |HRPRNG|	replace:: hera-rsa.princeton.rdhpcs.noaa.gov
.. |HRBRNG|	replace:: hera-rsa.boulder.rdhpcs.noaa.gov

.. |JCPRNG|	replace:: jet.princeton.rdhpcs.noaa.gov
.. |JCBRNG|	replace:: jet.boulder.rdhpcs.noaa.gov
.. |JRPRNG|	replace:: jet-rsa.princeton.rdhpcs.noaa.gov
.. |JRBRNG|	replace:: jet-rsa.boulder.rdhpcs.noaa.gov

.. |NCPRNG|	replace:: niagara.princeton.rdhpcs.noaa.gov
.. |NCBRNG|	replace:: niagara.boulder.rdhpcs.noaa.gov
.. |NRPRNG|	replace:: niagara-rsa.princeton.rdhpcs.noaa.gov
.. |NRBRNG|	replace:: niagara-rsa.boulder.rdhpcs.noaa.gov

.. |OUG|	replace:: :ref:`orion-user-guide`

+-------------------+-----------------+--------------------+
| **RDHPCS System** | |CBHN|          | |RBHN|             |
+-------------------+-----------------+--------------------+
| Gaea              | |GCPRNG|        | |GRPRNG|           |
+                   +                 +                    +
|                   | |GCBRNG|        | |GRBRNG|           |
+-------------------+-----------------+--------------------+
| Hera              | |HCBRNG|        | |HRBRNG|           |
+                   +                 +                    +
|                   | |HCPRNG|        | |HRPRNG|           |
+-------------------+-----------------+--------------------+
| Jet               | |JCBRNG|        | |JRBRNG|           |
+                   +                 +                    +
|                   | |JCPRNG|        | |JRPRNG|           |
+-------------------+-----------------+--------------------+
| Niagara           | |NCBRNG|        | |NRBRNG|           |
+                   +                 +                    +
|                   | |NCPRNG|        | |NRPRNG|           |
+-------------------+-----------------+--------------------+
| Cloud             | Unavailable     | Use ParallelWorks  |
+-------------------+-----------------+--------------------+
| MSU-HPC Orion     | Unavailable     | |OUG|              |
+-------------------+-----------------+--------------------+


COMPILERS

.. _compilers:

Compilers
=========

The following compilers and MPI stacks are available on RDHPCS systems:

* Compilers: Intel, Nvidia/PGI, NAG
* MPI: Intel MPI

We recommend the Intel compiler/Intel MPI combination, unless there is a
specific reason to use other options.

Using the Intel compiler with Intel MPI
---------------------------------------

To see the available modules, run the  command `` module spider intel impi``,
which will print a list of available intel and impi modules.

Load the desired version of the module files as follows:

.. code-block:: shell

    module load intel/<version> impi/<version>

Then use the following commands/wrappers to compile your applications.

For serial codes:

.. code-block:: shell

    ifx/ifort: for Fortran codes
    icx/icc: for C/C++ codes


For parallel codes:

.. code-block:: shell

    mpiifx/mpiifort -fc=ifx:  for Fortran MPI codes
    mpiicx: for C/C++ codes

Use the man pages, or the ``--help`` option on these commands, to get more
detailed information about the options available with those commands.

Recommended Intel Compiler Options for Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following options are a starting point to optimize code. Users
should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell

   -O3 -xHOST -ip   -align array64byte                                  # The -xHOST is recommended for Hera users only
   -O3 -qopt-zmm-usage=high -axCORE-AVX512  -align array64byte -ip      # For Skylake processors (Hera/kJet)

.. note::

   Using the AVX-512 instructions may or may not improve performance. We
   recommended that you experiment with and without these options and use the
   one that performs the best.

Compiling for multiple processor types
--------------------------------------

Jet consists of multiple clusters of various types of processors. If you
compile the codes with "fat" executables, it will be possible to run your
applications on any of the Jet partitions.  As you can then take advantage of
any of the available clusters and not wait for specific partitions to be
available, this will likely improve your job turnaround.

Use the following optimization flags to create "fat" executables that can run
on any of the Jet clusters.

.. code-block:: shell

   -O3 -axSSE4.2,AVX,CORE-AVX2,CORE-AVX512  -align array64byte -ip


Compiling for reproducible results
----------------------------------

Some applications may need to use the ``-fp-`` model to obtain consistent
arithmetic results across core counts. This option better controls the order of
execution and may affect performance. See ``man ifort``; for additional
information.

.. code-block:: shell

   -fp-model strict
   -fp-model precise


Recommended Intel compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code. The
-gen-interfaces can also be useful for finding errors.

.. code-block:: shell

   -O0 -g -traceback -check all -fpe0

Thread-safe compilation
^^^^^^^^^^^^^^^^^^^^^^^

If thread-safe compilation is desired, be sure to use one of the following
options (this is an issue with only Intel Fortran compiler):

.. code-block:: shell

   -qopenmp (if the source file has OpenMP directives that need to be honored)
   -recursive    # or -auto (these two are equivalent)

.. warning::

   If none of the options above are used, only scalers are put on stack and the
   generated code may not be thread safe. If you have used ``xlf_r`` or
   ``mpxlf_r`` options on IBM systems, you should use thread-safe compilation
   options on Intel fortran compiler.

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

Run the command: ``ifx -–help`` to see all the available options.

Using the Nvidia/PGI compilers
------------------------------

Users should use the Intel compiler unless they have demonstrated that there is
a good reason not to. The Intel compiler is the most supported and well tested
compiler on the system.

The vendor of the PGI compiler, The Portland Group, has been acquired by
Nvidia. Since the older versions of this compiler are deprecated we only
document the commands for the newer versions.

To see the available versions of the PGI/Nvidia HPC compilers, use the
command ``module available nvhpc``.

You need to load a module for a specific version of the compiler before you are
can use that compiler: ``module load nvhpc/<version>``


Then use the following commands/wrappers for compiling your applications.

For serial programs:

.. code-block:: shell

   nvfortran - for Fortran sources
   nvc       - for C sources
   nvcc      - for Cuda C sources
   nvc++     - for C++ sources


For parallel programs:

.. code-block:: shell

   mpinvf77  - for Fortran 77 MPI sources
   mpinvf90  - for Fortran 90 MPI sources
   mpinvc    - for C MPI sources
   mpinvcc   - for Cuda C MPI sources
   mpinvc++  - for C++ MPI sources


Documentation on Nvidia/PGI compiler options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The man pages are the best resource for documentation on compiler options.
After you've loaded the modules as instructed above, run

.. code-block:: shell

   man nvfortran
   man nvcc


Nvidia/PGI compiler options for optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for optimizing code.
Users should keep in mind that each code is different, and some tuning and
experimentation with different settings may be required.

.. code-block:: shell


   -O3 -fastsse -tp=sandybridge,ivybridge,haswell,skylake


Nvidia/PGI compiler options for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the following options as a starting point for debugging code.
These options are very helpful in detecting common errors in code.

.. code-block:: shell

   -O0 -g -traceback -Mbounds -Mchkfpstk -Mchkptr -Mchkstk

