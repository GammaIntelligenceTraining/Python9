import json

# Opens JSON file
with open('sample2.json', 'r', encoding='UTF8') as file:
    # Method "load" is used to read a file and "loads" is used to read string
    data = json.load(file)
    print(data)


# For loop to delete person['has_licence'] entry if it is equal to False
for person in data['people']:
    if person['has_licence'] == False:
        del person['has_licence']
print(data)
#
# # Method "dump" is used to save to file and "dumps" to save to string
with open('sample_edited.json', 'w') as file:
    json.dump(data, file, indent=2)