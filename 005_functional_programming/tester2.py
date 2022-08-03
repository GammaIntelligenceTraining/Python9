def square(x, y):
    z = y ** x
    return z

def doubles(some_number):
    return some_number * 2

def triples(x):
    return x * 3

def many_squares(x):
    for num in x:
        print(num ** 2)

def print_message(name, surname, age, salary, gender):
    if gender.lower() == 'male':
        if salary == None:
            result = f'His name is {name} {surname}. He is {age} years old.'
        else:
            result = f'His name is {name} {surname}. He is {age} years old. His salary is {salary:.2f}.'
        return print(result)
    elif gender.lower() == 'female':
        if salary == None:
            result = f'Her name is {name} {surname}. She is {age} years old.'
        else:
            result = f'Her name is {name} {surname}. She is {age} years old. Her salary is {salary:.2f}.'
        return print(result)

employees = [['John', 'Smith', 33, 1500, 'Male'], ['Mary', 'Gold', 27, 2500, 'feMale'],
            ['Jack', 'Black', 20, 2000, 'male'], ['John', 'Smith', 33, 1500, 'Male'], ['Mary', 'Gold', 27, 2500, 'feMale'],
            ['Jack', 'Black', 20, 2000, 'male'], ['John', 'Smith', 33, 1500, 'Male'], ['Mary', 'Gold', 27, 2500, 'feMale'],
            ['Jack', None, 28, None, 'male'], ['John', 'Smith', 33, 1500, 'Male'], ['Mary', 'Gold', 27, 2500, 'feMale'],
            ['Jack Robet', 'Black', 20, 2000, 'male'], ['John', 'Smith', 33, 1500, 'Male'], ['Mary', 'Gold', 27, 2500, 'feMale'],
            ['Jack', 'Black', 20, 2000, 'male']]
# for employee in employees:
#     print_message(employee[0], employee[1], employee[2], employee[3], employee[4])

for name, surname, age, salary, gender in employees:
    print_message(name, surname, age, salary, gender)


