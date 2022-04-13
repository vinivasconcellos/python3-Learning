def ParImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if ParImpar(num):
    print('É PAR!')
else:
    print('É ÍMPAR!')
