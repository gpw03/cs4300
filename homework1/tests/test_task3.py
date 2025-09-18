
import task3

def test_sign_check():
    # Check negative value
    assert task3.check_sign(-7) == "negative"
    # Check positive value
    assert task3.check_sign(6) == "positive"
    # Check zero
    assert task3.check_sign(0) == "zero"

def test_count():
    # checking to make sure the sum of all numbers from 1 to 100 is returned (5050)
    assert task3.one_to_hundred() == 5050

def test_prime_nums():
    # Checking to make sure a list of the first 10 primes is returned
    assert task3.print_prime_nums() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
