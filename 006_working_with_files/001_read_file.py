# Open files in python

# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

file = open('text_files//lorem.txt', 'r', encoding='UTF8')
print(file.name)  # Prints file name and path
print(file.mode)  # Prints mode that file is opened with
print(file.closed)  # Returns True if file is closed and False if not
file.close()  # Closes file. If file is not closed, you can run into maximum opened files in your system and get an error.


# Opens files as context manager
# Automaticaly closes file after block of code is done
with open('text_files/lorem.txt', 'r', encoding='UTF8') as file:
    # Sample 1
    # Will read everything inside text file and save it in file_content variable
    file_content = file.read()
    print(file_content)

    # # Sample 2
    # # # Will read lines of text file and store each line as list item in file_content variable
    # file_content = file.readlines()
    # print(file_content)

    # # Sample 3
    # # # Will read only one line and store it in file_content variable
    # file_content = file.readline()
    # print(file_content, end='')
    # #
    # file_content = file.readline()
    # print(file_content, end='')  # End = '' will help to get rid of \n symbol in the end of a line

    # # Sample 4
    # # Will read and print each line in file. This method won't overload your memory in case of large files
    # for line in file:
    #     print(line, end='')

    # # Sample 5
    # # Number in () tells how many characters of the file to read
    # file_content = file.read(5000)
    # print(file_content, end='')
    #
    # file_content = file.read(5000)
    # print(file_content, end='')

    # file_content = file.read(5000)  # Won't return anything if there is nothing to read left
    # print(file_content, end='')

    # # Sample 6
    # # Will loop through the file reading and printing 100 characters each loop
    # size_to_read = 100
    # file_content = file.read(size_to_read)
    # while len(file_content) > 0:
    #     print(file_content, end='****')
    #     file_content = file.read(size_to_read)  # If you delete this line, you will get infinite loop

    # # Sample 7
    # #
    # size_to_read = 100
    # file_content = file.read(size_to_read)
    # print(file_content, end='')
    #
    # file.seek(0)  # Will tell where to start reading
    #
    # file_content = file.read(size_to_read)
    # print(file_content)

    # # Sample 8
    # # Will return error if you try to write file opened with 'r' method
    # file.write('TEST')