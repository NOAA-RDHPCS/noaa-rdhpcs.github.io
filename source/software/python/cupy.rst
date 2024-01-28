
***************
Installing CuPy
***************

.. note::

   The guide is designed to be followed from start to finish, as certain steps
   must be completed in the correct order before some commands work properly.

Overview
========

This guide teaches you how to build CuPy from source into a custom virtual
environment. This is done using ``conda``.

In this guide, you will:

* Learn how to install CuPy
* Learn the basics of CuPy
* Compare speeds to NumPy

CuPy
====

GPU computing has become a big part of the data science landscape, as array
operations with NVIDIA GPUs can provide considerable speedups over CPU
computing. Although GPU computing is often utilized in codes that are written in
Fortran and C, GPU-related Python packages are quickly becoming popular in the
data science community. One of these packages is `CuPy <https://cupy.dev/>`__, a
NumPy/SciPy-compatible array library accelerated with NVIDIA CUDA.

CuPy is a library that implements NumPy arrays on NVIDIA GPUs by utilizing CUDA
Toolkit libraries like cuBLAS, cuRAND, cuSOLVER, cuSPARSE, cuFFT, cuDNN and
NCCL. Although optimized NumPy is a significant step up from Python in terms of
speed, performance is still limited by the CPU (especially at larger data sizes)
-- this is where CuPy comes in. Because CuPy's interface is nearly a mirror of
NumPy, it acts as a replacement to run existing NumPy/SciPy code on NVIDIA CUDA
platforms, which helps speed up calculations further. CuPy supports most of the
array operations that NumPy provides, including array indexing, math, and
transformations. Most operations provide an immediate speed-up out of the box,
and some operations are sped up by over a factor of 100 (see CuPy benchmark
timings below, from the `Single-GPU CuPy Speedups
<https://medium.com/rapids-ai/single-gpu-cupy-speedups-ea99cbbb0cbb>`__
article).

.. image:: /images/python_cupy_1.png
   :align: center
   :width: 50%

Compute nodes equipped with NVIDIA GPUs will be able to take full advantage of
CuPy's capabilities on the system, providing significant speedups over
NumPy-written code. **CuPy with AMD GPUs is still being explored, and the same
performance is not guaranteed (especially with larger data sizes).**
**Instructions for Hera's fge partition are available in this guide, but users
must note that the CuPy developers have labeled this method as** `experimental
<https://docs.cupy.dev/en/stable/install.html#using-cupy-on-amd-gpu-experimental>`__
**and has** `limitations
<https://docs.cupy.dev/en/stable/install.html#limitations>`__.

.. _cupy-envs:

Installing CuPy
===============

.. warning::

   Before setting up your environment, you must exit and log back in so that you
   have a fresh login shell. This is to ensure that no previously activated
   environments exist in your ``$PATH`` environment variable. Additionally, you
   should execute ``module reset``.

Building CuPy from source is highly sensitive to the current environment
variables set in your profile. Because of this, it is extremely important that
all the modules and environments you plan to load are done in the correct order,
so that all the environment variables are set correctly.

First, load the gnu compiler module (most Python packages assume GCC), relevant
GPU module (necessary for CuPy), and the python module (allows you to create a
new environment):

.. code-block:: bash

   $ module load gnu/9.2.0 # might work with other GCC versions
   $ module load cuda/12.1.0
   $ module use /contrib/miniconda/modulefiles
   $ module load miniconda3/4.12.0

Loading a python module puts you in a "base" environment, but you need to create
a new environment using the ``conda create`` command or the ``venv``
command:

.. tab-set::

   .. tab-item:: Conda
      :sync: conda

      .. code-block:: bash

         $ conda create -p /scratch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/cupy python=3.10.13

   .. tab-item:: Venv
      :sync: venv

      .. code-block:: bash

         $ python3 -m venv /scrtch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/cupy


.. note::

   As noted in the :doc:`/software/python/index` page, it is highly recommended
   to create new environments in the "Project Home" directory.

After following the prompts for creating your new environment, you can now activate it:

