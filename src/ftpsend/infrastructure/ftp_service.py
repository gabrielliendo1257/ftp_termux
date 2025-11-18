import threading
from collections.abc import Callable

from pyftpdlib.handlers import DummyAuthorizer, FTPHandler
from pyftpdlib.servers import FTPServer

from ftpsend.domain.ports.ftp import FtpServerBase
from ftpsend.infrastructure.handlers import ConnectionHandler


class FtpServerService(FtpServerBase):

    def __init__(self, host: str, port: int, authorizer: DummyAuthorizer, add_user_connected: Callable, remove_user_connected: Callable) -> None:
        super().__init__(host, port)
        self.__authorizer = authorizer

        self.__handler = ConnectionHandler
        self.__handler.add_user_connected = add_user_connected
        self.__handler.remove_user_connected = remove_user_connected
        self.__handler.authorizer = self.__authorizer

        address = tuple([host, port])
        self.__server = FTPServer(address, self.__handler)
        self.__thread = None

    def get_handler(self):
        return self.__handler

    def serve_forever(self):
        self.__thread = threading.Thread(target=self.__server.serve_forever, daemon=True)
        self.__thread.start()

    def stop_server(self):
        self.__server.close_all()
        self.__server.close()

        if self.__thread:
            self.__thread.join(timeout=1)
        print("FTP server stopped.")