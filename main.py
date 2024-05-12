from ftp_protocol.handler.dependencies.check_dependencies import CheckDependencies
from conf import *

handler = CheckDependencies
handler.exist_executables(DEPENDENCIES_AND_COMMANDS)