.. tab-set::

   .. tab-item:: Conda
      :sync: conda

      .. code-block:: bash

         $ source activate /scrtch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/cupy

   .. tab-item:: Venv
      :sync: venv

      .. code-block:: bash

         $ source /scrtch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/cupy/bin/activate

CuPy depends on NumPy, so let's install an optimized version of NumPy into your
fresh environment:

.. tab-set::

   .. tab-item:: Conda
      :sync: conda

      .. code-block:: bash

         $ conda install -c defaults --override-channels numpy scipy

   .. tab-item:: Venv
      :sync: venv

      .. code-block:: bash

         $ pip install --no-cache-dir --upgrade pip
         $ pip install numpy scipy --no-cache-dir

After following the prompts, NumPy and its linear algebra dependencies should
successfully install. SciPy is an optional dependency, but it would allow you to
use the additional SciPy-based routines in CuPy:

Finally, install CuPy from source into your environment. To make sure that you
are building from source, and not a pre-compiled binary, use ``pip``:

.. code-block:: bash

   $ CC=gcc NVCC=nvcc pip install --no-cache-dir --no-binary=cupy cupy

The ``CC`` and ``NVCC`` flags ensure that you are passing the correct wrappers.
This installation takes, on average, 10-20 minutes to complete (due to building
everything from scratch), so don't panic if it looks like the install timed-out.
Eventually you should see output similar to this (versions will vary):

.. code-block::

   Successfully installed cupy-9.5.0 fastrlock-0.6

Getting Started With CuPy
=========================

.. note::

   Assuming you are continuing from the previous sections, you do not need to
   load any modules. Otherwise, you need to load the modules associated with
   your system covered in the :ref:`Installing CuPy section <cupy-envs>`.

When a kernel call is required in CuPy, it compiles a kernel code optimized for
the shapes and data types of given arguments, sends it to the GPU device, and
executes the kernel. Due to this, CuPy runs slower on its initial execution.
This slowdown will be resolved at the second execution because CuPy caches the
kernel code sent to GPU device. By default, the compiled code is cached to the
``$HOME/.cupy/kernel_cache`` directory, which the compute nodes will not be able
to access. It is good practice to change it to your scratch directory:

.. code-block:: bash

   $ export CUPY_CACHE_DIR="/scratch[12]/<LAB>/<PROJECT_ID>/<YOUR_USER_ID>/.cupy/kernel_cache"

Before you start testing CuPy with Python scripts, let's go over some of the
basics. The developers provide a great introduction to using CuPy in their user
guide under the `CuPy Basics
<https://docs.cupy.dev/en/stable/user_guide/basic.html>`__ section. We will be
following this walkthrough. 

As is the standard with NumPy being imported as "np", CuPy is often imported in
a similar fashion:

.. code-block:: python

   >>> import numpy as np
   >>> import cupy as cp

Similar to NumPy arrays, CuPy arrays can be declared with the ``cupy.ndarray``
class. NumPy arrays will be created on the CPU (the "host"), while CuPy arrays
will be created on the GPU (the "device"):

.. code-block:: python

   >>> x_cpu = np.array([1,2,3])
   >>> x_gpu = cp.array([1,2,3])

Manipulating a CuPy array can also be done in the same way as manipulating NumPy
arrays:

.. code-block:: python

   >>> x_cpu*2.
   array([2., 4., 6.])
   >>> x_gpu*2.
   array([2., 4., 6.])
   >>> l2_cpu = np.linalg.norm(x_cpu)
   >>> l2_gpu = cp.linalg.norm(x_gpu)
   >>> print(l2_cpu,l2_gpu)
   3.7416573867739413 3.7416573867739413

Useful functions for initializing arrays like ``np.linspace``, ``np.arange``,
and ``np.zeros`` also have a CuPy equivalent:

.. code-block:: python

   >>> cp.zeros(3)
   array([0., 0., 0.])
   >>> cp.linspace(0,10,11)
   array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
   >>> cp.arange(0,11,1)
   array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

