from random import shuffle
a1 = input('Informe um nome: ')
a2 = input('Informe outro nome: ')
a3 = input('Informe outro nome: ')
a4 = input('Informe outro nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem das apresentações é: {lista}')
