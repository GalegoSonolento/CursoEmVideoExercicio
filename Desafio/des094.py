# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pess = dict()
geral = list()
while True:
    pess['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] '))
    while True:
        if sexo not in 'MmFf':
            print('ERRO! Por favor digite apenas M ou F')
            sexo = str(input('Sexo: [M/F] '))
        else:
            break
    pess['sexo'] = sexo
    idade = int(input('Idade: '))
    while True:
        if idade < 0:
            print('ERRO! Idade inválida! Tenha 0 anos de idade ou mais')
            idade = int(input('Idade: '))
        else:
            break
    pess['idade'] = idade
    geral.append(pess.copy())
    pess.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp not in 'NnSs':
        print('ERRO! Responda apenas S ou N.')
    elif resp in 'Nn':
        break
print(geral)
