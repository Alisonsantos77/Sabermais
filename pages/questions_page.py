import flet as ft
import asyncio
from components.file_picker_handler import on_file_picker_result
from services.upload_processor import processar_upload
from utils.notifications import show_notification_plyer


def QuestionPage(page: ft.Page):
    wallpaper_container = ft.Ref[ft.Container]()
    select_file_button = ft.Ref[ft.ElevatedButton]()
    submit_button = ft.Ref[ft.ElevatedButton]()

    selected_file = ft.Text(
        value="Nenhum arquivo selecionado",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    # Configuração do FilePicker
    file_picker = ft.FilePicker(on_result=lambda e: on_file_picker_result(
        e, page, wallpaper_container, selected_file))
    page.overlay.append(file_picker)

    select_file_button_control = ft.ElevatedButton(
        ref=select_file_button,
        text="Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["mp4"]),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.BLACK,
                ft.ControlState.HOVERED: ft.colors.WHITE,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    async def on_confirm_upload(e):
        await processar_upload(page)
        page.go('/quiz')

    submit_button_control = ft.ElevatedButton(
        ref=submit_button,
        text="Executar",
        on_click=on_confirm_upload,
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.BLACK,
                ft.ControlState.HOVERED: ft.colors.WHITE,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Estude o seu conhecimento com o Quiz!",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Divider(),
                ft.Container(
                    ref=wallpaper_container,
                    image=ft.Image(
                        src='https://images8.alphacoders.com/136/1363709.png',
                        fit=ft.ImageFit.COVER
                    ),
                    height=300,
                    expand=True,
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    controls=[
                        select_file_button_control,
                        submit_button_control,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                selected_file,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
