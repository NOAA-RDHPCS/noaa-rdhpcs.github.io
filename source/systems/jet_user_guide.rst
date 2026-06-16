.. meta::
   :description: User guide for Jet, a NOAA RDHPCS system scheduled for
    decommission on March 31, 2026, with guidance on migrating workloads
    and data to other RDHPCS resources.
   :keywords: Jet, RDHPCS, decommission, migration, hurricane forecasting,
    partitions, Slurm

.. _jet-user-guide:

**************
Jet User Guide
**************

.. _Data Transfers:  https://docs.rdhpcs.noaa.gov/data/transfers.html
.. _Helpdesk:		   https://docs.rdhpcs.noaa.gov/help/index.html
.. _Presentation:    https://docs.google.com/presentation/d/1yW_qDjhRbklwEn7LlDySBuq_GksvAVg1N6QpsYPsmZg/edit?slide=id.p#slide=id.p
.. _Google Doc:      https://docs.google.com/document/d/1-Q9ktwH8ytgPkHNu9dBvLbq439gCcYw_ANDvb8WbRsY/edit?tab=t.0#heading=h.yzfl0j6tk081

.. Attention::

   **Jet has been decommissioned as of March 31, 2026!**

Jet Data Disposition
---------------------

Certain Jet user data is currently accessible from the Ursa
login nodes in “read-only” mode, and will remain available until July 31, 2026.

* Files from ``/home/$USER`` are found at: ``/jet/home/$USER``
* Files from ``/contrib`` are found at: ``/jet/contrib``
* Files from ``/lfs[5,6]`` are found at: ``/jet/lfs[5,6]``


**Note: For LFS, only files accessed on Jet within the last 30 days of
Jet (accessed between March 1 through March 31, 2026) are made available.**


If you have data in these locations that you wish to retain, transfer the data
to another RDHPCS system or your local environment prior to July 31, 2026.

.. WARNING::

   **Jet data will not be available after July 31, 2026.**

