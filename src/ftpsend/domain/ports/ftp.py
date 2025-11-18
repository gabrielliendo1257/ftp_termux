from abc import ABC, abstractmethod


class FtpServerBase(ABC):

    def __init__(self, host: str, port: int) -> None:
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @abstractmethod
    def serve_forever(self): ...


class FtpClientBase(ABC):

    @abstractmethod
    def connect_to_server(self): ...

    @abstractmethod
    def send_command(self): ...
