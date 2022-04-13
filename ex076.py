listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Mochila', 157.99,
            'Caderno', 14.9,
            'Canetas', 22.30)
print('-'*29)
print(f'{"LISTA DE COMPRAS":^29}')
print('-'*29)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
