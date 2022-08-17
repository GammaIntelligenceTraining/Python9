# Documentation
# https://docs.python.org/3/library/csv.html?highlight=csv#module-csv
import csv

# Opens like any other file
with open('csv_files//test.csv', 'r', encoding='UTF8') as csv_file:

    # reader() method creates a csv.reader object that is iterable
    csv_reader = csv.reader(csv_file)
    print(csv_reader)

    # next() method, skips a row
    next(csv_reader)
    #
    # # iteration of csv_reader will return lists of csv data lines
    for line in csv_reader:
        # print(line)
        # these lists can be indexed too
        print(line)

# Write data to a file
with open('csv_files//test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open another file for writing
    with open('csv_files//test_copy.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-', lineterminator='\n')

#
        # writerow() method, writes one line
        for line in csv_reader:
            csv_writer.writerow(line)

# Sample of reading a csv file with wrong delimiter
with open('csv_files//test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', lineterminator='\n')
    for line in csv_reader:
        print(line)

# Sample of reading a csv file with wrong delimiter
with open('csv_files//test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)

# Write data to a file
with open('csv_files//test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Open another file for writing
    with open('csv_files//test_copy.csv', 'w') as new_file:
        fieldnames = ['Name', 'Date of birth', 'Town']
        # fieldnames = ['Name', 'Date of birth']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
        csv_writer.writeheader()

        # writerow() method, writes one line
        for line in csv_reader:
            # del line['Town']
            csv_writer.writerow(line)

