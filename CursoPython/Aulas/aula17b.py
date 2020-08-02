nomes = []
while True:
    nomes.append(input('Informe um nome: '))
    cn = input('Deseja continuar? [S/N]')
    while cn not in 'SsNn':
        cn = input('Deseja continuar? [S/N]')
    if cn in 'Nn':
        break
for p, n in enumerate(nomes):
    print(f'O nome {n} está na posição {p}')