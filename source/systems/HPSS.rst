The centralized, long-term data archive system at National Environmental Security Computing Center (NESCC) is based on IBM's High Performance Storage System (HPSS). The NESCC HPSS environment includes 22 petabytes of front-end disk cache, five Oracle SL8500 enterprise tape libraries, three Spectra Logic TFinity tape libraries, and 148 tape drives. Total available capacity is 430 PB. HPSS is accessible from WCOSS2, Hera, Niagara, Jet, and Gaea.

Users should keep the following things in mind when using the HPSS system:

* The HPSS system is well suited for storing large volumes of data.
* Users should avoid transferring many small files (in the megabyte range or smaller) to HPSS since the process of moving numerous individual small files to and from tape is inefficient. Please tar up small files into one large tar file before storing data into HPSS, or use HTAR.
* All data stored in HPSS is single copy. Deleted data cannot be recovered.
* HPSS is not accessible from compute nodes. Access is available via Hera/Niagara/Jet front-end nodes (FEs), Gaea Data Transfer Nodes (DTN’s), and WCOSS2 transfer nodes.
* Batch jobs that require access to HPSS should be submitted to the respective systems service or transfer queues.

For questions regarding the HPSS system, email rdhpcs.hpss.help@noaa.gov.