from loguru import logger
import flet as ft
from routes import setup_routes

logger.add("app.log", format="{time} {level} {message}",
           level="INFO", rotation="1 MB", compression="zip")


def main(page: ft.Page):
    logger.info("Aplicação iniciada")

    theme_mode = page.session.get("theme_mode")
    if theme_mode:
        page.theme_mode = theme_mode
        logger.info(f"Tema carregado da sessão: {theme_mode}")
    else:
        page.theme_mode = ft.ThemeMode.SYSTEM
        logger.info("Nenhuma preferência de tema na sessão, usando o padrão SYSTEM")

    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE)
    page.title = "Painel Alison dev"

    def on_key_event(e: ft.KeyboardEvent):
        logger.info(f"Evento de teclado: {e.key}")
        if e.key == "F1":
            page.go('/home')
        elif e.key == "F2":
            page.go('/questions')
        elif e.key == "F3":
            page.go('/about')
        elif e.key.lower() == "t":
            if page.theme_mode == ft.ThemeMode.LIGHT:
                page.theme_mode = ft.ThemeMode.DARK
            else:
                page.theme_mode = ft.ThemeMode.LIGHT
            # Armazena a preferência do usuário na sessão
            page.session.set("theme_mode", page.theme_mode)
            logger.info(f"Tema alterado para: {page.theme_mode}")
            page.update()

    page.on_keyboard_event = on_key_event

    setup_routes(page)
    page.update()


if __name__ == "__main__":
    logger.info("Inicializando a aplicação")
    ft.app(target=main, assets_dir='assets')
