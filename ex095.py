jogador = {}
golsp = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    n = 0
    while n < partidas:
        golsp.append(int(input(f'Quantidade de Gols na partida {n+1}: ')))
        n += 1
    jogador['gols'] = golsp[:]
    jogador['total'] = sum(golsp)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Inválido. Informe S ou N.')
    golsp.clear()
    if resp == 'N':
        break
print(time)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    levant = int(input('Quer mostrar os dados de qual jogador? (999 para parar): '))
    if levant == 999:
        break
    if levant >= len(time):
        print(f'Erro, não existe jogador com código {levant}')
    else:
        print(f'---Levantamento do jogador {time[levant]["nome"]}---')
        for i, g in enumerate(time[levant]['gols']):
            print(f'-> Na partida {i+1}, fez {g} gols.')
    print()
print('Volte sempre!')

'''while True:
    
    for i, v in enumerate(time['gols']):
        print(f'Na partida {i}, fez {v} gols.')
#for k, v in jogador.items():
 #   print(f'O {k} é {v}.')
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas, fazendo {golsp} gols, respectivamente em cada, com um total de {jogador["total"]} gols.')
#for i, v in enumerate(jogador['gols']):
#    print(f'Na partida {i}, fez {v} gols.')
#print(f'Foi um total de {jogador["total"]} gols.')
'''