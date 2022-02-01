import pytest

@pytest.mark.parametrize("numerator, output", [(25, 0), (5, 0), (33, 0), (40, 0)])
def test_divisible_by_five(numerator, output):
    assert numerator % 5 == output