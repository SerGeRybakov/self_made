operations = {
    '+': '+',
    '-': '-',
    '*': '*',
    'pow': '**',
    '/': '/',
    'mod': '%',
    'div': '//'
}
try:
    x = float(input('Input first number: '))
    y = float(input('Input second number: '))
    method = input('Input method: ')

    if y == 0 and (method == '/' or method == 'div' or method == 'mod'):
        print('Division by 0!')
    else:
        if method in operations.keys():
            print(f'{eval((str(x)) + operations[method].strip() + str(y))}')
        else:
            while method not in operations.keys():
                print("There's no such method. Methods are:")
                print(*operations.keys())
                method = input('Input method: ')

except ZeroDivisionError:
    print('Division by 0!')



# # Очень короткий вариант
# x, y, action = (input() for _ in '...')
# operations = {"mod": "%", "div": "//", "pow": "**"}
# print(eval("({}) {} {}".format(x, operations.get(action), y)))
