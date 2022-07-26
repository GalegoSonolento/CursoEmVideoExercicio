# Exercício Python 086: Crie um programa que declare uma matriz de dimensão
# 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

listaMestre = [[], [], []]
posicoes = [[x, y] for x in range(0, 3) for y in range(0, 3)]
# print(posicoes)
for i in range(0, 9):
    num = int(input(f'Digite um valor para {posicoes[i]}: '))
    if posicoes[i][1] == 0:
        listaMestre[0].append(num)
    elif posicoes[i][1] == 1:
        listaMestre[1].append(num)
    elif posicoes[i][1] == 2:
        listaMestre[2].append(num)
# print(listaMestre)
# for i in range(0, 3):
#     if i == 0:
#         print(f'[{listaMestre[0][0]: ^5}]', end='')
#         print(f'[{listaMestre[1][0]: ^5}]', end='')
#         print(f'[{listaMestre[2][0]: ^5}]', end='')
#         print()
#     elif i == 1:
#         print(f'[{listaMestre[0][1]: ^5}]', end='')
#         print(f'[{listaMestre[1][1]: ^5}]', end='')
#         print(f'[{listaMestre[2][1]: ^5}]', end='')
#         print()
#     elif i == 2:
#         print(f'[{listaMestre[0][2]: ^5}]', end='')
#         print(f'[{listaMestre[1][2]: ^5}]', end='')
#         print(f'[{listaMestre[2][2]: ^5}]', end='')
#         print()
# Esse segundo método de resuloção do print formatado realmente facilita na hora de codar (além do código ficar
# um tanto mais curto)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{listaMestre[c][l]:^5}]', end='')
    print()
