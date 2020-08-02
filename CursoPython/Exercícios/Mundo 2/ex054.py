from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(0, 7):
    num = int(input('Informe o ano de nascimento: '))
    if ano - num >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} Pessoas são maiores de idade\n'
      f'{menor} Pessoas são menores de idade\n')
