def leiaInt(txt):
    ok = False
    while True:
        n = str(input(txt))
        if n.isdigit():
            n = int(n)
            ok = True
        else:
            print('Erro. Digite um número.')
        if ok:
            break
    return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
