def escreva(txt):
    base = '-'*2
    if len(txt) > len(base):
        base = '-'*(len(base) + len(txt))
        print(base)
        print(f' {txt}')
    else:
        print(base)
        print(f' {txt}')


escreva(str(input('Escreva uma frase: ')))
