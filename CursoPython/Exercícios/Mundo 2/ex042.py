lada = float(input('Informe o tamanho de um lado do triângulo: '))
leda = float(input('Informe o tamanho de outro lado do triângulo: '))
lida = float(input('Informe o tamanho de outro lado do triângulo: '))

if lada + leda > lida and leda + lida > lada and lida + lada > leda:
    if lada == leda and leda == lida and lida == lada:
        print('EQUILÁTERO')
    elif lada == leda or leda == lida or lida == lada:
        print('ISÓSCELES')
    elif lada != leda and leda != lida and lida != lada:
        print('ESCALENO')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO COM OS LADOS APRESENTADOS')
