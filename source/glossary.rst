.. _glossary:

Glossary
========

.. glossary::

    compute node
        A node type where parallel and threaded applications should be run.
        These nodes typically have large core counts, and a high amount of
        memory per core.  The :command:`srun` is typically used to launch
        parallel jobs on these nodes.

    data transfer node
        A node type that is configured for the transfer of data files across
        local and remote file systems.

    :abbr:`DTN (data transfer node)`
        See :term:`data transfer node`.

    front-end node
        See :term:`login node`.

    login node
        A node type that is mainly used for interactive, and single threaded
        application usage.  This is the node type where users are placed when
        accessing a system.

    Slurm
        An open source cluster management and job scheduling system.
