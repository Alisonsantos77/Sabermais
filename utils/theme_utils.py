import flet as ft


def DarkVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#ff0054",  # Cor principal vibrante
            # Texto sobre a cor primária (branco para contraste)
            on_primary="#fefeff",
            background="#01002a",  # Cor de fundo escura
            surface="#031867",  # Cor de superfícies (azul profundo)
            # Texto sobre superfícies (branco para contraste)
            on_surface="#fefeff",
            secondary="#031867",  # Cor secundária (azul intenso)
            on_secondary="#fefeff",  # Texto sobre a cor secundária
            on_background="#fefeff",  # Texto sobre fundo escuro
        )
    )


def RelaxVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#031867",  # Cor principal suave (azul profundo)
            on_primary="#fefeff",  # Texto sobre a cor primária (branco)
            background="#ff0054",  # Cor de fundo vibrante
            surface="#01002a",  # Cor de superfícies (preto azulado)
            on_surface="#fefeff",  # Texto sobre superfícies (branco)
            secondary="#fefeff",  # Cor secundária (branco para contraste)
            on_secondary="#031867",  # Texto sobre a cor secundária
            on_background="#fefeff",  # Texto sobre fundo
        )
    )
