def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Vini Vasconcellos.
    """
    s = a + b + c
    return s


r1 = somar(3, 5, 8)
r2 = somar(1, 8)
r3 = somar(7)
print(f'As somas foram, respectivamente {r1}, {r2} e {r3}.')
