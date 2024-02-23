# py-usb-shutdown

is a watchdog that waits for a change on your USB ports and then immediately shuts down your computer

## Related project

* https://github.com/NateBrune/silk-guardian
* https://github.com/hephaest0s/usbkill

## Builds

the app is located in the `dist` folder later

under linux run as root the fake `LinuxLogonService` application

### Windows

tested in an unattended virtualbox Windows 10 virtual machine installation

in a powershell at project folder use the following commands

```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\scripts\windows_setup_python.ps1
.\scripts\windows_build.ps1
```

### Linux

tested in an unattended virtualbox debian 12 virtual machine installation

in a shell at project folder use the following commands

```bash
chmod +x ./scripts/linux_build.sh
./scripts/linux_build.sh
```
