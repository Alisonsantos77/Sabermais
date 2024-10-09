import flet as ft


def AboutPage(page: ft.Page):
    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Sobre",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.PRIMARY
                ),
                ft.Text(
                    "Este aplicativo foi pensado para você que está estudando para o vestibular e quer otimizar seu tempo. "
                    "Você só precisa enviar a videoaula, e nossa IA faz o trabalho pesado, criando um questionário no "
                    "estilo vestibular com base no que foi apresentado. Fácil, prático e eficiente!",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                    color=ft.colors.ON_SECONDARY
                ),
                ft.Text(
                    "Desenvolvido por: Alison Santos",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.PRIMARY
                ),
                ft.Text(
                    "Sou Alison, programador especializado em backend (mas não me perco no frontend). Trabalho como "
                    "freelancer e gosto de criar soluções que realmente façam a diferença. Com experiência em Django, Python e "
                    "agora focado em Flet, estou sempre buscando maneiras de agregar valor ao dia a dia das pessoas.",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                    color=ft.colors.ON_SECONDARY
                ),
                ft.Text(
                    "Se quiser bater um papo ou conhecer mais sobre meu trabalho, é só usar os links abaixo. Vamos "
                    "trocar uma ideia!",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                    color=ft.colors.ON_SECONDARY
                ),
                ft.Text(
                    "Contatos:",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.PRIMARY
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            content=ft.Image(
                                src='images/contact/icons8-whatsapp-48.png',
                                width=40,
                                height=40
                            ),
                            icon_color=ft.colors.PRIMARY,
                            tooltip="Abrir WhatsApp",
                            url="https://wa.link/oebrg2",
                            style=ft.ButtonStyle(
                                overlay_color={
                                    "": ft.colors.TRANSPARENT,
                                    "hovered": ft.colors.GREEN
                                },
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src='images/contact/outlook-logo.png',
                                width=40,
                                height=40
                            ),
                            icon_color=ft.colors.PRIMARY,
                            tooltip="Enviar Email",
                            url="mailto:Alisondev77@hotmail.com?subject=Feedback%20-%20MultiTools&body=Olá, gostaria de fornecer feedback.",
                            style=ft.ButtonStyle(
                                overlay_color={
                                    "": ft.colors.TRANSPARENT,
                                    "hovered": ft.colors.BLUE
                                },
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src='images/contact/icons8-linkedin-48.png',
                                width=40,
                                height=40
                            ),
                            tooltip="Acessar LinkedIn",
                            url="https://www.linkedin.com/in/alisonsantosdev",
                            style=ft.ButtonStyle(
                                overlay_color={
                                    "": ft.colors.TRANSPARENT,
                                    "hovered": ft.colors.BLUE
                                },
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src='images/contact/icons8-github-64.png',
                                width=40,
                                height=40
                            ),
                            icon_color=ft.colors.PRIMARY,
                            tooltip="Acessar GitHub",
                            url="https://github.com/Alisonsantos77",
                            style=ft.ButtonStyle(
                                overlay_color={
                                    "": ft.colors.TRANSPARENT,
                                    "hovered": ft.colors.GREY
                                },
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            spacing=20,
        ),
    )
