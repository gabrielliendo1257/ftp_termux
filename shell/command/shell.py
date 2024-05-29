from typing import List
from shell.command.commands import *
from shell.command.core.state import *
import shlex


class Shell:

    success = True
    _commands = list()
    state: State = None

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, value):
        value = shlex.split(value)
        self._buffer = value

    @property
    def promp(self):
        return self._promp

    @promp.setter
    def promp(self, promp: str):
        self._promp = promp

    def register(self):
        CommandInterface.add_command([SetCommand(), GetCommand()])

    def init(self):
        self.register()
        CommandInterface.add_command(self._commands)
        CommandInterface.set_buffer(self._buffer)
        try:
            exist_command = self._buffer[0] in CommandInterface.get_commands()
            Shell.success = True
        except IndexError:
            Shell.success = False
        if Shell.success:
            if not exist_command:
                self.state = ErrorState()
                self.state.on_object = self
                self.state.on_error()
            else:
                self.state = SuccessState()
                self.state.parameters = self.buffer
                self.state.on_object = self
                self.state.on_success()
