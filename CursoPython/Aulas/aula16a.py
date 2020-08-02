valores = list()
for c in range(0, 5):
    valores.append(input('Informe um valor: '))
for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}')
print(f'Essa lista contem {len(valores)} valores!')
valores.sort(reverse=True)
task = list(range(5, 31))
print(valores)
print(task)
