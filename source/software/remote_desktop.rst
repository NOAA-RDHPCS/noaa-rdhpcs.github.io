##############
Remote Desktop
##############

While the command-line interface (SSH) is the primary method for interacting
with NOAA RDHPCS systems, many workflows require a graphical user interface
(GUI). A **Remote Desktop** provides a full, graphical window into the HPC
environment, allowing you to run visualization software, debuggers, and data
analysis tools as if you were sitting directly in front of a workstation at the
data center.

What is a Remote Desktop?
=========================

A remote desktop session allows you to view and interact with a desktop
environment (such as MATE or GNOME) running on an RDHPCS Front End (FE) or
visualization node. Unlike a standard SSH terminal which only transmits text, a
remote desktop transmits the display pixels and receives your mouse and
keyboard inputs.

We currently support Parallel Works ACTIVATE as our primary remote desktop
solution. ACTIVATE is similar to `Open OnDemandX2Go
<https://www.openondemand.org/>`_ as it is designed to perform well even over
low-bandwidth connections by compressing the graphical data efficiently, and
allows users to have a uniform interface across all the RDHPCS systems,
including the cloud-based systems.

When Should You Use It?
=======================

You should consider using a remote desktop session for the following workflows:

* **Data Visualization:** Running graphical applications like **Matlab**,
  **IDL**, **ParaView**, **Ncview**, or **VAPOR** to inspect model outputs
  without downloading massive datasets to your local machine.
* **Code Development:** Using graphical IDEs (e.g., VS Code, Eclipse) or visual
  debuggers (e.g., ARM Forge/DDT).
* **Session Persistence:** If your local internet connection drops, an X2Go
  session remains running on the server. You can reconnect later and find your
  open windows exactly where you left them.
* **Complex File Management:** Using a graphical file manager to organize or
  inspect directory structures.

Remote Desktop vs. SSH X11 Forwarding
=====================================

Users often ask why they cannot simply use `ssh -X` (X11 forwarding) to run
graphical applications. While X11 forwarding works for simple, lightweight
windows, it is inefficient for complex graphics.

+---------------------+-----------------------+------------------------+
| Feature             | SSH X11 Forwarding    | Remote Desktop         |
+=====================+=======================+========================+
| **Performance**     | Slow over WAN; sends  | Fast; sends compressed |
|                     | raw drawing commands. | images.                |
+---------------------+-----------------------+------------------------+
| **Persistence**     | Session dies if the   | Session stays alive    |
|                     | network drops.        | (suspend/resume).      |
+---------------------+-----------------------+------------------------+
| **Experience**      | Single window         | Full desktop           |
|                     | functionality.        | experience.            |
+---------------------+-----------------------+------------------------+
| **Best For**        | Simple plots,         | 3D Visualization, IDEs,|
|                     | text editors, (e.g.,  | IDEs, complex apps,    |
|                     | gvim, gedit).         | prolonged work.        |
+---------------------+-----------------------+------------------------+

.. important::

   Remote desktop sessions typically run on **Front End (FE)**, not on the
   compute nodes. These nodes are shared resources.

.. warning::

   Do not run heavy computational jobs (MPI jobs, massive compilations) inside
   your remote desktop terminal. Always submit heavy compute tasks to the
   scheduler (Slurm) using ``sbatch`` or ``salloc``.

Using ACTIVATE Remote Desktop
=============================

