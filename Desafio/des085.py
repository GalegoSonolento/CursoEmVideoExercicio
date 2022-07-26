# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# listaMestre = []
# pares = []
# impares = []
# listaMestre.append(pares)
# listaMestre.append(impares)
# Esse tipo de código aqui em cima não é necessário, ele é feito simplesmente com os appends básicos de uma lista.
# Esse trecho de código pode ser reduzido à uma linha:
listaMestre = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        listaMestre[0].append(num)
    else:
        listaMestre[1].append(num)
print('-=' * 30)
listaMestre[0].sort()
listaMestre[1].sort()
print(f'Os valores pares digitados foram: {listaMestre[0]}')
print(f'Os valores ímpares digitados foram: {listaMestre[1]}')
