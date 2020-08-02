num = [[], []]
for c in range(1, 8):
    n = int(input(f'Informe o {c}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Lista de números pares: {sorted(num[0])}')
print(f'Lista de números ímpares: {sorted(num[1])}')
