NOAA RDHPCS Git Server
=========================

Git is a popular software version control system designed to help developers track changes in source code,
manage multiple versions of files, and collaborate efficiently across teams. Git follows a distributed
design and allows every user to maintain a complete copy of the repository history, making development
faster, more flexible, and resilient. A Git server builds on these capabilities by providing a
centralized platform to host, manage, and share Git repositories, enabling teams and individuals to
collaborate more effectively on software development projects. It offers a secure and organized
environment for maintaining project history, managing branches, controlling access, reviewing code, and
integrating with other development tools, making it an essential component of modern software development
and delivery workflows. NOAA provides a secure Git server based on self-hosted Gitlab that is accessible
only from the RDHPCS systems. In addition to providing a Git server, the Gitlab also offers self hosted
CI/CD pipelines as well as artifact/container registry, both of which are very useful for NOAA software
developers.

Web Access
----------
Initial access to the Git server has to be done through web to setup account, create new repos, and
configure settings for password-less login for git and container registry. There are two methods to
access the Git server web interface via tunnels.

SSLVPN
~~~~~~

.. image:: /images/gitserver1.png
   :alt: VPN portal showing the Create new book workflow for the Git server.
   :width: 700px

1. Log in to `sslvpn.rdhpcs.noaa.gov <https://sslvpn.rdhpcs.noaa.gov>`__ and click **Create new bookmark for
   Your.Name@noaa.gov**. In the pane that opens, fill the two fields shown below, leave the remaining fields
   blank, and then press the **OK** button.

   - **Name:** ``Git Server``
   - **URL:** ``https://git.rdhpcs.noaa.gov``

   .. note::

     Including ``https://`` in the URL is required.


2. Click the **Bookmarks** tab for ``Your.Name@noaa.gov`` and then select the newly created **Git Server**
   widget. A new browser tab should open and point to the Git server.

   .. image:: /images/gitserver2.png
      :alt: Bookmarks tab showing the Git Server entry.
      :width: 700px

Manual Tunnel
~~~~~~~~~~~~~

1. Set up a tunnel to any RDHPCS machine:

   .. code-block:: bash

      ssh -D <port-no> User.Name@bastion.<princeton/boulder>.rdhpcs.noaa.gov

2. Configure browser proxy settings. Check your browser documentation on how to modify the proxy settings.
   In the example below, Mozilla Firefox with a tunneling port number ``9999`` is used.

   .. image:: /images/gitserver3.png
      :alt: Firefox network proxy settings for SOCKS tunnel access.
      :width: 650px

3. Open ``https://git.rdhpcs.noaa.gov`` in the browser. You should see the GitLab server with NOAA SAML SSO.
   Sign in with your NOAA credentials and complete MFA using your YubiKey.


Git Usage
---------

Git Repo Creation
~~~~~~~~~~~~~~~~~

Git repository have to be created from the browser. When creating a project, GitLab may ask whether
to use your username or a group name as the namespace.  In this document, let us assume the first
project created is ``User.Name/first_project``.

Git Client Access
~~~~~~~~~~~~~~~~~
Git access is typically through a git client (git command or IDE) on the RDHPCS system. The URL for
the git repo on the  git server is dependent on whether ssh or https protocol is used. Login and
password details have to be supplied if https protocol is used and it would be tedious to supply
login credentials all the times. SSH protocol enables password-less connection through SSH keys.
They are created on the client and then added to your account on the Git server.

Register an SSH key
+++++++++++++++++++
1. On the RDHPCS system, from which the user wants to connect to the Git server, generate an SSH
   key pair using ``ssh-keygen`` command. Various options can be passed to the ``ssh-keygen``
   command such as key-type with ``-t`` flag. Some of the popular key types are ``rsa`` and ``ed25519``.
   Depending on the key type selected, the command typically creates files such as ``$HOME/.ssh/id_rsa``
   and ``$HOME/.ssh/id_rsa.pub`` or similar files for other key types.
2. Copy the contents of the ``.pub`` file.
3. On the Git server website, click on the project, and then click on **SSH Keys** from the left pane.
4. Click **Add new key** button.
5. Paste the public key, provide a title such as the hostname where the key was created, and click **Add key**.

More details can be found in the GitLab documentation available at:
`GitLab user authentication docs <https://docs.gitlab.com/auth/user_authentication/>`__.


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
^^^^^^^^^^^^^^^^^^^^^^^^

Add the following line to ``singularity.conf`` or ``apptainer.conf``:

.. code-block:: ini

   mksquashfs procs = 4

Configure the Apptainer cache directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, Apptainer uses the home directory for cache storage. On multi-user RDHPCS systems,
home directories are often too small, so use a scratch location instead:

.. code-block:: bash

   export APPTAINER_CACHEDIR=/scratch[3-5]/<project-path>/User.Name/apptainer_cache_dir

You can also place this command in ``~/.bashrc`` and then source the file or log in again.

.. note::

   Choose one of ``/scratch3`` through ``/scratch5``.
   ``/scratch3`` and ``/scratch4`` are available on both Hera and Ursa.
   ``/scratch5`` is available only on Ursa.

Image pull and push
~~~~~~~~~~~~~~~~~~~

Step 1: Pull an image from a public Docker registry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example using ``alpine:latest``:

.. code-block:: bash

   apptainer -c singularity.conf pull docker://alpine:latest

This creates ``alpine_latest.sif`` in the current working directory.

Step 2: Create a PAT on the GitLab server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Click the user icon in the top-right corner and select **Edit Profile**.
2. In the left pane, click **Personal Access Tokens**.
3. Click **Add new token**.
4. Save the token in a secure location.

.. warning::

   You can view the PAT only once after creation.


Step 3: Log in to the GitLab registry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   apptainer registry login -u User.Name oras://git.rdhpcs.noaa.gov:5050

Enter your PAT when prompted.

Step 4: Push the Apptainer image to the GitLab server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   apptainer push alpine_latest.sif \
     oras://git.rdhpcs.noaa.gov:5050/User.Name/first_project/alpine:latest

This assumes ``User.Name/first_project`` already exists on the GitLab server. At a more advanced
level, CI/CD pipelines are used to build and push the containers to the registry as part of the
software release cycle.

Step 5: Pull images from the GitLab server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After uploading, you can remove the local file and pull it again from the registry:

.. code-block:: bash

   apptainer pull \
     oras://git.rdhpcs.noaa.gov:5050/User.Name/first_project/alpine:latest

This creates ``alpine_latest.sif`` in the working directory.

To use a custom local image name:

.. code-block:: bash

   apptainer pull my_alpine_image.sif \
     docker://git.rdhpcs.noaa.gov:5050/group/project/image:<tag>

