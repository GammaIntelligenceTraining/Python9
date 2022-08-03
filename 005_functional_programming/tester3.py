def fizzbuzz(start_num, stop_num):
    for num in range(start_num, stop_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            if num % 100000 == 0:
                print(num, 'FizzBuzz')
        elif num % 3 == 0:
            if num % 100000 == 0:
                print(num, 'Fizz')
        elif num % 5 == 0:
            if num % 100000 == 0:
                print(num, 'Buzz')

fizzbuzz(int(input('Please enter start number: ')), int(input('Please enter stop number: ')))