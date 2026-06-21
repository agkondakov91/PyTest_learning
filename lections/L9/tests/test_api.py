import pytest


@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"name": "Товар", "price": 100.0}, 201),  # корректные данные
        ({"name": "", "price": 100.0}, 422),  # пустое имя
        ({"name": "Товар", "price": 0}, 422),  # нулевая цена
        ({"name": "Товар", "price": -50}, 422),  # отрицательная цена
        ({"price": 100.0}, 422),  # нет имени
    ],
    ids=[
        "correct data",
        "empty name",
        "zero price",
        "negative price",
        "unnamed",
    ],
)
def test_create_product_validation(client, payload, expected_status):
    response = client.post("/products/", json=payload)
    assert response.status_code == expected_status


def test_list_products_empty(client):
    """Пустое хранилище — пустой список в ответе."""
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_nonexistent_product_returns_404(client):
    """Запрос несуществующего товара возвращает 404."""
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Товар не найден"


def test_create_product(client):
    """Создание товара возвращает 201 и данные товара."""
    payload = {"name": "Ноутбук", "price": 50000.0, "is_active": True}
    response = client.post("/products/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Ноутбук"
    assert data["price"] == 50000.0
    assert data["id"] == 1  # первый созданный товар получает id=1


def test_create_product_appears_in_list(client):
    """Созданный товар появляется в общем списке."""
    client.post("/products/", json={"name": "Мышь", "price": 1500.0})
    response = client.get("/products/")

    assert response.status_code == 200
    products = response.json()
    assert len(products) == 1
    assert products[0]["name"] == "Мышь"


def test_create_product_invalid_price_returns_422(client):
    """Отрицательная цена не проходит валидацию Pydantic."""
    payload = {"name": "Сломанный товар", "price": -100.0}
    response = client.post("/products/", json=payload)
    assert response.status_code == 422


def test_create_product_missing_name_returns_422(client):
    """Отсутствие обязательного поля — ошибка валидации."""
    payload = {"price": 1000.0}
    response = client.post("/products/", json=payload)
    assert response.status_code == 422


def test_delete_product(client):
    """Удаление существующего товара возвращает 204."""
    create_response = client.post(
        "/products/", json={"name": "Клавиатура", "price": 2500.0}
    )
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_product_returns_404(client):
    """Удаление несуществующего товара возвращает 404."""
    response = client.delete("/products/999")
    assert response.status_code == 404


def test_full_product_lifecycle(client):
    """
    Полный жизненный цикл товара:
    создать → прочитать → удалить → проверить отсутствие.
    """

    # Создаём
    create_response = client.post(
        "/products/", json={"name": "Монитор", "price": 15000.0}
    )
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # Читаем
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Монитор"

    # Удаляем
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 204

    # Проверяем отсутствие
    final_get = client.get(f"/products/{product_id}")
    assert final_get.status_code == 404
