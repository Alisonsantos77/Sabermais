from loguru import logger
import flet as ft
from routes import setup_routes
from utils.theme_utils import DarkVideoQTheme, RelaxVideoQTheme
from utils.notifications import show_notification, icon_path


def toggle_theme(page: ft.Page, theme_mode: ft.ThemeMode):
    if theme_mode == ft.ThemeMode.DARK:
        page.theme = DarkVideoQTheme()
        logger.info("Tema: Dark")
    else:
        page.theme = RelaxVideoQTheme()
        logger.info("Tema: Light")
    page.theme_mode = theme_mode
    page.client_storage.set("theme_mode", theme_mode.name)
    page.update()


logger.add("logs/app.log", format="{time} {level} {message}",
           level="INFO", rotation="1 MB", compression="zip")


def main(page: ft.Page):
    logger.info("saber+ iniciado")
    show_notification(page, "Título da Notificação", "Mensagem da notificação", icon_path)

    theme_mode_value = page.client_storage.get("theme_mode")
    if theme_mode_value:
        try:
            theme_mode = ft.ThemeMode[theme_mode_value]
            toggle_theme(page, theme_mode)
        except KeyError:
            toggle_theme(page, ft.ThemeMode.LIGHT)
    else:
        toggle_theme(page, ft.ThemeMode.LIGHT)

    page.title = "saber+"

    def alternar_tema(e):
        current_theme = page.client_storage.get("theme_mode") or "LIGHT"
        new_theme_mode = ft.ThemeMode.LIGHT if current_theme == "DARK" else ft.ThemeMode.DARK
        toggle_theme(page, new_theme_mode)

    shd = ft.ShakeDetector(
        minimum_shake_count=2,
        shake_slop_time_ms=300,
        shake_count_reset_time_ms=1000,
        on_shake=lambda _: print("SHAKE DETECTED!"),
    )
    page.overlay.append(shd)

    def on_key_event(e: ft.KeyboardEvent):
        logger.info(f"Tecla: {e.key}")
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
        elif e.key.lower() == "t" or shd:
            alternar_tema(None)

    page.on_keyboard_event = on_key_event

    setup_routes(page)
    page.update()


if __name__ == "__main__":
    logger.info("Inicializando saber+")
    ft.app(target=main, assets_dir='assets')
