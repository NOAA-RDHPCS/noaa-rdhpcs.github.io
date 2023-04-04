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

    `Climate Modeling and Research System (CMRS) at ORNL <https://gaeadocs.rdhpcs.noaa.gov/wiki/index.php>``

   
  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Hera
    ^^^^^

    `Predicting high-impact weather events <https://heradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page> `` 

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Jet
    ^^^^

    `Hurricane Forecast Improvement Program (HFIP) <https://jetdocs.rdhpcs.noaa.gov/wiki/index.php/Start>``

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Niagara
    ^^^^^^^^

    `Collaborative resource for data transfer. <https://niagaradocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page Niagara Docs Start Page>``

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    MSU-HPC
    ^^^^^^^

    `High Performance Computing collaboration with Mississippi State University (MSU) <https://oriondocs.rdhpcs.noaa.gov/wiki/index.php Main_Page>``

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    Cloud
    ^^^^^^

    `Platform to create HPC computational clusters as needed.<https://clouddocs.rdhpcs.noaa.gov/wiki/index.php/Main_Page>``

