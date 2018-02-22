class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__()


def get_inverse(n):
    if int(n) < 0:
        raise NegativeNumberError
    return 1/int(n)


def main():
    try:
        value = input("Enter a number: ")
        inverse = get_inverse(value)
        print("The result is: {}".format(inverse))
        valid = True
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError:
        print("Error: The value cannot be negative")


if __name__ == "__main__":
    main()
