# listaMestre = [[], [], []]
# posicoes = [[x, y] for x in range(0, 3) for y in range(0, 3)]
# # print(posicoes)
# for i in range(0, 9):
#     num = int(input(f'Digite um valor para {posicoes[i]}: '))
#     if posicoes[i][1] == 0:
#         listaMestre[0].append(num)
#     elif posicoes[i][1] == 1:
#         listaMestre[1].append(num)
#     elif posicoes[i][1] == 2:
#         listaMestre[2].append(num)
# # print(listaMestre)
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

# Anotações:
# - Ao invés de dar append em todos os números, é interessante já declarar a lista com os valores colodos (depois
# basta substituí-los)
# -

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
