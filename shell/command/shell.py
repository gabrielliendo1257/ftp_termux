from typing import List
from shell.command.commands import *
from shell.dist.commands import *


class Shell:

    success = True
    _commands = list()

    def __init__(self, buffer: str = None, promp: str = None) -> None:
        self._buffer = buffer
        self._promp = promp

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, value):
        self._buffer = value

    @property
    def promp(self):
        return self._promp

    @promp.setter
    def promp(self, promp: str):
        self._promp = promp

    def register(value):
        CommandInterface.add_command([SetCommand(), GetCommand(), CutCommand()])

    def init(self):
        self.register()

        CommandInterface.add_command(self._commands)
        CommandInterface.set_buffer(self._buffer)
        exist_command = self._buffer in CommandInterface.get_commands()
        if not exist_command:
            self.success = False
            print("El comando nose reconoce ==> " + self._buffer)
        else:
            self.success = True
            if self.success:
                command_obj = CommandInterface.get_commands().get(self._buffer)
                command_obj.execute()
