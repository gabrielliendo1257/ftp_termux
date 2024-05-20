from shell.command.commands import CommandInterface


class CutCommand(CommandInterface):
    _name = "cut"

    def execute(self):
        print("Ejecutando cut command")
