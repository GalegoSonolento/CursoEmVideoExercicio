# listaMestre = []
# pares = []
# impares = []
# listaMestre.append(pares)
# listaMestre.append(impares)
# for i in range(1, 8):
#     num = int(input(f'Digite o {i}° valor: '))
#     if num % 2 == 0:
#         listaMestre[0].append(num)
#     else:
#         listaMestre[1].append(num)
# print('-=' * 30)
# listaMestre[0].sort()
# listaMestre[1].sort()
# print(f'Os valores pares digitados foram: {listaMestre[0]}')
# print(f'Os valores ímpares digitados foram: {listaMestre[1]}')

# Anotações
# - É possível criar listas internas já na criação da lista abstrata
# -

num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')
