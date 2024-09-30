.. _cron_scron:

.. note::

    Cron is available on :ref:`Hera <hera-user-guide>`, :ref:`Jet
    <jet-user-guide>`, and :ref:`Niagara <niagara-user-guide>`.  Users on the
    other RDHPCS systems, for example :ref:`Gaea <gaea-user-guide>` and
    :ref:`PPAN <ppan-user-guide>` must use :ref:`rdhpcs_scrontab`.

**********************
Cron and Slurm crontab
**********************

Occasionally users may want to automate a common recurring task. Typical use
cases are to initiate batch jobs, transfer input data from an external site, or
run some automated testing. The UNIX :command:`cron` service allows users to
schedule scripts to be run based on a recurrence rule.  Slurm also has a
cron-like feature :command:`scrontab` that is enabled on all RDHPCS systems.

At this time, :command:`cron` is only available on :ref:`Hera
<hera-user-guide>`, :ref:`Jet <jet-user-guide>`, and :ref:`Niagara
<niagara-user-guide>`.

Users can use `Slurm crontab <https://slurm.schedmd.com/scrontab.html>`_
(:command:`scrontab`) on all RDHPCS systems.  Users on :ref:`Gaea
<gaea-user-guide>` and :ref:`PPAN <ppan-user-guide>` must use
:command:`scrontab`. .. _rdhpcs-cron:

Please review the :ref:`Cron/Scrontab RDHPCS policies <cron_usage_policy>` to
verify your cron/scrontab jobs fit within the approved policy.

Cron
====

Cron is a job scheduler that automates repetitive tasks by running them at
specific intervals on Unix-like operating systems.

Install and edit crontab entries
--------------------------------

To schedule a process with cron, you establish a crontab entry. This can be
done interactively by running the command :command:`crontab` with the ``-e``
option (``crontab -e``) to edit your crontab directly, or you can create a file
and *install* it with ``crontab <filename>``. Additionally, you can list your
current crontab entries with ``crontab -l``.  See ``man crontab`` for more
details.

In either case, the crontab entry has a very particular, fixed format.

.. _crontab-syntax:

.. code-block::
    :caption: Sample crontab entry format

    # ┌───────────── minute (0-59)
    # │ ┌───────────── hour (0-23)
    # │ │ ┌───────────── day of the month (1-31)
    # │ │ │ ┌───────────── month (1-12)
    # │ │ │ │ ┌───────────── day of the week (0-6) (Sunday to Saturday)
    # │ │ │ │ │
    # │ │ │ │ │
    # │ │ │ │ │
      * * * * * <command to execute>

That is, 5 fields that define the recurrence rule, and a command to execute.
The syntax also supports ranges and stepping values. Some examples:


.. code-block::
    :caption: Sample crontab entries

    # run every 15 minutes:
    */15 * * * * <my rapid command>

    # run every night at 23:04 (11:04 PM):
    4 23 * * * <my daily command>

    # 09:23 on every day-of-week from Monday through Friday.
    23 9 * * 1-5 <my weekday commands>

    # the first day of every-other month
    0 0 1 */2 * <my infrequent command>

The `crontab guru <https://crontab.guru/>`_ is a helpful research for cron.

.. seealso::

    :manpage:`crontab(5)`
        Online manual page for crontab.

    `Crontab guru`_
        A helpful resource for translating crontab time syntax into
        human-friendly time specifications, and other cron-related items
        including examples.

.. _rdhpcs_scrontab:

Slurm Crontab
=============

.. note::

    Scrontab times are in **UTC**.

The `Slurm crontab <https://slurm.schedmd.com/scrontab.html>`_
(:command:`scrontab`) tool combines same functionality as cron with the
resiliency of the batch system. Jobs are run on a pool of login nodes.  You can
also find and modify your scrontab job on any login node.

You can edit your scrontab script with ``scrontab -e``.  Once you save your
script, it will automatically be scheduled by the batch system.

You can view your existing scripts with ``scrontab -l``

