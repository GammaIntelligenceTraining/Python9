# https://docs.python.org/3/library/exceptions.html
while True:
    try:
        user_input = input('Please enter your Estonian national ID number: ')
        user_input = str(int(user_input))
        print(user_input)
        if len(user_input) != 11:
            raise UserWarning

    except ValueError:
        print('Code you entered is not numeric')
        continue
    except UserWarning:
        print('Code you entered is not 11 numbers long')
        continue
    else:
        print('Else statement')
    finally:
        print('Program finished working')
