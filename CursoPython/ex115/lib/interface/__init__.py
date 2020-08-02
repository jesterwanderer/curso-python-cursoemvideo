def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mErro! O Arrombado preferiu não digitar o número.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam


def cab(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cab("MENU PRINCIPAL!")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Digite sua opção: ")
    return opc
