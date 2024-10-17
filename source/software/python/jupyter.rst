.. _jupyter_on_rdhpcs_systems:

*************************
Jupyter on RDHPCS Systems
*************************

.. warning::

    Use of Jupyter on RDHPCS systems is considered user-installed software.  The
    RDHPCS help desk technicians can only offer minimal support.

Jupyter is a powerful tool enabling reproducible research and teaching. Use it
to create notebooks that contain both computer code and rich text elements
(paragraphs, equations, figures, widgets, links). This allows you to create
human-readable documents containing executable data analytics components,
results, and descriptions.

.. rubric:: JupyterLab

JupyterLab is a web-based interactive development environment for Jupyter. It
provide a way to use notebooks, text editors, terminals, and custom components
together. You can configure and arrange the user interface to support a wide
range of workflows in data science, scientific computing, and machine learning.

.. rubric:: JupyterHub

JupyterHub is a way to serve Jupyter Labs for multiple users within a project.
It is a multi-user Hub that spawns, manages, and proxies multiple selectable
instances of the single-user JupyterLab server.

JupyterLab
==========

Install JupyterLab
------------------

JupyterLab can be installed using either ``pip`` or ``conda install``.  In
either case, refer to :ref:`python-guides` and :ref:`conda-basics` for
information on creating a virtual environment for the JupyterLab installation.

To install JupyterLab, run the command:

.. tab-set::

   .. tab-item:: Pip
      :sync: pip

      .. code-block:: shell

        $ pip install jupyterlab

   .. tab-item:: Conda
      :sync: conda

      .. code-block:: shell

        $ conda install jupyterlab

.. note::

    The `JupyterLab maintainers <https://jupyter.org/install#jupyterlab>`__
    suggest using the `conda-forge channel <https://conda-forge.org/>`__ when
    installing JupyterLab via conda.

Starting JupyterLab
-------------------

To launch JupyterLab, activate the python environment and run the ``jupyter
lab`` command:

.. tab-set::

    .. tab-item:: Pip
       :sync: pip

       .. code-block:: shell

            $ source /path/to/venv/jupyter/bin/activate
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

    .. tab-item:: Conda
       :sync: conda

       .. code-block:: shell

            $ conda activate /path/to/venv/jupyter
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

The ``jupyter lab`` command will print many lines to the screen.  Look for
lines that resemble:

.. code-block:: shell

    To access the server, open this file in a browser:
        file:///path/to/jupyter/runtime/jpserver-12345-open.html
    Or copy and paste one of these URLs:
        http://localhost:<port#>/lab?token=################################################
        http://127.0.0.1:<port#>/lab?token=################################################

Take note of the the URL including the full token, you will need to paste it
into a browser's URL bar.

.. warning::

    Your Jupyter session may cause yours and your fellow users' performance to
    suffer if you do not run on the compute nodes.  It is always highly
    recommended to run on the compute nodes through the use of an interactive
    batch session.

Access the JupyterLab session
-----------------------------

The firewalls on the RDHPCS systems do not allow direct connection to the head
(login) or compute nodes.  To allow your locally running web browser to access
the JupyterLab service you will need to use the pre-established port tunnels.
There are a few additional steps to access a JupyterLab session that is running
on the compute nodes.

To access a JupyterLab session on a head node, you will need connect using two
local terminal sessions.  The first terminal session will establish the
user-assigned pre-established SSH port tunnels.  The second session will
establish an additional tunnels to allow the JupyterLab to connect to the
running JupyterLab port on the head or compute node.

.. note::

    The last command in the second session window will not give you a shell
    prompt on the HPC head node.

.. warning::

    Both terminal sessions must remain open and active.  Closing either window
    will terminate the tunnels, causing the connection to the JupyterLab session
    to stop working.

JupyterLab on Head Nodes
^^^^^^^^^^^^^^^^^^^^^^^^

window 1
""""""""

Login to the HPC system and establish your tunnel using your assigned user
local port number:

.. code-block:: shell

    $ ssh -L 12345:127.0.0.1:12345 J.Doe@<bastion>.rdhpcs.noaa.gov

Once logged in, start the JupyterLab session using a port number in the range
8800-8900 range:

.. tab-set::

    .. tab-item:: Pip
       :sync: pip

       .. code-block:: shell

            $ source /path/to/venv/jupyter/bin/activate
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

    .. tab-item:: Conda
       :sync: conda

       .. code-block:: shell

            $ conda activate /path/to/venv/jupyter
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

.. note::

    Take note of the URL provided to you by Jupyter for a later step.  It will
    resemble
    ``http://127.0.0.1:<port#>/lab?token=################################################``.
    You will need the full token number.

.. warning::

    Be aware that the port number assigned by Jupyter may be different
    than the one specified. This can occur when the chosen port is already
    in use. In this case, Jupyter will assign the next available port.
    If the port number changes, make note of it for the next command.

window 2
""""""""

Establish a tunnel for traffic on port ``<port#>`` used to launch the
JupyterLab session between your localhost and the RDHPCS system:

.. code-block:: shell

    $ ssh -p 12345 -L <port#>:127.0.0.1:<port#> J.Doe@127.0.0.1

.. note::

    This will not give you a prompt on the RDHPCS system.

Open your browser on your local machine, and navigate to the entire URL
(including the token) you noted above when you ran ``jupyter lab`` in window 1

JupyterLab on Compute Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

window 1
""""""""

Login to the HPC system and establish your tunnel using your assigned user
local port number:

.. code-block:: shell

    $ ssh -L 12345:127.0.0.1:12345 J.Doe@<bastion>.rdhpcs.noaa.gov

Start an interactive batch session.  On the compute node, use ``hostname`` to
get the name of the compute node.  This will be needed later:

.. code-block:: shell

    $ srun -A <project> -p <partition> -N 1 -t <time_limit> --pty bash -il
    srun: job 12345678 queued and waiting for resources
    srun: job 12345678 has been allocated resources
    $ hostname
    cn_host01

Start the JupyterLab session using a port number in the range 8800-8900 range:

.. tab-set::

    .. tab-item:: Pip
       :sync: pip

       .. code-block:: shell

            $ source /path/to/venv/jupyter/bin/activate
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

    .. tab-item:: Conda
       :sync: conda

       .. code-block:: shell

            $ conda activate /path/to/venv/jupyter
            $ jupyter lab --no-browser --port=<port#>  # Choose a port value between 8800-8900

.. note::

    Take note of the URL provided to you by Jupyter for a later step.  It will
    resemble
    ``http://127.0.0.1:<port#>/lab?token=################################################``.
    You will need the full token number.

.. warning::

    Be aware that the port number assigned by Jupyter may be different
    than the one specified. This can occur when the chosen port is already
    in use. In this case, Jupyter will assign the next available port.
    If the port number changes, make note of it for the next two commands.

window 2
""""""""

Establish a tunnel for traffic on port ``<port#>`` used to launch the
JupyterLab session between your localhost and the RDHPCS system:

.. code-block:: shell

    $ ssh -p 12345 -L <port#>:127.0.0.1:<port#> J.Doe@127.0.0.1

Once the connection is established, using the compute node host name establish
a connection to the compute node with tunnels to the JupyterLab session port:

.. code-block:: shell

    $ ssh -L <port#>:127.0.0.1:<port#> <cn_hostname>

.. note::

    This last SSH connection will not give you a prompt on the compute node.


Open your browser on your local machine, and navigate to the entire URL
(including the token) you noted above when you ran ``jupyter lab`` in window 1
