maior = 0
menor = 0
for c in range(0, 5):
    num = float(input('Informe seu Peso: '))
    if num > maior:
        maior = num
        menor = num
    if num < menor:
        menor = num
print(f'{maior} É o maior peso.')
print(f'{menor} É o menor peso.')
