Overview
========

GCP (general copy) is a convenience wrapper for copying data between the
Gaea and PPAN Analysis NOAA RDHPCS sites, as well as the NOAA GFDL site.
GCP abstracts away the complexities of transferring data efficiently
between the various NOAA sites and their filesystems. Its syntax is
similar to the standard UNIX copy tool, cp.

GCP 2.3.26 is available on Gaea, PPAN, and GFDL Linux Workstations. It
is obtainable via "module load gcp" or "module load gcp/2.3". This
version is the latest as of 2022-08-01; all other versions are
considered obsolete and will not function properly due to system
updates.

.. _user_guide:

User Guide
==========

.. _getting_started:

Getting Started
---------------

Using GCP is simple – just use a variant of the commands below to
perform a transfer:

::

   module load gcp
   gcp -v /path/to/some/source/file /path/to/some/destination/file

The -v option enables verbose output, including some very useful
information for debugging.

You can obtain a detailed list of all of the available options with:

::

   gcp --help

Smartsites
----------

GCP introduces a concept known as smartsites. This concept enables the
transfer of files from one NOAA system to another. Each NOAA site has
its own smartsite. The currently supported smartsites in GCP are:

- gfdl - gaea

To transfer data from one site to another, simple prepend the smartsite
and a colon to your file location (example: gaea:/path/to/file).

This smartsite example pushes data from a source site (GFDL) to a remote
site (Gaea). Note that we are not required to use a smartsite for the
local site we are currently operating from (but it is not an error to
include it). The following commands are equivalent:

::

   gcp -v /path/to/some/file gaea:/path/to/remote/destination
   gcp -v gfdl:/path/to/some/file gaea:/path/to/remote/destination

The smartsite needn't always be part of the destination file path, as
gcp is capable of pulling data from a remote site as well as pushing it:

::

   gcp -v gaea:/path/to/a/file /path/to/a/local/destination

.. _log_session_id:

Log Session ID
--------------

GCP includes a comprehensive logging system. Each transfer is recorded
and is easily searchable by the GCP development team in the event that
debugging is needed.

Each transfer is given a unique log session id, but this session id is
only visible if the -v option is used. It is highly recommended that
this option always be enabled in your transfers. A sample of the
expected output is below:

::

   gcp -v /path/to/source/file /path/to/destination
   gcp 2.3.26 on an204.princeton.rdhpcs.noaa.gov by Chandin.Wilson at Mon Aug 8 16:39:28 2022
   Unique log session id is 07f6dd51-6c4d-4e51-86b4-e3344c01c3ae at 2022-08-08Z20:39

If you experience any problems while using GCP, please re-run your
transfer using the -v option and provide the session id with your help
desk ticket.

.. _supported_filesystems:

Supported Filesystems
---------------------

GCP can copy data from many filesystems, but not all. Below is a list of
supported filesystems for each site. Note that sometimes GCP is able to
support a filesystem from within the local site, but not from external
sites.

.. _gfdl_workstations:

GFDL Workstations
~~~~~~~~~~~~~~~~~

**Note:** You cannot transfer files from a GFDL workstation to any
remote site. You must use GFDL's PAN cluster to push or pull files to a
remote site.

Filesystems that GCP supports locally from GFDL workstations:

- /net - /net2 - /home - /work - /archive

Filesystems that GCP supports remotely from other sites:

- /home - /ptmp - /work - /archive

Gaea
~~~~

The Gaea site contains multiple node types. The nodes that are used for
interactive work are called the eslogin nodes. Different filesystems are
supported on each node type, so please refer to the list below.

Filesystems that GCP supports locally from Gaea:

- eslogin

| ``- /lustre/f2``
| ``- /ncrc/home``

- ldtn

| `` - /lustre/f2``
| `` - /ncrc/home``

- rdtn

| `` - /ncrc/home``
| `` - /lustre/f2``

- compute (c3/c4)

| `` - /ncrc/home``
| `` - /lustre/f2``

Filesystems that GCP supports remotely from other sites:

- /ncrc/home - /lustre/f2

.. _helpful_hints:

Helpful Hints
-------------

.. _creating_directories:

Creating Directories
~~~~~~~~~~~~~~~~~~~~

GCP provides an option for automatically creating new directories (-cd).

The final segment of the path is interpreted as a directory if a
trailing slash is included. Otherwise, it will be interpreted as a file.
A few examples are below.

Transferring into new directories:

::

   gcp -cd /path/to/a/file /path/to/a/nonexistent/directory/

The above results in a file called 'file' being created in a directory
called 'directory':

::

   /path/to/a/nonexistent/directory/file

Transferring into a file:

::

   gcp -cd /path/to/a/file /path/to/a/nonexistent/directory

The above results in a file called 'directory' being created in a
directory called 'nonexistent':

::

   /path/to/a/nonexistent/directory

Changes
=======

GCP development and releases are tracked in the GFDL Gitlab project. See
https://gitlab.gfdl.noaa.gov/gcp/gcp for further detail.
