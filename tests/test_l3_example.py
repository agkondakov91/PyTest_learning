import pytest

from lections.L2.calculator import add, divide, subtract


@pytest.mark.skip(reason="Функция ещё не реализована")
def test_future_feature():
    assert some_future_function() == 42  # noqa


@pytest.mark.xfail(reason="Известный баг, тикет #123")
def test_known_bug():
    assert divide(10, 0) == 0  # noqa # мы знаем, что это упадёт


@pytest.mark.fast
def test_add():
    assert add(2, 3) == 5


@pytest.mark.fast
def test_subtract():
    assert subtract(10, 3) == 7


@pytest.mark.slow
def test_heavy_calculation():
    # Представим, что это долгий тест
    result = sum(add(i, i) for i in range(1_000_000))
    assert result > 0
