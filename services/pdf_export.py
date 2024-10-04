from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor


def export_score_pdf(score_data, questions, file_name="resultado_quiz.pdf"):
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_style.fontSize = 22
    title_style.alignment = TA_CENTER

    subtitle_style = styles["Heading2"]
    subtitle_style.fontSize = 18
    subtitle_style.alignment = TA_CENTER

    body_style = styles["BodyText"]
    body_style.fontSize = 12
    body_style.alignment = TA_JUSTIFY

    highlighted_style = ParagraphStyle(
        "Highlighted", parent=body_style, textColor=HexColor("#0077CC"), fontSize=12
    )

    pdf = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    elements.append(Paragraph("Resultado do Quiz", title_style))
    elements.append(Spacer(1, 12))

    total_questions = score_data.get("total_perguntas", len(questions))
    respostas_corretas = score_data.get("respostas_corretas", 0)
    score_text = f"Você acertou {respostas_corretas} de {total_questions} perguntas!"
    elements.append(Paragraph(score_text, subtitle_style))
    elements.append(Spacer(1, 12))

    progress_percentage = (respostas_corretas / total_questions) * 100
    progress_bar_text = f"Desempenho: {progress_percentage:.2f}%"
    elements.append(Paragraph(progress_bar_text, highlighted_style))
    elements.append(Spacer(1, 12))

    table_data = [["Pergunta", "Sua Resposta", "Resultado"]]
    for idx, pergunta_obj in enumerate(questions, start=1):
        pergunta_texto = pergunta_obj['pergunta']
        resposta_correta = pergunta_obj['resposta_letra'].strip().lower()
        user_answer = score_data.get(f"resposta_pergunta_{idx}", "Não respondida").strip().lower()

        if user_answer == resposta_correta:
            resultado = "✅ Correta"
        elif user_answer == "não respondida":
            resultado = "⚠️ Não Respondida"
        else:
            resultado = "❌ Incorreta"

        table_data.append([pergunta_texto, user_answer.upper(), resultado])

    table = Table(table_data, colWidths=[3 * inch, 1.5 * inch, 1.5 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#CCCCCC")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    about_text = (
        "Este aplicativo foi pensado para você que está estudando para o vestibular e quer otimizar seu tempo."
        "Você só precisa enviar a videoaula, e nossa IA faz o trabalho pesado, criando um questionário no estilo "
        "vestibular."
    )
    elements.append(Paragraph(about_text, body_style))
    elements.append(Spacer(1, 12))

    developer_text = (
        "Desenvolvido por: Alison Santos\n"
        "Sou Alison, programador especializado em backend (mas não me perco no frontend). "
        "Trabalho como freelancer e gosto de criar soluções que realmente façam a diferença."
    )
    elements.append(Paragraph(developer_text, body_style))

    pdf.build(elements)
