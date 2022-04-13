import moeda

num = float(input('Digite um valor: R$'))
taxa = float(input('Qual a taxa de aumento e desconto: '))
a = moeda.a(num, taxa)
print(f'Com aumento de {taxa}%, o valor final fica R$ {a:.2f}')
d = moeda.d(num, taxa)
print(f'O valor com desconto de {taxa}% sai por R$ {d:.2f}')
do = moeda.do(num)
print(f'O dobro do valor é R$ {do:.2f}.')
m = moeda.m(num)
print(f'Metade do preço é R$ {m:.2f}')
