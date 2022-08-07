# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

listaMestre = [[], [], []]
somaPares = 0
somaCol3 = 0
maiorLinha2 = 0
posicoes = [[x, y] for x in range(0, 3) for y in range(0, 3)]
cont = 0
for i in range(0, 9):
    num = int(input(f'Digite um valor para {posicoes[i]}: '))
    cont += 1
    if posicoes[i][1] == 0:
        listaMestre[0].append(num)
    elif posicoes[i][1] == 1:
        listaMestre[1].append(num)
    elif posicoes[i][1] == 2:
        listaMestre[2].append(num)
    if num % 2 == 0:
        somaPares += num
    if cont == 3:
        somaCol3 += num
        cont = 0
    if posicoes[i][0] == 1:
        if maiorLinha2 == 0:
            maiorLinha2 = num
        elif num > maiorLinha2:
            maiorLinha2 = num
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{listaMestre[c][l]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados para a matriz é: {somaPares}')
print(f'A soma dos valores da 3° coluna da matriz é: {somaCol3}')
print(f'O maior valor da linha dois é: {maiorLinha2}')
