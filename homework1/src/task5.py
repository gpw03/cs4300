# Creates a list
def print_books():
    # Creating list with books and authors
    favorite_books = [
        "The Tattoist of Auschwits, Heather Morris", 
        "Refugee, Alan Gratz", 
        "The Tipping Point, Malcolm Gladwell", 
        "The Pragmatic Programmer, David Thomas, Andrew Hunt", 
        "Plague, Michael Grant"
    ]

    # Slicing the first 3 books off the list
    top_three = favorite_books[:3]
    print(top_three) # Printing

# This function created a student database then returns it
def student_database() -> dict[str, int]:
    # Creating the student database and filling with values
    student_db = {
        "Gabe": 1,
        "Ryan": 2,
        "Zach": 3,
        "Addie": 4, 
        "Kristen": 5, 
        "Cash": 6, 
        "Michael": 7
    }
    # Returning the DB so it can be looked at in testing
    return student_db

# Calling the function with test values and printing
if __name__ == "__main__":
    print("print_books() output:")
    print_books()
    print("student_database() db:")
    db = student_database()
    print(db)
