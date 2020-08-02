import random
a1 = input('Informe o nome de um aluno: ')
a2 = input('Informe o nome de outro aluno: ')
a3 = input('Informe o nome de outro aluno: ')
a4 = input('Informe o nome de outro aluno: ')
lista = [a1, a2, a3, a4]
print(f'O escolhido foi {random.choice(lista)}')
