from ftp_protocol.handler.dependencies.check_dependencies import CheckDependencies
from ftp_protocol.core.native import Native

handler = CheckDependencies
handler.exist_executables(Native.commands)
