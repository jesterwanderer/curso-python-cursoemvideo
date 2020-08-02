ficha = {}
ficha['nome'] = input('Informe o nome do aluno: ')
ficha['media'] = float(input('Informe a média do aluno: '))
print(f'Nome do aluno: {ficha["nome"]}')
print(f'Média = {ficha["media"]}')
if ficha['media'] >= 7:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')
