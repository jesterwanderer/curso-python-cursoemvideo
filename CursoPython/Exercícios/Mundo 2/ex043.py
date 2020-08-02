# CALCULADORA IMC
peso = float(input('Informe seu peso em KG: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura * altura)
print(f'Seu IMC é = {imc}')
if imc < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= imc <= 25:
    print('Peso Ideal!')
elif 25 <= imc <= 30:
    print('Sobrepeso!')
elif 30 <= imc <= 40:
    print('Obesidade!!')
else:
    print('Obesidade Mórbida!!!')
