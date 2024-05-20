from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class CommandInterface(ABC):
    _commands: Dict[str, CommandInterface] = dict()
    _name: str = None
    _buffer: str = None

    @classmethod
    def set_buffer(cls, data: str):
        cls._buffer = data

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
        print("Ejecutando el comando set")


class GetCommand(CommandInterface):
    _name = "get"

    def execute(self):
        print("Ejecutando el comando get")
