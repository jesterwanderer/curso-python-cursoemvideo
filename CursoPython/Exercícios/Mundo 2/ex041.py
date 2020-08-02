from datetime import date
ano = int(input('Em que ano você nasceu? '))
anoAtual = date.today().year
idade = anoAtual - ano
if idade <= 9:
    print('MIRIM')
elif 10 <= idade <= 14:
    print('INFANTIL')
elif 15 <= idade <= 19:
    print('JÚNIOR')
elif 20 <= idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
