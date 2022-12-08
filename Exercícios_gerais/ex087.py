# listaMestre = [[], [], []]
# somaPares = 0
# somaCol3 = 0
# maiorLinha2 = 0
# posicoes = [[x, y] for x in range(0, 3) for y in range(0, 3)]
# cont = 0
# for i in range(0, 9):
#     num = int(input(f'Digite um valor para {posicoes[i]}: '))
#     cont += 1
#     if posicoes[i][1] == 0:
#         listaMestre[0].append(num)
#     elif posicoes[i][1] == 1:
#         listaMestre[1].append(num)
#     elif posicoes[i][1] == 2:
#         listaMestre[2].append(num)
#     if num % 2 == 0:
#         somaPares += num
#     if cont == 3:
#         somaCol3 += num
#         cont = 0
#     if posicoes[i][0] == 1:
#         if maiorLinha2 == 0:
#             maiorLinha2 = num
#         elif num > maiorLinha2:
#             maiorLinha2 = num
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{listaMestre[c][l]:^5}]', end='')
#     print()
# print('-=' * 30)
# print(f'A soma de todos os valores pares digitados para a matriz é: {somaPares}')
# print(f'A soma dos valores da 3° coluna da matriz é: {somaCol3}')
# print(f'O maior valor da linha dois é: {maiorLinha2}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0       # essas declaraões são próprias do python - não existe muito como fazer o código sem elas
for l in range(0, 3):       # Leitura de matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:   # Verificação de elemento par -> para a soma
            spar += matriz[l][c]    # Pega o valor que seria mostrado no print da matriz e coloca-o na soma
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):       # Esse for substitui a necessidade de colocar uma anotação dentro do for de criação da matriz
    scol += matriz[l][2]    # Aqui ele faz a mesma coisa que no print da matriz, mas com o índice de coluna (2) fixo. É possível administrar a esse nível sem fazer um if
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):                   # Mesmo propósito da verificação anterior
    if c == 0 or mai < matriz[1][c]:    # Aqui a verificação de primeira passagem se faz necessário para ser possível o desenvolvimento da lógica sem problemas de leitura
        mai = matriz[1][c]
print(f'O maior número da segunda linha é: {mai}')




















