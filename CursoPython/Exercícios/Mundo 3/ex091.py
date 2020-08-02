from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for c in range(0, 4):
    jogo[f'jogador{[c+1]}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('+='*30)
print('=+=+==+=+==+=+= RANKING =+=+==+=+==+=+=')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}º Lugar foi o {v[0]} que tirou {v[1]}')
    sleep(0.5)
