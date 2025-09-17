# Importing functions from task2.py
import task2

# Testing add_ints()
def test_int():
    assert task2.add_ints(2, 3) == 5
    assert task2.add_ints(-2, 8) == 6

# Testing divide_floats()
def test_float():
    assert task2.divide_floats(3.5, 2.0) == 1.75
    assert task2.divide_floats(-3.5, 2.0) == -1.75

# Testing concat_strings()
def test_strings():
    assert task2.concat_strings("Hi", "Hello") == "HiHello"
    assert task2.concat_strings("One", " Two") == "One Two"

# Testing above_twenty()
def test_bool():
    assert task2.above_twenty(21) == True
    assert task2.above_twenty(20) == False
    assert task2.above_twenty(19) == False