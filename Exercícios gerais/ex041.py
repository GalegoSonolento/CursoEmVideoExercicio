from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você é um nadador mirim')
elif idade <= 14:
    print('Você é um nadador infantil')
elif idade <= 19:
    print('Você é um nadador júnior')
elif idade <= 25:
    print('Você é um nadador sênior')
elif idade > 25:
    print('Você um MASTER nadador')