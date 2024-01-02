Python - Windows Environment Management 
=======================================

After Python installation, to use it directly from the command line, the Windows User
Environment Variables must be updated.

In addition to updating the Windows User Environment Variables, simple scripts
that enable working with multiple Python versions and their virtual environments
must be downloaded and configured.

User Environment Variable
-------------------------

To setup the User Environment Variables, open a Command Prompt and
paste the below script in it (use **Copy button** instead of manual select)::


    powershell
    # Start of Powershell Script
    $pyversion = 'Python310'
    $localPath = [Environment]::GetEnvironmentVariable('Path', 'user');
    $date = Get-Date -Format dd-mm-yyyy_hh-mm-ss
    $folderCreate = "$Env:USERPROFILE\.pyenvs\"
    if (-Not (Test-Path -Path $folderCreate)) {
        mkdir $folderCreate;
    }
    $output = "$Env:USERPROFILE\.pyenvs\path_as_on_${date}.txt"
    $localPath > $output
    $path2add = "$Env:USERPROFILE\.scripts\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Python\$pyversion\Scripts\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Python\$pyversion\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Git\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Git\cmd\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Git\bin\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Git\usr\bin\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\Git\mingw64\bin\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    $path2add = "$Env:LOCALAPPDATA\Programs\PowerShell\";
    If (!$localPath.contains($path2add)) {
        $localPath = $path2add + ";" + $localPath;
    }
    [Environment]::SetEnvironmentVariable('Path', $localPath, 'user');
    [Environment]::SetEnvironmentVariable('PYENVS', $Env:USERPROFILE + '\.pyenvs\' + $pyversion + '\', 'user')
    echo "Environment Variable Update Completed! > ☺"


The above script will append the following the Path (User Environment Variable):

    1. "%localappdata%\\Programs\\Python\\Python310\\"
    2. "%localappdata%\\Programs\\Python\\Python310\\Scripts\\"
    3. "%userprofile%\\.scripts\\"
    4. "%localappdata%\\Programs\\Git\\"
    5. "%localappdata%\\Programs\\Git\\cmd\\"
    6. "%localappdata%\\Programs\\Git\\bin\\"
    7. "%localappdata%\\Programs\\Git\\usr\\bin\\"
    8. "%localappdata%\\Programs\\Git\\mingw64\\bin\\"
    9. "%localappdata%\\\Programs\\PowerShell\\"

Additionally it creates PYENVS (User Environment Variable) with the value
"%userprofile%\\.pyenvs\\Python310\\"

Python Environment Management Scripts
-------------------------------------

To download and configure the Python Environment Management Scripts, open a Command Prompt
and paste the below script in it (use **Copy button** instead of manual select)::


    powershell -command Invoke-WebRequest https://gitlab.com/engineered-in/resources/-/raw/main/docs/Python-Environment-Management-Scripts.zip?inline=false -OutFile "%temp%\.scripts.zip"
    powershell -command Expand-Archive "%temp%\.scripts.zip" -DestinationPath "%userprofile%" -Force
    echo "Scripts Installation Successful! > ☺"


The above script will download and extract the scripts that enable working with
multiple Python versions and their Virtual Environments.

The scripts (command prompt .bat and powershell .ps1) will be downloded are
    1. pyenv.bat   &  pyenv.ps1
    2. py313.bat   &  py313.ps1
    3. py312.bat   &  py312.ps1
    4. py311.bat   &  py311.ps1
    5. py310.bat   &  py310.ps1
    6. py39.bat    &  py39.ps1
    7. py38.bat    &  py38.ps1
    8. py37.bat    &  py37.ps1
    9. py36.bat    &  py36.ps1

Switching Python Version
------------------------

The default python version is ``Python 3.10``.

For switching to another python version, say Python 3.9, in the command prompt or powershell
simply type ::

    py39

This will execute ``py39.bat`` or ``py39.ps1`` which will set the current python environment as
Python 3.9

Creating Virtual Environment
----------------------------

``pyenv.bat`` or ``pyenv.ps1`` is used for creating new virtual environments (venv) in the
current Python version.

To create a virtual environment named ``test``, in the command prompt or powershell simply
type::

    pyenv test

This will check if a venv named ``test`` exist in the current python
version (say `%userprofile%/.pyenvs/Python310/` ).

If the ``test`` venv exist, it will activate it.  

If the ``test`` venv does not exist, a new venv named ``test`` will be created.

Activating Virtual Environment
------------------------------

``pyenv.bat`` or ``pyenv.ps1`` is used for activating existing virtual environments (venv) in the
current Python version.

To activate an existing virtual environment named ``test``, in the command prompt or powershell
simply type::

    pyenv test

This will check if a venv named ``test`` exist in the current python
version (say `%userprofile%/.pyenvs/Python310/` ).

If the ``test`` venv exist, it will activate it.  

If the ``test`` venv does not exist, a new venv named ``test`` will be created.
