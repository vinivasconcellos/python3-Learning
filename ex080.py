lista = []
for pos in range (0, 5):
    n = int(input('Digite um valor: '))
    if pos == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor {lista[pos]} foi adicionado na posição {pos} da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor {lista[pos]} foi adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Lista: {lista}')
