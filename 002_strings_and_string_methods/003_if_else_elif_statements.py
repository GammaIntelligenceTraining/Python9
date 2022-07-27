id_code = input('Please enter your national id: ')

if len(id_code) == 11:
    print('Your ID code is', id_code)
elif len(id_code) > 11:
    print('Code you entered is longer than 11 digits')
else:
    print('Code you entered is shorter than 11 digits')
