dados = list()
info = list()
maior = menor = 0
while True:
    dados.append(input('Informe seu nome: '))
    dados.append(int(input('Informe seu peso: ')))
    if len(info) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    info.append(dados[:])
    dados.clear()
    cn = input('Deseja continuar? [S/N] ')
    if cn in 'Nn':
        break
    elif cn not in 'Ss':
        cn = input('Deseja continuar? [S/N] ')
print(f'{len(info)} Pessoas foram cadastradas!')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in info:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for p in info:
    if p[1] == menor:
        print(p[0], end=' ')
