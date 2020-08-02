from datetime import date
ano = int(input('Informe o ano que você nasceu: '))
anoAtual = date.today().year
idade = anoAtual - ano
if idade < 18:
    quantidade = 18 - idade
    print(f'Você deverá se alistar daqui a {quantidade} anos!')
elif idade == 18:
    print('Você deverá se alistar este ano!')
else:
    quantidade = idade - 18
    print('O periodo do seu alistamento já passou!\n'
          f'Você está {quantidade} anos atrasado!\n'
          f'PAGUE {quantidade * 10} FLEXÕES IMEDIATAMENTE!!!')
