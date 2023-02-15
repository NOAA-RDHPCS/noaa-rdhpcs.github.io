.. _data-and-transfers:

##################
Data and Transfers
##################

.. toctree::
   :maxdepth: 2



 #  Data Transfers
 ## Introduction
Available on Gaea is a tool called GCP, which allows for internal transfers on Gaea and to/from other NOAA RDHPCS resources (ZEUS and GFDL PPAN). Please reference System Details if you are unfamiliar with the filesystems or expected use of each variety of node on Gaea.

Available Tools
- GCP
- spdcp - lustre to lustre specific
- globus-url-copy (GridFTP)
- scp
- rsync
- cp
- hsi and htar (for Zeus' HPSS)
We suggest all users use GCP as the primary data transfer tool.

Examples
**f2 <-> f2** 

Users can transfer data between the lustre f2 filesystem using GCP. This can be done on the login nodes, and ldtns Gco commands issued on the compute nodes will result in a [L|R]DTN job being created and gcp will block until that job is completed by defaut.

**module load gcp**

`gcp /lustre/f2/dev/$USER/file /lustre/f2/scratch/$USER/path/file

**Gaea <-> GFDL**

Users can transfer data between GFDL and Gaea filesystems with GCP. This can be done on the login nodes and rdtn's only. Users can interactively run gcp commands from a login node or submit gcp calls in scripts to run in the rdtn queue.

`module load gcp
gcp gaea:/lustre/f2/scratch/$USER/file gfdl:/gfdl/specific/path/file
gcp gfdl:/gfdl/specific/path/file gaea:/lustre/f2/dev/$USER/path/file

**Gaea <-> Remote NOAA Site**

Users can transfer data between GFDL and Gaea filesystems with GridFTP, rsync or scp. This can be done on the login nodes and RDTNs only. Please place large transfers (>1GB) in batch jobs on the RDTN queue. This will respect other users on the login nodes by reducing interactive impact.

`scp /lustre/f2/scratch/$USER/path/name/here some.remote.site:/a/path/over/there
globus-url-copy file:/path/on/Gaea/file gsiftp://some.remote.site/path/to/destination/file
globus-url-copy gsiftp://some.remote.site/path/to/remote/file file:/destination/path/on/Gaea/file

**Gaea <-> External**

Users can use port tunnels associated with their login sessions to move files between Gaea and their workstations. NOAA users will find this to be far slower than GCP.

- Get your uid from the 'id' command on Gaea. Substitute your Gaea user name for First.Last
- Log out of Gaea entirely.
- Edit your workstation's ~/.ssh/config file to contain the following (you can also put this on your desktop/laptop workstation):

> Host gaea
  HostName                gaea.rdhpcs.noaa.gov
  User                    First.Last
  ControlMaster           auto
  LocalForward            uid+30000 localhost:uid+30000
  RemoteForward           uid+20000 localhost:22
  NoHostAuthenticationForLocalhost yes

Host gaea1 gaea2 gaea3 gaea4 gaea5 gaea6 gaea7 gaea8 gaea?.ncrc.gov
  HostName                localhost
  Port                    uid+30000
  User                    First.Last
  LogLevel                Quiet

Host *
  CheckHostIP yes
  ForwardAgent            yes
  ForwardX11Trusted       yes
  ControlPath ~/.ssh/%r@%h:%p
  ControlMaster           no
  AddressFamily       inet
  IdentityFile ~/.ssh/ntt_id_rsa
  ServerAliveInterval     60

- Run: ssh gaea
- Check that your tunnels get created (there will be a bit of output near the banner about this.)
- In your Gaea session, cd to the location you want your file to be transferred to.
- In your Gaea session, run scp -P 50017 your_workstation_username@localhost:/path/to/file .

**Gaea <-> Fairmont HPSS**
Users can transfer data between Gaea and Zeus' High Performance Storage System (HPSS) through the use of the HSI and HTAR commands. These commands are only available on Gaea's Remote Data Transfer Nodes (RDTNs). A user can submit a script to run on the RDTNs.

- Minimum Headers for a submitted RDTN job.
`#SBATCH --clusters=es
#SBATCH --partition=rdtn

- Load the HSI module and list the contents of your directory
`module load hsi

- Check connectivity to the hsi, replacing the below file path with yours on HPSS
`hsi "ls -P /BMC/nesccmgmt/$USER/"

- Retrieve Files using HSI into the current directory on the RDTN. The -q option limits output spam.
`hsi -q "get /BMC/nesccmgmt/Karol.Zieba/sample_file"

- Upload Files using HSI
`hsi -q "put /lustre/f2/scratch/$USER/file_to_upload : /BMC/nesccmgmt/$USER/file_to_upload"

- Tar many small files from the RDTN using HTAR. Note that using asterisk will not work.

`htar cf /BMC/nesccmgmt/$USER/tarred_file.tar file1 file2 path/file3

- Untar many small files into your current directory on the RDTN using HTAR

`htar xf /BMC/nesccmgmt/$USER/tarred_file.tar

Further information on interfacing with HPSS and the HSI/HTAR commands can be found below.

http://www.mgleicher.us/GEL/htar/htar_user_guide.html
https://nesccdocs.rdhpcs.noaa.gov/wiki/index.php/Using_The_HSMS_%28HPSS%29

## External (Untrusted) Data Transfers
To support external data transfers with methods that are faster and simpler than the port tunnel method, NOAA RDHPCS has a data transfer node. This means data can be transferred to Gaea without the use of the port tunnel or existing ssh connection. Not only is this simpler, but provides for much faster transfers. The difference between the eDTN and the DTN as described above is that the eDTN does not mount the Gaea filesystems. Transferring through the eDTN to Gaea requires a two step process. First, files are transferred from external hosts to the eDTN. Second, from Gaea, the files are pulled back from the eDTN.

For authentication, use of your token is required from external transfers to the eDTN. From within Gaea, use of your token is not required.

The eDTN supports the use of scp, sftp, bbcp, and ssh based globus-url-copy.

### Copying files from external systems to the eDTN

`jsmith# scp WRF.tar.gz John.Smith@edtn.fairmont.rdhpcs.noaa.gov:
 
 Access is via First.Last username only.  Enter RSA PASSCODE:
The trailing colon (':') is critical. You can also specify ":/home/John.Smith/"

Your response should be your pin+PASSCODE.

### Retrieving files on Gaea from the eDTN
To transfer files from the eDTN server to Gaea without requiring your token, you must use GSI enabled transfer methods. For scp, sftp, and bbcp, this mean appending "gsi" to the front of the command. So the commands that are best to use are gsiscp, gsisftp, and gsibbcp.

To pull the files back from the eDTN, initiate on of these commands:

`John.Smith# gsiscp -S `which gsissh` edtn.fairmont.rdhpcs.noaa.gov:WRF.tar.gz .

### eDTN Purge Policy
Files older than 7 days will be automatically removed. This policy may change based on disk space and management needs.

### Managing files on the eDTN
If you need to login and manage any files, create or remove directories, or any other tasks on the eDTN, use gsisftp from Gaea. This provides and FTP like interface through ssh.

`# sftp -S `which gsissh` John.Smith@edtn.fairmont.rdhpcs.noaa.gov
`Access is via First.Last username only. Enter RSA PASSCODE:
Connected to edtn.fairmont.rdhpcs.noaa.gov.
sftp> ls
bigfile    bigfile1   bigfileA
sftp> rm bigfile
Removing /home/Craig.Tierney/bigfile
sftp> rm bigfile*
Removing /home/Craig.Tierney/bigfile1
Removing /home/Craig.Tierney/bigfileA
sftp> ls
sftp> mkdir newdir1
sftp> ls
newdir1
sftp> cd newdir1
sftp> pwd
Remote working directory: /home/Craig.Tierney/newdir1
sftp> cd ..
sftp> rmdir newdir1
sftp> ls

`sftp> help
Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
                                   filesystem containing 'path'
exit                               Quit sftp
get [-Ppr] remote [local]          Download file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln oldpath newpath                 Symlink remote file
lpwd                               Print local working directory
ls [-1afhlnrSt] [path]             Display remote directory listing
lumask umask                       Set local umask to 'umask'
mkdir path                         Create remote directory
progress                           Toggle display of progress meter
put [-Ppr] local [remote]          Upload file
pwd                                Display remote working directory
quit                               Quit sftp
rename oldpath newpath             Rename remote file
rm path                            Delete remote file
rmdir path                         Remove remote directory
symlink oldpath newpath            Symlink remote file
version                            Show SFTP version
!command                           Execute 'command' in local shell
!                                  Escape to local shell
?                                  Synonym for help


