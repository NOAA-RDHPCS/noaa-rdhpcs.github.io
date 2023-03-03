.. _connecting:

##########
Connecting
##########

This simple overview explains the elements of a basic job in Gaea. It includes compiling, running, combining, data transfer, and allocation.

Compiling 
----

Gaea offers PrgEnv-intel, Prg-Env-pgi, and several other modules that make it as easy as possible to get your programs running . PrgEnv-pgi is loaded by default. You compile by calling either cc or ftn, according to the language your code is written in. See Compilers for more detail, especially for compiling multithreaded applications.

You may either compile live in your login shell on a Gaea login node, or in a job in the eslogin queue in the es partition of Gaea's batch system. To tell a job script to run on the login nodes, specify the following in your script:

`#SBATCH --clusters=es
#SBATCH --partition=eslogin
#SBATCH --ntasks=1 `

or, from the sbatch command line:

`sbatch --clusters=es --partition=eslogin --ntasks=1 /path/to/compile_script`

Running
---

Once your executable is compiled and in place with your data on F2, you are ready to submit your compute job. Please submit your compute job to either c3 or c4.

`#SBATCH --clusters=c3
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=32 # Gaea charges for node use.  Nodes are 32 cores on c3 and 36 core on c4.  This example will get charged for 4 nodes.

or, from the sbatch command line:

`sbatch --clusters=c3 --nodes=4 --ntasks-per-node=32 /path/to/run_script
sbatch --clusters=c4 --nodes=4 --ntasks-per-node=36 /path/to/run_script`

Your compute job script will run on one of the compute nodes allocated to your job. To run your executable on them use the srun or srun-multi command. Your executable and data must reside on F2 as only lustre filesystems are mounted on the compute nodes. Also, your job's PWD should be in F2 when you run srun or srun-multi. A simple example is shown below:

`cd /lustre/f2/scratch/$user/
srun-multi --nodes=128 --ntasks-per-node=32 /lustre/f2/scratch/$user/path/to/executable`

Staging/Combining
----

Staging data to and from model run directories is a common task on Gaea. So is combining model output when your model uses multiple output writers for scalability of your MPI communications. The Local Data Transfer Nodes (LDTNs) are the resource provided for these tasks. Please keep these tasks off of the c3/c4 compute clusters and eslogin nodes. There is a NOAA-developed tool called gcp which is available for data transfers on Gaea. To tell a job script to run on the LDTN nodes, specify the following in your script:

`#SBATCH --clusters=es
#SBATCH --partition=ldtn
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1 #set ntasks-per-node to the number of cores your job will need, up to 16

or, from the sbatch command line:

`sbatch --clusters=es --partition=ldtn --nodes=1 --ntasks-per-node=1 /path/to/staging_script

Transferring Data to/from Gaea
----

Data transfers between Gaea and the world outside of Gaea should be performed on the Remote Data Transfer Nodes (RDTNs). There is a NOAA-developed tool called gcp, which is available for data transfers on Gaea. HPSS users are only able to access HPSS from jobs on the RDTNs. To tell a job script to run on the login nodes, specify the following in your script:

#SBATCH --clusters=es
#SBATCH --partition=rdtn
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1 #set ntasks-per-node to the number of cores your job will need, up to 8

or, from the sbatch command line:

sbatch --clusters=es --partition=rdtn --nodes=1 --ntasks-per-node=1 /path/to/trasfer_script

Allocation
----

Gaea users have default projects. If you are only a member of a single project, or if your experiments always run under your default project, you don't need to do anything special to run. Users who are members of more than one project need to enter their preferred project via the --account option to sbatch to correctly charge to each experiment's project.

You can use AIM to request access to new projects. Once access is granted in AIM it can take up to two days to be reflected in Gaea's Slurm scheduler. If you still don't have the granted access after two days, please put in a help desk ticket so admins can investigate your issue. To determine your Slurm account memberships, run the following command:
sacctmgr list associations user=First.Last

To submit jobs to the scheduler under a specific account do the following from the sbatch command line:

> sbatch --account=gfdl_z

or add the following to your job script's #SBATCH headers:

`#SBATCH --account=gfdl_z

Running a Simple Job
----

Here's an example of a basic script to run on Gaea. It is a skeleton script for c1:c2 to help users who don't have access to, or prefer not to use, a workflow manager. This script copies everything in the experiment subdirectory from ltfs to fs, runs the experiment, and then copies the changed and new files from fs to ltfs.

Running the Script
---

This script assumes that the data and executable are staged to /lustre/ltfs/scratch/$USER/$experiment_subdir. The scripts and data are located at /usw/user_scripts/
Use gcp to get the skeleton script from /usw/user_scripts/c1_c2_skeleton to your local home directory:

gcp /usw/user_scripts/c1_c2_skeleton ~$USER/

Use gcp to get other files from /usw/user_scripts/ to your f1 directory
gcp -r /usw/user_scripts/ /lustre/f1/$USER/c1_c2_skeleton

Open the skeleton script. (The comments in the script will help you understand what each item does.)

vim ~$USER/c1_c2_skeleton

Users MUST modify the paths in the '#PBS -d' line and the walltime in the '#PBS -l walltime' line. (i.e /lustre/f1/First.Last/ for -d, and walltime can be set to 20 min for this tutorial)
WARNING do not use environment variables like $USER in setting the directory as it will not be available at run time for the script
now go to your home directory and submit your job
msub c1_c2_skeleton

Once the job is submitted
Once the job is submitted, you can use these commands to check on your job:
To view the status of your job
showq -u $USER

The -c flag will show jobs that have completed with exit codes
showq -u $USER -c

To to check a detailed status of your job replace "jobid" with your job's id. For example: checkjob gaea.123456789. Additionally you add an option, -v, to get more information.
checkjob jobid

Once the job is Finished
Once your job is finished you will have a output file in your directory /lustre/f1/$USER
You should have a log file (ex. c1_c2_skeleton_gaea.8279963)
You should have a folder with the output files (ex. 6307731.c2-sys0.ncrc.gov/c1_c2_skeleton_gaea.8279963/)


.. toctree::
   :maxdepth: 2
