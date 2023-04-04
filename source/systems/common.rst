######
Common
######

This table will be updated with Common System Elements

+---------------------+---------------+------------------+---------------+------------------+
|                     | Hera TCA      | Hera FGA         | Juno TCA      | Juno FGA         |
+=====================+===============+==================+===============+==================+
| CPU Type            | Intel SkyLake | Intel Haswell    | Intel SkyLake | Intel Haswell    |
+---------------------+---------------+------------------+---------------+------------------+
| CPU Speed           | 2.40 GHz      | 2.460 GHz        | 2.40 GHz      | 2.460 GHz        |
+---------------------+---------------+------------------+---------------+------------------+
| Reg Compute Nodes   | 1328          | 100              | 14            | 2                |
+---------------------+---------------+------------------+---------------+------------------+
| Cores/node          | 40            | 20               | 40            | 20               |
+---------------------+---------------+------------------+---------------+------------------+
| Total Cores         | 53,120        | 2000             | 560           | 40               |
+---------------------+---------------+------------------+---------------+------------------+
| Memory/Core         | 96 GB         | 256 GB           | 90 GB         | 256 GB           |
+---------------------+---------------+------------------+---------------+------------------+
| Peak Flops/node     | 12            | NA               | 12            | NA               |
+---------------------+---------------+------------------+---------------+------------------+
| Service Code Memory | 187 GB        | NA               | 187 GB        | NA               |
+---------------------+---------------+------------------+---------------+------------------+


Here is language for tabs with code content

.. tab-set::

   .. tab-item:: [t]csh

      .. code-block:: tcsh

         setenv SLURM_CLUSTERS t4,c3,c4,gfdl,es

   .. tab-item:: bash

      .. code-block:: bash

         export SLURM_CLUSTERS=t4,c3,c4,gfdl,es


Here is language for cards

 .. grid:: 6

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Gaea
    ^^^^^

    Gaea is located in Oak Ridge National Laboratory at ORNL’s National Center for Computational Sciences (NCCS). This Climate Modeling and Research System (CMRS) is accessed remotely through two 10-gigabit WAN connections. Gaea is the largest of four NOAA research and development HPC systems.

    https://gaeadocs.rdhpcs.noaa.gov/wiki/index.php/Welcome_to_Gaeadocs Gaea Docs Start Page

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Hera
    ^^^^^

    Hera is located at NOAA Environmental Security Computing Center (NESCC) in Fairmont, West Virginia. It is Cray System. The compute capacity of Hera supports the development of weather modeling across the Office of Oceanic and Atmospheric Research and National Weather Service to improve the prediction of high-impact weather events and evaluate potential future directions for models and data assimilation.

    https://heradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page Hera Docs Start Page

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Jet
    ^^^^

    Jet primarily supports the HPC needs of the Hurricane Forecast Improvement Program (HFIP), numerical weather prediction, and other weather research. Since 2009, Jet has been used to run real-time jobs, via reservation schemes in the batch scheduler, to support HFIP during hurricane season and various other high-priority R2O projects.

    https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Start Jet Docs Start Page

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Niagara
    ^^^^^^^^

    The Niagara system is  a collaborative resource where data can be securely copied to and from any location, by any authorized user. It can also be used as a service to disseminate research and development data to NOAA's collaborators around the globe.

    https://niagaradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page Niagara Docs Start Page

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    MSU-HPC
    ^^^^^^^

    MSU-High Performance Computing, managed externally by Mississippi State University (MSU), is the fourth largest academic supercomputer in the United States to date. MSU-HCP is funded via grants from NOAA to support research activities in environmental modeling, including weather modeling and simulation. 

    https://oriondocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page MSU-HPC Docs Start Page

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Cloud
    ^^^^^^

    The Cloud Platform allows NOAA users to create HPC clusters on an as-needed basis, with resources that are appropriate for the task at hand.

    https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page Cloud Docs Start Page

