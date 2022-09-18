# OOP allows us logically group our data and functions
# in the way it is easy to reuse and also easy to build upon if need be
# Method is as a function presented in class
# Class is like a blueprint for creating instances of class


### Creating a class
class Employee:
    pass

# Creating two instances of an Employee class.
emp_1 = Employee()
emp_2 = Employee()

# Both of these instances are objects of Employee class but are unique
print(emp_1)
print(emp_2)
#
# if emp_1 == emp_2:
#     print('They are same')
# elif emp_1 != emp_2:
#     print("They are not same")


### Simple method
# Adding attributes to instances of a Class
emp_1.first = 'Jack'
emp_1.last = 'Smith'
emp_1.email = 'jack.smith@example.com'
emp_1.pay = 2000

# emp_2.first = 'Mary'
# emp_2.last = 'Jones'
# emp_2.email = 'mary.jones@example.com'
# emp_2.pay = 2500
#
# print(emp_1.email)
# print(emp_2.email)

### __init__ method
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)


# Now all needed values can be passed in ()
emp_1 = Employee('Jack', 'Smith', 2000)
emp_2 = Employee('Mary', 'Jones', 2500)

# Instances of an Employee class are created
print(emp_1.first)
print(emp_2.first)

# Email method still can be used
print(emp_1.email)
print(emp_2.email)


### Printing full name
# Format a string
print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last))

# Printing full name through a Class
print(emp_1.Fullname())
print(emp_2.Fullname())

print(Employee.Fullname(emp_1))
print(Employee.Fullname(emp_2))

