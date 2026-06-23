def apply_discount(price: float, discount: float) -> float | int:
    if price < 0:
        raise ValueError("A price cannot be negative")
    if not (0 <= discount <= 100):
        raise ValueError("The discount must be between 0 and 100")

    result = price * (1 - discount / 100)
    return round(result, 2)
