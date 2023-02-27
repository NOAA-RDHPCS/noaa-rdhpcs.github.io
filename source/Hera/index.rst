####
Hera
####

.. toctree::
   :maxdepth: 2

About NESCC 
-------------------------

The NOAA Environmental Security Computing Center (NESCC), located in Fairmont, West Virginia, is the location of NOAA's newest High Performance Computing Data Center. This site provides computing resources to support NOAA's research in Weather and Climate modeling as well as its other environmental research areas.

There are currently two major systems at NESCC:

- Hera - A 760 Tflop Cray Compute Cluster high performance computing system
- HPSS - A 50 Petabyte IBM/Oracle hierarchical storage management system.

Hera System Features:

- Capacity of 3,270 trillion floating point operations per second – or 3.27 petaflops
- The Fine Grain Graphical Processing Units have a total capacity of 2,000 trillion floating point operations per second, or 2.0 petaflops
- 45 million hours per month with 63,840 cores and a total scratch disk capacity of 18.5 Petabytes.

NESCC is also home to Niagara, a cloud-based computing resource. In addition, Test and Development systems are available through NESCC for system and application testing.

System Configuration
----------

|    | Hera TCA  |Hera FGA | Juno TCA | Juno FGA |
| ----- | ----- | ----- | ----- | ----- |
| CPU Type | Intel SkyLake | Intel Haswell | Intel SkyLake | Intel Haswell |
| CPU Speed | 2.40 GHz | 2.460 GHz | 2.40 GHz | 2.460 GHz |
| Reg Compute Nodes | 1328 | 100| 14 | 2 |
| Cores/node | 40 | 20 | 40 | 20 |
| Total Cores | 53,120 | 2000 | 560 | 40 |
| Memory/Core | 96 GB | 256 GB | 90 GB | 256 GB |
| Peak Flops/node | 12 | NA | 12 | NA |
| Service Code Memory | 187 GB | NA | 187 GB | NA |
| Total BigMem Nodes | 268 | NA | 268 | NA |
| BibMem Node Memory | 384 GB | NA | 384 GB | NA |
| CPU Flops | 2672 TF | 83.1 TF |28 TF|1.6 TF|
| GPUs/Node | NA | 8 P100 | NA | 8 P100 |
| Total GPUs | NA | 800 | NA | 16 |
| GPU Flops/GPU | NA | 4.7 | NA | 4.7 |
| Interconnect | HDR-100 IB | FDR-10 (40 Gbps) | HDR-100 IB | FDR-10 (40 Gbps) |
| Total GPU Flops | NA | 3760 TF | NA | 75 TF |

Notes:

- The Skylake 6148 CPU has two AVX-512 units and hence a theoretical peak of 32 double precision floating point operations per cycle with a base clock rate for floating point operations of 1.6 GHz. 
- Total flops is a measure of peak, and doesn’t necessarily represent actual performance.
- Juno is the Test and Development System. Users must be granted specific access to the system for use.
- The FGA part (the nodes with GPUs) are the same as what was on Theia; But the network has been upgraded to EDR.
