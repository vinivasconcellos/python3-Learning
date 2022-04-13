jogador = {}
golsp = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
n = g = 0
while n < partidas:
    golsp.append(int(input(f'Quantidade de Gols na partida {n+1}: ')))
    n += 1
jogador['gols'] = golsp[:]
jogador['total'] = sum(golsp)
print(jogador)
for k, v in jogador.items():
    print(f'O {k} é {v}.')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas, fazendo {golsp} gols, respectivamente em cada, com um total de {jogador["total"]} gols.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
