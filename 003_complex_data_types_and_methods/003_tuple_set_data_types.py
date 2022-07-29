# List, Tuple, Set differences

# List is ORDERED and MUTABLE object
courses = ['Math', 'History', 'Programming', 'Physics']
print(courses)
courses[0] = 'Sports'
print(courses)

# Tuple is ORDERED and NOT MUTABLE object
courses_tuple = ('Math', 'History', 'Programming', 'Physics')
print(courses_tuple)
print(courses_tuple[2])

# will raise error
courses_tuple[2] = 10

# However tuples can be added to each other
t1 = (1, 2, 3)
t2 = (3, 4, 5)
print(t1 + t2)

# Set is NOT ORDERED and MUTABLE object
# doesn't contain duplicates
courses_set = {'Math', 'History', 'Programming', 'Physics', 'Math'}
print(courses_set)
courses_set.remove('Math')
print(courses_set)

# Set specific methods
set1 = {'Math', 'History', 'Programming', 'Physics'}
set2 = {'Art', 'Physics', 'Design', 'History'}

# intersection() method returns a set of intersection between two sets
print(set1.intersection(set2))

# difference() method returns a set of differences in two sets
print(set2.difference(set1))
print(set1.difference(set2))

# union() method will return a set of all values from both sets
print(set1.union(set2))

# Converting list, tuple, set

# Empty list
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {}  # This will create a dictionary instead of set
empty_set = set()