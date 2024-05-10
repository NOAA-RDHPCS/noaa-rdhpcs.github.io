.. _modules:

#######
Modules
#######

Lmod is a Lua based module software management system that helps manage the user environment (PATH, LD_LIBRARY_PATH) through module files. LMOD is used on various HPC systems including Gaea, Hera, and Jet. The `Lmod documentation <https://lmod.readthedocs.io/en/latest/010_user.html>`_ explains the use of Modules in detail.

View Active Modules
===================

Use ``module list`` to see what modules are loaded in your environment.

.. code-block:: shell

    $ module list 

Find Modules
============ 

Lmod provides several commands to help you find modules including module avail, and module spider.

To view a list of available modules in MODULEPATH use ``module avail <module>``. The command will show only modules that can be loaded in the current environment.

.. code-block:: shell

    $module avail 


The command ``module spider <module>`` will show all modules and versions with the name.  This includes modules that cannot be loaded in the current environment.

.. code-block:: shell

    $ module spider cray-netcdf/4.9.0.1
    ----------------------------------
    cray-netcdf: cray-netcdf/4.9.0.1
    ----------------------------------

	You will need to load all module(s) on any one of the lines below before the "cray-netcdf/4.9.0.1" module is available to load.

  	aocc/3.2.0  cray-hdf5/1.12.2.1
  	aocc/3.2.0  cray-hdf5/1.12.2.3
  	aocc/3.2.0  cray-hdf5/1.12.2.7
  	gcc/10.3.0  cray-hdf5/1.12.2.1
  	gcc/10.3.0  cray-hdf5/1.12.2.3




**NOTE**: ``module spider`` command reports all modules along with all module trees in the hierarchical system while ``module avail`` does not. To see all possible modules and their versions, use ``module spider``



Load Modules
============ 

User ``module load`` to load a module into the current environment of a session or job.

.. code-block:: shell

    $ module load <module>

Use ``module unload`` to remove a loaded module

.. code-block:: shell

    $ module unload <module>

LMOD employs a hierarchical system that, when used properly, considers dependencies and prerequisites for a given software package.  

For example, the ``cray-netcdf`` module depends on the ``cray-hdf5`` module and cannot be seen by the standard module avail commands nor be loaded until the cray-hdf5 module is loaded.

The LMOD hierarchical system will automatically deactivate or swap an upstream module dependency. 

When that happens, any downstream module will still be loaded but inactivated. 

.. code-block:: shell

    $ module load cray-hdf5 
    
    $ module load cray-netcdf
    
    $ module unload cray-hdf5
    
    Inactive Modules:
    cray-netcdf


In this example, the cray-netcdf module depends on the cray-hdf5 module.  When the cray-hdf5 module is unloaded, the cray-netcdf module becomes inactive.  

Reloading the cray-hdf5 module will reactivate the cray-netcdf module.


Adding Additional Module Paths
==============================

Do not manually set the ``MODULESPATH`` environment variable.  Manually setting the ``MODULESPATH`` environment variable will produce unknown behavior.  

Use ``module use <path>`` or ``module use -a <path>`` to add more module paths.


Modules with sh, bash, and ksh scripts
======================================


How can I get the shell functions created by modules in bash shell scripts such as job submission scripts?
----------------------------------------------------------------------------------------------------------

Make sure that shell functions and alias works correctly in bash interactive sub-shells.

Once that works then change the first line of the shell script to be:

.. code-block:: shell

    #!/bin/bash -l

**Note**: That is not a minus one. 

This will cause the startup scripts to be sourced before the first executable statement in the script.

Why doesn’t the module command work in shell scripts?
-----------------------------------------------------

First it is recommended that the script be a bash script and not a shell script, so start the script with ``#!/bin/bash``. 

The environment variable ``BASH_ENV`` must point to a file which defines the module command. ``MODULEHOME`` should point to the file that defines the module command. 

You can also do the following in your script before using the module command

.. code-block:: shell

    $ source $MODULESHOME/init/sh



Command Summary
---------------

+--------------------------------+---------------------------------------------------------+
|Command                         |Description                                              |
+================================+=========================================================+
|module list                     |List active modules in the user environment              |
+--------------------------------+---------------------------------------------------------+
|module avail [module]           |List available modules in MODULEPATH                     |
+--------------------------------+---------------------------------------------------------+
|module spider [module]          |Query all modules in MODULEPATH and any module hierarchy |
+--------------------------------+---------------------------------------------------------+
|module load [module]            |Load a module file in the users environment              |
+--------------------------------+---------------------------------------------------------+
|module unload [module]          |Remove a loaded module from the user environment         |
+--------------------------------+---------------------------------------------------------+
|module swap [module1] [module2] |Replace module1 with module2                             |
+--------------------------------+---------------------------------------------------------+
|module use [-a] [path]          |Prepend or Append path to MODULEPATH                     |
+--------------------------------+---------------------------------------------------------+
|module unuse [path]             |Remove path from MODULEPATH                              |
+--------------------------------+---------------------------------------------------------+
|module show [module]            |Show content of commands performed by loading module file|
+--------------------------------+---------------------------------------------------------+


**Warning**

Please **DO NOT** use the command module purge. This will remove all modules currently loaded by default in your environment and will lead to major errors. 
If you have accidentally used the command purge, log out of GAEA and log in. This will give you the default environment with the default modules loaded.


