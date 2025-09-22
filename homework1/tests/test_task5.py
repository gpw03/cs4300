import task5

# Test function for print_books() in task5
def test_book_list(capsys):
    task5.print_books() # Call print_books()
    output = capsys.readouterr() # Capture output of print_books()
    # Make sure the output is the top three books
    assert output.out == "['The Tattoist of Auschwits, Heather Morris', 'Refugee, Alan Gratz', 'The Tipping Point, Malcolm Gladwell']\n"

# Test function for student_databases() in task5
# Checks to make sure the reurned var is a dictionary type
# Then making there the name and sid are strings and ints
def test_student_database():
    # Calling function to return database, store in db
    db = task5.student_database()
    # Making sure db is a dictionary
    assert isinstance(db, dict)
    # Iterating through each item to make sure:
    # The names are all strings
    # The student Id (sid) numbers are all ints
    for name, sid in db.items():
        assert isinstance(name, str)
        assert isinstance(sid, int)
