n = list()
p = list()
i = list()
while True:
    num = int(input('Informe um número: '))
    n.append(num)
    continuar = input('Deseja continuar? [S/N] ')
    while continuar not in 'SnNs':
        continuar = input('Deseja continuar? [S/N] ').strip()
    if continuar in 'Nn':
        break
for c in range(0, len(n)):
    if n[c] % 2 == 0:
        p.append(n[c])
    else:
        i.append(n[c])
print('-='*30)
print(f'A lista completa é {n}')
print(f'A lista de pares é {p}')
print(f'A lista de impares é {i}')
print(f'-='*30)
