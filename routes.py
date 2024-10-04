import flet as ft
from loguru import logger
from pages.questions_page import QuestionPage
from pages.home_page import HomePage
from pages.about_page import AboutPage
from pages.score_page import ScorePage

def setup_routes(page: ft.Page):
    logger.info("Configurando rotas")

    def change_route(e):
        selected_index = e.control.selected_index
        logger.info(f"Alterando rota com base no índice selecionado: {selected_index}")
        if selected_index == 0:
            page.go('/home')
        elif selected_index == 1:
            page.go('/questions')
        elif selected_index == 2:
            page.go('/about')
        elif selected_index == 3:
            page.go('/score')  # Adicionando rota para a página de pontuação

    # NavigationDrawer
    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Text("Menu Principal", size=24, weight=ft.FontWeight.BOLD),
                padding=ft.padding.all(10),
            ),
            ft.Divider(height=1),
            ft.NavigationDrawerDestination(
                label="Home",
                icon=ft.icons.HOME_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.HOME),
            ),
            ft.NavigationDrawerDestination(
                label="Questions",
                icon=ft.icons.QUESTION_ANSWER_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.QUESTION_ANSWER),
            ),
            ft.NavigationDrawerDestination(
                label="About",
                icon=ft.icons.INFO_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.INFO),
            ),
            ft.NavigationDrawerDestination(  # Adicionando a opção de Score no menu
                label="Score",
                icon=ft.icons.SCOREBOARD_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SCOREBOARD),
            ),
        ],
        on_change=change_route
    )

    page.drawer = drawer

    def route_change(route):
        logger.info(f"Rota alterada para: {route}")
        if page.route == "/home":
            page.title = "Home - Painel Alison dev"
            if not page.views or page.views[-1].route != '/home':
                page.views.clear()
                page.views.append(
                    ft.View(
                        route='/home',
                        appbar=ft.AppBar(title=ft.Text("Home")),
                        controls=[HomePage(page)],
                        drawer=drawer,
                    )
                )
        elif page.route == "/questions":
            page.title = "Questions - Painel Alison dev"
            if not page.views or page.views[-1].route != '/questions':
                page.views.clear()
                page.views.append(
                    ft.View(
                        route='/questions',
                        appbar=ft.AppBar(title=ft.Text("Questions")),
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[QuestionPage(page)],
                        drawer=drawer,
                    )
                )
        elif page.route == "/about":
            page.title = "About - Painel Alison dev"
            if not page.views or page.views[-1].route != '/about':
                page.views.clear()
                page.views.append(
                    ft.View(
                        route='/about',
                        scroll=ft.ScrollMode.AUTO,
                        appbar=ft.AppBar(title=ft.Text("About")),
                        controls=[AboutPage(page)],
                        drawer=drawer,
                    )
                )
        elif page.route == "/score":
            page.title = "Score - Painel Alison dev"  # Título para a página de pontuação
            if not page.views or page.views[-1].route != '/score':
                page.views.clear()
                page.views.append(
                    ft.View(
                        route='/score',
                        scroll=ft.ScrollMode.AUTO,
                        appbar=ft.AppBar(title=ft.Text("Score")),
                        controls=[ScorePage(page)],  # Chamando a página de pontuação
                        drawer=drawer,
                    )
                )
        else:
            logger.warning(f"Rota desconhecida: {route}, redirecionando para /home")
            page.go('/home')
            return
        page.update()

    def view_pop(view):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            logger.info(f"Retornando para a rota anterior: {top_view.route}")
            page.go(top_view.route)
        else:
            logger.info("Sem mais views no histórico, retornando à home.")
            page.go('/home')

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    if not page.route:
        logger.info("Nenhuma rota especificada, redirecionando para /home")
        page.go('/home')
    else:
        route_change(page.route)
