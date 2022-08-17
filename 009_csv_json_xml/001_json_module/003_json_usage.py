import json

with open('sample2.json', 'r', encoding='UTF8') as file:
    data = json.load(file)

for person in data['people']:
    name = person['name']
    phone = person['phone']
    emails = person['emails']
    has_licence = person['has_licence']
    salary = person['salary']
    print('Name: ' + name)
    print('Gross salary: ' + str(salary))
    print('Net salary: ' + str(salary * 0.8))