from ftp_protocol.core.native import Native
from typing import Dict
import yaml
import os
import re

regex = re.compile(r"\$\[.*?\]")

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

EXTERNAL_DEPENDENCY_FILE = os.path.join(BASE_DIR, "external.yml")

SYSTEM = Native.os_platform

dpn = []
with open(os.path.join(BASE_DIR, EXTERNAL_DEPENDENCY_FILE), "r") as file:
    data_external = yaml.safe_load(file)
    linux_dependencies = data_external["external"]["linux"]
    windows_dependencies = data_external["external"]["windows"]
    if SYSTEM == "windows":
        dpn = windows_dependencies
    else:
        dpn = linux_dependencies

dpn_comnd: Dict[str, str] = {}
for exec in dpn:
    dpn_comnd[exec] = regex.sub(exec, Native.commands["check_dependencies"])

DEPENDENCIES_AND_COMMANDS = dpn_comnd

FTP_HOST = ""
FTP_PORT = ""
