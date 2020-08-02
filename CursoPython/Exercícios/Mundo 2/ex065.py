r = 's'
c = maior = menor = soma = 0
while r == 's':
    num = int(input('Informe um número: '))
    soma += num
    c += 1
    if c == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = input('Deseja continuar[S/N]? ').lower().strip()[0]
print(f'A média de todos os valores é = {soma / c}\n'
      f'O maior número é = {maior}\n'
      f'O menor número é = {menor}\n')

''' num = int(input('Informe um número: '))
contador = 0
soma = 0
while num != 0:
    contador += 1
    soma = num + soma
    num = int(input('Informe um número: '))
print(f'A média dos números digitados é {soma / contador:.1f}')
continuar = (input('Deseja continuar[S/N]? ')).upper()
while continuar == 'S':
    num = int(input('Informe um número: '))
    while num != 0:
        contador += 1
        soma = num + soma
        num = int(input('Informe um número: '))
    print(f'A média dos números digitados é {soma / contador:.1f}')
    continuar = (input('Deseja continuar[S/N]? ')).upper() '''
