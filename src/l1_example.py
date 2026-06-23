def add(a: int, b: int) -> int:
    return a + b


def test_add():
    result = add(40, 2)
    expected = 43
    assert result == expected, "FAILED"
    print(f"test: {result} == {expected}, PASSED")


test_add()
