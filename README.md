# py-usb-shutdown

is a watchdog that waits for a change on your USB ports and then immediately shuts down your computer

## Related project

* https://github.com/NateBrune/silk-guardian
* https://github.com/hephaest0s/usbkill

## Windows builds

tested in an unattended virtualbox Windows 10 virtual machine installation

in a powershell manually install python from https://www.python.org/

```PowerShell
$url = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
$dest = ".\python-3.11.5-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile $dest
.\python-3.11.5-amd64.exe /quiet InstallAllUsers=0 PrependPath=1
```

accept the User Account Control (UAC) and after a period of time

use the following commands to build an executable found in the default `dist` directory

```PowerShell
py -m pip install --user pipx
C:\Users\vboxuser\AppData\Roaming\Python\Python311\Scripts\pipx install poetry
cd Z:\py-usb-shutdown
C:\Users\vboxuser\.local\pipx\venvs\poetry\Scripts\poetry.exe install
C:\Users\vboxuser\.local\pipx\venvs\poetry\Scripts\poetry.exe run build_windows
```
