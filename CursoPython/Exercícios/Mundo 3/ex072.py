num = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    n = int(input('Informe um número de 0 a 20: '))
    while n not in range(0, 21):
        n = int(input('[ERRO]Informe um número de 0 a 20: '))
    print(f'Você digitou o número {num[n]}!')
