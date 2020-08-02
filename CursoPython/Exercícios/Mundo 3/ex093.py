jogador = dict()
gols = list()
total = 0
jogador['nome'] = input('Informe o nome do jogador: ')
partidas = int(input('Quantas paridas ele jogou? '))
for c in range(0, partidas):
    ng = int(input(f'Quantos gols na {c+1}ª partida? '))
    gols.append(ng)
    total += ng
jogador['gols'] = gols
jogador['total'] = total
print('+='*30)
print(jogador)
print('+='*30)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}.')
print('+='*30)
print(f'O JOGADOR {jogador["nome"]} JOGOU {partidas} partidas.')
for c in range(0, partidas):
    print(f'=> Na partida {c+1}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador["total"]} gols!')
