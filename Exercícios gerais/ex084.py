# cadastro = []
# pessoa = []
# cont = 0
# pesados = []
# leves = []
# pesoMax = 0
# pesoMin = 0
# while True:
#     nome = str(input('Nome: '))
#     peso = float(input('Peso: '))
#     pessoa.append(nome)
#     pessoa.append(peso)
#     guarda = pessoa[:]
#     cadastro.append(guarda)
#     pessoa.clear()
#     cont += 1
#     escolha = str(input('Quer continuar? [S/N] '))[0]
#     if escolha in 'nN':
#         break
# for i, j in enumerate(cadastro):
#     if i == 0:
#         pesoMax = j[1]
#         pesoMin = j[1]
#         # print(pesoMax, pesoMin)
#     if j[1] > pesoMax:
#         pesoMax = j[1]
#     if j[1] < pesoMin:
#         pesoMin = j[1]
# for i in cadastro:
#     if i[1] == pesoMax:
#         pesados.append(i[0])
#     elif i[1] == pesoMin:
#         leves.append(i[0])
# print('-=' * 30)
# # print(cadastro)
# # print(cont)
# print(f'Você cadastrou {cont} pessoas.')
# print(f'O maior peso foi de {pesoMax}kg. Peso de {pesados}')
# print(f'O menor peso foi de {pesoMin}kg. Peso de {leves}')

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
