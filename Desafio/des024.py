# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
nome = str(input('Digite o nome de sua cidade: ')).upper()
nome.find('SANTO')
if 'SANTO' in nome:
    print('Sua cidade começa com \'SANTO\'')
else:
    print('Sua cidade não começa com \'SANTO\'')
