import itertools

def more_than_two(x):
    if x > 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]


# Compress returns an iterable of values when True
result = itertools.compress(letters, selectors)

for item in result:
    print(item)

# Filter function example
result = filter(more_than_two, numbers)

for item in result:
    print(item)

# filterfalse() does opposite to regular filter() functions
result = itertools.filterfalse(more_than_two, numbers)

for item in result:
    print(item)

# dropwhile() and takewhile()
result = itertools.dropwhile(more_than_two, numbers2)
# result = itertools.takewhile(more_than_two, numbers2)

for item in result:
    print(item)


# accumulate()
result = itertools.accumulate(numbers)

for item in result:
    print(item)