print('-='*20)
print('ANALISADOR DE TRIÂNGULOS!')
print('-='*20)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Seguimento: '))
c = float(input('Terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('UM TRIÂNGULO PODE SER FORMADO!')
else:
    print('UM TRIÂNGULO NÃO PODE SER FORMADO!')
