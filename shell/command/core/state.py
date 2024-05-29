from abc import ABC, abstractmethod
from typing import List


class State(ABC):
    _on_object: object = None

    @property
    def on_object(self):
        return self._on_object

    @on_object.setter
    def on_object(self, value):
        self._on_object = value

    def on_command(self): ...
    def on_error(self): ...
    def on_success(self): ...
    def on_exit(self): ...
    def on_locked(self): ...


class SuccessState(State):
    parameters: List[str] = None
    command: str = None

    def on_success(self):
        from shell.command.shell import Shell

        Shell.success = True
        from shell.command.commands import CommandInterface

        command_obj = CommandInterface.get_commands().get(
            CommandInterface.get_params()[0]
        )
        command_obj.execute()

    def on_error(self):
        print("Sin ocurrencia de errores.")


class ErrorState(State):

    def on_error(self):
        from shell.command.shell import Shell

        Shell.success = False
        print("Error desconocido")


class ExitState(State):

    def on_exit(self):
        print("Saliendo del programa.")
