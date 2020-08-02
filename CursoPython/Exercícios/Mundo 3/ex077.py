palavras = ('Amora', 'Abacaxi', 'Abacate', 'Melancia', 'Laranja', 'Uva')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeio':
            print(letra.lower(), end=' ')
