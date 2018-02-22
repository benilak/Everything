def main():
    valid = False
    while not valid:
        try:
            number = int(input("Enter a number: "))
            print("The result is: {}".format(number*2))
            valid = True
        except Exception:
            print("The value entered is not valid")


if __name__ == "__main__":
    main()

