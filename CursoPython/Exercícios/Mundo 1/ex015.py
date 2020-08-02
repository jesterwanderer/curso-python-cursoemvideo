d = int(input('Informe por quantos dias você alugou o carro: '))
km = float(input('Informe quantos km você rodou com o carro: '))
print(f'O preço a pagar pelo aluguel do carro é {(d * 60) + (km * 0.15):.2f}')
