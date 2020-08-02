num = int(input('Digite o número que você quer converter: '))
print(''' Escolha uma das bases para conversão:
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')
opcao = int(input('Informe sua opcão: '))
if opcao == 1:
    print(f'{num} em BINÁRIO é = {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em OCTAL é = {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em HEXADECIMA é = {hex(num)[2:]}')
else:
    print('ERRO')
