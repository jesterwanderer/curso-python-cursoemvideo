jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = input('Informe o nome do jogador: ')
    pt = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, pt):
        partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        cn = input('Deseja continuar [S/N]? ').strip().upper()[0]
        if cn in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if cn == 'N':
        print('+='*30)
        break
print('Nº:    ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end=' ')
print()
print('_-'*26)
for i, v in enumerate(time):
    print(f'{i+1:>3}      ', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('_-'*26)
while True:
    b = int(input('Informe o Nº do jogador [999 PARA]: ')) - 1
    if b == 998:
        break
    if b >= len(time):
        print(f'ERRO! Jogador {b+1} não existe!')
    else:
        print(f'LEVANTAMENTO do Jogador {time[b]["nome"]}')
        for i, v in enumerate(time[b]["gols"]):
            print(f'   => No {i+1}º jogo, fez {v} gols.')
        print('-=' * 30)
print('+='*30)
