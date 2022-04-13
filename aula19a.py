pessoas = {'nome': 'Vini', 'sexo': 'M', 'idade': 31}
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.values(): #.values e .keys são iguais
#    print(k)
#del pessoas['sexo'] #deletar uma variável
#pessoas['nome'] = 'Leandro' #alterar o nome
pessoas['peso'] = 68.5 #adicionar uma variável
for k, v in pessoas.items():
    print(f'{k} = {v}')