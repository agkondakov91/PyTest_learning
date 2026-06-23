import pytest

from src.l2_calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    # Arrange — готовим данные
    numerator = 10
    denominator = 2
    expect = 5.0

    # Act — вызываем код, который тестируем
    result = divide(numerator, denominator)

    # Assert — проверяем результат
    assert expect == result


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
