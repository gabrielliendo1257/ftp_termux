from collections.abc import Callable
from fcntl import FASYNC

import flet as ft


class FtpBasicSettings(ft.Container):

    def __init__(self, start_server: Callable, stop_server: Callable, remove_all_users: Callable):
        super().__init__()
        self.__start_server = start_server
        self.__stop_server = stop_server
        self.__remove_all_users = remove_all_users

        self.__hostname = ft.TextField(label="Hostname", on_change=self.validate)
        self.__port = ft.TextField(label="Port", on_change=self.validate)

        self.__button_start_server = ft.ElevatedButton(text="Start server", expand=True, disabled=True,
                                                       on_click=self.start_server)
        self.__button_stop_server = ft.ElevatedButton(text="Stop server", expand=True, disabled=True,
                                                      on_click=self.stop_server)

        self.bgcolor = ft.Colors.with_opacity(0.06, ft.Colors.BLUE_200)
        self.padding = 20
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.__hostname,
                        self.__port,
                    ]
                ),
                ft.Row(
                    controls=[
                        self.__button_start_server,
                        self.__button_stop_server,
                    ]
                )
            ]
        )

    def validate(self, e):
        if self.__hostname.value == "" or self.__port.value == "":
            return

        self.__button_start_server.disabled = False
        self.update()

    def start_server(self, e):
        self.__start_server(self.__hostname.value, int(self.__port.value))

        self.__hostname.disabled = True
        self.__port.disabled = True
        self.__button_start_server.disabled = True
        self.__button_stop_server.disabled = False

        self.update()

    def stop_server(self, e):
        self.__stop_server()

        self.__hostname.disabled = False
        self.__port.disabled = False
        self.__button_start_server.disabled = False
        self.__button_stop_server.disabled = True

        self.__remove_all_users()

        self.update()
