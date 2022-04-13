lista = []
menor = maior = me = ma = 0
for pos in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        menor = maior = lista[pos]
#        ma += 1
#        me += 1
    else:
        if lista[pos] > maior:
            maior = lista[pos]
#            ma = pos + 1
        if lista[pos] < menor:
            menor = lista[pos]
#            me = pos + 1
print(f'Lista: {lista}')
print(f'O menor valor foi {menor}, e é encontrado na(s) posição(ões) ', end='')
for pos, v in enumerate(lista):
    if lista[pos] == menor:
        print(f'{pos+1}...', end='')
print(f'\nO maior valor foi {maior}, e é encontrado na(s) posição(ões) ', end='')
for pos, v in enumerate(lista):
    if lista[pos] == maior:
        print(f'{pos+1}...', end='')
