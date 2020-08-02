num = int(input('Informe um número: '))
c = soma = 0
while num != 999:
    if num == 999:
        break
    else:
        soma += num
        c += 1
        num = int(input('Informe um número: '))
print(f'{c} Números foram digitados\n'
      f'O resultado da soma foi = {soma}')
