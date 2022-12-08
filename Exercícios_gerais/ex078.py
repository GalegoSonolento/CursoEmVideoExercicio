# # Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# # No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
#
# lista = []
# for i in range(0, 5):
#     lista.append(int(input(f'Digite um valor para a posição {i}: ')))
# maior = menor = lista[0]
# for i in lista:
#     if maior < i:
#         maior = i
#     elif menor > i:
#         menor = i
# print('=-'*20)
# print(f'O maior valor foi {maior} nas posições ', end='')
# for i, j in enumerate(lista):
#     if j == maior:
#         print(f'{i}... ', end=' ')
# print(f'\nO menor valor foi {menor} nas posições ', end=' ')
# for i, j in enumerate(lista):
#     if j == menor:
#         print(f'{i}... ', end=' ')
# 17 linhas

listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end=' ')
print(f'\nO menor valor digitado foi {men} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
#21 linhas
