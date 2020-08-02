pessoa = {}
galera = []
mulheres = []
soma = 0
while True:
    pessoa['nome'] = input('Informe um nome: ')
    while True:
        pessoa['sexo'] = input('Informe seu sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F!')
    pessoa['idade'] = int(input('Informe sua idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        cn = input('Deseja continuar? ').upper()[0]
        if cn in 'SN':
            break
        print('Resposta Inválida, Digite apenas S ou N!')
    if cn in 'N':
        break
media = soma / len(galera)
print('+='*30)
print(f'{len(galera)} pessoas foram cadastradas.')
print(f'A média das idades é de {media} anos.')
for p in galera:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
print(f'Mulheres cadastradas: {mulheres}')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} => {v};', end=' ')
        print()
print(f'=+=+=+FINISH+=+=+=')
