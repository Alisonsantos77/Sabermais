def show_notification_plyer(title, message, max_length=100):
    if message is None:
        message = "Nenhuma mensagem disponível."

    # Limitar a mensagem ao tamanho máximo, se necessário
    display_message = (message[:max_length] +
                       '...') if len(message) > max_length else message

    print(f"{title}: {display_message}")
