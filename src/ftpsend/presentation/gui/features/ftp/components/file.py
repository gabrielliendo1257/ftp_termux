import flet as ft


class FolderPickerCard(ft.Container):
    def __init__(self, on_folder_selected=None, main_title: str = None):
        super().__init__()
        self.text = main_title or "Titulo por defecto."

        self.on_folder_selected = on_folder_selected
        self.bgcolor = "#1f1f1f"
        self.padding = 20
        self.border_radius = 12
        self.border = ft.border.all(1, "#333333")

        self.__file_picker = ft.FilePicker(
            on_result=self._folder_selected
        )

        self.selected_path = ft.Text(
            "Ninguna carpeta seleccionada",
            size=13,
            color=ft.Colors.GREY_400
        )

        self.content = ft.Column(
            spacing=15,
            controls=[
                ft.Text(
                    self.text,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),

                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Icon(ft.Icons.FOLDER_ROUNDED, color=ft.Colors.BLUE_300),
                        self.selected_path,
                    ],
                ),

                ft.FilledButton(
                    "Elegir carpeta",
                    icon=ft.Icons.FOLDER_OPEN,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor="#2b7bff",
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=self.pick_folder,
                ),
                self.__file_picker,
            ]
        )

    # ---------------------------------------------
    # Evento de selección de carpeta
    # ---------------------------------------------
    def pick_folder(self, e):
        self.__file_picker.get_directory_path()

    # ---------------------------------------------
    # Resultado del FilePicker
    # ---------------------------------------------
    def _folder_selected(self, e: ft.FilePickerResultEvent):
        if e.path:
            self.selected_path.value = e.path
            self.selected_path.color = ft.Colors.WHITE
            self.update()

            if self.on_folder_selected:
                self.on_folder_selected(e.path)
        else:
            self.selected_path.value = "Ninguna carpeta seleccionada"
            self.selected_path.color = ft.Colors.GREY_400
            self.update()
