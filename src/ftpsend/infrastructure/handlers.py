from collections.abc import Callable

from pyftpdlib.handlers import FTPHandler

from ftpsend.domain.user import UserConnected


class ConnectionHandler(FTPHandler):

    add_user_connected: Callable
    remove_user_connected: Callable

    def on_connect(self):
        print("Connection established")

    def on_disconnect(self):
        self.remove_user_connected(self.username, self.remote_port)

    def on_login(self, username):
        self.add_user_connected(UserConnected(self.remote_ip, self.remote_port, self.started, username))