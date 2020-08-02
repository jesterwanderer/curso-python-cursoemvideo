dados = []
info = []
tmaior = tmenor = 0
while True:
    dados.append(input('Informe o nome do jogador: '))
    dados.append(int(input('Informe a idade do jogador: ')))
    info.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar? [S/N]')[0]
    if continuar in 'Nn':
        break
    elif continuar not in 'Ss':
        continuar = input('Deseja continuar? [S/N]')
for c in info:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade!')
        tmaior += 1
    else:
        print(f'{c[0]} é menor de idade!')
        tmenor += 1
