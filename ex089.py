alunos = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>9}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>9.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('<<< Volte sempre! >>>')
