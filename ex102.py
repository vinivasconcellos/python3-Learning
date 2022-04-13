def fatorial(num, show=False):
    """
    -> Cálculo de Fatorial
    :param num: número qualquer a calcular o fatorial
    :param show: (opcional) mostrar a conta
    :return: mostra o valor do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = {fatorial(num)}', end='')
        f *= c
    return f


#Main Program
help(fatorial)
num = int(input('Digite um número: '))
print(f'\nO fatorial de {num} é {fatorial(num, True)}.')
