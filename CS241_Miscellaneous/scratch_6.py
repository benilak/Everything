def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    copy = numbers
    numbers = [copy[0]]
    for i in range(len(copy) - 1):
        numbers.append("x")
        for k in range(i, -1, -1):
            if numbers[k] > copy[i + 1]:
                numbers[k + 1] = numbers[k]
                numbers[k] = "x"
                if numbers[0] == "x":
                    numbers[0] = copy[i + 1]
            else:
                numbers[k + 1] = copy[i + 1]
                break

numbers = [3, 7, 1, 9]

sort(numbers)

print(numbers)