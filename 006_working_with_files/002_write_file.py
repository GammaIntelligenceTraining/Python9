# Write files in Python

# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# Open file with write ('w') method.
# If file doesn't exist, it will create it. If it does exist, it will overwrite it. Be careful! Use 'a' to append.

string_variable = 'Hello world'
with open('text_files//test_text.txt', 'w', encoding='UTF8') as file:
    # # Sample 1
    # # Will add new string to the end of existing
    # file.write('Test')
    # file.write('Test')

    # # Sample 2
    # # Will add second line to begining of the file and overwrite length of new string
    file.write(string_variable)
    # file.seek(0)
    # file.write('*****')
