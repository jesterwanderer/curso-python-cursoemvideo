def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Você tem {idade} anos, Voto: NEGADO!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Você tem {idade} anos, Voto: OPCIONAL!'
    else:
        return f'Você tem {idade} anos, Voto: OBRIGATÓRIO!'


na = int(input('Ano de nascimento: '))
print(voto(na))
