from win10toast import ToastNotifier
import time
import os
import flet as ft

# Inicializar o ToastNotifier
toaster = ToastNotifier()

icon_path = "assets/images/icon_wintoast.ico"
sound_path = "assets/audios/notification_song.wav"


def show_notification(page, title, message, icon_path, duration=5):
    if not os.path.exists(icon_path):
        print(f"Ícone não encontrado: {icon_path}")
        icon_path = None

    if not title or not message:
        print("Título ou mensagem inválida.")
        return

    try:
        audio = ft.Audio(src=sound_path, autoplay=True, volume=0.5)
        page.controls.append(audio)
        page.update()
    except Exception as e:
        print(f"Erro ao tocar o som: {e}")

    toaster.show_toast(
        title,
        message,
        icon_path=icon_path,
        duration=duration,
        threaded=True,
    )

    time.sleep(0.5)

    # Verificar se a notificação ainda está ativa
    while toaster.notification_active():
        time.sleep(0.1)
