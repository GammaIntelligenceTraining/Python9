import itertools

def get_city(person):
    return person['city']

people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
]


result = itertools.groupby(people, get_city)

# Creating copies
copy1, copy2 = itertools.tee(result)


for key, group in copy1:
    print(key, group)
    print()
    # Print people grouped by city
    group = list(group)
    for person in group:
        print(person)

    # Print city and count how many people
    print(key, len(list(group)))

    # In case dictionary is not sorted, groups will be messed up

