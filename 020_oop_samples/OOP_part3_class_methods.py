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

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class methods
    @classmethod
    def set_pay_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)



# ### Using a class method will change value for class and all instances
emp_1.raise_amount = 1.20
Employee.set_pay_raise(1.10)
# emp_2.set_pay_raise(1.10)
print(Employee.raise_amount)
print(emp_1.raise_amount)


### Formatting a string into a class required variables

emp_str_1 = 'Bob-Morgan-1500'
emp_str_2 = 'Jane-Simons-3500'
emp_str_3 = 'Simon-Brooks-3000'

# Conventional method
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.fullname())

# Using a class method
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.fullname(), new_emp_2.email)

