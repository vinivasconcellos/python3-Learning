def notas(*n, sit=False):
    """
    -> Notas dos alunos
    :param q: quantidade de notas
    :param ma: maior nota
    :param me: menor nota
    :param m: média das notas
    :param sit: (opcional) situação: Ruim, Mediano, Muito bom
    :return: dicionário com várias informações do aluno
    """
    r = {}
    r['quantidade'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 5:
            r['situação'] = 'Ruim'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'Mediano'
        elif 7 <= r['média'] < 8.5:
            r['situação'] = 'Bom'
        else:
            r['situação'] = 'Muito Bom!'
    return r


resp = notas(8.5, 8, 8.5, 10, sit=True)
print(resp)
help(notas)

'''def notas(*n, sit=False):
    """
    -> Notas dos alunos
    :param q: quantidade de notas
    :param ma: maior nota
    :param me: menor nota
    :param m: média das notas
    :param sit: (opcional) situação: Ruim, Mediano, Muito bom
    :return: dicionário com várias informações do aluno
    """
    na = []
    c = 0
    for c in range(0, q):
            n = int(input('Nota: '))
            na.append(n)
            c += 1
    r = {}
    r['quantidade'] = len(na)
    r['maior'] = max(na)
    r['menor'] = min(na)
    r['média'] = sum(na)/len(na)
    if sit:
        if r['média'] < 5:
            r['situação'] = 'Ruim'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'Mediano'
        else:
            r['situação'] = 'Muito bom'
    return r


q = int(input('Quantidade de notas: '))
#notas={'quantidade', 'maior', 'menor', 'média', sit=True}
#print(na)
#help(notas)'''
