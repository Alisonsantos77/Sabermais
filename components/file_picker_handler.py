import flet as ft
from services.thumbnail_generator import generate_thumbnail_with_pillow


def on_file_picker_result(e: ft.FilePickerResultEvent, page, mascote, selected_file):
    if e.files:
        file_name = e.files[0].name
        video_path = e.files[0].path
        page.session.set("video_path", video_path)
        page.session.set("last_selected_file", file_name)

        file_size = round(e.files[0].size / (1024 * 1024), 2)

        thumbnail_filename = f"thumbnail_{file_name}.jpg"

        thumbnail_path = generate_thumbnail_with_pillow(
            video_path, thumbnail_filename)

        if thumbnail_path:
            mascote.current.src = thumbnail_path
            mascote.current.update()

        selected_file.value = f"Arquivo: {file_name}\nTamanho: {file_size} MB\n"
    else:
        selected_file.value = "Nenhum arquivo selecionado"
        mascote.current.src = "/images/mascote/triste.png" 
        mascote.current.update()
    page.update()
