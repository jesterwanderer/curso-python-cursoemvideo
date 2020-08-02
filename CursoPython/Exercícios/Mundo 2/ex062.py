from time import sleep
num = int(input('Informe um número: '))
razao = int(input('Informe a razão: '))
c = 10
b = 10
print(num, end=' > ')
while c != 1:
    c -= 1
    print(num + razao, end=' > ')
    num = num + razao
v = int(input(' Deseja mostrar mais quantos termos? '))
while v != 0:
    if v != 0:
        c = v
        while c != 0:
            c -= 1
            print(num + razao, end=' > ')
            num = num + razao
            b += 1
        v = int(input(' Deseja mostrar mais quantos termos? '))
print(f'{b} Termos foram mostrados. FIM!')
