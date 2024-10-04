import flet as ft


def HomePage(page: ft.Page):
    return ft.Container(

        content=ft.Column(
            controls=[
                ft.Text(value="Home Page", size=16),
                ft.ElevatedButton(
                    text="Ir para a página de perguntas", on_click=lambda e: page.go("/questions"))
            ]
        )
    )