CuPy has a concept of a "current device", which is the current activated GPU
device that will operate on an array or where future arrays will be allocated.
Most of the time, if not explicitly declared or switched, the initial default
device will be GPU 0. To find out what device a CuPy array is allocated on, you
can call the ``cupy.ndarray.device`` attribute:

.. code-block:: python

   >>> x_gpu.device
   <CUDA Device 0>

To get a total number of devices that you can access, use the ``getDeviceCount``
function:

.. code-block:: python

   >>> cp.cuda.runtime.getDeviceCount()
   4

The current device can be switched using ``cupy.cuda.Device(<DEVICE_ID>).use()``:

.. code-block:: python

   >>> cp.cuda.Device(1).use()
   >>> x_gpu_1 = cp.array([1, 2, 3, 4, 5])
   >>> x_gpu_1.device
   <CUDA Device 1>

Similarly, you can temporarily switch to a device using the ``with`` context:

.. code-block:: python

   >>> cp.cuda.Device(0).use()
   >>> with cp.cuda.Device(3):
   ...    x_gpu_3 = cp.array([1, 2, 3, 4, 5])
   ...
   >>> x_gpu_0 = cp.array([1, 2, 3, 4, 5])
   >>> x_gpu_0.device
   <CUDA Device 0>
   >>> x_gpu_3.device
   <CUDA Device 3>

Trying to perform operations on an array stored on a different GPU will result
in an error:

.. code-block:: python

   >>> with cp.cuda.Device(0):
   ...    x_gpu_0 = cp.array([1, 2, 3, 4, 5]) # create an array in GPU 0
   ...
   >>> with cp.cuda.Device(1):
   ...    x_gpu_0 * 2  # ERROR: trying to use x_gpu_0 on GPU 1
   ...
   Traceback (most recent call last):
   ValueError: Array device must be same as the current device: array device = 0 while current = 1

To solve the above error, you must transfer ``x_gpu_0`` to "Device 1". A CuPy
array can be transferred to a specific GPU using the ``cupy.asarray()`` function
while on the specific device:

.. code-block:: python

   >>> with cp.cuda.Device(1):
   ...    cp.asarray(x_gpu_0) * 2  # fixes the error, moves x_gpu_0 to GPU 1
   ...
   array([ 2,  4,  6,  8, 10])

A NumPy array on the CPU can also be transferred to a GPU using the same
``cupy.asarray()`` function:

.. code-block:: python

   >>> x_cpu = np.array([1, 1, 1]) # create an array on the CPU
   >>> x_gpu = cp.asarray(x_cpu)  # move the CPU array to the current device
   >>> x_gpu
   array([1, 1, 1])

To transfer from a GPU back to the CPU, you use the ``cupy.asnumpy()`` function
instead:

.. code-block:: python

   >>> x_gpu = cp.zeros(3)  # create an array on the current device
   >>> x_cpu = cp.asnumpy(x_gpu)  # move the GPU array to the CPU
   >>> x_cpu
   array([ 0., 0., 0.])

Associated with the concept of current devices are current "streams". In CuPy,
all CUDA operations are enqueued onto the current stream, and the queued tasks
on the same stream will be executed in serial (but asynchronously with respect
to the CPU). This can result in some GPU operations finishing before some CPU
operations. As CuPy streams are out of the scope of this guide, you can find
additional information in the `CuPy User Guide
<https://docs.cupy.dev/en/stable/user_guide/index.html>`__.

NumPy Speed Comparison
======================

Now that you know how to use CuPy, time to see the actual benefits that CuPy
provides for large datasets. More specifically, let's see how much faster CuPy
can be than NumPy on Summit. You won't need to fix any errors; this is mainly a
demonstration on what CuPy is capable of.

There are a few things to consider when running on GPUs, which also apply to
using CuPy:

* Higher precision means higher cost (time and space)
* The structuring of your data is important
* The larger the data, the better for GPUs (but needs careful planning)

These points are explored in the example script ``timings.py``:

