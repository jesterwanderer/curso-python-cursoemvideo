salario = float(input('Informe o seu salário: '))
if salario > 1250:
    print(f'Parabéns você recebeu um aumento de 10%\n'
          f'O seu salário passa de R$ {salario:.2f} para R$ {((salario * 10) / 100) + salario:.2f}')
else:
    print(f'Parabéns você recebeu um aumento de 15%\n'
          f'O seu salário passa de R$ {salario:.2f} para R$ {((salario * 15) / 100) + salario:.2f}')
