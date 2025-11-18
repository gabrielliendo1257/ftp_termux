import flet as ft
from pyftpdlib.authorizers import DummyAuthorizer

from ftpsend.domain.user import UserConnected
from ftpsend.infrastructure.ftp_service import FtpServerService
from ftpsend.presentation.gui.features.ftp.components.user import UserComponent, ConnectedUsersCard

from ftpsend.presentation.gui.features.ftp.components.ftp_config import FtpBasicSettings


class HomePage(ft.Column):

    def __init__(self) -> None:
        super().__init__()
        self.__user_component = UserComponent(set_authorizer=self.set_authorizer)
        self.__ftp_basic_settings = FtpBasicSettings(start_server=self.start_server, stop_server=self.stop_server, remove_all_users=self.remove_all_users)
        self.__connected_user_card = ConnectedUsersCard()

        self.__path = None
        self.__authorizer = None
        self.__ftp_service = None
        self.scroll = ft.ScrollMode.AUTO

        self.padding = 10
        self.expand = True
        self.border_radius = 14
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 10
        self.controls = [
            ft.ListView(
                expand=True,
                spacing=10,
                auto_scroll=False,
                controls=[
                    self.__user_component,
                    self.__ftp_basic_settings,
                    self.__connected_user_card,
                ]
            )
        ]

    def start_server(self, hostname: str, port: int) -> None:
        from pyftpdlib.log import logging
        self.__ftp_service = FtpServerService(hostname, port, self.__authorizer, self.add_user_connected, self.remove_user_connected)
        self.__ftp_service.serve_forever()

    def stop_server(self) -> None:
        self.__ftp_service.stop_server()

    def set_authorizer(self, authorizer: DummyAuthorizer):
        self.__authorizer = authorizer

    def add_user_connected(self, user_connected: UserConnected):
        self.__connected_user_card.add_user(user_connected)

    def remove_user_connected(self, username: str, remote_port):
        self.__connected_user_card.remove_user(username, remote_port)

    def folder_chosen_destiny(self, path):
        self.__path = path

    def remove_all_users(self):
        self.__connected_user_card.remove_all_users()