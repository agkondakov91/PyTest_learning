def calculate_total(items: list[dict]) -> float:
    """
    Считает итоговую сумму заказа.
    items: список словарей вида {"price": float, "quantity": int}
    """
    if not items:
        return 0.0

    total = 0.0
    for item in items:
        if item["quantity"] < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        total += item["price"] * item["quantity"]

    return round(total, 2)
