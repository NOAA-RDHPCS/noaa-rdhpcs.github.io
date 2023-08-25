Allocations
===========

RDHPCS System compute allocations are decided upon by the RDHPCS
Allocation Committee (AC), with oversight from the NOAA HPC Board. The
approved System allocations are typically given to portfolios as a % of
the System or an average core-hours per month. Each portfolio is
represented on the Allocation Committee and an Allocation Committee
Chair is assigned by the HPC board typically for a 1+ year term. Each
portfolio has a portfolio manager (PfM) who is responsible for managing
their projects and PI’s and distributing their allocation amongst their
projects as needed on each System where they have an allocation. Within
a portfolio, allocations on a System can be traded by the PfM as
desired. Portfolios may trade allocations with each other on a System or
between Systems with all concerned PfM’s approval and with documentation
and communication with the AC, but this is done typically for specified
period of time. The PfM in conjunction with the PI’s is also responsible
for managing disk quota and archive tape usage. A portfolio’s disk quota
on a system is initially based on their % of compute allocation on that
System.

For information on how allocations are implemented on a System please
see: `How SLURM with Fairshare
Works <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/SLURM_FairShare>`__

For more information about the Allocation Committee, see `Allocation
Committee <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/High_Performance_Computing_%26_Communications_(HPCC)_Overview#Allocation_Committee>`__

For more information about Portfolio Managers, see `Portfolio
Managers <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/High_Performance_Computing_%26_Communications_(HPCC)_Overview#Portfolio_Managers>`__

To review the Allocation Request Form, see `R&D HPC Allocation Request
Form <https://docs.google.com/forms/d/10A-V_ZkWE_VRkRw1Bg3s6ekx2RWdGDNSwOZ23QEQv6g/edit>`__

.. _request_an_increase_in_allocations:

Request an Increase in Allocations
----------------------------------

To obtain an increase in Allocations, review the `Allocation Committee
Procedures
document <https://docs.google.com/document/d/1qrLyf92b7vKcHch5eKFOK1fetr7c2QW1r2iFxAtzwB8/edit>`__.
This document describes the procedures and timelines involved in the
request. It also includes a list of Portfolio Managers and the
Allocation Request Form.

#. Identify your Portfolio Manager (PfM).
#. Request that your PfM complete an Allocation Request form.
#. The PfM will complete and submit the request for approval.

.. _adding_a_project_to_an_allocation:

Adding a Project to an Allocation
---------------------------------

Requests for additional project allocation needs to be submitted through
the **PfM** to OTRS or AIM. If the request involves different
portfolios, both PfMs will need to approve and accept the transfer. The
request should contain the following:

-  **FROM Project:** The project where hours will be subtracted.
-  **TO Project:** The project where hours will be added.
-  **AMOUNT:** The amount of core hours to be moved in the transfer.
-  **TIME:** Is this a temporary or permanent transfer? If temporary,
   please include the date when you would like this transfer to be
   reverted.

**NOTE:** Allocation increases for a project are constrained by the
amount of compute resources designated to a portfolio by the AC. If
additional compute is needed beyond the scope of the portfolio's
resources, PfMs may donate or trade hours as desired. Requests for new
or increased allocations beyond the allotted portfolio amount on a
system should be emailed to the Allocation Committee Chair, as they will
need to be approved by the Allocation Committee.

Quotas
======

.. _requesting_additional_storage_for_a_project:

Requesting Additional Storage for a Project
-------------------------------------------

When requesting additional storage quota, please be mindful of project
space usage. Remember that the scratch spaces are not for long term
storage. Please utilize HPSS for long term storage. Submit requests for
additional quota via
`OTRS <https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Help_Requests#Help_Requests>`__
from the PfM. The request should contain the following:

| • AMOUNT: The amount of quota needed.
| • JUSTIFICATION:The reason why this space is needed.
| • TIME FRAME: Is this a temporary or permanent implementation? If
  temporary, please include the date when you would like this increase
  to be reverted.
