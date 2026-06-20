import pytest
from shop.models import Category, Product


@pytest.mark.django_db
def test_category_str():
    """__str__ возвращает название категории."""
    category = Category.objects.create(name="Электроника")
    assert str(category) == "Электроника"


@pytest.mark.django_db
def test_product_str(product):
    assert str(product) == "Ноутбук"


@pytest.mark.django_db
def test_product_discounted_price(product):
    """Скидка 10% на товар за 50000 = 45000."""
    assert product.discounted_price(10) == 45000.0


@pytest.mark.django_db
def test_product_discounted_price_zero(product):
    """Скидка 0% — цена не меняется."""
    assert product.discounted_price(0) == 50000.0


@pytest.mark.django_db
def test_product_discounted_price_full(product):
    """Скидка 100% — цена становится 0."""
    assert product.discounted_price(100) == 0.0


@pytest.mark.django_db
def test_product_discounted_price_invalid(product):
    """Скидка вне диапазона вызывает ValueError."""
    with pytest.raises(ValueError, match="от 0 до 100"):
        product.discounted_price(110)


@pytest.mark.django_db
def test_product_is_active_by_default(category):
    """Товар активен по умолчанию."""
    product = Product.objects.create(
        name="Мышь",
        price=1500.00,
        category=category,
    )
    assert product.is_active is True


@pytest.mark.django_db
def test_only_active_products_in_queryset(product, inactive_product):
    """Фильтр is_active=True возвращает только активные товары."""
    active = Product.objects.filter(is_active=True)
    assert product in active
    assert inactive_product not in active
