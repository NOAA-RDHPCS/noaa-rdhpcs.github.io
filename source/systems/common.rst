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

 .. grid:: 4

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C3
    ^^^

    Cray XC40-LC

    1,504 compute nodes
    (2 x Intel Haswell 16-cores per node)

    64GB DDR4 per node; 96TB total

    1.77 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C4
    ^^^

    Cray XC40-LC

    2,656 compute nodes (2 x Intel Broadwell 18-cores per node)

    64GB DDR4 per node; 145TB total

    3.52 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    C5
    ^^^

    HPE EX

    1,792 compute nodes (2 x AMD Rome 64-cores per node)

    251 GB DDR5 per node; 449TB total

    10.2 PF peak

  .. grid-item-card::
    :class-header: sd-bg-muted sd-text-light

    F2 File System
    ^^^

    DDN Lustre

    32 PB total usable; ZFS compression

    36 OSS; 72 OST; 4 MDS        