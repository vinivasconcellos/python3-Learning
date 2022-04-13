aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'em Recuperação'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
print(f'O aluno {aluno["nome"]} teve média {aluno["media"]}, e está {aluno["situacao"]}.')

'''aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    print('Aluno aprovado.')
elif aluno['media'] >= 5 and aluno['media'] < 7:
    print('Aluno em recuperação.')
elif aluno['media'] < 5:
    print('Aluno reprovado.')
print(f'O aluno {aluno["nome"]} teve média {aluno["media"]}.')'''
