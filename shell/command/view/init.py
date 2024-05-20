from shell.dist.promp import MyCustomPromp
from abc import ABC, abstractmethod


class ViewInterface(ABC):

    @abstractmethod
    def rendering(self): ...


class Cli(ViewInterface):

    def rendering(self):
        promp = MyCustomPromp()
        from shell.command.shell import Shell

        shell = Shell()
        shell.promp = promp.get_promp()
        try:
            while True:
                user = input(shell.promp)
                shell.buffer = user
                shell.init()
        except KeyboardInterrupt:
            print("Saliendo y cerrando procesos abiertos.")


class Gui(ViewInterface):

    def rendering(self):
        print("Funcion no implementada")
