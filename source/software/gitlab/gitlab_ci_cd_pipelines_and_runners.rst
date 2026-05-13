
GitLab CI/CD Pipelines
----------------------

GitLab CI/CD pipelines automate the process of building, testing, validating,
and deploying application code whenever changes are pushed to a git repository.
A pipeline is defined in a file named ``.gitlab-ci.yml`` at the root of the
git repository. This file contains stages, jobs, scripts, variables, and rules that
control how the automation runs.

A typical pipeline is organized into stages such as ``build``, ``test``, and
``deploy``. Each stage can contain one or more jobs. Jobs in the same stage can
run in parallel, while stages usually run in order. For example, the test stage
runs only after the build stage completes successfully, and the deploy stage
runs only after the test stage passes.

Pipelines help teams maintain consistent delivery practices by reducing manual
steps, catching errors early, and ensuring that code is validated before it
reaches production or another target environment.

Example ``.gitlab-ci.yml`` Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example shows a simple pipeline with three stages: build, test, and deploy.

.. code-block:: yaml

   stages:
     - build
     - test
     - deploy

   build_job:
     stage: build
     script:
       - echo "Building the application..."
       - mkdir -p build
       - echo "Build output" > build/output.txt
     artifacts:
       paths:
         - build/

   test_job:
     stage: test
     script:
       - echo "Running tests..."
       - test -f build/output.txt
       - echo "Tests completed successfully."

   deploy_job:
     stage: deploy
     script:
       - echo "Deploying the application..."
       - echo "Deployment completed."
     only:
       - main

In this example:

* ``stages`` defines the order of execution.
* ``build_job`` creates a build artifact.
* ``test_job`` checks that the build output exists.
* ``deploy_job`` runs only when changes are pushed to the ``main`` branch.
* ``artifacts`` allows files created in one job to be passed to later stages.

This type of pipeline can be expanded to include application compilation, unit tests,
code quality checks, security scans, container image builds, and deployment to
development, staging, or production environments.

GitLab Runners
--------------

A GitLab Runner is an agent that executes the jobs defined in a GitLab CI/CD
pipeline. When a pipeline starts, GitLab assigns each job to an available runner.
The runner checks out the repository, executes the job script, collects artifacts,
and sends the job result back to GitLab.

Runners can be installed on RDHPCS systems such as Hera and Ursa.
Users are advised to two executor types, either shell, or a custum slurm executor
from https://github.com/Algebraic-Programming/slurm-gitlab-executor.
The executor determines the environment in
which pipeline jobs run.

The ``shell`` executor runs CI/CD job commands directly on the login node using
the user configured shell, such as Bash. This executor is simple to configure and
useful when pipelines are run occassionally. Shell executor provides direct access
to tools, scripts, directories, compilers, or system-level utilities already
installed on the RDHPCS cluster.

However, because shell executor jobs run directly on the login node, they should be
used sparingly so as to not overwhelm the login nodes. 

Installing GitLab Runner on RDHPCS systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gitlab Runners can be installed at user scope on RDHPCS systems. The following example
shows a common installation flow targeting an RDHPCS cluster.

.. code-block:: bash
   
   # Create a folder in /scratch3 or /scratch4 under appropriate project directory or
   # in your home directory
   mkdir -p <target_folder>/bin

   # Add the folder to the PATH environment variable. For permanency between logins
   # add the below line to your shell configuration file if your shell is bash or zsh
   export PATH=$PATH:<target_folder>/bin

   # For C-style shells use
   setenv PATH $PATH:<target_folder>/bin

   # Download the GitLab Runner binary
   curl -L --output <target_folder>/bin/gitlab-runner "https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/latest/binaries/gitlab-runner-linux-amd64"

   # Give Permissions to execute GitLab Runner
   chmod +x <target_folder>/bin/gitlab-runner


Registering a Runner with Shell Executor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before registering the runner, create or obtain a runner authentication token from GitLab.

In GitLab, go to the project or group where the runner should be registered:

* Project-level runner: ``Project`` > ``Settings`` > ``CI/CD`` > ``Runners``
* Group-level runner: ``Group`` > ``Settings`` > ``CI/CD`` > ``Runners``

Then register the runner on the server.

.. code-block:: bash

   gitlab-runner register

