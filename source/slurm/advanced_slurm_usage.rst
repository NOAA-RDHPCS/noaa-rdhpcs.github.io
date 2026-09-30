.. meta::
   :description: Advanced Slurm techniques for running many job steps in
    parallel with controlled CPU placement, including exclusivity,
    cpu-bind, and hyperthread isolation.
   :keywords: Slurm, srun, cpu-bind, exclusive, hint, nomultithread,
    job steps, parallel, HPC

.. _advanced-slurm-usage:

#####################
Advanced Slurm Usage
#####################

This page collects advanced Slurm techniques for users who are already
comfortable with the basics of ``sbatch``, ``salloc``, and ``srun``.  It
currently covers running many job steps in parallel with controlled CPU
placement.

.. _parallel-srun-steps:

Running Parallel ``srun`` Job Steps in the Background
=======================================================

Overview
--------

This pattern launches many independent ``srun`` job steps in parallel, in the
background, with one process pinned to one physical core each.  It is useful
for testing core placement, CPU binding, and job step isolation across
different systems.

A simple ``sleep`` command is used as the test executable throughout this
section.  It requires no compilation, no MPI runtime, and no external
dependencies, which keeps the focus on Slurm's scheduling and binding behavior
rather than on the test program itself.

Prerequisites
--------------

* An active Slurm allocation (``salloc`` or ``sbatch``) with one or more CPUs
  reserved.
* Access to ``srun``, ``squeue``, ``sacct``, and ``scontrol`` on the login or
  batch node.
* A :file:`logs/` directory for per-step output.

Core Concepts
--------------

Two Slurm flags govern how job steps share (or do not share) CPU resources.
They are independent of each other and are commonly used together.

``--exclusive``
    A sharing policy.  It prevents other job steps from using the CPUs
    allocated to this step while it is running.  It does not control which
    specific CPU IDs are chosen.

``--cpu-bind``
    A placement mechanism.  It pins a task to specific CPU core IDs using
    ``sched_setaffinity``.  It does not control whether other steps may also
    use those cores.

``--hint=nomultithread``
    Restricts CPU selection to one hardware thread per physical core.  Without
    this flag, ``--exclusive`` still prevents two steps from sharing the same
    logical CPU ID, but it does **not** prevent two steps from landing on
    sibling hardware threads of the same physical core on SMT-enabled systems.

Recommended Flag Combination
------------------------------

For a single-threaded test program running one task per step, the following
combination gives the cleanest, most reproducible one-process-per-physical-core
behavior:

.. code-block:: bash

   srun --exclusive \
        --hint=nomultithread \
        -n1 \
        --cpus-per-task=1 \
        --cpu-bind=cores \
        --output=logs/task_${i}.log \
        sleep 30 &

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Purpose
   * - ``-n1``
     - One task per step.
   * - ``--cpus-per-task=1``
     - Reserve exactly one CPU per task.
   * - ``--exclusive``
     - No other step may share this CPU.
   * - ``--hint=nomultithread``
     - Avoid sibling hyperthread collisions.
   * - ``--cpu-bind=cores``
     - Pin the task to its assigned core.

Launching Steps in Parallel
-----------------------------

This script is intended to run directly on a compute node, after an
interactive allocation has already been granted.  Request the allocation
with ``salloc``, specifying the same resources the loop will use:

.. code-block:: bash

   salloc -A <account> -M <cluster> -t 00:10:00 -N1 --ntasks=10

Once ``salloc`` returns and places the shell on a compute node, run the
script directly, for example ``./myscript.sh``.  The ``#SBATCH`` style
directives shown later in this section have no effect in this mode; the
resources requested on the ``salloc`` command line are what determine the
allocation.

Each ``srun`` invocation is backgrounded with ``&`` inside a loop so the shell
does not wait for one step to finish before launching the next.

