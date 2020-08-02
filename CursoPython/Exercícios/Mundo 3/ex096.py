def area():
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    print(f'A área do terreno {l} x {c} é de {l*c}m².')


print('Controle de terrenos'.upper())
print('+='*20)
area()
