"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    sublist = [numbers[0]]
    for i in range(len(numbers) - 1):
        sublist.append("x")
        for k in range(i, -1, -1):
            if sublist[k] > numbers[i + 1]:
                sublist[k + 1] = sublist[k]
                sublist[k] = "x"
                if sublist[0] == "x":
                    sublist[0] = numbers[i + 1]
            else:
                sublist[k + 1] = numbers[i + 1]
                break
    return sublist

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    numbers = sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()