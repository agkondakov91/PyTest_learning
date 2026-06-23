def add(a: int, b: int) -> int:
    """Складывает два числа."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Вычитает второе число из первого."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Перемножает два числа."""
    return a * b


def divide(a: float, b: float) -> float:
    """Делит первое число на второе."""
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    return a / b
