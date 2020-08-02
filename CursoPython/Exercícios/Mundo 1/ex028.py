import random
from time import sleep
print('--==+=='*10)
print('Vou pensar em um número entre 0 e 5, Tente adivinhar!'.upper())
print('--==+=='*10)
nump = random.randint(0, 5)
numc = int(input('EM QUE NÚMERO EU PENSEI? '))
print('PROCESSANDO...')
sleep(2)
if numc == nump:
    print('Parabéns você acertou!!!'.upper())
else:
    print(f'HA!HA!HA! VOCÊ ERROU EU PENSEI NO NÚMERO {nump} NÃO NO {numc}\n'
          f'BOA SORTE NA PRÓXIMA!')
