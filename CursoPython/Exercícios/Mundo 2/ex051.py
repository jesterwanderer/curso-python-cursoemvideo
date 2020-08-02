num = int(input('Informe um número: '))
ra = int(input('Informe a razão: '))
dec = num + (10 - 1) * ra
for c in range(num, dec + ra, ra):
    print(c, end=' > ')
print('FIM')
