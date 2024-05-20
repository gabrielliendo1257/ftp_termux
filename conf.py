from ftp_protocol.core.native import NativeSO
from ftp_protocol.core.systems import windowsSystem, LinuxSystem
from typing import Dict
import yaml
import sys
import os
import re

regex = re.compile(r"\$\[.*?\]")

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

EXTERNAL_DEPENDENCY_FILE = os.path.join(BASE_DIR, "external.yml")

SYSTEM = NativeSO.get_platform()

dependencies = []
with open(os.path.join(BASE_DIR, EXTERNAL_DEPENDENCY_FILE), "r") as file:
    data_external = yaml.safe_load(file)
    linux_dependencies = data_external["external"]["linux"]
    windows_dependencies = data_external["external"]["windows"]
    if SYSTEM == "windows":
        os_obj = windowsSystem(windows_dependencies)
        dependencies = windows_dependencies
        commands = os_obj.get_commands()
    elif SYSTEM == "linux":
        os_obj = LinuxSystem()
        dependencies = linux_dependencies
        commands = os_obj.get_commands()
    else:
        print("Sistema o shell no soportada.")
        sys.exit(-3)

dpn_comnd: Dict[str, str] = {}
for exec in dependencies:
    dpn_comnd[exec] = regex.sub(exec, commands["check_dependencies"])

DEPENDENCIES_AND_COMMANDS = dpn_comnd

FTP_HOST_WEB = commands["ftp_host_web"]
FTP_HOST_LOCAL = commands["ftp_host_local"]
FTP_PORT = commands["ftp_port"]
