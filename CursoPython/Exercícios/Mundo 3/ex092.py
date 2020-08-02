import datetime
ficha = {}
ficha['nome'] = input('Informe o seu nome: ')
ficha['idade'] = datetime.date.today().year - int(input('Informe seu ano de nascimento: '))
ficha['CTPS'] = int(input('Carteira de Trabalho [Digite 0 se não possuir]:  '))
if ficha['CTPS'] != 0:
    ficha['anoc'] = int(input('Informe seu ano de contratação: '))
    ficha['salario'] = float(input('Informe seu salário: '))
    ia = (datetime.date.today().year - ficha['anoc']) + 35
    ficha['aposentadoria'] = ia
    print(ficha)
    print(f'Seu nome é {ficha["nome"]}.')
    print(f'Você terá {ficha["idade"]} anos até o final deste ano.')
    print(f'Seu CTPS tem o valor: {ficha["CTPS"]}.')
    print(f'Seu salário é de R$ {ficha["salario"]}.')
    print(f'Você se aposentará aos {ficha["aposentadoria"]} anos.')
else:
    print(ficha)
    print(f'Seu nome é {ficha["nome"]}.')
    print(f'Você terá {ficha["idade"]} anos até o final deste ano.')
    print(f'Seu CTPS tem o valor: {ficha["CTPS"]}.')
