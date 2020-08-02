def leiaint(msg):
    ok = False
    while True:
        num = input(msg).strip()
        if num.isnumeric():
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return num


numi = leiaint('Digite um número Inteiro: ')
numr = leiafloat('Digite um número Real: ')
print(f'Você digitou {numi} e {numr}')
