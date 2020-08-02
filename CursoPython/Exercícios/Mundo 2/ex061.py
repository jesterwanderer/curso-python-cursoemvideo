num = int(input('Informe um número: '))
razao = int(input('Informe a razão: '))
c = 10
print(f'{num} > ', end='')
while c != 1:
    c -= 1
    print(num + razao, end=' > ')
    num = num + razao
print('ACABOU!')
