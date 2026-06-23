import pytest

from src.l6_cart import Cart


@pytest.fixture
def empty_cart():
    """Возвращает пустую корзину."""
    return Cart()


@pytest.fixture
def filled_cart():
    # --- SETUP: выполняется ДО теста ---
    cart = Cart()
    cart.add_item("Ноутбук", 50000, 1)
    cart.add_item("Мышь", 1500, 2)
    print(f"\n[fixture] Корзина создана, товаров: {cart.count()}")

    yield cart  # ← тест получает корзину здесь и выполняется

    # --- TEARDOWN: выполняется ПОСЛЕ теста ---
    cart.clear()
    print(f"[fixture] Корзина очищена, товаров: {cart.count()}")


@pytest.fixture
def cart_with_laptop(empty_cart):
    """Корзина с одним ноутбуком."""
    empty_cart.add_item("Ноутбук", 50000, 1)
    return empty_cart


@pytest.fixture
def cart_with_accessories(cart_with_laptop):
    """Корзина с ноутбуком и аксессуарами."""
    cart_with_laptop.add_item("Мышь", 1500, 1)
    cart_with_laptop.add_item("Коврик", 500, 1)
    return cart_with_laptop


def test_cart_total(filled_cart):
    assert filled_cart.total() == 53000.0


def test_cart_count(filled_cart):
    assert filled_cart.count() == 2


def test_cart_remove_item(filled_cart):
    filled_cart.remove_item("Мышь")
    assert filled_cart.count() == 1


def test_empty_cart_total(empty_cart):
    assert empty_cart.total() == 0.0


def test_full_cart_total(cart_with_accessories):
    assert cart_with_accessories.total() == 52000.0


def test_full_cart_count(cart_with_accessories):
    assert cart_with_accessories.count() == 3


def test_negative_price():
    cart = Cart()
    item = {"name": "Item1", "price": -10}
    with pytest.raises(ValueError, match="не может быть отрицательной"):
        cart.add_item(**item)


def test_negative_quantity():
    cart = Cart()
    item = {"name": "Item1", "price": 10, "quantity": -42}
    with pytest.raises(ValueError, match="должно быть больше нуля"):
        cart.add_item(**item)
