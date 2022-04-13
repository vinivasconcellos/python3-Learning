def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = int(input('Digite um número: '))
f2 = int(input('Digite um número: '))
f3 = int(input('Digite um número: '))
print(f'Os fatoriais de {f1}, {f2} e {f3} são respectivamente {fatorial(f1)}, {fatorial(f2)} e {fatorial(f3)}.')
