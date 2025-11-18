import flet as ft

from ftpsend.presentation.gui.features.ftp.pages.home import HomePage

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    page.add(HomePage())

def run():
    ft.app(target=main)
