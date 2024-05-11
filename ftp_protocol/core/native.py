from typing import Dict, Any
import platform


def get_native_commands(os: str) -> Dict[str, str]:
    command_map = {
        "windows": {
            "node": "powershell.exe Get-Command npm -ErrorAction SilentlyContinue",
            "java": "powershell.exe Get-Command java -ErrorAction SilentlyContinue",
            "maven": "powershell.exe Get-Command mvn -ErrorAction SilentlyContinue",
            "maven": "powershell.exe Get-Command mvnn -ErrorAction SilentlyContinue",
        },
        "linux": {},
    }
    return command_map.get(os)


class Native:

    commands = get_native_commands(platform.system().lower())
