class Employee:

    # Class variables
    num_of_employees = 0
    raise_amount = 1.04

    # Regular methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        # Add 1 each time an instance is created
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Method to increase pay
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)


### pay_raise method was added
print(emp_1.pay)
emp_1.pay_raise()
print(emp_1.pay)


### Instance of a class parameters can be called by __dict__ command
print(emp_1.__dict__)
print(Employee.__dict__)

# variable can be change for a class
Employee.raise_amount = 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# or for one instance only
emp_1.raise_amount = 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)


### Example of an atribute that doesn't require using self
print(Employee.num_of_employees)
