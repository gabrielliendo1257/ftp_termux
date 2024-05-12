from typing import Dict, Any
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
