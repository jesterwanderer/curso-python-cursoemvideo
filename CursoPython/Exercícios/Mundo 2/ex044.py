produto = float(input('Informe o valor do produto: '))
num = int(input('Digite [1] Para pagar a vista no dinheiro\n'
                'Digite [2] Para pagar a vista no cartão\n'
                'Digite [3] Para pagar em 2X no cartão\n'
                'Digite [4] Para pagar em 3X ou mais: '))
if num == 1:
    print(f'Valor a ser pago R$ {produto - ((produto * 10) / 100):.2f}')
elif num == 2:
    print(f'Valor a ser pago R$ {produto - ((produto * 5) / 100):.2f}')
elif num == 3:
    print(f'Valor a ser pago  por parcela R$ {produto / 2:.2f}')
elif num == 4:
    qp = int(input('Quantas parcelas? '))
    print(f'Valor a ser pago por parcela R$ {(produto + ((produto * 20) / 100)) / qp}')
