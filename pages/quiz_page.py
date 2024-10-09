import flet as ft
from components.answer import Answer
from components.question_render import renderizar_perguntas
from utils.score_calculator import calcular_perguntas


def QuizPage(page: ft.Page):
    answer_instances = []
    questions = page.session.get("questions")
    hints = page.session.get("hints")

    if not questions:
        page.go('/questions')
        page.snack_bar = ft.SnackBar(
            ft.Text("Por favor, selecione um vídeo e gere as perguntas primeiro.")
        )
        page.snack_bar.open = True
        return ft.Container()


    def reiniciar_quiz(e):
        for idx in range(1, len(questions) + 1):
            key = f"resposta_pergunta_{idx}"
            # Verifica se a chave existe usando o método get
            if page.session.get(key) is not None:
                page.session.remove(key)
        page.go("/questions")

    question_container = ft.Column()

    # Renderiza as perguntas com suporte para dicas
    renderizar_perguntas(questions, question_container,
                         answer_instances, page, hints=hints)

    calcular_button = ft.ElevatedButton(
        text="Calcular Pontuação",
        on_click=lambda e: calcular_perguntas(e, answer_instances, page),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_700,
            color=ft.colors.WHITE,
        )
    )

    restart_button = ft.ElevatedButton(
        text="Reiniciar Quiz",
        on_click=reiniciar_quiz,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.RED_700,
            color=ft.colors.WHITE,
        )
    )

    # Adiciona os botões ao question_container
    question_container.controls.append(
        ft.Row(
            controls=[calcular_button, restart_button],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Quiz", size=30, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=question_container,
                            col=10,
                        )]),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )
