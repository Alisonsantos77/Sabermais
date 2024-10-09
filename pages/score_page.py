import flet as ft


def ScorePage(page: ft.Page):
    score_data = page.session.get("score")
    questions = page.session.get("questions")
    explanations = page.session.get("explanations")

    if not score_data or not questions:
        page.go('/quiz')
        page.snack_bar = ft.SnackBar(
            ft.Text("Por favor, responda as perguntas antes de ver sua pontuação."),
            bgcolor=ft.colors.ERROR
        )
        page.snack_bar.open = True
        return ft.Container()

    total_questions = score_data["total_perguntas"] if "total_perguntas" in score_data else len(questions)
    respostas_corretas = score_data["respostas_corretas"] if "respostas_corretas" in score_data else 0

    detailed_results = []
    for idx, pergunta_obj in enumerate(questions, start=1):
        pergunta_texto = pergunta_obj['pergunta']
        resposta_correta = pergunta_obj['resposta_letra'].strip().lower()
        user_answer = page.session.get(f"resposta_pergunta_{idx}")

        if user_answer is None:
            user_answer = "Não respondida"
        else:
            user_answer = user_answer.strip().lower()

        explanation = explanations[idx - 1] if explanations and len(explanations) >= idx else "Nenhuma explicação disponível."

        if user_answer == resposta_correta:
            resultado = "✅ Correta"
            resultado_cor = ft.colors.ON_SECONDARY
        elif user_answer == "não respondida":
            resultado = "⚠️ Não Respondida"
            resultado_cor = ft.colors.SECONDARY
        else:
            resultado = "❌ Incorreta"
            resultado_cor = ft.colors.ERROR

        detailed_results.append(
            ft.Column(
                controls=[
                    ft.Text(f"{idx}. {pergunta_texto}", size=16,weight=ft.FontWeight.BOLD, color=ft.colors.ON_SECONDARY),
                    ft.Text(f"Sua resposta: {user_answer.upper()}", color=ft.colors.ON_SECONDARY),
                    ft.Text(f"Resultado: {resultado}", color=resultado_cor),
                    ft.Text(f"Explicação: {explanation}", color=ft.colors.ON_SECONDARY),
                    ft.Divider(),
                ]
            )
        )

    score_text = ft.Text(
        f"Você acertou {respostas_corretas} de {total_questions} perguntas!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.PRIMARY
    )

    # Exibir Histórico de Pontuações
    historico_pontuacoes = page.session.get("historico_pontuacoes")
    if historico_pontuacoes is None:
        historico_pontuacoes = []

    historico_detailed_results = [
        ft.ListTile(
            title=ft.Text(f"Tentativa {idx + 1}: {item['respostas_corretas']} de { item['total_perguntas']} perguntas corretas."),
            subtitle=ft.Text(f"Feedback: {item['feedback']}")
        ) for idx, item in enumerate(historico_pontuacoes)
    ]

    historico_section = ft.Column(
        controls=[
            ft.Text("Histórico de Pontuações", size=20,
                    weight=ft.FontWeight.BOLD, color=ft.colors.ON_SECONDARY),
            ft.ListView(
                controls=historico_detailed_results,
                padding=ft.padding.all(10),
            ),
            ft.Divider(),
        ]
    ) if historico_pontuacoes else ft.Container()

    def reiniciar_quiz(e):
        for id_question in range(1, total_questions + 1):
            page.session.remove(f"resposta_pergunta_{id_question}")
        page.session.remove("questions")
        page.session.remove("score")
        page.go('/questions')


    restart_button = ft.ElevatedButton(
        text="Reiniciar Quiz",
        on_click=reiniciar_quiz,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.SECONDARY,
            color=ft.colors.ON_SECONDARY,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    pdf_export_button = ft.ElevatedButton(
        text="Exportar PDF",
        icon=ft.icons.FILE_DOWNLOAD,
        on_click=lambda _: print("Pdf export clicado"),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.PRIMARY,
            color=ft.colors.ON_PRIMARY,
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
                historico_section,
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
