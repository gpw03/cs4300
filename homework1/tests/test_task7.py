import task7

# Testing numpy functions from task7.py
def test_numpy(capsys):
    # Testing the mean function
    assert task7.calculate_mean([1, 2, 3, 4, 5]) == 3.0
    assert task7.calculate_mean([.1, 9.9]) == 5.0
    # Testing the median function
    assert task7.calculate_median([1, 2, 3, 4, 5]) == 3.0
    assert task7.calculate_median([.1, 9.9, 100]) == 9.9
    # Testing the dot product function
    assert task7.calculate_dot_product([1, 2], [3, 4]) == 11
    assert task7.calculate_dot_product([0, 2], [3, 0]) == 0
