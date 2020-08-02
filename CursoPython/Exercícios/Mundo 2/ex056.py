contador = 0
idad = 0
soma = 0
velho = ''
mulheres = 0
for c in range(0, 4):
    nome = input('Informe seu nome: ').title()
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo [M/F]: ').upper()
    soma = idade + soma
    if idade > idad and sexo == 'M':
        idad = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        contador = contador + 1
print(f'A média de idade das pessoas é de {soma / 4} anos.')
print(f' O Homem mais velho se chama {velho}.')
print(f'{contador} Mulher(es) tem menos de 20 anos.')
