    # https://docs.python.org/3/reference/datamodel.html

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Meant to be seen by other developers
    # Commonly used for debugging
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # Meant to be readable representation of an object
    # If __str__ is not defined, __repr__ will be used
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Method for adding two objects
    def __add__(self, other):
        return self.pay + other.pay

    # Len methond
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)

print(1+2)
print('a' + 'b')

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(1 + 2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)

print(len("Test"))

print('test'.__len__())

print(len(emp_1))