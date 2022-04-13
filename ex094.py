pessoas = {}
dados = []
mulheres = []
p = tidades = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Inválido. Digite somente M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())
    tidades += pessoas['idade']
    p += 1
    media = tidades / p
    while True:
        resp = str(input('Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Inválido. Digite somente S ou N.')
    if resp == 'N':
        break
print(dados)
print(f'Foram cadastradas {p} pessoas.')
print(f'A média de idades das pessoas cadastradas é {media:.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for pes in dados:
    if pes['sexo'] in 'Ff':
        print(f'{pes["nome"]} ', end='')
print()
print('Lista das pessoas que estão com idade acima da média ', end='')
for pes in dados:
    if pes['idade'] > media:
        print(f'{pes["nome"]} com {pes["idade"]} anos ', end='')
print()
