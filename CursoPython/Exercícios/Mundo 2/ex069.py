maior = 0
mmenor = 0
h = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
    continuar = input('Deseja continuar[S/N]? ').strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mmenor += 1
    if continuar == 'N':
        break
print('=-'*10, 'FIM DO PROGRAMA', '=-'*10)
print(f'Total de pessoas maiores de 18 anos: {maior}\n'
      f'Ao todo temos {h} Homens Cadastrados\n'
      f'E temos {mmenor} Mulheres com menos de 20 anos.')
