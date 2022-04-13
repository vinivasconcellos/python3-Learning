import moeda

num = float(input('Digite um valor: R$'))
taxa = float(input('Qual a taxa de aumento e desconto: '))
print(f'Com aumento de {taxa}%, o valor final fica {moeda.moeda(moeda.a(num, taxa))}')
print(f'O valor com desconto de {taxa}% sai por {moeda.moeda(moeda.d(num, taxa))}')
print(f'O dobro do valor é {moeda.moeda(moeda.do(num))}.')
print(f'Metade do preço é {moeda.moeda(moeda.m(num))}')
