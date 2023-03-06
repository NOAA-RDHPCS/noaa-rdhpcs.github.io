.. toctree::
   :maxdepth: 2

##########
SLURM Tips
##########

Please be aware that Gaea is not like a usual Slurm cluster.  Slurm expects that all nodes are homogeneous and capable of being used for any purpose.  Gaea is a heterogeneous set of clusters (hence the need to specify a cluster as shown below.)  This also means that partitions (queues) for resources with different purposes will need to set up your job's environment to provide access to the software for that purpose.(data transfer nodes being chief among these.)  Under Slurm your job will only have the system shell init scripts run if you specify --exportNONE.  The result is that --exportNONE is a required argument to get your job to see software specific to a given node type, e.g. HSI/HTAR for HPSS on the data transfer nodes.

For general information about SLURM, see [https://rdhpcs-common-docs.rdhpcs.noaa.gov/wiki/index.php/Introduction_to_SLURM Introduction to SLURM] and subsequent topics in the Commondocs pages.

To find the accounts to which you belong


sacctmgr show assoc where user$USER formatcluster,partition,account,user%20,qos%60

### To c3:

sbatch --clustersc3 --nodes1 --accountgfdl_z --qosnormal --exportNONE /path/to/job/script

### To c3, but urgent 

sbatch --clustersc3 --nodes1 --accountgfdl_z --qosurgent --exportNONE /path/to/job/script

### To c4: 

sbatch --clustersc4 --nodes1 --accountgfdl_z --qosnormal --exportNONE /path/to/job/script

### To the LDTNs: 

sbatch --clusterses --partitionldtn --nodes1 --ntasks-per-node1 --accountgfdl_z --qosnormal --exportNONE /path/to/job/script

### To the RDTNs: 

sbatch --clusterses --partitionrdtn --nodes1 --ntasks-per-node1 --accountgfdl_z --qosnormal --exportNONE /path/to/job/script

### To submit interactive work to c3: 

salloc --clustersc3 --qosinteractive --nodes1 --x11

If you’re using x2go the X forwarding won’t work without the following workaround: gsissh -XY to another gaea login node and then run salloc.

### Running your models: 

In your c3 job scripts or interactive sessions you will want to run your model executable. If your model is simple (single component, etc) then use srun. If it is a coupled model or otherwise has multiple execution contexts and/or executables, you will need to use srun-multi.

srun ./executable

srun-multi --ntasks1 --cpus-per-task32 ./executable : --ntasks 128 --cpus-per-task1 ./executable

### Note: 

We are working an issue where modulecmd is not initialized in all shells. If you find that modulecmd is missing, add the following to your job script:

source /opt/modules/default/init/&lt;your_job_script_shell_type&gt;

Monitoring your jobs
----

### Shell Setup 

Do not set these in jobs/shells you intend to submit work from as they will override your job submission script #SBATCH directives, causing warnings and errors. Use them in shells you intend to monitor jobs from.

### In [t]csh: 

setenv SLURM_CLUSTERS t4,c3,c4,gfdl,es

### In bash: 

export SLURM_CLUSTERSt4,c3,c4,gfdl,es

### Jobs in the queue: 

squeue -a

### Completed Jobs: 

Slurm does not keep completed jobs in squeue.

sacct -S 2019-03-01 -E now -a

If you don’t specify -S and -E options sacct gives you data from today.

### Getting details about a job: 

Slurm only keeps information about completed jobs available via scontrol for 5 minutes after completion. After that time, sacct is the currently available way of getting information about completed jobs.

scontrol show job --clusterses 5978

 Fair Share Reporting: 

### Summary of all accounts 

sshare

### Summary of one account 

sshare -A aoml

### Details by user of one account 

sshare -a -A gefs

### Details by user of all accounts 

sshare -a

 Priority Analysis of Your Job: 

### sprio 

sprio -j 12345
