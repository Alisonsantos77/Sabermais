import flet as ft


def PageNotFound(page: ft.Page):
    return ft.Column(
        [
            ft.Text("404 - Página Não Encontrada", size=30,
                    weight=ft.FontWeight.BOLD, color="red"),
            ft.Text("A página que você está tentando acessar não existe."),
            ft.ElevatedButton(text="Voltar ao Início",
                              on_click=lambda _: page.go('/home'))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
