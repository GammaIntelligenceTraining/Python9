# Collections module

# Counter
from collections import Counter

sample_string = 'aaaaabbbbbbxcccccsadasdasdsss'
my_counter = Counter(sample_string)

# Counter returns a dictionary
print(my_counter)

# It can be indexed by key
print(my_counter['a'])

# keys() and values() methods are also applicable
print(my_counter.keys())
print(my_counter.values())

# # Most common items
# print(my_counter.most_common())
#
# # number in () will tell how many most commons to show
# print(my_counter.most_common(2))
#
# # Indexing works too
# print(my_counter.most_common(2)[0][0])
#
# # All elements can be extracted
# print(my_counter.elements())
# print(list(my_counter.elements()))

# # namedtuple
# from collections import namedtuple
#
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)

# OrderedDict
from collections import OrderedDict

some_dict = {'Name': 'Jack', 'Surname': 'Smith', 'Age': 30, 'Hometown': 'Atlanta'}
ordered_dict = OrderedDict()
ordered_dict['Name'] = 'Jack'
ordered_dict['Surname'] = 'Smith'
ordered_dict['Age'] = 30
ordered_dict['Hometown'] = 'Atlanta'
print(some_dict)
print(ordered_dict)


# Default dict
from collections import defaultdict

default_dict = defaultdict(int)  # Float, List and any other type of data
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['c'])


# # Deque
# from collections import deque
#
# # Deque works as normal list
# d = deque()
# d.append(1)
# d.append(2)
# print(d)
#
# # Difference is that you can choose where to append
# d.appendleft(3)
# print(d)
#
# # Deleting item from left side
# d.popleft()
# print(d)
#
# # Extending list from left side
# d.extendleft([4, 5, 6])
# print(d)
#
# # Rotating list elements
# d.rotate(1)
# print(d)
#
# # As many steps as you want
# d.rotate(2)
# print(d)
#
# # And also backwards
# d.rotate(-3)
# print(d)
