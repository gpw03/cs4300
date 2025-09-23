# Importing functions from task2.py
import task2
import pytest

@pytest.mark.parametrize(
    "int_1, int_2, expected",
    [
        (2, 3, 5), 
        (-2, 8, 6)
    ]
)

# Testing add_ints()
def test_int(int_1: int, int_2: int, expected: int):
    result = task2.add_ints(int_1, int_2)
    assert result == expected

@pytest.mark.parametrize(
    "float_1, float_2, expected",
    [
        (3.5, 2.0, 1.75),
        (-3.5, 2.0, -1.75)
    ]
)

# Testing divide_floats()
def test_float(float_1: float, float_2: float, expected: float):
    result = task2.divide_floats(float_1, float_2)
    assert result == expected

@pytest.mark.parametrize(
    "string_one, string_two, expected",
    [
        ("Hi", "Hello", "HiHello"),
        ("One", " Two", "One Two")
    ]
)

# Testing concat_strings()
def test_strings(string_one: str, string_two: str, expected: str):
    result = task2.concat_strings(string_one, string_two)
    assert result == expected

@pytest.mark.parametrize(
    "val, expected",
    [
        (21, True),
        (20, False),
        (19, False)
    ]
)

# Testing above_twenty()
def test_bool(val, expected):
    result = task2.above_twenty(val)
    assert result == expected