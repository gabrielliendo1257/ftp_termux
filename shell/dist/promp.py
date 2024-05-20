from shell.command.view.cli.promp import Promp
from shell.command.shell import Shell
import os


class MyCustomPromp(Promp):

    def promp(self):
        ftp_promp = "ftp:shell"
        self._promp = ftp_promp + "> "
