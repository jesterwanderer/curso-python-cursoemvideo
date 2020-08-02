soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        contador = contador + 1
        soma = c + soma
print(f'Resultado da soma dos {contador} números é = {soma}')
