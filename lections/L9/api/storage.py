from api.models import Product, ProductCreate

# "База данных" — обычный список в памяти
_products: list[Product] = []
_next_id = 1


def get_all_products() -> list[Product]:
    """Возвращает все товары."""
    return _products


def get_product_by_id(product_id: int) -> Product | None:
    """Возвращает товар по id или None, если не найден."""
    for product in _products:
        if product.id == product_id:
            return product
    return None


def create_product(data: ProductCreate) -> Product:
    """Создаёт новый товар и добавляет в хранилище."""
    global _next_id
    product = Product(id=_next_id, **data.model_dump())
    _products.append(product)
    _next_id += 1
    return product


def delete_product(product_id: int) -> bool:
    """Удаляет товар по id. Возвращает True, если товар был найден и удалён."""
    global _products
    product = get_product_by_id(product_id)
    if product is None:
        return False
    _products = [p for p in _products if p.id != product_id]
    return True


def clear_storage() -> None:
    """Полностью очищает хранилище. Используется в тестах."""
    global _products, _next_id
    _products = []
    _next_id = 1
