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



Jan 22, 2025: DTNs for Ursa are now available
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DTNs and the new file systems for Ursa are now available for your use.

.. note::

  The ``/scratch3`` and ``/scratch4`` filesystems will be upgraded
  in February. There will be a 3-5 day
  outage for those file systems at that time.

**Currently these two new filesystems are only mounted
and accessible from Hera and the new Ursa DTNs.**

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * -
     - Host Name
     - File System
     - Globus Endpoints
   * - Trusted
     - dtn-ursa.fairmont.rdhpcs.noaa.gov
     - /scratch[34]
     - noaardhpcs#ursa
   * - Untrusted
     - udtn-ursa.fairmont.rdhpcs.noaa.gov
     - /scratch[34]/data_untrusted
     - noaardhpcs#ursa_untrusted



Using these new DTNs you can do data transfers to the ``/scratch3``
and ``/scratch4`` filesystems either using Linux tools such
as scp and rsync, or by using Globus Online.


Please see the :ref:`data-transfer-overview` for more details.