.. code-block:: bash

   #!/bin/bash
   set -euo pipefail

   mkdir -p logs

   NUM_CPUS=${SLURM_NTASKS:-${SLURM_CPUS_ON_NODE:-1}}

   SLEEP_SECONDS=30
   PIDS=()

   for i in $(seq 0 $((NUM_CPUS - 1))); do
       srun --exclusive \
            --hint=nomultithread \
            -n1 \
            --cpus-per-task=1 \
            --cpu-bind=verbose,cores \
            --output=logs/task_${i}.log \
            sleep "${SLEEP_SECONDS}" &
       PIDS+=($!)
       echo "Launched step ${i} -> PID ${PIDS[-1]}"
   done

   wait "${PIDS[@]}"
   echo "All ${NUM_CPUS} steps completed"

Because ``sleep`` writes no output of its own, ``--cpu-bind=verbose`` is
included so Slurm itself reports the CPU mask each task was bound to, directly
in the step's log file.

Discovering the Allocated CPU Count
--------------------------------------

It is tempting to discover the CPU count by inspecting the current shell's own
affinity mask, for example with ``taskset -cp $$``.  This approach is
unreliable and should be avoided:

* Under ``sbatch``, the script itself runs as the batch step.  Slurm confines
  the batch step to a single CPU by default, regardless of how many CPUs the
  job as a whole was granted, so ``taskset`` inside the script reports only
  one CPU even though the full allocation is reserved.
* Under an interactive ``salloc`` session, the shell landed on after reaching
  the compute node is not guaranteed to carry the full job's affinity mask
  either, depending on how that shell was started.

In both cases the job's real allocation is still correct; only the shell's
own reported affinity is misleading.  Use the Slurm-provided environment
variables instead, since these reflect the job record itself rather than the
affinity of whichever process happens to be running the script:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - What it reports
   * - ``SLURM_NTASKS``
     - Total tasks requested via ``--ntasks``.
   * - ``SLURM_CPUS_ON_NODE``
     - Total CPUs allocated on the current node.
   * - ``SLURM_JOB_CPUS_PER_NODE``
     - CPUs per node, possibly in a compressed multi-node form such as
       ``96(x2)``.

``taskset`` remains useful for a different purpose: confirming, after launch,
which core a specific running task actually landed on (see
`Interpreting --cpu-bind=verbose Output`_).  It is simply the wrong tool for
determining the size of the job's own allocation.

Submitting via ``sbatch``
----------------------------

The same script runs under ``sbatch`` once resource directives are added to
the top of the file.  Directives must use a single ``#SBATCH``, not ``##``,
and must appear before any executable line:

.. code-block:: bash

   #!/bin/bash
   #SBATCH -A <account>
   #SBATCH -M <cluster>
   #SBATCH -t 00:10:00
   #SBATCH --cpus-per-task=1
   #SBATCH --ntasks=10
   #SBATCH -N1

   set -euo pipefail

   mkdir -p logs

   NUM_CPUS=${SLURM_NTASKS:-${SLURM_CPUS_ON_NODE:-1}}
   SLEEP_SECONDS=30
   PIDS=()

   for i in $(seq 0 $((NUM_CPUS - 1))); do
       srun --exclusive \
            --hint=nomultithread \
            -n1 \
            --cpus-per-task=1 \
            --cpu-bind=verbose,cores \
            --output=logs/task_${i}.log \
            sleep "${SLEEP_SECONDS}" &
       PIDS+=($!)
   done

   wait "${PIDS[@]}"
   echo "All ${NUM_CPUS} steps completed"

Submit with:

.. code-block:: bash

   sbatch myscript.sh

Then confirm the allocation matched what was requested:

.. code-block:: bash

   sacct -j <jobid> --format=JobID,NNodes,NTasks,AllocCPUS,State

If the ``logs/`` directory does not already exist and a top-level
``--output=logs/...`` directive is added for the batch step itself, Slurm may
attempt to write that file before the script body has a chance to run
``mkdir -p logs``.  Either create ``logs/`` ahead of time, or omit a
directory path from the batch step's own ``--output`` directive and let it
fall back to the default file in the submission directory.

