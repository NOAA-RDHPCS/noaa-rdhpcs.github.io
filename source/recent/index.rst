Recent User-Facing Changes
==========================

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

