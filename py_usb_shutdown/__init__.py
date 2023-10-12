import json
import os
import platform
import re
import subprocess
import sys
import time

CONFIG = {
    'poll_interval': 0.25,
    'platforms': {
        'Linux': {
            'shutdown': 'shutdown -h now'
        },
        'Windows': {
            'shutdown': 'shutdown /s /f /t 0'
        }
    }
}


def watch_drives() -> None:
    current_platform = check_platform(CONFIG)
    prev = read_devices(current_platform)
    while True:
        devices = read_devices(current_platform)
        if prev != devices:
            os.system(CONFIG["platforms"][current_platform]["shutdown"])
            prev = devices
        time.sleep(CONFIG['poll_interval'])


def check_platform(config: dict) -> str:
    current_platform = platform.system()
    supported_platforms = [k for k in config['platforms']]
    if current_platform not in supported_platforms:
        print('platform system not supported')
        sys.exit(1)
    return current_platform


def read_devices(current_platform: str) -> list:
    if current_platform == 'Linux':
        ret = list_drives_linux()
    elif current_platform == 'Windows':
        ret = list_drives_windows()
    else:
        print(f'[-] no list devices method due to platform: {current_platform}')
        sys.exit(1)
    return ret


def list_drives_linux() -> list:
    """
    Get a list of device ids using 'lsusb'
    :return: list of device ids
    """
    regex = re.compile(r'(.*)\s+')
    devices = regex.findall(subprocess.check_output(
        args=['lsusb'],
        shell=True
    ).decode('utf-8').strip())
    return devices


def list_drives_windows() -> any:
    """
    Get a list of drives using WMI
    :return: list of Drive
    """
    create_no_window = 0x08000000
    proc = subprocess.run(
        args=[
            'powershell',
            '-noprofile',
            '-command',
            'Get-WmiObject -Class Win32_USBControllerDevice'
            + ' | Select-Object deviceid,volumename,drivetype'
            + ' | ConvertTo-Json'
        ],
        text=True,
        stdout=subprocess.PIPE,
        creationflags=create_no_window
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        print('Failed to enumerate drives')
        return []
    devices = json.loads(proc.stdout)
    return devices
