import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_product_list_returns_200(client):
    """Страница списка товаров возвращает статус 200."""
    url = reverse("product_list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_list_shows_active_products(client, product, inactive_product):
    """В списке отображаются только активные товары."""
    url = reverse("product_list")
    response = client.get(url)
    content = response.content.decode()

    assert "Ноутбук" in content
    assert "Старый телефон" not in content


@pytest.mark.django_db
def test_product_list_context(client, product):
    """View передаёт в шаблон queryset с товарами."""
    url = reverse("product_list")
    response = client.get(url)

    assert "products" in response.context
    assert product in response.context["products"]


@pytest.mark.django_db
def test_product_detail_returns_200(client, product):
    """Страница товара возвращает статус 200."""
    url = reverse("product_detail", kwargs={"pk": product.pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail_shows_correct_product(client, product):
    """На странице товара отображается правильное название и цена."""
    url = reverse("product_detail", kwargs={"pk": product.pk})
    response = client.get(url)
    content = response.content.decode()

    assert "Ноутбук" in content
    assert "50000" in content


@pytest.mark.django_db
def test_product_detail_inactive_returns_404(client, inactive_product):
    """Страница неактивного товара возвращает 404."""
    url = reverse("product_detail", kwargs={"pk": inactive_product.pk})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_product_list_empty(client):
    """Пустой список товаров — страница всё равно возвращает 200."""
    url = reverse("product_list")
    response = client.get(url)
    assert response.status_code == 200
