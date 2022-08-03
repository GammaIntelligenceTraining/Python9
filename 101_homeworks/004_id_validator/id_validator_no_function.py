while True:  # First while cycle to keep entering code is wrong
    user_id = input('Please enter ID code or type "EXIT": ')
    if user_id.lower() == 'exit':
        print('Good bye!')
        break
    else:
        # Try, except, else to check id for errors
        try:
            int(user_id)
            if len(user_id) != 11:
                raise UserWarning
        except ValueError:
            print('ID you entered is not numeric! ')
        except UserWarning:
            if len(user_id) > 11:
                print('ID is too long')
            else:
                print('ID is too short')
            continue
        else:
            # If statement to get first numbers of birth year and gender
            if user_id[0] == '1':
                bcent = '18'
                gender = 'Male'
            elif user_id[0] == '2':
                bcent = '18'
                gender = 'Female'
            elif user_id[0] == '3':
                bcent = '19'
                gender = 'Male'
            elif user_id[0] == '4':
                bcent = '19'
                gender = 'Female'
            elif user_id[0] == '5':
                bcent = '20'
                gender = 'Male'
            elif user_id[0] == '6':
                bcent = '20'
                gender = 'Female'
            else:
                bcent = 'Unknown'
                gender = 'Unknown'

            # Get year, mont and day of birth
            byear = user_id[1:3]
            bmonth = user_id[3:5]
            bday = user_id[5:7]

            # If statement to get region of birth
            if int(user_id[7:10]) in range(1, 11):
                bregion = 'Kuressaare haigla'
            elif int(user_id[7:10]) in range(11, 20):
                bregion = 'Tartu Ülikooli Naistekliinik'
            elif int(user_id[7:10]) in range(21, 151):
                bregion = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif int(user_id[7:10]) in range(151, 161):
                bregion = 'Keila haigla'
            elif int(user_id[7:10]) in range(161, 221):
                bregion = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
            elif int(user_id[7:10]) in range(221, 271):
                bregion = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
            elif int(user_id[7:10]) in range(271, 371):
                bregion = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
            elif int(user_id[7:10]) in range(371, 421):
                bregion = 'Narva haigla'
            elif int(user_id[7:10]) in range(421, 471):
                bregion = 'Pärnu haigla'
            elif int(user_id[7:10]) in range(471, 491):
                bregion = 'Haapsalu haigla'
            elif int(user_id[7:10]) in range(491, 521):
                bregion = 'Järvamaa haigla (Paide)'
            elif int(user_id[7:10]) in range(521, 571):
                bregion = 'Rakvere haigla, Tapa haigla'
            elif int(user_id[7:10]) in range(571, 601):
                bregion = 'Valga haigla'
            elif int(user_id[7:10]) in range(601, 651):
                bregion = 'Viljandi haigla'
            elif int(user_id[7:10]) in range(651, 701):
                bregion = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
            else:
                bregion = 'Unknown'

            while True:  # Second cycle, to cycle menu
                user_menu = input("Please choose:\n1.Tell gender:\n"
                                  "2.Tell date of birth\n"
                                  "3.Tell birth region\n"
                                  "4.Validate ID\n5.Change ID\n"
                                  "0.Exit\n--> ")
                if user_menu == '1':
                    if gender != 'Unknown':
                        print(f'Gender: {gender}')
                    else:
                        print('Impossible to determine gender.')
                elif user_menu == '2':
                    if bcent != 'Unknown':
                        print(f'DOB: {bday}.{bmonth}.{bcent + byear}')
                    else:
                        print('Impossible to determine date of birth.')
                elif user_menu == '3':
                    if bregion != 'Unknown':
                        print(f'You were born in {bregion}.')
                    else:
                        print(f'You were not born in Estonia.')
                elif user_menu == '4':
                    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                    result = 0
                    cnt = 0
                    for num in chk1:
                        result += num * int(user_id[cnt])
                        cnt += 1
                    if result % 11 == int(user_id[10]):
                        print('ID is valid!')
                    else:
                        result = 0
                        cnt = 0
                        for num in chk2:
                            result += num * int(user_id[cnt])
                            cnt += 1
                        if result % 11 == int(user_id[10]):
                            print('ID is valid!')
                        else:
                            print('ID is not valid!')
                elif user_menu == '5':  # Return to previous while (enter id)
                    break
                elif user_menu == '0':
                    print('Good bye')
                    quit()  # Use quit() because break will return to previous cycle
                else:
                    print('Choice is out of range!')