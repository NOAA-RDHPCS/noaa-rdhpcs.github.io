Using GCP
=========

GCP (general copy) is a convenient tool for copying data between NOAA RDHPCS
sites. It simplifies efficient data transfer between the various NOAA sites and
their filesystems with a syntax similar to the standard unix copy tool, cp or
scp.

Using GCP is simple -- just use a variant of the commands below to perform a
transfer:

.. code-block:: bash

   module load gcp
   gcp -v /path/to/some/source/file /path/to/some/destination/file

.. note::

   The ``-v`` option enables verbose output, including useful information
   for debugging. You can obtain a full list of available options with
   ``gcp --help``.

Smartsites
----------

GCP introduces the *smartsites*, similar to the scp use of hostname, to
indicate the remote site to transfer to or from. This concept enables the
transfer of files from one NOAA system to another. Each NOAA site has its own
smartsite. The currently supported smartsites in GCP are:


+---------+----------------------------------------------------------------+
| GFDL    | Pan and GFDL workstations in Princeton, NJ                     |
+---------+----------------------------------------------------------------+
| Gaea    | ORNL hosted NCRC/CMRS system in Oak Ridge, TN                  |
+---------+----------------------------------------------------------------+


To transfer data from one site to another, simply prepend the smartsite and a
colon to your file location (for example, ``gaea:/path/to/file``).

This smartsite example pushes data from a source site (GFDL) to a remote site
(Gaea).

.. note::

   We are not required to use a smartsite for the local site where
   we currently operate (but it is not an error to include it).

The following commands are equivalent:

.. code-block:: bash

   gcp -v /path/to/some/file gaea:/path/to/remote/destination
   gcp -v gfdl:/path/to/some/file gaea:/path/to/remote/destination

.. note::

   It can be very inefficient to move a file from /archive. It's better to
   transfer to /ptmp first. You don't have to specify the smartsite in the
   destination file path, as gcp can pull data from a remote site as well as
   pushing it:

   ``gcp -v gaea:/path/to/a/file /path/to/a/local/destination``

Log Session ID
--------------

GCP includes a comprehensive logging system. Each transfer is recorded and is
easily searchable if debugging is needed. Each transfer has a
unique log session id, visible if the -v option is used. It is highly
recommended that this option always be enabled in your transfers. A sample of
the expected output is below:

.. code-block:: console

     gcp -v /path/to/source/file /path/to/destination
     gcp 2.0.246 on keo.gfdl.noaa.gov by First.Last at Mon May 13 12:24:07 2023
     Unique log session id is 2c2607db-608f-46a7-a06a-ac576b9494be at 2023-04-13Z16:24


If you experience any problems while using GCP, please re-run your
transfer using the -v option, and provide the session id with your
help desk ticket.

Supported Filesystems
---------------------

GCP can copy data from many filesystems at the HPCS sites, but not all. Below
is a list of supported filesystems for each site. Note that sometimes GCP is
able to support a filesystem from within the local site, but not from external
sites.

GFDL Workstations
^^^^^^^^^^^^^^^^^

.. note::

   You cannot transfer files from a GFDL
   workstation to any remote site. You must use GFDL's PAN cluster to push or pull
   files to a remote site.

.. note::

   You will need a valid Globus proxy certificate
   from PAN (analysis) in your home directory. This is created and/or updated
   for you when you log into PAN. Proxy certificates are valid for 30 days.


Filesystems that GCP supports locally from GFDL workstations:

   ``/net, /net2, /home, /nbhome, /work, /archive``

Filesystems that GCP supports remotely from GFDL workstations, only to data1:

   ``/net, /net2, /home, /nbhome, /work, /archive``

GFDL PAN
^^^^^^^^

Filesystems that GCP supports locally from GFDL's PAN cluster:

   ``/net, /net2, /home, /nbhome, /ptmp, /work, /archive``

Filesystems that GCP supports remotely from other sites:

   ``/home, /ptmp, /work, /archive``



Gaea
^^^^

The Gaea site contains multiple node types (eslogin, rdtn,
batch).

Filesystems that GCP supports locally from within Gaea:

   ``/gpfs/f5, gpfs/f6, /ncrc/home``

Filesystems that GCP supports remotely from other sites:

   ``/gpfs/f5, gpfs/f6, /ncrc/home``

Helpful Hints
-------------

Creating directories
^^^^^^^^^^^^^^^^^^^^

GCP provides an option for automatically creating new directories:

   ``-cd``

The final segment of the path is interpreted as a directory if a trailing slash
is included. Otherwise, it will be interpreted as a file. A few examples are
below.

Transferring into new directories:

   ``gcp -cd /path/to/a/file /path/to/a/nonexistent/directory/``

The above creates a file called 'file' in a directory called 'directory':

   ``/path/to/a/nonexistent/directory/file``

Transferring into a file:

   ``gcp -cd /path/to/a/file /path/to/a/nonexistent/directory``

The above creates a file called 'directory' in a directory called
'nonexistent':

   ``/path/to/a/nonexistent/directory``

Recursive transfers
^^^^^^^^^^^^^^^^^^^

GCP provides the ``-r`` option to recursively transfer the contents of
directories.

Synchronize
^^^^^^^^^^^

GCP provides the ``--sync`` option to transfer files to the destination only if
the source is newer. This works for both recursive and non recursive transfers.

Caveats
-------

   * Sources from remote sites cannot include wildcards.
   * GCP does not preserve timestamps or file permissions.

Using the --batch option on Gaea
--------------------------------

Use ``gcp --batch`` for non-blocking transfers.

   * Only available where dtn queues are configured.
   * This is a non-blocking transfer and so is only appropriate when you or the
     script does not need to know explicitly when the transfer started or
     completed.
   * The batch log file is stored in ``$HOME/.gcp_gaea``
   * Needed for transfers initiated on Gaea batch nodes.


.. note::

   Use of ``gcp -d/--debug`` is not recommended. The function of the
   debug option has been superseded by logging that is done for all
   transfers automatically. You can obtain the log session id by using
   the ``-v``/``--verbose`` option. The ``-d`` option produces voluminous
   output and is not recommended.


If you encounter any bugs, confusing documentation, or other issues with GCP,
please open a :ref:`Help ticket. <getting_help>`
