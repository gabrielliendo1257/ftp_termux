from ftp_protocol.commands import Init
from shell.command.view.handler import view_selection
from conf import *

init = Init()

if init.success:
    buffer = sys.argv
    view_selection(arguments=buffer)
