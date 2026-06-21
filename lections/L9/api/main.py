from api.models import Product, ProductCreate
from api.storage import (
    create_product,
    delete_product,
    get_all_products,
    get_product_by_id,
)
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Учебный API магазина")


@app.get("/products/", response_model=list[Product])
def list_products():
    """Возвращает список всех товаров."""
    return get_all_products()


@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int):
    """Возвращает один товар по id."""
    product = get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


@app.post("/products/", response_model=Product, status_code=201)
def add_product(product_data: ProductCreate):
    """Создаёт новый товар."""
    return create_product(product_data)


@app.delete("/products/{product_id}", status_code=204)
def remove_product(product_id: int):
    """Удаляет товар по id."""
    deleted = delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Товар не найден")
