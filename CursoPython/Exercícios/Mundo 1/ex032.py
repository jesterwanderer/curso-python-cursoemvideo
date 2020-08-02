from datetime import date
ano = int(input('Informe o ano que quer analizar!\n'
                'Informe [0] caso seja o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é BISSEXTO!')
else:
    print('O ano não é BISSEXTO!')
