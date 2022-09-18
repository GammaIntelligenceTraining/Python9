class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@example.com'

    # Decorator
    @ property
    def email(self):
        return '{}.{}@example.com'.format(self.first, self.last)
    @ property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

# This will change self.first but won't change first
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Jack Summers'
print(emp_1.fullname)

del emp_1.fullname