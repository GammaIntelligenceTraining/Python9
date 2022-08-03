
def fullname(first, last):
    return f'{first.capitalize()} {last.capitalize()}'


def salary_message(person):
    if person[3] == 'Male':
        return f'This is {fullname(person[0], person[1])}. His salary is {person[2]:.2f}'
    elif person[3] == 'Female':
        return f'This is {fullname(person[0], person[1])}. Her salary is {person[2]:.2f}'


employees = [
    ('Jack', 'Smith', 2000, 'Male'), ('Bob', 'Summers', 1500, 'Male'),
    ('Mary', 'Gold', 3000, 'Female'), ('Sarah', 'Connor', 2500, 'Female'),
    ('Jack', 'Smith', 2000, 'Male'), ('Bob', 'Summers', 1500, 'Male'),
    ('Mary', 'Gold', 3000, 'Female'), ('Sarah', 'Connor', 2500, 'Female'),
    ('Jack', 'Smith', 2000, 'Male'), ('Bob', 'Summers', 1500, 'Male'),
    ('Mary', 'Gold', 3000, 'Female'), ('Sarah', 'Connor', 2500, 'Female')
]
for employee in employees:
    print(salary_message(employee))

def enter_id():
    global isikukood
    isikukood = input('Please enter id: ')



isikukood = ''
enter_id()
print(isikukood)