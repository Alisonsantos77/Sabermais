import flet as ft


def DarkVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#10002B",  # Cor principal escura
            on_primary="#E0AAFF",  # Texto sobre a cor primária
            background="#240046",  # Cor de fundo
            surface="#5A189A",  # Cor de superfícies
            on_surface="#C77DFF",  # Texto sobre superfícies
            secondary="#7B2CBF",  # Cor secundária
            on_secondary="#9D4EDD",  # Texto sobre a cor secundária
            on_background="#E0AAFF",  # Texto sobre fundo
        )
    )


def RelaxVideoQTheme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#A48971",  # Cor principal suave
            on_primary="#F5D7BD",  # Texto sobre a cor primária
            background="#8D6B48",  # Cor de fundo
            surface="#BE986D",  # Cor de superfícies
            on_surface="#F5D7BD",  # Texto sobre superfícies
            secondary="#D2A87D",  # Cor secundária
            on_secondary="#F5D7BD",  # Texto sobre a cor secundária
            on_background="#F5D7BD",  # Texto sobre fundo
        )
    )
