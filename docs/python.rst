Python Setup (Without Admin right)
======================================

Download Python
---------------

- Visit https://www.python.org/downloads/windows/

- Download the latest Windows installer (64-bit)

**ADMINISTRATIVE PRIVILEGE** is **NOT REQUIRED** for installing python in
local user directory.

:doc:`environment` scripts are provided to simplify the
process of working with different Python versions and their virtual
environments during development.

Quick Download Links
--------------------

Windows Installers (x64) of various latest python releases are provided below for quick download

- `Python 3.11.4 <https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe>`_

- `Python 3.10.11 <https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe>`_

- `Python 3.9.13 <https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe>`_

- `Python 3.8.10 <https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe>`_

- `Python 3.7.9 <https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe>`_

- `Python 3.6.8 <https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe>`_

.. note:: 
   This documentation needs to be updated in the future when an advanced/latest 
   version of Python is released.  You are welcome to 
   `fork <https://gitlab.com/engineered-in/resources/-/forks/new>`_ 
   and update the documentation and submit a Merge request.

Install Python (Without Admin right)
----------------------------------------

- Open the downloaded ``python-x.x.xx-amd64.exe``

- Click on ``Customize installation`` (Choose location and features) button in the Installer

- **UNCHECK** ``py launcher`` and ``for all users (requires admin privileges)``

- Click Next

- **Check** ONLY ``Precompile standard library`` in the Advanced Options screen. 
  File Association, Shortcuts, Environment Variables, Debugging Symbols and Debug Binaries 
  are **NOT REQUIRED**

- Verify if the Customize install location points to    
  ``%userprofile%\AppData\Local\Programs\Python\Pythonxxx\``

- Click ``Install``
