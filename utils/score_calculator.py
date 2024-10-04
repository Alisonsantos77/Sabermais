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

    show_notification_plyer("Resultado do Quiz", feedback)
    page.session.set("score", {
                     "total_perguntas": total_perguntas, "respostas_corretas": respostas_corretas})
    page.go('/score')
