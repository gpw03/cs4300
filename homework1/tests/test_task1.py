# Importing the function from task1.py
import task1

# Test the output of hello() == "Hello, World!"
def test_hello(capsys):
    task1.hello() # Calling the function
    captured = capsys.readouterr() # Capturing the output
    assert captured.out == "Hello, World!\n" # Comparing the output print auto adds \n
