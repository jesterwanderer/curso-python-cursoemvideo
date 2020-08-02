from random import randint
from time import sleep
print('-='*29)
print('Pensei em um número entre 0 e 10 você consegue adivinhar?'.upper())
print('-='*29)
sleep(0.5)
computador = randint(0, 10)
num = int(input('Digite um número: '))
contador = 0
while num != computador:
    contador += 1
    print('ERROOOOOOOOOUUUUUUUUUUUUUUUUU!')
    sleep(0.5)
    num = int(input('Digite um número: '))
print(f'Parabéns eu também pensei no número {computador}!\n'
      f'Você precisou de {contador + 1} tentativas para acertar!')
