sexo = input('Informe seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dado Inválido, por favor informe seu sexo [M/F]: ').upper()
if sexo == 'M':
    print('Você é do sexo Masculino!')
elif sexo == 'F':
    print('Você é do sexo Feminino!')
