def teste(b):
    global a
    a = 6
    b += 3
    c = 3
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 2
teste(a)
print(f'A fora vale {a}.')
