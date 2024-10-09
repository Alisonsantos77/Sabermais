import flet as ft
from loguru import logger
from pages.questions_page import QuestionPage
from pages.quiz_page import QuizPage
from pages.home_page import HomePage
from pages.about_page import AboutPage
from pages.score_page import ScorePage
from pages.page_404 import PageNotFound
from components.drawer import create_drawer


def setup_routes(page: ft.Page):
    logger.info("Configurando rotas")

    def route_change(route):
        logger.info(f"Rota alterada para: {route}")
        page.title = "Home - Saber+"
        page.views.clear()
        page.views.append(
            ft.View(
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                route='/home',
                controls=[HomePage(page)],
            )
        )
        if page.route == "/questions":
            page.title = "Questions - Saber+"
            page.views.append(
                ft.View(
                    route='/questions',
                    appbar=ft.AppBar(bgcolor=ft.colors.TRANSPARENT),
                    controls=[QuestionPage(page)],
                    scroll=ft.ScrollMode.AUTO,
                    drawer=create_drawer(page),
                )
            )
        elif page.route == "/quiz":
            page.title = "Quiz - Saber+"
            page.views.append(
                ft.View(
                    route='/quiz',
                    appbar=ft.AppBar(bgcolor=ft.colors.TRANSPARENT),
                    controls=[QuizPage(page)],
                    scroll=ft.ScrollMode.AUTO,
                    drawer=create_drawer(page),
                )
            )
        elif page.route == "/about":
            page.title = "About - Saber+"
            page.views.append(
                ft.View(
                    route='/about',
                    appbar=ft.AppBar(bgcolor=ft.colors.TRANSPARENT),
                    controls=[AboutPage(page)],
                    drawer=create_drawer(page),
                )
            )
        elif page.route == "/score":
            page.title = "Score - Saber+"
            page.views.append(
                ft.View(
                    route='/score',
                    appbar=ft.AppBar(title=ft.Text("Score")),
                    controls=[ScorePage(page)],
                    scroll=ft.ScrollMode.AUTO,
                    drawer=create_drawer(page),
                )
            )
        elif route == "/404":
            logger.warning(f"Rota desconhecida: {route}, redirecionando para 404")
            page.views.clear()
            page.views.append(
                ft.View(
                    route='/404',
                    appbar=ft.AppBar(title=ft.Text("Página Não Encontrada")),
                    controls=[PageNotFound(page)],
                    drawer=create_drawer(page),
                )
            )
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
        logger.info("Nenhuma rota especificada")
        page.go('/404')
    else:
        route_change(page.route)
