Recent User-Facing Changes
==========================

Oct 30, 2026: Apps software stack updated on Hera and Ursa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The /apps stack has been updated on Hera and Ursa.  It has
the latest versions of the compilers/MPI stacks and their dependent
libraries. In order to use the new packages, you must
first load the following module:

.. code-block:: shell

  module load spack-apps/2026.10

Notable changes are as follows:

Hera
""""

* ``Intel-oneapi-mpi/2021.18.0`` with ``Intel-oneapi-compilers/2026.1.0``
  and dependent software such as hdf5, etc. have been installed.
* ``Intel-oneapi-mpi@2021.18.0`` with the system GNU compiler and
  dependent software such as hdf5 etc. have been installed with this
  combination.
* A number of utilities also have been updated.

Ursa
""""

* ``Intel-oneapi-mpi/2021.18.0`` with ``Intel-oneapi-compilers/2026.1.0``
  and dependent software such as hdf5, etc. have been installed.
* ``Intel-oneapi-mpi@2021.18.0`` with the system GNU compiler and
  dependent software such as hdf5 etc. have been installed with this
  combination.
* ``Hpcx-mpi/2.21.3`` with ``Intel-oneapi-compilers/2026.1.0``
  and dependent software such as hdf5, etc. have been installed
* ``Hpcx-mpi/2.21.3`` with the system GNU compiler and dependent software
  such as hdf5, etc. have been installed
* ``Nvhpc@26.9`` stack that includes the nvhpc compilers (formerly PGI)
  and the openmpi implementation that is included with that package has
  been installed.  Libraries such as hdf5 have been installed with this
  combination.
* A number of utilities also have been updated.

To see all available modules, run the ``module spider`` command.

