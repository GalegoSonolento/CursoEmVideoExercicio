# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('\033[31m Digite o seu nome: ')).upper().strip()
silva = nome.find('SILVA')
if silva == -1:
    print('\033[32m Seu nome não tem \'Silva\' em seu nome')
else:
    print('\033[33m Você tem \'Silva\' no nome')
