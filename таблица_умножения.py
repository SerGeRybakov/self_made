"""Multiplication table"""


x1 = int(input('Input lines first number: '))
x2 = int(input('Input lines last number: '))
y1 = int(input('Input columns first number: '))
y2 = int(input('Input columns last number: '))

# Making Y-headers in the first line of table
field = y1 - 1
while field <= y2:
    if field < y1:
        print(end='\t')
        field += 1
    else:
        print(field, end='\t')
        field += 1
else:
    print()

# Making lines with results. First row is made of X-headers.
for x in range(x1, x2 + 1):
    print(x, end='\t')
    for y in range(y1, y2 + 1):
        z = x * y
        print(z, end='\t')
    print()
