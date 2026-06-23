class Cart:
    def __init__(self):
        self.items: list[dict] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Добавляет товар в корзину."""
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name: str) -> None:
        """Удаляет товар из корзины по имени."""
        self.items = [item for item in self.items if item["name"] != name]

    def total(self) -> float:
        """Возвращает итоговую сумму."""
        return round(sum(item["price"] * item["quantity"] for item in self.items), 2)

    def clear(self) -> None:
        """Очищает корзину."""
        self.items = []

    def count(self) -> int:
        """Возвращает количество позиций в корзине."""
        return len(self.items)
