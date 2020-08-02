def ficha(nome=0, gols=0):
    from time import sleep
    print('+='*20)
    nome = input('Nome do jogador: ')
    if len(nome) == 0:
        nome = 'Desconhecido'
    gols = input('Número de gols: ')
    if len(gols) == 0:
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato. '


print(ficha())
