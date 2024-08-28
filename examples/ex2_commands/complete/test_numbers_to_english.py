# tests of num_to_eng function
import pytest

from numbers_to_english import num_to_eng


def test_num_to_eng():
    # Test cases for numbers less than or equal to 999
    assert num_to_eng(0) == "zero"
    assert num_to_eng(5) == "five"
    assert num_to_eng(10) == "ten"
    assert num_to_eng(15) == "fifteen"
    assert num_to_eng(20) == "twenty"
    assert num_to_eng(99) == "ninety nine"
    assert num_to_eng(100) == "one hundred"
    assert num_to_eng(123) == "one hundred twenty three"
    assert num_to_eng(999) == "nine hundred ninety nine"

    # Test cases for numbers greater than 999
    with pytest.raises(ValueError):
        num_to_eng(1000)

    with pytest.raises(ValueError):
        num_to_eng(123456)

    with pytest.raises(ValueError):
        num_to_eng(9999999)
