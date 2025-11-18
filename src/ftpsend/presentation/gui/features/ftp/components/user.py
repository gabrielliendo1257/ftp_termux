from collections.abc import Callable
from typing import Dict, List

import flet as ft

from ftpsend.domain.user import UserConnected
from ftpsend.infrastructure.authorizers import AdminAuthorizer
from ftpsend.presentation.gui.features.ftp.components.file import FolderPickerCard

PERMISSIONS = {
    "e": ("Enter", ft.Icons.FOLDER_OPEN),
    "l": ("List", ft.Icons.LIST),
    "r": ("Download", ft.Icons.DOWNLOAD),
    "a": ("Append", ft.Icons.ADD_CIRCLE_OUTLINE),
    "d": ("Delete", ft.Icons.DELETE),
    "f": ("Rename", ft.Icons.DRIVE_FILE_RENAME_OUTLINE),
    "m": ("Make Dir", ft.Icons.CREATE_NEW_FOLDER),
    "w": ("Upload", ft.Icons.UPLOAD),
}


class UserComponent(ft.Container):

    def __init__(self, set_authorizer: Callable):
        super().__init__()
        self.__folder_selected = None
        self.__default_permissions = "lr"
        self.__selected_permission_control: Dict[str, ft.Chip] = {}

        self.__username = ft.TextField(label="Username", on_change=self.validate)
        self.__password = ft.TextField(label="Password", on_change=self.validate)
        self.__permissions = ft.TextField(label="Permissions", on_change=self.validate)
        self.__selected_folder_picker = FolderPickerCard(on_folder_selected=self.folder_selected,
                                                         main_title="Carpeta (FTP).")

        self.__custom_authorizer = AdminAuthorizer()
        self.__authorizer = set_authorizer

        self.__add_button = ft.ElevatedButton("Agregar usuario", on_click=self.add_user, disabled=True)
        self.__dlg_modal_view = ft.AlertDialog(
            modal=True,
            title=ft.Text("Usuario agregado."),
            content=ft.Text("Usuario agregado exitosamente."),
            actions=[
                ft.TextButton("Aceptar", on_click=lambda e: self.page.close(self.__dlg_modal_view)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.__permission_view = None

        self.bgcolor = ft.Colors.with_opacity(0.06, ft.Colors.BLUE_200)
        self.padding = 20
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            alignment=ft.alignment.center,
            controls=[
                ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text("Usuarios FTP", size=18, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                self.__username,
                                self.__password,
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Asignar permisos", size=16, weight=ft.FontWeight.BOLD),
                                self.ordered_row(3, self.generate_chip_view()),
                            ]
                        ),
                        self.__selected_folder_picker,
                    ]
                ),
                self.__add_button,
            ]
        )

    def validate(self, e=None):
        if self.__username.value == "" or self.__password.value == "" or self.get_permissions() == "" or self.__folder_selected is None:
            return

        self.__add_button.disabled = False
        self.update()

    def add_user(self, e):

        print("Permissions: ", self.get_permissions())
        self.__custom_authorizer.add_user(
            self.__username.value, self.__password.value, str(self.__folder_selected), perm=self.get_permissions()
        )

        self.__authorizer(self.__custom_authorizer)
        self.page.open(self.__dlg_modal_view)
        self.__username.value = ""
        self.__password.value = ""
        self.__permissions.value = ""
        self.__add_button.disabled = True

        self.update()

    def folder_selected(self, path):
        self.__folder_selected = path

        self.validate()

    def generate_chip_view(self):
        chips_view = []

        for key, (label, icon) in PERMISSIONS.items():
            chip = ft.Chip(
                label=ft.Text(label),
                selected=key in self.__default_permissions,
                selected_color=ft.Colors.BLUE_700,
                bgcolor=ft.Colors.BLUE_GREY_800,
                shape=ft.RoundedRectangleBorder(radius=20),
                label_style=ft.TextStyle(color=ft.Colors.WHITE),
                leading=ft.Icon(icon, color=ft.Colors.WHITE60, size=18),
                on_select=self.on_change,
            )
            chips_view.append(chip)
            self.__selected_permission_control[key] = chip

        return chips_view

    def permissions_view(self) -> ft.Column:
        chips_view = []

        for key, (label, icon) in PERMISSIONS.items():
            chip = ft.Chip(
                label=ft.Text(label),
                selected=key in self.__default_permissions,
                selected_color=ft.Colors.BLUE_700,
                bgcolor=ft.Colors.BLUE_GREY_800,
                shape=ft.RoundedRectangleBorder(radius=20),
                label_style=ft.TextStyle(color=ft.Colors.WHITE),
                leading=ft.Icon(icon, color=ft.Colors.WHITE60, size=18),
                on_select=self.on_change,
            )

            chips_view.append(chip)
            self.__selected_permission_control[key] = chip

        return ft.Column(
            expand=True,
            controls=[
                ft.Text("Asignar permisos", size=16, weight=ft.FontWeight.BOLD),
                ft.GridView(
                    controls=chips_view,
                ),
            ]
        )

    def ordered_row(self, columns: int, data: list):
        def decision_column(count_data):
            num_column = count_data // columns
            rest = count_data % columns

            return num_column, rest

        num_columns, rest = decision_column(len(data))

        column_created = {}
        row = ft.Row()
        chip_views = self.generate_chip_view()

        for index in range(int(num_columns) + 1):
            column_created[str(index)] = ft.Column()

        for index in range(num_columns):
            for _ in range(num_columns + 1):
                chip_view = chip_views.pop(0)
                column_created.get(str(index)).controls.append(chip_view)

        for _ in range(rest):
            chip_view = chip_views.pop(0)
            column_created.get(str(rest)).controls.append(chip_view)

        for _, col_widget in column_created.items():
            row.controls.append(col_widget)

        return row

    def on_change(self, e):
        pass

    def get_permissions(self) -> str:
        enabled_keys = [k for k, chip in self.__selected_permission_control.items() if chip.selected]
        return "".join(enabled_keys)


