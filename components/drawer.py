import flet as ft


def create_drawer(page: ft.Page):
    theme = page.client_storage.get("theme_mode")
    return ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text("Saber+", size=30, weight=ft.FontWeight.BOLD,
                                color=ft.colors.PRIMARY),
                        ft.Image(
                            src="icon_windows.png",
                            width=100,
                            height=100,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    ],
                ),
                padding=ft.padding.all(10),
            ),
            ft.Divider(height=1),
            ft.NavigationDrawerDestination(
                label="Questions",
                icon=ft.icons.QUESTION_ANSWER_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.QUESTION_ANSWER),
            ),
            ft.NavigationDrawerDestination(
                label="Quiz",
                icon=ft.icons.LIST_ALT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.LIST_ALT),
            ),
            ft.NavigationDrawerDestination(
                label="About",
                icon=ft.icons.INFO_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.INFO),
            ),
            ft.NavigationDrawerDestination(
                label="Score",
                icon=ft.icons.SCOREBOARD_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SCOREBOARD),
            ),
            ft.Divider(height=1),
            ft.NavigationDrawerDestination(
                label=f"Theme {theme}",
                icon=ft.icons.WB_SUNNY_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.WB_SUNNY),
            ),
        ],
        on_change=lambda e: handle_drawer_change(e, page)
    )


def handle_drawer_change(e, page):
    selected_index = e.control.selected_index
    if selected_index == 0:
        page.go('/questions')
    elif selected_index == 1:
        page.go('/quiz')
    elif selected_index == 2:
        page.go('/about')
    elif selected_index == 3:
        page.go('/score')
