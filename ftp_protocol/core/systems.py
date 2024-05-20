from .native import NativeSO
from typing import List
import sys
import os


class windowsSystem(NativeSO):

    _dependencies: str = None
    shell_exec: str = "powershell.exe "
    _instance = None

    def get_commands(self):

        return {
            "check_dependencies": self.shell_exec + "Get-Command $[]",
            "ftp_host_web": self.shell_exec
            + "(Invoke-WebRequest -Uri 'https://api64.ipify.org?format=json').Content | ConvertFrom-Json | Select-Object -ExpandProperty ip",
            "ftp_host_local": self.shell_exec
            + "(Get-NetIPAddress | Where-Object { $_.AddressFamily -eq 'IPv4' -and $_.InterfaceAlias -eq 'Ethernet' }).IPAddress",
            "ftp_port": 21,
        }


class LinuxSystem(NativeSO):
    shell_exec: str = "bash "
    parameter: str = "-c "
    exec: str = shell_exec + parameter

    def __init__(self) -> None:
        self._support = self._shell_is_supported()
        if not self._support:
            print("Sistema o shell no soportada.")
            sys.exit(-3)

    def _shell_is_supported(self) -> bool:
        shell_path = os.environ.get("SHELL")
        if shell_path in self.get_supported_shells():
            return True
        return False

    def _get_supported_shells(self) -> List[str]:
        return ["bash"]

    def get_commands(self):
        return {
            "check_dependencies": self.exec + "which $[]",
            "ftp_host_web": self.exec
            + "(Invoke-WebRequest -Uri 'https://api64.ipify.org?format=json').Content | ConvertFrom-Json | Select-Object -ExpandProperty ip",
            "ftp_host_local": self.exec
            + "(Get-NetIPAddress | Where-Object { $_.AddressFamily -eq 'IPv4' -and $_.InterfaceAlias -eq 'Ethernet' }).IPAddress",
            "ftp_port": 21,
        }
