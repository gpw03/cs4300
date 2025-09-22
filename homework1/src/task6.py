import os

# Input is a filepath relative to the home directory 
# Opens file, then splits it by white space then get the length of that
def count_words(file_path: str) -> int:
    # Getting the full filepath
    full_file_path = os.path.expanduser(file_path)
    # Opening the file, reading the content, splitting by white spcace
    # then using len() to count the number of words. 
    with open(full_file_path, 'r') as f:
        content = f.read()
        words = content.split()
        word_count = len(words)
    return word_count # Returning word count