# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todos minúsculos
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome
nome = str(input('\033[31m Digite seu nome: ')).strip()
print('\033[31m', nome.upper())
print('\033[1;32', nome.lower())
espacos = nome.count(' ')
print('\033[1;33m', len(nome) - espacos)
nome1 = nome.split()
count = 0
for i in nome1:
    if count == 0:
        print('\033[1;34m', len(i))
        count += 1
