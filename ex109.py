import moeda

num = float(input('Digite um valor: R$'))
taxa = float(input('Qual a taxa de aumento e desconto: '))
print(f'Com aumento de {taxa}%, o valor final fica {moeda.a(num, taxa, True)}')
print(f'O valor com desconto de {taxa}% sai por {moeda.d(num, taxa, True)}')
print(f'O dobro do valor é {moeda.do(num, True)}.')
print(f'Metade do preço é {moeda.m(num, True)}')
