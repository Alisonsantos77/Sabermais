import flet as ft


def AboutPage(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Sobre", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Este aplicativo foi pensado para você que está estudando para o vestibular e quer otimizar seu tempo. "
                    "Você só precisa enviar a videoaula, e nossa IA faz o trabalho pesado, criando um questionário no "
                    "estilo vestibular"
                    "com base no que foi apresentado. Fácil, prático e eficiente!",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
                ft.Text("Desenvolvido por: Alison Santos", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Sou Alison, programador especializado em backend (mas não me perco no frontend). Trabalho como "
                    "freelancer"
                    "e gosto de criar soluções que realmente façam a diferença. Com experiência em Django, Python e "
                    "agora focado"
                    "em Flet, estou sempre buscando maneiras de agregar valor ao dia a dia das pessoas.",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
                ft.Text(
                    "Se quiser bater um papo ou conhecer mais sobre meu trabalho, é só usar os links abaixo. Vamos "
                    "trocar uma ideia!",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
                ft.Text("Contatos:", size=18, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            content=ft.Image(src='images/whatsapp-logo.png', width=40, height=40),
                            icon_color=ft.colors.GREEN,
                            tooltip="Abrir WhatsApp",
                            url="https://wa.link/oebrg2",
                            style=ft.ButtonStyle(
                                overlay_color={"": ft.colors.TRANSPARENT, "hovered": ft.colors.LIGHT_GREEN_200},
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(src='images/microsoft-outlook-logo.png', width=40, height=40),
                            icon_color=ft.colors.BLUE,
                            tooltip="Enviar Email",
                            url="mailto:Alisondev77@hotmail.com?subject=Feedback%20-%20MultiTools&body=Ol%C3%A1,"
                                "%20gostaria%20de%20fornecer%20feedback.",
                            style=ft.ButtonStyle(
                                overlay_color={"": ft.colors.TRANSPARENT, "hovered": ft.colors.LIGHT_BLUE_200},
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(src='images/linkedin-logo.png', width=40, height=40),
                            icon_color=ft.colors.BLUE,
                            tooltip="Acessar LinkedIn",
                            url="https://www.linkedin.com/in/alisonsantosdev",
                            style=ft.ButtonStyle(
                                overlay_color={"": ft.colors.TRANSPARENT, "hovered": ft.colors.LIGHT_BLUE_200},
                            ),
                        ),
                        ft.IconButton(
                            content=ft.Image(src='images/github-logo.png', width=40, height=40),
                            icon_color=ft.colors.GREY,
                            tooltip="Acessar GitHub",
                            url="https://github.com/Alisonsantos77",
                            style=ft.ButtonStyle(
                                overlay_color={"": ft.colors.TRANSPARENT, "hovered": ft.colors.GREY_300},
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            spacing=20,
        ),
        padding=20,
    )
