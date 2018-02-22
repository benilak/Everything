"""
File: check12a.py
Original Author: Brother Burton

Purpose: This file is a starting point to help you practice list comprehensions
"""


def get_part1_list():
    """
    Returns a list of the squares of the numbers [0-99], e.g., 0, 1, 4, 9, 16, 25 ...]
    """
    numbers = [x**2 for x in range(100)]  # TODO: Change this line to be a list comprehension

    return numbers


def get_part2_list():
    """
    Returns a list of the the numbers [0-99] that are divisible by either 5 or 7
    """
    numbers = [x for x in range(100) if x%5==0 or x%7==0] # TODO: Change this line to be a list comprehension

    return numbers

def get_part3_list():
    """
    Filters a list of words to return only those that are at
    least 4 letters long and contain an 'e'
    """
    old_words = ["tacos", "knowledge", "water", "on", "the", "I", "is", "hilari\
ous", "tie", "coat", "white", "covenants", "phone", "rubric", "send", "restrict\
ions"]

    new_words = [x for x in old_words if len(x)>=4 and "e" in x] # TODO: Change this line to be a list comprehension

    return new_words

def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()