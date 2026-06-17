import pytest

from lections.L6.cart import Cart


@pytest.fixture
def empty_cart():
    """Пустая корзина — доступна во всех тестовых файлах."""
    return Cart()


@pytest.fixture
def filled_cart():
    """Корзина с товарами — доступна во всех тестовых файлах."""
    cart = Cart()
    cart.add_item("Ноутбук", 50000, 1)
    cart.add_item("Мышь", 1500, 2)
    return cart


@pytest.fixture
def sample_items():
    """Список товаров для тестов заказов."""
    return [
        {"price": 100.0, "quantity": 2},
        {"price": 50.0, "quantity": 3},
    ]
