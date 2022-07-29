# For loops and lists
courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
print(courses)
# for loop will iterate iterable object and
# do something with each iter
for subject in courses:
    print(subject)

# enumerate() method creates indexes for iterable object values
# for loop returns 2 values, index in list and value
for index, subject in enumerate(courses):
    print(index, subject)

# start=(int) condition will start counting from index = 'int'
for index, subject in enumerate(courses, start=3):
    print(index, subject)