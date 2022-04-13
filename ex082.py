lista = []
listap = []
listai = []
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp == 'Nn':
        break
print(f'A lista é {lista}.')
listap.sort()
print(f'A lista somente com os valores pares é {listap}.')
listai.sort()
print(f'A lista somente com os valores ímpares é {listai}')
