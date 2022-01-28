import pytest

@pytest.fixture
def data_set():
    return (-111, -33.3, -5, 0, 0.67, 12, 100, 'abc')


def add_all_positive_numbers(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

def test_add_positive_integers(data_set):
    assert add_all_positive_numbers(data_set) == 112.67