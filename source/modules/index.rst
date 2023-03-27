Modules
-------

.. toctree::
   :maxdepth: 2

The Environment Modules system is a tool to help users manage their Unix or Linux shell environment, by allowing groups of related environment-variable settings to be made or removed dynamically. Modules provides commands to dynamically load, remove and view software.

Module Commands
===============

- **module help [module]**: Print the usage of each sub-command. If an argument is given, print the Module-specific help information for the module file(s)

.. code-block:: shell

> module help gcp

----------- Module Specific Help for 'gcp/2.2' --------------------

Sets up the shell environment for gcp

- **module availk**: List of all available modulefiles in the current MODULEPATH


.. code-block:: shell

> module avail
------------------------------------------ /opt/cray/ss/modulefiles ---------------------------------------
portals/2.2.0-1.0301.22039.18.1.ss(default) rca/1.0.0-2.0301.21810.11.20.ss(default)
------------------------------------------ /opt/cray/xt-asyncpe/default/modulefiles -----------------------
xtpe-accel-nvidia20  xtpe-barcelona       xtpe-istanbul        xtpe-mc12            xtpe-mc8             xtpe-network-gemini
xtpe-network-seastar xtpe-shanghai        xtpe-target-native
------------------------------------------ /opt/cray/modulefiles ------------------------------------------
atp/1.0.2(default)                   perftools/5.1.0(default)             portals/2.2.0-1.0300.20621.14.2.ss   trilinos/10.2.0(default)
atp/1.1.1                            perftools/5.1.2                      rca/1.0.0-2.0300.20198.8.26.ss       trilinos/10.6.2.0
ga/4.3.3(default)                    pmi/1.0-1.0000.7628.10.2.ss          rca/3.0.20                           xt-mpich2/5.0.1(default)
gdb/7.2(default)                     pmi/1.0-1.0000.7901.22.1.ss(default) stat/1.0.0(default)                  xt-mpich2/5.2.0
iobuf/2.0.1(default)                 pmi/1.0-1.0000.8256.50.1.ss          stat/1.1.3                           xt-mpt/5.0.1(default)
xt-mpt/5.2.0                         xt-shmem/5.0.1(default               xt-shmem/5.2.0

NOTE: this is not the complete print out of what your shell might print out

- **module add module_file**: Load module file(s) into the shell environment
- **module load module_file**: Load module file(s) into the shell environment

