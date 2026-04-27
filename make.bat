@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

SET SOURCEDIR=source
SET BUILDDIR=build
SET VENV=.venv
SET SPHINXBUILD=%VENV%\Scripts\sphinx-build
SET LINTRST=%VENV%\Scripts\doc8
SET PYTHON=%VENV%\Scripts\python
SET PIP=%VENV%\Scripts\pip
SET MIN_PY_VER=3.10
SET PORT=8000

REM Verify python3 is available and meets minimum version requirement.
python --version >NUL 2>NUL
if errorlevel 1 (
	echo.
	echo.Python not found. Please install Python %MIN_PY_VER% or newer.
	exit /b 1
)

for /f "tokens=*" %%V in ('python -c "import sys; print('ok' if sys.version_info >= (3,10) else 'old')"') do set PYTHON3_OK=%%V
if "%PYTHON3_OK%" == "old" (
	for /f "tokens=*" %%V in ('python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"') do set PYTHON3_VER=%%V
	echo.
	echo.Python %MIN_PY_VER%+ required, found %PYTHON3_VER%. Please upgrade Python.
	exit /b 1
)

REM Create the virtual environment and install dependencies if needed.
if not exist "%VENV%\Scripts\activate" (
	echo Creating Python virtual environment in %VENV%\ ...
	python -m venv %VENV%
	echo Installing dependencies from requirements.txt ...
	%PIP% install --quiet --upgrade pip
	%PIP% install --quiet -r requirements.txt
	echo Virtual environment ready.
)

if "%1" == "" goto help
if "%1" == "distclean" goto distclean
if "%1" == "lint" goto lint
if "%1" == "serve" goto serve
if "%1" == "venv" goto end

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
echo.  lint        to run a linter on the RST files in the source directory
echo.  serve       to start a local web server on port %PORT% to view the built docs
echo.  venv        to create the Python virtual environment and install dependencies
echo.  distclean   to remove the build directory and the virtual environment
goto end

:lint
%LINTRST% %SOURCEDIR%
goto end

:serve
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
echo Serving documentation at http://localhost:%PORT% (press Ctrl+C to stop)
%PYTHON% -m http.server %PORT% --directory "%BUILDDIR%\html"
goto end

:distclean
echo Removing build directory %BUILDDIR%\ ...
if exist "%BUILDDIR%" rmdir /s /q %BUILDDIR%
echo Removing virtual environment %VENV%\ ...
if exist "%VENV%" rmdir /s /q %VENV%
goto end

:end
popd
