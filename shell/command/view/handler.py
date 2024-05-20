from shell.command.view.init import Cli, Gui
from typing import List


def view_selection(arguments: List[str]):
    if len(arguments) > 1 and arguments[1].lower() == "cli":
        cli_obj = Cli()
        cli_obj.rendering()
    elif len(arguments) > 1 and arguments[1].lower() == "gui":
        gui_obj = Gui()
        gui_obj.rendering()
    elif len(arguments) == 1:
        print("Nose introdujeron parametros.")
    else:
        print("Comando no reconocido ==> ", arguments)
