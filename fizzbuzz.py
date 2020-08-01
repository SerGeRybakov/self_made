def fizz_buzz(x, y):
    string = ''
    for i in range(x, y+1):
        if i % 15 == 0:
            string = string + 'FizzBuzz' + ' '
        elif i % 3 == 0:
            string = string + 'Fizz' + ' '
        elif i % 5 == 0:
            string = string + 'Buzz' + ' '
        else:
            string = string + str(i) + ' '
    print(string)

fizz_buzz(1,100)
