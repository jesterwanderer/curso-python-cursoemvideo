pp = ('Celular', 2000,
      'Televisão', 4000,
      'Copo', 20)

for p in range(0, len(pp)):
    if p % 2 == 0:
        print(f'{pp[p]:.<30} R$ ', end='')
    else:
        print(f'{pp[p]:.2f}')
