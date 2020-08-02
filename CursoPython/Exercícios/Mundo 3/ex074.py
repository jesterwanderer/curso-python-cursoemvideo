from random import randint, sample
# num = tuple(sample(range(10), 5))
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {num}')
print(f'O maior número é: {max(num)}')
print(f'O menor número é: {min(num)}')
