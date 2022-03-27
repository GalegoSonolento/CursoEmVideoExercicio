# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todos minúsculos
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
espacos = nome.count(' ')
print(len(nome) - espacos)
nome1 = nome.split()
count = 0
for i in nome1:
    if count == 0:
        print(len(i))
        count += 1
