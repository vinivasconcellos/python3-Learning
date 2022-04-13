def ficha(j='', g=''):
    if j == '':
        j = '<desconhecido>'
    if not g.isdigit():
        g = 0
    print(f'O Jogador {j} fez {g} gol(s).')


j = str(input('Nome do jogador: ')).capitalize()
g = str(input('Quantos gols: '))
ficha(j, g)
