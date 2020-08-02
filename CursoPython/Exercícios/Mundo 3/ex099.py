from time import sleep
def maior():
    while True:
        m = 0
        valores = list()
        print('+~' * 20)
        while True:
            v = int(input('Informe um valor: '))
            valores.append(v)
            if v > m:
                m = v
            while True:
                cn = input('Deseja continuar [S/N]? ').upper()[0]
                print('+~' * 20)
                if cn in 'SN':
                    break
                print('Erro! Digite apenas S ou N.')
            if cn in 'N':
                break
        print('Analisando os Valores informados...')
        sleep(0.5)
        for c in valores:
            print(c, end=' ')
            sleep(0.3)
        print(f'Foram informados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {m}.')
        print('+~' * 20)
        while True:
            cn = input('Deseja continuar [S/N]? ').upper()[0]
            print('+~' * 20)
            if cn in 'SN':
                break
            print('Erro! Digite apenas S ou N.')
        if cn in 'N':
            break

maior()
