from random import randint
c = 0
print('=|='*9)
print('VAMOS JOGAR PAR OU ÍMPAR!!!')
print('=|='*9)
num = int(input('Informe um número de 1 a 10: '))
pi = input('Par ou Ímpar[P/I]? ').strip().upper()[0]
computador = randint(1, 10)
soma = num + computador
while num >= 0:
    if pi == 'P':
        if soma % 2 == 0:
            print('-='*20)
            print(f'Você Jogou {num} e o Computador Jogou {computador}')
            print(f'-'*30)
            print(f'TOTAL = {soma} É PAR VOCÊ VENCEU!')
            print('-=' * 20)
            c += 1
            num = int(input('Informe um número de 1 a 10: '))
            pi = input('Par ou Ímpar[P/I]? ').strip().upper()[0]
            computador = randint(1, 10)
            soma = num + computador
        else:
            print('-='*20)
            print(f'Você Jogou {num} e o Computador Jogou {computador}')
            print(f'-'*30)
            print(f'TOTAL = {soma} É ÍMPAR VOCÊ PERDEU!')
            print('-=' * 20)
            break
    elif pi == 'I':
        if soma % 2 == 0:
            print('-='*20)
            print(f'Você Jogou {num} e o Computador Jogou {computador}')
            print(f'-'*30)
            print(f'TOTAL = {soma} É PAR VOCÊ PERDEU!')
            print('-=' * 20)
            break
        else:
            print('-='*20)
            print(f'Você Jogou {num} e o Computador Jogou {computador}')
            print(f'-'*30)
            print(f'TOTAL = {soma} É ÍMPAR VOCÊ VENCEU!')
            print('-=' * 20)
            c += 1
            num = int(input('Informe um número de 1 a 10: '))
            pi = input('Par ou Ímpar[P/I]? ').strip().upper()[0]
            computador = randint(1, 10)
            soma = num + computador
print(f'GAME OVER! VOCÊ GANHOU {c} VEZES!')
