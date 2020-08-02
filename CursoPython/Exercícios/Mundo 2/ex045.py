#JOKENPÔ
from time import sleep
from random import randint

print('-*69*'*10)
print('VAMOS JOGAR JOKENPÔ (PEDRA PAPEL TESOURA)?')
print('-*69*'*10)
sino = input('[SIM/NÃO]: ')
if sino.upper() == 'SIM':
    print('PROCESSANDO...')
    sleep(1)

    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(1, 3)
    print('''Suas opções são:
     [1] Pedra
     [2] Papel
     [3] Tesoura''')
    jogador = str(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-='*11)
    print(f'O computador jogou {itens[computador]}')
    print(f'Você jogou {itens[jogador]}')
    print('-='*11)

    if jogador == '1':
        # Pedra
        if computador == 1:
            print('EMPATE')
        elif computador == 2:
            print('VOCÊ PERDEU')
        elif computador == 3:
            print('VOCÊ VENCEU')
        else:
            print('JOGADA INVÁLIDA')

    elif jogador == '2':
        # Papel
        if computador == 1:
            print('VOCÊ VENCEU')
        elif computador == 2:
            print('EMPATE')
        elif computador == 3:
            print('VOCÊ PERDEU')
        else:
            print('JOGADA INVÁLIDA')

    elif jogador == '3':
        # Tesoura
        if computador == 1:
            print('VOCÊ PERDEU')
        elif computador == 2:
            print('VOCÊ VENCEU')
        elif computador == 3:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')
else:
    print('GAME OVER')
