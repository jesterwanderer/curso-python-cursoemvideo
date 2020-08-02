cidade = input('Informe o nome de alguma cidade: ').strip()
cidades = cidade.upper().split()
print(f'Na cidade informada existe a palavra Santo?\n',
      ('SANTO' in cidades[0]))
