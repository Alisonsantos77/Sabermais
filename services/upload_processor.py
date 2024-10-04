import asyncio
from services.ia_service import gerar_perguntas
from services.extract_text_response import extract_questions_from_text
from utils.notifications import show_notification_plyer


async def processar_upload(page):
    video_path = page.session.get("video_path")
    if not video_path:
        show_notification_plyer("Erro", "Nenhum vídeo foi selecionado.")
        return

    show_notification_plyer("Processamento em Andamento",
                            "A IA está analisando o vídeo, por favor aguarde...")

    try:
        loop = asyncio.get_event_loop()
        perguntas_geradas = await loop.run_in_executor(None, gerar_perguntas, video_path)

        perguntas_extraidas = extract_questions_from_text(perguntas_geradas)
        if perguntas_extraidas:
            page.session.set("questions", perguntas_extraidas)
            show_notification_plyer(
                "Sucesso", "A análise do vídeo foi concluída e as perguntas foram geradas!")
        else:
            show_notification_plyer(
                "Erro", "Não foi possível extrair perguntas do vídeo.")

    except Exception as e:
        show_notification_plyer("Erro no Processamento",
                                f"Erro inesperado: {e}")
