import flet as ft
from components.answer import Answer
from utils.score_calculator import calcular_perguntas


def renderizar_perguntas(perguntas, question_container, answer_instances, page):
    question_container.controls.clear()
    answer_instances.clear()

    for idx, pergunta_obj in enumerate(perguntas, start=1):
        pergunta_texto = pergunta_obj['pergunta']
        opcoes_resposta = pergunta_obj['opcoes']
        letras_opcoes = pergunta_obj['letras_opcoes']
        resposta_correta_letra = pergunta_obj['resposta_letra']

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
