************
Queue Policy
************

.. toctree::
   :maxdepth: 2

--------
Overview
--------

Changes and fine-tuning to the queue structure can be done on a weekly basis through the Configuration Management process.

**Some overall points**

- The queuing system should allow groups/projects to spend their allocation each month.
- The tension between keeping persistent jobs in the system and running very large jobs suggests that there should be a limit on the number of cores a job may use, but with a capability to make exceptions for “novel” jobs that may require up to the entire system.
This will promote consideration of whether a job requires a large number of cores due to, for example, memory or schedule constraints, or whether it is simply desired.
- There should be queues with different priority levels usable by the scheduling algorithm.
At the very least, run-time variability would need to be assessed before we could even think of implementing this.

**Recommendations**

- Use a fair-share algorithm that can throttle scheduling priority by comparing how much of a particular allocation has been used at a given time with how much should have been used, assuming constant proportional usage. This will promote steady usage throughout the month.
- Use two separate allocations, renewed monthly, with multiple queues drawing down each of them:
50% of the available time for high-priority persistent and urgent work, that should minimize queue wait time. The Queues are:

-- Persistent, for job streams that are intended to stay in the system for “long” periods of time with virtually no wait time when new job segments are submitted.
-- Urgent, for schedule-driven work needing to be completed ASAP.
-- Novel, for jobs that have unusual resource requirements, typically needing more than 25% of the system’s cores. These can be run during an 8-hour period immediately after Preventative Maintenance is complete, since no other jobs will be running at that time.

- 50% for all other **normal-priority** allocated work. Queues would be:
-- Batch, for regular allocated jobs
-- Debugging/Interactive work. A windfall quality of service (QOS) tagis for work that will not be charged against an allocation. As of Jan. 15, 2013, windfall can only be specified with -l qos=windfall.

.. code-block:: shell

   > msub -l qos=windfall scriptName
   
or in your job script:

.. code-block:: shell

   #PBS -lqos=windfall

- Priorities between queues

-- Normally, Persistent and Urgent queues will have the highest priority, but remain subject to the fair-share algorithm. This will discourage groups from hoarding high-priority time for the end of the month.
-- Within a group/project, jobs in the Urgent queue are higher priority than jobs in the Persistent queue, with each group expected to manage the intra-group mix per their allocation.
-- Between groups/projects, jobs in the Persistent and Urgent queue are the same priority.
-- At any given time, the suite of jobs drawn from the Persistent and Urgent queues and running on the system should use about 50% of the available cores (per the fair-share algorithm), but that suite is permitted to use more than 50% as needed (with the implication that less than 50% will be used at other times of the month).

- Limit the largest job to 25% of the available cores except in the Novel queue.
- Limit time requested for individual job segments to 12 hours.
- Interactive/debugging jobs have a tiered limit:
  - < or = 72 cores (3 nodes) 12 hour limit
  - < or = 504 cores (21 nodes) 6 hour limit
  - can't go over 504
(These limits supersede the previous intent to limit interactive/debugging jobs to 2 node-days or 1152 core-hours.).

- Partitions
- Users are encouraged to add the following to their job submissions and/or job script -l partition=c3

.. code-block:: shell

   >msub -l partition=c3 /path/to/job/script

or in your job script:

.. code-block:: shell

   #PBS -l partition=c3