The Slurm crontab has a similar format to the standard :ref:`crontab
<crontab-syntax>`.  However, you must specify a group of Slurm options using
``#SCRON``, similar to ``#SBATCH`` in standard :ref:`Slurm job scripts
<slurm-scheduler>`.  The options to ``#SCRON`` include most of the options
available to :command:`sbatch`.  More details are available in the
:manpage:`sbatch(1)` man page.


Example scrontab Script
-----------------------

Each script must include traditional Slurm :command:`sbatch` flags like ``-A``
(``--account``) and ``-t`` (``--time``) proceeded with ``#SCRON``. These
``#SCRON`` options must proceed any command to be run, even if the options are
the same as the previous command.

.. code-block:: shell
    :caption: Sample Slurm crontab

    #SCRON -p cron
    #SCRON -A <account>
    #SCRON -t 00:30:00
    #SCRON -o output-%j.out
    #SCRON --open-mode=append
    0 */3 * * * <full_path_to_your_script>

In the above example, the scrontab job script will run every three hours.


Long-running scrontab jobs
--------------------------

It is suggested that jobs running under scrontab are short-running.  However,
projects often need long-running processes to manage their work. Long-running
jobs are supported.  However, maintenance, login nodes going offline, or the
exceeding the wall time may interrupt these jobs.  Since it is desirable to
have these jobs restart, we recommend you set a start up time to be fairly
frequent and add the ``--dependency=singleton`` to the job's scrontab flags:

.. code-block:: shell

    #SCRON --partition=cron
    #SCRON --account=<account>
    #SCRON --time=16:00:00
    #SCRON --dependency=singleton
    #SCRON --name=my_data_movement_helper
    0 * * * * <full_path_to_your_script>

This means Slurm will check every hour whether an instance of your job is
running, and if not, it will start it.

Use singleton for long running jobs

.. warning::

    You must use ``--dependency=singleton`` for long running jobs to avoid
    Slurm starting multiple instances of the same job every time your scrontab
    file is edited.

Monitoring scrontab jobs
------------------------

You can monitor your scrontab jobs supplying the ``--me`` and ``--p
<parition>`` flags to :command:`squeue`:

.. code-block:: shell

    squeue --me -p cron -O JobID,EligibleTime

This will show the next time the batch system will run your job. If the
scrontab job is set to repeat, the system will automatically reschedule the
next job. Additionally, if you modify your scrontab job, Slurm will
automatically cancel the old job and resubmit a new one.

Canceling a scrontab job
------------------------

To remove a scrontab job from your running jobs, you can edit the scrontab file
with ``scrontab -e`` and comment out all the lines associated with the entry.

.. warning:: Using scancel on a scrontab job

    The :command:`scancel` command will give a warning when attempting to
    remove a job started with scrontab.

    .. code-block:: shell

        $ scancel 555
        scancel: error: Kill job error on job id 555: Cannot scancel a scrontab
        job without the --hurry flag, or modify scrontab jobs through scontrol

    Canceling a scrontab job with the ``--hurry`` flag will prepend
    ``#DISABLED`` to the entry in the scrontab file. These comments will need
    to be removed before the job will be able to start again.

Using scrontab to submit other batch jobs
-----------------------------------------

You can use scrontab to submit batch jobs at regular intervals, often as part
of a larger workflow. It is important to note that scrontab jobs set certain
Slurm-related environment variables which may be inherited by batch jobs
submitted from the scrontab job.

A notable example is that scrontab jobs may set ``SLURM_MEM_PER_CPU`` which can
cause errors when inherited into batch jobs, often of the form srun: error:
Unable to create step for job <id>: More processors requested than permitted.

A known workaround to avoid this is to set

.. code-block:: shell

    if [[ ! -z "${SLURM_MEM_PER_CPU}" ]]; then
    unset SLURM_MEM_PER_CPU
    unset SLURM_OPEN_MODE
    fi

in the scrontab file to handle that specific environment variable, or to use
``unset ${!SLURM_@};`` to unset all Slurm-related environment variables in the
file.

