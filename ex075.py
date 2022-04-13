n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')

'''v=cont=0
pos = ' '
while v < 4:
    if v==0:
        n1=int(input('Digite um valor: '))
        if n1 == 9:
            cont += 1
        if n1 ==3:
            pos = 0
    if v==1:
        n2=int(input('Digite outro valor: '))
        if n2 == 9:
            cont += 1
        if n2 == 3:
            pos = 1
    if v==2:
        n3=int(input('Digite mais um valor: '))
        if n3 == 9:
            cont += 1
        if n3 == 3:
            pos = 2
    if v==3:
        n4=int(input('Digite o último valor: '))
        if n4 == 9:
            cont += 1
        if n4 == 3:
            pos = 3
    v += 1
tupla = (n1, n2, n3, n4)
print(f'{tupla}')
print(f'O número 9 apareceu {cont} vezes.')'''