from math import factorial
n = int(input('Informe um número: '))
c = n
f = 1
print(f'{n}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)
print(factorial(n))
# FAZER COM FOR
