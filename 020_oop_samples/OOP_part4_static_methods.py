import datetime

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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)

my_date = datetime.date(2021, 8, 21)
print(Employee.is_workday(my_date))