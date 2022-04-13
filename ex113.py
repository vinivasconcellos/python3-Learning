def leiaInt(txt):
    while True:
        try:
            ni = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número Inteiro válido.\033[m')
            continue
        else:
            return ni


def leiaFloat(txt):
    while True:
        try:
            nr = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número real válido.\033[m')
            continue
        else:
            return nr


ni = leiaInt('Digite um número Inteiro: ')
nr = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {ni} e o número real {nr}.')
