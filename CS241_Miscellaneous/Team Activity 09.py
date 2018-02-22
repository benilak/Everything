class CheckingAccount:
    def __init__(self, starting_balance = 0.00, num_checks = 0):
        self.balance = starting_balance
        self.check_count = num_checks
        if starting_balance < 0:
            raise BalanceError("Starting balance cannot be negative.")
        if num_checks < 0:
            raise OutOfChecksError("Number of check cannot be negative.")

    def deposit(self, amount):
        self.balance += amount

    def write_check(self, amount):
        if self.check_count - 1 < 0:
            raise OutOfChecksError("Error: No more checks available.")
        self.check_count += -1
        if self.balance - amount < 0:
            raise BalanceError("Overdraft error: Not enough funds.")
        self.balance += -amount


    def display(self):
        print("Account balance: ${}".format(self.balance))
        print("This account has {} available checks.".format(self.check_count))

    def apply_for_credit(self, amount):
        pass


class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(message)


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        try:
            display_menu()
            command = input("Enter a command: ")

            if command == "new":
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))

                acc = CheckingAccount(balance, num_checks)
            elif command == "display":
                acc.display()
            elif command == "deposit":
                amount = float(input("Amount: "))
                acc.deposit(amount)
            elif command == "check":
                amount = float(input("Amount: "))
                acc.write_check(amount)
            elif command == "credit":
                amount = float(input("Amount: "))
                acc.apply_for_credit(amount)
        except BalanceError as message:
            print(message)
        except OutOfChecksError as message:
            print(message)
            bool = input("Would you like to purchase more checks? (yes/no): ")
            if bool == "yes":
                acc.check_count += 25
                acc.balance += -5.00

if __name__ == "__main__":
    main()