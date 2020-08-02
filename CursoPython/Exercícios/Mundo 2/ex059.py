from time import sleep
op = 0
while op != 5:
    print('+='*13)
    a = int(input('Informe o primeiro número: '))
    b = int(input('Informe o segundo número: '))
    print('''ESCOLHA UMA OPÇÃO:
    [1] PARA SOMAR
    [2] PARA MULTIPLICAR
    [3] EXIBIR O MAIOR
    [4] DIGITAR NOVAMENTE
    [5] PARA SAIR''')
    op = int(input('Informe sua Escolha: '))
    if op == 1:
        print(f'{a} + {b} = {a+b}')
    elif op == 2:
        print(f'{a} X {b} = {a*b}')
    elif op == 3:
        if a > b:
            print(a)
        else:
            print(b)
    elif op == 4:
        op = 0
    elif op == 5:
        print('Finalizando Programa...'.upper(), end='')
        sleep(0.6)
        print(' > ', end=' ')
        sleep(0.6)
        print('*_* Morri!')
