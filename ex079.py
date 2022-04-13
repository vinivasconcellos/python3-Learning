lista = []
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado!')
    else:
        print('Valor já existe! Não será adicionado.')
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'{lista}')
