import asyncio
from services.ia_service import gerar_perguntas
from services.extract_text_response import extract_questions_from_text
from utils.notifications import show_notification, icon_path
import flet as ft


async def processar_upload(page):
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    video_path = page.session.get("video_path")

    if not video_path:
        if page.platform == "WINDOWS":
            show_notification(page, "Erro", "Nenhum vídeo foi selecionado.", icon_path=icon_path
            )
        elif page.platform in ["ANDROID", "IOS"]:
            hf.light_impact()
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro ao processar upload{e}"),
                bgcolor=ft.colors.ON_SURFACE
            )
        page.snack_bar.open = True
        page.update()

    if page.platform == "WINDOWS":
        show_notification(
            page,
            "Processamento em Andamento",
            "A IA está analisando o vídeo, por favor aguarde...",
            icon_path=icon_path
        )
    elif page.platform in ["ANDROID", "IOS"]:
        hf.light_impact()
        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                "Processamento em Andamento, por favor aguarde..."),
            bgcolor=ft.colors.ON_SURFACE
        )
        page.snack_bar.open = True
        page.update()

    try:
        loop = asyncio.get_event_loop()
        perguntas_geradas = await loop.run_in_executor(None, gerar_perguntas, video_path)

        perguntas_extraidas = extract_questions_from_text(perguntas_geradas)
        if perguntas_extraidas:
            # Armazenar as perguntas, respostas, explicações e dicas
            page.session.set("questions", perguntas_extraidas)

            # Verificando se cada pergunta contém as chaves 'dica' e 'explicacao'
            page.session.set("explanations", [q.get(
                'explicacao') for q in perguntas_extraidas])
            page.session.set("hints", [q.get('dica') for q in perguntas_extraidas])

            # Notificação de sucesso
            if page.platform == "WINDOWS":
                show_notification(
                    page,
                    "Sucesso", "A análise do vídeo foi concluída, e as perguntas foram geradas com explicações e dicas!",
                    icon_path=icon_path
                )
            elif page.platform in ["ANDROID", "IOS"]:
                hf.light_impact()
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "A análise do vídeo foi concluída, e as perguntas foram geradas com explicações e dicas!"),
                    bgcolor=ft.colors.ON_SURFACE
                )
                page.snack_bar.open = True
                page.update()
            else:
                # Notificação de erro
                if page.platform == "WINDOWS":
                    show_notification(
                        page,
                        "Erro", "Não foi possível extrair perguntas e detalhes do vídeo.",
                        icon_path=icon_path
                    )
                elif page.platform in ["ANDROID", "IOS"]:
                    hf.light_impact()
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(
                            "Não foi possível extrair perguntas e detalhes do vídeo."),
                        bgcolor=ft.colors.ON_SURFACE
                    )
                    page.snack_bar.open = True
                    page.update()
    except Exception as e:
        if page.platform == "WINDOWS":
            show_notification(page, f"Erro inesperado: {e}", icon_path=icon_path)
        elif page.platform in ["ANDROID", "IOS"]:
            hf.heavy_impact()
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro inesperado: {e}"),
                bgcolor=ft.colors.ON_SURFACE
            )
            page.snack_bar.open = True
            page.update()
