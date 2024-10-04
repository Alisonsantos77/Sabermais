from plyer import notification


def show_notification_plyer(title, message):
    max_length = 256
    title = (title[:max_length] + '...') if len(title) > max_length else title
    message = (message[:max_length] +
               '...') if len(message) > max_length else message

    notification.notify(
        title=title,
        message=message,
        timeout=5
    )
