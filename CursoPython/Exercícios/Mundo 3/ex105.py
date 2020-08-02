def notas(*n, sit=False):
    '''

    -> Dicionário Situacional
    :param n: recebe as notas.
    :param sit: Exibe a situação do aluno (opcional).
    :return: retorna um dicionário com as notas digitadas e a situação do aluno.
    '''

    r = dict()
    r['Quantidade'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)

    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


mostrar = notas(5, 7, 10, sit=True)
print(mostrar)
help(notas)
