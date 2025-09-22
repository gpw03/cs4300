import task6

# Checking if the function count_words() returns the correct number of words
# I created a new file task6_read_me_2.txt for another test
def test_check_word_count(capsys):
    assert task6.count_words('~/cs4300/homework1/task6_read_me.txt') == 104
    assert task6.count_words('~/cs4300/homework1/task6_read_me_2.txt') == 9

    