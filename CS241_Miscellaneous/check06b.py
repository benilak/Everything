class Phone:
    def __init__(self):
        self.area_code = int()
        self.prefix = int()
        self.suffix = int()

    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def display(self):
        print("\nPhone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))


class SmartPhone(Phone):
    def __init__(self):
        self.email = ""
        super().__init__()

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        print(self.email)


def main():
    phone = Phone()
    print("Phone:")
    phone.prompt_number()
    phone.display()

    print()

    smartphone = SmartPhone()
    print("Smart phone:")
    smartphone.prompt()
    smartphone.display()


if __name__ == "__main__":
    main()


