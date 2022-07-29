# Lists and tuples
# Lists and tuples are iterable objects


# Sample of an empty list
empty_list = []
empty_list2 = list()
print(type(empty_list))


# Sample of a list with objects in it
world = 'world'

filled_list = [1, 0.2, 'Hello', world, True, [1, 2, 3]]
print(filled_list)


# # Indexing list items
courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']
#
# len() method returns length of an iterable object
print(len(courses))  # Prints length of lists. Basically how many items in list
print(courses)  # Prints list itself
print(courses[0])  # Prints first item from list, keep in mind that list items start with 0
print(courses[4])  # Prints fifth item from list.
print(courses[-1])  # Prints last item from list.
print(courses[0:2])  # Prints first and second items, keep in mind that 2 will not be included
print(courses[:3])  # Prints from beginning similar as [0:3]
print(courses[2:])  # Prints all starting with index 2
print(courses[::-1])  # Prints all items from list in backwards order
