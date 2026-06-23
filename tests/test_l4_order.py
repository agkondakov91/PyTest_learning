import pytest

from src.l4_order import calculate_total

# --- Happy path ---


def test_calculate_total_single_item():
    items = [{"price": 100.0, "quantity": 2}]
    assert calculate_total(items) == 200.0


def test_calculate_total_multiple_items():
    items = [
        {"price": 100.0, "quantity": 2},
        {"price": 50.0, "quantity": 3},
    ]
    assert calculate_total(items) == 350.0


def test_calculate_total_rounds_to_two_decimals():
    items = [{"price": 0.1, "quantity": 3}]
    assert calculate_total(items) == 0.3


# --- Edge cases ---


def test_calculate_total_empty_list():
    assert calculate_total([]) == 0.0


def test_calculate_total_zero_quantity():
    items = [{"price": 500.0, "quantity": 0}]
    assert calculate_total(items) == 0.0


# --- Error cases ---


def test_calculate_total_negative_quantity_raises_error():
    items = [{"price": 100.0, "quantity": -1}]
    with pytest.raises(ValueError, match="не может быть отрицательным"):
        calculate_total(items)


# Просто проверяем, что исключение выброшено
with pytest.raises(ValueError):
    calculate_total([{"price": 100.0, "quantity": -1}])

# Проверяем тип и сообщение
with pytest.raises(ValueError, match="не может быть отрицательным"):
    calculate_total([{"price": 100.0, "quantity": -1}])

# Сохраняем исключение для дополнительных проверок
with pytest.raises(ValueError) as exc_info:
    calculate_total([{"price": 100.0, "quantity": -1}])

assert "отрицательным" in str(exc_info.value)
