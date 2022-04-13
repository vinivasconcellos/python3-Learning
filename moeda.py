def a(n = 0, tax = 0, formato=False):
    a = n * (1 + (tax/100))
    return a if formato is False else moeda(a)


def d(n = 0, tax = 0, formato=False):
    d = n * (1 - (tax/100))
    return d if formato is False else moeda(d)


def do(n = 0, formato=False):
    do = n * 2
    return do if formato is False else moeda(do)


def m(n = 0, formato=False):
    m =  n / 2
    return m if formato is False else moeda(m)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

