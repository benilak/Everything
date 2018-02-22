class Employee:
    def __init__(self, name):
        self.name = str(name)

    def display(self):
        print("Name: {}".format(self.name))


class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        super().__init__(name)
        self.hourly_wage = int(wage)

    def display(self):
         print("{} - ${}/hour".format(self.name, self.hourly_wage))


class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = int(salary)

    def display(self):
        print("{} - ${}/year".format(self.name, self.salary))


def main():

    employees = []
    command = ""

    print("\nTo add a salaried employee, press \'s\'.\n"
          "To add an hourly employee, press \'h\'.\n"
          "To quit, press \'q\'.")

    while command != 'q':

        command = input("\nEnter (\'s\'/\'h\'/\'q\'): ")
        if command == 's':
            name = input("\nEnter employee name: ")
            salary = input("Enter employee salary: ")
            employees.append(SalaryEmployee(name, salary))
        elif command == 'h':
            name = input("\nEnter employee name: ")
            salary = input("Enter employee wage: ")
            employees.append(HourlyEmployee(name, salary))
        elif command == 'q':
            break

    print()

    for employee in employees:
        employee.display()


if __name__ == "__main__":
    main()