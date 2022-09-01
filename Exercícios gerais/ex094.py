# # Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# # guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# # No final, mostre:
# # A) Quantas pessoas foram cadastradas
# # B) A média de idade
# # C) Uma lista com as mulheres
# # D) Uma lista de pessoas com idade acima da média
#
# pess = dict()
# geral = list()
# while True:
#     pess['nome'] = str(input('Nome: '))
#     sexo = str(input('Sexo: [M/F] '))
#     while True:
#         if sexo not in 'MmFf':
#             print('ERRO! Por favor digite apenas M ou F')
#             sexo = str(input('Sexo: [M/F] '))
#         else:
#             break
#     pess['sexo'] = sexo
#     idade = int(input('Idade: '))
#     while True:
#         if idade < 0:
#             print('ERRO! Idade inválida! Tenha 0 anos de idade ou mais')
#             idade = int(input('Idade: '))
#         else:
#             break
#     pess['idade'] = idade
#     geral.append(pess.copy())
#     pess.clear()
#     resp = str(input('Quer continuar? [S/N] ')).strip()[0]
#     while True:
#         if resp not in 'NnSs':
#             print('ERRO! Responda apenas S ou N.')
#             resp = str(input('Quer continuar? [S/N] ')).strip()[0]
#         else:
#             break
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
# mediaIdade = 0
# for i, v in enumerate(geral):
#     mediaIdade += geral[i]['idade']
# mediaIdade = mediaIdade / len(geral)
# print(f'B) A média de idade é de {mediaIdade:.2f} anos.')
# print('C) As mulheres cadastradas foram: ', end='')
# for i in range(0, len(geral)):
#     if geral[i]['sexo'] in 'Ff':
#         print(geral[i]['nome'], end='       ')
# print()
# print('D) Lista de pessoas que estão acima da média:')
# for i in range(0, len(geral)):
#     if geral[i]['idade'] > mediaIdade:
#         print(f'    nome = {geral[i]["nome"]}; sexo = {geral[i]["sexo"]}; idade = {geral[i]["idade"]}', end=' ')
# print()
# print('<<< ENCERRADO >>>')

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') # Validação do sexo (evitar transtornos)
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)    # Até aqui é apenas a entrada de dados
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for i in galera:
    if i['sexo'] in 'fF':
        print(f'{i["nome"]} ', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for i in galera:
    if i['idade'] >= media:
        print('   ')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')





























