# Empréstimo bancário
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Informe seu salário: '))
tempo = float(input('Em quantos anos você pretende pagar esse empréstimo? '))
prestacao = casa / (tempo * 12)
if prestacao <= (salario * 30) / 100:
    print(f'Parabéns o seu empréstimo foi aprovado!\n'
          f'O valor mensal da prestação será de R$ {prestacao:.2f}')
else:
    print('O Valor do empréstimo exede 30% do seu salário mensal.\n'
          'EMPRÉSTIMO NEGADO!!!')
    print(f'O valor da prestação seria R$ {prestacao}')
