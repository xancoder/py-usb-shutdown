# py-usb-shutdown

is a watchdog that waits for a change on your USB ports and then immediately shuts down your computer

## Related project

* https://github.com/NateBrune/silk-guardian
* https://github.com/hephaest0s/usbkill

## Windows builds

tested in an unattended virtualbox Windows 10 virtual machine installation, so path and names should be adopted

in a powershell at project folder use following commands

```PowerShell
$url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
$dest = ".\python-3.12.1-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile $dest

Start-Process -FilePath $dest -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1" -Wait

C:\Users\vboxuser\AppData\Local\Programs\Python\Python312\python -m pip install --user pipx
C:\Users\vboxuser\AppData\Roaming\Python\Python312\Scripts\pipx install poetry

C:\Users\vboxuser\.local\bin\poetry install
C:\Users\vboxuser\.local\bin\poetry run build_windows
```

the app is located in the `dist` folder

## Linux builds

tested in an unattended virtualbox debian virtual machine installation

in a terminal at project folder use following commands

```bash
# as root
apt install -y python3-poetry
# as user
poetry install
poetry run build_linux
```

start the app in the `dist` folder with root privileges
