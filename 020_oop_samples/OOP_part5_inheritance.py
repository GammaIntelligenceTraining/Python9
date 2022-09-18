class Employee:

    # Class variables
    raise_amount = 1.04

    # Regular methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Class inherits methods from other class
class Developer(Employee):
    raise_amount = 1.1
    
    def __init__(self, first, last, pay, prog_lang):
        # super().__init__() or Employee.__init__() is used to inherit methods from Employee class
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    # Method to add employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    # Method to remove employees
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employee(self):
        for emp in self.employees:
            print(emp.fullname())



# print(help(Developer))

emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)

print(emp_1.email)
print(emp_2.email)

dev_1 = Developer('Bob', 'Brown', 5000, 'Python')
dev_2 = Developer('Sarah', 'Simpson', 3000, 'C#')
# print(dev_1.email)
# print(dev_2.email)
#
# print(dev_1.pay)
# dev_1.pay_raise()
# print(dev_1.pay)
#
# print(emp_1.pay)
# emp_1.pay_raise()
# print(emp_1.pay)
#
# print(dev_1.email)
# print(dev_1.prog_lang)

man_1 = Manager('Simon', 'Green', 10000, [dev_1])
man_1.print_employee()
print('\n')
man_1.add_employee(dev_2)
man_1.print_employee()
print('\n')
man_1.remove_employee(dev_1)
man_1.print_employee()


# Check if object is instance
print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))


# Check if class is a subclass
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))