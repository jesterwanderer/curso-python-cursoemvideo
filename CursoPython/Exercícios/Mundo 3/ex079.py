lista = list()
while True:
    num = int(input('Informe um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número Duplicado não vou adicionar!')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in 'SnNs':
        continuar = input('Deseja continuar? [S/N]').strip().upper()
    if continuar in 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(lista)}')
