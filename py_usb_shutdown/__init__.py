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
            'shutdown': 'shutdown now -h',
        },
        'Windows': {
            'shutdown': 'shutdown /s /f /t 0'
        }
    }
}


def watch_drives() -> None:
    system = check_platform_system(CONFIG)

    prev_devices = read_devices(system)
    while True:
        devices = read_devices(system)
        if prev_devices != devices:
            os.system(CONFIG['platforms'][system]['shutdown'])
            prev_devices = devices
        time.sleep(CONFIG['poll_interval'])


def check_platform_system(config: dict) -> str:
    system = platform.system()

    supported_systems = [k for k in config['platforms']]
    if system not in supported_systems:
        print(f'[-] platform system not supported: {system}')
        sys.exit(1)
    return system


def read_devices(system: str) -> list:
    if system == 'Linux':
        ret = list_drives_linux()
    elif system == 'Windows':
        ret = list_drives_windows()
    else:
        print(f'[-] no list devices method due to platform: {system}')
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
        print('[-] failed to list drives on windows')
        return []
    devices = json.loads(proc.stdout)
    return devices
