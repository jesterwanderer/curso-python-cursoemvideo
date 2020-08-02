from time import sleep
boletim = list()
while True:
    nome = input('Informe seu nome: ')
    nota1 = int(input('Informe a primeira nota: '))
    nota2 = int(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    cn = input('Deseja continuar? [S/N] ')
    if cn in 'Nn':
        break
print('-='*20)
print('Nº       NOME        MÉDIA')
print('-='*20)
for i, v in enumerate(boletim):
    print(f'{i + 1}        {v[0]}         {v[2]}')
while True:
    op = int(input('Deseja mostrar a nota de qual aluno? [999 Interrompe]'))
    if op == 999:
        break
    if op <= len(boletim) -1:
        print(f'As notas de {boletim[op][0]} são {boletim[op][1]}')
