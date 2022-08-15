# Exercício Python 090: faça um programa que leia nome e média de um aluno,
# guardando também a situação num dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] < 7:
    boletim['situacao'] = str('Aprovado')
else:
    boletim['situacao'] = str('Reprovado')
print('-=' * 30)
for i, j in boletim.items():
    print(f' - {i} é igual a {j}')
