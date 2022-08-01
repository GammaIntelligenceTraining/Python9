people = [('Jack', 'Smith', 30, 'Tallinn', 'Male'), ('Mary', 'Gold', 25, 'London', 'Female'),
          ('Piere', 'Summers', 32, None, 'Male'), ('Sarah', 'Connor', 30, 'Berlin', 'Female')]

for person in people:
    if person[4] == 'Male':
        print(f'This is {person[0]} {person[1]}. He is {person[2]} years old. He is from {person[3]}.')
    elif person[4] == 'Female':
        print(f'This is {person[0]} {person[1]}. She is {person[2]} years old. She is from {person[3]}.')

for name, surname, age, town, gender in people:
    if gender == 'Male':
        print(f'This is {name} {surname}. He is {age} years old. He is from {town}.')
    elif gender == 'Female':
        print(f'This is {name} {surname}. She is {age} years old. She is from {town}.')


