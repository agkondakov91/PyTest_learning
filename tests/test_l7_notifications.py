from unittest.mock import MagicMock, patch

from lections.L7.notifications import notify_user_on_order


@patch("lections.L7.notifications.send_email")
def test_notify_user_on_order(mock_send_email: MagicMock):
    mock_send_email.return_value = True
    result = notify_user_on_order("user@example.com", 42)
    assert result is True

    mock_send_email.assert_called_once_with(
        "user@example.com", "Заказ №42 создан", "Ваш заказ №42 принят в обработку."
    )


def test_notify_user_sends_correct_subject():
    with patch("lections.L7.notifications.send_email") as mock_send_email:
        mock_send_email.return_value = True
        notify_user_on_order("user@example.com", 99)
        args = mock_send_email.call_args
        assert args[0][1] == "Заказ №99 создан"


@patch("lections.L7.notifications.send_email")
def test_send_email_called_once(mock_send_email: MagicMock):
    mock_send_email.return_value = True
    notify_user_on_order("user@example.com", 1)

    # Был вызван ровно один раз
    mock_send_email.assert_called_once()

    # Был вызван с конкретными аргументами
    # mock_send_email.assert_called_with(
    #     'user@example.com',
    #     'Заказ №1 создан',
    #     'Ваш заказ №1 принят в обработку.',
    # )

    # Не был вызван — противоположная проверка
    # mock_send_email.assert_not_called()

    # Сколько раз вызван
    assert mock_send_email.call_count == 1
