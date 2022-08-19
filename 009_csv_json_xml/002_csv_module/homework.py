import csv

def sort_value(some_list):
    return (sorted(some_list, key=lambda x: x[2], reverse=True))

data_list = []
with open('csv_files//2019.csv', 'r', encoding='UTF8') as csv_file:
    # next(csv_file)
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        data_list.append(line)

result_list = []
for x in data_list:
    result_list.append([x['Overall rank'], x['Country or region'], x['GDP per capita']])
print(sort_value(result_list))
#
result_list = []
top_string = ''
top_list = []
for x in data_list:
    top_list.append(x['GDP per capita'])
while len(result_list) < 10:
    for x in data_list:
        if x['GDP per capita'] == max(top_list) and x not in result_list:
            result_list.append(x)
            top_list.remove(x['GDP per capita'])
#
# for res in result_list:
#     print(res)


# code_list = ['124365432-002', '124361231-004', '124361368-001']
# print(sorted(code_list, key=lambda x: x[-3:]))