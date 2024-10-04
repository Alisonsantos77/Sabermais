import flet as ft
from services.pdf_export import export_score_pdf


def ScorePage(page: ft.Page):
    score_data = page.session.get("score")
    questions = page.session.get("questions")

    if not score_data or not questions:
        page.go('/quiz')
        page.snack_bar = ft.SnackBar(
            ft.Text("Por favor, responda as perguntas antes de ver sua pontuação."))
        page.snack_bar.open = True
        return ft.Container()

    total_questions = score_data.get("total_perguntas", len(questions))
    respostas_corretas = score_data.get("respostas_corretas", 0)

    detailed_results = []
    for idx, pergunta_obj in enumerate(questions, start=1):
        pergunta_texto = pergunta_obj['pergunta']
        resposta_correta = pergunta_obj['resposta_letra'].strip().lower()
        user_answer = page.session.get(f"resposta_pergunta_{idx}")
        if user_answer is None:
            user_answer = "Não respondida"
        else:
            user_answer = user_answer.strip().lower()

        if user_answer == resposta_correta:
            resultado = "✅ Correta"
            resultado_cor = ft.colors.GREEN
        elif user_answer == "não respondida":
            resultado = "⚠️ Não Respondida"
            resultado_cor = ft.colors.YELLOW
        else:
            resultado = "❌ Incorreta"
            resultado_cor = ft.colors.RED

        detailed_results.append(
            ft.Column(
                controls=[
                    ft.Text(f"{idx}. {pergunta_texto}",
                            size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Sua resposta: {
                            user_answer.upper()}", color=ft.colors.BLUE),
                    ft.Text(f"Resultado: {resultado}", color=resultado_cor),
                    ft.Divider(),
                ]
            )
        )

    score_text = ft.Text(
        f"Você acertou {respostas_corretas} de {total_questions} perguntas!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE
    )

    def reiniciar_quiz(e):
        for id_question in range(1, total_questions + 1):
            page.session.remove(f"resposta_pergunta_{id_question}")
        page.session.remove("questions")
        page.session.remove("score")
        page.go('/questions')

    def exportar_pdf(e):
        export_score_pdf(score_data, questions, "resultado_quiz.pdf")
        page.snack_bar = ft.SnackBar(
            ft.Text("Resultados exportados como PDF com sucesso!"))
        page.snack_bar.open = True
        page.update()

    restart_button = ft.ElevatedButton(
        text="Reiniciar Quiz",
        on_click=reiniciar_quiz,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_700,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    pdf_export_button = ft.ElevatedButton(
        text="Exportar PDF",
        icon=ft.icons.FILE_DOWNLOAD,
        on_click=exportar_pdf,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                score_text,
                ft.Divider(),
                ft.Column(
                    controls=detailed_results,
                    scroll=ft.ScrollMode.AUTO,
                ),
                ft.Row(
                    controls=[restart_button, pdf_export_button],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
