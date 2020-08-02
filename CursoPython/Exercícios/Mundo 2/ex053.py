frase = input('Escreva uma frase: ').replace(' ', "").upper()
invertido = frase[::-1]
if frase == invertido:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
