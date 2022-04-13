lista = []
resp = 'S'
cont = cont5 = 0
while resp in 'Ss':
    n= int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado')
print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A Lista em ordem decrescente é {lista}')
