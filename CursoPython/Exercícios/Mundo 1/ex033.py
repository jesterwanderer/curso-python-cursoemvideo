a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

maior = a
menor = a

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
