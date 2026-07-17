Gitlab Server
=============

..
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

NOAA RDHPCS provides a secure Git server (URL: https://git.rdhpcs.noaa.gov) and a
container registry (URL: https://registry.rdhpcs.noaa.gov) based on
a self-hosted Gitlab instance that is accessible only within
the NOAA network. The Gitlab instance
supports CI/CD pipelines that can run with self-hosted Gitlab Runners installed
on RDHPCS systems.

.. attention::

  Users need to use tunnels to access the NOAA RDHPCS Git server and the
  container registry from external machines such as personal laptops.


Web Access
----------
The Gitlab instance is accessed through the web to set up accounts,
create new projects, and configure settings for password-less
login for git and container registry. To access the Gitlab web interface from
a personal machine, first a tunnel has to be created followed by proxy setup
on your web browser.

Tunnel Setup
~~~~~~~~~~~~

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


Configure User Authentication for Command Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Private and internal projects hosted on the Gitlab require user
authentication when accessing the git repositories or container images.
The Gitlab instance does not support the Yubikey based
authentication from the command line. Instead, users are expected to
setup either SSH keys or a Personal Access Token (PAT).

SSH Keys
++++++++

SSH keys come in pairs and consist of a public and private key. Users typically
create them on the machine (client) from which the Gitlab server is accessed.
Each client machine requires its own set of SSH keys. The RDHPCS systems such
as Ursa and Hera have pregenerated SSH keys. Users have to upload the public
SSH key to the Gitlab server.
See `Use SSH keys with Gitlab <https://docs.gitlab.com/user/ssh/>`__
for detailed instructions.

Personal Access Token (PAT)
+++++++++++++++++++++++++++

PAT is useful to access the Gitlab API, container registry and for https based
git access. A PAT has to be created on the Gitlab server.

1. Click the user icon in the top-right corner and select **Edit Profile**.
2. In the left pane, click **Personal Access Tokens**.
3. Click **Add new token**.
4. Save the token in a secure location.

For detailed instructions on PAT, refer to the
`PAT documentation <https://docs.gitlab.com/user/profile/personal_access_tokens/>`__.

.. warning::

   PAT can only be accessed once after creation. Store it promptly.


Gitlab Project
~~~~~~~~~~~~~~

A git repository is designated as a Project on Gitlab server. Container images
stored in the container registry are associated with a Gitlab project. If users
want to upload a container image or create a new git repository, a Gitlab
project has to be created.  When creating a new project, the user may be asked
whether to use the user name or a group name as the namespace.  Unless the
project belongs to a group, use the user name.

A Gitlab project has three visibility levels: private, internal, and public.
A private project can only be accessed by the owners of the project who could
be a single user or a group owining the project.
If a repository or container images need to be shared to the RDHPCS users, the
associated project needs to have either internal or public visibility.
Because Gitlab server is accessible only from RDHPCS network, internal and
public visibility levels serve similar purpose except accessing public projects
do not require authentication to the Gitlab server. If the intent is to make a
project accessible to all the NOAA users, it is recommended to use
public visibility for a project instead of internal visibility.


Git Usage
---------

Git access is typically through a git client, (either git or glab commands on CLI
or an IDE such as VSCode) on the RDHPCS system. The URL for the git repo on
the git server is dependent on whether ssh or https protocol is used. User
id and PAT have to be supplied if https protocol is used. SSH protocol enables
password-less connection through SSH keys. To learn more about git, refer
to `git documentation <https://git-scm.com/>`__.

GitLab CLI (glab)
~~~~~~~~~~~~~~~~~

GitLab CLI tool named glab is installed on the RDHPCS systems. Using glab,
users can perform actions such as repository creation on the Git server,
cloning the repository, etc. The first step in using the GitLab CLI is 
authenticating the GitLab server.

.. code-block:: bash

   glab auth login --hostname https://git.rdhpcs.noaa.gov --token <YOUR_PAT_TOKEN>

By default glab command defaults to https://gitlab.com. To use the RDHPCS
git server, set the environment variable GITLAB_HOST.

.. code-block:: bash

   export GITLAB_HOST=https://git.rdhpcs.noaa.gov

To make it permanent add the above line to your ``~/.bashrc`` file and then
source the file or log in again. Users can add the SSH keys from the command line. 

.. code-block:: bash
 
   glab ssh-key add ~/.ssh/id_rsa.pub -t "<rdhpcs_machine_name>" --usage-type "auth"

Glab can be used to create a repo under user account.

.. code-block:: bash

   glab repo create <project-name>

To create the same repo under a group, run the below command.

.. code-block:: bash

   glab repo create <group-name>/<project-name>

All the repos owned by the user in the Git server can be listed by running the
below command.

.. code-block:: bash

   glab repo list 

A repo can be cloned using glab. Users can supply the full URL or they can 
supply the path shown in the ``glab repo list`` command. The path is usually
``<account-name or group-name>/<project-name>``.

.. code-block:: bash

   glab repo clone <path-to-repo>

For additional information on the GitLab CLI, refer to the `glab 
documentation <https://docs.gitlab.com/cli/>`__.

Similar to glab, GitHub CLI tool (gh) is also available on the RDHPCS
systems. Refer to the `gh documentation <https://cli.github.com/>`__
for additional information.


.. include:: gitlab_ci_cd_pipelines_and_runners.rst


Container Registry
------------------

The container registry is accessible at https://registry.rdhpcs.noaa.gov.

.. Users can use Apptainer on an RDHPCS system to:

    - Pull container images directly from GitLab's OCI/Docker registry.
    - Convert them into ``.sif`` (Singularity Image Format) files.
    - Run them securely without root privileges.
    - Authenticate using GitLab Personal Access Tokens.


Configuration on RDHPCS system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Registry Login
~~~~~~~~~~~~~~
A container image hosted on a registry can be either publicly accessible or
accessible only after authentication on the registry. For pushing images,
authentication is mandatory. To authenticate to the registry, first ensure
you have account on the Gitlab server. Then authenticate to the registry
using apptainer.

.. code-block:: bash

   apptainer registry login -u user.name oras://registry.rdhpcs.noaa.gov

Enter your PAT when prompted.

Image pull and push
~~~~~~~~~~~~~~~~~~~

Image Pull
++++++++++

1. Example using alpine linux docker image from DockerHub:

   .. code-block:: bash

      apptainer pull docker://alpine:latest

   For docker images :code:`docker://` prefix is needed. If the image name
   does not to supply any registry URL, DockerHub registry is used. Running
   the above command creates ``alpine_latest.sif`` in the working directory.

2. Assuming an alpine linux SIF image is stored on the RDHPCS registry,

   .. code-block:: bash

       apptainer pull \
         oras://registry.rdhpcs.noaa.gov/user.name/user_project/alpine:latest

   In the above command, :code:`user.name/user_project` represents the project
   under which the image is stored. Since the image is in SIF format,
   :code:`oras://` prefix is needed.

3. A custom local image name can also be used as shown below.

   .. code-block:: bash

       apptainer pull my_image.sif \
         docker://registry.rdhpcs.noaa.gov/group/project/<image>:<tag>

   When the above command is executed, instead of :code:`image_tag.sif`,
   :code:`my_image.sif` is created in the working directory.

Push Image to the RDHPCS container registry
+++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

   apptainer push alpine_latest.sif \
     oras://registry.rdhpcs.noaa.gov/user.name/project/alpine:latest

This assumes :code:`user.name/project` already exists on the Gitlab server.
At a more advanced level, CI/CD pipelines are used to build and push the
containers to the registry as part of the software release cycle.

