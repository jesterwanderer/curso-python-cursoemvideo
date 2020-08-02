while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        print('*_* Morri!')
        break
    print('=~' * 6)
    for c in range(0, 10):
        c += 1
        print(f'{c} X {num} = {c*num}')
    print('=~' * 6)
