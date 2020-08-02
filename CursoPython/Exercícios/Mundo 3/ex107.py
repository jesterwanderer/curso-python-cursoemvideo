import moeda
p = int(input('Informe o preço R$: '))
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, format=True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, format=True)}')
print(f'Reduzindo 27.5% temos {moeda.diminuir(p, 27.5, True)}')
