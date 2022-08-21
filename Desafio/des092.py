# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['ctps'] = str(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != '0':
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - dados['nascimento']
print('-=' * 30)
for k, v in dados.items():
    if k == 'contratacao':
        print(f'    - {k} foi em {v}')
    elif k == 'salario':
        print(f'    - O montante de {k} é {v}')
    elif k == 'aposentadoria':
        print(f'    - A {k} será com {v} anos')
    else:
        print(f'    - {k} é {v}')
