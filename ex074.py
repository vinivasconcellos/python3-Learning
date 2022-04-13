from random import randint
computador = (randint (0, 10), randint (0, 10), randint (0, 10), randint (0, 10), randint (0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in computador:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(computador)}')
print(f'O menor valor sorteado foi {min(computador)}')
