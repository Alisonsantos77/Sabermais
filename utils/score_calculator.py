from utils.notifications import show_notification_plyer


def calcular_perguntas(e, answer_instances, page):
    total_perguntas = len(answer_instances)
    respostas_corretas = sum(
        1 for answer in answer_instances if
        answer.selected_answer and answer.selected_answer.strip(
        ).lower() == answer.resposta_correta.strip().lower()
    )

    if respostas_corretas == total_perguntas:
        feedback = "🎉 Parabéns, você acertou todas!"
    elif respostas_corretas > total_perguntas / 2:
        feedback = f"👏 Bom trabalho! Você acertou {
            respostas_corretas} de {total_perguntas}."
    else:
        feedback = f"⚠️ Você acertou {respostas_corretas} de {
            total_perguntas}. Continue praticando!"


    feedback = feedback if feedback else "Resultado não disponível."
    show_notification_plyer("Resultado do Quiz", feedback)

    # Salvar a pontuação na sessão
    score_data = {
        "total_perguntas": total_perguntas,
        "respostas_corretas": respostas_corretas,
        "feedback": feedback
    }

    # Recuperar o histórico de pontuações anterior
    historico_pontuacoes = page.session.get("historico_pontuacoes")
    if historico_pontuacoes is None:
        historico_pontuacoes = []

    # Adicionar a nova pontuação ao histórico
    historico_pontuacoes.append(score_data)

    # Atualizar o histórico na sessão
    page.session.set("historico_pontuacoes", historico_pontuacoes)

    # Salvar a pontuação atual
    page.session.set("score", score_data)

    # Redirecionar para a página de resultados e exibir explicações
    page.go('/score')

    # Exibir explicações detalhadas sobre cada pergunta
    explanations = page.session.get("explanations")
    if explanations:
        for idx, explanation in enumerate(explanations, start=1):
            show_notification_plyer(
                f"Explicação da Pergunta {idx}", explanation)