.. code-block:: python

   # timings.py
   import cupy as cp
   import numpy as np
   import time as tp

   A      = np.random.rand(3000,3000) # NumPy rand
   G      = cp.random.rand(3000,3000) # CuPy rand
   G32    = cp.random.rand(3000,3000,dtype=cp.float32) # Create float32 matrix instead of float64 (default)
   G32_9k = cp.random.rand(9000,1000,dtype=cp.float32) # Create float32 matrix of a different shape

   t1 = tp.time()
   np.linalg.svd(A) # NumPy Singular Value Decomposition
   t2 = tp.time()
   print("CPU time: ", t2-t1)

   t3 = tp.time()
   cp.linalg.svd(G) # CuPy Singular Value Decomposition
   cp.cuda.Stream.null.synchronize() # Waits for GPU to finish
   t4 = tp.time()
   print("GPU time: ", t4-t3)

   t5 = tp.time()
   cp.linalg.svd(G32)
   cp.cuda.Stream.null.synchronize()
   t6 = tp.time()
   print("GPU float32 time: ", t6-t5)

   t7 = tp.time()
   cp.linalg.svd(G32_9k)
   cp.cuda.Stream.null.synchronize()
   t8 = tp.time()
   print("GPU float32 restructured time: ", t8-t7)

This script times the decomposition of a matrix with 9 million elements across
four different methods. First, NumPy is timed for a 3000x3000 dimension matrix.
Then, a 3000x3000 matrix in CuPy is timed. As you will see shortly, the use of
CuPy will result in a major performance boost when compared to NumPy, even
though the matrices are structured the same way. This is improved upon further
by switching the data type to ``float32`` from ``float64`` (the default).
Lastly, a 9000x1000 matrix is timed, which contains the same number of elements
as the original matrix, just rearranged. Although you may not expect it, the
restructuring results in a big performance boost as well.

Before asking for a compute node, change into your scratch directory:

.. code-block:: bash

   $ cd /scratch[12]<LAB>/<PROJECT_ID>/<USER_ID>
   $ mkdir cupy_test
   $ cd cupy_test

Let's see the boosts explicitly by running the ``timings.py`` script. To do so,
you must submit ``submit_timings`` to the queue:

.. code-block:: bash

   $ sbatch submit_timings.sl

Example "submit_timings" batch script:

.. code-block:: bash

   #!/bin/bash
   #SBATCH -A <PROJECT_ID>
   #SBATCH -t 00:05
   #SBATCH -p fge
   #SBATCH -N 1
   #SBATCH -J cupy_timings
   #SBATCH -o cupy_timings.%J.out
   #SBATCH -e cupy_timings.%J.err

   cd $SLURM_SUBMIT_DIR
   date

   module load gnu/9.2.0
   module load cuda/12.1.0
   module use /contrib/miniconda/modulefiles
   module load miniconda3/4.12.0

   conda activate /scratch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/envs/cupy
   export CUPY_CACHE_DIR="/scratch[12]/<LAB>/<PROJECT_ID>/<USER_ID>/.cupy/kernel_cache"

   srun -n 1 -G 1 python3 timings.py


After the job completes, in ``cupy_timings.<JOB_ID>.out`` you will see something
similar to:

.. code-block::

   CPU time:  21.632022380828857
   GPU time:  11.382664203643799
   GPU float32 time:  4.066986799240112
   GPU float32 restructured time:  0.8666532039642334

The exact numbers may be slightly different, but you should see a speedup factor
of approximately 2 or better when comparing "GPU time" to "CPU time". Switching
to ``float32`` was easier on memory for the GPU, which improved the time
further. Things are even better when you look at "GPU float32 restructured
time", which represents an additional factor of 4 speedup when compared to "GPU
float32 time". Overall, using CuPy and restructuring the data led to a speedup
factor of >20 when compared to traditional NumPy! This factor would diminish
with smaller datasets, but represents what CuPy is capable of at this scale.

You have now discovered what CuPy can provide! Now you can try speeding up your
own codes by swapping CuPy and NumPy where you can.

Additional Resources
====================

* `CuPy User Guide <https://docs.cupy.dev/en/stable/user_guide/index.html>`__
* `CuPy Website <https://cupy.dev/>`__
* `CuPy API Reference <https://docs.cupy.dev/en/stable/reference/index.html>`__
