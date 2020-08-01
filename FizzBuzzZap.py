def fizz_buzz(x, y):
    string = ''
    for i in range(x, y+1):
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
            string = string + 'FizzBuzzZap' + ' '
        elif i % 24 == 0:
            string = string + 'FizzBuzz' + ' '
        elif i % 4 == 0 and i % 9 == 0:
            string = string + 'FizzZap' + ' '
        elif i % 6 == 0 and i % 9 == 0:
            string = string + 'BuzzZap' + ' '
        elif i % 4 == 0:
            string = string + 'Fizz' + ' '
        elif i % 6 == 0:
            string = string + 'Buzz' + ' '
        elif i % 9 == 0:
            string = string + 'Zap' + ' '
        else:
            string = string + str(i) + ' '
    print(string)

fizz_buzz(1,300)
