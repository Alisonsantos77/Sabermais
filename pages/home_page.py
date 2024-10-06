import flet as ft


def HomePage(page: ft.Page):

    def navigate_to_questions(e):
        # Animação de loading pode ser adicionada aqui se necessário
        page.go("/questions")

    return ft.Container(
        padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                ft.Text(
                    value="Bem-vindo ao VideoQ!",
                    size=28,
                    color=ft.colors.ON_SURFACE,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    value="Acesse suas perguntas geradas automaticamente para estudo.",
                    size=16,
                    color=ft.colors.ON_SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    text="Ir para perguntas",
                    icon=ft.icons.QUESTION_ANSWER,
                    on_click=navigate_to_questions,
                    bgcolor=ft.colors.PRIMARY,
                    color=ft.colors.ON_PRIMARY,  
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        elevation=3, 
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,  # Espaço entre elementos
        )
    )
