total = milmais = menor = c = 0
barato = ''
while True:
    nome = (input('Informe o nome do produto: '))
    valor = float(input('Informe o preço do produto: '))
    c += 1
    total += valor
    if valor >= 1000:
        milmais += 1
    if c == 1 or valor < menor:
        menor = valor
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar[S/N]? ').strip().upper()[0]
    if continuar == 'N':
            break
print('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {total}')
print(f'Observamos {milmais} Produtos custando mais de R$ 1000')
print(f'{nome} foi o produto mais barato e custou R$ {menor}')
