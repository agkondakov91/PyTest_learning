import smtplib
from email.message import EmailMessage


def send_email(to: str, subject: str, body: str) -> bool:
    """Отправляет email. Возвращает True при успехе."""
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP("localhost", 1025) as server:
            server.send_message(msg)
        return True
    except Exception:
        return False


def notify_user_on_order(user_email: str, order_id: int) -> bool:
    """Уведомляет пользователя о создании заказа."""
    subject = f"Заказ №{order_id} создан"
    body = f"Ваш заказ №{order_id} принят в обработку."
    return send_email(user_email, subject, body)
