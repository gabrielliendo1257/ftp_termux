from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class CommandInterface(ABC):
    _commands: Dict[str, CommandInterface] = dict()
    _name: str = None
    _buffer: List[str] = None

    @classmethod
    def set_buffer(cls, data: List[str]):
        cls._buffer = data

    @classmethod
    def get_params(cls):
        return cls._buffer

    @classmethod
    def get_args(cls):
        return cls._buffer[1::]

    @classmethod
    def add_command(cls, command: CommandInterface | List[CommandInterface]):
        command_name: str = None
        if isinstance(command, CommandInterface):
            if not command._name:
                command_name = command.__class__.__name__
            else:
                command_name = command._name
            cls._commands[command_name] = command
        else:
            for interface in command:
                if not interface._name:
                    command_name = command.__class__.__name__
                else:
                    command_name = interface._name
                cls._commands[command_name] = interface

    @classmethod
    def get_commands(cls) -> Dict[str, CommandInterface]:
        return cls._commands

    @abstractmethod
    def execute(self): ...


class SetCommand(CommandInterface):
    _name = "set"

    def execute(self):
        if len(CommandInterface.get_args()) == 0:
            print("No se introdujeron parametros.")
            print(
                "Para ejecutar el manual de ayuda ejecute ==> ", self._name, " --help"
            )
        else:
            print(CommandInterface.get_params())
            print("Ejecutando set")
            print("Con parametros: ", CommandInterface.get_params()[1::])


class GetCommand(CommandInterface):
    _name = "get"

    def execute(self):
        print("Ejecutando el comando get")
        print("Con parametros: ", CommandInterface.get_params()[1::])
