num = int(input('Qual Tabuada deseja consultar? '))
print('-='*9)
print(f'  [Tabuada do {num}]'.upper())
print('-='*9)
for c in range(1, 11):
    print(f'| {num:2} X {c:2} = {num * c}')
