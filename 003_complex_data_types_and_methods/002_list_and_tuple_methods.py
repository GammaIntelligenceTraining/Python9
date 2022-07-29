courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
nums = [1, 5, 6, 8, 3, 4, 2]

# Variable replacement
test_list = [1, 2, 3]
print(test_list)
test_list[1] = 555
print(test_list)


# Adding removing items from list

# append() method inserts item into the end of list
courses.append('Art')
print(courses[-1])
print(courses)

# insert() method inserts item into specific place in list
# [some_list.insert(index, value)]
courses.insert(0, 'English')
print(courses[0])
print(courses)

# extend() method adds items from other list to the end
# if append() will be used
# list will be inserted as one item.
courses2 = ['Economics', 'Marketing']
courses.extend(courses2)
print(courses)

# remove() method removes item from a list
courses.remove('Math')  # Removes value in brackets
print(courses)

# pop() method removes last item in a list
courses.pop()
print(courses)

# pop() method also returns value of a popped item
# and can be stored in a variable
popped_item = courses.pop()
print(popped_item)
print(courses)


# Sorting lists

# reverse() method returns a reversed list
print(courses)
courses.reverse()
print(courses)

# sort() method sorts a list in alphabetical order
courses.sort()
print(courses)

# numbers will be sorted ascending order
print(nums)
nums.sort()
print(nums)

# reverse='bool' condition will sort list in reversed order
courses.sort(reverse=True)  # Sorting in reversed order
nums.sort(reverse=True)
print(courses)
print(nums)

# sorted() method sorts list but doesn't change original
print(sorted(courses))
print(courses)

# if stored in original variable
# sorted() replaces original
courses = sorted(courses)
print(courses)

# Statistical methods

# min() method returns minimum value from iterable object
print(min(courses))

# max() method returns maximum value from iterable object
print(max(nums))

# sum() method will sum all numbers from iterable object
# works with numeric values only!!!
print(sum(nums))

# index() method returns index of an item
print(courses.index('Programming'))
print(courses[1])

# will return False if not in list or True if is in list
print('Sports' in courses)

# List conversion methods
# join() method returns a string from list items joined by 'condition'
courses_str = ', '.join(courses)
print(courses_str)
print(type(courses), 'Courses')
print(type(courses_str), 'courses_str')

# split('condition') converts string back to list
# 'condition' will act as separator
new_list = courses_str.split(', ')
print(new_list)

# list can be merged using '+'
new_joined_list = courses + nums
print(new_joined_list)

# Creating a copy of a list
# this way will change both
# no matter what variable you make changes in
list_1 = ['Math', 'History', 'Programming', 'Physics']
list_2 = list_1
print(list_1)
print(list_2)

list_1[2] = 'Sports'
list_2[0] = 'Art'

print(list_1)
print(list_2)

# copy() method will create a copy of variable value
list_1 = ['Math', 'History', 'Programming', 'Physics']
list_2 = list_1.copy()
print(list_1)
print(list_2)

list_1[2] = 'Sports'
list_2[0] = 'Art'

print(list_1)
print(list_2)
