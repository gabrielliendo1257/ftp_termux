from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Tuple
from conf import *
import subprocess


class CommandInterface(ABC):

    @abstractmethod
    def execute(self): ...


class FtpAddress(CommandInterface):

    def __init__(self, receiver: Init, exec: Tuple[str]) -> None:
        self._receiver = receiver
        self.ftp_address = None
        self._exec = exec

    def execute(self):
        for exec in self._exec:
            result = self._receiver.process(exec)
            if result.stderr:
                print("Error al ejecutar el comando: " + exec)
                print(result.stderr)
            print("Result: " + result.stdout)


class CheckDependencies(CommandInterface):

    def __init__(self, receiver: Init, dependencies: str | Dict[str, str]) -> None:
        self._receiver = receiver
        self._dependencies = dependencies

    def execute(self):
        self._receiver.success = self._receiver.check_dependencies(self._dependencies)


class InstallerDependencies(CommandInterface): ...


class Init:

    _success: bool = None

    def __init__(self) -> None:
        self._dependencies = CheckDependencies(
            receiver=self, dependencies=DEPENDENCIES_AND_COMMANDS
        )
        self._dependencies.execute()

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value: bool):
        self._success = value

    def process(self, exec) -> subprocess.CompletedProcess[str]:
        return subprocess.run(exec, text=True, shell=True, capture_output=True)

    def _process_is_successful(self):
        if self.process.stderr:
            return False
        return True

    def check_dependencies(self, dependencies: str | Dict[str, str]) -> bool:
        success = True
        result = None
        if isinstance(dependencies, Dict):
            for dependencie, exec in dependencies.items():
                out = self.process(exec)
                if not out.stderr:
                    result = f"La dependencia ´{dependencie}´ esta en su sistema."
                else:
                    result = (
                        f"La dependencia ´{dependencie}´ no se reconoce en su sistema."
                    )
                    success = False
                print(result)
        else:
            out = self.process(dependencies)
            result = (
                f"La dependencia ´{dependencie}´ esta en su sistema."
                if not out.stderr
                else f"La dependencia ´{dependencie}´ no se reconoce en su sistema."
            )
            print(result)
        return success
