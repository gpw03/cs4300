import task4

def test_discount():
    # input and return values are = (int, float) -> int
    # Testing all combonations
    assert task4.calculate_discount(100, 20) == 80 # (int, int) -> int
    assert task4.calculate_discount(49.99, 20) == 39.99 # (float, int) -> float
    assert task4.calculate_discount(50, 20.5) == 39.75 # (int, float) -> float
    assert task4.calculate_discount(49.99, 20.5) == 39.74 # (float, float) -> float