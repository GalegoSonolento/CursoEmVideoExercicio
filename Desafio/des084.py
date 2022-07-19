# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = []
pessoa = []
cont = 0
pesados = []
leves = []
pesoMax = 0
pesoMin = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    guarda = pessoa[:]
    cadastro.append(guarda)
    pessoa.clear()
    cont += 1
    escolha = str(input('Quer continuar? [S/N] '))[0]
    if escolha in 'nN':
        break
for i, j in enumerate(cadastro):
    if i == 0:
        pesoMax = j[1]
        pesoMin = j[1]
        # print(pesoMax, pesoMin)
    if j[1] > pesoMax:
        pesoMax = j[1]
    if j[1] < pesoMin:
        pesoMin = j[1]
for i in cadastro:
    if i[1] == pesoMax:
        pesados.append(i[0])
    elif i[1] == pesoMin:
        leves.append(i[0])
print('-=' * 30)
# print(cadastro)
# print(cont)
print(f'Você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {pesoMax}kg. Peso de {pesados}')
print(f'O menor peso foi de {pesoMin}kg. Peso de {leves}')
