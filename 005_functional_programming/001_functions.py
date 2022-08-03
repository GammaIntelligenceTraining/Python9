def area(a, b):
    x = a * b
    return x

def perimeter(a, b):
    perimeter = 2 * (a + b)
    return perimeter

def print_message(name, age, profession):
    return print('Hi my name is', name, '. I am', age, 'years old. I work as a', profession, '.')

def no_parameters():
    x = 25 ** 0.5
    return x

# side_a = 5
# side_b = 10

# print(area(side_a, side_b))
# print(perimeter(side_a, side_b))

user_name, user_age, user_profession = input('Enter name, age and profession divided by space: ').split(' ')
print_message(user_name, user_age, user_profession)


#
# print(no_parameters())
