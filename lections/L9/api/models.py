from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    """Общие поля товара — для создания и чтения."""

    name: str = Field(min_length=3, max_length=200)
    price: float = Field(gt=0, description="Цена должна быть больше нуля")
    is_active: bool = True


class ProductCreate(ProductBase):
    """Данные, которые приходят при создании товара."""

    pass


class Product(ProductBase):
    """Полная модель товара — с id, как она хранится и отдаётся."""

    id: int
