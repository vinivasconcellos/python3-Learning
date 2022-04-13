def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


valores = [1, 3, 11, 6, 9]
dobra(valores)
print(valores)
