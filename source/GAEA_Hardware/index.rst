
#############
Gaee Hardware
#############

c3 partition
------------

* 1.1 petaflop Cray XC40
* 47872 Cores
  * 32 cores/node
  * 1496 nodes
  * 93.5 TB of memory
  * Intel Haswell Processors
* 4 Login nodes (Gaea9-12)


c4 partition
------------

* 1.99 petaflop Cray XC40
* 54,144 Cores
  * 36 cores/node
  * 1504 nodes
  * 98 TB of memory
  * Intel Broadwell Processors
* 4 Login nodes (Gaea13-16)

es partition
------------

rdtn queue
^^^^^^^^^^

- Remote Data Transfer Nodes - used for transferring data to/from the world outside of Gaea
- 8 nodes (rdtn01-08)
- 8 slots per node
- 64 total slots

ldtn queue
^^^^^^^^^^

- Local Data Transfer Nodes - used for I/O intensive operations, like model output combining
- 16 nodes (ldtn1-16)
- 8 cores/node
- 128 cores

eslogin queue
^^^^^^^^^^^^^

- login nodes - used for compiling
- 8 total
- gaea9-12 = c3
- gaea13-16 = c4
- 24 cores
- 256 GB memory
