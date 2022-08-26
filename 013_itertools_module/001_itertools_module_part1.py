import itertools

# Count

counter = itertools.count()

# Will create an infinite loop
for num in counter:
    print(num)
    # Will break the loop when reached 50000
    if num == 50000:
        break


# Will return counter value one by one
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Where used example
data = [100, 200, 300, 400]

# Zip function combines two iterables and pairs values together
daily_data = zip(itertools.count(), data)
for x in daily_data:
    print(x)

# zip_longest() method will create pairs until longest iterable has items
data = [100, 200, 300, 400]
daily_data = list(zip(data, range(10)))
print(daily_data)

daily_data2 = list(itertools.zip_longest(data, range(10)))
# daily_data2 = list(itertools.zip_longest(data, itertools.count()))
print(daily_data2)

# Count from, Count step
counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Count different ways
counter = itertools.count(start=0.5, step=-1.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# cycle() method cycles given values
counter = itertools.cycle([1, 2, 3])
counter = itertools.cycle(('On', 'Off'))

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# repeat, will repeat given values times=x
counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# Repeat
counter = itertools.repeat(2, times=3)

def squares(x):
    return x ** 2

result = map(squares, range(10))
print(list(result))

result2 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(result2))

result3 = map(pow, range(10), itertools.repeat(2))
print(list(result3))



