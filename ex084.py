pessoas = []
np = []
resp = 'S'
contp = maior = menor = 0
while resp in 'Ss':
    np.append(str(input('Nome: ')))
    contp += 1
    np.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = np[1]
    else:
        if np[1] > maior:
            maior = np[1]
        if np[1] < menor:
            menor = np[1]
    pessoas.append(np[:])
    np.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(np)
print(f'Foram cadastradas {contp} pessoas.')
print(f'O maior peso foi de {maior} kgs. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor} kgs. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
