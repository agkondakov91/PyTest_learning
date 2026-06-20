import pytest
from shop.models import Category, Product


@pytest.fixture
def category(db):
    """Тестовая категория товаров."""
    return Category.objects.create(name="Электроника")


@pytest.fixture
def product(category):
    """Активный тестовый товар."""
    return Product.objects.create(
        name="Ноутбук", price=50000.00, category=category, is_active=True
    )


@pytest.fixture
def inactive_product(category):
    """Неактивный товар — не должен отображаться в списке."""
    return Product.objects.create(
        name="Старый телефон", price=5000.00, category=category, is_active=False
    )
