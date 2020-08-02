lista = list()
while True:
    valor = int(input('Informe um valor: '))
    lista.append(valor)
    continuar = input('Deseja continuar? [S/N]').strip()[0]
    while continuar not in 'SnNs':
        continuar = input('Deseja continuar? [S/N]')
    if continuar in 'Nn':
        break
print('-='*30)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
