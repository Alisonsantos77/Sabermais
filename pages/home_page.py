import flet as ft


def HomePage(page: ft.Page):

    def navigate_to_questions(e):
        page.go("/questions")

    return ft.Container(
        padding=ft.padding.all(20),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Bem-vindo ao Saber+!",
                    size=28,
                    color=ft.colors.PRIMARY,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Image(
                    src="/images/mascote/acenando_frente.png",
                    fit=ft.ImageFit.CONTAIN,
                    height=300,
                    width=300,
                ),
                ft.Text(
                    value="Vamos começar?",
                    weight=ft.FontWeight.BOLD,
                    size=24,
                    color=ft.colors.PRIMARY,
                ),
                ft.IconButton(
                    icon=ft.icons.ARROW_FORWARD,
                    icon_color=ft.colors.PRIMARY,
                    tooltip="Ir para análise",
                    on_click=lambda _: page.go("/questions"),
                ),
            ],
            spacing=20,
        )
    )
