import flet as ft
from components.answer import Answer
from utils.score_calculator import calcular_perguntas


def renderizar_perguntas(perguntas, question_container, answer_instances, page, hints):
    question_container.controls.clear()
    answer_instances.clear()

    for idx, pergunta_obj in enumerate(perguntas, start=1):
        pergunta_texto = pergunta_obj['pergunta']
        opcoes_resposta = pergunta_obj['opcoes']
        letras_opcoes = pergunta_obj['letras_opcoes']
        resposta_correta_letra = pergunta_obj['resposta_letra']

        hint = hints[idx -
                     1] if hints and len(hints) >= idx else "Nenhuma dica disponível."

        question_container.controls.append(
            ft.Text(f"{idx}. {pergunta_texto}",
                    size=20, weight=ft.FontWeight.BOLD)
        )

        answer_group = Answer(
            page=page,
            pergunta_numero=idx,
            opcoes=opcoes_resposta,
            letras_opcoes=letras_opcoes,
            resposta_letra=resposta_correta_letra
        )

        question_container.controls.append(answer_group)
        answer_instances.append(answer_group)

        question_container.controls.append(
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.LIGHTBULB_OUTLINE,
                        tooltip="Ver Dica",
                        on_click=lambda e, hint_text=hint: mostrar_dica(
                            page, hint_text)
                    )
                ]
            )
        )


def mostrar_dica(page, hint_text):
    # Exibir "Nenhuma dica disponível" se a dica estiver faltando
    hint_display = hint_text if hint_text else "Nenhuma dica disponível."
    page.snack_bar = ft.SnackBar(
        content=ft.Text(f"Dica: {hint_display}"),
        bgcolor=ft.colors.AMBER_400
    )
    page.snack_bar.open = True
    page.update()
