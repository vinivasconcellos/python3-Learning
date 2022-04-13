a = [2, 3, 4, 7]
#b = a #se deixar só assim, se fizer alguma alteração em b, ele muda em a, pois eles ficam ligados pra sempre
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
