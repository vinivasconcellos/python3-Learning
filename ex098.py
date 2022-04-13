from time import sleep
def contador(i, f, p):
    while True:
        if p < 0:
            print('O Passo não pode ser zero!')
            print('Informe novamente o Passo.')
            p = int(input('Passo: '))
        elif p == 0:
            print('O Passo não pode ser zero!')
            print('Informe novamente o Passo.')
            p = int(input('Passo: '))
        else:
            break
    print()
    print(f'Contando de {i} até {f}, de {p} em {p}:')
    sleep(0.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p


contador(1, 10, 1)
contador(10, 0, 2)
print()
print('Agora é a sua vez de personalizar a contagem!')
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i, f, p)
