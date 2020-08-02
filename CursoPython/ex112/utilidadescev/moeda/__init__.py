def metade(n, format=False):
    m = n / 2
    if format:
        m = f'{m:.2f}'
        return m
    else:
        return m


def dobro(n, format=False):
    d = n * 2
    if format:
        d = f'{d:.2f}'
        return d
    else:
        return d


def aumentar(n, a, format=False):
    m = n + ((n * a) / 100)
    if format:
        m = f'{m:.2f}'
        return m
    else:
        return m


def diminuir(n, d, format=False):
    m = n - ((n * d) / 100)
    if format:
        m = f'{m:.2f}'
        return m
    else:
        return m


def moeda(n):
    m = f'{n:.2f}'
    return m

def titulo(msg):
    t = len(msg) + 4
    print('~'*t)
    print(f'  {msg}')
    print('~' * t)


import moeda
def resumo(a, b, c):
    print(f'{titulo("RESUMO DO VALOR")}')
    print(f'Preço Analisado:     R${a:.2f}'. replace('.', ','))
    print(f'Dobro do preço:      R${moeda.dobro(a, True)}'. replace('.', ','))
    print(f'Metade do preço:     R${moeda.metade(a, True)}'. replace('.', ','))
    print(f'{b}% de Aumento:      R${moeda.aumentar(a, b, True)}'.replace('.', ','))
    print(f'{c}% de Redução:      R${moeda.diminuir(a, c, True)}'. replace('.', ','))
