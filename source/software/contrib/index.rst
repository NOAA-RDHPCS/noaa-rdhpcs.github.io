
.. _contrib:

#######
Contrib
#######

Managing Packages in /contrib
=============================

The system staff do not have the resources to maintain every piece of software requested. There are also cases where developers of the software are the system users, and putting a layer in between them and the rest of the system users is inefficient. To support these needs, we have developed a ``/contrib`` package process. A /contrib package is one that is maintained by a user on the system. The system staff are not responsible for the use or maintenance of these packages.


Responsibilities of a Contrib Package Maintainer
------------------------------------------------

Maintainers are expected to:

* Follow the naming conventions and guidelines outlined in this document
* Apply security updates as quickly as possible after they become availble
* Update software for bug fixes and functionality as users request
* Respond to user email requests for help using the software

Contrib Packages Guidelines
---------------------------


* The package should be a single program or toolset.
   * We want to prevent having a single directory being a repository for many different packages.
* If you support multiple functions, please request multiple packages.
* The package may have build dependencies on other packages, but it must otherwise be self-contained.
* The package may not contain links to files in user or project directories.
* We expect each package to be less than 100MB.
* If you need more, please tell us when you request your package.
* We can support larger packages but we need to monitor the space used.
* We expect each package to have less than 100 files.


Contrib Package Maintainer Requests
-----------------------------------
If you wish to maintain a package in contrib, please send a request to the Help System with:

* List of the packages you wish to maintain.
* Justification why each is needed.
* The user who will be maintaining the package.
   * In certain cases, multiple users can manage a package, and unix group write permissions may be granted for the directory. In that case, specify the unix group that will be maintaining the package.

Managing a Contrib Package
--------------------------

After your request has been approved to use space in the /contrib directory, two directories will be created for you:

``/contrib/<package>``

``/contrib/<package>/modulefiles``

This is where you will install your software for this package and optionally install a module to allow users to load the environmental settings necessary to use this package. The variable <package> is the name of the /contrib package you requested. The directory convention of /contrib is designed to match that of /apps. Thus, one piece of software goes into a subdirectory under the /contrib level. If you want to manage multiple packages, please request multiple /contrib package. You can do this all at one time when submitting your request to the Help System.


Maintaining "Metadata" for the contrib Package
----------------------------------------------

Since contrib packages are intended to be used by other users on the system it will be helpful to have a /contrib/<package>/README file that contains at least the following information:

* Package Name:
* Purpose:
* Maintainer:
* Contact info for questions/help:
* Any other info that will be useful for general users to know


Contrib Package Directory Naming Conventions
--------------------------------------------
When installing software into your /contrib directory, first determine if this is software that should be versioned (multiple versions may exist at one time) or unversioned (there will only ever be one version installed, and upgrade will overwrite the existing software). For verisoned software, please install it into a subdirectory of your package that is named after the version number. For supporting multiple versions of software the install path should be:

``/contrib/<package>/<version>``

Where <package> is the directory assigned to you and $VER is the version number. Thus if your package is named ferret and you are installing the version 3.2.6, the software should be installed in:

``/contrib/ferret/3.2.6``

For supporting un-versioned software, only install the software directly into your package directory:

``/contrib/<package>/``