During registration, provide the requested values.

.. code-block:: text

   Enter the GitLab instance URL:
   https://git.rdhpcs.noaa.gov

   Enter the runner authentication token:
   <runner-token-from-gitlab>

   Enter a description for the runner:
   shell-runner-server

   Enter tags for the runner:
   ursa or hera to specify machine or some other tag

   Enter an executor:
   shell

After registration, the runner configuration is stored in:

.. code-block:: text

   $HOME/.gitlab-runner/config.toml 

A shell executor runner configuration may look similar to this:

.. code-block:: toml

   [[runners]]
     name = "shell-runner-server"
     url = "https://git.rdhpcs.noaa.gov"
     token = "RUNNER_TOKEN"
     executor = "shell"
     [runners.cache]
       MaxUploadedArchiveSize = 0


Users can register multiple runners with different tags and names.

Running the Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After registration, the runner can only be run in the user mode.

.. code-block:: bash

   gitlab-runner run

To check runner status from GitLab, return to the project or group runner settings page.
The runner should appear as available or online.

Using Runner Tags in a Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a runner is registered with tags, pipeline jobs can target that runner by using the
same tags in ``.gitlab-ci.yml``.

.. code-block:: yaml

   stages:
     - test

   shell_test_job:
     stage: test
     tags:
       - ursa
     script:
       - echo "This job runs on a shell executor runner."
       - hostname
       - whoami
       - pwd

The ``tags`` section ensures that the job runs only on a runner that has matching tags.
This is useful when a particular job needs to run on a particular cluster or when different
runners are configured for different purposes, such as builds, deployment jobs, or
high-performance workloads. The above pipeline can only run on a runner with a ``ursa`` tag.

Shell Executor Best Practices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the shell executor, follow these practices:

* Use shell runners only for projects that do not get developed actively.
* Try to avoid running untrusted code.
* Use runner tags to control which jobs can use the runner.
* Clean temporary files and workspace data.
* Store sensitive values as GitLab CI/CD variables instead of hardcoding them in scripts.

Custom Slurm Executor
~~~~~~~~~~~~~~~~~~~~~

The ``shell`` executor can overwhelm the login nodes for high velocty projects. For such 
cases, ``service`` partition can be used to run CI/CD pipelines. Users have to install a 
`custom slurm executor <https://github.com/Algebraic-Programming/slurm-gitlab-executor>`__
and update the gitlab runner to use the slurm executor. Users can refer to the
`instructions <https://github.com/Algebraic-Programming/slurm-gitlab-executor/blob/master/README.md>`__
to set up the slurm executor. In the end update the final runner configuration to point
``builds_dir`` and ``cache_dir`` variables to directories in either ``/scratch3`` or ``/scratch4``.

.. code-block:: yaml

   [[runners]]
      executor = "custom"
      ...
      builds_dir = "/scratch[3,4]/path/builds"
      cache_dir = "/scratch[3,4]/path/cache"

Slurm variables have to be specified in the ``.gitlab-ci.yml`` file to generate an appropriate sbatch
script that can be launched by the slurm executor. Slurm variables shown below are appropriate 
for the ``u1-service`` partition on Ursa cluster.

.. code-block:: yaml
   
   variables:
      CI_SLURM_ACCOUNT:
        value: "your_noaa_project"
        description: "Slurm account to use"
      CI_SLURM_PARTITION:
        value: "u1-service"
        description: "Slurm partition to use"
        options: ["u1-service"]
      CI_SLURM_MEM_PER_NODE:
        value: "100G"
        description: "Maximum memory allowed on u1-service is 250G"
      CI_SLURM_NNODES: 
        value: "1"
        description: "Number of nodes"
      CI_SLURM_NTASKS: 
        value: "1"
        description: "Number of tasks"
      CI_SLURM_CPUS_PER_TASK: 
        value: "8"
        description: "Maximum number cores allowed is 63"
      CI_SLURM_QOS:
        value: "batch"
      CI_SLURM_TIMELIMIT:
        value: "00-08:00:00" # 0 days, 8 hour, 0 minutes, 0 seconds
        description: "Max time limit of batch qos is 8 hours (format: days-hours:minutes:seconds)"
      RUNNER_SCRIPT_TIMEOUT: 8h

