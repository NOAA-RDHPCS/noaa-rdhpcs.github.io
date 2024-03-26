
**************************
Installing mpi4py and h5py
**************************

.. note::

   The guide is designed to be followed from start to finish, as certain steps
   must be completed in the correct order before some commands work properly.

Overview
========

This guide teaches you how to build a personal, parallel-enabled version of
h5py and how to write an HDF5 file in parallel using mpi4py and h5py.

In this guide, you will:

* Learn how to install mpi4py
* Learn how to install parallel h5py
* Test your build with Python scripts

Parallel HDF5
=============

Scientific simulations generate large amounts of data on Summit (about 100
Terabytes per day for some applications). Because of how large some data files
may be, it is important that writing and reading these files is done as fast as
possible. Less time spent doing input/output (I/O) leaves more time for
advancing a simulation or analyzing data.

One of the most utilized file types is the Hierarchical Data Format (HDF),
specifically the HDF5 format. `HDF5
<https://www.hdfgroup.org/solutions/hdf5/>`__ is designed to manage large
amounts of data and is built for fast I/O processing and storage. An HDF5 file
is a container for two kinds of objects: "datasets", which are array-like
collections of data, and "groups", which are folder-like containers that hold
datasets and other groups.

There are various tools that allow users to interact with HDF5 data, but we
will be focusing on `h5py <https://docs.h5py.org/en/stable/>`__ -- a Python
interface to the HDF5 library. h5py provides a simple interface to exploring
and manipulating HDF5 data as if they were Python dictionaries or NumPy arrays.
For example, you can extract specific variables through slicing, manipulate the
shapes of datasets, and even write completely new datasets from external NumPy
arrays.

Both HDF5 and h5py can be compiled with MPI support, which allows you to
optimize your HDF5 I/O in parallel. MPI support in Python is accomplished
through the `mpi4py <https://mpi4py.readthedocs.io/en/stable/>`__ package,
which provides complete Python bindings for MPI. Building h5py against mpi4py
allows you to write to an HDF5 file using multiple parallel processes, which
can be helpful for users handling large datasets in Python. h5Py is available
after loading the default Python module on either Summit or Andes, but it has
not been built with parallel support.

Setting up the environment
==========================

.. warning::

   Before setting up your environment, you must exit and log back in so that
   you have a fresh login shell. This is to ensure that no previously activated
   environments exist in your ``$PATH`` environment variable. Additionally, you
   should execute ``module reset``.

Building h5py from source is highly sensitive to the current environment
variables set in your profile. Because of this, it is extremely important that
all the modules and environments you plan to load are done in the correct
order, so that all the environment variables are set correctly.

First, load the gnu compiler module (most Python packages assume GCC), hdf5
module (necessary for h5py), and the python module (allows you to create a new
environment):

.. tab-set::

   .. tab-item:: Gaea
      :sync: gaea

      .. code-block:: bash

         $ module swap PrgEnv-intel PrgEnv-gnu
         $ module load cray-hdf5
         $ module load python

   .. tab-item:: Hera
      :sync: hera

      .. code-block:: bash

         $ module load gnu
         $ module load hdf5
         $ module use /contrib/miniconda/modulefiles
         $ module load miniconda3/4.12.0

   .. tab-item:: Jet
      :sync: jet

      .. code-block:: bash

         $ module load gcc
         $ module load hdf5
         $ module load python

   .. tab-item:: Niagara
      :sync: niagara

      .. code-block:: bash

         $ module load gcc
         $ module load hdf5
         $ module load python

Loading a python module puts you in a "base" environment, but you need to
create a new environment using the ``conda create`` command:


.. code-block:: bash

   $ conda create -p /<project_home>/<PROJECT_ID>/<USER_ID>/envs/h5pympi python=3.10.13

.. note::

   As noted in the :doc:`/software/python/index` page, it is highly recommended
   to create new environments in the "Project Home" directory.

After following the prompts for creating your new environment, you can now
activate it:

.. code-block:: bash

   $ conda activate /<project_home>/<PROJECT_ID>/<USER_ID>/envs/h5pympi

Installing mpi4py
=================

Now that you have a fresh environment, you will next install mpi4py from source
into your new environment. To make sure that you are building from source, and
not a pre-compiled binary, use ``pip``:

.. tab-set::

   .. tab-item:: Gaea
      :sync: gaea

      .. code-block:: bash

         $ MPICC="cc -shared" pip install --no-cache-dir --no-binary=mpi4py mpi4py

   .. tab-item:: Hera
      :sync: hera

      .. code-block:: bash

         $ MPICC="mpicc -shared" pip install --no-cache-dir --no-binary=mpi4py mpi4py

   .. tab-item:: Jet
      :sync: jet

      .. code-block:: bash

         $ MPICC="cc -shared" pip install --no-cache-dir --no-binary=mpi4py mpi4py

   .. tab-item:: Niagara
      :sync: niagara

      .. code-block:: bash

         $ MPICC="cc -shared" pip install --no-cache-dir --no-binary=mpi4py mpi4py

The ``MPICC`` flag ensures that you are using the correct C wrapper for MPI on
the system. Building from source typically takes longer than a simple ``conda
install``, so the download and installation may take a couple minutes. If
everything goes well, you should see a "Successfully installed mpi4py" message.

Installing h5py
===============

Next, install h5py from source. Because h5py depends on NumPy, install an
optimized version of the NumPy package:

.. code-block:: bash

   $ conda install -c defaults --override-channels numpy

The ``-c defaults --override-channels`` flags ensure that conda will search for
NumPy only on the "defaults" channel. Installing NumPy in this manner results
in an optimized NumPy that is built against linear algebra libraries, which
performs operations much faster.

Next, you are finally ready to install h5py from source:

.. tab-set::

   .. tab-item:: Gaea
      :sync: gaea

      .. code-block:: bash

         $ HDF5_MPI="ON" CC=cc pip install --no-cache-dir --no-binary=h5py h5py

   .. tab-item:: Hera
      :sync: hera

      .. code-block:: bash

         $ HDF5_MPI="ON" CC=mpicc pip install --no-cache-dir --no-binary=h5py h5py

   .. tab-item:: Jet
      :sync: jet

      .. code-block:: bash

         $ HDF5_MPI="ON" CC=mpicc pip install --no-cache-dir --no-binary=h5py h5py

   .. tab-item:: Niagara
      :sync: niagara

      .. code-block:: bash

         $ HDF5_MPI="ON" CC=mpicc pip install --no-cache-dir --no-binary=h5py h5py

The ``HDF5_MPI`` flag is the key to telling pip to build h5py with parallel
support, while the ``CC`` flag makes sure that you are using the correct C
wrapper for MPI. This installation will take much longer than both the mpi4py
and NumPy installations (5+ minutes if the system is slow). When the
installation finishes, you will see a "Successfully installed h5py" message.

Testing parallel h5py
=====================

Test your build by trying to write an HDF5 file in parallel using 42 MPI tasks.

First, change directories to your scratch area:

.. code-block:: bash

   $ cd /<project_home>/<PROJECT_ID>/<USER_ID>
   $ mkdir h5py_test
   $ cd h5py_test

Let's test that mpi4py is working properly first by executing the example
Python script ``hello_mpi.py``:

.. code-block:: python

   # hello_mpi.py
   from mpi4py import MPI

   comm = MPI.COMM_WORLD      # Use the world communicator
   mpi_rank = comm.Get_rank() # The process ID (integer 0-41 for a 42-process job)

   print('Hello from MPI rank %s !' %(mpi_rank))

To do so, submit a job to the batch queue:

.. code-block:: bash

   $ sbatch --export=NONE submit_hello.sl

Example "submit_hello" batch script:

.. code-block:: bash

   #!/bin/bash
   #SBATCH -A <PROJECT_ID>
   #SBATCH -J mpi4py
   #SBATCH -N 1
   #SBATCH -p batch
   #SBATCH -t 0:05:00

   cd $SLURM_SUBMIT_DIR
   date

   module load PrgEnv-gnu
   module load hdf5

   conda activate /project_home>/<PROJECT_ID>/<USER_ID>/envs/h5pympi

   srun -n42 python3 hello_mpi.py

If mpi4py is working properly, in ``mpi4py.<JOB_ID>.out`` you should see output
similar to:

.. code-block::

   Hello from MPI rank 21 !
   Hello from MPI rank 23 !
   Hello from MPI rank 28 !
   Hello from MPI rank 40 !
   Hello from MPI rank 0 !
   Hello from MPI rank 1 !
   Hello from MPI rank 32 !
   .
   .
   .

If you see this, great, it means that mpi4py was built successfully in your
environment.

Finally, let's see if you can get these tasks to write to an HDF5 file in
parallel using the "hdf5_parallel.py" script:

.. code-block:: python

   # hdf5_parallel.py
   from mpi4py import MPI
   import h5py

   comm = MPI.COMM_WORLD      # Use the world communicator
   mpi_rank = comm.Get_rank() # The process ID (integer 0-41 for a 42-process job)
   mpi_size = comm.Get_size() # Total amount of ranks

   with h5py.File('output.h5', 'w', driver='mpio', comm=MPI.COMM_WORLD) as f:
       dset = f.create_dataset('test', (42,), dtype='i')
       dset[mpi_rank] = mpi_rank

   comm.Barrier()

   if (mpi_rank == 0):
       print('42 MPI ranks have finished writing!')

The MPI tasks are going to write to a file named ``output.h5``, which contains
a dataset called "test" that is of size 42 (assigned to the ``dset`` variable
in Python). Each MPI task is going to assign their rank value to the ``dset``
array in Python, so you should end up with a dataset that contains 0-41 in
ascending order.

Time to execute ``hdf5_parallel.py`` by submitting ``submit_h5py`` to the batch
queue:

.. code-block:: bash

   $ sbatch --export=NONE submit_h5py.sl


Example "submit_h5py" batch script:

.. code-block:: bash

   #!/bin/bash
   #SBATCH -A <PROJECT_ID>
   #SBATCH -J h5py
   #SBATCH -N 1
   #SBATCH -p gpu
   #SBATCH -t 0:05:00

   cd $SLURM_SUBMIT_DIR
   date

   module load gnu
   module load hdf5
   module load python

   conda activate /<project_home>/<PROJECT_ID>/<USER_ID>/envs/h5pympi

   srun -n42 python3 hdf5_parallel.py


Provided there are no errors, you should see "42 MPI ranks have finished
writing!" in your output file, and there should be a new file called
``output.h5`` in your directory. To see explicitly that the MPI tasks did their
job, you can use the ``h5dump`` command to view the dataset named "test" in
output.h5:

.. code-block:: bash

   $ h5dump output.h5

   HDF5 "output.h5" {
   GROUP "/" {
      DATASET "test" {
         DATATYPE  H5T_STD_I32LE
         DATASPACE  SIMPLE { ( 42 ) / ( 42 ) }
         DATA {
         (0): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
         (19): 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
         (35): 35, 36, 37, 38, 39, 40, 41
         }
      }
   }
   }

If you see the above output, then the build was a success!

Additional Resources
====================

* `h5py Documentation <https://docs.h5py.org/en/stable/>`__
* `mpi4py Documentation <https://mpi4py.readthedocs.io/en/stable/>`__
* `HDF5 Support Page <https://portal.hdfgroup.org/display/HDF5/HDF5>`__
