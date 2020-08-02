num = (int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')))
print(f'Os números digitados foram: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na  {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado!')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

