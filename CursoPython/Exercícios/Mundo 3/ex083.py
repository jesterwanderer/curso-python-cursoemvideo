ex = input('Informe um número: ')
p = []
for s in ex:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')

'''ex = input('Digite uma expressão: ')
a = ex.count('(')
f = ex.count(')')
if a == f:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')'''
