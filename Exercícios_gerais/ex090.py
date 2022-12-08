# # Exercício Python 090: faça um programa que leia nome e média de um aluno,
# # guardando também a situação num dicionário.
# # No final, mostre o conteúdo da estrutura na tela.
#
# boletim = dict()
# boletim['nome'] = str(input('Nome: '))
# boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
# if boletim['media'] < 7:
#     boletim['situacao'] = str('Aprovado')
# else:
#     boletim['situacao'] = str('Reprovado')
# print('-=' * 30)
# for i, j in boletim.items():
#     print(f' - {i} é igual a {j}')

aluno = dict()
aluno['nome'] = str(input('Nome: '))    # Os dicionários não obrigam o programador a usar append
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))    # Dentro de aspas simples o sistema obrig a usar aspas
                                                                # duplas, para haver diferenciação nas strings.
if aluno['média'] >= 7:
    aluno['situação'] = str('Aprovado')
elif 5 < aluno['média'] < 7:
    aluno['situação'] = str('Recuperação')      # Você chama um dos valores de um dicionário da mesma forma q uma lista,
                                                # utilizando o índice para chamamento
else:
    aluno['situação'] = str('Reprovado')

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

































