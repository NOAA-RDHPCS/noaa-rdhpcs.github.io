Modules
-------

The Environment Modules system is a tool to help users manage their Unix or
Linux shell environment, by allowing groups of related environment-variable
settings to be made or removed dynamically. Modules provides commands to
dynamically load, remove and view software.

Module Commands
===============

- **module help [module]**: Print the usage of each sub-command. If an argument
  is given, print the Module-specific help information for the module file(s)

.. code-block:: shell

    module help gcp
    ----------- Module Specific Help for 'gcp/2.2' --------------------

Sets up the shell environment for gcp

- **module avail**: List of all available modulefiles in the current MODULEPATH


.. code-block:: shell

    module avail
    ------------------------------------------ /opt/cray/ss/modulefiles ---------------------------------------
    portals/2.2.0-1.0301.22039.18.1.ss(default) rca/1.0.0-2.0301.21810.11.20.ss(default)
    ------------------------------------------ /opt/cray/xt-asyncpe/default/modulefiles -----------------------
    xtpe-accel-nvidia20  xtpe-barcelona       xtpe-istanbul        xtpe-mc12            xtpe-mc8             xtpe-network-gemini
    xtpe-network-seastar xtpe-shanghai        xtpe-target-native
    ----------------------------------------- /opt/cray/modulefiles ------------------------------------------
    atp/1.0.2(default)                   perftools/5.1.0(default)             portals/2.2.0-1.0300.20621.14.2.ss   trilinos/10.2.0(default)
    atp/1.1.1                            perftools/5.1.2                      rca/1.0.0-2.0300.20198.8.26.ss       trilinos/10.6.2.0
    ga/4.3.3(default)                    pmi/1.0-1.0000.7628.10.2.ss          rca/3.0.20                           xt-mpich2/5.0.1(default)
    gdb/7.2(default)                     pmi/1.0-1.0000.7901.22.1.ss(default) stat/1.0.0(default)                  xt-mpich2/5.2.0
    iobuf/2.0.1(default)                 pmi/1.0-1.0000.8256.50.1.ss          stat/1.1.3                           xt-mpt/5.0.1(default)
    xt-mpt/5.2.0                         xt-shmem/5.0.1(default               xt-shmem/5.2.0

.. note::

  This is not the complete print out of what your shell might print out

- **module add module_file**: Load module file(s) into the shell environment
- **module load module_file**: Load module file(s) into the shell environment

.. code-block:: shell

    > module load gcp/1.1

- **module list**: List of Loaded modules

.. code-block:: shell

    > module list
    1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
    2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
    3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
    4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
    5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
    16) TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.4.3

    note gcp/1.4.3 is now Loaded at no.18

- **module rm module_file**: unload the module
- **module unload module_file**: unload the module

.. code-block:: shell

    > module unload gcp/1.4.3
    module list
    1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
    2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
    3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
    4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
    5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
    16) TimeZoneEDT                              17) CmrsEnv

    note gcp/1.4.3 is not Loaded

- **module Switch [available_module] replacement_module**: Switch loaded modulefile1 with modulefile2. If modulefile1 is not specified, then it is assumed to be the currently loaded module with the same root name as modulefile2
- **module swap [available_module] replacement_module**:  Switch loaded modulefile1 with modulefile2. If modulefile1 is not specified, then it is assumed to be the currently loaded module with the same root name as modulefile2

.. code-block:: shell

   > module load gcp/1.1
   module list
   Currently Loaded Modulefiles:
   1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
   2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
   3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
   4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
   5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
   16) TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.1

   module swap gcp/1.1 gcp/1.5.0
   1) modules/3.2.6.6                            6) xt-mpt/5.0.1                              11) PrgEnv-pgi/3.1.29
   2) xt-sysroot/3.1.29.securitypatch.20100707   7) pmi/1.0-1.0000.7901.22.1.ss               12) eswrap/1.0.9
   3) xtpe-network-seastar                       8) xt-sysroot/3.1.29                         13) moab/5.4.1
   4) pgi/10.6.0                                 9) portals/2.2.0-1.0301.22039.18.1.ss        14) torque/2.4.9-snap.201006181312
   5) xt-libsci/10.4.6                          10) xt-asyncpe/4.4                            15) xtpe-mc12
   16) TimeZoneEDT                              17) CmrsEnv                                   18) gcp/1.5.0

   Note: the gcp is now version 1.5.0

- **module show modulefile**: Display information about one or more modulefiles. The display sub-command will list the full path of the modulefile(s) and all (or most) of the environment changes the modulefile(s) will make if loaded. (It will not display any environment changes found within conditional statements.)
- **module display modulefile**: Display information about one or more modulefiles. The display sub-command will list the full path of the modulefile(s) and all (or most) of the environment changes the modulefile(s) will make if loaded. (It will not display any environment changes found within conditional statements.)



.. code-block:: shell

    > module show CmrsEnv
    -------------------------------------------------------------------
    /sw/eslogin/modulefiles/CmrsEnv:
    module-whatis    Sets up environment variables for the NCRC CMRS.
    setenv           CSCRATCH /lustre/fs/scratch
    setenv           CSTAGE /lustre/ltfs/stage
    setenv           CWORK /lustre/ltfs/scratch
    setenv           CHOME /ncrc/home1/Naresh.Kosgi
    -------------------------------------------------------------------

- **use [-a]–append] directory**: Prepend one or more directories to the MODULEPATH environment variable. The –append flag will append the directory to MODULEPATH.

.. warning::

  Please **DO NOT** use the command module purge. This will remove all modules currently loaded by default in your environment and will lead to major errors. If you have accidentally used the command purge, log out of GAEA and log in. This will give you the default environment with the default modules loaded.
