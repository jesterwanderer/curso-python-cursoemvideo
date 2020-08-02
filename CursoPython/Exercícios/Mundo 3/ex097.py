def escrevi(msg):
    t = len(msg) + 4
    print('+'*t)
    print(f'  {msg}')
    print('+' *t)

def escreva():
    while True:
        txt = input('Escreva algo: ').upper()
        print('~'*len(txt))
        print(txt)
        print('~' * len(txt))
        while True:
            cn = input('Deseja continuar? ').upper()
            if cn in 'SN':
                break
            print('ERRO! Digite apenas S ou N.')
        if cn == 'N':
            print('~' *13)
            print('ACABOU O CAÔ')
            print('~' *13)
            break


escreva()
escrevi('WubbaLubbaDubDub')
