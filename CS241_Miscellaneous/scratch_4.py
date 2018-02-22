def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            while True:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))
                acc = CheckingAccount(balance, num_checks)
                try:
                    acc = CheckingAccount(balance)
                    break
                except BalanceError as e:
                    print(e)

            while True:
                num_checks = int(input("Numbers of checks: "))

                try:
                    acc = CheckingAccount(balance, num_checks)
                    break
                except OutOfChecksError as e:
                    print(e)

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