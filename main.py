from loguru import logger
import flet as ft
from routes import setup_routes


def DarkVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#3A015C",
            on_primary="#FFFFFF",
            background="#11001C",
            surface="#4F0147",
            on_surface="#FFFFFF",
            secondary="#290025",
            on_secondary="#FFFFFF",
        )
    )


def RelaxVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#6C9A8B",
            on_primary="#FFFFFF",
            background="#FBF7F4",
            surface="#EED2CC",
            on_surface="#A1683A",
            secondary="#E8998D",
            on_secondary="#FFFFFF",
        )
    )


def toggle_theme(page: ft.Page, theme_mode):
    if theme_mode == ft.ThemeMode.DARK:
        page.theme = DarkVideoQTheme()
    else:
        page.theme = RelaxVideoQTheme()
    page.theme_mode = theme_mode
    # Armazena a preferência do tema na sessão
    page.session.set("theme_mode", theme_mode.value)
    logger.info(f"Tema alterado para: {theme_mode}")
    page.update()


logger.add("logs/app.log", format="{time} {level} {message}",
           level="INFO", rotation="1 MB", compression="zip")


def main(page: ft.Page):
    logger.info("Aplicação iniciada")

    # Carregar o tema da sessão, se houver
    theme_mode_value = page.session.get("theme_mode")
    if theme_mode_value:
        theme_mode = ft.ThemeMode(theme_mode_value)
        toggle_theme(page, theme_mode)
        logger.info(f"Tema carregado da sessão: {theme_mode}")
    else:
        page.theme_mode = ft.ThemeMode.SYSTEM
        logger.info(
            "Nenhuma preferência de tema na sessão, usando o padrão SYSTEM")

    page.title = "Painel Alison dev"

    # Função para eventos de teclado
    def on_key_event(e: ft.KeyboardEvent):
        logger.info(f"Evento de teclado: {e.key}")
        if e.key == "F1":
            page.go('/home')
        elif e.key == "F2":
            page.go('/questions')
        elif e.key == "F3":
            page.go('/about')
        elif e.key == "F4":
            page.go('/score')
        elif e.key == "F5":
            page.go('/quiz')
        elif e.key.lower() == "t":
            # Alternar entre os temas
            if page.theme_mode == ft.ThemeMode.DARK:
                new_theme_mode = ft.ThemeMode.LIGHT
            else:
                new_theme_mode = ft.ThemeMode.DARK
            toggle_theme(page, new_theme_mode)

    page.on_keyboard_event = on_key_event

    setup_routes(page)
    page.update()


if __name__ == "__main__":
    logger.info("Inicializando a aplicação")
    ft.app(target=main, assets_dir='assets')
