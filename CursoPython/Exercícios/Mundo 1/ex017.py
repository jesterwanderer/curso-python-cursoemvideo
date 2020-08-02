import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
h = math.hypot(co, ca)
print(f'A hipotenusa vale {h:.2f}')
