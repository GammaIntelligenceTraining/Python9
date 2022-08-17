# JSON - JavaScript Object Notation
# Documentation
# https://docs.python.org/3/library/json.html
import json

json_string = '''
{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true
    }
  ]
}'''

# Method "loads" is used to read string and "load" is used to read a file
data = json.loads(json_string)

# JSON data type is actually dictionary
print(type(data))
print(data)

# People list is accessed by 'people' key
print(type(data['people']))
print(data['people'][0]['emails'][0])

# For loop can be used with a 'people' list
for person in data['people']:
    # Prints entire person row
    print(person)
# #
#     # Prints specified data
    print(person['emails'][0])

people = data['people'][1]
print(people['name'], people['phone'])
print(people)

# # You can delete data from JSON
for person in data['people']:
    del person['phone']

print(data['people'])

# # Method "dumps" is used to save to string and "dump" to save to file
print(type(data))
print(data)
new_string = json.dumps(data, indent=2, sort_keys=True)  # sort_keys will sort keys in alphabetical order
print(new_string)
print(type(new_string))

# Separate data parts can be accessed
people = data['people']
person = people[0]
print(person['name'])
print(person['emails'])
print(person['phone'])