# # Refaça o desafio 51, lendo o primeiro termo e a razaõ de uma PA, mostrando os 10 primeiros termos da rpogressão
# # usando a estrutura while
#
# # # Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# # # progressão
# # a1 = int(input('Diga o primeiro termo de uma PA: '))
# # r = int(input('Diga a razão da PA: '))
# # if a1 == r:
# #     for i in range(a1, r * 11, r):
# #         print(i)
# # else:
# #     for j in range(a1, r * 10, r):
# #         print(j)
#
# # an = a1 + (n-1)r
# a1 = int(input('Digite o primeiro temo da PA: '))
# r = int(input('Digite a razão dessa PA: '))
# cont = 1
# termos = 10  # If it where without a prefixed number, I would ask the terms to the user
# while cont <= termos:
#     print('{}° termo: {}'.format(cont, a1 + (cont - 1) * r))
#     cont += 1

print('Gerador de PA')
print('-=='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
