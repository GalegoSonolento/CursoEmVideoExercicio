# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('Digite o seu nome: ')).upper().strip()
silva = nome.find('SILVA')
if silva == -1:
    print('Seu nome não tem \'Silva\' em seu nome')
else:
    print('Você tem \'Silva\' no nome')
