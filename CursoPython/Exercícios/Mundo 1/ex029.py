velocidade = int(input('Informe a velocidade do carro em KM: '))
if velocidade > 80:
    print(f'Você exedeu o limite de velocidade!\n'
          f'E foi MULTADO em R$: {(velocidade - 80) * 7:.2f}')
else:
    print('Você está dentro do limite de velocidade\n'
          'Continue assim e dirija com cuidado!')
