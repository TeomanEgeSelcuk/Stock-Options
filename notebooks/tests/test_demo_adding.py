import pytest
from demo_adding import add_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_add_numbers(a, b, expected):
    result = add_numbers(a, b)
    assert result == expected
