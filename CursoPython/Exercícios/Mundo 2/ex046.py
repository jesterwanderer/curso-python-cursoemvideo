from time import sleep
print('-='*18)
print('Os fogos começarão em 10 Segundos!!!'.upper())
print('-='*18)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('POW! '*5)
for pow in range(0, 5):
    print('* '*10)
    sleep(0.3)
    print(' *'*10)
    sleep(0.2)
    print('* '*10)
    sleep(0.3)
    print('# '*10)
