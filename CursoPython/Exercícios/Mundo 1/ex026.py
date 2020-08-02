frase = input('Digite uma frase: ').upper().strip()
print(f'A letra A aparece', frase.strip().count('A'), 'Vezes na frase')
print('A primeira letra A apareceu na posição', frase.find('A'))
print('A ultima letra A apareceu {}'.format(frase.rfind('A')))
