NOAA RDHPCS Git Server
=========================

Git is a popular software version control system designed to help
developers track changes in source code, manage multiple versions
of files, and collaborate efficiently across teams. Git follows a
distributed design and allows every user to maintain a complete
copy of the repository history, making development faster, more
flexible, and resilient. A Git server builds on these capabilities
by providing a centralized platform to host, manage, and share Git
repositories, enabling teams and individuals to collaborate more
effectively on software development projects. It offers a secure
and organized environment for maintaining project history, managing
branches, controlling access, reviewing code, and integrating with
other development tools, making it an essential component of modern
software development and delivery workflows. 

NOAA provides a secure
Git server based on self-hosted Gitlab that is accessible only from
the RDHPCS systems. In addition to providing a Git server, the Gitlab
also offers rtifact/container registry and supports self-hosted CI/CD
pipelines, both of which would be useful for NOAA software developers.

Web Access
----------
The Git server is accessed through the web, to set up accounts,
create new repos, and configure settings for password-less
login for git and container registry. 

Manual Tunnel
~~~~~~~~~~~~~

1. Set up a tunnel to any RDHPCS machine:

   .. code-block:: bash

      ssh -D <port-no> User.Name@bastion.<princeton/boulder>.rdhpcs.noaa.gov

2. Configure browser proxy settings. Check your browser documentation on
   how to modify the proxy settings. In the example below, Mozilla Firefox
   with a tunneling port number ``9999`` is used.

   .. image:: /images/gitserver3.png
      :alt: Firefox network proxy settings for SOCKS tunnel access.
      :width: 650px

3. Open ``https://git.rdhpcs.noaa.gov`` in the browser. You should see the
   Git server with NOAA sigon button. Sign in with your NOAA credentials
   and complete MFA using your YubiKey.


Git Usage
---------

Git Repo Creation
~~~~~~~~~~~~~~~~~

Git repositories must be created from the browser. When creating a project,
the user may be asked whether to use the username or a group name as the namespace.
If the project does not belong to a group, use the username. This
document assumes that the first project created is
``User.Name/first_project``.

Git Client Access
~~~~~~~~~~~~~~~~~
Git access is typically through a git client, (either git command on CLI
or IDE) on the RDHPCS system. The URL for the git repo on the  git server
is dependent on whether ssh or https protocol is used. Login and password
details have to be supplied if https protocol is used, and it would be
tedious to supply login credentials all the times. SSH protocol enables
password-less connection through SSH keys. They are created on the client
and then added to your account on the Git server.

Register an SSH key
+++++++++++++++++++

Connection with the Git servier requires SSH keys. See
`Use SSH keys with Gitlab <https://docs.gitlab.com/user/ssh/>`__
for detailed instructions.

Container Registry Usage with Apptainer
---------------------------------------

Users can use Apptainer on an RDHPCS system to:

- Pull container images directly from GitLab's OCI/Docker registry.
- Convert them into ``.sif`` (Singularity Image Format) files.
- Run them securely without root privileges.
- Authenticate using GitLab Personal Access Tokens.


Configuration on RDHPCS system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure ``mksquashfs``
++++++++++++++++++++++++

Add the following line to ``singularity.conf`` or ``apptainer.conf``:

.. code-block:: ini

   mksquashfs procs = 4

Configure the Apptainer cache directory
+++++++++++++++++++++++++++++++++++++++

By default, Apptainer uses the home directory for cache storage. On
multi-user RDHPCS systems, home directories are often too small, so
use a scratch location instead:

.. code-block:: bash

   export APPTAINER_CACHEDIR=/scratch[3-5]/<project-path>/User.Name/apptainer_cache_dir

You can also place this command in ``~/.bashrc`` and then source the
file or log in again.

.. note::

   Choose one of ``/scratch3`` through ``/scratch5``.
   ``/scratch3`` and ``/scratch4`` are available on both Hera and Ursa.
   ``/scratch5`` is available only on Ursa.

Create a Personal Access Token (PAT) on the GitLab server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click the user icon in the top-right corner and select **Edit Profile**.
2. In the left pane, click **Personal Access Tokens**.
3. Click **Add new token**.
4. Save the token in a secure location.

.. warning::

   You can view the PAT only once after creation.

Image pull and push
~~~~~~~~~~~~~~~~~~~

Step 1: Pull an image from a public registry
++++++++++++++++++++++++++++++++++++++++++++

Example using ``alpine:latest``:

.. code-block:: bash

   apptainer -c singularity.conf pull docker://alpine:latest

This creates ``alpine_latest.sif`` in the current working directory.

Step 2: Log in to the GitLab registry
+++++++++++++++++++++++++++++++++++++

.. code-block:: bash

   apptainer registry login -u User.Name oras://git.rdhpcs.noaa.gov:5050

Enter your PAT when prompted.

Step 3: Push the Apptainer image to the Git server
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

   apptainer push alpine_latest.sif \
     oras://git.rdhpcs.noaa.gov:5050/User.Name/first_project/alpine:latest

This assumes ``User.Name/first_project`` already exists on the Git server.
At a more advanced level, CI/CD pipelines are used to build and push the
containers to the registry as part of the software release cycle.

Step 4: Pull images from the Git server
+++++++++++++++++++++++++++++++++++++++

After uploading, you can remove the local file and pull it again from the
registry:

.. code-block:: bash

   apptainer pull \
     oras://git.rdhpcs.noaa.gov:5050/User.Name/first_project/alpine:latest

This creates ``alpine_latest.sif`` in the working directory.

A custom local image name, for example ``my_alpine_image``, can also be
used as shown below.

.. code-block:: bash

   apptainer pull my_alpine_image.sif \
     docker://git.rdhpcs.noaa.gov:5050/group/project/image:<tag>

