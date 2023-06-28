
Clears the Recycle Bin and certain directories:
C:\Windows\Prefetch
C:\Windows\Temp
Downloads
%TEMP%

1. Clone the repo
2. Install the venv if you don't have it already - pip install virtualenv
3. Createa new one python -m venv myenv
4. Activate it myenv\Scripts\activate - Windows; source myenv/bin/activate - macOS, Linux
5. Install these dependencies with pip install -r requirements.txt
6. Setup a bat script as so:

@echo off

echo Running script as administrator...
cd /d "%~dp0"
powershell -Command "Start-Process cmd -ArgumentList '/k cd C:\Users\{Username}\temp_clear\ && tempC\Scripts\activate && python main.py' -Verb RunAs"

Save as: {file_name}.bat