Confirming Parallel Execution
--------------------------------

While the steps are running, all of them should appear with a ``RUNNING``
state at the same time, not one after another:

.. code-block:: bash

   squeue --step=<jobid>.*

After completion, per-step timing and exit status are available through
``sacct``:

.. code-block:: bash

   sacct -j <jobid> \
         --format=JobID,Start,End,ExitCode,State,AllocCPUS -P

Interpreting ``--cpu-bind=verbose`` Output
---------------------------------------------

A typical line of ``--cpu-bind=verbose`` output looks like this:

.. code-block:: text

   cpu-bind=MASK - nodename, task 0 0 [12345]: mask 0x1 set

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Meaning
   * - ``cpu-bind=MASK``
     - Binding type reported (mask form).
   * - ``nodename``
     - Hostname the task ran on.
   * - ``task 0 0``
     - Local task ID, then global task ID.
   * - ``[12345]``
     - Operating system process ID (PID).
   * - ``mask 0x1``
     - Hexadecimal CPU affinity mask actually applied.
   * - ``set``
     - Confirms the binding call succeeded.

The process ID identifies the operating system process, not the Slurm step.
PIDs are reused by the kernel once a process exits, so a PID by itself cannot
be used to distinguish one step from another.  The Slurm step identity comes
from ``SLURM_JOB_ID.SLURM_STEP_ID``, which should be logged separately if
step-level correlation is required.

Detecting Genuine Core Collisions
------------------------------------

A CPU mask appearing in more than one step's log is not, by itself, proof of a
collision.  Steps that run sequentially will correctly reuse a core once the
earlier step has released it.  A genuine collision requires two conditions to
hold at once:

#. The same CPU mask appears under two different step IDs.
#. The ``Start`` and ``End`` timestamps of those two steps, as reported by
   ``sacct``, actually overlap in time.

.. code-block:: bash

   sacct -j <jobid> \
         --format=JobID,Start,End,ExitCode,State,AllocCPUS -P

If two steps share a mask and their time windows overlap, the isolation
configuration should be reviewed, starting with partition-level
oversubscription settings and the presence of ``--hint=nomultithread``.

Deliberate Core Sharing
--------------------------

The opposite goal, intentionally letting multiple steps share a single core for
contention testing, uses the inverse of the flags above:

.. code-block:: bash

   CPU_ID=0

   for i in $(seq 0 4); do
       srun -n1 \
            --cpus-per-task=1 \
            --overlap \
            --oversubscribe \
            --cpu-bind=map_cpu:${CPU_ID} \
            --output=logs/shared_core_task_${i}.log \
            sleep 30 &
   done
   wait

Oversubscription may also need to be enabled at the partition or allocation
level.  Check the partition configuration before relying on step-level flags
alone:

.. code-block:: bash

   scontrol show partition <partition_name>

Why a Plain Command Instead of MPI
-------------------------------------

An MPI test program is only useful when a step launches more than one
communicating task.  For steps that run a single task (``-n1``), an MPI program
adds initialization overhead and an additional dependency, namely a matching
``--mpi=`` launch plugin, without exercising any MPI functionality.  A plain
command such as ``sleep`` isolates the variable actually under test, which is
Slurm's core placement and binding behavior, and removes an unrelated source of
failure.

Summary
---------

* ``--exclusive`` prevents CPU ID reuse between concurrently running steps.
* ``--cpu-bind=cores`` pins each task to a specific core for the duration of
  the step.
* ``--hint=nomultithread`` is required in addition to ``--exclusive`` to avoid
  sibling hyperthread contention on SMT-enabled systems.
* CPU mask reuse across steps is only a problem when the corresponding time
  windows overlap.
* A minimal command such as ``sleep`` is sufficient for single-task binding
  and placement tests; MPI is only needed once a step launches multiple
  communicating tasks.
