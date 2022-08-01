condition = True

while condition:
    user_input = input('Please enter ID: ')
    if len(user_input) != 11:
        print('Wrong code entered')
    else:
        condition2 = True
        while condition2:
            print(user_input)
            user_input2 = input('Please enter name or "x" to exit: ')
            if user_input2 == '':
                print('error')
            elif user_input2 == 'x':
                condition2 = False
                condition = False
            else:
                print(user_input2)
                condition2 = False
            condition = False



