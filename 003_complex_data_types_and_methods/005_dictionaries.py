# Dictionary must have a key and value
x = 5
student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Art', 'Programming'],
           1: 'int key', 0.2: 'float key', x: 'variable', 'var key': x}
print(student)

# To get value key must be insereted into []
print(student['age'])

# If key is variable, both variable name and variable value can be used
print(student[x])
print(student[5])
print(student['var key'])

print(student['job'])  # Will return error if not in dictionary
print(student.get('job'))  # Will return None if not in dictionary
print(student.get('courses'))  # Will return value if is in dictionary
print(student.get('job', 'Not Found'))  # Will return 'Not Found' instead of None


student['phone'] = '555-5555'  # Will add 'phone' key and its value to dictionary
student['name'] = 'Michael'  # Will change value

student.update({'name': 'Michael', 'age': 27, 'phone': '555-5555'})  # Can be used to modify/add values and keys
print(student)

del student['age']  # Will delete key and value
print(student)

age = student.pop('age')  # Same as list, will return value and remove key-value pair. Can return popped value.
print(student)
print(age)

print(len(student))  # Will return length of a dictionary

print(student.keys())  # Will return all keys in dictionary
print(student.values())  # Will return all values
print(student.items())  # Will return key-value pairs

for key in student:  # Will return all keys in a dictionary
    print(key)
#
for key, value in student.items():  # Will return all key-value pairs in dictionary
    print(key, value)