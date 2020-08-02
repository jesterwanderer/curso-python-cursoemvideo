from time import sleep
from random import randint
ms = []
c = int(input('[MEGA SENA] Você quer sortear quantos jogos? '))
a = 1
while a < c + 1:
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in ms:
            ms.append(num)
        else:
            ms.append(randint(1, 60))
    print(f'JOGO {a}: {ms}')
    sleep(0.5)
    ms.clear()
    a += 1
