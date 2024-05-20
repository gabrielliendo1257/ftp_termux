from abc import ABC


class Promp():

    def __init__(self) -> None:
        self._promp: str = None
        self.promp()

    def promp(self):
        self._promp = "$ "

    def get_promp(self):
        return self._promp