class ConnectedUsersCard(ft.Container):

    def __init__(self):
        super().__init__()
        self.__users_references = {}

        self.bgcolor = "#1e1e1e"
        self.padding = 20
        self.border_radius = 12

        self.users_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )

        self.content = ft.Column(
            controls=[
                ft.Text(
                    "Usuarios Conectados",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Divider(color="#333333"),
                self.users_list
            ]
        )

    # ------------------------------------------------------
    # MÉTODO PARA ACTUALIZAR EL COMPONENTE
    # ------------------------------------------------------
    def add_user(self, user: UserConnected):
        card = UserCard(user)
        key = user.username + str(user.port)
        self.__users_references[key] = card
        self.users_list.controls.append(card)

        self.update()

    def remove_user(self, username, remote_port):
        try:
            card = self.__users_references.pop(username + str(remote_port))
            self.users_list.controls.remove(card)

            self.update()
        except KeyError:
            pass

    def remove_all_users(self):
        self.__users_references.clear()
        self.users_list.controls.clear()

        self.update()


# ------------------------------------------------------
# UI DE CADA USUARIO
# ------------------------------------------------------
class UserCard(ft.Container):

    def __init__(self, user: UserConnected):
        super().__init__()
        self.bgcolor = "#2b2b2b"
        self.padding = 16

        self.content = ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            user.username,
                            size=18,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Icon(
                            ft.Icons.CIRCLE,
                            size=14,
                            color=ft.Colors.GREEN_400
                        ),
                    ],
                ),
                ft.Text(f"IP: {user.ip}  •  Puerto: {user.port}",
                        size=13, color=ft.Colors.GREY_400),

                ft.Text(f"Conectado desde: {user.connected_at}",
                        size=12, color=ft.Colors.GREY_500),
            ]
        )

    def delete_user_card(self):
        self.visible = False
        self.content = None

        self.update()
