import pytest

from lections.L5.discount import apply_discount


@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (1000, 10, 900.0),
        (1000, 50, 500.0),
        (1000, 0, 1000.0),
        (1000, 100, 0.0),
    ],
    ids=[
        "discount 10%",
        "discount 50%",
        "no discounts",
        "discount 100%",
    ],
)
def test_apply_discount(price, discount, expected):
    assert apply_discount(price, discount) == expected


@pytest.mark.parametrize(
    "price, discount, error_message",
    [
        (-100, 10, "A price cannot be negative"),
        (1000, -5, "The discount must be between 0 and 100"),
        (1000, 110, "The discount must be between 0 and 100"),
    ],
)
def test_apply_discount_raises(price, discount, error_message):
    with pytest.raises(ValueError, match=error_message):
        apply_discount(price, discount)


@pytest.mark.parametrize("price", [100, 500, 1000])
@pytest.mark.parametrize("discount", [0, 10, 50])
def test_apply_discount_combinations(price, discount):
    result = apply_discount(price, discount)
    assert 0 <= result <= price  # результат всегда между 0 и исходной ценой
