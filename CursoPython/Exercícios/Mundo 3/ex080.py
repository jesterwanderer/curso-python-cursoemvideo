lista = []
for c in range(0, 5):
    n = int(input('Informe um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adiconado no final da lista!')
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                print(f'Adiconado na posição {p} da lista!')
                break
            p += 1
print('-='*30)
print(f'Os números em ordem ficam assim: {lista}')
