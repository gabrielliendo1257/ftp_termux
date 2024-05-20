from typing import Dict, List
from abc import ABC, abstractmethod
import platform

# -ErrorAction SilentlyContinue


def get_native_commands(os: str) -> Dict[str, str]:
    command_map = {
        "windows": {
            "check_dependencies": "powershell.exe Get-Command $[]",
            "ftp_host": "",
            "ftp_port": "",
        },
        "linux": {
            "check_dependencies": "wihch $[]",
        },
    }
    return command_map.get(os)


class Native:

    os_platform = platform.system().lower()
    commands = get_native_commands(os_platform)


class NativeSO(ABC):

    _dependencies: List[str]

    def __init__(self, dependencies: List[str]) -> None:
        self._dependencies = dependencies

    @staticmethod
    def get_platform():
        return platform.system().lower()

    @abstractmethod
    def get_commands(self): ...
