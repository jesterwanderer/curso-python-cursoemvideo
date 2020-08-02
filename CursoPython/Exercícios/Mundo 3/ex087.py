matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
print('=+'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('+='*30)
print(f'A soma dos pares = {soma}')
print(f'A soma dos valores da terceira coluna = {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior número da segunda linha é {maior}')
