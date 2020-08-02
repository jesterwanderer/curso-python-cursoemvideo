def helping(com):
    help(com)

def tit(msg, cor=0):
    t = len(msg) + 4
    print('~'* t)
    print(f'  {msg}')
    print('~' * t)


# P. Principal
comando = ''
while True:
    tit('SISTEMA DE AJUDA PyHelp')
    comando = input('Função ou Biblioteca >>> ')
    if comando.upper() == 'FIM':
        break
    else:
        helping(comando)
tit('ATÉ LOGO!')
