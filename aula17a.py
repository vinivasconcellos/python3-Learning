num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
#num.remove(2) #se tem mais de um número, ele remove o primeiro que encontra
if 5 in num:
    num.remove(5)
else:
    print('Não foi encontrado o número 4.')
#num.pop() #elimina o último elemento
#num.pop(3) #elimina o que está na posição 3
print(num)
print(f'Essa lista tem {len(num)} elementos.')
