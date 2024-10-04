import flet as ft
from services.thumbnail_generator import generate_thumbnail


def on_file_picker_result(e: ft.FilePickerResultEvent, page, wallpaper_container, selected_file):
    if e.files:
        file_name = e.files[0].name
        video_path = e.files[0].path
        page.session.set("video_path", video_path)
        page.session.set("last_selected_file", file_name)

        file_size = round(e.files[0].size / (1024 * 1024), 2)

        thumbnail_path = generate_thumbnail(
            video_path, f"thumbnail_{file_name}.jpg")

        wallpaper_container.current.image_src = thumbnail_path
        wallpaper_container.current.update()

        selected_file.value = f"Arquivo: {
            file_name}\nTamanho: {file_size} MB\n"
    else:
        selected_file.value = "Nenhum arquivo selecionado"
        wallpaper_container.current.image_src = "https://images8.alphacoders.com/136/1363709.png"
        wallpaper_container.current.update()
    page.update()
