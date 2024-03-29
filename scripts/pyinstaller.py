import pathlib

import PyInstaller.__main__

HERE = pathlib.Path(__file__).parent.absolute()
path_to_icon = str((HERE / '../assets/logo.ico').resolve())
path_to_main = str((HERE / '../cmd/cli.py').resolve())

LN = 'LinuxLogonService'
WN = 'WindowsLogonService'


def build_linux():
    PyInstaller.__main__.run([
        path_to_main,
        '--clean',
        '--onefile',
        '--windowed',
        f'-n{LN}'
    ])


def build_windows():
    PyInstaller.__main__.run([
        path_to_main,
        '--clean',
        '--onefile',
        '--windowed',
        f'--icon={path_to_icon}',
        f'-n{WN}'
    ])
