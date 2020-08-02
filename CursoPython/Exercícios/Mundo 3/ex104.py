def leiaInt(msg):
    ok = False
    while True:
        num = input(msg)
        if num.isnumeric():
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return num


n = leiaInt('Informe um número: ')
print(f'você acabou de digitar o número: {n}')
