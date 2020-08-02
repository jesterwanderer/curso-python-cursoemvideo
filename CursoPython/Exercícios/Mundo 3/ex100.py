from random import randint
from time import sleep
sorteados = []
spl = []
def sorteia():
    r = 0
    for c in range(0, 5):
        r = randint(0, 10)
        sorteados.append(r)
    print('Valores sorteados: ', end=' ')
    for c in sorteados:
        print(c, end=' ')
        sleep(0.5)
def somaPar():
    sp = 0
    for c in sorteados:
        if c % 2 == 0:
            spl.append(c)
            sp += c
    print(f'Somando os valores pares de {sorteados} que são {spl}, temos {sp}')


sorteia()
print()
somaPar()
