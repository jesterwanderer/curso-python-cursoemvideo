from time import sleep
def contador():
    print('+~'*20)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11, 1):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')
    print('+~' * 20)
    print('Contadem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')
    print('+~' * 20)
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('+~' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
    else:
        while i > f:
            print(i, end=' ')
            sleep(0.3)
            i -= p
    print('FIM!')
    print('+~' * 20)


contador()
