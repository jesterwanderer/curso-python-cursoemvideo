soma = c = 0
num = int(input('Informe um número [999 PARA PARAR!]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Informe um número [999 PARA PARAR!]: '))
print(f'Você digitou {c} números e a soma deles é = {soma}')
