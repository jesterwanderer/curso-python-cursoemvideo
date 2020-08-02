produto = int(input('Informe o preço do produto: '))
print(f'O produto custava R$: {produto}\n'
      f'Mas agora com o desconto de 5% custa R$: {produto - ((produto * 5) / 100)}')
