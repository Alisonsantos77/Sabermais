import flet as ft
import asyncio
from components.file_picker_handler import on_file_picker_result
from services.upload_processor import processar_upload
from utils.notifications import show_notification, icon_path


def QuestionPage(page: ft.Page):
    mascote = ft.Ref[ft.Image]()
    select_file_button_rf = ft.Ref[ft.ElevatedButton]()
    submit_button_rf = ft.Ref[ft.ElevatedButton]()

    selected_file = ft.Text(
        value="Pronto para a aventura? Escolha seu arquivo e vamos lá!",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.PRIMARY,
    )

    file_picker = ft.FilePicker(
        on_result=lambda e: on_file_picker_result(e, page, mascote, selected_file)
    )
    page.overlay.append(file_picker)

    select_file_button_control = ft.ElevatedButton(
        ref=select_file_button_rf,
        text="Selecionar Arquivo",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: [
            file_picker.pick_files(
                allow_multiple=False,
                allowed_extensions=["mp4", ".mov", ".avi", ".mkv"],
                dialog_title="Sele ",
            )
        ],
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.PRIMARY,
                ft.ControlState.HOVERED: ft.colors.SECONDARY,
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.ON_PRIMARY,
                ft.ControlState.HOVERED: ft.colors.ON_SECONDARY,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        ),
    )

    hf = ft.HapticFeedback()
    page.overlay.append(hf)

    async def on_confirm_upload(e):
        submit_button_rf.current.disabled = True
        select_file_button_rf.current.visible = False
        submit_button_rf.current.text = "Processando..."
        select_file_button_rf.current.update()
        submit_button_rf.current.update()
        try:
            await processar_upload(page)
        except Exception as e:
            if page.platform == "WINDOWS":
                show_notification(page, "Erro ao processar upload{e}", icon_path)
            elif page.platform == "ANDROID" or page.platform == "IOS":
                hf.heavy_impact()
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"Erro ao processar upload{e}"),
                    bgcolor=ft.colors.AMBER_400,
                )
            page.snack_bar.open = True
            page.update()
            print(f"Erro ao processar upload: {e}")
            return
        submit_button_rf.current.disabled = False
        select_file_button_rf.current.visible = True
        submit_button_rf.current.text = "Executar"
        submit_button_rf.current.update()
        select_file_button_rf.current.update()
        page.go("/quiz")

    submit_button_rf_control = ft.ElevatedButton(
        ref=submit_button_rf,
        text="Executar",
        icon=ft.icons.PLAY_CIRCLE_FILL,
        on_click=on_confirm_upload,
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.PRIMARY,
                ft.ControlState.HOVERED: ft.colors.SECONDARY,
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.ON_PRIMARY,
                ft.ControlState.HOVERED: ft.colors.ON_SECONDARY,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        ),
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Olá! Sou Quizzly",
                    style=(
                        ft.TextStyle(
                            weight=ft.FontWeight.BOLD, size=30, color=ft.colors.PRIMARY
                        )
                    ),
                ),
                ft.Text(
                    "Vejo que você quer dar uma olhada no seu vídeo.",
                    style=(
                        ft.TextStyle(
                            weight=ft.FontWeight.W_600, size=16, color=ft.colors.PRIMARY
                        )
                    ),
                ),
                ft.Divider(),
                ft.Container(
                    content=ft.Image(
                        ref=mascote,
                        src="/images/mascote/acenando_frente.png",
                        fit=ft.ImageFit.CONTAIN,
                        height=300,
                        width=300,
                    ),
                ),
                ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        ft.Container(
                            selected_file,
                            alignment=ft.alignment.center,
                            padding=5,
                            col=12,
                        ),
                        ft.Container(
                            content=select_file_button_control,
                            padding=5,
                            col={"sm": 12, "md": 6, "xl": 4},
                        ),
                        ft.Container(
                            submit_button_rf_control,
                            padding=5,
                            col={"sm": 12, "md": 6, "xl": 4},
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
        ),
    )
