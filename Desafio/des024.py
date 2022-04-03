# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
nome = str(input('\033[1;31m Digite o nome de sua cidade: ')).upper()
nome.find('SANTO')
if 'SANTO' in nome:
    print('\033[32m Sua cidade começa com \'SANTO\'')
else:
    print('\033[33m Sua cidade não começa com \'SANTO\'')
